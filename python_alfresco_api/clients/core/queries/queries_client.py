"""
Queries Operations Client - Level 3: Queries-Specific Operations

This module provides queries-specific operations within the Core API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.

Each operation provides 4 variants:
- operation(params) - basic sync with explicit parameters
- operation_async(params) - basic async with explicit parameters  
- operation_detailed(params) - detailed sync with explicit parameters
- operation_detailed_async(params) - detailed async with explicit parameters

Perfect for MCP servers and documentation generation.
"""

import asyncio
from typing import Optional, List, Union, Any
from httpx import Response

# Import from Level 3 (operation-specific models)
from .models import QueriesResponse, QueriesListResponse, CreateQueriesRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_core_client.core_client.api.queries import (
            find_nodes as _find_nodes,
            find_people as _find_people,
            find_sites as _find_sites
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class QueriesClient:
    """
    Queries operations client with 4-pattern detailed functions.
    
    Provides high-level methods for queries management operations
    that are essential for MCP servers and queries workflows.
    
    Each operation has 4 variants for maximum flexibility:
    - Basic sync/async for simple use cases
    - Detailed sync/async for full HTTP response access
    """
    
    def __init__(self, parent_client):
        """Initialize with parent client for delegation."""
        self.parent_client = parent_client
        
        # Store raw operation references
        if RAW_OPERATIONS_AVAILABLE:
            self._find_nodes = _find_nodes
            self._find_people = _find_people
            self._find_sites = _find_sites
    
    @property
    def raw_client(self):
        """Delegate to parent client's raw client."""
        return self.parent_client.raw_client
    
    @property
    def httpx_client(self):
        """Delegate to parent client's httpx client."""
        return self.parent_client.httpx_client

    # ==================== FIND_NODES OPERATION ====================
    
    def find_nodes(self, term: str, root_node_id: Optional[str] = None, skip_count: Optional[int] = None, 
                   max_items: Optional[int] = None, node_type: Optional[str] = None, 
                   include: Optional[List[str]] = None, order_by: Optional[List[str]] = None, 
                   fields: Optional[List[str]] = None) -> Any:
        """Find Nodes operation."""
        from ....raw_clients.alfresco_core_client.core_client.api.queries import find_nodes
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return find_nodes.sync(
            client=self.raw_client,
            term=term,
            root_node_id=root_node_id if root_node_id is not None else UNSET,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            node_type=node_type if node_type is not None else UNSET,
            include=include if include is not None else UNSET,
            order_by=order_by if order_by is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    async def find_nodes_async(self, term: str, root_node_id: Optional[str] = None, skip_count: Optional[int] = None, 
                              max_items: Optional[int] = None, node_type: Optional[str] = None, 
                              include: Optional[List[str]] = None, order_by: Optional[List[str]] = None, 
                              fields: Optional[List[str]] = None) -> Any:
        """Find Nodes operation (async)."""
        from ....raw_clients.alfresco_core_client.core_client.api.queries import find_nodes
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return await find_nodes.asyncio(
            client=self.raw_client,
            term=term,
            root_node_id=root_node_id if root_node_id is not None else UNSET,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            node_type=node_type if node_type is not None else UNSET,
            include=include if include is not None else UNSET,
            order_by=order_by if order_by is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    def find_nodes_detailed(self, term: str, root_node_id: Optional[str] = None, skip_count: Optional[int] = None, 
                           max_items: Optional[int] = None, node_type: Optional[str] = None, 
                           include: Optional[List[str]] = None, order_by: Optional[List[str]] = None, 
                           fields: Optional[List[str]] = None) -> Response:
        """Find Nodes operation (detailed)."""
        from ....raw_clients.alfresco_core_client.core_client.api.queries import find_nodes
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return find_nodes.sync_detailed(
            client=self.raw_client,
            term=term,
            root_node_id=root_node_id if root_node_id is not None else UNSET,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            node_type=node_type if node_type is not None else UNSET,
            include=include if include is not None else UNSET,
            order_by=order_by if order_by is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    async def find_nodes_detailed_async(self, term: str, root_node_id: Optional[str] = None, skip_count: Optional[int] = None, 
                                       max_items: Optional[int] = None, node_type: Optional[str] = None, 
                                       include: Optional[List[str]] = None, order_by: Optional[List[str]] = None, 
                                       fields: Optional[List[str]] = None) -> Response:
        """Find Nodes operation (detailed, async)."""
        from ....raw_clients.alfresco_core_client.core_client.api.queries import find_nodes
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return await find_nodes.asyncio_detailed(
            client=self.raw_client,
            term=term,
            root_node_id=root_node_id if root_node_id is not None else UNSET,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            node_type=node_type if node_type is not None else UNSET,
            include=include if include is not None else UNSET,
            order_by=order_by if order_by is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )

    # ==================== FIND_PEOPLE OPERATION ====================
    
    def find_people(self, term: str, skip_count: Optional[int] = None, max_items: Optional[int] = None, 
                    fields: Optional[List[str]] = None, order_by: Optional[List[str]] = None) -> Any:
        """Find People operation."""
        from ....raw_clients.alfresco_core_client.core_client.api.queries import find_people
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return find_people.sync(
            client=self.raw_client,
            term=term,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            fields=fields if fields is not None else UNSET,
            order_by=order_by if order_by is not None else UNSET
        )
    
    async def find_people_async(self, term: str, skip_count: Optional[int] = None, max_items: Optional[int] = None, 
                               fields: Optional[List[str]] = None, order_by: Optional[List[str]] = None) -> Any:
        """Find People operation (async)."""
        from ....raw_clients.alfresco_core_client.core_client.api.queries import find_people
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return await find_people.asyncio(
            client=self.raw_client,
            term=term,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            fields=fields if fields is not None else UNSET,
            order_by=order_by if order_by is not None else UNSET
        )
    
    def find_people_detailed(self, term: str, skip_count: Optional[int] = None, max_items: Optional[int] = None, 
                            fields: Optional[List[str]] = None, order_by: Optional[List[str]] = None) -> Response:
        """Find People operation (detailed)."""
        from ....raw_clients.alfresco_core_client.core_client.api.queries import find_people
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return find_people.sync_detailed(
            client=self.raw_client,
            term=term,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            fields=fields if fields is not None else UNSET,
            order_by=order_by if order_by is not None else UNSET
        )
    
    async def find_people_detailed_async(self, term: str, skip_count: Optional[int] = None, max_items: Optional[int] = None, 
                                        fields: Optional[List[str]] = None, order_by: Optional[List[str]] = None) -> Response:
        """Find People operation (detailed, async)."""
        from ....raw_clients.alfresco_core_client.core_client.api.queries import find_people
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return await find_people.asyncio_detailed(
            client=self.raw_client,
            term=term,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            fields=fields if fields is not None else UNSET,
            order_by=order_by if order_by is not None else UNSET
        )

    # ==================== FIND_SITES OPERATION ====================
    
    def find_sites(self, term: str, skip_count: Optional[int] = None, max_items: Optional[int] = None, 
                   order_by: Optional[List[str]] = None, fields: Optional[List[str]] = None) -> Any:
        """Find Sites operation."""
        from ....raw_clients.alfresco_core_client.core_client.api.queries import find_sites
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return find_sites.sync(
            client=self.raw_client,
            term=term,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            order_by=order_by if order_by is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    async def find_sites_async(self, term: str, skip_count: Optional[int] = None, max_items: Optional[int] = None, 
                              order_by: Optional[List[str]] = None, fields: Optional[List[str]] = None) -> Any:
        """Find Sites operation (async)."""
        from ....raw_clients.alfresco_core_client.core_client.api.queries import find_sites
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return await find_sites.asyncio(
            client=self.raw_client,
            term=term,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            order_by=order_by if order_by is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    def find_sites_detailed(self, term: str, skip_count: Optional[int] = None, max_items: Optional[int] = None, 
                           order_by: Optional[List[str]] = None, fields: Optional[List[str]] = None) -> Response:
        """Find Sites operation (detailed)."""
        from ....raw_clients.alfresco_core_client.core_client.api.queries import find_sites
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return find_sites.sync_detailed(
            client=self.raw_client,
            term=term,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            order_by=order_by if order_by is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    async def find_sites_detailed_async(self, term: str, skip_count: Optional[int] = None, max_items: Optional[int] = None, 
                                       order_by: Optional[List[str]] = None, fields: Optional[List[str]] = None) -> Response:
        """Find Sites operation (detailed, async)."""
        from ....raw_clients.alfresco_core_client.core_client.api.queries import find_sites
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return await find_sites.asyncio_detailed(
            client=self.raw_client,
            term=term,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            order_by=order_by if order_by is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )

    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self._client_factory, 'base_url', 'unknown')
        return f"QueriesClient(base_url='{base_url}')" 