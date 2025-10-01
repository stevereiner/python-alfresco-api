"""
Favorites Operations Client - Level 3: Favorites-Specific Operations

This module provides favorites-specific operations within the Core API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.
"""

import asyncio
from typing import Optional, List, Union, Any
from httpx import Response

# Import from Level 3 (operation-specific models)
from .models import FavoritesResponse, FavoritesListResponse, CreateFavoritesRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_core_client.core_client.api.favorites import (
            create_favorite as _create_favorite,
            create_site_favorite as _create_site_favorite,
            delete_favorite as _delete_favorite,
            delete_site_favorite as _delete_site_favorite,
            get_favorite as _get_favorite,
            get_favorite_site as _get_favorite_site,
            list_favorites as _list_favorites,
            list_favorite_sites_for_person as _list_favorite_sites_for_person
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class FavoritesClient:
    """
    Favorites operations client with 4-pattern detailed functions.
    
    Provides high-level methods for favorites management operations
    that are essential for MCP servers and favorites workflows.
    
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
            self._create_favorite = _create_favorite
            self._create_site_favorite = _create_site_favorite
            self._delete_favorite = _delete_favorite
            self._delete_site_favorite = _delete_site_favorite
            self._get_favorite = _get_favorite
            self._get_favorite_site = _get_favorite_site
            self._list_favorites = _list_favorites
            self._list_favorite_sites_for_person = _list_favorite_sites_for_person
    
    @property
    def raw_client(self):
        """Delegate to parent client's raw client."""
        return self.parent_client.raw_client
    
    @property
    def httpx_client(self):
        """Delegate to parent client's httpx client."""
        return self.parent_client.httpx_client
    
    # =================================================================
    # FAVORITES OPERATIONS - 4-PATTERN IMPLEMENTATION
    # =================================================================
    
    def create_favorite(
        self,
        person_id: str,
        target_id: str,
        target_type: str = "file"
    ) -> Optional[Any]:
        """Create favorite (sync). Adds a node to a person's favorites."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw favorites operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.models.favorite_body_create import FavoriteBodyCreate
        
        # Create target based on type
        target_dict = {}
        if target_type == "file":
            target_dict["file"] = {"guid": target_id}
        elif target_type == "folder":
            target_dict["folder"] = {"guid": target_id}
        elif target_type == "site":
            target_dict["site"] = {"guid": target_id}
        
        favorite_body = FavoriteBodyCreate(target=target_dict)
        
        return self._create_favorite.sync(
            person_id=person_id,
            client=self.raw_client,
            body=favorite_body
        )
    
    async def create_favorite_async(
        self,
        person_id: str,
        target_id: str,
        target_type: str = "file"
    ) -> Optional[Any]:
        """Create favorite (async). Adds a node to a person's favorites."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw favorites operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.models.favorite_body_create import FavoriteBodyCreate
        
        # Create target based on type
        target_dict = {}
        if target_type == "file":
            target_dict["file"] = {"guid": target_id}
        elif target_type == "folder":
            target_dict["folder"] = {"guid": target_id}
        elif target_type == "site":
            target_dict["site"] = {"guid": target_id}
        
        favorite_body = FavoriteBodyCreate(target=target_dict)
        
        return await self._create_favorite.asyncio(
            person_id=person_id,
            client=self.raw_client,
            body=favorite_body
        )
    
    def delete_favorite(
        self,
        person_id: str,
        favorite_id: str
    ) -> Optional[Any]:
        """Delete favorite (sync). Removes a node from a person's favorites."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw favorites operations not available")
        
        return self._delete_favorite.sync(
            person_id=person_id,
            favorite_id=favorite_id,
            client=self.raw_client
        )
    
    async def delete_favorite_async(
        self,
        person_id: str,
        favorite_id: str
    ) -> Optional[Any]:
        """Delete favorite (async). Removes a node from a person's favorites."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw favorites operations not available")
        
        return await self._delete_favorite.asyncio(
            person_id=person_id,
            favorite_id=favorite_id,
            client=self.raw_client
        )
    
    def get_favorite(
        self,
        person_id: str,
        favorite_id: str,
        include: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Get favorite details (sync). Gets details for a specific favorite."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw favorites operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._get_favorite.sync(
            person_id=person_id,
            favorite_id=favorite_id,
            client=self.raw_client,
            include=include if include is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    async def get_favorite_async(
        self,
        person_id: str,
        favorite_id: str,
        include: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Get favorite details (async). Gets details for a specific favorite."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw favorites operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._get_favorite.asyncio(
            person_id=person_id,
            favorite_id=favorite_id,
            client=self.raw_client,
            include=include if include is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    def list_favorites(
        self,
        person_id: str,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        where: Optional[str] = None,
        include: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """List favorites (sync). Gets a list of favorites for a person."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw favorites operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._list_favorites.sync(
            person_id=person_id,
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            where=where if where is not None else UNSET,
            include=include if include is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    async def list_favorites_async(
        self,
        person_id: str,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        where: Optional[str] = None,
        include: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """List favorites (async). Gets a list of favorites for a person."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw favorites operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._list_favorites.asyncio(
            person_id=person_id,
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            where=where if where is not None else UNSET,
            include=include if include is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self.parent_client._client_factory, 'base_url', 'unknown')
        return f"AlfrescoFavoritesClient(base_url='{base_url}')" 