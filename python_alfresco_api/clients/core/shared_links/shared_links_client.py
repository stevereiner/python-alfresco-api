"""
Shared Links Operations Client - Level 3: Shared Links-Specific Operations

This module provides shared_links-specific operations within the Core API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.
"""

import asyncio
from typing import Optional, List, Union, Any
from httpx import Response

# Import from Level 3 (operation-specific models)
from .models import SharedLinksResponse, SharedLinksListResponse, CreateSharedLinksRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_core_client.core_client.api.shared_links import (
            create_shared_link as _create_shared_link,
            delete_shared_link as _delete_shared_link,
            email_shared_link as _email_shared_link,
            get_shared_link as _get_shared_link,
            get_shared_link_content as _get_shared_link_content,
            get_shared_link_rendition as _get_shared_link_rendition,
            get_shared_link_rendition_content as _get_shared_link_rendition_content,
            list_shared_links as _list_shared_links,
            list_shared_link_renditions as _list_shared_link_renditions
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class SharedLinksClient:
    """
    Shared Links operations client with 4-pattern detailed functions.
    
    Provides high-level methods for shared_links management operations
    that are essential for MCP servers and shared_links workflows.
    
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
            self._create_shared_link = _create_shared_link
            self._delete_shared_link = _delete_shared_link
            self._email_shared_link = _email_shared_link
            self._get_shared_link = _get_shared_link
            self._get_shared_link_content = _get_shared_link_content
            self._get_shared_link_rendition = _get_shared_link_rendition
            self._get_shared_link_rendition_content = _get_shared_link_rendition_content
            self._list_shared_links = _list_shared_links
            self._list_shared_link_renditions = _list_shared_link_renditions
    
    @property
    def raw_client(self):
        """Delegate to parent client's raw client."""
        return self.parent_client.raw_client
    
    @property
    def httpx_client(self):
        """Delegate to parent client's httpx client."""
        return self.parent_client.httpx_client
    
    # =================================================================
    # SHARED LINKS OPERATIONS - BASIC IMPLEMENTATION (SYNC/ASYNC ONLY)
    # =================================================================
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self.parent_client._client_factory, 'base_url', 'unknown')
        return f"AlfrescoSharedLinksClient(base_url='{base_url}')"
    
    # =================================================================
    # CREATE SHARED LINK
    # =================================================================
    
    def create_shared_link(
        self,
        node_id: str,
        expires_at: Optional[str] = None,
        include: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Create shared link (sync). Creates a shared link to a file."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw shared links operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.models.shared_link_body_create import SharedLinkBodyCreate
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        shared_link_body = SharedLinkBodyCreate(
            node_id=node_id,
            expires_at=expires_at
        )
        
        return self._create_shared_link.sync(
            client=self.raw_client,
            body=shared_link_body,
            include=include if include is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    async def create_shared_link_async(
        self,
        node_id: str,
        expires_at: Optional[str] = None,
        include: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Create shared link (async). Creates a shared link to a file."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw shared links operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.models.shared_link_body_create import SharedLinkBodyCreate
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        shared_link_body = SharedLinkBodyCreate(
            node_id=node_id,
            expires_at=expires_at
        )
        
        return await self._create_shared_link.asyncio(
            client=self.raw_client,
            body=shared_link_body,
            include=include if include is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    # =================================================================
    # GET SHARED LINK
    # =================================================================
    
    def get_shared_link(
        self,
        shared_id: str,
        include: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Get shared link (sync). Gets information about a shared link."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw shared links operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._get_shared_link.sync(
            shared_id=shared_id,
            client=self.raw_client,
            include=include if include is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    async def get_shared_link_async(
        self,
        shared_id: str,
        include: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Get shared link (async). Gets information about a shared link."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw shared links operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._get_shared_link.asyncio(
            shared_id=shared_id,
            client=self.raw_client,
            include=include if include is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    # =================================================================
    # LIST SHARED LINKS
    # =================================================================
    
    def list_shared_links(
        self,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        where: Optional[str] = None,
        include: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """List shared links (sync). Gets a list of shared links for the current user."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw shared links operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._list_shared_links.sync(
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            where=where if where is not None else UNSET,
            include=include if include is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    async def list_shared_links_async(
        self,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        where: Optional[str] = None,
        include: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """List shared links (async). Gets a list of shared links for the current user."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw shared links operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._list_shared_links.asyncio(
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            where=where if where is not None else UNSET,
            include=include if include is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    # =================================================================
    # DELETE SHARED LINK
    # =================================================================
    
    def delete_shared_link(
        self,
        shared_id: str
    ) -> Optional[Any]:
        """Delete shared link (sync). Deletes a shared link."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw shared links operations not available")
        
        return self._delete_shared_link.sync(
            shared_id=shared_id,
            client=self.raw_client
        )
    
    async def delete_shared_link_async(
        self,
        shared_id: str
    ) -> Optional[Any]:
        """Delete shared link (async). Deletes a shared link."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw shared links operations not available")
        
        return await self._delete_shared_link.asyncio(
            shared_id=shared_id,
            client=self.raw_client
        )
    
    # =================================================================
    # EMAIL SHARED LINK
    # =================================================================
    
    def email_shared_link(
        self,
        shared_id: str,
        recipient_emails: List[str],
        message: Optional[str] = None,
        locale: Optional[str] = None
    ) -> Optional[Any]:
        """Email shared link (sync). Sends an email notification about a shared link."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw shared links operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.models.shared_link_body_email import SharedLinkBodyEmail
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        email_body = SharedLinkBodyEmail(
            recipient_emails=recipient_emails,
            message=message,
            locale=locale
        )
        
        return self._email_shared_link.sync(
            shared_id=shared_id,
            client=self.raw_client,
            body=email_body
        )
    
    async def email_shared_link_async(
        self,
        shared_id: str,
        recipient_emails: List[str],
        message: Optional[str] = None,
        locale: Optional[str] = None
    ) -> Optional[Any]:
        """Email shared link (async). Sends an email notification about a shared link."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw shared links operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.models.shared_link_body_email import SharedLinkBodyEmail
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        email_body = SharedLinkBodyEmail(
            recipient_emails=recipient_emails,
            message=message,
            locale=locale
        )
        
        return await self._email_shared_link.asyncio(
            shared_id=shared_id,
            client=self.raw_client,
            body=email_body
        )
    
    # =================================================================
    # GET SHARED LINK RENDITION
    # =================================================================
    
    def get_shared_link_rendition(
        self,
        shared_id: str,
        rendition_id: str,
        attachment: Optional[bool] = None,
        if_modified_since: Optional[str] = None,
        range_: Optional[str] = None
    ) -> Optional[Any]:
        """Get shared link rendition (sync). Gets a rendition of a shared link."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw shared links operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._get_shared_link_rendition.sync(
            shared_id=shared_id,
            rendition_id=rendition_id,
            client=self.raw_client,
            attachment=attachment if attachment is not None else UNSET,
            if_modified_since=if_modified_since if if_modified_since is not None else UNSET,
            range_=range_ if range_ is not None else UNSET
        )
    
    async def get_shared_link_rendition_async(
        self,
        shared_id: str,
        rendition_id: str,
        attachment: Optional[bool] = None,
        if_modified_since: Optional[str] = None,
        range_: Optional[str] = None
    ) -> Optional[Any]:
        """Get shared link rendition (async). Gets a rendition of a shared link."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw shared links operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._get_shared_link_rendition.asyncio(
            shared_id=shared_id,
            rendition_id=rendition_id,
            client=self.raw_client,
            attachment=attachment if attachment is not None else UNSET,
            if_modified_since=if_modified_since if if_modified_since is not None else UNSET,
            range_=range_ if range_ is not None else UNSET
        )
    
    # =================================================================
    # LIST SHARED LINK RENDITIONS
    # =================================================================
    
    def list_shared_link_renditions(
        self,
        shared_id: str
    ) -> Optional[Any]:
        """List shared link renditions (sync). Gets a list of renditions for a shared link."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw shared links operations not available")
        
        return self._list_shared_link_renditions.sync(
            shared_id=shared_id,
            client=self.raw_client
        )
    
    async def list_shared_link_renditions_async(
        self,
        shared_id: str
    ) -> Optional[Any]:
        """List shared link renditions (async). Gets a list of renditions for a shared link."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw shared links operations not available")
        
        return await self._list_shared_link_renditions.asyncio(
            shared_id=shared_id,
            client=self.raw_client
        ) 