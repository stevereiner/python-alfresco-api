"""
Delete node operations for Alfresco nodes.
Simplified function-based approach - no classes, just clean functions.
"""

from typing import Optional, List, Union


def delete_node(client, node_id: str, permanent: bool = False) -> None:
    """
    Delete a node (synchronous).
    
    Perfect for scripts, MCP servers, and command-line tools.
    
    Args:
        client: The nodes client instance
        node_id (str): Node identifier to delete
        permanent (bool): If True, permanently delete; if False, move to trash
        
    Returns:
        None
        
    Examples:
        ```python
        # Move node to trash in Alfresco (recoverable)
        client.nodes.delete("abc123-def456")
        
        # Permanently delete node
        client.nodes.delete("abc123-def456", permanent=True)
        ```
        
    Raises:
        NodeNotFoundError: Node with given ID doesn't exist
        PermissionError: User lacks permission to delete node
        ConflictError: Node cannot be deleted (has children, locked, etc.)
        
    Note:
        This method calls the raw sync client directly for optimal performance.
        For async operations, use delete_node_async().
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import delete_node
    
    # Get raw client
    raw_client = client.raw_client
    
    # Execute raw sync operation - calls sync httpx directly
    delete_node.sync_detailed(
        client=raw_client,
        node_id=node_id,
        permanent=permanent
    )


async def delete_node_async(client, node_id: str, permanent: bool = False) -> None:
    """
    Delete a node (asynchronous).
    
    Args:
        client: The nodes client instance
        node_id: Node identifier
        permanent: If True, permanently delete; if False, move to trash
        
    Examples:
        ```python
        # Move to trash (recoverable)
        await client.nodes.delete_async("abc123-def456")
        
        # Permanent deletion
        await client.nodes.delete_async("abc123-def456", permanent=True)
        ```
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import delete_node
    
    # Get raw client  
    raw_client = client.raw_client
    
    # Execute raw operation (delete_node only has asyncio_detailed)
    await delete_node.asyncio_detailed(
        client=raw_client,
        node_id=node_id,
        permanent=permanent
    )


def delete_node_detailed(client, node_id: str, permanent: bool = False):
    """
    Delete node operation (detailed sync).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import delete_node
    
    # Get raw client
    raw_client = client.raw_client
    
    # Execute raw sync_detailed operation
    return delete_node.sync_detailed(
        client=raw_client,
        node_id=node_id,
        permanent=permanent
    )


async def delete_node_detailed_async(client, node_id: str, permanent: bool = False):
    """
    Delete node operation (detailed async).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import delete_node
    
    # Get raw client
    raw_client = client.raw_client
    
    # Execute raw asyncio_detailed operation
    return await delete_node.asyncio_detailed(
        client=raw_client,
        node_id=node_id,
        permanent=permanent
    )


    # ==================== COPY DETAILED METHODS - Added for 4-Pattern ====================
