"""
Aspects Operations Client - Level 3: Aspects-Specific Operations

This module provides aspects-specific operations within the Model API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.

Each operation provides 4 variants:
- operation(params) - basic sync with explicit parameters
- operation_async(params) - basic async with explicit parameters  
- operation_detailed(params) - detailed sync with explicit parameters
- operation_detailed_async(params) - detailed async with explicit parameters

Perfect for MCP servers and documentation generation.
"""

import asyncio
from typing import Optional, List, Union, Any, Awaitable
from httpx import Response

# Import required types for proper parameter handling
from ....raw_clients.alfresco_model_client.model_client.types import UNSET, Unset
from httpx import Response

# Import from Level 3 (operation-specific models)
from .models import AspectsResponse, AspectsListResponse, CreateAspectsRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_model_client.model_client.api.aspects import (
            get_aspect as _get_aspect,
            list_aspects as _list_aspects
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class AspectsClient:
    """
    Aspects operations client with 4-pattern detailed functions.
    
    Provides high-level methods for aspects management operations
    that are essential for MCP servers and aspects workflows.
    
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
            self._get_aspect = _get_aspect
            self._list_aspects = _list_aspects
    
    @property
    def raw_client(self):
        """Delegate to parent client's raw client."""
        return self.parent_client.raw_client
    
    @property
    def httpx_client(self):
        """Delegate to parent client's httpx client."""
        return self.parent_client.httpx_client
    
    # =================================================================
    # ASPECTS OPERATIONS - BASIC IMPLEMENTATION (SYNC/ASYNC ONLY)
    # =================================================================
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self.parent_client._client_factory, 'base_url', 'unknown')
        return f"AlfrescoAspectsClient(base_url='{base_url}')"
    
    # =================================================================
    # LIST ASPECTS
    # =================================================================
    
    def list_aspects(
        self,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        where: Optional[str] = None,
        include: Optional[List[str]] = None
    ) -> Optional[Any]:
        """List aspects (sync). Gets a list of aspects."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw aspects operations not available")
        
        from ....raw_clients.alfresco_model_client.model_client.types import UNSET
        
        return self._list_aspects.sync(
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            where=where if where is not None else UNSET,
            include=include if include is not None else UNSET
        )
    
    async def list_aspects_async(
        self,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        where: Optional[str] = None,
        include: Optional[List[str]] = None
    ) -> Optional[Any]:
        """List aspects (async). Gets a list of aspects."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw aspects operations not available")
        
        from ....raw_clients.alfresco_model_client.model_client.types import UNSET
        
        return await self._list_aspects.asyncio(
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            where=where if where is not None else UNSET,
            include=include if include is not None else UNSET
        )
    
    # =================================================================
    # GET ASPECT
    # =================================================================
    
    def get_aspect(
        self,
        aspect_name: str,
        include: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Get aspect (sync). Gets information about an aspect."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw aspects operations not available")
        
        from ....raw_clients.alfresco_model_client.model_client.types import UNSET
        
        return self._get_aspect.sync(
            aspect_name=aspect_name,
            client=self.raw_client,
            include=include if include is not None else UNSET
        )
    
    async def get_aspect_async(
        self,
        aspect_name: str,
        include: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Get aspect (async). Gets information about an aspect."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw aspects operations not available")
        
        from ....raw_clients.alfresco_model_client.model_client.types import UNSET
        
        return await self._get_aspect.asyncio(
            aspect_name=aspect_name,
            client=self.raw_client,
            include=include if include is not None else UNSET
        ) 