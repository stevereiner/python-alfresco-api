"""
Discovery Client Implementation - Clean Tier 3 Implementation

This module provides the actual DiscoveryClient implementation,
separate from the __init__.py import-only structure.
"""

import asyncio
from typing import Optional, List, Union, Any, Awaitable
from httpx import Response

# Import required types for proper parameter handling
from ....raw_clients.alfresco_discovery_client.discovery_client.types import UNSET, Unset
from httpx import Response

# Import model types for proper parameter signatures
from ....raw_clients.alfresco_discovery_client.discovery_client.models.discovery_entry import DiscoveryEntry

# Import from Level 3 (operation-specific models)
from .models import DiscoveryResponse, DiscoveryListResponse, CreateDiscoveryRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_discovery_client.discovery_client.api.discovery import (
            get_repository_information as _get_repository_information
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class DiscoveryClient:
    """
    Discovery client with 4-pattern detailed functions.
    
    Clean Tier 3 implementation with different name from AlfrescoDiscoveryClient.
    Provides high-level methods for discovery management operations
    that are essential for MCP servers and discovery workflows.
    
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
            self._get_repository_information = _get_repository_information
    
    @property
    def raw_client(self):
        """Delegate to parent client's raw client."""
        return self.parent_client.raw_client
    
    @property
    def httpx_client(self):
        """Delegate to parent client's httpx client."""
        return self.parent_client.httpx_client
    
    # ==================== 4-PATTERN OPERATIONS ====================

    # ==================== GET_REPOSITORY_INFORMATION OPERATION - Complete 4-Pattern ====================
    
    def get_repository_information(self) -> Any:
        """
        Get Repository Information operation (sync).
        
        Perfect for MCP servers and discovery workflows.
        Returns parsed response for common use cases.
        
        Args:
            No parameters
        
        Returns:
            Parsed response object
        """
        if not hasattr(self, '_get_repository_information'):
            raise ImportError("Raw client operation not available")
        
        return self._get_repository_information.sync(client=self.raw_client)
    
    async def get_repository_information_async(self) -> Any:
        """
        Get Repository Information operation (async).
        
        Perfect for MCP servers and discovery workflows.
        Returns parsed response for common use cases.
        
        Args:
            No parameters
        
        Returns:
            Parsed response object
        """
        if not hasattr(self, '_get_repository_information'):
            raise ImportError("Raw client operation not available")
        
        return await self._get_repository_information.asyncio(client=self.raw_client)
    
    def get_repository_information_detailed(self):
        """
        Get Repository Information operation (detailed sync).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        
        Args:
            No parameters
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        if not hasattr(self, '_get_repository_information'):
            raise ImportError("Raw client operation not available")
        
        return self._get_repository_information.sync_detailed(client=self.raw_client)
    
    async def get_repository_information_detailed_async(self):
        """
        Get Repository Information operation (detailed async).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        
        Args:
            No parameters
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        if not hasattr(self, '_get_repository_information'):
            raise ImportError("Raw client operation not available")
        
        return await self._get_repository_information.asyncio_detailed(client=self.raw_client)

    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self.parent_client._client_factory, 'base_url', 'unknown')
        return f"DiscoveryClient(base_url='{base_url}')" 