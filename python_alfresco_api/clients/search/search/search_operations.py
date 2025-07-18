"""
Search Client Implementation - Clean Tier 3 Implementation

This module provides the actual SearchClient implementation,
separate from the __init__.py import-only structure.
"""

import asyncio
from typing import Optional, List, Union, Any, Awaitable
from httpx import Response

# Import required types for proper parameter handling
from ....raw_clients.alfresco_search_client.search_client.types import UNSET, Unset
from httpx import Response

# Import model types for proper parameter signatures
from ....raw_clients.alfresco_search_client.search_client.models.result_set_paging import ResultSetPaging
from ....raw_clients.alfresco_search_client.search_client.models.search_request import SearchRequest

# Import from Level 3 (operation-specific models)
from .models import SearchResponse, SearchListResponse, CreateSearchRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_search_client.search_client.api.search import (
            search as _search
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class SearchClient:
    """
    Search client with 4-pattern detailed functions.
    
    Clean Tier 3 implementation with different name from AlfrescoSearchClient.
    Provides high-level methods for search management operations
    that are essential for MCP servers and search workflows.
    
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
            self._search = _search
    
    def _get_raw_client(self):
        """Get or create the raw client."""
        if self._raw_client is None:
            # Import the raw client directly
            from ....raw_clients.alfresco_search_client.search_client.client import AuthenticatedClient
            
            # Create the raw client with same auth setup as core client
            self._raw_client = AuthenticatedClient(
                base_url=f"{self._client_factory.base_url}/alfresco/api/-default-/public/search/versions/1",
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
    
    # ==================== 4-PATTERN OPERATIONS ====================

    # ==================== SEARCH OPERATION - Complete 4-Pattern ====================
    
    def search(self, body: Union[SearchRequest, Unset] = UNSET) -> Any:
        """
        Search operation (sync).
        
        Perfect for MCP servers and search workflows.
        Returns parsed response for common use cases.
        
        Args:
            body: Union[SearchRequest, Unset] = UNSET
        
        Returns:
            Parsed response object
        """
        if not hasattr(self, '_search'):
            raise ImportError("Raw client operation not available")
        
        return self._search.sync(client=self._get_raw_client(), body=body)  # type: ignore
    
    async def search_async(self, body: Union[SearchRequest, Unset] = UNSET) -> Any:
        """
        Search operation (async).
        
        Perfect for MCP servers and search workflows.
        Returns parsed response for common use cases.
        
        Args:
            body: Union[SearchRequest, Unset] = UNSET
        
        Returns:
            Parsed response object
        """
        if not hasattr(self, '_search'):
            raise ImportError("Raw client operation not available")
        
        return await self._search.asyncio(client=self._get_raw_client(), body=body)  # type: ignore
    
    def search_detailed(self, body: Union[SearchRequest, Unset] = UNSET):
        """
        Search operation (detailed sync).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        
        Args:
            body: Union[SearchRequest, Unset] = UNSET
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        if not hasattr(self, '_search'):
            raise ImportError("Raw client operation not available")
        
        return self._search.sync_detailed(client=self._get_raw_client(), body=body)  # type: ignore
    
    async def search_detailed_async(self, body: Union[SearchRequest, Unset] = UNSET):
        """
        Search operation (detailed async).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        
        Args:
            body: Union[SearchRequest, Unset] = UNSET
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        if not hasattr(self, '_search'):
            raise ImportError("Raw client operation not available")
        
        return await self._search.asyncio_detailed(client=self._get_raw_client(), body=body)  # type: ignore

    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self._client_factory, 'base_url', 'unknown')
        return f"SearchClient(base_url='{base_url}')" 