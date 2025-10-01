"""
Tags Operations Client - Level 3: Tags-Specific Operations

This module provides tags-specific operations within the Core API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.
"""

import asyncio
from typing import Optional, List, Union, Any
from httpx import Response

# Import from Level 3 (operation-specific models)
from .models import TagsResponse, TagsListResponse, CreateTagsRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_core_client.core_client.api.tags import (
            create_tag_for_node as _create_tag_for_node,
            delete_tag_from_node as _delete_tag_from_node,
            get_tag as _get_tag,
            list_tags as _list_tags,
            list_tags_for_node as _list_tags_for_node,
            update_tag as _update_tag
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class TagsClient:
    """
    Tags operations client with 4-pattern detailed functions.
    
    Provides high-level methods for tags management operations
    that are essential for MCP servers and tags workflows.
    
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
            self._create_tag_for_node = _create_tag_for_node
            self._delete_tag_from_node = _delete_tag_from_node
            self._get_tag = _get_tag
            self._list_tags = _list_tags
            self._list_tags_for_node = _list_tags_for_node
            self._update_tag = _update_tag
    
    @property
    def raw_client(self):
        """Delegate to parent client's raw client."""
        return self.parent_client.raw_client
    
    @property
    def httpx_client(self):
        """Delegate to parent client's httpx client."""
        return self.parent_client.httpx_client
    
    # =================================================================
    # TAGS OPERATIONS - BASIC IMPLEMENTATION (SYNC/ASYNC ONLY)
    # =================================================================
    
    def create_tag_for_node(
        self,
        node_id: str,
        tag: str,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Create tag for node (sync). Adds a tag to a node."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw tags operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.models.tag_body import TagBody
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        tag_body = TagBody(tag=tag)
        
        return self._create_tag_for_node.sync(
            node_id=node_id,
            client=self.raw_client,
            body=tag_body,
            fields=fields if fields is not None else UNSET
        )
    
    async def create_tag_for_node_async(
        self,
        node_id: str,
        tag: str,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Create tag for node (async). Adds a tag to a node."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw tags operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.models.tag_body import TagBody
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        tag_body = TagBody(tag=tag)
        
        return await self._create_tag_for_node.asyncio(
            node_id=node_id,
            client=self.raw_client,
            body=tag_body,
            fields=fields if fields is not None else UNSET
        )
    
    def delete_tag_from_node(
        self,
        node_id: str,
        tag_id: str
    ) -> Optional[Any]:
        """Delete tag from node (sync). Removes a tag from a node."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw tags operations not available")
        
        return self._delete_tag_from_node.sync(
            node_id=node_id,
            tag_id=tag_id,
            client=self.raw_client
        )
    
    async def delete_tag_from_node_async(
        self,
        node_id: str,
        tag_id: str
    ) -> Optional[Any]:
        """Delete tag from node (async). Removes a tag from a node."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw tags operations not available")
        
        return await self._delete_tag_from_node.asyncio(
            node_id=node_id,
            tag_id=tag_id,
            client=self.raw_client
        )
    
    def get_tag(
        self,
        tag_id: str,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Get tag details (sync). Gets details for a specific tag."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw tags operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._get_tag.sync(
            tag_id=tag_id,
            client=self.raw_client,
            fields=fields if fields is not None else UNSET
        )
    
    async def get_tag_async(
        self,
        tag_id: str,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Get tag details (async). Gets details for a specific tag."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw tags operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._get_tag.asyncio(
            tag_id=tag_id,
            client=self.raw_client,
            fields=fields if fields is not None else UNSET
        )
    
    def list_tags(
        self,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """List tags (sync). Gets a list of tags."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw tags operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._list_tags.sync(
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    async def list_tags_async(
        self,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """List tags (async). Gets a list of tags."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw tags operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._list_tags.asyncio(
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    def list_tags_for_node(
        self,
        node_id: str,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """List tags for node (sync). Gets a list of tags for a specific node."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw tags operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return self._list_tags_for_node.sync(
            node_id=node_id,
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    async def list_tags_for_node_async(
        self,
        node_id: str,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """List tags for node (async). Gets a list of tags for a specific node."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw tags operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        return await self._list_tags_for_node.asyncio(
            node_id=node_id,
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    def update_tag(
        self,
        tag_id: str,
        tag: str,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Update tag (sync). Updates details for a specific tag."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw tags operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.models.tag_body import TagBody
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        tag_body = TagBody(tag=tag)
        
        return self._update_tag.sync(
            tag_id=tag_id,
            client=self.raw_client,
            body=tag_body,
            fields=fields if fields is not None else UNSET
        )
    
    async def update_tag_async(
        self,
        tag_id: str,
        tag: str,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """Update tag (async). Updates details for a specific tag."""
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw tags operations not available")
        
        from ....raw_clients.alfresco_core_client.core_client.models.tag_body import TagBody
        from ....raw_clients.alfresco_core_client.core_client.types import UNSET
        
        tag_body = TagBody(tag=tag)
        
        return await self._update_tag.asyncio(
            tag_id=tag_id,
            client=self.raw_client,
            body=tag_body,
            fields=fields if fields is not None else UNSET
        )
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self.parent_client._client_factory, 'base_url', 'unknown')
        return f"AlfrescoTagsClient(base_url='{base_url}')" 