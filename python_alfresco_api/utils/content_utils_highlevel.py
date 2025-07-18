"""
High-Level Content Utilities for Alfresco API V1.1

This module provides convenient content operations using the V1.1 hierarchical
client architecture. Uses the actual working method signatures from the node tests.

Perfect for MCP servers and applications that want clean, Pythonic interfaces.
"""

import os
import io
import tempfile
import mimetypes
from typing import Optional, Dict, Any, Union, BinaryIO, List
from pathlib import Path
from datetime import datetime

from python_alfresco_api.clients.core import AlfrescoCoreClient
from python_alfresco_api.clients.core.nodes.models import CreateNodeRequest
from python_alfresco_api.clients.core.models import NodeType


def create_folder_highlevel(
    core_client: AlfrescoCoreClient,
    name: str,
    parent_id: str = "-my-",
    title: Optional[str] = None,
    description: Optional[str] = None,
    properties: Optional[Dict[str, Any]] = None
) -> Any:
    """
    Create a folder using V1.1 hierarchical methods.
    
    Args:
        core_client: The V1.1 hierarchical core client
        name: Folder name
        parent_id: Parent node ID (default: '-my-' for user's home)
        title: Optional folder title
        description: Optional folder description
        properties: Optional additional properties
        
    Returns:
        Node creation response from V1.1 API
        
    Examples:
        >>> # Create folder using V1.1 methods
        >>> folder = create_folder_highlevel(core_client, "My Documents")
        >>> 
        >>> # Create with properties
        >>> folder = create_folder_highlevel(
        ...     core_client, 
        ...     "Projects",
        ...     title="Project Documents",
        ...     description="All project files"
        ... )
    """
    # Build properties dict
    node_properties = properties or {}
    if title:
        node_properties["cm:title"] = title
    if description:
        node_properties["cm:description"] = description
    
    # Create folder using V1.1 hierarchical methods
    create_request = CreateNodeRequest(
        name=name,
        node_type=NodeType.FOLDER,
        properties=node_properties,
        auto_rename=True,
        aspects=None,
        versioning_enabled=None,
        major_version=None
    )
    
    return core_client.nodes.create(
        parent_id=parent_id,
        request=create_request
    )


def create_document_highlevel(
    core_client: AlfrescoCoreClient,
    name: str,
    parent_id: str = "-my-",
    title: Optional[str] = None,
    description: Optional[str] = None,
    properties: Optional[Dict[str, Any]] = None
) -> Any:
    """
    Create a document node (without content) using V1.1 hierarchical methods.
    
    Args:
        core_client: The V1.1 hierarchical core client
        name: Document name
        parent_id: Parent node ID (default: '-my-' for user's home)
        title: Optional document title
        description: Optional document description
        properties: Optional additional properties
        
    Returns:
        Node creation response from V1.1 API
        
    Examples:
        >>> # Create document using V1.1 methods
        >>> doc = create_document_highlevel(core_client, "report.txt")
    """
    # Build properties dict
    node_properties = properties or {}
    if title:
        node_properties["cm:title"] = title
    if description:
        node_properties["cm:description"] = description
    
    # Create document using V1.1 hierarchical methods
    create_request = CreateNodeRequest(
        name=name,
        node_type=NodeType.CONTENT,
        properties=node_properties,
        auto_rename=True,
        aspects=None,
        versioning_enabled=None,
        major_version=None
    )
    
    return core_client.nodes.create(
        parent_id=parent_id,
        request=create_request
    )


def update_content_from_file_highlevel(
    core_client: AlfrescoCoreClient,
    node_id: str,
    file_path: Union[str, Path],
    filename: Optional[str] = None,
    include: Optional[List[str]] = None
) -> Any:
    """
    Update node content from a file using V1.1 hierarchical methods.
    
    Uses the proven working pattern: core_client.nodes.update_content()
    
    Args:
        core_client: The V1.1 hierarchical core client
        node_id: ID of the node to update
        file_path: Path to the file content
        filename: Optional new filename
        include: Optional include list for response
        
    Returns:
        Content update response from V1.1 API
        
    Examples:
        >>> # Update content using working V1.1 pattern
        >>> result = update_content_from_file_highlevel(
        ...     core_client, 
        ...     "doc-123",
        ...     "updated_report.pdf",
        ...     filename="report_v2.pdf",
        ...     include=["properties"]
        ... )
    """
    # Convert to Path object
    file_path_obj = Path(file_path)
    
    if not file_path_obj.exists():
        raise FileNotFoundError(f"File does not exist: {file_path}")
    
    if not file_path_obj.is_file():
        raise ValueError(f"Path is not a file: {file_path}")
    
    # Use filename or derive from path
    update_filename = filename or file_path_obj.name
    
    # Read file and create BytesIO stream (proven working pattern)
    with open(file_path_obj, 'rb') as f:
        content = f.read()
    
    content_stream = io.BytesIO(content)
    
    # Use the proven working V1.1 pattern
    return core_client.nodes.update_content(
        node_id=node_id,
        content=content_stream,
        filename=update_filename,
        include=include
    )


def update_content_from_string_highlevel(
    core_client: AlfrescoCoreClient,
    node_id: str,
    content_text: str,
    filename: Optional[str] = None,
    encoding: str = 'utf-8',
    include: Optional[List[str]] = None
) -> Any:
    """
    Update node content from a string using V1.1 hierarchical methods.
    
    Args:
        core_client: The V1.1 hierarchical core client
        node_id: ID of the node to update
        content_text: Text content to upload
        filename: Optional filename
        encoding: Text encoding (default: utf-8)
        include: Optional include list for response
        
    Returns:
        Content update response from V1.1 API
        
    Examples:
        >>> # Update with text content
        >>> content = "This is my document content"
        >>> result = update_content_from_string_highlevel(
        ...     core_client,
        ...     "doc-123", 
        ...     content,
        ...     filename="document.txt"
        ... )
    """
    # Convert string to bytes and create stream
    content_bytes = content_text.encode(encoding)
    content_stream = io.BytesIO(content_bytes)
    
    # Use the proven working V1.1 pattern
    return core_client.nodes.update_content(
        node_id=node_id,
        content=content_stream,
        filename=filename,
        include=include
    )


def update_content_from_stream_highlevel(
    core_client: AlfrescoCoreClient,
    node_id: str,
    content_stream: BinaryIO,
    filename: Optional[str] = None,
    include: Optional[List[str]] = None
) -> Any:
    """
    Update node content from a stream using V1.1 hierarchical methods.
    
    Direct wrapper around the proven working pattern.
    
    Args:
        core_client: The V1.1 hierarchical core client
        node_id: ID of the node to update
        content_stream: Binary stream containing the content
        filename: Optional filename
        include: Optional include list for response
        
    Returns:
        Content update response from V1.1 API
        
    Examples:
        >>> # Update from stream
        >>> content = io.BytesIO(b"Binary content")
        >>> result = update_content_from_stream_highlevel(
        ...     core_client,
        ...     "doc-123",
        ...     content,
        ...     filename="data.bin"
        ... )
    """
    # Use the proven working V1.1 pattern directly
    return core_client.nodes.update_content(
        node_id=node_id,
        content=content_stream,
        filename=filename,
        include=include
    )


def create_and_upload_file_highlevel(
    core_client: AlfrescoCoreClient,
    file_path: Union[str, Path],
    parent_id: str = "-my-",
    filename: Optional[str] = None,
    title: Optional[str] = None,
    description: Optional[str] = None,
    properties: Optional[Dict[str, Any]] = None,
    include: Optional[List[str]] = None
) -> Any:
    """
    Create a new document and upload content in one operation.
    
    Combines create + update_content using V1.1 hierarchical methods.
    
    Args:
        core_client: The V1.1 hierarchical core client
        file_path: Path to the file to upload
        parent_id: Parent node ID (default: '-my-' for user's home)
        filename: Optional custom filename
        title: Optional document title
        description: Optional document description
        properties: Optional additional properties
        include: Optional include list for response
        
    Returns:
        Final document with content
        
    Examples:
        >>> # Create and upload in one step
        >>> result = create_and_upload_file_highlevel(
        ...     core_client,
        ...     "report.pdf",
        ...     title="Annual Report",
        ...     description="Company annual report"
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
    
    # Step 1: Create the document node
    created_doc = create_document_highlevel(
        core_client=core_client,
        name=upload_filename,
        parent_id=parent_id,
        title=title,
        description=description,
        properties=properties
    )
    
    # Step 2: Upload content to the created node
    updated_doc = update_content_from_file_highlevel(
        core_client=core_client,
        node_id=created_doc.entry.id,
        file_path=file_path_obj,
        filename=upload_filename,
        include=include
    )
    
    return updated_doc


def get_node_info_highlevel(
    core_client: AlfrescoCoreClient,
    node_id: str,
    include: Optional[List[str]] = None
) -> Any:
    """
    Get node information using V1.1 hierarchical methods.
    
    Args:
        core_client: The V1.1 hierarchical core client
        node_id: ID of the node
        include: Optional include list for additional data
        
    Returns:
        Node information from V1.1 API
        
    Examples:
        >>> # Get node info
        >>> info = get_node_info_highlevel(
        ...     core_client, 
        ...     "doc-123",
        ...     include=["properties", "path"]
        ... )
    """
    return core_client.nodes.get(
        node_id=node_id,
        include=include
    )


# V1.1 High-Level Content Operations Summary
def list_content_operations_highlevel() -> List[str]:
    """
    List all available high-level content operations using V1.1 architecture.
    
    Returns:
        List of operation names
    """
    return [
        "create_folder_highlevel",
        "create_document_highlevel",
        "update_content_from_file_highlevel",
        "update_content_from_string_highlevel", 
        "update_content_from_stream_highlevel",
        "create_and_upload_file_highlevel",
        "get_node_info_highlevel"
    ] 