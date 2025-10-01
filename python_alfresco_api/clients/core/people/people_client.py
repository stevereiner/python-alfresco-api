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
    
    def __init__(self, parent_client):
        """Initialize with client factory for raw client access."""
        self.parent_client = parent_client
        self._raw_client = None
        
        # Store raw operation references
        if RAW_OPERATIONS_AVAILABLE:
            self._create_person = _create_person
            self._get_person = _get_person
            self._list_people = _list_people
            self._request_password_reset = _request_password_reset
            self._reset_password = _reset_password
            self._update_person = _update_person
    
    @property
    def raw_client(self):
        """Delegate to parent client's raw client."""
        return self.parent_client.raw_client
    
    @property
    def httpx_client(self):
        """Delegate to parent client's httpx client."""
        return self.parent_client.httpx_client
    
    # =================================================================
    # PEOPLE OPERATIONS - 4-PATTERN IMPLEMENTATION
    # =================================================================
    
    def create_person(
        self,
        person_id: str,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Create person (sync). Creates a new person in the repository."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw people operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.models.person_body_create import PersonBodyCreate
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        person_body = PersonBodyCreate(
            id=person_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        
        return self._create_person.sync(
            client=self.raw_client,
            body=person_body,
            fields=fields if fields is not None else UNSET
        )
    
    async def create_person_async(
        self,
        person_id: str,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Create person (async). Creates a new person in the repository."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw people operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.models.person_body_create import PersonBodyCreate
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        person_body = PersonBodyCreate(
            id=person_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        
        return await self._create_person.asyncio(
            client=self.raw_client,
            body=person_body,
            fields=fields if fields is not None else UNSET
        )
    
    def get_person(
        self,
        person_id: str,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Get person details (sync). Gets details for a specific person."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw people operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._get_person.sync(
            person_id=person_id,
            client=self.raw_client,
            fields=fields if fields is not None else UNSET
        )
    
    async def get_person_async(
        self,
        person_id: str,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Get person details (async). Gets details for a specific person."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw people operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._get_person.asyncio(
            person_id=person_id,
            client=self.raw_client,
            fields=fields if fields is not None else UNSET
        )
    
    def list_people(
        self,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        order_by: Optional[List[str]] = None,
        include: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """List people (sync). Gets a list of people in the repository."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw people operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._list_people.sync(
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            order_by=order_by if order_by is not None else UNSET,
            include=include if include is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    async def list_people_async(
        self,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        order_by: Optional[List[str]] = None,
        include: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """List people (async). Gets a list of people in the repository."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw people operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._list_people.asyncio(
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            order_by=order_by if order_by is not None else UNSET,
            include=include if include is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    def update_person(
        self,
        person_id: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        email: Optional[str] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Update person (sync). Updates details for a specific person."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw people operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.models.person_body_update import PersonBodyUpdate
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        person_body = PersonBodyUpdate()
        if first_name is not None:
            person_body.first_name = first_name
        if last_name is not None:
            person_body.last_name = last_name
        if email is not None:
            person_body.email = email
        
        return self._update_person.sync(
            person_id=person_id,
            client=self.raw_client,
            body=person_body,
            fields=fields if fields is not None else UNSET
        )
    
    async def update_person_async(
        self,
        person_id: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        email: Optional[str] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Update person (async). Updates details for a specific person."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw people operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.models.person_body_update import PersonBodyUpdate
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        person_body = PersonBodyUpdate()
        if first_name is not None:
            person_body.first_name = first_name
        if last_name is not None:
            person_body.last_name = last_name
        if email is not None:
            person_body.email = email
        
        return await self._update_person.asyncio(
            person_id=person_id,
            client=self.raw_client,
            body=person_body,
            fields=fields if fields is not None else UNSET
        )
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self.parent_client._client_factory, 'base_url', 'unknown')
        return f"AlfrescoPeopleClient(base_url='{base_url}')" 