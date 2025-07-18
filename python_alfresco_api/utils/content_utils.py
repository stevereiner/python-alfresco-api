"""
Content utility functions for the Alfresco API.

This module provides convenient utility functions for content operations
that MCP servers and other applications need, using authenticated HTTP client
patterns that won't be overwritten by codegen.
"""

import os
import tempfile
import mimetypes
from typing import Optional, Dict, Any, Union, BinaryIO
from pathlib import Path
import base64

from python_alfresco_api.clients.core import AlfrescoCoreClient


def upload_file(
    core_client: AlfrescoCoreClient,
    file_path: Union[str, Path],
    parent_id: str = "-my-",
    filename: Optional[str] = None,
    description: Optional[str] = None,
    properties: Optional[Dict[str, Any]] = None,
    auto_rename: bool = True
) -> Any:
    """
    Upload a file to Alfresco repository using authenticated HTTP client.
    
    Args:
        core_client: The v1.1 hierarchical core client
        file_path: Path to the file to upload
        parent_id: Parent node ID (default: '-my-' for user's home)
        filename: Optional custom filename (default: use file's name)
        description: Optional file description
        properties: Optional additional properties
        auto_rename: Whether to auto-rename if name conflicts exist
        
    Returns:
        Upload response from Alfresco API
        
    Examples:
        >>> # Simple upload
        >>> result = upload_file(core_client, "report.pdf")
        >>> 
        >>> # Upload with properties
        >>> result = upload_file(
        ...     core_client, 
        ...     "data.xlsx",
        ...     parent_id="folder-123",
        ...     description="Monthly report data",
        ...     properties={"cm:title": "Q4 Data"}
        ... )
    """
    # Convert to Path object
    file_path_obj = Path(file_path)
    
    if not file_path_obj.exists():
        raise FileNotFoundError(f"File does not exist: {file_path}")
    
    if not file_path_obj.is_file():
        raise ValueError(f"Path is not a file: {file_path}")
    
    # Use filename or derive from path
    upload_filename = filename or file_path_obj.name
    
    # Read file content
    with open(file_path_obj, 'rb') as f:
        content = f.read()
    
    # Get authenticated HTTP client
    http_client = core_client._get_raw_client().get_httpx_client()
    
    # Prepare multipart data (proven working approach from mcp-tools)
    files = {
        'filedata': (upload_filename, content, _guess_mime_type(upload_filename)),
        'name': (None, upload_filename),
        'nodeType': (None, 'cm:content'),
        'relativePath': (None, '')
    }
    
    # Add optional fields
    if description:
        files['description'] = (None, description)
    
    if auto_rename:
        files['autoRename'] = (None, 'true')
    
    # Add properties
    if properties:
        for key, value in properties.items():
            files[key] = (None, str(value))
    
    # Build URL for upload
    base_url = core_client._client_factory.base_url
    url = f"{base_url}/alfresco/api/-default-/public/alfresco/versions/1/nodes/{parent_id}/children"
    
    # Upload file
    response = http_client.post(url, files=files)
    response.raise_for_status()
    
    return response.json()


def download_file(
    core_client: AlfrescoCoreClient,
    node_id: str,
    output_path: Optional[Union[str, Path]] = None,
    as_attachment: bool = False
) -> Union[bytes, str]:
    """
    Download a file from Alfresco repository.
    
    Args:
        core_client: The v1.1 hierarchical core client
        node_id: ID of the file node to download
        output_path: Optional path to save file (if None, return content)
        as_attachment: Whether to download as attachment
        
    Returns:
        File content as bytes if output_path is None, otherwise path where saved
        
    Examples:
        >>> # Download to memory
        >>> content = download_file(core_client, "file-123")
        >>> 
        >>> # Download to file
        >>> path = download_file(core_client, "file-123", "local_file.pdf")
    """
    # Get authenticated HTTP client
    http_client = core_client._get_raw_client().get_httpx_client()
    
    # Build URL for download
    base_url = core_client._client_factory.base_url
    url = f"{base_url}/alfresco/api/-default-/public/alfresco/versions/1/nodes/{node_id}/content"
    
    # Add attachment parameter if needed
    params = {}
    if as_attachment:
        params['attachment'] = 'true'
    
    # Download file
    response = http_client.get(url, params=params)
    response.raise_for_status()
    
    content = response.content
    
    if output_path:
        # Save to file
        output_path_obj = Path(output_path)
        output_path_obj.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path_obj, 'wb') as f:
            f.write(content)
        
        return str(output_path_obj)
    else:
        # Return content
        return content


def update_content(
    core_client: AlfrescoCoreClient,
    node_id: str,
    file_path: Union[str, Path, bytes],
    major_version: bool = False,
    comment: Optional[str] = None,
    filename: Optional[str] = None
) -> Any:
    """
    Update content of an existing file.
    
    Args:
        core_client: The v1.1 hierarchical core client
        node_id: ID of the file node to update
        file_path: Path to new content, or bytes content
        major_version: Whether to create major version
        comment: Optional version comment
        filename: Optional filename (for bytes content)
        
    Returns:
        Update response from Alfresco API
        
    Examples:
        >>> # Update from file
        >>> result = update_content(core_client, "file-123", "updated.pdf")
        >>> 
        >>> # Update with major version
        >>> result = update_content(
        ...     core_client, 
        ...     "file-123", 
        ...     "final.pdf",
        ...     major_version=True,
        ...     comment="Final version"
        ... )
    """
    # Handle different content types
    if isinstance(file_path, bytes):
        # Direct bytes content
        content = file_path
        if not filename:
            filename = f"updated_content_{node_id}"
    else:
        # File path (str or Path)
        file_path_obj = Path(str(file_path))
        if not file_path_obj.exists():
            raise FileNotFoundError(f"File does not exist: {file_path}")
        
        with open(file_path_obj, 'rb') as f:
            content = f.read()
        
        filename = filename or file_path_obj.name
    
    # Get authenticated HTTP client
    http_client = core_client._get_raw_client().get_httpx_client()
    
    # Build URL for content update
    base_url = core_client._client_factory.base_url
    url = f"{base_url}/alfresco/api/-default-/public/alfresco/versions/1/nodes/{node_id}/content"
    
    # Prepare parameters
    params = {}
    if major_version:
        params['majorVersion'] = 'true'
    if comment:
        params['comment'] = comment
    
    # Prepare content with proper MIME type
    mime_type = _guess_mime_type(filename)
    
    # Update content using PUT
    response = http_client.put(
        url, 
        content=content,
        params=params,
        headers={'Content-Type': mime_type}
    )
    response.raise_for_status()
    
    return response.json()


def _guess_mime_type(filename: str) -> str:
    """Guess MIME type from filename."""
    mime_type, _ = mimetypes.guess_type(filename)
    return mime_type or 'application/octet-stream'


def get_content_info(
    core_client: AlfrescoCoreClient,
    node_id: str
) -> Dict[str, Any]:
    """
    Get content information for a file node.
    
    Args:
        core_client: The v1.1 hierarchical core client
        node_id: ID of the file node
        
    Returns:
        Content information including size, MIME type, etc.
    """
    # Use the high-level API to get node info
    node_response = core_client.nodes.get(node_id, include=["properties"])
    
    if not hasattr(node_response, 'entry'):
        raise ValueError(f"No node found with ID: {node_id}")
    
    entry = node_response.entry
    content_info = getattr(entry, 'content', None)
    
    if not content_info:
        raise ValueError(f"Node {node_id} has no content")
    
    return {
        'mime_type': getattr(content_info, 'mime_type', 'unknown'),
        'size_in_bytes': getattr(content_info, 'size_in_bytes', 0),
        'encoding': getattr(content_info, 'encoding', 'unknown')
    }


# Export all functions
__all__ = [
    'upload_file',
    'download_file', 
    'update_content',
    'get_content_info'
] 