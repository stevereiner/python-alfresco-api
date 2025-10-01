"""
Unlock a node operations for Alfresco nodes.
Clean function-based approach with 4 patterns: sync, async, detailed_sync, detailed_async.
"""

from typing import Optional, List, Union
from .models import NodeResponse, NodeListResponse


def unlock_node(
    client,
    node_id: str,
    include: Optional[List[Union[str, str]]] = None
) -> NodeResponse:
    """
    Unlock a node (synchronous).
    
    Perfect for scripts, MCP servers, and command-line tools.
    
    Args:
        client: NodesClient instance
        node_id (str): Node identifier to unlock
        include (Optional[List[Union[str, str]]]): Additional data to include in response
        
    Returns:
        NodeResponse: Unlocked node information
        
    Examples:
        ```python
        # Unlock a locked node
        unlocked = client.nodes.unlock(node_id="abc123-def456")
        
        # Unlock with additional properties
        unlocked = client.nodes.unlock(
            node_id="abc123-def456",
            include=["properties", "aspectNames"]
        )
        ```
        
    Raises:
        NodeNotFoundError: Node with given ID doesn't exist
        PermissionError: User lacks permission to unlock node
        ConflictError: Node is not locked or locked by another user
        ValidationError: Invalid request parameters
        
    Note:
        This method calls the raw sync client directly for optimal performance.
        For async operations, use unlock_node_async().
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import unlock_node
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client.raw_client
    
    # Convert include options
    include_params = UNSET
    if include:
        include_params = include
    
    # Execute raw sync operation
    result = unlock_node.sync(
        client=raw_client,
        node_id=node_id,
        include=include_params
    )
    
    # Validate and return rich model
    if result is None:
        raise ValueError(f"Failed to unlock node {node_id}")
    return NodeResponse.model_validate(result.to_dict())


async def unlock_node_async(
    client,
    node_id: str,
    include: Optional[List[Union[str, str]]] = None
) -> NodeResponse:
    """
    Unlock a node (asynchronous).
    
    Args:
        client: NodesClient instance
        node_id: Node identifier to unlock
        include: Additional data to include in response
        
    Returns:
        NodeResponse: Unlocked node information
        
    Examples:
        ```python
        # Unlock a locked node (async)
        unlocked = await client.nodes.unlock_async(node_id="abc123-def456")
        ```
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import unlock_node
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client.raw_client
    
    # Convert include options
    include_params = UNSET
    if include:
        include_params = include
    
    # Execute raw async operation
    result = await unlock_node.asyncio(
        client=raw_client,
        node_id=node_id,
        include=include_params
    )
    
    # Validate and return rich model
    if result is None:
        raise ValueError(f"Failed to unlock node {node_id}")
    return NodeResponse.model_validate(result.to_dict())


def unlock_node_detailed(
    client,
    node_id: str,
    include: Optional[List[Union[str, str]]] = None
):
    """
    Unlock a node (detailed sync).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Args:
        client: NodesClient instance
        node_id: Node identifier to unlock
        include: Additional data to include in response
        
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import unlock_node
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client.raw_client
    
    # Convert include options
    include_params = UNSET
    if include:
        include_params = include
    
    # Execute raw sync_detailed operation
    return unlock_node.sync_detailed(
        client=raw_client,
        node_id=node_id,
        include=include_params
    )


async def unlock_node_detailed_async(
    client,
    node_id: str,
    include: Optional[List[Union[str, str]]] = None
):
    """
    Unlock a node (detailed async).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Args:
        client: NodesClient instance
        node_id: Node identifier to unlock
        include: Additional data to include in response
        
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import unlock_node
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client.raw_client
    
    # Convert include options
    include_params = UNSET
    if include:
        include_params = include
    
    # Execute raw asyncio_detailed operation
    return await unlock_node.asyncio_detailed(
        client=raw_client,
        node_id=node_id,
        include=include_params
    )
