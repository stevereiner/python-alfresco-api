"""
Networks Operations Client - Level 3: Networks-Specific Operations

This module provides networks-specific operations within the Core API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.
"""

import asyncio
from typing import Optional, List, Union, Any
from httpx import Response

# Import from Level 3 (operation-specific models)
from .models import NetworksResponse, NetworksListResponse, CreateNetworksRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_core_client.core_client.api.networks import (
            get_network as _get_network,
            get_network_for_person as _get_network_for_person,
            list_networks_for_person as _list_networks_for_person
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class NetworksClient:
    """
    Networks operations client with 4-pattern detailed functions.
    
    Provides high-level methods for networks management operations
    that are essential for MCP servers and networks workflows.
    
    Each operation has 4 variants for maximum flexibility:
    - Basic sync/async for simple use cases
    - Detailed sync/async for full HTTP response access
    """
    
    def __init__(self, parent_client):
        """Initialize with client factory for raw client access."""
        self.parent_client = parent_client
        self._raw_client = None
        
        # Store raw operation references
        if RAW_OPERATIONS_AVAILABLE:
            self._get_network = _get_network
            self._get_network_for_person = _get_network_for_person
            self._list_networks_for_person = _list_networks_for_person
    
    @property
    def raw_client(self):
        """Delegate to parent client's raw client."""
        return self.parent_client.raw_client
    
    @property
    def httpx_client(self):
        """Delegate to parent client's httpx client."""
        return self.parent_client.httpx_client
    
    # =================================================================
    # NETWORKS OPERATIONS - BASIC IMPLEMENTATION (SYNC/ASYNC ONLY)
    # =================================================================
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self.parent_client._client_factory, 'base_url', 'unknown')
        return f"AlfrescoNetworksClient(base_url='{base_url}')"
    
    # =================================================================
    # GET NETWORK
    # =================================================================
    
    def get_network(
        self,
        network_id: str,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Get network (sync). Gets information about a network."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw networks operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._get_network.sync(
            network_id=network_id,
            client=self.raw_client,
            fields=fields if fields is not None else UNSET
        )
    
    async def get_network_async(
        self,
        network_id: str,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Get network (async). Gets information about a network."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw networks operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._get_network.asyncio(
            network_id=network_id,
            client=self.raw_client,
            fields=fields if fields is not None else UNSET
        )
    
    # =================================================================
    # GET NETWORK FOR PERSON
    # =================================================================
    
    def get_network_for_person(
        self,
        person_id: str,
        network_id: str,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Get network for person (sync). Gets network information for a person."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw networks operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._get_network_for_person.sync(
            person_id=person_id,
            network_id=network_id,
            client=self.raw_client,
            fields=fields if fields is not None else UNSET
        )
    
    async def get_network_for_person_async(
        self,
        person_id: str,
        network_id: str,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Get network for person (async). Gets network information for a person."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw networks operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._get_network_for_person.asyncio(
            person_id=person_id,
            network_id=network_id,
            client=self.raw_client,
            fields=fields if fields is not None else UNSET
        )
    
    # =================================================================
    # LIST NETWORKS FOR PERSON
    # =================================================================
    
    def list_networks_for_person(
        self,
        person_id: str,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """List networks for person (sync). Gets a list of networks for a person."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw networks operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._list_networks_for_person.sync(
            person_id=person_id,
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    async def list_networks_for_person_async(
        self,
        person_id: str,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """List networks for person (async). Gets a list of networks for a person."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw networks operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._list_networks_for_person.asyncio(
            person_id=person_id,
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            fields=fields if fields is not None else UNSET
        ) 