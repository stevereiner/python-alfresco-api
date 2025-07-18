"""
Trashcan Operations Client - Level 3: Trashcan-Specific Operations

This module provides trashcan-specific operations within the Core API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.
"""

import asyncio
from typing import Optional, List, Union, Any
from httpx import Response

# Import from Level 3 (operation-specific models)
from .models import TrashcanResponse, TrashcanListResponse, CreateTrashcanRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_core_client.core_client.api.trashcan import (
            delete_deleted_node as _delete_deleted_node,
            get_deleted_node as _get_deleted_node,
            get_deleted_node_content as _get_deleted_node_content,
            get_deleted_node_rendition as _get_deleted_node_rendition,
            get_deleted_node_rendition_content as _get_deleted_node_rendition_content,
            list_deleted_nodes as _list_deleted_nodes,
            list_deleted_node_renditions as _list_deleted_node_renditions,
            restore_deleted_node as _restore_deleted_node
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class TrashcanClient:
    """
    Trashcan operations client with 4-pattern detailed functions.
    
    Provides high-level methods for trashcan management operations
    that are essential for MCP servers and trashcan workflows.
    
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
            self._delete_deleted_node = _delete_deleted_node
            self._get_deleted_node = _get_deleted_node
            self._get_deleted_node_content = _get_deleted_node_content
            self._get_deleted_node_rendition = _get_deleted_node_rendition
            self._get_deleted_node_rendition_content = _get_deleted_node_rendition_content
            self._list_deleted_nodes = _list_deleted_nodes
            self._list_deleted_node_renditions = _list_deleted_node_renditions
            self._restore_deleted_node = _restore_deleted_node
    
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
    
    # Placeholder for trashcan operations - will be populated from the original file
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self._client_factory, 'base_url', 'unknown')
        return f"AlfrescoTrashcanClient(base_url='{base_url}')" 