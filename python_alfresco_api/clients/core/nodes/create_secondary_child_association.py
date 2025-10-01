"""
Create secondary child association operations for Alfresco nodes.
"""

from typing import Optional, List, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from ....raw_clients.alfresco_core_client.core_client.models import ChildAssociationEntry

def create_secondary_child_association(
    nodes_client,
    node_id: str,
    child_id: str,
    assoc_type: str,
    fields: Optional[List[str]] = None
) -> Optional["ChildAssociationEntry"]:
    """
    Create secondary child association (sync).
    
    Args:
        nodes_client: NodesClient instance
        node_id: Parent node ID
        child_id: Child node ID
        assoc_type: Association type to create
        fields: Fields to include in response
        
    Returns:
        ChildAssociationEntry: Operation result
    """
    # Lazy import of raw operation, body model, and UNSET
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import create_secondary_child_association
    from ....raw_clients.alfresco_core_client.core_client.models import ChildAssociationBody
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = nodes_client.raw_client
    
    # Create the body object
    body = ChildAssociationBody(
        child_id=child_id,
        assoc_type=assoc_type
    )
    
    # Execute raw sync operation
    return create_secondary_child_association.sync(
        client=raw_client,
        node_id=node_id,
        body=body,
        fields=fields if fields is not None else UNSET
    )

async def create_secondary_child_association_async(
    nodes_client,
    node_id: str,
    child_id: str,
    assoc_type: str,
    fields: Optional[List[str]] = None
) -> Optional["ChildAssociationEntry"]:
    """
    Create secondary child association (async).
    
    Args:
        nodes_client: NodesClient instance
        node_id: Parent node ID
        child_id: Child node ID
        assoc_type: Association type to create
        fields: Fields to include in response
        
    Returns:
        ChildAssociationEntry: Operation result
    """
    # Lazy import of raw operation, body model, and UNSET
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import create_secondary_child_association
    from ....raw_clients.alfresco_core_client.core_client.models import ChildAssociationBody
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = nodes_client.raw_client
    
    # Create the body object
    body = ChildAssociationBody(
        child_id=child_id,
        assoc_type=assoc_type
    )
    
    # Execute raw async operation
    return await create_secondary_child_association.asyncio(
        client=raw_client,
        node_id=node_id,
        body=body,
        fields=fields if fields is not None else UNSET
    )

def create_secondary_child_association_detailed(
    nodes_client,
    node_id: str,
    child_id: str,
    assoc_type: str,
    fields: Optional[List[str]] = None
):
    """
    Create secondary child association (detailed sync).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Args:
        nodes_client: NodesClient instance
        node_id: Parent node ID
        child_id: Child node ID
        assoc_type: Association type to create
        fields: Fields to include in response
        
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation, body model, and UNSET
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import create_secondary_child_association
    from ....raw_clients.alfresco_core_client.core_client.models import ChildAssociationBody
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = nodes_client.raw_client
    
    # Create the body object
    body = ChildAssociationBody(
        child_id=child_id,
        assoc_type=assoc_type
    )
    
    # Execute raw sync_detailed operation
    return create_secondary_child_association.sync_detailed(
        client=raw_client,
        node_id=node_id,
        body=body,
        fields=fields if fields is not None else UNSET
    )

async def create_secondary_child_association_detailed_async(
    nodes_client,
    node_id: str,
    child_id: str,
    assoc_type: str,
    fields: Optional[List[str]] = None
):
    """
    Create secondary child association (detailed async).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Args:
        nodes_client: NodesClient instance
        node_id: Parent node ID
        child_id: Child node ID
        assoc_type: Association type to create
        fields: Fields to include in response
        
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation, body model, and UNSET
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import create_secondary_child_association
    from ....raw_clients.alfresco_core_client.core_client.models import ChildAssociationBody
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET
    
    # Get raw client
    raw_client = nodes_client.raw_client
    
    # Create the body object
    body = ChildAssociationBody(
        child_id=child_id,
        assoc_type=assoc_type
    )
    
    # Execute raw asyncio_detailed operation
    return await create_secondary_child_association.asyncio_detailed(
        client=raw_client,
        node_id=node_id,
        body=body,
        fields=fields if fields is not None else UNSET
    )
