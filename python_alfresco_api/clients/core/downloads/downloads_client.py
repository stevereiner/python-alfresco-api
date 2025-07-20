"""
Downloads Operations Client - Level 3: Downloads-Specific Operations

This module provides downloads-specific operations within the Core API.
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
from .models import DownloadsResponse, DownloadsListResponse, CreateDownloadsRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_core_client.core_client.api.downloads import (
            cancel_download as _cancel_download,
            create_download as _create_download,
            get_download as _get_download
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class DownloadsClient:
    """
    Downloads operations client with 4-pattern detailed functions.
    
    Provides high-level methods for downloads management operations
    that are essential for MCP servers and downloads workflows.
    
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
            self._cancel_download = _cancel_download
            self._create_download = _create_download
            self._get_download = _get_download
    
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

    # ==================== CANCEL_DOWNLOAD OPERATION ====================
    
    def cancel_download(self, download_id: str) -> Any:
        """Cancel Download operation."""
        from ....raw_clients.alfresco_core_client.core_client.api.downloads import cancel_download
        return cancel_download.sync(client=self._get_raw_client(), download_id=download_id)
    
    async def cancel_download_async(self, download_id: str) -> Any:
        """Cancel Download operation (async)."""
        from ....raw_clients.alfresco_core_client.core_client.api.downloads import cancel_download
        return await cancel_download.asyncio(client=self._get_raw_client(), download_id=download_id)
    
    def cancel_download_detailed(self, download_id: str) -> Response:
        """Cancel Download operation (detailed)."""
        from ....raw_clients.alfresco_core_client.core_client.api.downloads import cancel_download
        return cancel_download.sync_detailed(client=self._get_raw_client(), download_id=download_id)
    
    async def cancel_download_detailed_async(self, download_id: str) -> Response:
        """Cancel Download operation (detailed, async)."""
        from ....raw_clients.alfresco_core_client.core_client.api.downloads import cancel_download
        return await cancel_download.asyncio_detailed(client=self._get_raw_client(), download_id=download_id)

    # ==================== CREATE_DOWNLOAD OPERATION ====================
    
    def create_download(self, body: Any, fields: Optional[List[str]] = None) -> Any:
        """Create Download operation."""
        from ....raw_clients.alfresco_core_client.core_client.api.downloads import create_download
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return create_download.sync(
            client=self._get_raw_client(), 
            body=body, 
            fields=fields if fields is not None else UNSET
        )
    
    async def create_download_async(self, body: Any, fields: Optional[List[str]] = None) -> Any:
        """Create Download operation (async)."""
        from ....raw_clients.alfresco_core_client.core_client.api.downloads import create_download
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return await create_download.asyncio(
            client=self._get_raw_client(), 
            body=body, 
            fields=fields if fields is not None else UNSET
        )
    
    def create_download_detailed(self, body: Any, fields: Optional[List[str]] = None) -> Response:
        """Create Download operation (detailed)."""
        from ....raw_clients.alfresco_core_client.core_client.api.downloads import create_download
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return create_download.sync_detailed(
            client=self._get_raw_client(), 
            body=body, 
            fields=fields if fields is not None else UNSET
        )
    
    async def create_download_detailed_async(self, body: Any, fields: Optional[List[str]] = None) -> Response:
        """Create Download operation (detailed, async)."""
        from ....raw_clients.alfresco_core_client.core_client.api.downloads import create_download
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return await create_download.asyncio_detailed(
            client=self._get_raw_client(), 
            body=body, 
            fields=fields if fields is not None else UNSET
        )

    # ==================== GET_DOWNLOAD OPERATION ====================
    
    def get_download(self, download_id: str, fields: Optional[List[str]] = None) -> Any:
        """Get Download operation."""
        from ....raw_clients.alfresco_core_client.core_client.api.downloads import get_download
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return get_download.sync(
            client=self._get_raw_client(), 
            download_id=download_id, 
            fields=fields if fields is not None else UNSET
        )
    
    async def get_download_async(self, download_id: str, fields: Optional[List[str]] = None) -> Any:
        """Get Download operation (async)."""
        from ....raw_clients.alfresco_core_client.core_client.api.downloads import get_download
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return await get_download.asyncio(
            client=self._get_raw_client(), 
            download_id=download_id, 
            fields=fields if fields is not None else UNSET
        )
    
    def get_download_detailed(self, download_id: str, fields: Optional[List[str]] = None) -> Response:
        """Get Download operation (detailed)."""
        from ....raw_clients.alfresco_core_client.core_client.api.downloads import get_download
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return get_download.sync_detailed(
            client=self._get_raw_client(), 
            download_id=download_id, 
            fields=fields if fields is not None else UNSET
        )
    
    async def get_download_detailed_async(self, download_id: str, fields: Optional[List[str]] = None) -> Response:
        """Get Download operation (detailed, async)."""
        from ....raw_clients.alfresco_core_client.core_client.api.downloads import get_download
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        return await get_download.asyncio_detailed(
            client=self._get_raw_client(), 
            download_id=download_id, 
            fields=fields if fields is not None else UNSET
        )

    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self._client_factory, 'base_url', 'unknown')
        return f"DownloadsClient(base_url='{base_url}')" 