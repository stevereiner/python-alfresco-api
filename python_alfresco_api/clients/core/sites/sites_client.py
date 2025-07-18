"""
Sites Operations Client - Level 3: Sites-Specific Operations

This module provides sites-specific operations within the Core API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.
"""

import asyncio
from typing import Optional, List, Union, Any
from httpx import Response

# Import from Level 3 (operation-specific models)
from .models import SitesResponse, SitesListResponse, CreateSitesRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_core_client.core_client.api.sites import (
            approve_site_membership_request as _approve_site_membership_request,
            create_site as _create_site,
            create_site_membership as _create_site_membership,
            create_site_membership_request_for_person as _create_site_membership_request_for_person,
            delete_site as _delete_site,
            delete_site_membership as _delete_site_membership,
            delete_site_membership_request_for_person as _delete_site_membership_request_for_person,
            get_site as _get_site,
            get_site_container as _get_site_container,
            get_site_membership as _get_site_membership,
            get_site_membership_for_person as _get_site_membership_for_person,
            get_site_membership_request_for_person as _get_site_membership_request_for_person,
            list_site_containers as _list_site_containers,
            list_site_membership_requests_for_person as _list_site_membership_requests_for_person,
            list_site_memberships as _list_site_memberships,
            list_site_memberships_for_person as _list_site_memberships_for_person,
            list_sites as _list_sites,
            reject_site_membership_request as _reject_site_membership_request,
            update_site as _update_site,
            update_site_membership as _update_site_membership,
            update_site_membership_request_for_person as _update_site_membership_request_for_person
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class SitesClient:
    """
    Sites operations client with 4-pattern detailed functions.
    
    Provides high-level methods for sites management operations
    that are essential for MCP servers and sites workflows.
    
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
            self._approve_site_membership_request = _approve_site_membership_request
            self._create_site = _create_site
            self._create_site_membership = _create_site_membership
            self._create_site_membership_request_for_person = _create_site_membership_request_for_person
            self._delete_site = _delete_site
            self._delete_site_membership = _delete_site_membership
            self._delete_site_membership_request_for_person = _delete_site_membership_request_for_person
            self._get_site = _get_site
            self._get_site_container = _get_site_container
            self._get_site_membership = _get_site_membership
            self._get_site_membership_for_person = _get_site_membership_for_person
            self._get_site_membership_request_for_person = _get_site_membership_request_for_person
            self._list_site_containers = _list_site_containers
            self._list_site_membership_requests_for_person = _list_site_membership_requests_for_person
            self._list_site_memberships = _list_site_memberships
            self._list_site_memberships_for_person = _list_site_memberships_for_person
            self._list_sites = _list_sites
            self._reject_site_membership_request = _reject_site_membership_request
            self._update_site = _update_site
            self._update_site_membership = _update_site_membership
            self._update_site_membership_request_for_person = _update_site_membership_request_for_person
    
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
    
    # Placeholder for sites operations - will be populated from the original file
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self._client_factory, 'base_url', 'unknown')
        return f"AlfrescoSitesClient(base_url='{base_url}')" 