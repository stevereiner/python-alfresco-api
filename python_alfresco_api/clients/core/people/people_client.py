"""
People Operations Client - Level 3: People-Specific Operations

This module provides people-specific operations within the Core API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.
"""

import asyncio
from typing import Optional, List, Union, Any
from httpx import Response

# Import from Level 3 (operation-specific models)
from .models import PeopleResponse, PeopleListResponse, CreatePeopleRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_core_client.core_client.api.people import (
            create_person as _create_person,
            get_person as _get_person,
            list_people as _list_people,
            request_password_reset as _request_password_reset,
            reset_password as _reset_password,
            update_person as _update_person
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class PeopleClient:
    """
    People operations client with 4-pattern detailed functions.
    
    Provides high-level methods for people management operations
    that are essential for MCP servers and people workflows.
    
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
            self._create_person = _create_person
            self._get_person = _get_person
            self._list_people = _list_people
            self._request_password_reset = _request_password_reset
            self._reset_password = _reset_password
            self._update_person = _update_person
    
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
    
    # Placeholder for people operations - will be populated from the original file
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self._client_factory, 'base_url', 'unknown')
        return f"AlfrescoPeopleClient(base_url='{base_url}')" 