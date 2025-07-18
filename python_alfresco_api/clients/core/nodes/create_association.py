"""
Create association operations for Alfresco nodes.
"""

from typing import Optional, List, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from ....raw_clients.alfresco_core_client.core_client.models import AssociationEntry

def create_association(
    nodes_client,
    node_id: str,
    target_id: str,
    assoc_type: str,
    fields: Optional[List[str]] = None
) -> Optional["AssociationEntry"]:
    """
    Create association between nodes (sync).
    
    Args:
        nodes_client: NodesClient instance
        node_id: Source node ID
        target_id: Target node ID
        assoc_type: Association type to create
        fields: Fields to include in response
        
    Returns:
        AssociationEntry: Operation result
    """
    # Lazy import of raw operation, body model, and UNSET
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import create_association
    from ....raw_clients.alfresco_core_client.core_client.models import AssociationBody
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = nodes_client._get_raw_client()
    
    # Create the body object using from_dict to ensure proper field mapping
    body_dict = {
        "targetId": target_id,
        "assocType": assoc_type
    }
    body = AssociationBody.from_dict(body_dict)
    
    # Execute raw sync operation with error handling
    try:
        return create_association.sync(
            client=raw_client,
            node_id=node_id,
            body=body,
            fields=fields if fields is not None else UNSET
        )
    except KeyError as e:
        # Handle missing fields from Alfresco response
        if 'assocType' in str(e):
            # Use detailed method to get raw response and return json data
            response = create_association.sync_detailed(
                client=raw_client,
                node_id=node_id,
                body=body,
                fields=fields if fields is not None else UNSET
            )
            # Return the raw json data without strict model parsing
            if hasattr(response, 'content') and response.status_code == 201:
                import json
                return json.loads(response.content)
            return None
        else:
            raise

async def create_association_async(
    nodes_client,
    node_id: str,
    target_id: str,
    assoc_type: str,
    fields: Optional[List[str]] = None
) -> Optional["AssociationEntry"]:
    """
    Create association between nodes (async).
    
    Args:
        nodes_client: NodesClient instance
        node_id: Source node ID
        target_id: Target node ID
        assoc_type: Association type to create
        fields: Fields to include in response
        
    Returns:
        AssociationEntry: Operation result
    """
    # Lazy import of raw operation, body model, and UNSET
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import create_association
    from ....raw_clients.alfresco_core_client.core_client.models import AssociationBody
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = nodes_client._get_raw_client()
    
    # Create the body object using from_dict to ensure proper field mapping
    body_dict = {
        "targetId": target_id,
        "assocType": assoc_type
    }
    body = AssociationBody.from_dict(body_dict)
    
    # Execute raw async operation with error handling
    try:
        return await create_association.asyncio(
            client=raw_client,
            node_id=node_id,
            body=body,
            fields=fields if fields is not None else UNSET
        )
    except KeyError as e:
        # Handle missing fields from Alfresco response
        if 'assocType' in str(e):
            # Use detailed method to get raw response and return json data
            response = await create_association.asyncio_detailed(
                client=raw_client,
                node_id=node_id,
                body=body,
                fields=fields if fields is not None else UNSET
            )
            # Return the raw json data without strict model parsing
            if hasattr(response, 'content') and response.status_code == 201:
                import json
                return json.loads(response.content)
            return None
        else:
            raise

def create_association_detailed(
    nodes_client,
    node_id: str,
    target_id: str,
    assoc_type: str,
    fields: Optional[List[str]] = None
):
    """
    Create association between nodes (detailed sync).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Args:
        nodes_client: NodesClient instance
        node_id: Source node ID
        target_id: Target node ID
        assoc_type: Association type to create
        fields: Fields to include in response
        
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation, body model, and UNSET
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import create_association
    from ....raw_clients.alfresco_core_client.core_client.models import AssociationBody
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = nodes_client._get_raw_client()
    
    # Create the body object using from_dict to ensure proper field mapping
    body_dict = {
        "targetId": target_id,
        "assocType": assoc_type
    }
    body = AssociationBody.from_dict(body_dict)
    
    # Execute raw sync_detailed operation
    return create_association.sync_detailed(
        client=raw_client,
        node_id=node_id,
        body=body,
        fields=fields if fields is not None else UNSET
    )

async def create_association_detailed_async(
    nodes_client,
    node_id: str,
    target_id: str,
    assoc_type: str,
    fields: Optional[List[str]] = None
):
    """
    Create association between nodes (detailed async).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Args:
        nodes_client: NodesClient instance
        node_id: Source node ID
        target_id: Target node ID
        assoc_type: Association type to create
        fields: Fields to include in response
        
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation, body model, and UNSET
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import create_association
    from ....raw_clients.alfresco_core_client.core_client.models import AssociationBody
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = nodes_client._get_raw_client()
    
    # Create the body object using from_dict to ensure proper field mapping
    body_dict = {
        "targetId": target_id,
        "assocType": assoc_type
    }
    body = AssociationBody.from_dict(body_dict)
    
    # Execute raw asyncio_detailed operation
    return await create_association.asyncio_detailed(
        client=raw_client,
        node_id=node_id,
        body=body,
        fields=fields if fields is not None else UNSET
    )
