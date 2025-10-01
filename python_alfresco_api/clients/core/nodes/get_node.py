"""
Get node information operations for Alfresco nodes.
Simplified function-based approach - no classes, just clean functions.
"""

from typing import Optional, List, Union
from .models import NodeResponse, IncludeOption


def get_node(
    client,
    node_id: str,
    include: Optional[List[Union[str, IncludeOption]]] = None,
    fields: Optional[List[str]] = None
) -> NodeResponse:
    """
    Get node information by ID (synchronous).
    
    Perfect for scripts, MCP servers, and command-line tools.
    
    Args:
        client: The nodes client instance
        node_id (str): Node identifier (UUID or special alias like '-my-')
        include (Optional[List[Union[str, IncludeOption]]]): Additional data to include
        fields (Optional[List[str]]): Specific fields to return (limits response size)
        
    Returns:
        NodeResponse: Node information with comprehensive metadata
        
    Examples:
        ```python
        # Get node details from Alfresco
        node = client.nodes.get("abc123-def456")
        
        # Get node with additional data
        node = client.nodes.get(
            "abc123-def456",
            include=["properties", "permissions", "path"]
        )
        
        # Get specific fields only
        node = client.nodes.get(
            "abc123-def456", 
            fields=["id", "name", "nodeType"]
        )
        ```
        
    Raises:
        NodeNotFoundError: Node with given ID doesn't exist
        PermissionError: User lacks permission to access node
        ValidationError: Invalid parameters provided
        
    Note:
        This method calls the raw sync client directly for optimal performance.
        For async operations, use get_node_async().
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import get_node
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client.raw_client
    
    # Convert include options to strings if needed
    include_params = UNSET
    if include:
        include_params = [
            item.value if isinstance(item, IncludeOption) else item
            for item in include
        ]
    
    # Convert fields to UNSET if None
    fields_params = UNSET if fields is None else fields
    
    # Execute raw sync operation - calls sync httpx directly
    result = get_node.sync(
        client=raw_client,
        node_id=node_id,
        include=include_params,
        fields=fields_params
    )
    
    # Validate and return rich model
    if result is None:
        raise ValueError(f"Node {node_id} not found")
    return NodeResponse.model_validate(result.to_dict())


async def get_node_async(
    client,
    node_id: str,
    include: Optional[List[Union[str, IncludeOption]]] = None,
    fields: Optional[List[str]] = None
) -> NodeResponse:
    """
    Get node information by ID (asynchronous).
    
    Args:
        client: The nodes client instance
        node_id: Node identifier (UUID or special alias like '-my-')
        include: Additional data to include (properties, permissions, path, etc.)
        fields: Specific fields to return (limits response size)
        
    Returns:
        NodeResponse with comprehensive node information
        
    Examples:
        ```python
        # Async usage for web apps
        node = await client.nodes.get_async("abc123-def456")
        
        # Include additional data
        node = await client.nodes.get_async(
            "abc123-def456",
            include=["properties", "permissions", "path"]
        )
        
        # Get specific fields only
        node = await client.nodes.get_async(
            "abc123-def456", 
            fields=["id", "name", "nodeType"]
        )
        ```
        
    Raises:
        NodeNotFoundError: Node with given ID doesn't exist
        PermissionError: User lacks permission to access node
        ValidationError: Invalid parameters provided
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import get_node
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client.raw_client
    
    # Convert include options to strings if needed
    include_params = UNSET
    if include:
        include_params = [
            item.value if isinstance(item, IncludeOption) else item
            for item in include
        ]
    
    # Convert fields to UNSET if None
    fields_params = UNSET if fields is None else fields
    
    # Execute raw operation
    result = await get_node.asyncio(
        client=raw_client,
        node_id=node_id,
        include=include_params,
        fields=fields_params
    )
    
    # Validate and return rich model - result is NodeEntry or None
    if result is None:
        raise ValueError(f"Node {node_id} not found")
    return NodeResponse.model_validate(result.to_dict())


def get_node_detailed(
    client,
    node_id: str,
    include: Optional[List[Union[str, IncludeOption]]] = None,
    fields: Optional[List[str]] = None
):
    """
    Get node operation (detailed sync).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import get_node
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client.raw_client
    
    # Convert include options to strings if needed
    include_params = UNSET
    if include:
        include_params = [
            item.value if isinstance(item, IncludeOption) else item
            for item in include
        ]
    
    # Convert fields to UNSET if None
    fields_params = UNSET if fields is None else fields
    
    # Execute raw sync_detailed operation
    return get_node.sync_detailed(
        client=raw_client,
        node_id=node_id,
        include=include_params,
        fields=fields_params
    )


async def get_node_detailed_async(
    client,
    node_id: str,
    include: Optional[List[Union[str, IncludeOption]]] = None,
    fields: Optional[List[str]] = None
):
    """
    Get node operation (detailed async).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import get_node
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client.raw_client
    
    # Convert include options to strings if needed
    include_params = UNSET
    if include:
        include_params = [
            item.value if isinstance(item, IncludeOption) else item
            for item in include
        ]
    
    # Convert fields to UNSET if None
    fields_params = UNSET if fields is None else fields
    
    # Execute raw asyncio_detailed operation
    return await get_node.asyncio_detailed(
        client=raw_client,
        node_id=node_id,
        include=include_params,
        fields=fields_params
    )


    # ==================== CREATE DETAILED METHODS - Added for 4-Pattern ====================
