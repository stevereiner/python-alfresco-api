"""
List associations where this node is the source operations for Alfresco nodes.
Clean function-based approach with 4 patterns: sync, async, detailed_sync, detailed_async.
"""

from typing import Optional, List, Union
from .models import NodeResponse, NodeListResponse


def list_source_associations(
    client,
    node_id: str,
    where: Optional[str] = None,
    include: Optional[List[str]] = None,
    fields: Optional[List[str]] = None
) -> NodeListResponse:
    """
    List associations where this node is the source (synchronous).
    
    Perfect for scripts, MCP servers, and command-line tools.
    
    Args:
        client: NodesClient instance
        node_id (str): Node identifier to list source associations for
        where (Optional[str]): WHERE clause to filter associations
        include (Optional[List[str]]): Additional data to include in response
        fields (Optional[List[str]]): Specific fields to return
        
    Returns:
        NodeListResponse: List of source associations
        
    Examples:
        ```python
        # List all source associations
        associations = client.nodes.list_source_associations(
            node_id="abc123-def456"
        )
        
        # List with filtering
        associations = client.nodes.list_source_associations(
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
        For async operations, use list_source_associations_async().
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import list_source_associations
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client._get_raw_client()
    
    # Convert parameters
    where_param = UNSET if where is None else where
    include_param = UNSET if include is None else include
    fields_param = UNSET if fields is None else fields
    
    # Execute raw sync operation with error handling
    try:
        result = list_source_associations.sync(
            client=raw_client,
            node_id=node_id,
            where=where_param,
            include=include_param,
            fields=fields_param
        )
        
        # Validate and return rich model
        if result is None:
            raise ValueError(f"Failed to list source associations for node {node_id}")
        return NodeListResponse.model_validate(result.to_dict())
        
    except KeyError as e:
        # Handle missing fields from Alfresco response
        if 'createdAt' in str(e) or 'createdByUser' in str(e):
            # Use detailed method to get raw response and return json data
            response = list_source_associations.sync_detailed(
                client=raw_client,
                node_id=node_id,
                where=where_param,
                include=include_param,
                fields=fields_param
            )
            # Return the raw json data without strict model parsing
            if hasattr(response, 'content') and response.status_code == 200:
                import json
                raw_data = json.loads(response.content)
                return NodeListResponse.model_validate(raw_data)
            # Return empty list as fallback
            empty_response = {"list": {"entries": []}}
            return NodeListResponse.model_validate(empty_response)
        else:
            raise


async def list_source_associations_async(
    client,
    node_id: str,
    where: Optional[str] = None,
    include: Optional[List[str]] = None,
    fields: Optional[List[str]] = None
) -> NodeListResponse:
    """
    List associations where this node is the source (asynchronous).
    
    Args:
        client: NodesClient instance
        node_id: Node identifier to list source associations for
        where: WHERE clause to filter associations
        include: Additional data to include in response
        fields: Specific fields to return
        
    Returns:
        NodeListResponse: List of source associations
        
    Examples:
        ```python
        # List source associations (async)
        associations = await client.nodes.list_source_associations_async(
            node_id="abc123-def456"
        )
        ```
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import list_source_associations
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client._get_raw_client()
    
    # Convert parameters
    where_param = UNSET if where is None else where
    include_param = UNSET if include is None else include
    fields_param = UNSET if fields is None else fields
    
    # Execute raw async operation with error handling
    try:
        result = await list_source_associations.asyncio(
            client=raw_client,
            node_id=node_id,
            where=where_param,
            include=include_param,
            fields=fields_param
        )
        
        # Validate and return rich model
        if result is None:
            raise ValueError(f"Failed to list source associations for node {node_id}")
        return NodeListResponse.model_validate(result.to_dict())
        
    except (KeyError, ValueError) as e:
        # Handle missing fields from Alfresco response
        if 'createdAt' in str(e) or 'createdByUser' in str(e):
            # Use HTTPx client directly to bypass raw client's problematic model parsing
            httpx_client = raw_client.get_async_httpx_client()
            
            # Build URL and parameters manually
            url = f"/nodes/{node_id}/source-associations"
            params = {}
            if where_param != UNSET:
                params["where"] = where_param
            if include_param != UNSET and isinstance(include_param, list):
                params["include"] = ",".join(include_param)
            if fields_param != UNSET and isinstance(fields_param, list):
                params["fields"] = ",".join(fields_param)
            
            # Make direct HTTP request
            try:
                response = await httpx_client.get(url, params=params)
                if response.status_code == 200:
                    raw_data = response.json()
                    # Return the raw JSON data directly to avoid model parsing issues
                    return NodeListResponse.model_validate(raw_data)
                else:
                    # Return empty list as fallback
                    empty_response = {"list": {"entries": []}}
                    return NodeListResponse.model_validate(empty_response)
            except Exception:
                # Return empty list as fallback
                empty_response = {"list": {"entries": []}}
                return NodeListResponse.model_validate(empty_response)
        else:
            raise


def list_source_associations_detailed(
    client,
    node_id: str,
    where: Optional[str] = None,
    include: Optional[List[str]] = None,
    fields: Optional[List[str]] = None
):
    """
    List associations where this node is the source (detailed sync).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Args:
        client: NodesClient instance
        node_id: Node identifier to list source associations for
        where: WHERE clause to filter associations
        include: Additional data to include in response
        fields: Specific fields to return
        
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import list_source_associations
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client._get_raw_client()
    
    # Convert parameters
    where_param = UNSET if where is None else where
    include_param = UNSET if include is None else include
    fields_param = UNSET if fields is None else fields
    
    # Execute raw sync_detailed operation
    return list_source_associations.sync_detailed(
        client=raw_client,
        node_id=node_id,
        where=where_param,
        include=include_param,
        fields=fields_param
    )


async def list_source_associations_detailed_async(
    client,
    node_id: str,
    where: Optional[str] = None,
    include: Optional[List[str]] = None,
    fields: Optional[List[str]] = None
):
    """
    List associations where this node is the source (detailed async).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Args:
        client: NodesClient instance
        node_id: Node identifier to list source associations for
        where: WHERE clause to filter associations
        include: Additional data to include in response
        fields: Specific fields to return
        
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import list_source_associations
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client._get_raw_client()
    
    # Convert parameters
    where_param = UNSET if where is None else where
    include_param = UNSET if include is None else include
    fields_param = UNSET if fields is None else fields
    
    # Execute raw asyncio_detailed operation
    return await list_source_associations.asyncio_detailed(
        client=raw_client,
        node_id=node_id,
        where=where_param,
        include=include_param,
        fields=fields_param
    )
