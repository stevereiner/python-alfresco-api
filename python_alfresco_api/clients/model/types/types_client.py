"""
Types Operations Client - Level 3: Types-Specific Operations

This module provides types-specific operations within the Model API.
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
from .models import TypesResponse, TypesListResponse, CreateTypesRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_model_client.model_client.api.types import (
            get_type as _get_type,
            list_types as _list_types
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class TypesClient:
    """
    Types operations client with 4-pattern detailed functions.
    
    Provides high-level methods for types management operations
    that are essential for MCP servers and types workflows.
    
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
            self._get_type = _get_type
            self._list_types = _list_types
    
    @property
    def raw_client(self):
        """Delegate to parent client's raw client."""
        return self.parent_client.raw_client
    
    @property
    def httpx_client(self):
        """Delegate to parent client's httpx client."""
        return self.parent_client.httpx_client
    
    # =================================================================
    # TYPES OPERATIONS - BASIC IMPLEMENTATION (SYNC/ASYNC ONLY)
    # =================================================================
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self.parent_client._client_factory, 'base_url', 'unknown')
        return f"AlfrescoTypesClient(base_url='{base_url}')"
    
    # =================================================================
    # LIST TYPES
    # =================================================================
    
    def list_types(
        self,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        where: Optional[str] = None,
        include: Optional[List[str]] = None
    ) -> Optional[Any]:
        """List types (sync). Gets a list of types."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw types operations not available")
        
        from ....raw_clients.alfresco_model_client.model_client.types import UNSET
        
        return self._list_types.sync(
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            where=where if where is not None else UNSET,
            include=include if include is not None else UNSET
        )
    
    async def list_types_async(
        self,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        where: Optional[str] = None,
        include: Optional[List[str]] = None
    ) -> Optional[Any]:
        """List types (async). Gets a list of types."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw types operations not available")
        
        from ....raw_clients.alfresco_model_client.model_client.types import UNSET
        
        return await self._list_types.asyncio(
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            where=where if where is not None else UNSET,
            include=include if include is not None else UNSET
        )
    
    # =================================================================
    # GET TYPE
    # =================================================================
    
    def get_type(
        self,
        type_name: str,
        include: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Get type (sync). Gets information about a type."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw types operations not available")
        
        from ....raw_clients.alfresco_model_client.model_client.types import UNSET
        
        return self._get_type.sync(
            type_name=type_name,
            client=self.raw_client,
            include=include if include is not None else UNSET
        )
    
    async def get_type_async(
        self,
        type_name: str,
        include: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Get type (async). Gets information about a type."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw types operations not available")
        
        from ....raw_clients.alfresco_model_client.model_client.types import UNSET
        
        return await self._get_type.asyncio(
            type_name=type_name,
            client=self.raw_client,
            include=include if include is not None else UNSET
        ) 