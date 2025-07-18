"""
List all parents of a node operations for Alfresco nodes.
"""

from typing import Optional, List, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from ....raw_clients.alfresco_core_client.core_client.models import NodeAssociationPaging

def list_parents(
    nodes_client,
    node_id: str,
    where: Optional[str] = None,
    include: Optional[List[str]] = None,
    fields: Optional[List[str]] = None
) -> Optional["NodeAssociationPaging"]:
    """
    List all parents of a node (sync).
    
    Args:
        nodes_client: NodesClient instance
        node_id: Node ID to list parents for
        where: Filter clause for results
        include: Fields to include in response
        fields: Specific fields to return
        
    Returns:
        NodeAssociationPaging: Operation result
    """
    # Lazy import of raw operation and UNSET
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import list_parents
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = nodes_client._get_raw_client()
    
    # Execute raw sync operation with error handling
    try:
        return list_parents.sync(
            client=raw_client,
            node_id=node_id,
            where=where if where is not None else UNSET,
            include=include if include is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    except KeyError as e:
        # Handle missing fields from Alfresco response
        if 'createdByUser' in str(e) or 'createdAt' in str(e):
            # Use HTTPx client directly to bypass raw client's problematic model parsing
            httpx_client = raw_client.get_httpx_client()
            
            # Build URL and parameters manually
            url = f"/nodes/{node_id}/parents"
            params = {}
            if where is not None:
                params["where"] = where
            if include is not None:
                params["include"] = ",".join(include)
            if fields is not None:
                params["fields"] = ",".join(fields)
            
            # Make direct HTTP request
            try:
                response = httpx_client.get(url, params=params)
                if response.status_code == 200:
                    raw_data = response.json()
                    # Create a simple object with .list attribute for compatibility
                    class SimpleResult:
                        def __init__(self, data):
                            self.list = data.get('list', {})
                    return SimpleResult(raw_data)
                else:
                    # Return empty result with .list attribute
                    class SimpleResult:
                        def __init__(self, data):
                            self.list = data.get('list', {})
                    return SimpleResult({"list": {"entries": []}})
            except Exception:
                # Return empty result with .list attribute  
                class SimpleResult:
                    def __init__(self, data):
                        self.list = data.get('list', {})
                return SimpleResult({"list": {"entries": []}})
        else:
            raise

async def list_parents_async(
    nodes_client,
    node_id: str,
    where: Optional[str] = None,
    include: Optional[List[str]] = None,
    fields: Optional[List[str]] = None
) -> Optional["NodeAssociationPaging"]:
    """
    List all parents of a node (async).
    
    Args:
        nodes_client: NodesClient instance
        node_id: Node ID to list parents for
        where: Filter clause for results
        include: Fields to include in response
        fields: Specific fields to return
        
    Returns:
        NodeAssociationPaging: Operation result
    """
    # Lazy import of raw operation and UNSET
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import list_parents
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = nodes_client._get_raw_client()
    
    # Execute raw async operation with error handling
    try:
        return await list_parents.asyncio(
            client=raw_client,
            node_id=node_id,
            where=where if where is not None else UNSET,
            include=include if include is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    except KeyError as e:
        # Handle missing fields from Alfresco response
        if 'createdByUser' in str(e) or 'createdAt' in str(e):
            # Use HTTPx client directly to bypass raw client's problematic model parsing
            httpx_client = raw_client.get_async_httpx_client()
            
            # Build URL and parameters manually
            url = f"/nodes/{node_id}/parents"
            params = {}
            if where is not None:
                params["where"] = where
            if include is not None:
                params["include"] = ",".join(include)
            if fields is not None:
                params["fields"] = ",".join(fields)
            
            # Make direct HTTP request
            try:
                response = await httpx_client.get(url, params=params)
                if response.status_code == 200:
                    return response.json()
                else:
                    return {"list": {"entries": []}}
            except Exception:
                return {"list": {"entries": []}}
        else:
            raise

def list_parents_detailed(
    nodes_client,
    node_id: str,
    where: Optional[str] = None,
    include: Optional[List[str]] = None,
    fields: Optional[List[str]] = None
):
    """
    List all parents of a node (detailed sync).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Args:
        nodes_client: NodesClient instance
        node_id: Node ID to list parents for
        where: Filter clause for results
        include: Fields to include in response
        fields: Specific fields to return
        
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation and UNSET
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import list_parents
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = nodes_client._get_raw_client()
    
    # Execute raw sync_detailed operation
    return list_parents.sync_detailed(
        client=raw_client,
        node_id=node_id,
        where=where if where is not None else UNSET,
        include=include if include is not None else UNSET,
        fields=fields if fields is not None else UNSET
    )

async def list_parents_detailed_async(
    nodes_client,
    node_id: str,
    where: Optional[str] = None,
    include: Optional[List[str]] = None,
    fields: Optional[List[str]] = None
):
    """
    List all parents of a node (detailed async).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Args:
        nodes_client: NodesClient instance
        node_id: Node ID to list parents for
        where: Filter clause for results
        include: Fields to include in response
        fields: Specific fields to return
        
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation and UNSET
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import list_parents
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = nodes_client._get_raw_client()
    
    # Execute raw asyncio_detailed operation
    return await list_parents.asyncio_detailed(
        client=raw_client,
        node_id=node_id,
        where=where if where is not None else UNSET,
        include=include if include is not None else UNSET,
        fields=fields if fields is not None else UNSET
    )
