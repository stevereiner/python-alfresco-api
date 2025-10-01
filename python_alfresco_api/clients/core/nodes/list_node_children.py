"""
List node children operations for Alfresco nodes.
Simplified function-based approach - no classes, just clean functions.
"""

from typing import Optional, List, Union
from .models import NodeListResponse, IncludeOption


def list_node_children(
    client,
    node_id: str,
    skip_count: int = 0,
    max_items: int = 100,
    include: Optional[List[Union[str, IncludeOption]]] = None,
    fields: Optional[List[str]] = None,
    order_by: Optional[List[str]] = None,
    where: Optional[str] = None,
    include_source: Optional[bool] = None
) -> NodeListResponse:
    """
    List children of a node (synchronous).
    
    Perfect for scripts, MCP servers, and command-line tools.
    
    Args:
        client: The nodes client instance
        node_id (str): Parent node identifier
        skip_count (int): Number of items to skip
        max_items (int): Maximum number of items to return
        include (Optional[List[Union[str, IncludeOption]]]): Additional data to include
        fields (Optional[List[str]]): Specific fields to return
        order_by (Optional[List[str]]): Sort order
        where (Optional[str]): Filter expression
        include_source (Optional[bool]): Include source information
        
    Returns:
        NodeListResponse: List of child nodes
        
    Examples:
        ```python
        # List children of a folder
        children = client.nodes.list_children("abc123-def456")
        
        # List with pagination
        children = client.nodes.list_children(
            "abc123-def456",
            skip_count=10,
            max_items=25
        )
        
        # List with filters
        children = client.nodes.list_children(
            "abc123-def456",
            where="(nodeType='cm:content')",
            order_by=["name ASC"]
        )
        ```
        
    Raises:
        NodeNotFoundError: Parent node doesn't exist
        PermissionError: User lacks permission to access node
        ValidationError: Invalid parameters provided
        
    Note:
        This method calls the raw sync client directly for optimal performance.
        For async operations, use list_node_children_async().
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import list_node_children
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
    
    # Convert optional parameters to UNSET if None
    fields_params = UNSET if fields is None else fields
    order_by_params = UNSET if order_by is None else order_by
    where_params = UNSET if where is None else where
    include_source_params = UNSET if include_source is None else include_source
    
    # Execute raw sync operation
    result = list_node_children.sync(
        client=raw_client,
        node_id=node_id,
        skip_count=skip_count,
        max_items=max_items,
        include=include_params,
        fields=fields_params,
        order_by=order_by_params,
        where=where_params,
        include_source=include_source_params
    )
    
    # Validate and return rich model
    if result is None:
        raise ValueError(f"Failed to list children for node {node_id}")
    return NodeListResponse.model_validate(result.to_dict())


async def list_node_children_async(
    client,
    node_id: str,
    skip_count: int = 0,
    max_items: int = 100,
    include: Optional[List[Union[str, IncludeOption]]] = None,
    fields: Optional[List[str]] = None,
    order_by: Optional[List[str]] = None,
    where: Optional[str] = None,
    include_source: Optional[bool] = None
) -> NodeListResponse:
    """
    List children of a node (asynchronous).
    
    Args:
        client: The nodes client instance
        node_id: Parent node identifier
        skip_count: Number of items to skip
        max_items: Maximum number of items to return
        include: Additional data to include
        fields: Specific fields to return
        order_by: Sort order
        where: Filter expression
        include_source: Include source information
        
    Returns:
        NodeListResponse: List of child nodes
        
    Examples:
        ```python
        # Async list children
        children = await client.nodes.list_children_async("abc123-def456")
        
        # With pagination and filters
        children = await client.nodes.list_children_async(
            "abc123-def456",
            skip_count=10,
            max_items=25,
            where="(nodeType='cm:content')",
            order_by=["name ASC"]
        )
        ```
        
    Raises:
        NodeNotFoundError: Parent node doesn't exist
        PermissionError: User lacks permission to access node
        ValidationError: Invalid parameters provided
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import list_node_children
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
    
    # Convert optional parameters to UNSET if None
    fields_params = UNSET if fields is None else fields
    order_by_params = UNSET if order_by is None else order_by
    where_params = UNSET if where is None else where
    include_source_params = UNSET if include_source is None else include_source
    
    # Execute raw async operation
    result = await list_node_children.asyncio(
        client=raw_client,
        node_id=node_id,
        skip_count=skip_count,
        max_items=max_items,
        include=include_params,
        fields=fields_params,
        order_by=order_by_params,
        where=where_params,
        include_source=include_source_params
    )
    
    # Validate and return rich model
    if result is None:
        raise ValueError(f"Failed to list children for node {node_id}")
    return NodeListResponse.model_validate(result.to_dict())


def list_node_children_detailed(
    client,
    node_id: str,
    skip_count: int = 0,
    max_items: int = 100,
    include: Optional[List[Union[str, IncludeOption]]] = None,
    fields: Optional[List[str]] = None,
    order_by: Optional[List[str]] = None,
    where: Optional[str] = None,
    include_source: Optional[bool] = None
):
    """
    List children operation (detailed sync).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import list_node_children
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
    
    # Convert optional parameters to UNSET if None
    fields_params = UNSET if fields is None else fields
    order_by_params = UNSET if order_by is None else order_by
    where_params = UNSET if where is None else where
    include_source_params = UNSET if include_source is None else include_source
    
    # Execute raw sync_detailed operation
    return list_node_children.sync_detailed(
        client=raw_client,
        node_id=node_id,
        skip_count=skip_count,
        max_items=max_items,
        include=include_params,
        fields=fields_params,
        order_by=order_by_params,
        where=where_params,
        include_source=include_source_params
    )


async def list_node_children_detailed_async(
    client,
    node_id: str,
    skip_count: int = 0,
    max_items: int = 100,
    include: Optional[List[Union[str, IncludeOption]]] = None,
    fields: Optional[List[str]] = None,
    order_by: Optional[List[str]] = None,
    where: Optional[str] = None,
    include_source: Optional[bool] = None
):
    """
    List children operation (detailed async).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import list_node_children
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
    
    # Convert optional parameters to UNSET if None
    fields_params = UNSET if fields is None else fields
    order_by_params = UNSET if order_by is None else order_by
    where_params = UNSET if where is None else where
    include_source_params = UNSET if include_source is None else include_source
    
    # Execute raw asyncio_detailed operation
    return await list_node_children.asyncio_detailed(
        client=raw_client,
        node_id=node_id,
        skip_count=skip_count,
        max_items=max_items,
        include=include_params,
        fields=fields_params,
        order_by=order_by_params,
        where=where_params,
        include_source=include_source_params
    )
