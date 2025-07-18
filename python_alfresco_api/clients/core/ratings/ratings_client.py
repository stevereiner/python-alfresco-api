
"""
Ratings Operations Client - Level 3: Ratings-Specific Operations

This module provides ratings-specific operations within the Core API.
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
from .models import RatingsResponse, RatingsListResponse, CreateRatingsRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_core_client.core_client.api.ratings import (
            create_rating as _create_rating,
            delete_rating as _delete_rating,
            get_rating as _get_rating,
            list_ratings as _list_ratings
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class RatingsClient:
    """
    Ratings operations client with 4-pattern detailed functions.
    
    Provides high-level methods for ratings management operations
    that are essential for MCP servers and ratings workflows.
    
    Each operation has 4 variants for maximum flexibility:
    - Basic sync/async for simple use cases
    - Detailed sync/async for full HTTP response access
    """
    
    def __init__(self, client_factory):
        """Initialize with client factory for raw client access."""
        self._client_factory = client_factory
        self._raw_client = None
        
        # Store raw operation references
        if RAW_OPERATIONS_AVAILABLE:
            self._create_rating = _create_rating
            self._delete_rating = _delete_rating
            self._get_rating = _get_rating
            self._list_ratings = _list_ratings
    
    def _get_raw_client(self):
        """Get or create the raw client."""
        if self._raw_client is None:
            # Import the raw core client directly
            from ....raw_clients.alfresco_core_client.core_client.client import AuthenticatedClient
            
            # Create the raw client with same auth setup
            self._raw_client = AuthenticatedClient(
                base_url=f"{self._client_factory.base_url}/alfresco/api/-default-/public/alfresco/versions/1",
                token=self._client_factory.auth.get_auth_token(),
                prefix=self._client_factory.auth.get_auth_prefix(),
                verify_ssl=self._client_factory.verify_ssl
            )
        return self._raw_client
    
    def get_httpx_client(self):
        """
        Get direct access to raw httpx client for advanced operations.
        
        Perfect for MCP servers that need raw HTTP access.
        """
        return self._get_raw_client().get_httpx_client()

    # ==================== CREATE_RATING OPERATION ====================
    
    def create_rating(self, node_id: str, body: Any, fields: Optional[List[str]] = None) -> Any:
        """Create Rating operation."""
        from ....raw_clients.alfresco_core_client.core_client.api.ratings import create_rating
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return create_rating.sync(
            client=self._get_raw_client(),
            node_id=node_id,
            body=body,
            fields=fields if fields is not None else UNSET
        )
    
    async def create_rating_async(self, node_id: str, body: Any, fields: Optional[List[str]] = None) -> Any:
        """Create Rating operation (async)."""
        from ....raw_clients.alfresco_core_client.core_client.api.ratings import create_rating
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return await create_rating.asyncio(
            client=self._get_raw_client(),
            node_id=node_id,
            body=body,
            fields=fields if fields is not None else UNSET
        )
    
    def create_rating_detailed(self, node_id: str, body: Any, fields: Optional[List[str]] = None) -> Response:
        """Create Rating operation (detailed)."""
        from ....raw_clients.alfresco_core_client.core_client.api.ratings import create_rating
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return create_rating.sync_detailed(
            client=self._get_raw_client(),
            node_id=node_id,
            body=body,
            fields=fields if fields is not None else UNSET
        )
    
    async def create_rating_detailed_async(self, node_id: str, body: Any, fields: Optional[List[str]] = None) -> Response:
        """Create Rating operation (detailed, async)."""
        from ....raw_clients.alfresco_core_client.core_client.api.ratings import create_rating
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return await create_rating.asyncio_detailed(
            client=self._get_raw_client(),
            node_id=node_id,
            body=body,
            fields=fields if fields is not None else UNSET
        )

    # ==================== DELETE_RATING OPERATION ====================
    
    def delete_rating(self, node_id: str, rating_id: str) -> Any:
        """Delete Rating operation."""
        from ....raw_clients.alfresco_core_client.core_client.api.ratings import delete_rating
        return delete_rating.sync(client=self._get_raw_client(), node_id=node_id, rating_id=rating_id)
    
    async def delete_rating_async(self, node_id: str, rating_id: str) -> Any:
        """Delete Rating operation (async)."""
        from ....raw_clients.alfresco_core_client.core_client.api.ratings import delete_rating
        return await delete_rating.asyncio(client=self._get_raw_client(), node_id=node_id, rating_id=rating_id)
    
    def delete_rating_detailed(self, node_id: str, rating_id: str) -> Response:
        """Delete Rating operation (detailed)."""
        from ....raw_clients.alfresco_core_client.core_client.api.ratings import delete_rating
        return delete_rating.sync_detailed(client=self._get_raw_client(), node_id=node_id, rating_id=rating_id)
    
    async def delete_rating_detailed_async(self, node_id: str, rating_id: str) -> Response:
        """Delete Rating operation (detailed, async)."""
        from ....raw_clients.alfresco_core_client.core_client.api.ratings import delete_rating
        return await delete_rating.asyncio_detailed(client=self._get_raw_client(), node_id=node_id, rating_id=rating_id)

    # ==================== GET_RATING OPERATION ====================
    
    def get_rating(self, node_id: str, rating_id: str, fields: Optional[List[str]] = None) -> Any:
        """Get Rating operation."""
        from ....raw_clients.alfresco_core_client.core_client.api.ratings import get_rating
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return get_rating.sync(
            client=self._get_raw_client(),
            node_id=node_id,
            rating_id=rating_id,
            fields=fields if fields is not None else UNSET
        )
    
    async def get_rating_async(self, node_id: str, rating_id: str, fields: Optional[List[str]] = None) -> Any:
        """Get Rating operation (async)."""
        from ....raw_clients.alfresco_core_client.core_client.api.ratings import get_rating
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return await get_rating.asyncio(
            client=self._get_raw_client(),
            node_id=node_id,
            rating_id=rating_id,
            fields=fields if fields is not None else UNSET
        )
    
    def get_rating_detailed(self, node_id: str, rating_id: str, fields: Optional[List[str]] = None) -> Response:
        """Get Rating operation (detailed)."""
        from ....raw_clients.alfresco_core_client.core_client.api.ratings import get_rating
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return get_rating.sync_detailed(
            client=self._get_raw_client(),
            node_id=node_id,
            rating_id=rating_id,
            fields=fields if fields is not None else UNSET
        )
    
    async def get_rating_detailed_async(self, node_id: str, rating_id: str, fields: Optional[List[str]] = None) -> Response:
        """Get Rating operation (detailed, async)."""
        from ....raw_clients.alfresco_core_client.core_client.api.ratings import get_rating
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return await get_rating.asyncio_detailed(
            client=self._get_raw_client(),
            node_id=node_id,
            rating_id=rating_id,
            fields=fields if fields is not None else UNSET
        )

    # ==================== LIST_RATINGS OPERATION ====================
    
    def list_ratings(self, node_id: str, skip_count: Optional[int] = None, max_items: Optional[int] = None, 
                     fields: Optional[List[str]] = None) -> Any:
        """List Ratings operation."""
        from ....raw_clients.alfresco_core_client.core_client.api.ratings import list_ratings
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return list_ratings.sync(
            client=self._get_raw_client(),
            node_id=node_id,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    async def list_ratings_async(self, node_id: str, skip_count: Optional[int] = None, max_items: Optional[int] = None, 
                                fields: Optional[List[str]] = None) -> Any:
        """List Ratings operation (async)."""
        from ....raw_clients.alfresco_core_client.core_client.api.ratings import list_ratings
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return await list_ratings.asyncio(
            client=self._get_raw_client(),
            node_id=node_id,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    def list_ratings_detailed(self, node_id: str, skip_count: Optional[int] = None, max_items: Optional[int] = None, 
                             fields: Optional[List[str]] = None) -> Response:
        """List Ratings operation (detailed)."""
        from ....raw_clients.alfresco_core_client.core_client.api.ratings import list_ratings
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return list_ratings.sync_detailed(
            client=self._get_raw_client(),
            node_id=node_id,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    async def list_ratings_detailed_async(self, node_id: str, skip_count: Optional[int] = None, max_items: Optional[int] = None, 
                                         fields: Optional[List[str]] = None) -> Response:
        """List Ratings operation (detailed, async)."""
        from ....raw_clients.alfresco_core_client.core_client.api.ratings import list_ratings
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return await list_ratings.asyncio_detailed(
            client=self._get_raw_client(),
            node_id=node_id,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )

    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self._client_factory, 'base_url', 'unknown')
        return f"RatingsClient(base_url='{base_url}')" 