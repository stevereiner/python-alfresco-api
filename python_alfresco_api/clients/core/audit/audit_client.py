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
    
    def __init__(self, parent_client):
        """Initialize with client factory for raw client access."""
        self.parent_client = parent_client
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
    
    @property
    def raw_client(self):
        """Delegate to parent client's raw client."""
        return self.parent_client.raw_client
    
    @property
    def httpx_client(self):
        """Delegate to parent client's httpx client."""
        return self.parent_client.httpx_client
    
    # =================================================================
    # AUDIT OPERATIONS - BASIC IMPLEMENTATION (SYNC/ASYNC ONLY)
    # =================================================================
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self.parent_client._client_factory, 'base_url', 'unknown')
        return f"AlfrescoAuditClient(base_url='{base_url}')"
    
    # =================================================================
    # LIST AUDIT APPS
    # =================================================================
    
    def list_audit_apps(
        self,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """List audit apps (sync). Gets a list of audit applications."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw audit operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._list_audit_apps.sync(
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    async def list_audit_apps_async(
        self,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """List audit apps (async). Gets a list of audit applications."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw audit operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._list_audit_apps.asyncio(
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    # =================================================================
    # GET AUDIT APP
    # =================================================================
    
    def get_audit_app(
        self,
        audit_app_id: str,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Get audit app (sync). Gets information about an audit application."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw audit operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._get_audit_app.sync(
            audit_app_id=audit_app_id,
            client=self.raw_client,
            fields=fields if fields is not None else UNSET
        )
    
    async def get_audit_app_async(
        self,
        audit_app_id: str,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Get audit app (async). Gets information about an audit application."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw audit operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._get_audit_app.asyncio(
            audit_app_id=audit_app_id,
            client=self.raw_client,
            fields=fields if fields is not None else UNSET
        )
    
    # =================================================================
    # UPDATE AUDIT APP
    # =================================================================
    
    def update_audit_app(
        self,
        audit_app_id: str,
        is_enabled: bool,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Update audit app (sync). Updates an audit application."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw audit operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.models.audit_app_body_update import AuditAppBodyUpdate
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        audit_app_body = AuditAppBodyUpdate(is_enabled=is_enabled)
        
        return self._update_audit_app.sync(
            audit_app_id=audit_app_id,
            client=self.raw_client,
            body=audit_app_body,
            fields=fields if fields is not None else UNSET
        )
    
    async def update_audit_app_async(
        self,
        audit_app_id: str,
        is_enabled: bool,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Update audit app (async). Updates an audit application."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw audit operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.models.audit_app_body_update import AuditAppBodyUpdate
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        audit_app_body = AuditAppBodyUpdate(is_enabled=is_enabled)
        
        return await self._update_audit_app.asyncio(
            audit_app_id=audit_app_id,
            client=self.raw_client,
            body=audit_app_body,
            fields=fields if fields is not None else UNSET
        )
    
    # =================================================================
    # LIST AUDIT ENTRIES FOR AUDIT APP
    # =================================================================
    
    def list_audit_entries_for_audit_app(
        self,
        audit_app_id: str,
        skip_count: Optional[int] = None,
        order_by: Optional[List[str]] = None,
        max_items: Optional[int] = None,
        where: Optional[str] = None,
        include: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """List audit entries for audit app (sync). Gets audit entries for an audit application."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw audit operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._list_audit_entries_for_audit_app.sync(
            audit_app_id=audit_app_id,
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            order_by=order_by if order_by is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            where=where if where is not None else UNSET,
            include=include if include is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    async def list_audit_entries_for_audit_app_async(
        self,
        audit_app_id: str,
        skip_count: Optional[int] = None,
        order_by: Optional[List[str]] = None,
        max_items: Optional[int] = None,
        where: Optional[str] = None,
        include: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """List audit entries for audit app (async). Gets audit entries for an audit application."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw audit operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._list_audit_entries_for_audit_app.asyncio(
            audit_app_id=audit_app_id,
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            order_by=order_by if order_by is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            where=where if where is not None else UNSET,
            include=include if include is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    # =================================================================
    # LIST AUDIT ENTRIES FOR NODE
    # =================================================================
    
    def list_audit_entries_for_node(
        self,
        node_id: str,
        skip_count: Optional[int] = None,
        order_by: Optional[List[str]] = None,
        max_items: Optional[int] = None,
        where: Optional[str] = None,
        include: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """List audit entries for node (sync). Gets audit entries for a node."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw audit operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._list_audit_entries_for_node.sync(
            node_id=node_id,
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            order_by=order_by if order_by is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            where=where if where is not None else UNSET,
            include=include if include is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    async def list_audit_entries_for_node_async(
        self,
        node_id: str,
        skip_count: Optional[int] = None,
        order_by: Optional[List[str]] = None,
        max_items: Optional[int] = None,
        where: Optional[str] = None,
        include: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """List audit entries for node (async). Gets audit entries for a node."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw audit operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._list_audit_entries_for_node.asyncio(
            node_id=node_id,
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            order_by=order_by if order_by is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            where=where if where is not None else UNSET,
            include=include if include is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    # =================================================================
    # GET AUDIT ENTRY
    # =================================================================
    
    def get_audit_entry(
        self,
        audit_app_id: str,
        audit_entry_id: str,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Get audit entry (sync). Gets information about an audit entry."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw audit operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._get_audit_entry.sync(
            audit_app_id=audit_app_id,
            audit_entry_id=audit_entry_id,
            client=self.raw_client,
            fields=fields if fields is not None else UNSET
        )
    
    async def get_audit_entry_async(
        self,
        audit_app_id: str,
        audit_entry_id: str,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Get audit entry (async). Gets information about an audit entry."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw audit operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._get_audit_entry.asyncio(
            audit_app_id=audit_app_id,
            audit_entry_id=audit_entry_id,
            client=self.raw_client,
            fields=fields if fields is not None else UNSET
        )
    
    # =================================================================
    # DELETE AUDIT ENTRY
    # =================================================================
    
    def delete_audit_entry(
        self,
        audit_app_id: str,
        audit_entry_id: str
    ) -> Optional[Any]:
        """Delete audit entry (sync). Deletes an audit entry."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw audit operations not available")
        
        return self._delete_audit_entry.sync(
            audit_app_id=audit_app_id,
            audit_entry_id=audit_entry_id,
            client=self.raw_client
        )
    
    async def delete_audit_entry_async(
        self,
        audit_app_id: str,
        audit_entry_id: str
    ) -> Optional[Any]:
        """Delete audit entry (async). Deletes an audit entry."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw audit operations not available")
        
        return await self._delete_audit_entry.asyncio(
            audit_app_id=audit_app_id,
            audit_entry_id=audit_entry_id,
            client=self.raw_client
        )
    
    # =================================================================
    # DELETE AUDIT ENTRIES FOR AUDIT APP
    # =================================================================
    
    def delete_audit_entries_for_audit_app(
        self,
        audit_app_id: str,
        where: Optional[str] = None
    ) -> Optional[Any]:
        """Delete audit entries for audit app (sync). Deletes audit entries for an audit application."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw audit operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._delete_audit_entries_for_audit_app.sync(
            audit_app_id=audit_app_id,
            client=self.raw_client,
            where=where if where is not None else UNSET
        )
    
    async def delete_audit_entries_for_audit_app_async(
        self,
        audit_app_id: str,
        where: Optional[str] = None
    ) -> Optional[Any]:
        """Delete audit entries for audit app (async). Deletes audit entries for an audit application."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw audit operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._delete_audit_entries_for_audit_app.asyncio(
            audit_app_id=audit_app_id,
            client=self.raw_client,
            where=where if where is not None else UNSET
        ) 