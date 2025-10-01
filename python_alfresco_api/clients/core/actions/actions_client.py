"""
Actions Operations Client - Level 3: Actions-Specific Operations

This module provides actions-specific operations within the Core API.
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
from .models import ActionsResponse, ActionsListResponse, CreateActionsRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_core_client.core_client.api.actions import (
            action_details as _action_details,
            action_exec as _action_exec,
            list_actions as _list_actions,
            node_actions as _node_actions
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class ActionsClient:
    """
    Actions operations client with 4-pattern detailed functions.
    
    Provides high-level methods for actions management operations
    that are essential for MCP servers and actions workflows.
    
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
            self._action_details = _action_details
            self._action_exec = _action_exec
            self._list_actions = _list_actions
            self._node_actions = _node_actions
    
    @property
    def raw_client(self):
        """Delegate to parent client's raw client."""
        return self.parent_client.raw_client
    
    @property
    def httpx_client(self):
        """Delegate to parent client's httpx client."""
        return self.parent_client.httpx_client
    
    # ==================== 4-PATTERN OPERATIONS ====================

    # ==================== ACTION_DETAILS OPERATION ====================
    
    def action_details(self, action_definition_id: Any) -> ActionsResponse:
        """
        Action Details operation.
        
        Perfect for MCP servers and actions workflows.
        Returns simplified response for common use cases.
        """
        if not hasattr(self, '_action_details'):
            raise ImportError("Raw client operation not available")
        
        result = self._action_details.sync(client=self.raw_client, action_definition_id=action_definition_id)
        
        # Convert to standardized response
        from ..models import BaseEntry
        return ActionsResponse(entry=BaseEntry(id=f"result-actions"))
    
    async def action_details_async(self, action_definition_id: Any) -> ActionsResponse:
        """
        Action Details operation (async).
        
        Perfect for MCP servers and actions workflows.
        Returns simplified response for common use cases.
        """
        if not hasattr(self, '_action_details'):
            raise ImportError("Raw client operation not available")
        
        result = await self._action_details.asyncio(client=self.raw_client, action_definition_id=action_definition_id)
        
        # Convert to standardized response
        from ..models import BaseEntry
        return ActionsResponse(entry=BaseEntry(id=f"result-actions"))
    
    def action_details_detailed(self, action_definition_id: Any):
        """
        Action Details operation (detailed).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        """
        if not hasattr(self, '_action_details'):
            raise ImportError("Raw client operation not available")
        
        return self._action_details.sync_detailed(client=self.raw_client, action_definition_id=action_definition_id)
    
    async def action_details_detailed_async(self, action_definition_id: Any):
        """
        Action Details operation (detailed, async).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        """
        if not hasattr(self, '_action_details'):
            raise ImportError("Raw client operation not available")
        
        return await self._action_details.asyncio_detailed(client=self.raw_client, action_definition_id=action_definition_id)

    # ==================== ACTION_EXEC OPERATION ====================
    
    def action_exec(self, body: Any) -> ActionsResponse:
        """
        Action Exec operation.
        
        Perfect for MCP servers and actions workflows.
        Returns simplified response for common use cases.
        """
        if not hasattr(self, '_action_exec'):
            raise ImportError("Raw client operation not available")
        
        result = self._action_exec.sync(client=self.raw_client, body=body)
        
        # Convert to standardized response
        from ..models import BaseEntry
        return ActionsResponse(entry=BaseEntry(id=f"result-actions"))
    
    async def action_exec_async(self, body: Any) -> ActionsResponse:
        """
        Action Exec operation (async).
        
        Perfect for MCP servers and actions workflows.
        Returns simplified response for common use cases.
        """
        if not hasattr(self, '_action_exec'):
            raise ImportError("Raw client operation not available")
        
        result = await self._action_exec.asyncio(client=self.raw_client, body=body)
        
        # Convert to standardized response
        from ..models import BaseEntry
        return ActionsResponse(entry=BaseEntry(id=f"result-actions"))
    
    def action_exec_detailed(self, body: Any):
        """
        Action Exec operation (detailed).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        """
        if not hasattr(self, '_action_exec'):
            raise ImportError("Raw client operation not available")
        
        return self._action_exec.sync_detailed(client=self.raw_client, body=body)
    
    async def action_exec_detailed_async(self, body: Any):
        """
        Action Exec operation (detailed, async).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        """
        if not hasattr(self, '_action_exec'):
            raise ImportError("Raw client operation not available")
        
        return await self._action_exec.asyncio_detailed(client=self.raw_client, body=body)

    # ==================== LIST_ACTIONS OPERATION ====================
    
    def list_actions(self, skip_count: Any, max_items: Any, order_by: Any, fields: Any) -> ActionsResponse:
        """
        List Actions operation.
        
        Perfect for MCP servers and actions workflows.
        Returns simplified response for common use cases.
        """
        if not hasattr(self, '_list_actions'):
            raise ImportError("Raw client operation not available")
        
        result = self._list_actions.sync(client=self.raw_client, skip_count=skip_count, max_items=max_items, order_by=order_by, fields=fields)
        
        # Convert to standardized response
        from ..models import BaseEntry
        return ActionsResponse(entry=BaseEntry(id=f"result-actions"))
    
    async def list_actions_async(self, skip_count: Any, max_items: Any, order_by: Any, fields: Any) -> ActionsResponse:
        """
        List Actions operation (async).
        
        Perfect for MCP servers and actions workflows.
        Returns simplified response for common use cases.
        """
        if not hasattr(self, '_list_actions'):
            raise ImportError("Raw client operation not available")
        
        result = await self._list_actions.asyncio(client=self.raw_client, skip_count=skip_count, max_items=max_items, order_by=order_by, fields=fields)
        
        # Convert to standardized response
        from ..models import BaseEntry
        return ActionsResponse(entry=BaseEntry(id=f"result-actions"))
    
    def list_actions_detailed(self, skip_count: Any, max_items: Any, order_by: Any, fields: Any):
        """
        List Actions operation (detailed).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        """
        if not hasattr(self, '_list_actions'):
            raise ImportError("Raw client operation not available")
        
        return self._list_actions.sync_detailed(client=self.raw_client, skip_count=skip_count, max_items=max_items, order_by=order_by, fields=fields)
    
    async def list_actions_detailed_async(self, skip_count: Any, max_items: Any, order_by: Any, fields: Any):
        """
        List Actions operation (detailed, async).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        """
        if not hasattr(self, '_list_actions'):
            raise ImportError("Raw client operation not available")
        
        return await self._list_actions.asyncio_detailed(client=self.raw_client, skip_count=skip_count, max_items=max_items, order_by=order_by, fields=fields)

    # ==================== NODE_ACTIONS OPERATION ====================
    
    def node_actions(self, node_id: Any, skip_count: Any, max_items: Any, order_by: Any, fields: Any) -> ActionsResponse:
        """
        Node Actions operation.
        
        Perfect for MCP servers and actions workflows.
        Returns simplified response for common use cases.
        """
        if not hasattr(self, '_node_actions'):
            raise ImportError("Raw client operation not available")
        
        result = self._node_actions.sync(client=self.raw_client, node_id=node_id, skip_count=skip_count, max_items=max_items, order_by=order_by, fields=fields)
        
        # Convert to standardized response
        from ..models import BaseEntry
        return ActionsResponse(entry=BaseEntry(id=f"result-actions"))
    
    async def node_actions_async(self, node_id: Any, skip_count: Any, max_items: Any, order_by: Any, fields: Any) -> ActionsResponse:
        """
        Node Actions operation (async).
        
        Perfect for MCP servers and actions workflows.
        Returns simplified response for common use cases.
        """
        if not hasattr(self, '_node_actions'):
            raise ImportError("Raw client operation not available")
        
        result = await self._node_actions.asyncio(client=self.raw_client, node_id=node_id, skip_count=skip_count, max_items=max_items, order_by=order_by, fields=fields)
        
        # Convert to standardized response
        from ..models import BaseEntry
        return ActionsResponse(entry=BaseEntry(id=f"result-actions"))
    
    def node_actions_detailed(self, node_id: Any, skip_count: Any, max_items: Any, order_by: Any, fields: Any):
        """
        Node Actions operation (detailed).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        """
        if not hasattr(self, '_node_actions'):
            raise ImportError("Raw client operation not available")
        
        return self._node_actions.sync_detailed(client=self.raw_client, node_id=node_id, skip_count=skip_count, max_items=max_items, order_by=order_by, fields=fields)
    
    async def node_actions_detailed_async(self, node_id: Any, skip_count: Any, max_items: Any, order_by: Any, fields: Any):
        """
        Node Actions operation (detailed, async).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        """
        if not hasattr(self, '_node_actions'):
            raise ImportError("Raw client operation not available")
        
        return await self._node_actions.asyncio_detailed(client=self.raw_client, node_id=node_id, skip_count=skip_count, max_items=max_items, order_by=order_by, fields=fields)
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self._client_factory, 'base_url', 'unknown')
        return f"AlfrescoActionsClient(base_url='{base_url}')" 