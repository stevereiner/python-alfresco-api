"""
High-Level Node Utilities for Alfresco API V1.1

This module provides convenient node operations using the V1.1 hierarchical
client architecture. Uses proven working methods like core_client.nodes.get(),
core_client.nodes.create(), core_client.nodes.delete(), etc.

Perfect for MCP servers and applications that need basic node management.
"""

from typing import Optional, Dict, Any, List
from python_alfresco_api.clients.core import AlfrescoCoreClient
from python_alfresco_api.clients.core.nodes.models import CreateNodeRequest
from python_alfresco_api.clients.core.models import NodeType


def get_node_highlevel(
    core_client: AlfrescoCoreClient,
    node_id: str
) -> Any:
    """
    Get node information using V1.1 hierarchical methods.
    
    Uses the proven working pattern: core_client.nodes.get()
    
    Args:
        core_client: The V1.1 hierarchical core client
        node_id: ID of the node to retrieve
        
    Returns:
        Node information from V1.1 API
        
    Examples:
        >>> # Get basic node info
        >>> node = get_node_highlevel(core_client, "doc-123")
    """
    return core_client.nodes.get(node_id=node_id)


def list_children_highlevel(
    core_client: AlfrescoCoreClient,
    parent_id: str = "-my-",
    max_items: int = 100
) -> Any:
    """
    List child nodes using V1.1 hierarchical methods.
    
    Uses the proven working pattern: core_client.nodes.list_children()
    
    Args:
        core_client: The V1.1 hierarchical core client
        parent_id: Parent node ID (default: '-my-' for user's home)
        max_items: Maximum number of items to return
        
    Returns:
        List of child nodes from V1.1 API
        
    Examples:
        >>> # List files in user's home
        >>> children = list_children_highlevel(core_client)
        >>> 
        >>> # List with pagination
        >>> children = list_children_highlevel(
        ...     core_client,
        ...     parent_id="folder-123",
        ...     max_items=50
        ... )
    """
    return core_client.nodes.list_children(
        node_id=parent_id,
        max_items=max_items
    )


def create_folder_simple_highlevel(
    core_client: AlfrescoCoreClient,
    name: str,
    parent_id: str = "-my-",
    properties: Optional[Dict[str, Any]] = None
) -> Any:
    """
    Create a folder using V1.1 hierarchical methods.
    
    Args:
        core_client: The V1.1 hierarchical core client
        name: Folder name
        parent_id: Parent node ID (default: '-my-' for user's home)
        properties: Optional additional properties
        
    Returns:
        Created folder from V1.1 API
        
    Examples:
        >>> # Create simple folder
        >>> folder = create_folder_simple_highlevel(core_client, "My Documents")
    """
    create_request = CreateNodeRequest(
        name=name,
        node_type=NodeType.FOLDER,
        properties=properties,
        auto_rename=True,
        aspects=None,
        versioning_enabled=None,
        major_version=None
    )
    
    return core_client.nodes.create(
        parent_id=parent_id,
        request=create_request
    )


def create_document_simple_highlevel(
    core_client: AlfrescoCoreClient,
    name: str,
    parent_id: str = "-my-",
    properties: Optional[Dict[str, Any]] = None
) -> Any:
    """
    Create a document node using V1.1 hierarchical methods.
    
    Args:
        core_client: The V1.1 hierarchical core client
        name: Document name
        parent_id: Parent node ID (default: '-my-' for user's home)
        properties: Optional additional properties
        
    Returns:
        Created document from V1.1 API
        
    Examples:
        >>> # Create simple document
        >>> doc = create_document_simple_highlevel(core_client, "report.txt")
    """
    create_request = CreateNodeRequest(
        name=name,
        node_type=NodeType.CONTENT,
        properties=properties,
        auto_rename=True,
        aspects=None,
        versioning_enabled=None,
        major_version=None
    )
    
    return core_client.nodes.create(
        parent_id=parent_id,
        request=create_request
    )


def delete_node_highlevel(
    core_client: AlfrescoCoreClient,
    node_id: str,
    permanent: bool = False
) -> bool:
    """
    Delete a node using V1.1 hierarchical methods.
    
    Uses the proven working pattern: core_client.nodes.delete()
    
    Args:
        core_client: The V1.1 hierarchical core client
        node_id: ID of the node to delete
        permanent: Whether to permanently delete (bypass trash)
        
    Returns:
        True if deletion was successful
        
    Examples:
        >>> # Move to trash
        >>> success = delete_node_highlevel(core_client, "doc-123")
        >>> 
        >>> # Permanent deletion
        >>> success = delete_node_highlevel(
        ...     core_client,
        ...     "doc-123",
        ...     permanent=True
        ... )
    """
    core_client.nodes.delete(
        node_id=node_id,
        permanent=permanent
    )
    return True  # If no exception, deletion was successful


def get_node_path_highlevel(
    core_client: AlfrescoCoreClient,
    node_id: str
) -> Optional[str]:
    """
    Get the full path of a node using V1.1 hierarchical methods.
    
    Args:
        core_client: The V1.1 hierarchical core client
        node_id: ID of the node
        
    Returns:
        Full path string or None if not available
        
    Examples:
        >>> # Get node path
        >>> path = get_node_path_highlevel(core_client, "doc-123")
        >>> if path:
        ...     print(path)  # "/Company Home/User Homes/admin/Documents/report.pdf"
    """
    try:
        node_info = core_client.nodes.get(node_id=node_id)
        
        if hasattr(node_info.entry, 'path') and node_info.entry.path:
            path_info = node_info.entry.path
            if hasattr(path_info, 'name'):
                return path_info.name
            elif isinstance(path_info, dict) and 'name' in path_info:
                return path_info['name']
        
        # Fallback: just return the node name
        return node_info.entry.name
    except Exception:
        return None


def bulk_delete_nodes_highlevel(
    core_client: AlfrescoCoreClient,
    node_ids: List[str],
    permanent: bool = False
) -> Dict[str, bool]:
    """
    Delete multiple nodes using V1.1 hierarchical methods.
    
    Args:
        core_client: The V1.1 hierarchical core client
        node_ids: List of node IDs to delete
        permanent: Whether to permanently delete
        
    Returns:
        Dictionary mapping node_id to success status
        
    Examples:
        >>> # Bulk delete to trash
        >>> results = bulk_delete_nodes_highlevel(
        ...     core_client,
        ...     ["doc-123", "doc-456", "folder-789"]
        ... )
        >>> print(results)  # {"doc-123": True, "doc-456": True, "folder-789": False}
    """
    results = {}
    
    for node_id in node_ids:
        try:
            delete_node_highlevel(
                core_client=core_client,
                node_id=node_id,
                permanent=permanent
            )
            results[node_id] = True
        except Exception as e:
            print(f"Failed to delete {node_id}: {e}")
            results[node_id] = False
    
    return results


# V1.1 High-Level Node Operations Summary
def list_node_operations_highlevel() -> List[str]:
    """
    List all available high-level node operations using V1.1 architecture.
    
    Returns:
        List of operation names
    """
    return [
        "get_node_highlevel",
        "list_children_highlevel",
        "create_folder_simple_highlevel",
        "create_document_simple_highlevel",
        "delete_node_highlevel",
        "get_node_path_highlevel",
        "bulk_delete_nodes_highlevel"
    ] 