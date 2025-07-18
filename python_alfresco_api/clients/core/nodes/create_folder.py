"""
Create folder (convenience wrapper) operations for Alfresco nodes.
"""

from typing import Optional, List, Union, TYPE_CHECKING, Any, cast

if TYPE_CHECKING:
    from .models import NodeResponse

def create_folder(
    nodes_client,
    name: str,
    parent_id: str = "-my-",
    properties: Optional[dict] = None,
    auto_rename: bool = True,
    fields: Optional[List[str]] = None
) -> Optional["NodeResponse"]:
    """
    Create a new folder (sync).
    
    Perfect for MCP servers, content organization, and workflows.
    Convenience method for creating folders with proper defaults.
    
    Args:
        nodes_client: NodesClient instance
        name: Folder name
        parent_id: Parent folder ID (default: "-my-" for user's home)
        properties: Custom properties to set on the folder
        auto_rename: Automatically rename if name conflicts exist
        fields: Fields to include in response
        
    Returns:
        NodeResponse: Response with created folder details (has .entry attribute)
        
    Examples:
        >>> # Create simple folder
        >>> folder = client.create_folder("My Documents")
        >>> print(f"Created: {folder.entry.name}")
        
        >>> # Create folder with properties
        >>> folder = client.create_folder(
        ...     "Project Files",
        ...     parent_id="workspace-123",
        ...     properties={"cm:title": "Project Documentation"}
        ... )
        
    Raises:
        ValueError: If invalid parameters
        PermissionError: If insufficient permissions
    """
    # Lazy import of raw operation, body model, and UNSET
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import create_node
    from ....raw_clients.alfresco_core_client.core_client.models import NodeBodyCreate
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = nodes_client._get_raw_client()
    
    # Create the body object for folder creation
    # Handle properties as regular dict (not model) to avoid to_dict() errors
    body_dict = {
        "name": name,
        "nodeType": "cm:folder"
    }
    if properties is not None:
        body_dict["properties"] = properties
    
    body = NodeBodyCreate.from_dict(body_dict)
    
    # Use HTTPx client directly to bypass raw client's problematic body handling
    # Raw client has duplicate isinstance checks that always use multipart
    httpx_client = raw_client.get_httpx_client()
    
    # Build URL and parameters manually
    url = f"/nodes/{parent_id}/children"
    params: dict[str, str] = {}
    if auto_rename:
        params["autoRename"] = str(auto_rename).lower()
    if fields is not None:
        params["fields"] = ",".join(fields)
    
    # Build JSON body
    json_body = body_dict
    
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
            from .models import NodeResponse, Node
            raw_data = response.json()
            # Create Node object from raw data
            node = Node.model_validate(raw_data)
            # Wrap in NodeResponse for proper .entry attribute access
            return NodeResponse(entry=node)
        else:
            # Handle error responses
            response.raise_for_status()
            
    except Exception as e:
        # Handle any errors including KeyError from missing fields
        if 'createdByUser' in str(e) or response.status_code == 201:
            # Return raw JSON data if model parsing fails
            try:
                raw_data = response.json()
                # Still try to create Node from raw data, with fallback handling
                from .models import NodeResponse, Node
                try:
                    node = Node.model_validate(raw_data)
                    return NodeResponse(entry=node)
                except:
                    # If Node creation fails, create minimal response
                    class MinimalEntry:
                        def __init__(self, data):
                            self.id = data.get('id', 'unknown')
                            self.name = data.get('name', 'unknown')
                            self.node_type = data.get('nodeType', 'cm:folder')
                    class MinimalResponse:
                        def __init__(self, entry):
                            self.entry = entry
                    return MinimalResponse(MinimalEntry(raw_data))
            except:
                return None
        else:
            raise

async def create_folder_async(
    nodes_client,
    name: str,
    parent_id: str = "-my-",
    properties: Optional[dict] = None,
    auto_rename: bool = True,
    fields: Optional[List[str]] = None
) -> Optional["NodeResponse"]:
    """
    Create a new folder (async).
    
    Perfect for MCP servers, content organization, and workflows.
    Convenience method for creating folders with proper defaults.
    
    Args:
        nodes_client: NodesClient instance
        name: Folder name
        parent_id: Parent folder ID (default: "-my-" for user's home)
        properties: Custom properties to set on the folder
        auto_rename: Automatically rename if name conflicts exist
        fields: Fields to include in response
        
    Returns:
        NodeResponse: Response with created folder details (has .entry attribute)
    """
    # Lazy import of raw operation, body model, and UNSET
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import create_node
    from ....raw_clients.alfresco_core_client.core_client.models import NodeBodyCreate
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = nodes_client._get_raw_client()
    
    # Create the body object for folder creation
    # Handle properties as regular dict (not model) to avoid to_dict() errors
    body_dict = {
        "name": name,
        "nodeType": "cm:folder"
    }
    if properties is not None:
        body_dict["properties"] = properties
    
    body = NodeBodyCreate.from_dict(body_dict)
    
    # Use HTTPx client directly to bypass raw client's problematic body handling
    # Raw client has duplicate isinstance checks that always use multipart
    httpx_client = raw_client.get_async_httpx_client()
    
    # Build URL and parameters manually
    url = f"/nodes/{parent_id}/children"
    params: dict[str, str] = {}
    if auto_rename:
        params["autoRename"] = str(auto_rename).lower()
    if fields is not None:
        params["fields"] = ",".join(fields)
    
    # Build JSON body
    json_body = body_dict
    
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
            from .models import NodeResponse, Node
            raw_data = response.json()
            # Create Node object from raw data
            node = Node.model_validate(raw_data)
            # Wrap in NodeResponse for proper .entry attribute access
            return NodeResponse(entry=node)
        else:
            # Handle error responses
            response.raise_for_status()
            
    except Exception as e:
        # Handle any errors including KeyError from missing fields
        if 'createdByUser' in str(e) or response.status_code == 201:
            # Return raw JSON data if model parsing fails
            try:
                raw_data = response.json()
                # Still try to create Node from raw data, with fallback handling
                from .models import NodeResponse, Node
                try:
                    node = Node.model_validate(raw_data)
                    return NodeResponse(entry=node)
                except:
                    # If Node creation fails, create minimal response
                    class MinimalEntry:
                        def __init__(self, data):
                            self.id = data.get('id', 'unknown')
                            self.name = data.get('name', 'unknown')
                            self.node_type = data.get('nodeType', 'cm:folder')
                    class MinimalResponse:
                        def __init__(self, entry):
                            self.entry = entry
                    return MinimalResponse(MinimalEntry(raw_data))
            except:
                return None
        else:
            raise

def create_folder_detailed(
    nodes_client,
    name: str,
    parent_id: str = "-my-",
    properties: Optional[dict] = None,
    auto_rename: bool = True,
    fields: Optional[List[str]] = None
):
    """
    Create folder (detailed sync).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Args:
        nodes_client: NodesClient instance
        name: Folder name
        parent_id: Parent folder ID (default: "-my-" for user's home)
        properties: Custom properties to set on the folder
        auto_rename: Automatically rename if name conflicts exist
        fields: Fields to include in response
        
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation, body model, and UNSET
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import create_node
    from ....raw_clients.alfresco_core_client.core_client.models import NodeBodyCreate
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = nodes_client._get_raw_client()
    
    # Create the body object for folder creation
    body = NodeBodyCreate(
        name=name,
        node_type="cm:folder",
        properties=cast(Any, properties) if properties is not None else UNSET
    )
    
    # Execute raw sync_detailed operation
    return create_node.sync_detailed(
        client=raw_client,
        node_id=parent_id,
        body=body,
        auto_rename=auto_rename,
        fields=fields if fields is not None else UNSET
    )

async def create_folder_detailed_async(
    nodes_client,
    name: str,
    parent_id: str = "-my-",
    properties: Optional[dict] = None,
    auto_rename: bool = True,
    fields: Optional[List[str]] = None
):
    """
    Create folder (detailed async).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Args:
        nodes_client: NodesClient instance
        name: Folder name
        parent_id: Parent folder ID (default: "-my-" for user's home)
        properties: Custom properties to set on the folder
        auto_rename: Automatically rename if name conflicts exist
        fields: Fields to include in response
        
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation, body model, and UNSET
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import create_node
    from ....raw_clients.alfresco_core_client.core_client.models import NodeBodyCreate
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = nodes_client._get_raw_client()
    
    # Create the body object for folder creation
    body = NodeBodyCreate(
        name=name,
        node_type="cm:folder",
        properties=cast(Any, properties) if properties is not None else UNSET
    )
    
    # Execute raw asyncio_detailed operation
    return await create_node.asyncio_detailed(
        client=raw_client,
        node_id=parent_id,
        body=body,
        auto_rename=auto_rename,
        fields=fields if fields is not None else UNSET
    )
