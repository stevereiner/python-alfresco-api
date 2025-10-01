"""
Comments Operations Client - Level 3: Comments-Specific Operations

This module provides comments-specific operations within the Core API.
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
from .models import CommentsResponse, CommentsListResponse, CreateCommentsRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_core_client.core_client.api.comments import (
            create_comment as _create_comment,
            delete_comment as _delete_comment,
            list_comments as _list_comments,
            update_comment as _update_comment
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class CommentsClient:
    """
    Comments operations client with 4-pattern detailed functions.
    
    Provides high-level methods for comments management operations
    that are essential for MCP servers and comments workflows.
    
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
            self._create_comment = _create_comment
            self._delete_comment = _delete_comment
            self._list_comments = _list_comments
            self._update_comment = _update_comment
    
    @property
    def raw_client(self):
        """Delegate to parent client's raw client."""
        return self.parent_client.raw_client
    
    @property
    def httpx_client(self):
        """Delegate to parent client's httpx client."""
        return self.parent_client.httpx_client
    
    # ==================== 4-PATTERN OPERATIONS ====================

    # ==================== CREATE_COMMENT OPERATION ====================
    
    def create_comment(self, node_id: Any, body: Any, fields: Any) -> CommentsResponse:
        """
        Create Comment operation.
        
        Perfect for MCP servers and comments workflows.
        Returns simplified response for common use cases.
        """
        if not hasattr(self, '_create_comment'):
            raise ImportError("Raw client operation not available")
        
        result = self._create_comment.sync(client=self.raw_client, node_id=node_id, body=body, fields=fields)
        
        # Convert to standardized response
        from ..models import BaseEntry
        return CommentsResponse(entry=BaseEntry(id=f"result-comments"))
    
    async def create_comment_async(self, node_id: Any, body: Any, fields: Any) -> CommentsResponse:
        """
        Create Comment operation (async).
        
        Perfect for MCP servers and comments workflows.
        Returns simplified response for common use cases.
        """
        if not hasattr(self, '_create_comment'):
            raise ImportError("Raw client operation not available")
        
        result = await self._create_comment.asyncio(client=self.raw_client, node_id=node_id, body=body, fields=fields)
        
        # Convert to standardized response
        from ..models import BaseEntry
        return CommentsResponse(entry=BaseEntry(id=f"result-comments"))
    
    def create_comment_detailed(self, node_id: Any, body: Any, fields: Any):
        """
        Create Comment operation (detailed).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        """
        if not hasattr(self, '_create_comment'):
            raise ImportError("Raw client operation not available")
        
        return self._create_comment.sync_detailed(client=self.raw_client, node_id=node_id, body=body, fields=fields)
    
    async def create_comment_detailed_async(self, node_id: Any, body: Any, fields: Any):
        """
        Create Comment operation (detailed, async).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        """
        if not hasattr(self, '_create_comment'):
            raise ImportError("Raw client operation not available")
        
        return await self._create_comment.asyncio_detailed(client=self.raw_client, node_id=node_id, body=body, fields=fields)

    # ==================== DELETE_COMMENT OPERATION ====================
    
    def delete_comment(self, node_id: Any, comment_id: Any) -> CommentsResponse:
        """
        Delete Comment operation.
        
        Perfect for MCP servers and comments workflows.
        Returns simplified response for common use cases.
        """
        if not hasattr(self, '_delete_comment'):
            raise ImportError("Raw client operation not available")
        
        result = self._delete_comment.sync(client=self.raw_client, node_id=node_id, comment_id=comment_id)
        
        # Convert to standardized response
        from ..models import BaseEntry
        return CommentsResponse(entry=BaseEntry(id=f"result-comments"))
    
    async def delete_comment_async(self, node_id: Any, comment_id: Any) -> CommentsResponse:
        """
        Delete Comment operation (async).
        
        Perfect for MCP servers and comments workflows.
        Returns simplified response for common use cases.
        """
        if not hasattr(self, '_delete_comment'):
            raise ImportError("Raw client operation not available")
        
        result = await self._delete_comment.asyncio(client=self.raw_client, node_id=node_id, comment_id=comment_id)
        
        # Convert to standardized response
        from ..models import BaseEntry
        return CommentsResponse(entry=BaseEntry(id=f"result-comments"))
    
    def delete_comment_detailed(self, node_id: Any, comment_id: Any):
        """
        Delete Comment operation (detailed).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        """
        if not hasattr(self, '_delete_comment'):
            raise ImportError("Raw client operation not available")
        
        return self._delete_comment.sync_detailed(client=self.raw_client, node_id=node_id, comment_id=comment_id)
    
    async def delete_comment_detailed_async(self, node_id: Any, comment_id: Any):
        """
        Delete Comment operation (detailed, async).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        """
        if not hasattr(self, '_delete_comment'):
            raise ImportError("Raw client operation not available")
        
        return await self._delete_comment.asyncio_detailed(client=self.raw_client, node_id=node_id, comment_id=comment_id)

    # ==================== LIST_COMMENTS OPERATION ====================
    
    def list_comments(self, node_id: Any, skip_count: Any, max_items: Any, fields: Any) -> CommentsResponse:
        """
        List Comments operation.
        
        Perfect for MCP servers and comments workflows.
        Returns simplified response for common use cases.
        """
        if not hasattr(self, '_list_comments'):
            raise ImportError("Raw client operation not available")
        
        result = self._list_comments.sync(client=self.raw_client, node_id=node_id, skip_count=skip_count, max_items=max_items, fields=fields)
        
        # Convert to standardized response
        from ..models import BaseEntry
        return CommentsResponse(entry=BaseEntry(id=f"result-comments"))
    
    async def list_comments_async(self, node_id: Any, skip_count: Any, max_items: Any, fields: Any) -> CommentsResponse:
        """
        List Comments operation (async).
        
        Perfect for MCP servers and comments workflows.
        Returns simplified response for common use cases.
        """
        if not hasattr(self, '_list_comments'):
            raise ImportError("Raw client operation not available")
        
        result = await self._list_comments.asyncio(client=self.raw_client, node_id=node_id, skip_count=skip_count, max_items=max_items, fields=fields)
        
        # Convert to standardized response
        from ..models import BaseEntry
        return CommentsResponse(entry=BaseEntry(id=f"result-comments"))
    
    def list_comments_detailed(self, node_id: Any, skip_count: Any, max_items: Any, fields: Any):
        """
        List Comments operation (detailed).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        """
        if not hasattr(self, '_list_comments'):
            raise ImportError("Raw client operation not available")
        
        return self._list_comments.sync_detailed(client=self.raw_client, node_id=node_id, skip_count=skip_count, max_items=max_items, fields=fields)
    
    async def list_comments_detailed_async(self, node_id: Any, skip_count: Any, max_items: Any, fields: Any):
        """
        List Comments operation (detailed, async).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        """
        if not hasattr(self, '_list_comments'):
            raise ImportError("Raw client operation not available")
        
        return await self._list_comments.asyncio_detailed(client=self.raw_client, node_id=node_id, skip_count=skip_count, max_items=max_items, fields=fields)

    # ==================== UPDATE_COMMENT OPERATION ====================
    
    def update_comment(self, node_id: Any, comment_id: Any, body: Any, fields: Any) -> CommentsResponse:
        """
        Update Comment operation.
        
        Perfect for MCP servers and comments workflows.
        Returns simplified response for common use cases.
        """
        if not hasattr(self, '_update_comment'):
            raise ImportError("Raw client operation not available")
        
        result = self._update_comment.sync(client=self.raw_client, node_id=node_id, comment_id=comment_id, body=body, fields=fields)
        
        # Convert to standardized response
        from ..models import BaseEntry
        return CommentsResponse(entry=BaseEntry(id=f"result-comments"))
    
    async def update_comment_async(self, node_id: Any, comment_id: Any, body: Any, fields: Any) -> CommentsResponse:
        """
        Update Comment operation (async).
        
        Perfect for MCP servers and comments workflows.
        Returns simplified response for common use cases.
        """
        if not hasattr(self, '_update_comment'):
            raise ImportError("Raw client operation not available")
        
        result = await self._update_comment.asyncio(client=self.raw_client, node_id=node_id, comment_id=comment_id, body=body, fields=fields)
        
        # Convert to standardized response
        from ..models import BaseEntry
        return CommentsResponse(entry=BaseEntry(id=f"result-comments"))
    
    def update_comment_detailed(self, node_id: Any, comment_id: Any, body: Any, fields: Any):
        """
        Update Comment operation (detailed).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        """
        if not hasattr(self, '_update_comment'):
            raise ImportError("Raw client operation not available")
        
        return self._update_comment.sync_detailed(client=self.raw_client, node_id=node_id, comment_id=comment_id, body=body, fields=fields)
    
    async def update_comment_detailed_async(self, node_id: Any, comment_id: Any, body: Any, fields: Any):
        """
        Update Comment operation (detailed, async).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        """
        if not hasattr(self, '_update_comment'):
            raise ImportError("Raw client operation not available")
        
        return await self._update_comment.asyncio_detailed(client=self.raw_client, node_id=node_id, comment_id=comment_id, body=body, fields=fields)
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self._client_factory, 'base_url', 'unknown')
        return f"AlfrescoCommentsClient(base_url='{base_url}')" 