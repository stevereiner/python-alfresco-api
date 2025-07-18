"""
Node utility functions for the Alfresco API.

This module provides convenient utility functions for common node operations
that MCP servers and other applications need, using the v1.1 hierarchical
client methods consistently (no raw httpx mixing).
"""

from typing import Optional, Dict, Any, List, Union, BinaryIO
import os
import tempfile
from datetime import datetime
from pathlib import Path

from python_alfresco_api.clients.core import AlfrescoCoreClient


def browse_repository(
    core_client: AlfrescoCoreClient,
    parent_id: str = "-my-",
    max_items: int = 100,
    skip_count: int = 0,
    include_properties: bool = True
) -> Any:
    """
    Browse repository contents (list folders/files).
    
    Args:
        core_client: The v1.1 hierarchical core client
        parent_id: Parent node ID (default: '-my-' for user's home)
        max_items: Maximum number of items to return
        skip_count: Number of items to skip for pagination
        include_properties: Whether to include node properties
        
    Returns:
        List of child nodes from the Alfresco API
    """
    # Build include list
    include_list = []
    if include_properties:
        include_list.extend(["properties", "path", "allowableOperations"])
    
    # Use the v1.1 nodes client consistently
    return core_client.nodes.list_children(
        node_id=parent_id,
        max_items=max_items,
        skip_count=skip_count
    )


def get_node_properties(
    core_client: AlfrescoCoreClient,
    node_id: str,
    include_path: bool = True,
    include_permissions: bool = False
) -> Any:
    """
    Get node properties and metadata.
    
    Args:
        core_client: The v1.1 hierarchical core client
        node_id: The node ID to get properties for
        include_path: Whether to include path information
        include_permissions: Whether to include permission information
        
    Returns:
        Node details from the Alfresco API
    """
    # Build include list
    include_list = ["properties"]
    
    if include_path:
        include_list.append("path")
    
    if include_permissions:
        include_list.append("permissions")
    
    # Use the v1.1 nodes client consistently
    return core_client.nodes.get_node(
        node_id=node_id,
        include=include_list
    )


def create_folder(
    core_client: AlfrescoCoreClient,
    name: str,
    parent_id: str = "-my-",
    title: Optional[str] = None,
    description: Optional[str] = None,
    properties: Optional[Dict[str, Any]] = None
) -> Any:
    """
    Create a new folder.
    
    Args:
        core_client: The v1.1 hierarchical core client
        name: Folder name
        parent_id: Parent node ID (default: '-my-' for user's home)
        title: Optional folder title
        description: Optional folder description
        properties: Optional additional properties
        
    Returns:
        Created folder details from the Alfresco API
    """
    # Build properties dict
    folder_props = {}
    if title:
        folder_props["cm:title"] = title
    if description:
        folder_props["cm:description"] = description
    if properties:
        folder_props.update(properties)
    
    # Use the v1.1 nodes client's create_folder_node method directly
    return core_client.nodes.create_folder_node(
        name=name,
        parent_id=parent_id,
        properties=folder_props if folder_props else None
    )


def update_node_properties(
    core_client: AlfrescoCoreClient,
    node_id: str,
    properties: Dict[str, Any],
    name: Optional[str] = None
) -> Any:
    """
    Update node properties and metadata.
    
    Args:
        core_client: The v1.1 hierarchical core client
        node_id: The node ID to update
        properties: Properties to update
        name: Optional new name for the node
        
    Returns:
        Updated node details from the Alfresco API
    """
    # Import the update request model
    from ..clients.core.nodes.models import UpdateNodeRequest
    
    # Create update request
    update_request = UpdateNodeRequest(
        properties=properties,
        name=name
    )
    
    # Use the v1.1 nodes client consistently
    return core_client.nodes.update_node(
        node_id=node_id,
        request=update_request
    )


def delete_node(
    core_client: AlfrescoCoreClient,
    node_id: str,
    permanent: bool = False
) -> Any:
    """
    Delete a node (move to trash or permanent deletion).
    
    Args:
        core_client: The v1.1 hierarchical core client
        node_id: The node ID to delete
        permanent: Whether to permanently delete (default: move to trash)
        
    Returns:
        Delete operation result from the Alfresco API
    """
    # Use the v1.1 nodes client consistently
    result = core_client.nodes.delete(
        node_id=node_id,
        permanent=permanent
    )
    
    # Return success indicator if result is None/empty (successful deletion)
    if result is None:
        return {"deleted": True, "node_id": node_id, "permanent": permanent}
    
    return result


def upload_document(
    core_client: AlfrescoCoreClient,
    file_path: Union[str, Path],
    parent_id: str = "-my-",
    name: Optional[str] = None,
    title: Optional[str] = None,
    description: Optional[str] = None,
    properties: Optional[Dict[str, Any]] = None,
    major_version: bool = False
) -> Any:
    """
    Upload a document to Alfresco.
    
    Args:
        core_client: The v1.1 hierarchical core client
        file_path: Path to the file to upload
        parent_id: Parent node ID (default: '-my-' for user's home)
        name: Optional custom name (default: use filename)
        title: Optional document title
        description: Optional document description
        properties: Optional additional properties
        major_version: Whether to create as major version
        
    Returns:
        Upload result from the Alfresco API
    """
    file_path = Path(file_path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Determine filename
    filename = name or file_path.name
    
    # Build properties dict
    doc_props = {}
    if title:
        doc_props["cm:title"] = title
    if description:
        doc_props["cm:description"] = description
    if properties:
        doc_props.update(properties)
    
    # Use content_utils for upload implementation
    from . import content_utils
    
    return content_utils.upload_file(
        core_client=core_client,
        file_path=file_path,
        parent_id=parent_id,
        filename=filename,
        description=description,
        properties=doc_props if doc_props else None
    )


def download_document(
    core_client: AlfrescoCoreClient,
    node_id: str,
    output_path: Optional[Union[str, Path]] = None,
    attachment: bool = False
) -> Any:
    """
    Download a document from Alfresco.
    
    Args:
        core_client: The v1.1 hierarchical core client
        node_id: The node ID to download
        output_path: Optional path to save the file (if None, returns content)
        attachment: Whether to download as attachment
        
    Returns:
        Download response from the Alfresco API
    """
    # Use content_utils for download implementation
    from . import content_utils
    
    return content_utils.download_file(
        core_client=core_client,
        node_id=node_id,
        output_path=output_path,
        as_attachment=attachment
    )


def checkout_document(
    core_client: AlfrescoCoreClient,
    node_id: str
) -> Any:
    """
    Checkout a document for editing (lock it).
    
    Args:
        core_client: The v1.1 hierarchical core client
        node_id: The node ID to checkout
        
    Returns:
        Checkout result from the Alfresco API
    """
    # Use the v1.1 versions client consistently
    return core_client.versions.checkout(node_id=node_id)


def checkin_document(
    core_client: AlfrescoCoreClient,
    node_id: str,
    content: Optional[Union[str, bytes, Path]] = None,
    comment: Optional[str] = None,
    major_version: bool = False
) -> Any:
    """
    Checkin a document (create new version and unlock).
    
    Args:
        core_client: The v1.1 hierarchical core client
        node_id: The node ID to checkin
        content: Optional new content (file path, string, or bytes)
        comment: Optional version comment
        major_version: Whether to create major version
        
    Returns:
        Checkin result from the Alfresco API
    """
    # If new content is provided, update it first
    if content:
        if isinstance(content, Path) or (isinstance(content, str) and os.path.exists(content)):
            # File path - use content client to update
            core_client.content.update_content(
                node_id=node_id,
                file_path=content,
                major_version=major_version,
                comment=comment
            )
        else:
            # String or bytes content - need to create temp file
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                if isinstance(content, str):
                    temp_file.write(content.encode('utf-8'))
                else:
                    temp_file.write(content)
                temp_file.flush()
                
                # Update with temp file
                core_client.content.update_content(
                    node_id=node_id,
                    file_path=temp_file.name,
                    major_version=major_version,
                    comment=comment
                )
                
                # Clean up temp file
                os.unlink(temp_file.name)
    
    # Use the v1.1 versions client consistently
    return core_client.versions.checkin(
        node_id=node_id,
        comment=comment,
        major_version=major_version
    )


def cancel_checkout(
    core_client: AlfrescoCoreClient,
    node_id: str
) -> Any:
    """
    Cancel checkout of a document (unlock without creating version).
    
    Args:
        core_client: The v1.1 hierarchical core client
        node_id: The node ID to cancel checkout for
        
    Returns:
        Cancel checkout result from the Alfresco API
    """
    # Use the v1.1 versions client consistently
    return core_client.versions.cancel_checkout(node_id=node_id)


def find_nodes(
    core_client: AlfrescoCoreClient,
    search_term: str,
    max_items: int = 100,
    skip_count: int = 0,
    node_type: Optional[str] = None,
    parent_id: Optional[str] = None
) -> Any:
    """
    Find nodes by search term (simple node search).
    
    Args:
        core_client: The v1.1 hierarchical core client
        search_term: Term to search for
        max_items: Maximum number of results
        skip_count: Number of results to skip
        node_type: Optional node type filter
        parent_id: Optional parent node to search within
        
    Returns:
        Search results from the Alfresco API
    """
    # Use the v1.1 search client convenience method directly
    from ..client_factory import ClientFactory
    from ..raw_clients.alfresco_search_client.search_client.models import SearchRequest, RequestQuery, RequestQueryLanguage, RequestPagination
    from ..raw_clients.alfresco_search_client.search_client.types import UNSET
    
    # Get search client from the same factory
    factory = core_client._client_factory
    search_client = factory.create_search_client()
    
    # Build query with type filter
    query_parts = [f'TEXT:"{search_term}"']
    
    if node_type:
        query_parts.append(f'TYPE:"{node_type}"')
    
    if parent_id:
        query_parts.append(f'PARENT:"{parent_id}"')
    
    query = ' AND '.join(query_parts)
    
    # Create the search request
    query_obj = RequestQuery(
        query=query,
        language=RequestQueryLanguage.AFTS
    )
    
    pagination = RequestPagination(
        max_items=max_items,
        skip_count=skip_count
    )
    
    search_request = SearchRequest(
        query=query_obj,
        paging=pagination,
        sort=UNSET,
        filter_queries=UNSET,
        include=UNSET,
        scope=UNSET
    )
    
    # Use the search client convenience method
    return search_client.search_content(body=search_request)


# Common node type constants for MCP tools
NODE_TYPES = {
    'folder': 'cm:folder',
    'document': 'cm:content',
    'link': 'app:filelink',
    'site': 'st:site'
}

# Common property keys for MCP tools
PROPERTY_KEYS = {
    'title': 'cm:title',
    'description': 'cm:description',
    'author': 'cm:author',
    'creator': 'cm:creator',
    'created': 'cm:created',
    'modified': 'cm:modified',
    'modifier': 'cm:modifier',
    'size': 'cm:content.size',
    'mimetype': 'cm:content.mimetype'
}


# Export all functions
__all__ = [
    'browse_repository',
    'get_node_properties',
    'create_folder',
    'update_node_properties',
    'delete_node',
    'upload_document',
    'download_document',
    'checkout_document',
    'checkin_document',
    'cancel_checkout',
    'find_nodes',
    'NODE_TYPES',
    'PROPERTY_KEYS'
] 