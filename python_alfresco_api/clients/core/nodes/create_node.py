"""
Create new node operations for Alfresco nodes.
Simplified function-based approach - no classes, just clean functions.
"""

from typing import Optional, List, Union
from .models import NodeResponse, CreateNodeRequest


def create_node(
    client,
    parent_id: str,
    request: CreateNodeRequest
) -> NodeResponse:
    """
    Create a new node (synchronous).
    
    Perfect for scripts, MCP servers, and command-line tools.
    
    Args:
        client: The nodes client instance
        parent_id (str): Parent folder ID (or '-my-' for user's home)
        request (CreateNodeRequest): Node creation parameters
        
    Returns:
        NodeResponse: Created node information
        
    Examples:
        ```python
        # Create a folder in Alfresco
        folder = client.nodes.create(
            parent_id="-my-",
            request=CreateNodeRequest(
                name="Documents",
                node_type="cm:folder"
            )
        )
        
        # Create a file with properties
        file_node = client.nodes.create(
            parent_id=folder.entry.id,
            request=CreateNodeRequest(
                name="report.pdf",
                node_type="cm:content",
                properties={"cm:title": "Annual Report 2024"}
            )
        )
        ```
        
    Raises:
        ParentNotFoundError: Parent folder doesn't exist
        PermissionError: User lacks permission to create in parent
        ConflictError: Node with same name already exists
        ValidationError: Invalid request parameters
        
    Note:
        This method calls the raw sync client directly for optimal performance.
        For async operations, use create_node_async().
    """
    # Lazy import of raw operation and models
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import create_node
    from ....raw_clients.alfresco_core_client.core_client.models.node_body_create import NodeBodyCreate
    from ....raw_clients.alfresco_core_client.core_client.models.node_body_create_properties import NodeBodyCreateProperties
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client._get_raw_client()
    
    # Create proper body object
    properties = UNSET
    if request.properties:
        properties = NodeBodyCreateProperties.from_dict(request.properties)
        
    aspects = UNSET if request.aspects is None else request.aspects
    
    body = NodeBodyCreate(
        name=request.name,
        node_type=getattr(request.node_type, 'value', str(request.node_type)),
        aspect_names=aspects,
        properties=properties
    )
    
    # Use HTTPx client directly to bypass raw client's problematic body handling
    # Raw client has duplicate isinstance checks that always use multipart
    httpx_client = raw_client.get_httpx_client()
    
    # Build URL and parameters manually
    url = f"/nodes/{parent_id}/children"
    params: dict[str, str] = {}
    auto_rename = getattr(request, 'auto_rename', True)
    if auto_rename:
        params["autoRename"] = str(auto_rename).lower()
    
    # Add versioning parameters if provided
    if request.versioning_enabled is not None:
        params["versioningEnabled"] = str(request.versioning_enabled).lower()
    if request.major_version is not None:
        params["majorVersion"] = str(request.major_version).lower()
    
    # Build JSON body from request
    json_body = {
        "name": request.name,
        "nodeType": getattr(request.node_type, 'value', str(request.node_type))
    }
    
    if request.properties:
        json_body["properties"] = request.properties
    if request.aspects:
        json_body["aspectNames"] = request.aspects
    
    # Make direct HTTP request with proper JSON content type
    try:
        response = httpx_client.post(
            url,
            json=json_body,
            params=params,
            headers={"Content-Type": "application/json"}
        )
        
        # Handle response
        if response.status_code == 201:
            from ....raw_clients.alfresco_core_client.core_client.models import NodeEntry
            result = NodeEntry.from_dict(response.json())
            return NodeResponse.model_validate(result.to_dict())
        else:
            # Handle error responses
            response.raise_for_status()
            # This should never be reached due to raise_for_status()
            raise ValueError(f"Unexpected response status: {response.status_code}")
            
    except Exception as e:
        # Handle any errors including KeyError from missing fields
        if 'createdByUser' in str(e) or response.status_code == 201:
            # Return raw JSON data if model parsing fails
            try:
                result_data = response.json()
                return NodeResponse.model_validate(result_data)
            except:
                pass
        raise ValueError(f"Failed to create node in parent {parent_id}: {str(e)}")


async def create_node_async(
    client,
    parent_id: str,
    request: CreateNodeRequest
) -> NodeResponse:
    """
    Create a new node (asynchronous).
    
    Args:
        client: The nodes client instance
        parent_id: Parent folder ID (or '-my-' for user's home)
        request: Node creation parameters
        
    Returns:
        NodeResponse with created node information
        
    Examples:
        ```python
        # Create folder
        folder = await client.nodes.create_async(
            parent_id="-my-",
            request=CreateNodeRequest(
                name="My Documents",
                node_type="cm:folder",
                properties={
                    "cm:title": "My Document Collection",
                    "cm:description": "Personal documents folder"
                }
            )
        )
        
        # Create content node
        file_node = await client.nodes.create_async(
            parent_id=folder.entry.id,
            request=CreateNodeRequest(
                name="report.pdf",
                node_type="cm:content",
                properties={
                    "cm:title": "Annual Report 2024",
                    "cm:author": "Finance Team"
                }
            )
        )
        ```
        
    Raises:
        ParentNotFoundError: Parent folder doesn't exist
        PermissionError: User lacks permission to create in parent
        ConflictError: Node with same name already exists
        ValidationError: Invalid request parameters
    """
    # Lazy import of raw operation and models
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import create_node
    from ....raw_clients.alfresco_core_client.core_client.models.node_body_create import NodeBodyCreate
    from ....raw_clients.alfresco_core_client.core_client.models.node_body_create_properties import NodeBodyCreateProperties
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client._get_raw_client()
    
    # Create proper body object
    properties = UNSET
    if request.properties:
        properties = NodeBodyCreateProperties.from_dict(request.properties)
        
    aspects = UNSET if request.aspects is None else request.aspects
    
    body = NodeBodyCreate(
        name=request.name,
        node_type=getattr(request.node_type, 'value', str(request.node_type)),
        aspect_names=aspects,
        properties=properties
    )
    
    # Use HTTPx client directly to bypass raw client's problematic body handling
    # Raw client has duplicate isinstance checks that always use multipart
    httpx_client = raw_client.get_async_httpx_client()
    
    # Build URL and parameters manually
    url = f"/nodes/{parent_id}/children"
    params: dict[str, str] = {}
    auto_rename = getattr(request, 'auto_rename', True)
    if auto_rename:
        params["autoRename"] = str(auto_rename).lower()
    
    # Add versioning parameters if provided
    if request.versioning_enabled is not None:
        params["versioningEnabled"] = str(request.versioning_enabled).lower()
    if request.major_version is not None:
        params["majorVersion"] = str(request.major_version).lower()
    
    # Build JSON body from request
    json_body = {
        "name": request.name,
        "nodeType": getattr(request.node_type, 'value', str(request.node_type))
    }
    
    if request.properties:
        json_body["properties"] = request.properties
    if request.aspects:
        json_body["aspectNames"] = request.aspects
    
    # Make direct HTTP request with proper JSON content type
    try:
        response = await httpx_client.post(
            url,
            json=json_body,
            params=params,
            headers={"Content-Type": "application/json"}
        )
        
        # Handle response
        if response.status_code == 201:
            from ....raw_clients.alfresco_core_client.core_client.models import NodeEntry
            result = NodeEntry.from_dict(response.json())
            return NodeResponse.model_validate(result.to_dict())
        else:
            # Handle error responses
            response.raise_for_status()
            # This should never be reached due to raise_for_status()
            raise ValueError(f"Unexpected response status: {response.status_code}")
            
    except Exception as e:
        # Handle any errors including KeyError from missing fields
        if 'createdByUser' in str(e) or response.status_code == 201:
            # Return raw JSON data if model parsing fails
            try:
                result_data = response.json()
                return NodeResponse.model_validate(result_data)
            except:
                pass
        raise ValueError(f"Failed to create node in parent {parent_id}: {str(e)}")


def create_node_detailed(
    client,
    parent_id: str,
    request: CreateNodeRequest
):
    """
    Create node operation (detailed sync).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import create_node
    from ....raw_clients.alfresco_core_client.core_client.models.node_body_create import NodeBodyCreate
    from ....raw_clients.alfresco_core_client.core_client.models.node_body_create_properties import NodeBodyCreateProperties
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client._get_raw_client()
    
    # Create proper body object
    properties = UNSET
    if request.properties:
        properties = NodeBodyCreateProperties.from_dict(request.properties)
        
    aspects = UNSET if request.aspects is None else request.aspects
    
    body = NodeBodyCreate(
        name=request.name,
        node_type=getattr(request.node_type, 'value', str(request.node_type)),
        aspect_names=aspects,
        properties=properties
    )
    
    # Execute raw sync_detailed operation
    versioning_enabled = UNSET if request.versioning_enabled is None else request.versioning_enabled
    major_version = UNSET if request.major_version is None else request.major_version
    
    return create_node.sync_detailed(
        client=raw_client,
        node_id=parent_id,
        body=body,
        auto_rename=getattr(request, 'auto_rename', True),
        versioning_enabled=versioning_enabled,
        major_version=major_version
    )


async def create_node_detailed_async(
    client,
    parent_id: str,
    request: CreateNodeRequest
):
    """
    Create node operation (detailed async).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation and models
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import create_node
    from ....raw_clients.alfresco_core_client.core_client.models.node_body_create import NodeBodyCreate
    from ....raw_clients.alfresco_core_client.core_client.models.node_body_create_properties import NodeBodyCreateProperties
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = client._get_raw_client()
    
    # Create proper body object
    properties = UNSET
    if request.properties:
        properties = NodeBodyCreateProperties.from_dict(request.properties)
        
    aspects = UNSET if request.aspects is None else request.aspects
    
    body = NodeBodyCreate(
        name=request.name,
        node_type=getattr(request.node_type, 'value', str(request.node_type)),
        aspect_names=aspects,
        properties=properties
    )
    
    # Execute raw async_detailed operation
    versioning_enabled = UNSET if request.versioning_enabled is None else request.versioning_enabled
    major_version = UNSET if request.major_version is None else request.major_version
    
    return await create_node.asyncio_detailed(
        client=raw_client,
        node_id=parent_id,
        body=body,
        auto_rename=getattr(request, 'auto_rename', True),
        versioning_enabled=versioning_enabled,
        major_version=major_version
    )


    # ==================== UPDATE DETAILED METHODS - Added for 4-Pattern ====================
