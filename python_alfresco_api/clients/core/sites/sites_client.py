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
    
    def __init__(self, parent_client):
        """Initialize with client factory for raw client access."""
        self.parent_client = parent_client
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
    
    @property
    def raw_client(self):
        """Delegate to parent client's raw client."""
        return self.parent_client.raw_client
    
    @property
    def httpx_client(self):
        """Delegate to parent client's httpx client."""
        return self.parent_client.httpx_client
    
    # =================================================================
    # SITES OPERATIONS - 4-PATTERN IMPLEMENTATION
    # =================================================================
    
    def create_site(
        self,
        site_id: str,
        title: str,
        description: Optional[str] = None,
        visibility: str = "PUBLIC",
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Create site (sync). Creates a new site."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw sites operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.models.site_body_create import SiteBodyCreate
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        site_body = SiteBodyCreate(
            id=site_id,
            title=title,
            description=description,
            visibility=visibility
        )
        
        return self._create_site.sync(
            client=self.raw_client,
            body=site_body,
            fields=fields if fields is not None else UNSET
        )
    
    async def create_site_async(
        self,
        site_id: str,
        title: str,
        description: Optional[str] = None,
        visibility: str = "PUBLIC",
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Create site (async). Creates a new site."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw sites operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.models.site_body_create import SiteBodyCreate
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        site_body = SiteBodyCreate(
            id=site_id,
            title=title,
            description=description,
            visibility=visibility
        )
        
        return await self._create_site.asyncio(
            client=self.raw_client,
            body=site_body,
            fields=fields if fields is not None else UNSET
        )
    
    def get_site(
        self,
        site_id: str,
        relations: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Get site details (sync). Gets details for a specific site."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw sites operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._get_site.sync(
            site_id=site_id,
            client=self.raw_client,
            relations=relations if relations is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    async def get_site_async(
        self,
        site_id: str,
        relations: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Get site details (async). Gets details for a specific site."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw sites operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._get_site.asyncio(
            site_id=site_id,
            client=self.raw_client,
            relations=relations if relations is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    def list_sites(
        self,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        order_by: Optional[List[str]] = None,
        relations: Optional[List[str]] = None,
        fields: Optional[List[str]] = None,
        where: Optional[str] = None
    ) -> Optional[Any]:
        """List sites (sync). Gets a list of sites."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw sites operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._list_sites.sync(
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            order_by=order_by if order_by is not None else UNSET,
            relations=relations if relations is not None else UNSET,
            fields=fields if fields is not None else UNSET,
            where=where if where is not None else UNSET
        )
    
    async def list_sites_async(
        self,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        order_by: Optional[List[str]] = None,
        relations: Optional[List[str]] = None,
        fields: Optional[List[str]] = None,
        where: Optional[str] = None
    ) -> Optional[Any]:
        """List sites (async). Gets a list of sites."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw sites operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._list_sites.asyncio(
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            order_by=order_by if order_by is not None else UNSET,
            relations=relations if relations is not None else UNSET,
            fields=fields if fields is not None else UNSET,
            where=where if where is not None else UNSET
        )
    
    def update_site(
        self,
        site_id: str,
        title: Optional[str] = None,
        description: Optional[str] = None,
        visibility: Optional[str] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Update site (sync). Updates details for a specific site."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw sites operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.models.site_body_update import SiteBodyUpdate
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        site_body = SiteBodyUpdate()
        if title is not None:
            site_body.title = title
        if description is not None:
            site_body.description = description
        if visibility is not None:
            site_body.visibility = visibility
        
        return self._update_site.sync(
            site_id=site_id,
            client=self.raw_client,
            body=site_body,
            fields=fields if fields is not None else UNSET
        )
    
    async def update_site_async(
        self,
        site_id: str,
        title: Optional[str] = None,
        description: Optional[str] = None,
        visibility: Optional[str] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Update site (async). Updates details for a specific site."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw sites operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.models.site_body_update import SiteBodyUpdate
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        site_body = SiteBodyUpdate()
        if title is not None:
            site_body.title = title
        if description is not None:
            site_body.description = description
        if visibility is not None:
            site_body.visibility = visibility
        
        return await self._update_site.asyncio(
            site_id=site_id,
            client=self.raw_client,
            body=site_body,
            fields=fields if fields is not None else UNSET
        )
    
    def delete_site(
        self,
        site_id: str,
        permanent: bool = False
    ) -> Optional[Any]:
        """Delete site (sync). Deletes a specific site."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw sites operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._delete_site.sync(
            site_id=site_id,
            client=self.raw_client,
            permanent=permanent if permanent is not None else UNSET
        )
    
    async def delete_site_async(
        self,
        site_id: str,
        permanent: bool = False
    ) -> Optional[Any]:
        """Delete site (async). Deletes a specific site."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw sites operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._delete_site.asyncio(
            site_id=site_id,
            client=self.raw_client,
            permanent=permanent if permanent is not None else UNSET
        )
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self.parent_client._client_factory, 'base_url', 'unknown')
        return f"AlfrescoSitesClient(base_url='{base_url}')" 