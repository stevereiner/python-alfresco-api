"""
Update node properties operations for Alfresco nodes.
Clean function-based approach with 4 patterns: sync, async, detailed_sync, detailed_async.
"""

from typing import Optional, List, Union
from .models import (
    NodeResponse, NodeListResponse, CreateNodeRequest, UpdateNodeRequest,
    CopyNodeRequest, MoveNodeRequest, IncludeOption
)


def update_node(
    client,
    node_id: str, 
    request: UpdateNodeRequest,
    include: Optional[List[Union[str, IncludeOption]]] = None
) -> NodeResponse:
    """
    Update node properties (synchronous).
    
    Perfect for scripts, MCP servers, and command-line tools.
    
    Args:
        client: NodesClient instance
        node_id (str): Node identifier to update
        request (UpdateNodeRequest): Update parameters (name, properties)
        include (Optional[List[Union[str, IncludeOption]]]): Additional data to include in response
        
    Returns:
        NodeResponse: Updated node information
        
    Examples:
        ```python
        # Update node name in Alfresco
        updated = client.nodes.update(
            node_id="abc123-def456",
            request=UpdateNodeRequest(name="New Report Name.pdf")
        )
        
        # Update node properties
        updated = client.nodes.update(
            node_id="abc123-def456",
            request=UpdateNodeRequest(
                properties={
                    "cm:title": "Updated Annual Report 2024",
                    "cm:description": "Updated with Q4 data"
                }
            ),
            include=["properties"]
        )
        ```
        
    Raises:
        NodeNotFoundError: Node with given ID doesn't exist
        PermissionError: User lacks permission to update node
        ValidationError: Invalid request parameters
        
    Note:
        This method calls the raw sync client directly for optimal performance.
        For async operations, use update_node_async().
    """
    # Lazy import of raw operation and models
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import update_node
    from ....raw_clients.alfresco_core_client.core_client.models.node_body_update import NodeBodyUpdate
    from ....raw_clients.alfresco_core_client.core_client.models.node_body_update_properties import NodeBodyUpdateProperties
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client._get_raw_client()
    
    # Convert include options
    include_params = UNSET
    if include:
        include_params = [
            item.value if isinstance(item, IncludeOption) else item
            for item in include
        ]
    
    # Create proper body object
    properties = UNSET
    request_properties = getattr(request, 'properties', None)
    if request_properties:
        properties = NodeBodyUpdateProperties.from_dict(request_properties)
        
    body = NodeBodyUpdate(
        name=getattr(request, 'name', None) or UNSET,
        properties=properties
    )
    
    # Execute raw sync operation - calls sync httpx directly
    result = update_node.sync(
        client=raw_client,
        node_id=node_id,
        body=body,
        include=include_params
    )
    
    # Validate and return rich model
    if result is None:
        raise ValueError(f"Failed to update node {node_id}")
    return NodeResponse.model_validate(result.to_dict())


async def update_node_async(
    client,
    node_id: str, 
    request: UpdateNodeRequest,
    include: Optional[List[Union[str, IncludeOption]]] = None
) -> NodeResponse:
    """
    Update node properties (asynchronous).
    
    Args:
        client: NodesClient instance
        node_id: Node identifier
        request: Update parameters  
        include: Additional data to include in response
        
    Returns:
        NodeResponse with updated node information
        
    Examples:
        ```python
        # Update node name and properties
        updated = await client.nodes.update_async(
            node_id="abc123-def456",
            request=UpdateNodeRequest(
                name="Updated Report.pdf",
                properties={
                    "cm:title": "Updated Annual Report 2024",
                    "cm:description": "Updated with Q4 data"
                }
            ),
            include=["properties"]
        )
        ```
    """
    # Lazy import of raw operation and models
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import update_node
    from ....raw_clients.alfresco_core_client.core_client.models.node_body_update import NodeBodyUpdate
    from ....raw_clients.alfresco_core_client.core_client.models.node_body_update_properties import NodeBodyUpdateProperties
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client._get_raw_client()
    
    # Convert include options
    include_params = UNSET
    if include:
        include_params = [
            item.value if isinstance(item, IncludeOption) else item
            for item in include
        ]
    
    # Create proper body object
    properties = UNSET
    request_properties = getattr(request, 'properties', None)
    if request_properties:
        properties = NodeBodyUpdateProperties.from_dict(request_properties)
        
    body = NodeBodyUpdate(
        name=getattr(request, 'name', None) or UNSET,
        properties=properties
    )
    
    # Execute raw operation
    result = await update_node.asyncio(
        client=raw_client,
        node_id=node_id,
        body=body,
        include=include_params
    )
    
    # Validate and return rich model
    if result is None:
        raise ValueError(f"Failed to update node {node_id}")
    return NodeResponse.model_validate(result.to_dict())


def update_node_detailed(
    client,
    node_id: str, 
    request: UpdateNodeRequest, 
    include: Optional[List[Union[str, IncludeOption]]] = None
):
    """
    Update operation (detailed sync).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Args:
        client: NodesClient instance
        node_id: Node identifier
        request: Update parameters
        include: Additional data to include in response
        
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import update_node
    from ....raw_clients.alfresco_core_client.core_client.models.node_body_update import NodeBodyUpdate
    from ....raw_clients.alfresco_core_client.core_client.models.node_body_update_properties import NodeBodyUpdateProperties
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client._get_raw_client()
    
    # Convert include options
    include_params = UNSET
    if include:
        include_params = [
            item.value if isinstance(item, IncludeOption) else item
            for item in include
        ]
    
    # Create proper body object
    properties = UNSET
    request_properties = getattr(request, 'properties', None)
    if request_properties:
        properties = NodeBodyUpdateProperties.from_dict(request_properties)
        
    body = NodeBodyUpdate(
        name=getattr(request, 'name', None) or UNSET,
        properties=properties
    )
    
    # Execute raw sync_detailed operation
    return update_node.sync_detailed(
        client=raw_client,
        node_id=node_id,
        body=body,
        include=include_params
    )


async def update_node_detailed_async(
    client,
    node_id: str, 
    request: UpdateNodeRequest, 
    include: Optional[List[Union[str, IncludeOption]]] = None
):
    """
    Update operation (detailed async).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Args:
        client: NodesClient instance
        node_id: Node identifier
        request: Update parameters
        include: Additional data to include in response
        
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import update_node
    from ....raw_clients.alfresco_core_client.core_client.models.node_body_update import NodeBodyUpdate
    from ....raw_clients.alfresco_core_client.core_client.models.node_body_update_properties import NodeBodyUpdateProperties
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client._get_raw_client()
    
    # Convert include options
    include_params = UNSET
    if include:
        include_params = [
            item.value if isinstance(item, IncludeOption) else item
            for item in include
        ]
    
    # Create proper body object
    properties = UNSET
    request_properties = getattr(request, 'properties', None)
    if request_properties:
        properties = NodeBodyUpdateProperties.from_dict(request_properties)
        
    body = NodeBodyUpdate(
        name=getattr(request, 'name', None) or UNSET,
        properties=properties
    )
    
    # Execute raw async_detailed operation
    return await update_node.asyncio_detailed(
        client=raw_client,
        node_id=node_id,
        body=body,
        include=include_params
    )


    # ==================== DELETE DETAILED METHODS - Added for 4-Pattern ====================
