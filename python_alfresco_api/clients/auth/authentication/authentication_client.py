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
from ....raw_clients.alfresco_auth_client.auth_client.models.ticket_body import TicketBody
from ....raw_clients.alfresco_auth_client.auth_client.models.ticket_entry import TicketEntry
from ....raw_clients.alfresco_auth_client.auth_client.models.valid_ticket_entry import ValidTicketEntry

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
    
    def __init__(self, parent_client):
        """Initialize with client factory for raw client access."""
        self.parent_client = parent_client
        self._raw_client = None
        
        # Store raw operation references
        if RAW_OPERATIONS_AVAILABLE:
            self._create_ticket = _create_ticket
            self._delete_ticket = _delete_ticket
            self._validate_ticket = _validate_ticket
    
    @property
    def raw_client(self):
        """Delegate to parent client's raw client."""
        return self.parent_client.raw_client
    
    @property
    def httpx_client(self):
        """Delegate to parent client's httpx client."""
        return self.parent_client.httpx_client
    
    # =================================================================
    # AUTHENTICATION OPERATIONS - 4-PATTERN IMPLEMENTATION
    # =================================================================
    
    def create_ticket(
        self,
        username: str,
        password: str
    ) -> Optional[Any]:
        """
        Create authentication ticket (sync).
        
        Creates a new authentication ticket for the given credentials.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw authentication operations not available")
        
        from ....raw_clients.alfresco_auth_client.auth_client.models.ticket_body import TicketBody
        
        ticket_body = TicketBody(user_id=username, password=password)
        
        return self._create_ticket.sync(
            client=self.raw_client,
            body=ticket_body
        )
    
    async def create_ticket_async(
        self,
        username: str,
        password: str
    ) -> Optional[Any]:
        """
        Create authentication ticket (async).
        
        Creates a new authentication ticket for the given credentials.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw authentication operations not available")
        
        from ....raw_clients.alfresco_auth_client.auth_client.models.ticket_body import TicketBody
        
        ticket_body = TicketBody(user_id=username, password=password)
        
        return await self._create_ticket.asyncio(
            client=self.raw_client,
            body=ticket_body
        )
    
    def create_ticket_detailed(
        self,
        username: str,
        password: str
    ) -> Response:
        """
        Create authentication ticket (detailed sync).
        
        Creates a new authentication ticket with full HTTP response.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw authentication operations not available")
        
        from ....raw_clients.alfresco_auth_client.auth_client.models.ticket_body import TicketBody
        
        ticket_body = TicketBody(user_id=username, password=password)
        
        return self._create_ticket.sync_detailed(
            client=self.raw_client,
            body=ticket_body
        )
    
    async def create_ticket_detailed_async(
        self,
        username: str,
        password: str
    ) -> Response:
        """
        Create authentication ticket (detailed async).
        
        Creates a new authentication ticket with full HTTP response.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw authentication operations not available")
        
        from ....raw_clients.alfresco_auth_client.auth_client.models.ticket_body import TicketBody
        
        ticket_body = TicketBody(user_id=username, password=password)
        
        return await self._create_ticket.asyncio_detailed(
            client=self.raw_client,
            body=ticket_body
        )
    
    def validate_ticket(self) -> Optional[Any]:
        """
        Validate current authentication ticket (sync).
        
        Validates the current authentication ticket.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw authentication operations not available")
        
        return self._validate_ticket.sync(
            client=self.raw_client
        )
    
    async def validate_ticket_async(self) -> Optional[Any]:
        """
        Validate current authentication ticket (async).
        
        Validates the current authentication ticket.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw authentication operations not available")
        
        return await self._validate_ticket.asyncio(
            client=self.raw_client
        )
    
    def validate_ticket_detailed(self) -> Response:
        """
        Validate current authentication ticket (detailed sync).
        
        Validates the current authentication ticket with full HTTP response.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw authentication operations not available")
        
        return self._validate_ticket.sync_detailed(
            client=self.raw_client
        )
    
    async def validate_ticket_detailed_async(self) -> Response:
        """
        Validate current authentication ticket (detailed async).
        
        Validates the current authentication ticket with full HTTP response.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw authentication operations not available")
        
        return await self._validate_ticket.asyncio_detailed(
            client=self.raw_client
        )
    
    def delete_ticket(self) -> Optional[Any]:
        """
        Delete current authentication ticket (sync).
        
        Deletes/invalidates the current authentication ticket.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw authentication operations not available")
        
        return self._delete_ticket.sync(
            client=self.raw_client
        )
    
    async def delete_ticket_async(self) -> Optional[Any]:
        """
        Delete current authentication ticket (async).
        
        Deletes/invalidates the current authentication ticket.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw authentication operations not available")
        
        return await self._delete_ticket.asyncio(
            client=self.raw_client
        )
    
    def delete_ticket_detailed(self) -> Response:
        """
        Delete current authentication ticket (detailed sync).
        
        Deletes/invalidates the current authentication ticket with full HTTP response.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw authentication operations not available")
        
        return self._delete_ticket.sync_detailed(
            client=self.raw_client
        )
    
    async def delete_ticket_detailed_async(self) -> Response:
        """
        Delete current authentication ticket (detailed async).
        
        Deletes/invalidates the current authentication ticket with full HTTP response.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw authentication operations not available")
        
        return await self._delete_ticket.asyncio_detailed(
            client=self.raw_client
        )
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self.parent_client._client_factory, 'base_url', 'unknown')
        return f"AlfrescoAuthenticationClient(base_url='{base_url}')" 