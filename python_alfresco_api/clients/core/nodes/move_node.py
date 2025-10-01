"""
Move node operations for Alfresco nodes.
Clean function-based approach with 4 patterns: sync, async, detailed_sync, detailed_async.
"""

from typing import Optional, List, Union
import asyncio
from .models import (
    NodeResponse, NodeListResponse, CreateNodeRequest, UpdateNodeRequest,
    CopyNodeRequest, MoveNodeRequest, IncludeOption
)


def move_node(
    client,
    node_id: str,
    request: MoveNodeRequest,
    include: Optional[List[Union[str, IncludeOption]]] = None
) -> NodeResponse:
    """
    Move a node to another location (synchronous).
    
    Perfect for scripts, MCP servers, and command-line tools.
    
    Args:
        client: NodesClient instance
        node_id (str): Source node identifier to move
        request (MoveNodeRequest): Move parameters (target parent, new name)
        include (Optional[List[Union[str, IncludeOption]]]): Additional data to include in response
        
    Returns:
        NodeResponse: Moved node information
        
    Examples:
        ```python
        # Move node to another folder in Alfresco
        moved = client.nodes.move(
            node_id="abc123-def456",
            request=MoveNodeRequest(target_parent_id="target-folder-123")
        )
        
        # Move node with new name
        moved = client.nodes.move(
            node_id="abc123-def456",
            request=MoveNodeRequest(
                target_parent_id="target-folder-123",
                name="Moved Report.pdf"
            ),
            include=["properties", "path"]
        )
        ```
        
    Raises:
        NodeNotFoundError: Source node or target parent doesn't exist
        PermissionError: User lacks permission to move or create in target
        ConflictError: Node with same name already exists in target
        ValidationError: Invalid request parameters
        
    Note:
        This method calls the raw sync client directly for optimal performance.
        For async operations, use move_node_async().
    """
    # Lazy import of raw operation and models
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import move_node
    from ....raw_clients.alfresco_core_client.core_client.models.node_body_move import NodeBodyMove
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client.raw_client
    
    # Convert include options
    include_params = UNSET
    if include:
        include_params = [
            item.value if isinstance(item, IncludeOption) else item
            for item in include
        ]
    
    # Create proper body object
    target_parent_id = getattr(request, 'target_parent_id', None)
    if not target_parent_id:
        raise ValueError("target_parent_id is required for move operation")
    
    body = NodeBodyMove(
        target_parent_id=target_parent_id,
        name=getattr(request, 'name', None) or UNSET
    )
    
    # Execute raw sync operation
    result = move_node.sync(
        client=raw_client,
        node_id=node_id,
        body=body,
        include=include_params
    )
    
    # Validate and return rich model
    if result is None:
        raise ValueError(f"Failed to move node {node_id}")
    return NodeResponse.model_validate(result.to_dict())


async def move_node_async(
    client,
    node_id: str,
    request: MoveNodeRequest,
    include: Optional[List[Union[str, IncludeOption]]] = None
) -> NodeResponse:
    """
    Move a node to another location (asynchronous).
    
    Args:
        client: NodesClient instance
        node_id: Source node identifier to move
        request: Move parameters (target parent, new name)
        include: Additional data to include in response
        
    Returns:
        NodeResponse: Moved node information
        
    Examples:
        ```python
        # Move node to another folder (async)
        moved = await client.nodes.move_async(
            node_id="abc123-def456",
            request=MoveNodeRequest(target_parent_id="target-folder-123")
        )
        ```
    """
    # Lazy import of raw operation and models
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import move_node
    from ....raw_clients.alfresco_core_client.core_client.models.node_body_move import NodeBodyMove
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client.raw_client
    
    # Convert include options
    include_params = UNSET
    if include:
        include_params = [
            item.value if isinstance(item, IncludeOption) else item
            for item in include
        ]
    
    # Create proper body object
    target_parent_id = getattr(request, 'target_parent_id', None)
    if not target_parent_id:
        raise ValueError("target_parent_id is required for move operation")
    
    body = NodeBodyMove(
        target_parent_id=target_parent_id,
        name=getattr(request, 'name', None) or UNSET
    )
    
    # Execute raw operation
    result = await move_node.asyncio(
        client=raw_client,
        node_id=node_id,
        body=body,
        include=include_params
    )
    
    # Validate and return rich model
    if result is None:
        raise ValueError(f"Failed to move node {node_id}")
    return NodeResponse.model_validate(result.to_dict())


def move_node_detailed(
    client,
    node_id: str, 
    request: MoveNodeRequest, 
    include: Optional[List[Union[str, IncludeOption]]] = None
):
    """
    Move operation (detailed sync).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Args:
        client: NodesClient instance
        node_id: Source node identifier
        request: Move parameters
        include: Additional data to include in response
        
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import move_node
    from ....raw_clients.alfresco_core_client.core_client.models.node_body_move import NodeBodyMove
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client.raw_client
    
    # Convert include options
    include_params = UNSET
    if include:
        include_params = [
            item.value if isinstance(item, IncludeOption) else item
            for item in include
        ]
    
    # Create proper body object
    target_parent_id = getattr(request, 'target_parent_id', None)
    if not target_parent_id:
        raise ValueError("target_parent_id is required for move operation")
    
    body = NodeBodyMove(
        target_parent_id=target_parent_id,
        name=getattr(request, 'name', None) or UNSET
    )
    
    # Execute raw sync_detailed operation
    return move_node.sync_detailed(
        client=raw_client,
        node_id=node_id,
        body=body,
        include=include_params
    )


async def move_node_detailed_async(
    client,
    node_id: str, 
    request: MoveNodeRequest, 
    include: Optional[List[Union[str, IncludeOption]]] = None
):
    """
    Move operation (detailed async).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Args:
        client: NodesClient instance
        node_id: Source node identifier
        request: Move parameters
        include: Additional data to include in response
        
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import move_node
    from ....raw_clients.alfresco_core_client.core_client.models.node_body_move import NodeBodyMove
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client.raw_client
    
    # Convert include options
    include_params = UNSET
    if include:
        include_params = [
            item.value if isinstance(item, IncludeOption) else item
            for item in include
        ]
    
    # Create proper body object
    target_parent_id = getattr(request, 'target_parent_id', None)
    if not target_parent_id:
        raise ValueError("target_parent_id is required for move operation")
    
    body = NodeBodyMove(
        target_parent_id=target_parent_id,
        name=getattr(request, 'name', None) or UNSET
    )
    
    # Execute raw async_detailed operation
    return await move_node.asyncio_detailed(
        client=raw_client,
        node_id=node_id,
        body=body,
        include=include_params
    )


    # ==================== GET_CHILDREN DETAILED METHODS - Added for 4-Pattern ====================
