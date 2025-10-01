"""
Renditions Operations Client - Level 3: Renditions-Specific Operations

This module provides renditions-specific operations within the Core API.
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
from .models import RenditionsResponse, RenditionsListResponse, CreateRenditionsRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_core_client.core_client.api.renditions import (
            create_rendition as _create_rendition,
            get_rendition as _get_rendition,
            list_renditions as _list_renditions
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class RenditionsClient:
    """
    Renditions operations client with 4-pattern detailed functions.
    
    Provides high-level methods for renditions management operations
    that are essential for MCP servers and renditions workflows.
    
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
            self._create_rendition = _create_rendition
            self._get_rendition = _get_rendition
            self._list_renditions = _list_renditions
    
    @property
    def raw_client(self):
        """Delegate to parent client's raw client."""
        return self.parent_client.raw_client
    
    @property
    def httpx_client(self):
        """Delegate to parent client's httpx client."""
        return self.parent_client.httpx_client

    # ==================== CREATE_RENDITION OPERATION ====================
    
    def create_rendition(self, node_id: str, body: Any) -> Any:
        """Create Rendition operation."""
        from ....raw_clients.alfresco_core_client.core_client.api.renditions import create_rendition
        return create_rendition.sync(client=self.raw_client, node_id=node_id, body=body)
    
    async def create_rendition_async(self, node_id: str, body: Any) -> Any:
        """Create Rendition operation (async)."""
        from ....raw_clients.alfresco_core_client.core_client.api.renditions import create_rendition
        return await create_rendition.asyncio(client=self.raw_client, node_id=node_id, body=body)
    
    def create_rendition_detailed(self, node_id: str, body: Any) -> Response:
        """Create Rendition operation (detailed)."""
        from ....raw_clients.alfresco_core_client.core_client.api.renditions import create_rendition
        return create_rendition.sync_detailed(client=self.raw_client, node_id=node_id, body=body)
    
    async def create_rendition_detailed_async(self, node_id: str, body: Any) -> Response:
        """Create Rendition operation (detailed, async)."""
        from ....raw_clients.alfresco_core_client.core_client.api.renditions import create_rendition
        return await create_rendition.asyncio_detailed(client=self.raw_client, node_id=node_id, body=body)

    # ==================== GET_RENDITION OPERATION ====================
    
    def get_rendition(self, node_id: str, rendition_id: str) -> Any:
        """Get Rendition operation."""
        from ....raw_clients.alfresco_core_client.core_client.api.renditions import get_rendition
        return get_rendition.sync(client=self.raw_client, node_id=node_id, rendition_id=rendition_id)
    
    async def get_rendition_async(self, node_id: str, rendition_id: str) -> Any:
        """Get Rendition operation (async)."""
        from ....raw_clients.alfresco_core_client.core_client.api.renditions import get_rendition
        return await get_rendition.asyncio(client=self.raw_client, node_id=node_id, rendition_id=rendition_id)
    
    def get_rendition_detailed(self, node_id: str, rendition_id: str) -> Response:
        """Get Rendition operation (detailed)."""
        from ....raw_clients.alfresco_core_client.core_client.api.renditions import get_rendition
        return get_rendition.sync_detailed(client=self.raw_client, node_id=node_id, rendition_id=rendition_id)
    
    async def get_rendition_detailed_async(self, node_id: str, rendition_id: str) -> Response:
        """Get Rendition operation (detailed, async)."""
        from ....raw_clients.alfresco_core_client.core_client.api.renditions import get_rendition
        return await get_rendition.asyncio_detailed(client=self.raw_client, node_id=node_id, rendition_id=rendition_id)

    # ==================== LIST_RENDITIONS OPERATION ====================
    
    def list_renditions(self, node_id: str, where: Optional[str] = None) -> Any:
        """List Renditions operation."""
        from ....raw_clients.alfresco_core_client.core_client.api.renditions import list_renditions
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return list_renditions.sync(
            client=self.raw_client,
            node_id=node_id,
            where=where if where is not None else UNSET
        )
    
    async def list_renditions_async(self, node_id: str, where: Optional[str] = None) -> Any:
        """List Renditions operation (async)."""
        from ....raw_clients.alfresco_core_client.core_client.api.renditions import list_renditions
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return await list_renditions.asyncio(
            client=self.raw_client,
            node_id=node_id,
            where=where if where is not None else UNSET
        )
    
    def list_renditions_detailed(self, node_id: str, where: Optional[str] = None) -> Response:
        """List Renditions operation (detailed)."""
        from ....raw_clients.alfresco_core_client.core_client.api.renditions import list_renditions
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return list_renditions.sync_detailed(
            client=self.raw_client,
            node_id=node_id,
            where=where if where is not None else UNSET
        )
    
    async def list_renditions_detailed_async(self, node_id: str, where: Optional[str] = None) -> Response:
        """List Renditions operation (detailed, async)."""
        from ....raw_clients.alfresco_core_client.core_client.api.renditions import list_renditions
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return await list_renditions.asyncio_detailed(
            client=self.raw_client,
            node_id=node_id,
            where=where if where is not None else UNSET
        )

    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self._client_factory, 'base_url', 'unknown')
        return f"RenditionsClient(base_url='{base_url}')" 