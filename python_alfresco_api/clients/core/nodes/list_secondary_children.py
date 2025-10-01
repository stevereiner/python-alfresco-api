"""
List secondary children of a node operations for Alfresco nodes.
Clean function-based approach with 4 patterns: sync, async, detailed_sync, detailed_async.
"""

from typing import Optional, List, Union
from .models import NodeResponse, NodeListResponse


def list_secondary_children(
    client,
    node_id: str,
    where: Optional[str] = None,
    include: Optional[List[str]] = None,
    fields: Optional[List[str]] = None
) -> NodeListResponse:
    """
    List secondary children of a node (synchronous).
    
    Perfect for scripts, MCP servers, and command-line tools.
    
    Args:
        client: NodesClient instance
        node_id (str): Node identifier to list secondary children for
        where (Optional[str]): WHERE clause to filter children
        include (Optional[List[str]]): Additional data to include in response
        fields (Optional[List[str]]): Specific fields to return
        
    Returns:
        NodeListResponse: List of secondary children
        
    Examples:
        ```python
        # List all secondary children
        children = client.nodes.list_secondary_children(
            node_id="abc123-def456"
        )
        
        # List with filtering
        children = client.nodes.list_secondary_children(
            node_id="abc123-def456",
            where="nodeType='cm:content'",
            include=["properties"]
        )
        ```
        
    Raises:
        NodeNotFoundError: Node with given ID doesn't exist
        PermissionError: User lacks permission to view secondary children
        ValidationError: Invalid request parameters
        
    Note:
        This method calls the raw sync client directly for optimal performance.
        For async operations, use list_secondary_children_async().
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import list_secondary_children
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client.raw_client
    
    # Convert parameters
    where_param = UNSET if where is None else where
    include_param = UNSET if include is None else include
    fields_param = UNSET if fields is None else fields
    
    # Execute raw sync operation
    result = list_secondary_children.sync(
        client=raw_client,
        node_id=node_id,
        where=where_param,
        include=include_param,
        fields=fields_param
    )
    
    # Handle empty results (expected when no secondary children exist)
    if result is None:
        # Create empty response structure
        empty_response = {
            "list": {
                "entries": [],
                "pagination": {
                    "count": 0,
                    "hasMoreItems": False,
                    "totalItems": 0,
                    "skipCount": 0,
                    "maxItems": 100
                }
            }
        }
        return NodeListResponse.model_validate(empty_response)
    
    return NodeListResponse.model_validate(result.to_dict())


async def list_secondary_children_async(
    client,
    node_id: str,
    where: Optional[str] = None,
    include: Optional[List[str]] = None,
    fields: Optional[List[str]] = None
) -> NodeListResponse:
    """
    List secondary children of a node (asynchronous).
    
    Args:
        client: NodesClient instance
        node_id: Node identifier to list secondary children for
        where: WHERE clause to filter children
        include: Additional data to include in response
        fields: Specific fields to return
        
    Returns:
        NodeListResponse: List of secondary children
        
    Examples:
        ```python
        # List secondary children (async)
        children = await client.nodes.list_secondary_children_async(
            node_id="abc123-def456"
        )
        ```
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import list_secondary_children
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client.raw_client
    
    # Convert parameters
    where_param = UNSET if where is None else where
    include_param = UNSET if include is None else include
    fields_param = UNSET if fields is None else fields
    
    # Execute raw async operation
    result = await list_secondary_children.asyncio(
        client=raw_client,
        node_id=node_id,
        where=where_param,
        include=include_param,
        fields=fields_param
    )
    
    # Handle empty results (expected when no secondary children exist)
    if result is None:
        # Create empty response structure
        empty_response = {
            "list": {
                "entries": [],
                "pagination": {
                    "count": 0,
                    "hasMoreItems": False,
                    "totalItems": 0,
                    "skipCount": 0,
                    "maxItems": 100
                }
            }
        }
        return NodeListResponse.model_validate(empty_response)
    
    return NodeListResponse.model_validate(result.to_dict())


def list_secondary_children_detailed(
    client,
    node_id: str,
    where: Optional[str] = None,
    include: Optional[List[str]] = None,
    fields: Optional[List[str]] = None
):
    """
    List secondary children of a node (detailed sync).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Args:
        client: NodesClient instance
        node_id: Node identifier to list secondary children for
        where: WHERE clause to filter children
        include: Additional data to include in response
        fields: Specific fields to return
        
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import list_secondary_children
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client.raw_client
    
    # Convert parameters
    where_param = UNSET if where is None else where
    include_param = UNSET if include is None else include
    fields_param = UNSET if fields is None else fields
    
    # Execute raw sync_detailed operation
    return list_secondary_children.sync_detailed(
        client=raw_client,
        node_id=node_id,
        where=where_param,
        include=include_param,
        fields=fields_param
    )


async def list_secondary_children_detailed_async(
    client,
    node_id: str,
    where: Optional[str] = None,
    include: Optional[List[str]] = None,
    fields: Optional[List[str]] = None
):
    """
    List secondary children of a node (detailed async).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Args:
        client: NodesClient instance
        node_id: Node identifier to list secondary children for
        where: WHERE clause to filter children
        include: Additional data to include in response
        fields: Specific fields to return
        
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import list_secondary_children
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client.raw_client
    
    # Convert parameters
    where_param = UNSET if where is None else where
    include_param = UNSET if include is None else include
    fields_param = UNSET if fields is None else fields
    
    # Execute raw asyncio_detailed operation
    return await list_secondary_children.asyncio_detailed(
        client=raw_client,
        node_id=node_id,
        where=where_param,
        include=include_param,
        fields=fields_param
    )
