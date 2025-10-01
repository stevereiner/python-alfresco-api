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
    
    def __init__(self, parent_client):
        """Initialize with client factory for raw client access."""
        self.parent_client = parent_client
        self._raw_client = None
        
        # Store raw operation references
        if RAW_OPERATIONS_AVAILABLE:
            self._search = _search
    
    @property
    def raw_client(self):
        """Delegate to parent client's raw client."""
        return self.parent_client.raw_client
    
    @property
    def httpx_client(self):
        """Delegate to parent client's httpx client."""
        return self.parent_client.httpx_client
    
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
        
        return self._search.sync(client=self.raw_client, body=body)  # type: ignore
    
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
        
        return await self._search.asyncio(client=self.raw_client, body=body)  # type: ignore
    
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
        
        return self._search.sync_detailed(client=self.raw_client, body=body)  # type: ignore
    
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
        
        return await self._search.asyncio_detailed(client=self.raw_client, body=body)  # type: ignore

    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self.parent_client._client_factory, 'base_url', 'unknown')
        return f"SearchClient(base_url='{base_url}')" 