"""
Audit Operations Client - Level 3: Audit-Specific Operations

This module provides audit-specific operations within the Core API.
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
from .models import AuditResponse, AuditListResponse, CreateAuditRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_core_client.core_client.api.audit import (
            delete_audit_entries_for_audit_app as _delete_audit_entries_for_audit_app,
            delete_audit_entry as _delete_audit_entry,
            get_audit_app as _get_audit_app,
            get_audit_entry as _get_audit_entry,
            list_audit_apps as _list_audit_apps,
            list_audit_entries_for_audit_app as _list_audit_entries_for_audit_app,
            list_audit_entries_for_node as _list_audit_entries_for_node,
            update_audit_app as _update_audit_app
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class AuditClient:
    """
    Audit operations client with 4-pattern detailed functions.
    
    Provides high-level methods for audit management operations
    that are essential for MCP servers and audit workflows.
    
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
            self._delete_audit_entries_for_audit_app = _delete_audit_entries_for_audit_app
            self._delete_audit_entry = _delete_audit_entry
            self._get_audit_app = _get_audit_app
            self._get_audit_entry = _get_audit_entry
            self._list_audit_apps = _list_audit_apps
            self._list_audit_entries_for_audit_app = _list_audit_entries_for_audit_app
            self._list_audit_entries_for_node = _list_audit_entries_for_node
            self._update_audit_app = _update_audit_app
    
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
    
    # Placeholder for audit operations - will be populated from the original file
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self._client_factory, 'base_url', 'unknown')
        return f"AlfrescoAuditClient(base_url='{base_url}')" 