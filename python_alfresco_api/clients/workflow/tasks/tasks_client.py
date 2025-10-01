"""
Tasks Operations Client - Level 3: Tasks-Specific Operations

This module provides tasks-specific operations within the Workflow API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.

Each operation provides 4 variants:
- operation(params) - basic sync with explicit parameters
- operation_async(params) - basic async with explicit parameters  
- operation_detailed(params) - detailed sync with explicit parameters
- operation_detailed_async(params) - detailed async with explicit parameters

Perfect for MCP servers and documentation generation.

TasksClient Operations (13 operations × 4 patterns = 52 methods):
1. create_task_item
2. create_task_variables
3. delete_task_item
4. delete_task_variable
5. get_task
6. get_task_form_model
7. list_tasks
8. list_tasks_for_process
9. list_task_candidates
10. list_task_items
11. list_task_variables
12. update_task
13. update_task_variable
"""

import asyncio
from typing import Optional, List, Union, Any, Awaitable
from httpx import Response

# Import required types for proper parameter handling
from ....raw_clients.alfresco_workflow_client.workflow_client.types import UNSET, Unset
from httpx import Response

# Import model types for proper parameter signatures
from ....raw_clients.alfresco_workflow_client.workflow_client.models.candidate_paging import CandidatePaging
from ....raw_clients.alfresco_workflow_client.workflow_client.models.item_body import ItemBody
from ....raw_clients.alfresco_workflow_client.workflow_client.models.item_paging import ItemPaging
from ....raw_clients.alfresco_workflow_client.workflow_client.models.task_body import TaskBody
from ....raw_clients.alfresco_workflow_client.workflow_client.models.task_entry import TaskEntry
from ....raw_clients.alfresco_workflow_client.workflow_client.models.task_form_model_paging import TaskFormModelPaging
from ....raw_clients.alfresco_workflow_client.workflow_client.models.task_paging import TaskPaging
from ....raw_clients.alfresco_workflow_client.workflow_client.models.variable import Variable
from ....raw_clients.alfresco_workflow_client.workflow_client.models.variable_entry import VariableEntry
from ....raw_clients.alfresco_workflow_client.workflow_client.models.variable_paging import VariablePaging

# Import from Level 3 (operation-specific models)
from .models import TasksResponse, TasksListResponse, CreateTasksRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_workflow_client.workflow_client.api.tasks import (
            create_task_item as _create_task_item,
            create_task_variables as _create_task_variables,
            delete_task_item as _delete_task_item,
            delete_task_variable as _delete_task_variable,
            get_task as _get_task,
            get_task_form_model as _get_task_form_model,
            list_tasks as _list_tasks,
            list_tasks_for_process as _list_tasks_for_process,
            list_task_candidates as _list_task_candidates,
            list_task_items as _list_task_items,
            list_task_variables as _list_task_variables,
            update_task as _update_task,
            update_task_variable as _update_task_variable
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False

# Fixed typing compatibility: Response[Any] -> Response for Python < 3.9 
class TasksClient:
    """
    Tasks operations client with 4-pattern detailed functions.
    
    Clean Tier 3 implementation with different name from AlfrescoWorkflowClient.
    Provides high-level methods for tasks management operations
    that are essential for MCP servers and tasks workflows.
    
    Each operation has 4 variants for maximum flexibility:
    - Basic sync/async for simple use cases
    - Detailed sync/async for full HTTP response access
    
    Complete API Coverage:
    - Task management (create, get, update, delete)
    - Task items (create, list, delete)
    - Task variables (create, list, update, delete)
    - Task candidates (list)
    - Task form models (get)
    - Process-specific tasks (list)
    """
    
    def __init__(self, parent_client):
        """Initialize with client factory for raw client access."""
        self.parent_client = parent_client
        self._raw_client = None
        
        # Store raw operation references
        if RAW_OPERATIONS_AVAILABLE:
            self._create_task_item = _create_task_item
            self._create_task_variables = _create_task_variables
            self._delete_task_item = _delete_task_item
            self._delete_task_variable = _delete_task_variable
            self._get_task = _get_task
            self._get_task_form_model = _get_task_form_model
            self._list_tasks = _list_tasks
            self._list_tasks_for_process = _list_tasks_for_process
            self._list_task_candidates = _list_task_candidates
            self._list_task_items = _list_task_items
            self._list_task_variables = _list_task_variables
            self._update_task = _update_task
            self._update_task_variable = _update_task_variable
    
    @property
    def raw_client(self):
        """Delegate to parent client's raw client."""
        return self.parent_client.raw_client
    
    @property
    def httpx_client(self):
        """Delegate to parent client's httpx client."""
        return self.parent_client.httpx_client
    
    # ==================== 4-PATTERN OPERATIONS ====================
    # Note: Due to size constraints, showing abbreviated version of 52 methods
    # Full implementation includes all 13 operations × 4 patterns each
    
    # ==================== CREATE_TASK_ITEM OPERATION - Complete 4-Pattern ====================
    
    def create_task_item(self, task_id: str, body: ItemBody = UNSET) -> Any:
        """Create Task Item operation (sync)."""
        if not hasattr(self, '_create_task_item'):
            raise ImportError("Raw client operation not available")
        return self._create_task_item.sync(client=self.raw_client, task_id=task_id, body=body)
    
    async def create_task_item_async(self, task_id: str, body: ItemBody = UNSET) -> Any:
        """Create Task Item operation (async)."""
        if not hasattr(self, '_create_task_item'):
            raise ImportError("Raw client operation not available")
        return await self._create_task_item.asyncio(client=self.raw_client, task_id=task_id, body=body)
    
    def create_task_item_detailed(self, task_id: str, body: ItemBody = UNSET) -> Response:
        """Create Task Item operation (detailed sync)."""
        if not hasattr(self, '_create_task_item'):
            raise ImportError("Raw client operation not available")
        return self._create_task_item.sync_detailed(client=self.raw_client, task_id=task_id, body=body)
    
    async def create_task_item_detailed_async(self, task_id: str, body: ItemBody = UNSET) -> Response:
        """Create Task Item operation (detailed async)."""
        if not hasattr(self, '_create_task_item'):
            raise ImportError("Raw client operation not available")
        return await self._create_task_item.asyncio_detailed(client=self.raw_client, task_id=task_id, body=body)

    # ==================== CREATE_TASK_VARIABLES OPERATION - Complete 4-Pattern ====================
    
    def create_task_variables(self, task_id: str, body: Variable = UNSET) -> Any:
        """Create Task Variables operation (sync)."""
        if not hasattr(self, '_create_task_variables'):
            raise ImportError("Raw client operation not available")
        return self._create_task_variables.sync(client=self.raw_client, task_id=task_id, body=body)
    
    async def create_task_variables_async(self, task_id: str, body: Variable = UNSET) -> Any:
        """Create Task Variables operation (async)."""
        if not hasattr(self, '_create_task_variables'):
            raise ImportError("Raw client operation not available")
        return await self._create_task_variables.asyncio(client=self.raw_client, task_id=task_id, body=body)
    
    def create_task_variables_detailed(self, task_id: str, body: Variable = UNSET) -> Response:
        """Create Task Variables operation (detailed sync)."""
        if not hasattr(self, '_create_task_variables'):
            raise ImportError("Raw client operation not available")
        return self._create_task_variables.sync_detailed(client=self.raw_client, task_id=task_id, body=body)
    
    async def create_task_variables_detailed_async(self, task_id: str, body: Variable = UNSET) -> Response:
        """Create Task Variables operation (detailed async)."""
        if not hasattr(self, '_create_task_variables'):
            raise ImportError("Raw client operation not available")
        return await self._create_task_variables.asyncio_detailed(client=self.raw_client, task_id=task_id, body=body)

    # ==================== DELETE_TASK_ITEM OPERATION - Complete 4-Pattern ====================
    
    def delete_task_item(self, task_id: str, item_id: str) -> Any:
        """Delete Task Item operation (sync)."""
        if not hasattr(self, '_delete_task_item'):
            raise ImportError("Raw client operation not available")
        return self._delete_task_item.sync(client=self.raw_client, task_id=task_id, item_id=item_id)
    
    async def delete_task_item_async(self, task_id: str, item_id: str) -> Any:
        """Delete Task Item operation (async)."""
        if not hasattr(self, '_delete_task_item'):
            raise ImportError("Raw client operation not available")
        return await self._delete_task_item.asyncio(client=self.raw_client, task_id=task_id, item_id=item_id)
    
    def delete_task_item_detailed(self, task_id: str, item_id: str) -> Response:
        """Delete Task Item operation (detailed sync)."""
        if not hasattr(self, '_delete_task_item'):
            raise ImportError("Raw client operation not available")
        return self._delete_task_item.sync_detailed(client=self.raw_client, task_id=task_id, item_id=item_id)
    
    async def delete_task_item_detailed_async(self, task_id: str, item_id: str) -> Response:
        """Delete Task Item operation (detailed async)."""
        if not hasattr(self, '_delete_task_item'):
            raise ImportError("Raw client operation not available")
        return await self._delete_task_item.asyncio_detailed(client=self.raw_client, task_id=task_id, item_id=item_id)

    # ==================== DELETE_TASK_VARIABLE OPERATION - Complete 4-Pattern ====================
    
    def delete_task_variable(self, task_id: str, variable_name: str) -> Any:
        """Delete Task Variable operation (sync)."""
        if not hasattr(self, '_delete_task_variable'):
            raise ImportError("Raw client operation not available")
        return self._delete_task_variable.sync(client=self.raw_client, task_id=task_id, variable_name=variable_name)
    
    async def delete_task_variable_async(self, task_id: str, variable_name: str) -> Any:
        """Delete Task Variable operation (async)."""
        if not hasattr(self, '_delete_task_variable'):
            raise ImportError("Raw client operation not available")
        return await self._delete_task_variable.asyncio(client=self.raw_client, task_id=task_id, variable_name=variable_name)
    
    def delete_task_variable_detailed(self, task_id: str, variable_name: str) -> Response:
        """Delete Task Variable operation (detailed sync)."""
        if not hasattr(self, '_delete_task_variable'):
            raise ImportError("Raw client operation not available")
        return self._delete_task_variable.sync_detailed(client=self.raw_client, task_id=task_id, variable_name=variable_name)
    
    async def delete_task_variable_detailed_async(self, task_id: str, variable_name: str) -> Response:
        """Delete Task Variable operation (detailed async)."""
        if not hasattr(self, '_delete_task_variable'):
            raise ImportError("Raw client operation not available")
        return await self._delete_task_variable.asyncio_detailed(client=self.raw_client, task_id=task_id, variable_name=variable_name)

    # ==================== GET_TASK OPERATION - Complete 4-Pattern ====================
    
    def get_task(self, task_id: str, properties: Union[Unset, Any] = UNSET) -> Any:
        """Get Task operation (sync)."""
        if not hasattr(self, '_get_task'):
            raise ImportError("Raw client operation not available")
        return self._get_task.sync(client=self.raw_client, task_id=task_id, properties=properties)
    
    async def get_task_async(self, task_id: str, properties: Union[Unset, Any] = UNSET) -> Any:
        """Get Task operation (async)."""
        if not hasattr(self, '_get_task'):
            raise ImportError("Raw client operation not available")
        return await self._get_task.asyncio(client=self.raw_client, task_id=task_id, properties=properties)
    
    def get_task_detailed(self, task_id: str, properties: Union[Unset, Any] = UNSET) -> Response:
        """Get Task operation (detailed sync)."""
        if not hasattr(self, '_get_task'):
            raise ImportError("Raw client operation not available")
        return self._get_task.sync_detailed(client=self.raw_client, task_id=task_id, properties=properties)
    
    async def get_task_detailed_async(self, task_id: str, properties: Union[Unset, Any] = UNSET) -> Response:
        """Get Task operation (detailed async)."""
        if not hasattr(self, '_get_task'):
            raise ImportError("Raw client operation not available")
        return await self._get_task.asyncio_detailed(client=self.raw_client, task_id=task_id, properties=properties)

    # ==================== GET_TASK_FORM_MODEL OPERATION - Complete 4-Pattern ====================
    
    def get_task_form_model(self, task_id: str, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET) -> Any:
        """Get Task Form Model operation (sync)."""
        if not hasattr(self, '_get_task_form_model'):
            raise ImportError("Raw client operation not available")
        return self._get_task_form_model.sync(client=self.raw_client, task_id=task_id, skip_count=skip_count, max_items=max_items, properties=properties)
    
    async def get_task_form_model_async(self, task_id: str, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET) -> Any:
        """Get Task Form Model operation (async)."""
        if not hasattr(self, '_get_task_form_model'):
            raise ImportError("Raw client operation not available")
        return await self._get_task_form_model.asyncio(client=self.raw_client, task_id=task_id, skip_count=skip_count, max_items=max_items, properties=properties)
    
    def get_task_form_model_detailed(self, task_id: str, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET) -> Response:
        """Get Task Form Model operation (detailed sync)."""
        if not hasattr(self, '_get_task_form_model'):
            raise ImportError("Raw client operation not available")
        return self._get_task_form_model.sync_detailed(client=self.raw_client, task_id=task_id, skip_count=skip_count, max_items=max_items, properties=properties)
    
    async def get_task_form_model_detailed_async(self, task_id: str, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET) -> Response:
        """Get Task Form Model operation (detailed async)."""
        if not hasattr(self, '_get_task_form_model'):
            raise ImportError("Raw client operation not available")
        return await self._get_task_form_model.asyncio_detailed(client=self.raw_client, task_id=task_id, skip_count=skip_count, max_items=max_items, properties=properties)

    # ==================== LIST_TASKS OPERATION - Complete 4-Pattern ====================
    
    def list_tasks(self, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET, order_by: Union[Unset, Any] = UNSET, where: Union[Unset, Any] = UNSET) -> Any:
        """List Tasks operation (sync)."""
        if not hasattr(self, '_list_tasks'):
            raise ImportError("Raw client operation not available")
        return self._list_tasks.sync(client=self.raw_client, skip_count=skip_count, max_items=max_items, properties=properties, order_by=order_by, where=where)
    
    async def list_tasks_async(self, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET, order_by: Union[Unset, Any] = UNSET, where: Union[Unset, Any] = UNSET) -> Any:
        """List Tasks operation (async)."""
        if not hasattr(self, '_list_tasks'):
            raise ImportError("Raw client operation not available")
        return await self._list_tasks.asyncio(client=self.raw_client, skip_count=skip_count, max_items=max_items, properties=properties, order_by=order_by, where=where)
    
    def list_tasks_detailed(self, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET, order_by: Union[Unset, Any] = UNSET, where: Union[Unset, Any] = UNSET) -> Response:
        """List Tasks operation (detailed sync)."""
        if not hasattr(self, '_list_tasks'):
            raise ImportError("Raw client operation not available")
        return self._list_tasks.sync_detailed(client=self.raw_client, skip_count=skip_count, max_items=max_items, properties=properties, order_by=order_by, where=where)
    
    async def list_tasks_detailed_async(self, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET, order_by: Union[Unset, Any] = UNSET, where: Union[Unset, Any] = UNSET) -> Response:
        """List Tasks operation (detailed async)."""
        if not hasattr(self, '_list_tasks'):
            raise ImportError("Raw client operation not available")
        return await self._list_tasks.asyncio_detailed(client=self.raw_client, skip_count=skip_count, max_items=max_items, properties=properties, order_by=order_by, where=where)

    # ==================== LIST_TASKS_FOR_PROCESS OPERATION - Complete 4-Pattern ====================
    
    def list_tasks_for_process(self, process_id: str, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET, order_by: Union[Unset, Any] = UNSET) -> Any:
        """List Tasks For Process operation (sync)."""
        if not hasattr(self, '_list_tasks_for_process'):
            raise ImportError("Raw client operation not available")
        return self._list_tasks_for_process.sync(client=self.raw_client, process_id=process_id, skip_count=skip_count, max_items=max_items, properties=properties, order_by=order_by)
    
    async def list_tasks_for_process_async(self, process_id: str, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET, order_by: Union[Unset, Any] = UNSET) -> Any:
        """List Tasks For Process operation (async)."""
        if not hasattr(self, '_list_tasks_for_process'):
            raise ImportError("Raw client operation not available")
        return await self._list_tasks_for_process.asyncio(client=self.raw_client, process_id=process_id, skip_count=skip_count, max_items=max_items, properties=properties, order_by=order_by)
    
    def list_tasks_for_process_detailed(self, process_id: str, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET, order_by: Union[Unset, Any] = UNSET) -> Response:
        """List Tasks For Process operation (detailed sync)."""
        if not hasattr(self, '_list_tasks_for_process'):
            raise ImportError("Raw client operation not available")
        return self._list_tasks_for_process.sync_detailed(client=self.raw_client, process_id=process_id, skip_count=skip_count, max_items=max_items, properties=properties, order_by=order_by)
    
    async def list_tasks_for_process_detailed_async(self, process_id: str, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET, order_by: Union[Unset, Any] = UNSET) -> Response:
        """List Tasks For Process operation (detailed async)."""
        if not hasattr(self, '_list_tasks_for_process'):
            raise ImportError("Raw client operation not available")
        return await self._list_tasks_for_process.asyncio_detailed(client=self.raw_client, process_id=process_id, skip_count=skip_count, max_items=max_items, properties=properties, order_by=order_by)

    # ==================== LIST_TASK_CANDIDATES OPERATION - Complete 4-Pattern ====================
    
    def list_task_candidates(self, task_id: str, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET) -> Any:
        """List Task Candidates operation (sync)."""
        if not hasattr(self, '_list_task_candidates'):
            raise ImportError("Raw client operation not available")
        return self._list_task_candidates.sync(client=self.raw_client, task_id=task_id, skip_count=skip_count, max_items=max_items, properties=properties)
    
    async def list_task_candidates_async(self, task_id: str, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET) -> Any:
        """List Task Candidates operation (async)."""
        if not hasattr(self, '_list_task_candidates'):
            raise ImportError("Raw client operation not available")
        return await self._list_task_candidates.asyncio(client=self.raw_client, task_id=task_id, skip_count=skip_count, max_items=max_items, properties=properties)
    
    def list_task_candidates_detailed(self, task_id: str, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET) -> Response:
        """List Task Candidates operation (detailed sync)."""
        if not hasattr(self, '_list_task_candidates'):
            raise ImportError("Raw client operation not available")
        return self._list_task_candidates.sync_detailed(client=self.raw_client, task_id=task_id, skip_count=skip_count, max_items=max_items, properties=properties)
    
    async def list_task_candidates_detailed_async(self, task_id: str, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET) -> Response:
        """List Task Candidates operation (detailed async)."""
        if not hasattr(self, '_list_task_candidates'):
            raise ImportError("Raw client operation not available")
        return await self._list_task_candidates.asyncio_detailed(client=self.raw_client, task_id=task_id, skip_count=skip_count, max_items=max_items, properties=properties)

    # ==================== LIST_TASK_ITEMS OPERATION - Complete 4-Pattern ====================
    
    def list_task_items(self, task_id: str, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET) -> Any:
        """List Task Items operation (sync)."""
        if not hasattr(self, '_list_task_items'):
            raise ImportError("Raw client operation not available")
        return self._list_task_items.sync(client=self.raw_client, task_id=task_id, skip_count=skip_count, max_items=max_items, properties=properties)
    
    async def list_task_items_async(self, task_id: str, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET) -> Any:
        """List Task Items operation (async)."""
        if not hasattr(self, '_list_task_items'):
            raise ImportError("Raw client operation not available")
        return await self._list_task_items.asyncio(client=self.raw_client, task_id=task_id, skip_count=skip_count, max_items=max_items, properties=properties)
    
    def list_task_items_detailed(self, task_id: str, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET) -> Response:
        """List Task Items operation (detailed sync)."""
        if not hasattr(self, '_list_task_items'):
            raise ImportError("Raw client operation not available")
        return self._list_task_items.sync_detailed(client=self.raw_client, task_id=task_id, skip_count=skip_count, max_items=max_items, properties=properties)
    
    async def list_task_items_detailed_async(self, task_id: str, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET) -> Response:
        """List Task Items operation (detailed async)."""
        if not hasattr(self, '_list_task_items'):
            raise ImportError("Raw client operation not available")
        return await self._list_task_items.asyncio_detailed(client=self.raw_client, task_id=task_id, skip_count=skip_count, max_items=max_items, properties=properties)

    # ==================== LIST_TASK_VARIABLES OPERATION - Complete 4-Pattern ====================
    
    def list_task_variables(self, task_id: str, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET, where: Union[Unset, Any] = UNSET) -> Any:
        """List Task Variables operation (sync)."""
        if not hasattr(self, '_list_task_variables'):
            raise ImportError("Raw client operation not available")
        return self._list_task_variables.sync(client=self.raw_client, task_id=task_id, skip_count=skip_count, max_items=max_items, properties=properties, where=where)
    
    async def list_task_variables_async(self, task_id: str, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET, where: Union[Unset, Any] = UNSET) -> Any:
        """List Task Variables operation (async)."""
        if not hasattr(self, '_list_task_variables'):
            raise ImportError("Raw client operation not available")
        return await self._list_task_variables.asyncio(client=self.raw_client, task_id=task_id, skip_count=skip_count, max_items=max_items, properties=properties, where=where)
    
    def list_task_variables_detailed(self, task_id: str, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET, where: Union[Unset, Any] = UNSET) -> Response:
        """List Task Variables operation (detailed sync)."""
        if not hasattr(self, '_list_task_variables'):
            raise ImportError("Raw client operation not available")
        return self._list_task_variables.sync_detailed(client=self.raw_client, task_id=task_id, skip_count=skip_count, max_items=max_items, properties=properties, where=where)
    
    async def list_task_variables_detailed_async(self, task_id: str, skip_count: Union[Unset, Any] = UNSET, max_items: Union[Unset, Any] = UNSET, properties: Union[Unset, Any] = UNSET, where: Union[Unset, Any] = UNSET) -> Response:
        """List Task Variables operation (detailed async)."""
        if not hasattr(self, '_list_task_variables'):
            raise ImportError("Raw client operation not available")
        return await self._list_task_variables.asyncio_detailed(client=self.raw_client, task_id=task_id, skip_count=skip_count, max_items=max_items, properties=properties, where=where)

    # ==================== UPDATE_TASK OPERATION - Complete 4-Pattern ====================
    
    def update_task(self, task_id: str, body: TaskBody = UNSET, select: Union[Unset, Any] = UNSET) -> Any:
        """Update Task operation (sync)."""
        if not hasattr(self, '_update_task'):
            raise ImportError("Raw client operation not available")
        return self._update_task.sync(client=self.raw_client, task_id=task_id, body=body, select=select)
    
    async def update_task_async(self, task_id: str, body: TaskBody = UNSET, select: Union[Unset, Any] = UNSET) -> Any:
        """Update Task operation (async)."""
        if not hasattr(self, '_update_task'):
            raise ImportError("Raw client operation not available")
        return await self._update_task.asyncio(client=self.raw_client, task_id=task_id, body=body, select=select)
    
    def update_task_detailed(self, task_id: str, body: TaskBody = UNSET, select: Union[Unset, Any] = UNSET) -> Response:
        """Update Task operation (detailed sync)."""
        if not hasattr(self, '_update_task'):
            raise ImportError("Raw client operation not available")
        return self._update_task.sync_detailed(client=self.raw_client, task_id=task_id, body=body, select=select)
    
    async def update_task_detailed_async(self, task_id: str, body: TaskBody = UNSET, select: Union[Unset, Any] = UNSET) -> Response:
        """Update Task operation (detailed async)."""
        if not hasattr(self, '_update_task'):
            raise ImportError("Raw client operation not available")
        return await self._update_task.asyncio_detailed(client=self.raw_client, task_id=task_id, body=body, select=select)

    # ==================== UPDATE_TASK_VARIABLE OPERATION - Complete 4-Pattern ====================
    
    def update_task_variable(self, task_id: str, variable_name: str, body: Variable = UNSET) -> Any:
        """Update Task Variable operation (sync)."""
        if not hasattr(self, '_update_task_variable'):
            raise ImportError("Raw client operation not available")
        return self._update_task_variable.sync(client=self.raw_client, task_id=task_id, variable_name=variable_name, body=body)
    
    async def update_task_variable_async(self, task_id: str, variable_name: str, body: Variable = UNSET) -> Any:
        """Update Task Variable operation (async)."""
        if not hasattr(self, '_update_task_variable'):
            raise ImportError("Raw client operation not available")
        return await self._update_task_variable.asyncio(client=self.raw_client, task_id=task_id, variable_name=variable_name, body=body)
    
    def update_task_variable_detailed(self, task_id: str, variable_name: str, body: Variable = UNSET) -> Response:
        """Update Task Variable operation (detailed sync)."""
        if not hasattr(self, '_update_task_variable'):
            raise ImportError("Raw client operation not available")
        return self._update_task_variable.sync_detailed(client=self.raw_client, task_id=task_id, variable_name=variable_name, body=body)
    
    async def update_task_variable_detailed_async(self, task_id: str, variable_name: str, body: Variable = UNSET) -> Response:
        """Update Task Variable operation (detailed async)."""
        if not hasattr(self, '_update_task_variable'):
            raise ImportError("Raw client operation not available")
        return await self._update_task_variable.asyncio_detailed(client=self.raw_client, task_id=task_id, variable_name=variable_name, body=body)

    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self.parent_client._client_factory, 'base_url', 'unknown')
        return f"TasksClient(base_url='{base_url}')" 
