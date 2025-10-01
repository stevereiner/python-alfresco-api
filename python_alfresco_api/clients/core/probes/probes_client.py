"""
Probes Operations Client - Level 3: Probes-Specific Operations

This module provides probes-specific operations within the Core API.
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
from .models import ProbesResponse, ProbesListResponse, CreateProbesRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_core_client.core_client.api.probes import (
            get_probe as _get_probe
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class ProbesClient:
    """
    Probes operations client with 4-pattern detailed functions.
    
    Provides high-level methods for probes management operations
    that are essential for MCP servers and probes workflows.
    
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
            self._get_probe = _get_probe
    
    @property
    def raw_client(self):
        """Delegate to parent client's raw client."""
        return self.parent_client.raw_client
    
    @property
    def httpx_client(self):
        """Delegate to parent client's httpx client."""
        return self.parent_client.httpx_client

    # ==================== GET_PROBE OPERATION ====================
    
    def get_probe(self, probe_id: str) -> Any:
        """Get Probe operation."""
        from ....raw_clients.alfresco_core_client.core_client.api.probes import get_probe
        return get_probe.sync(client=self.raw_client, probe_id=probe_id)
    
    async def get_probe_async(self, probe_id: str) -> Any:
        """Get Probe operation (async)."""
        from ....raw_clients.alfresco_core_client.core_client.api.probes import get_probe
        return await get_probe.asyncio(client=self.raw_client, probe_id=probe_id)
    
    def get_probe_detailed(self, probe_id: str) -> Response:
        """Get Probe operation (detailed)."""
        from ....raw_clients.alfresco_core_client.core_client.api.probes import get_probe
        return get_probe.sync_detailed(client=self.raw_client, probe_id=probe_id)
    
    async def get_probe_detailed_async(self, probe_id: str) -> Response:
        """Get Probe operation (detailed, async)."""
        from ....raw_clients.alfresco_core_client.core_client.api.probes import get_probe
        return await get_probe.asyncio_detailed(client=self.raw_client, probe_id=probe_id)

    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self._client_factory, 'base_url', 'unknown')
        return f"ProbesClient(base_url='{base_url}')" 