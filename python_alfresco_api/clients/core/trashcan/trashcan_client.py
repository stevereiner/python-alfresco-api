"""
Trashcan Operations Client - Level 3: Trashcan-Specific Operations

This module provides trashcan-specific operations within the Core API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.
"""

import asyncio
from typing import Optional, List, Union, Any
from httpx import Response

# Import from Level 3 (operation-specific models)
from .models import TrashcanResponse, TrashcanListResponse, CreateTrashcanRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_core_client.core_client.api.trashcan import (
            delete_deleted_node as _delete_deleted_node,
            get_deleted_node as _get_deleted_node,
            get_deleted_node_content as _get_deleted_node_content,
            get_deleted_node_rendition as _get_deleted_node_rendition,
            get_deleted_node_rendition_content as _get_deleted_node_rendition_content,
            list_deleted_nodes as _list_deleted_nodes,
            list_deleted_node_renditions as _list_deleted_node_renditions,
            restore_deleted_node as _restore_deleted_node
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class TrashcanClient:
    """
    Trashcan operations client with 4-pattern detailed functions.
    
    Provides high-level methods for trashcan management operations
    that are essential for MCP servers and trashcan workflows.
    
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
            self._delete_deleted_node = _delete_deleted_node
            self._get_deleted_node = _get_deleted_node
            self._get_deleted_node_content = _get_deleted_node_content
            self._get_deleted_node_rendition = _get_deleted_node_rendition
            self._get_deleted_node_rendition_content = _get_deleted_node_rendition_content
            self._list_deleted_nodes = _list_deleted_nodes
            self._list_deleted_node_renditions = _list_deleted_node_renditions
            self._restore_deleted_node = _restore_deleted_node
    
    @property
    def raw_client(self):
        """Delegate to parent client's raw client."""
        return self.parent_client.raw_client
    
    @property
    def httpx_client(self):
        """Delegate to parent client's httpx client."""
        return self.parent_client.httpx_client
    
    # =================================================================
    # TRASHCAN OPERATIONS - BASIC IMPLEMENTATION (SYNC/ASYNC ONLY)
    # =================================================================
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self.parent_client._client_factory, 'base_url', 'unknown')
        return f"AlfrescoTrashcanClient(base_url='{base_url}')"
    
    # =================================================================
    # LIST DELETED NODES
    # =================================================================
    
    def list_deleted_nodes(
        self,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        include: Optional[List[str]] = None
    ) -> Optional[Any]:
        """List deleted nodes (sync). Gets a list of deleted nodes for the current user."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw trashcan operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._list_deleted_nodes.sync(
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            include=include if include is not None else UNSET
        )
    
    async def list_deleted_nodes_async(
        self,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        include: Optional[List[str]] = None
    ) -> Optional[Any]:
        """List deleted nodes (async). Gets a list of deleted nodes for the current user."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw trashcan operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._list_deleted_nodes.asyncio(
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            include=include if include is not None else UNSET
        )
    
    # =================================================================
    # GET DELETED NODE
    # =================================================================
    
    def get_deleted_node(
        self,
        deleted_node_id: str,
        include: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Get deleted node (sync). Gets information about a deleted node."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw trashcan operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._get_deleted_node.sync(
            deleted_node_id=deleted_node_id,
            client=self.raw_client,
            include=include if include is not None else UNSET
        )
    
    async def get_deleted_node_async(
        self,
        deleted_node_id: str,
        include: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Get deleted node (async). Gets information about a deleted node."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw trashcan operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._get_deleted_node.asyncio(
            deleted_node_id=deleted_node_id,
            client=self.raw_client,
            include=include if include is not None else UNSET
        )
    
    # =================================================================
    # RESTORE DELETED NODE
    # =================================================================
    
    def restore_deleted_node(
        self,
        deleted_node_id: str,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Restore deleted node (sync). Restores a deleted node."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw trashcan operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._restore_deleted_node.sync(
            deleted_node_id=deleted_node_id,
            client=self.raw_client,
            fields=fields if fields is not None else UNSET
        )
    
    async def restore_deleted_node_async(
        self,
        deleted_node_id: str,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Restore deleted node (async). Restores a deleted node."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw trashcan operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._restore_deleted_node.asyncio(
            deleted_node_id=deleted_node_id,
            client=self.raw_client,
            fields=fields if fields is not None else UNSET
        )
    
    # =================================================================
    # DELETE DELETED NODE (PERMANENT DELETE)
    # =================================================================
    
    def delete_deleted_node(
        self,
        deleted_node_id: str
    ) -> Optional[Any]:
        """Delete deleted node (sync). Permanently deletes a deleted node."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw trashcan operations not available")
        
        return self._delete_deleted_node.sync(
            deleted_node_id=deleted_node_id,
            client=self.raw_client
        )
    
    async def delete_deleted_node_async(
        self,
        deleted_node_id: str
    ) -> Optional[Any]:
        """Delete deleted node (async). Permanently deletes a deleted node."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw trashcan operations not available")
        
        return await self._delete_deleted_node.asyncio(
            deleted_node_id=deleted_node_id,
            client=self.raw_client
        )
    
    # =================================================================
    # GET ARCHIVED NODE RENDITION
    # =================================================================
    
    def get_archived_node_rendition(
        self,
        deleted_node_id: str,
        rendition_id: str,
        attachment: Optional[bool] = None,
        if_modified_since: Optional[str] = None,
        range_: Optional[str] = None
    ) -> Optional[Any]:
        """Get archived node rendition (sync). Gets a rendition of a deleted node."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw trashcan operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._get_archived_node_rendition.sync(
            deleted_node_id=deleted_node_id,
            rendition_id=rendition_id,
            client=self.raw_client,
            attachment=attachment if attachment is not None else UNSET,
            if_modified_since=if_modified_since if if_modified_since is not None else UNSET,
            range_=range_ if range_ is not None else UNSET
        )
    
    async def get_archived_node_rendition_async(
        self,
        deleted_node_id: str,
        rendition_id: str,
        attachment: Optional[bool] = None,
        if_modified_since: Optional[str] = None,
        range_: Optional[str] = None
    ) -> Optional[Any]:
        """Get archived node rendition (async). Gets a rendition of a deleted node."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw trashcan operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._get_archived_node_rendition.asyncio(
            deleted_node_id=deleted_node_id,
            rendition_id=rendition_id,
            client=self.raw_client,
            attachment=attachment if attachment is not None else UNSET,
            if_modified_since=if_modified_since if if_modified_since is not None else UNSET,
            range_=range_ if range_ is not None else UNSET
        )
    
    # =================================================================
    # LIST DELETED NODE RENDITIONS
    # =================================================================
    
    def list_deleted_node_renditions(
        self,
        deleted_node_id: str
    ) -> Optional[Any]:
        """List deleted node renditions (sync). Gets a list of renditions for a deleted node."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw trashcan operations not available")
        
        return self._list_deleted_node_renditions.sync(
            deleted_node_id=deleted_node_id,
            client=self.raw_client
        )
    
    async def list_deleted_node_renditions_async(
        self,
        deleted_node_id: str
    ) -> Optional[Any]:
        """List deleted node renditions (async). Gets a list of renditions for a deleted node."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw trashcan operations not available")
        
        return await self._list_deleted_node_renditions.asyncio(
            deleted_node_id=deleted_node_id,
            client=self.raw_client
        ) 