"""
Delete association between nodes operations for Alfresco nodes.
"""

from typing import Optional, List, Union, TYPE_CHECKING

def delete_association(
    nodes_client,
    node_id: str,
    target_id: str,
    assoc_type: Optional[str] = None
) -> None:
    """
    Delete association between nodes (sync).
    
    Args:
        nodes_client: NodesClient instance
        node_id: Source node ID
        target_id: Target node ID
        assoc_type: Association type to delete
        
    Returns:
        None: Operation result
    """
    # Lazy import of raw operation and UNSET
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import delete_association
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = nodes_client.raw_client
    
    # Execute raw sync operation
    response = delete_association.sync_detailed(
        client=raw_client,
        node_id=node_id,
        target_id=target_id,
        assoc_type=assoc_type if assoc_type is not None else UNSET
    )
    return response.parsed

async def delete_association_async(
    nodes_client,
    node_id: str,
    target_id: str,
    assoc_type: Optional[str] = None
) -> None:
    """
    Delete association between nodes (async).
    
    Args:
        nodes_client: NodesClient instance
        node_id: Source node ID
        target_id: Target node ID
        assoc_type: Association type to delete
        
    Returns:
        None: Operation result
    """
    # Lazy import of raw operation and UNSET
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import delete_association
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = nodes_client.raw_client
    
    # Execute raw async operation
    response = await delete_association.asyncio_detailed(
        client=raw_client,
        node_id=node_id,
        target_id=target_id,
        assoc_type=assoc_type if assoc_type is not None else UNSET
    )
    return response.parsed

def delete_association_detailed(
    nodes_client,
    node_id: str,
    target_id: str,
    assoc_type: Optional[str] = None
):
    """
    Delete association between nodes (detailed sync).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Args:
        nodes_client: NodesClient instance
        node_id: Source node ID
        target_id: Target node ID
        assoc_type: Association type to delete
        
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation and UNSET
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import delete_association
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = nodes_client.raw_client
    
    # Execute raw sync_detailed operation
    return delete_association.sync_detailed(
        client=raw_client,
        node_id=node_id,
        target_id=target_id,
        assoc_type=assoc_type if assoc_type is not None else UNSET
    )

async def delete_association_detailed_async(
    nodes_client,
    node_id: str,
    target_id: str,
    assoc_type: Optional[str] = None
):
    """
    Delete association between nodes (detailed async).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Args:
        nodes_client: NodesClient instance
        node_id: Source node ID
        target_id: Target node ID
        assoc_type: Association type to delete
        
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation and UNSET
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import delete_association
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = nodes_client.raw_client
    
    # Execute raw asyncio_detailed operation
    return await delete_association.asyncio_detailed(
        client=raw_client,
        node_id=node_id,
        target_id=target_id,
        assoc_type=assoc_type if assoc_type is not None else UNSET
    )
