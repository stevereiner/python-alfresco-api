"""
Shared Links Operations Client - Level 3: Shared Links-Specific Operations

This module provides shared_links-specific operations within the Core API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.
"""

import asyncio
from typing import Optional, List, Union, Any
from httpx import Response

# Import from Level 3 (operation-specific models)
from .models import SharedLinksResponse, SharedLinksListResponse, CreateSharedLinksRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_core_client.core_client.api.shared_links import (
            create_shared_link as _create_shared_link,
            delete_shared_link as _delete_shared_link,
            email_shared_link as _email_shared_link,
            get_shared_link as _get_shared_link,
            get_shared_link_content as _get_shared_link_content,
            get_shared_link_rendition as _get_shared_link_rendition,
            get_shared_link_rendition_content as _get_shared_link_rendition_content,
            list_shared_links as _list_shared_links,
            list_shared_link_renditions as _list_shared_link_renditions
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class SharedLinksClient:
    """
    Shared Links operations client with 4-pattern detailed functions.
    
    Provides high-level methods for shared_links management operations
    that are essential for MCP servers and shared_links workflows.
    
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
            self._create_shared_link = _create_shared_link
            self._delete_shared_link = _delete_shared_link
            self._email_shared_link = _email_shared_link
            self._get_shared_link = _get_shared_link
            self._get_shared_link_content = _get_shared_link_content
            self._get_shared_link_rendition = _get_shared_link_rendition
            self._get_shared_link_rendition_content = _get_shared_link_rendition_content
            self._list_shared_links = _list_shared_links
            self._list_shared_link_renditions = _list_shared_link_renditions
    
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
    
    # Placeholder for shared_links operations - will be populated from the original file
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self._client_factory, 'base_url', 'unknown')
        return f"AlfrescoSharedLinksClient(base_url='{base_url}')" 