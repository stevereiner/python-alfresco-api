"""
Processes Operations Client - Level 3: Processes-Specific Operations

This module provides processes-specific operations within the Workflow API.
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
from ....raw_clients.alfresco_workflow_client.workflow_client.types import UNSET, Unset
from httpx import Response

# Import model types for proper parameter signatures
from ....raw_clients.alfresco_workflow_client.workflow_client.models.item_body import ItemBody
from ....raw_clients.alfresco_workflow_client.workflow_client.models.item_paging import ItemPaging
from ....raw_clients.alfresco_workflow_client.workflow_client.models.process_body import ProcessBody
from ....raw_clients.alfresco_workflow_client.workflow_client.models.process_entry import ProcessEntry
from ....raw_clients.alfresco_workflow_client.workflow_client.models.process_paging import ProcessPaging
from ....raw_clients.alfresco_workflow_client.workflow_client.models.variable_body import VariableBody
from ....raw_clients.alfresco_workflow_client.workflow_client.models.variable_entry import VariableEntry
from ....raw_clients.alfresco_workflow_client.workflow_client.models.variable_paging import VariablePaging

# Import from Level 3 (operation-specific models)
from .models import ProcessesResponse, ProcessesListResponse, CreateProcessesRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_workflow_client.workflow_client.api.processes import (
            create_process as _create_process,
            create_process_item as _create_process_item,
            create_process_variable as _create_process_variable,
            create_process_variables as _create_process_variables,
            delete_process as _delete_process,
            delete_process_item as _delete_process_item,
            delete_process_variable as _delete_process_variable,
            get_process as _get_process,
            list_processes as _list_processes,
            list_process_items as _list_process_items,
            list_process_variables as _list_process_variables
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class ProcessesClient:
    """
    Processes operations client with 4-pattern detailed functions.
    
    Clean Tier 3 implementation with different name from AlfrescoWorkflowClient.
    Provides high-level methods for processes management operations
    that are essential for MCP servers and processes workflows.
    
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
            self._create_process = _create_process
            self._create_process_item = _create_process_item
            self._create_process_variable = _create_process_variable
            self._create_process_variables = _create_process_variables
            self._delete_process = _delete_process
            self._delete_process_item = _delete_process_item
            self._delete_process_variable = _delete_process_variable
            self._get_process = _get_process
            self._list_processes = _list_processes
            self._list_process_items = _list_process_items
            self._list_process_variables = _list_process_variables
    
    @property
    def raw_client(self):
        """Delegate to parent client's raw client."""
        return self.parent_client.raw_client
    
    @property
    def httpx_client(self):
        """Delegate to parent client's httpx client."""
        return self.parent_client.httpx_client
    
    # ==================== 4-PATTERN OPERATIONS ====================

    # ==================== CREATE_PROCESS OPERATION - Complete 4-Pattern ====================
    
    def create_process(self, body: ProcessBody = UNSET) -> Any:
        """
        Create Process operation (sync).
        
        Perfect for MCP servers and processes workflows.
        Returns parsed response for common use cases.
        
        Args:
            body: ProcessBody = UNSET
        
        Returns:
            Parsed response object
        """
        if not hasattr(self, '_create_process'):
            raise ImportError("Raw client operation not available")
        
        return self._create_process.sync(client=self.raw_client, body=body)
    
    async def create_process_async(self, body: ProcessBody = UNSET) -> Any:
        """
        Create Process operation (async).
        
        Perfect for MCP servers and processes workflows.
        Returns parsed response for common use cases.
        
        Args:
            body: ProcessBody = UNSET
        
        Returns:
            Parsed response object
        """
        if not hasattr(self, '_create_process'):
            raise ImportError("Raw client operation not available")
        
        return await self._create_process.asyncio(client=self.raw_client, body=body)
    
    def create_process_detailed(self, body: ProcessBody = UNSET) -> Response:
        """
        Create Process operation (detailed sync).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        
        Args:
            body: ProcessBody = UNSET
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        if not hasattr(self, '_create_process'):
            raise ImportError("Raw client operation not available")
        
        return self._create_process.sync_detailed(client=self.raw_client, body=body)
    
    async def create_process_detailed_async(self, body: ProcessBody = UNSET) -> Response:
        """
        Create Process operation (detailed async).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        
        Args:
            body: ProcessBody = UNSET
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        if not hasattr(self, '_create_process'):
            raise ImportError("Raw client operation not available")
        
        return await self._create_process.asyncio_detailed(client=self.raw_client, body=body)

    # ==================== CREATE_PROCESS_ITEM OPERATION - Complete 4-Pattern ====================
    
    def create_process_item(self, process_id: str, body: ItemBody = UNSET) -> Any:
        """
        Create Process Item operation (sync).
        
        Perfect for MCP servers and processes workflows.
        Returns parsed response for common use cases.
        
        Args:
            process_id: str
            body: ItemBody = UNSET
        
        Returns:
            Parsed response object
        """
        if not hasattr(self, '_create_process_item'):
            raise ImportError("Raw client operation not available")
        
        return self._create_process_item.sync(client=self.raw_client, process_id=process_id, body=body)
    
    async def create_process_item_async(self, process_id: str, body: ItemBody = UNSET) -> Any:
        """
        Create Process Item operation (async).
        
        Perfect for MCP servers and processes workflows.
        Returns parsed response for common use cases.
        
        Args:
            process_id: str
            body: ItemBody = UNSET
        
        Returns:
            Parsed response object
        """
        if not hasattr(self, '_create_process_item'):
            raise ImportError("Raw client operation not available")
        
        return await self._create_process_item.asyncio(client=self.raw_client, process_id=process_id, body=body)
    
    def create_process_item_detailed(self, process_id: str, body: ItemBody = UNSET) -> Response:
        """
        Create Process Item operation (detailed sync).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        
        Args:
            process_id: str
            body: ItemBody = UNSET
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        if not hasattr(self, '_create_process_item'):
            raise ImportError("Raw client operation not available")
        
        return self._create_process_item.sync_detailed(client=self.raw_client, process_id=process_id, body=body)
    
    async def create_process_item_detailed_async(self, process_id: str, body: ItemBody = UNSET) -> Response:
        """
        Create Process Item operation (detailed async).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        
        Args:
            process_id: str
            body: ItemBody = UNSET
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        if not hasattr(self, '_create_process_item'):
            raise ImportError("Raw client operation not available")
        
        return await self._create_process_item.asyncio_detailed(client=self.raw_client, process_id=process_id, body=body)

    # ==================== CREATE_PROCESS_VARIABLE OPERATION - Complete 4-Pattern ====================
    
    def create_process_variable(self, process_id: str, variable_name: str, body: VariableBody = UNSET) -> Any:
        """
        Create Process Variable operation (sync).
        
        Perfect for MCP servers and processes workflows.
        Returns parsed response for common use cases.
        
        Args:
            process_id: str
            variable_name: str
            body: VariableBody = UNSET
        
        Returns:
            Parsed response object
        """
        if not hasattr(self, '_create_process_variable'):
            raise ImportError("Raw client operation not available")
        
        return self._create_process_variable.sync(client=self.raw_client, process_id=process_id, variable_name=variable_name, body=body)
    
    async def create_process_variable_async(self, process_id: str, variable_name: str, body: VariableBody = UNSET) -> Any:
        """
        Create Process Variable operation (async).
        
        Perfect for MCP servers and processes workflows.
        Returns parsed response for common use cases.
        
        Args:
            process_id: str
            variable_name: str
            body: VariableBody = UNSET
        
        Returns:
            Parsed response object
        """
        if not hasattr(self, '_create_process_variable'):
            raise ImportError("Raw client operation not available")
        
        return await self._create_process_variable.asyncio(client=self.raw_client, process_id=process_id, variable_name=variable_name, body=body)
    
    def create_process_variable_detailed(self, process_id: str, variable_name: str, body: VariableBody = UNSET) -> Response:
        """
        Create Process Variable operation (detailed sync).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        
        Args:
            process_id: str
            variable_name: str
            body: VariableBody = UNSET
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        if not hasattr(self, '_create_process_variable'):
            raise ImportError("Raw client operation not available")
        
        return self._create_process_variable.sync_detailed(client=self.raw_client, process_id=process_id, variable_name=variable_name, body=body)
    
    async def create_process_variable_detailed_async(self, process_id: str, variable_name: str, body: VariableBody = UNSET) -> Response:
        """
        Create Process Variable operation (detailed async).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        
        Args:
            process_id: str
            variable_name: str
            body: VariableBody = UNSET
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        if not hasattr(self, '_create_process_variable'):
            raise ImportError("Raw client operation not available")
        
        return await self._create_process_variable.asyncio_detailed(client=self.raw_client, process_id=process_id, variable_name=variable_name, body=body)

    # ==================== CREATE_PROCESS_VARIABLES OPERATION - Complete 4-Pattern ====================
    
    def create_process_variables(self, process_id: str, body: VariableBody = UNSET) -> Any:
        """
        Create Process Variables operation (sync).
        
        Perfect for MCP servers and processes workflows.
        Returns parsed response for common use cases.
        
        Args:
            process_id: str
            body: VariableBody = UNSET
        
        Returns:
            Parsed response object
        """
        if not hasattr(self, '_create_process_variables'):
            raise ImportError("Raw client operation not available")
        
        return self._create_process_variables.sync(client=self.raw_client, process_id=process_id, body=body)
    
    async def create_process_variables_async(self, process_id: str, body: VariableBody = UNSET) -> Any:
        """
        Create Process Variables operation (async).
        
        Perfect for MCP servers and processes workflows.
        Returns parsed response for common use cases.
        
        Args:
            process_id: str
            body: VariableBody = UNSET
        
        Returns:
            Parsed response object
        """
        if not hasattr(self, '_create_process_variables'):
            raise ImportError("Raw client operation not available")
        
        return await self._create_process_variables.asyncio(client=self.raw_client, process_id=process_id, body=body)
    
    def create_process_variables_detailed(self, process_id: str, body: VariableBody = UNSET) -> Response:
        """
        Create Process Variables operation (detailed sync).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        
        Args:
            process_id: str
            body: VariableBody = UNSET
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        if not hasattr(self, '_create_process_variables'):
            raise ImportError("Raw client operation not available")
        
        return self._create_process_variables.sync_detailed(client=self.raw_client, process_id=process_id, body=body)
    
    async def create_process_variables_detailed_async(self, process_id: str, body: VariableBody = UNSET) -> Response:
        """
        Create Process Variables operation (detailed async).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        
        Args:
            process_id: str
            body: VariableBody = UNSET
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        if not hasattr(self, '_create_process_variables'):
            raise ImportError("Raw client operation not available")
        
        return await self._create_process_variables.asyncio_detailed(client=self.raw_client, process_id=process_id, body=body)

    # ==================== DELETE_PROCESS OPERATION - Complete 4-Pattern ====================
    
    def delete_process(self, process_id: str) -> Any:
        """
        Delete Process operation (sync).
        
        Perfect for MCP servers and processes workflows.
        Returns parsed response for common use cases.
        
        Args:
            process_id: str
        
        Returns:
            Parsed response object
        """
        if not hasattr(self, '_delete_process'):
            raise ImportError("Raw client operation not available")
        
        return self._delete_process.sync(client=self.raw_client, process_id=process_id)
    
    async def delete_process_async(self, process_id: str) -> Any:
        """
        Delete Process operation (async).
        
        Perfect for MCP servers and processes workflows.
        Returns parsed response for common use cases.
        
        Args:
            process_id: str
        
        Returns:
            Parsed response object
        """
        if not hasattr(self, '_delete_process'):
            raise ImportError("Raw client operation not available")
        
        return await self._delete_process.asyncio(client=self.raw_client, process_id=process_id)
    
    def delete_process_detailed(self, process_id: str) -> Response:
        """
        Delete Process operation (detailed sync).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        
        Args:
            process_id: str
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        if not hasattr(self, '_delete_process'):
            raise ImportError("Raw client operation not available")
        
        return self._delete_process.sync_detailed(client=self.raw_client, process_id=process_id)
    
    async def delete_process_detailed_async(self, process_id: str) -> Response:
        """
        Delete Process operation (detailed async).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        
        Args:
            process_id: str
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        if not hasattr(self, '_delete_process'):
            raise ImportError("Raw client operation not available")
        
        return await self._delete_process.asyncio_detailed(client=self.raw_client, process_id=process_id)

    # ==================== DELETE_PROCESS_ITEM OPERATION - Complete 4-Pattern ====================
    
    def delete_process_item(self, process_id: str, item_id: str) -> Any:
        """
        Delete Process Item operation (sync).
        
        Perfect for MCP servers and processes workflows.
        Returns parsed response for common use cases.
        
        Args:
            process_id: str
            item_id: str
        
        Returns:
            Parsed response object
        """
        if not hasattr(self, '_delete_process_item'):
            raise ImportError("Raw client operation not available")
        
        return self._delete_process_item.sync(client=self.raw_client, process_id=process_id, item_id=item_id)
    
    async def delete_process_item_async(self, process_id: str, item_id: str) -> Any:
        """
        Delete Process Item operation (async).
        
        Perfect for MCP servers and processes workflows.
        Returns parsed response for common use cases.
        
        Args:
            process_id: str
            item_id: str
        
        Returns:
            Parsed response object
        """
        if not hasattr(self, '_delete_process_item'):
            raise ImportError("Raw client operation not available")
        
        return await self._delete_process_item.asyncio(client=self.raw_client, process_id=process_id, item_id=item_id)
    
    def delete_process_item_detailed(self, process_id: str, item_id: str) -> Response:
        """
        Delete Process Item operation (detailed sync).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        
        Args:
            process_id: str
            item_id: str
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        if not hasattr(self, '_delete_process_item'):
            raise ImportError("Raw client operation not available")
        
        return self._delete_process_item.sync_detailed(client=self.raw_client, process_id=process_id, item_id=item_id)
    
    async def delete_process_item_detailed_async(self, process_id: str, item_id: str) -> Response:
        """
        Delete Process Item operation (detailed async).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        
        Args:
            process_id: str
            item_id: str
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        if not hasattr(self, '_delete_process_item'):
            raise ImportError("Raw client operation not available")
        
        return await self._delete_process_item.asyncio_detailed(client=self.raw_client, process_id=process_id, item_id=item_id)

    # ==================== DELETE_PROCESS_VARIABLE OPERATION - Complete 4-Pattern ====================
    
    def delete_process_variable(self, process_id: str, variable_name: str) -> Any:
        """
        Delete Process Variable operation (sync).
        
        Perfect for MCP servers and processes workflows.
        Returns parsed response for common use cases.
        
        Args:
            process_id: str
            variable_name: str
        
        Returns:
            Parsed response object
        """
        if not hasattr(self, '_delete_process_variable'):
            raise ImportError("Raw client operation not available")
        
        return self._delete_process_variable.sync(client=self.raw_client, process_id=process_id, variable_name=variable_name)
    
    async def delete_process_variable_async(self, process_id: str, variable_name: str) -> Any:
        """
        Delete Process Variable operation (async).
        
        Perfect for MCP servers and processes workflows.
        Returns parsed response for common use cases.
        
        Args:
            process_id: str
            variable_name: str
        
        Returns:
            Parsed response object
        """
        if not hasattr(self, '_delete_process_variable'):
            raise ImportError("Raw client operation not available")
        
        return await self._delete_process_variable.asyncio(client=self.raw_client, process_id=process_id, variable_name=variable_name)
    
    def delete_process_variable_detailed(self, process_id: str, variable_name: str) -> Response:
        """
        Delete Process Variable operation (detailed sync).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        
        Args:
            process_id: str
            variable_name: str
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        if not hasattr(self, '_delete_process_variable'):
            raise ImportError("Raw client operation not available")
        
        return self._delete_process_variable.sync_detailed(client=self.raw_client, process_id=process_id, variable_name=variable_name)
    
    async def delete_process_variable_detailed_async(self, process_id: str, variable_name: str) -> Response:
        """
        Delete Process Variable operation (detailed async).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        
        Args:
            process_id: str
            variable_name: str
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        if not hasattr(self, '_delete_process_variable'):
            raise ImportError("Raw client operation not available")
        
        return await self._delete_process_variable.asyncio_detailed(client=self.raw_client, process_id=process_id, variable_name=variable_name)

    # ==================== GET_PROCESS OPERATION - Complete 4-Pattern ====================
    
    def get_process(self, process_id: str, properties: Union[Unset, Any] = UNSET) -> Any:
        """
        Get Process operation (sync).
        
        Perfect for MCP servers and processes workflows.
        Returns parsed response for common use cases.
        
        Args:
            process_id: str
            properties: Union[Unset, Any] = UNSET
        
        Returns:
            Parsed response object
        """
        if not hasattr(self, '_get_process'):
            raise ImportError("Raw client operation not available")
        
        return self._get_process.sync(client=self.raw_client, process_id=process_id, properties=properties)
    
    async def get_process_async(self, process_id: str, properties: Union[Unset, Any] = UNSET) -> Any:
        """
        Get Process operation (async).
        
        Perfect for MCP servers and processes workflows.
        Returns parsed response for common use cases.
        
        Args:
            process_id: str
            properties: Union[Unset, Any] = UNSET
        
        Returns:
            Parsed response object
        """
        if not hasattr(self, '_get_process'):
            raise ImportError("Raw client operation not available")
        
        return await self._get_process.asyncio(client=self.raw_client, process_id=process_id, properties=properties)
    
    def get_process_detailed(self, process_id: str, properties: Union[Unset, Any] = UNSET) -> Response:
        """
        Get Process operation (detailed sync).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        
        Args:
            process_id: str
            properties: Union[Unset, Any] = UNSET
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        if not hasattr(self, '_get_process'):
            raise ImportError("Raw client operation not available")
        
        return self._get_process.sync_detailed(client=self.raw_client, process_id=process_id, properties=properties)
    
    async def get_process_detailed_async(self, process_id: str, properties: Union[Unset, Any] = UNSET) -> Response:
        """
        Get Process operation (detailed async).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        
        Args:
            process_id: str
            properties: Union[Unset, Any] = UNSET
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        if not hasattr(self, '_get_process'):
            raise ImportError("Raw client operation not available")
        
        return await self._get_process.asyncio_detailed(client=self.raw_client, process_id=process_id, properties=properties)

    # ==================== LIST_PROCESSES OPERATION - Complete 4-Pattern ====================
    
    def list_processes(self, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET, order_by: Union[Unset, Any] = UNSET, where: Union[Unset, Any] = UNSET) -> Any:
        """
        List Processes operation (sync).
        
        Perfect for MCP servers and processes workflows.
        Returns parsed response for common use cases.
        
        Args:
            skip_count: Union[Unset, Any] = UNSET
            max_items: Union[Unset, Any] = UNSET
            properties: Union[Unset, Any] = UNSET
            order_by: Union[Unset, Any] = UNSET
            where: Union[Unset, Any] = UNSET
        
        Returns:
            Parsed response object
        """
        if not hasattr(self, '_list_processes'):
            raise ImportError("Raw client operation not available")
        
        return self._list_processes.sync(client=self.raw_client, skip_count=skip_count, max_items=max_items, properties=properties, order_by=order_by, where=where)
    
    async def list_processes_async(self, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET, order_by: Union[Unset, Any] = UNSET, where: Union[Unset, Any] = UNSET) -> Any:
        """
        List Processes operation (async).
        
        Perfect for MCP servers and processes workflows.
        Returns parsed response for common use cases.
        
        Args:
            skip_count: Union[Unset, Any] = UNSET
            max_items: Union[Unset, Any] = UNSET
            properties: Union[Unset, Any] = UNSET
            order_by: Union[Unset, Any] = UNSET
            where: Union[Unset, Any] = UNSET
        
        Returns:
            Parsed response object
        """
        if not hasattr(self, '_list_processes'):
            raise ImportError("Raw client operation not available")
        
        return await self._list_processes.asyncio(client=self.raw_client, skip_count=skip_count, max_items=max_items, properties=properties, order_by=order_by, where=where)
    
    def list_processes_detailed(self, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET, order_by: Union[Unset, Any] = UNSET, where: Union[Unset, Any] = UNSET) -> Response:
        """
        List Processes operation (detailed sync).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        
        Args:
            skip_count: Union[Unset, Any] = UNSET
            max_items: Union[Unset, Any] = UNSET
            properties: Union[Unset, Any] = UNSET
            order_by: Union[Unset, Any] = UNSET
            where: Union[Unset, Any] = UNSET
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        if not hasattr(self, '_list_processes'):
            raise ImportError("Raw client operation not available")
        
        return self._list_processes.sync_detailed(client=self.raw_client, skip_count=skip_count, max_items=max_items, properties=properties, order_by=order_by, where=where)
    
    async def list_processes_detailed_async(self, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET, order_by: Union[Unset, Any] = UNSET, where: Union[Unset, Any] = UNSET) -> Response:
        """
        List Processes operation (detailed async).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        
        Args:
            skip_count: Union[Unset, Any] = UNSET
            max_items: Union[Unset, Any] = UNSET
            properties: Union[Unset, Any] = UNSET
            order_by: Union[Unset, Any] = UNSET
            where: Union[Unset, Any] = UNSET
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        if not hasattr(self, '_list_processes'):
            raise ImportError("Raw client operation not available")
        
        return await self._list_processes.asyncio_detailed(client=self.raw_client, skip_count=skip_count, max_items=max_items, properties=properties, order_by=order_by, where=where)

    # ==================== LIST_PROCESS_ITEMS OPERATION - Complete 4-Pattern ====================
    
    def list_process_items(self, process_id: str, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET) -> Any:
        """
        List Process Items operation (sync).
        
        Perfect for MCP servers and processes workflows.
        Returns parsed response for common use cases.
        
        Args:
            process_id: str
            skip_count: Union[Unset, Any] = UNSET
            max_items: Union[Unset, Any] = UNSET
            properties: Union[Unset, Any] = UNSET
        
        Returns:
            Parsed response object
        """
        if not hasattr(self, '_list_process_items'):
            raise ImportError("Raw client operation not available")
        
        return self._list_process_items.sync(client=self.raw_client, process_id=process_id, skip_count=skip_count, max_items=max_items, properties=properties)
    
    async def list_process_items_async(self, process_id: str, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET) -> Any:
        """
        List Process Items operation (async).
        
        Perfect for MCP servers and processes workflows.
        Returns parsed response for common use cases.
        
        Args:
            process_id: str
            skip_count: Union[Unset, Any] = UNSET
            max_items: Union[Unset, Any] = UNSET
            properties: Union[Unset, Any] = UNSET
        
        Returns:
            Parsed response object
        """
        if not hasattr(self, '_list_process_items'):
            raise ImportError("Raw client operation not available")
        
        return await self._list_process_items.asyncio(client=self.raw_client, process_id=process_id, skip_count=skip_count, max_items=max_items, properties=properties)
    
    def list_process_items_detailed(self, process_id: str, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET) -> Response:
        """
        List Process Items operation (detailed sync).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        
        Args:
            process_id: str
            skip_count: Union[Unset, Any] = UNSET
            max_items: Union[Unset, Any] = UNSET
            properties: Union[Unset, Any] = UNSET
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        if not hasattr(self, '_list_process_items'):
            raise ImportError("Raw client operation not available")
        
        return self._list_process_items.sync_detailed(client=self.raw_client, process_id=process_id, skip_count=skip_count, max_items=max_items, properties=properties)
    
    async def list_process_items_detailed_async(self, process_id: str, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET) -> Response:
        """
        List Process Items operation (detailed async).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        
        Args:
            process_id: str
            skip_count: Union[Unset, Any] = UNSET
            max_items: Union[Unset, Any] = UNSET
            properties: Union[Unset, Any] = UNSET
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        if not hasattr(self, '_list_process_items'):
            raise ImportError("Raw client operation not available")
        
        return await self._list_process_items.asyncio_detailed(client=self.raw_client, process_id=process_id, skip_count=skip_count, max_items=max_items, properties=properties)

    # ==================== LIST_PROCESS_VARIABLES OPERATION - Complete 4-Pattern ====================
    
    def list_process_variables(self, process_id: str, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET) -> Any:
        """
        List Process Variables operation (sync).
        
        Perfect for MCP servers and processes workflows.
        Returns parsed response for common use cases.
        
        Args:
            process_id: str
            skip_count: Union[Unset, Any] = UNSET
            max_items: Union[Unset, Any] = UNSET
            properties: Union[Unset, Any] = UNSET
        
        Returns:
            Parsed response object
        """
        if not hasattr(self, '_list_process_variables'):
            raise ImportError("Raw client operation not available")
        
        return self._list_process_variables.sync(client=self.raw_client, process_id=process_id, skip_count=skip_count, max_items=max_items, properties=properties)
    
    async def list_process_variables_async(self, process_id: str, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET) -> Any:
        """
        List Process Variables operation (async).
        
        Perfect for MCP servers and processes workflows.
        Returns parsed response for common use cases.
        
        Args:
            process_id: str
            skip_count: Union[Unset, Any] = UNSET
            max_items: Union[Unset, Any] = UNSET
            properties: Union[Unset, Any] = UNSET
        
        Returns:
            Parsed response object
        """
        if not hasattr(self, '_list_process_variables'):
            raise ImportError("Raw client operation not available")
        
        return await self._list_process_variables.asyncio(client=self.raw_client, process_id=process_id, skip_count=skip_count, max_items=max_items, properties=properties)
    
    def list_process_variables_detailed(self, process_id: str, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET) -> Response:
        """
        List Process Variables operation (detailed sync).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        
        Args:
            process_id: str
            skip_count: Union[Unset, Any] = UNSET
            max_items: Union[Unset, Any] = UNSET
            properties: Union[Unset, Any] = UNSET
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        if not hasattr(self, '_list_process_variables'):
            raise ImportError("Raw client operation not available")
        
        return self._list_process_variables.sync_detailed(client=self.raw_client, process_id=process_id, skip_count=skip_count, max_items=max_items, properties=properties)
    
    async def list_process_variables_detailed_async(self, process_id: str, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET) -> Response:
        """
        List Process Variables operation (detailed async).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        
        Args:
            process_id: str
            skip_count: Union[Unset, Any] = UNSET
            max_items: Union[Unset, Any] = UNSET
            properties: Union[Unset, Any] = UNSET
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        if not hasattr(self, '_list_process_variables'):
            raise ImportError("Raw client operation not available")
        
        return await self._list_process_variables.asyncio_detailed(client=self.raw_client, process_id=process_id, skip_count=skip_count, max_items=max_items, properties=properties)

    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self.parent_client._client_factory, 'base_url', 'unknown')
        return f"ProcessesClient(base_url='{base_url}')" 
