"""
Preferences Operations Client - Level 3: Preferences-Specific Operations

This module provides preferences-specific operations within the Core API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.
"""

import asyncio
from typing import Optional, List, Union, Any
from httpx import Response

# Import from Level 3 (operation-specific models)
from .models import PreferencesResponse, PreferencesListResponse, CreatePreferencesRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_core_client.core_client.api.preferences import (
            get_preference as _get_preference,
            list_preferences as _list_preferences
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class PreferencesClient:
    """
    Preferences operations client with 4-pattern detailed functions.
    
    Provides high-level methods for preferences management operations
    that are essential for MCP servers and preferences workflows.
    
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
            self._get_preference = _get_preference
            self._list_preferences = _list_preferences
    
    @property
    def raw_client(self):
        """Delegate to parent client's raw client."""
        return self.parent_client.raw_client
    
    @property
    def httpx_client(self):
        """Delegate to parent client's httpx client."""
        return self.parent_client.httpx_client
    
    # =================================================================
    # PREFERENCES OPERATIONS - BASIC IMPLEMENTATION (SYNC/ASYNC ONLY)
    # =================================================================
    
    def get_preference(
        self,
        person_id: str,
        preference_name: str,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Get preference (sync). Gets a specific preference for a person."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw preferences operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._get_preference.sync(
            person_id=person_id,
            preference_name=preference_name,
            client=self.raw_client,
            fields=fields if fields is not None else UNSET
        )
    
    async def get_preference_async(
        self,
        person_id: str,
        preference_name: str,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Get preference (async). Gets a specific preference for a person."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw preferences operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._get_preference.asyncio(
            person_id=person_id,
            preference_name=preference_name,
            client=self.raw_client,
            fields=fields if fields is not None else UNSET
        )
    
    def list_preferences(
        self,
        person_id: str,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """List preferences (sync). Gets a list of preferences for a person."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw preferences operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._list_preferences.sync(
            person_id=person_id,
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    async def list_preferences_async(
        self,
        person_id: str,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """List preferences (async). Gets a list of preferences for a person."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw preferences operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._list_preferences.asyncio(
            person_id=person_id,
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self.parent_client._client_factory, 'base_url', 'unknown')
        return f"AlfrescoPreferencesClient(base_url='{base_url}')" 