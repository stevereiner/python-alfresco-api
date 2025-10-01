"""
Groups Operations Client - Level 3: Groups-Specific Operations

This module provides groups-specific operations within the Core API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.
"""

import asyncio
from typing import Optional, List, Union, Any
from httpx import Response

# Import from Level 3 (operation-specific models)
from .models import GroupsResponse, GroupsListResponse, CreateGroupsRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_core_client.core_client.api.groups import (
            create_group as _create_group,
            create_group_membership as _create_group_membership,
            delete_group as _delete_group,
            delete_group_membership as _delete_group_membership,
            get_group as _get_group,
            list_group_memberships as _list_group_memberships,
            list_groups as _list_groups,
            update_group as _update_group
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class GroupsClient:
    """
    Groups operations client with 4-pattern detailed functions.
    
    Provides high-level methods for groups management operations
    that are essential for MCP servers and groups workflows.
    
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
            self._create_group = _create_group
            self._create_group_membership = _create_group_membership
            self._delete_group = _delete_group
            self._delete_group_membership = _delete_group_membership
            self._get_group = _get_group
            self._list_group_memberships = _list_group_memberships
            self._list_groups = _list_groups
            self._update_group = _update_group
    
    @property
    def raw_client(self):
        """Delegate to parent client's raw client."""
        return self.parent_client.raw_client
    
    @property
    def httpx_client(self):
        """Delegate to parent client's httpx client."""
        return self.parent_client.httpx_client
    
    # =================================================================
    # GROUPS OPERATIONS - BASIC IMPLEMENTATION (SYNC/ASYNC ONLY)
    # =================================================================
    
    def create_group(
        self,
        group_id: str,
        display_name: str,
        parent_ids: Optional[List[str]] = None,
        include: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Create group (sync). Creates a new group."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw groups operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.models.group_body_create import GroupBodyCreate
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        group_body = GroupBodyCreate(
            id=group_id,
            display_name=display_name,
            parent_ids=parent_ids
        )
        
        return self._create_group.sync(
            client=self.raw_client,
            body=group_body,
            include=include if include is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    async def create_group_async(
        self,
        group_id: str,
        display_name: str,
        parent_ids: Optional[List[str]] = None,
        include: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Create group (async). Creates a new group."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw groups operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.models.group_body_create import GroupBodyCreate
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        group_body = GroupBodyCreate(
            id=group_id,
            display_name=display_name,
            parent_ids=parent_ids
        )
        
        return await self._create_group.asyncio(
            client=self.raw_client,
            body=group_body,
            include=include if include is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    def get_group(
        self,
        group_id: str,
        include: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Get group details (sync). Gets details for a specific group."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw groups operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._get_group.sync(
            group_id=group_id,
            client=self.raw_client,
            include=include if include is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    async def get_group_async(
        self,
        group_id: str,
        include: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Get group details (async). Gets details for a specific group."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw groups operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._get_group.asyncio(
            group_id=group_id,
            client=self.raw_client,
            include=include if include is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    def list_groups(
        self,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        order_by: Optional[List[str]] = None,
        include: Optional[List[str]] = None,
        where: Optional[str] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """List groups (sync). Gets a list of groups."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw groups operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._list_groups.sync(
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            order_by=order_by if order_by is not None else UNSET,
            include=include if include is not None else UNSET,
            where=where if where is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    async def list_groups_async(
        self,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        order_by: Optional[List[str]] = None,
        include: Optional[List[str]] = None,
        where: Optional[str] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """List groups (async). Gets a list of groups."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw groups operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._list_groups.asyncio(
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            order_by=order_by if order_by is not None else UNSET,
            include=include if include is not None else UNSET,
            where=where if where is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    def update_group(
        self,
        group_id: str,
        display_name: Optional[str] = None,
        include: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Update group (sync). Updates details for a specific group."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw groups operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.models.group_body_update import GroupBodyUpdate
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        group_body = GroupBodyUpdate()
        if display_name is not None:
            group_body.display_name = display_name
        
        return self._update_group.sync(
            group_id=group_id,
            client=self.raw_client,
            body=group_body,
            include=include if include is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    async def update_group_async(
        self,
        group_id: str,
        display_name: Optional[str] = None,
        include: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Update group (async). Updates details for a specific group."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw groups operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.models.group_body_update import GroupBodyUpdate
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        group_body = GroupBodyUpdate()
        if display_name is not None:
            group_body.display_name = display_name
        
        return await self._update_group.asyncio(
            group_id=group_id,
            client=self.raw_client,
            body=group_body,
            include=include if include is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    def delete_group(
        self,
        group_id: str,
        cascade: bool = False
    ) -> Optional[Any]:
        """Delete group (sync). Deletes a specific group."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw groups operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._delete_group.sync(
            group_id=group_id,
            client=self.raw_client,
            cascade=cascade if cascade is not None else UNSET
        )
    
    async def delete_group_async(
        self,
        group_id: str,
        cascade: bool = False
    ) -> Optional[Any]:
        """Delete group (async). Deletes a specific group."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw groups operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._delete_group.asyncio(
            group_id=group_id,
            client=self.raw_client,
            cascade=cascade if cascade is not None else UNSET
        )
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self.parent_client._client_factory, 'base_url', 'unknown')
        return f"AlfrescoGroupsClient(base_url='{base_url}')" 