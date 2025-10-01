"""
Lock a node for editing operations for Alfresco nodes.
Clean function-based approach with 4 patterns: sync, async, detailed_sync, detailed_async.
"""

from typing import Optional, List, Union
from .models import NodeResponse, NodeListResponse


def lock_node(
    client,
    node_id: str,
    request: Optional[dict] = None,
    include: Optional[List[Union[str, str]]] = None
) -> NodeResponse:
    """
    Lock a node for editing (synchronous).
    
    Perfect for scripts, MCP servers, and command-line tools.
    
    Args:
        client: NodesClient instance
        node_id (str): Node identifier to lock
        request (Optional[dict]): Lock parameters (timeout, type, lifetime)
        include (Optional[List[Union[str, str]]]): Additional data to include in response
        
    Returns:
        NodeResponse: Locked node information
        
    Examples:
        ```python
        # Lock node with default settings
        locked = client.nodes.lock(node_id="abc123-def456")
        
        # Lock node with custom timeout
        locked = client.nodes.lock(
            node_id="abc123-def456",
            request={"timeToExpire": 3600, "type": "FULL", "lifetime": "PERSISTENT"}
        )
        ```
        
    Raises:
        NodeNotFoundError: Node with given ID doesn't exist
        PermissionError: User lacks permission to lock node
        ConflictError: Node is already locked
        ValidationError: Invalid request parameters
        
    Note:
        This method calls the raw sync client directly for optimal performance.
        For async operations, use lock_node_async().
    """
    # Lazy import of raw operation and models
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import lock_node
    from ....raw_clients.alfresco_core_client.core_client.models.node_body_lock import NodeBodyLock
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client.raw_client
    
    # Convert include options
    include_params = UNSET
    if include:
        include_params = include
    
    # Create proper body object
    if request:
        body = NodeBodyLock.from_dict(request)
    else:
        body = NodeBodyLock()
    
    # Execute raw sync operation
    result = lock_node.sync(
        client=raw_client,
        node_id=node_id,
        body=body,
        include=include_params
    )
    
    # Validate and return rich model
    if result is None:
        raise ValueError(f"Failed to lock node {node_id}")
    return NodeResponse.model_validate(result.to_dict())


async def lock_node_async(
    client,
    node_id: str,
    request: Optional[dict] = None,
    include: Optional[List[Union[str, str]]] = None
) -> NodeResponse:
    """
    Lock a node for editing (asynchronous).
    
    Args:
        client: NodesClient instance
        node_id: Node identifier to lock
        request: Lock parameters (timeout, type, lifetime)
        include: Additional data to include in response
        
    Returns:
        NodeResponse: Locked node information
        
    Examples:
        ```python
        # Lock node with default settings (async)
        locked = await client.nodes.lock_async(node_id="abc123-def456")
        ```
    """
    # Lazy import of raw operation and models
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import lock_node
    from ....raw_clients.alfresco_core_client.core_client.models.node_body_lock import NodeBodyLock
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client.raw_client
    
    # Convert include options
    include_params = UNSET
    if include:
        include_params = include
    
    # Create proper body object
    if request:
        body = NodeBodyLock.from_dict(request)
    else:
        body = NodeBodyLock()
    
    # Execute raw async operation
    result = await lock_node.asyncio(
        client=raw_client,
        node_id=node_id,
        body=body,
        include=include_params
    )
    
    # Validate and return rich model
    if result is None:
        raise ValueError(f"Failed to lock node {node_id}")
    return NodeResponse.model_validate(result.to_dict())


def lock_node_detailed(
    client,
    node_id: str,
    request: Optional[dict] = None,
    include: Optional[List[Union[str, str]]] = None
):
    """
    Lock a node for editing (detailed sync).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Args:
        client: NodesClient instance
        node_id: Node identifier to lock
        request: Lock parameters
        include: Additional data to include in response
        
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import lock_node
    from ....raw_clients.alfresco_core_client.core_client.models.node_body_lock import NodeBodyLock
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client.raw_client
    
    # Convert include options
    include_params = UNSET
    if include:
        include_params = include
    
    # Create proper body object
    if request:
        body = NodeBodyLock.from_dict(request)
    else:
        body = NodeBodyLock()
    
    # Execute raw sync_detailed operation
    return lock_node.sync_detailed(
        client=raw_client,
        node_id=node_id,
        body=body,
        include=include_params
    )


async def lock_node_detailed_async(
    client,
    node_id: str,
    request: Optional[dict] = None,
    include: Optional[List[Union[str, str]]] = None
):
    """
    Lock a node for editing (detailed async).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Args:
        client: NodesClient instance
        node_id: Node identifier to lock
        request: Lock parameters
        include: Additional data to include in response
        
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import lock_node
    from ....raw_clients.alfresco_core_client.core_client.models.node_body_lock import NodeBodyLock
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client.raw_client
    
    # Convert include options
    include_params = UNSET
    if include:
        include_params = include
    
    # Create proper body object
    if request:
        body = NodeBodyLock.from_dict(request)
    else:
        body = NodeBodyLock()
    
    # Execute raw asyncio_detailed operation
    return await lock_node.asyncio_detailed(
        client=raw_client,
        node_id=node_id,
        body=body,
        include=include_params
    )
