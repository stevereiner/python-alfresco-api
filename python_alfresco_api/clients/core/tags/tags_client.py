"""
Tags Operations Client - Level 3: Tags-Specific Operations

This module provides tags-specific operations within the Core API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.
"""

import asyncio
from typing import Optional, List, Union, Any
from httpx import Response

# Import from Level 3 (operation-specific models)
from .models import TagsResponse, TagsListResponse, CreateTagsRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_core_client.core_client.api.tags import (
            create_tag_for_node as _create_tag_for_node,
            delete_tag_from_node as _delete_tag_from_node,
            get_tag as _get_tag,
            list_tags as _list_tags,
            list_tags_for_node as _list_tags_for_node,
            update_tag as _update_tag
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class TagsClient:
    """
    Tags operations client with 4-pattern detailed functions.
    
    Provides high-level methods for tags management operations
    that are essential for MCP servers and tags workflows.
    
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
            self._create_tag_for_node = _create_tag_for_node
            self._delete_tag_from_node = _delete_tag_from_node
            self._get_tag = _get_tag
            self._list_tags = _list_tags
            self._list_tags_for_node = _list_tags_for_node
            self._update_tag = _update_tag
    
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
    
    # Placeholder for tags operations - will be populated from the original file
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self._client_factory, 'base_url', 'unknown')
        return f"AlfrescoTagsClient(base_url='{base_url}')" 