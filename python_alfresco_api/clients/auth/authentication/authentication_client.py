"""
Authentication Operations Client - Level 3: Authentication-Specific Operations

This module provides authentication-specific operations within the Auth API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.

Each operation provides 4 variants:
- operation(params) - basic sync with explicit parameters
- operation_async(params) - basic async with explicit parameters  
- operation_detailed(params) - detailed sync with explicit parameters
- operation_detailed_async(params) - detailed async with explicit parameters

Perfect for MCP servers and documentation generation.
"""

import asyncio
from typing import Optional, List, Union, Any, Awaitable
from httpx import Response

# Import required types for proper parameter handling
from ....raw_clients.alfresco_auth_client.auth_client.types import UNSET, Unset
from httpx import Response

# Import model types for proper parameter signatures
from ....raw_clients.alfresco_auth_client.auth_client.models.ticketbody import TicketBody
from ....raw_clients.alfresco_auth_client.auth_client.models.ticketentry import TicketEntry
from ....raw_clients.alfresco_auth_client.auth_client.models.validticketentry import ValidTicketEntry

# Import from Level 3 (operation-specific models)
from .models import AuthenticationResponse, AuthenticationListResponse, CreateAuthenticationRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_auth_client.auth_client.api.authentication import (
            create_ticket as _create_ticket,
            delete_ticket as _delete_ticket,
            validate_ticket as _validate_ticket
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class AuthenticationClient:
    """
    Authentication operations client with 4-pattern detailed functions.
    
    Provides high-level methods for authentication management operations
    that are essential for MCP servers and authentication workflows.
    
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
            self._create_ticket = _create_ticket
            self._delete_ticket = _delete_ticket
            self._validate_ticket = _validate_ticket
    
    def _get_raw_client(self):
        """Get or create the raw client."""
        if self._raw_client is None:
            # Import the raw auth client directly
            from ....raw_clients.alfresco_auth_client.auth_client.client import AuthenticatedClient
            
            # Create the raw client with same auth setup
            self._raw_client = AuthenticatedClient(
                base_url=f"{self._client_factory.base_url}/alfresco/api/-default-/public/authentication/versions/1",
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
    
    # Placeholder for authentication operations - will be populated from the original file
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self._client_factory, 'base_url', 'unknown')
        return f"AlfrescoAuthenticationClient(base_url='{base_url}')" 