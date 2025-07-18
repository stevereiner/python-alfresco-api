"""
List associations where this node is the target operations for Alfresco nodes.
Clean function-based approach with 4 patterns: sync, async, detailed_sync, detailed_async.
"""

from typing import Optional, List, Union
from .models import NodeResponse, NodeListResponse


def list_target_associations(
    client,
    node_id: str,
    where: Optional[str] = None,
    include: Optional[List[str]] = None,
    fields: Optional[List[str]] = None
) -> NodeListResponse:
    """
    List associations where this node is the target (synchronous).
    
    Perfect for scripts, MCP servers, and command-line tools.
    
    Args:
        client: NodesClient instance
        node_id (str): Node identifier to list target associations for
        where (Optional[str]): WHERE clause to filter associations
        include (Optional[List[str]]): Additional data to include in response
        fields (Optional[List[str]]): Specific fields to return
        
    Returns:
        NodeListResponse: List of target associations
        
    Examples:
        ```python
        # List all target associations
        associations = client.nodes.list_target_associations(
            node_id="abc123-def456"
        )
        
        # List with filtering
        associations = client.nodes.list_target_associations(
            node_id="abc123-def456",
            where="assocType='cm:references'",
            include=["properties"]
        )
        ```
        
    Raises:
        NodeNotFoundError: Node with given ID doesn't exist
        PermissionError: User lacks permission to view associations
        ValidationError: Invalid request parameters
        
    Note:
        This method calls the raw sync client directly for optimal performance.
        For async operations, use list_target_associations_async().
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import list_target_associations
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client._get_raw_client()
    
    # Convert parameters
    where_param = UNSET if where is None else where
    include_param = UNSET if include is None else include
    fields_param = UNSET if fields is None else fields
    
    # Execute raw sync operation
    result = list_target_associations.sync(
        client=raw_client,
        node_id=node_id,
        where=where_param,
        include=include_param,
        fields=fields_param
    )
    
    # Validate and return rich model
    if result is None:
        raise ValueError(f"Failed to list target associations for node {node_id}")
    return NodeListResponse.model_validate(result.to_dict())


async def list_target_associations_async(
    client,
    node_id: str,
    where: Optional[str] = None,
    include: Optional[List[str]] = None,
    fields: Optional[List[str]] = None
) -> NodeListResponse:
    """
    List associations where this node is the target (asynchronous).
    
    Args:
        client: NodesClient instance
        node_id: Node identifier to list target associations for
        where: WHERE clause to filter associations
        include: Additional data to include in response
        fields: Specific fields to return
        
    Returns:
        NodeListResponse: List of target associations
        
    Examples:
        ```python
        # List target associations (async)
        associations = await client.nodes.list_target_associations_async(
            node_id="abc123-def456"
        )
        ```
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import list_target_associations
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client._get_raw_client()
    
    # Convert parameters
    where_param = UNSET if where is None else where
    include_param = UNSET if include is None else include
    fields_param = UNSET if fields is None else fields
    
    # Execute raw async operation
    result = await list_target_associations.asyncio(
        client=raw_client,
        node_id=node_id,
        where=where_param,
        include=include_param,
        fields=fields_param
    )
    
    # Validate and return rich model
    if result is None:
        raise ValueError(f"Failed to list target associations for node {node_id}")
    return NodeListResponse.model_validate(result.to_dict())


def list_target_associations_detailed(
    client,
    node_id: str,
    where: Optional[str] = None,
    include: Optional[List[str]] = None,
    fields: Optional[List[str]] = None
):
    """
    List associations where this node is the target (detailed sync).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Args:
        client: NodesClient instance
        node_id: Node identifier to list target associations for
        where: WHERE clause to filter associations
        include: Additional data to include in response
        fields: Specific fields to return
        
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import list_target_associations
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client._get_raw_client()
    
    # Convert parameters
    where_param = UNSET if where is None else where
    include_param = UNSET if include is None else include
    fields_param = UNSET if fields is None else fields
    
    # Execute raw sync_detailed operation
    return list_target_associations.sync_detailed(
        client=raw_client,
        node_id=node_id,
        where=where_param,
        include=include_param,
        fields=fields_param
    )


async def list_target_associations_detailed_async(
    client,
    node_id: str,
    where: Optional[str] = None,
    include: Optional[List[str]] = None,
    fields: Optional[List[str]] = None
):
    """
    List associations where this node is the target (detailed async).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Args:
        client: NodesClient instance
        node_id: Node identifier to list target associations for
        where: WHERE clause to filter associations
        include: Additional data to include in response
        fields: Specific fields to return
        
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import list_target_associations
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client._get_raw_client()
    
    # Convert parameters
    where_param = UNSET if where is None else where
    include_param = UNSET if include is None else include
    fields_param = UNSET if fields is None else fields
    
    # Execute raw asyncio_detailed operation
    return await list_target_associations.asyncio_detailed(
        client=raw_client,
        node_id=node_id,
        where=where_param,
        include=include_param,
        fields=fields_param
    )
