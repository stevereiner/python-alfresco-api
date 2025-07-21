"""
ProcessDefinitions Operations Client - Level 3: ProcessDefinitions-Specific Operations

This module provides process_definitions-specific operations within the Workflow API.
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
from ....raw_clients.alfresco_workflow_client.workflow_client.models.process_definition_entry import ProcessDefinitionEntry
from ....raw_clients.alfresco_workflow_client.workflow_client.models.process_definition_paging import ProcessDefinitionPaging
from ....raw_clients.alfresco_workflow_client.workflow_client.models.task_form_model_paging import TaskFormModelPaging

# Import from Level 3 (operation-specific models)
from .models import ProcessDefinitionsResponse, ProcessDefinitionsListResponse, CreateProcessDefinitionsRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_workflow_client.workflow_client.api.process_definitions import (
            get_process_definition as _get_process_definition,
            get_process_definition_image as _get_process_definition_image,
            get_process_definition_start_form_model as _get_process_definition_start_form_model,
            list_process_definitions as _list_process_definitions
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class ProcessDefinitionsClient:
    """
    ProcessDefinitions operations client with 4-pattern detailed functions.
    
    Clean Tier 3 implementation with different name from AlfrescoWorkflowClient.
    Provides high-level methods for process_definitions management operations
    that are essential for MCP servers and process_definitions workflows.
    
    Each operation has 4 variants for maximum flexibility:
    - Basic sync/async for simple use cases
    - Detailed sync/async for full HTTP response access
    """
    
    def __init__(self, client_factory):
        """Initialize with client factory for raw client access."""
        self._client_factory = client_factory
        self._raw_client = None
        
        # Store raw operation references
        if RAW_OPERATIONS_AVAILABLE:
            self._get_process_definition = _get_process_definition
            self._get_process_definition_image = _get_process_definition_image
            self._get_process_definition_start_form_model = _get_process_definition_start_form_model
            self._list_process_definitions = _list_process_definitions
    
    def _get_raw_client(self):
        """Get or create the raw client."""
        if self._raw_client is None:
            # Import the raw client directly
            from ....raw_clients.alfresco_workflow_client.workflow_client.client import AuthenticatedClient
            
            # Create the raw client with same auth setup
            self._raw_client = AuthenticatedClient(
                base_url=f"{self._client_factory.base_url}/alfresco/api/workflow/versions/1",
                token=self._client_factory.auth.get_auth_token(),
                prefix=self._client_factory.auth.get_auth_prefix(),
                verify_ssl=self._client_factory.verify_ssl
            )
        return self._raw_client
    
    def get_httpx_client(self):
        """
        Get direct access to raw httpx client for advanced operations.
        
        Perfect for MCP servers that need raw HTTP access.
        """
        return self._get_raw_client().get_httpx_client()
    
    # ==================== 4-PATTERN OPERATIONS ====================

    # ==================== GET_PROCESS_DEFINITION OPERATION - Complete 4-Pattern ====================
    
    def get_process_definition(self, process_definition_id: str, properties: Union[Unset, Any] = UNSET) -> Any:
        """
        Get Process Definition operation (sync).
        
        Perfect for MCP servers and process_definitions workflows.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise RuntimeError("Raw operations not available - check client installation")
        
        return self._get_process_definition.sync(
            process_definition_id=process_definition_id,
            properties=properties,
            client=self._get_raw_client()
        )
    
    async def get_process_definition_async(self, process_definition_id: str, properties: Union[Unset, Any] = UNSET) -> Any:
        """
        Get Process Definition operation (async).
        
        Perfect for async MCP servers and process_definitions workflows.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise RuntimeError("Raw operations not available - check client installation")
        
        return await self._get_process_definition.asyncio(
            process_definition_id=process_definition_id,
            properties=properties,
            client=self._get_raw_client()
        )
    
    def get_process_definition_detailed(self, process_definition_id: str, properties: Union[Unset, Any] = UNSET) -> Response:
        """
        Get Process Definition operation (detailed sync).
        
        Returns the full HTTP response for advanced processing.
        Perfect for MCP servers needing response headers, status codes, etc.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise RuntimeError("Raw operations not available - check client installation")
        
        return self._get_process_definition.sync_detailed(
            process_definition_id=process_definition_id,
            properties=properties,
            client=self._get_raw_client()
        )
    
    async def get_process_definition_detailed_async(self, process_definition_id: str, properties: Union[Unset, Any] = UNSET) -> Response:
        """
        Get Process Definition operation (detailed async).
        
        Returns the full HTTP response for advanced processing.
        Perfect for async MCP servers needing response headers, status codes, etc.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise RuntimeError("Raw operations not available - check client installation")
        
        return await self._get_process_definition.asyncio_detailed(
            process_definition_id=process_definition_id,
            properties=properties,
            client=self._get_raw_client()
        )

    # ==================== GET_PROCESS_DEFINITION_IMAGE OPERATION - Complete 4-Pattern ====================
    
    def get_process_definition_image(self, process_definition_id: str) -> Any:
        """
        Get Process Definition Image operation (sync).
        
        Perfect for MCP servers and process_definitions workflows.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise RuntimeError("Raw operations not available - check client installation")
        
        return self._get_process_definition_image.sync(
            process_definition_id=process_definition_id,
            client=self._get_raw_client()
        )
    
    async def get_process_definition_image_async(self, process_definition_id: str) -> Any:
        """
        Get Process Definition Image operation (async).
        
        Perfect for async MCP servers and process_definitions workflows.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise RuntimeError("Raw operations not available - check client installation")
        
        return await self._get_process_definition_image.asyncio(
            process_definition_id=process_definition_id,
            client=self._get_raw_client()
        )
    
    def get_process_definition_image_detailed(self, process_definition_id: str) -> Response:
        """
        Get Process Definition Image operation (detailed sync).
        
        Returns the full HTTP response for advanced processing.
        Perfect for MCP servers needing response headers, status codes, etc.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise RuntimeError("Raw operations not available - check client installation")
        
        return self._get_process_definition_image.sync_detailed(
            process_definition_id=process_definition_id,
            client=self._get_raw_client()
        )
    
    async def get_process_definition_image_detailed_async(self, process_definition_id: str) -> Response:
        """
        Get Process Definition Image operation (detailed async).
        
        Returns the full HTTP response for advanced processing.
        Perfect for async MCP servers needing response headers, status codes, etc.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise RuntimeError("Raw operations not available - check client installation")
        
        return await self._get_process_definition_image.asyncio_detailed(
            process_definition_id=process_definition_id,
            client=self._get_raw_client()
        )

    # ==================== GET_PROCESS_DEFINITION_START_FORM_MODEL OPERATION - Complete 4-Pattern ====================
    
    def get_process_definition_start_form_model(self, process_definition_id: str) -> Any:
        """
        Get Process Definition Start Form Model operation (sync).
        
        Perfect for MCP servers and process_definitions workflows.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise RuntimeError("Raw operations not available - check client installation")
        
        return self._get_process_definition_start_form_model.sync(
            process_definition_id=process_definition_id,
            client=self._get_raw_client()
        )
    
    async def get_process_definition_start_form_model_async(self, process_definition_id: str) -> Any:
        """
        Get Process Definition Start Form Model operation (async).
        
        Perfect for async MCP servers and process_definitions workflows.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise RuntimeError("Raw operations not available - check client installation")
        
        return await self._get_process_definition_start_form_model.asyncio(
            process_definition_id=process_definition_id,
            client=self._get_raw_client()
        )
    
    def get_process_definition_start_form_model_detailed(self, process_definition_id: str) -> Response:
        """
        Get Process Definition Start Form Model operation (detailed sync).
        
        Returns the full HTTP response for advanced processing.
        Perfect for MCP servers needing response headers, status codes, etc.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise RuntimeError("Raw operations not available - check client installation")
        
        return self._get_process_definition_start_form_model.sync_detailed(
            process_definition_id=process_definition_id,
            client=self._get_raw_client()
        )
    
    async def get_process_definition_start_form_model_detailed_async(self, process_definition_id: str) -> Response:
        """
        Get Process Definition Start Form Model operation (detailed async).
        
        Returns the full HTTP response for advanced processing.
        Perfect for async MCP servers needing response headers, status codes, etc.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise RuntimeError("Raw operations not available - check client installation")
        
        return await self._get_process_definition_start_form_model.asyncio_detailed(
            process_definition_id=process_definition_id,
            client=self._get_raw_client()
        )

    # ==================== LIST_PROCESS_DEFINITIONS OPERATION - Complete 4-Pattern ====================
    
    def list_process_definitions(self, skip_count: Union[Unset, int] = UNSET, max_items: Union[Unset, int] = UNSET, deployment_id: Union[Unset, str] = UNSET, name: Union[Unset, str] = UNSET, name_like: Union[Unset, str] = UNSET, category: Union[Unset, str] = UNSET, category_not_equals: Union[Unset, str] = UNSET, key: Union[Unset, str] = UNSET, key_like: Union[Unset, str] = UNSET, resource_name: Union[Unset, str] = UNSET, resource_name_like: Union[Unset, str] = UNSET, version: Union[Unset, int] = UNSET, latest: Union[Unset, bool] = UNSET, suspended: Union[Unset, bool] = UNSET, sort: Union[Unset, str] = UNSET, properties: Union[Unset, Any] = UNSET, include: Union[Unset, List[str]] = UNSET) -> Any:
        """
        List Process Definitions operation (sync).
        
        Perfect for MCP servers and process_definitions workflows.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise RuntimeError("Raw operations not available - check client installation")
        
        return self._list_process_definitions.sync(
            skip_count=skip_count,
            max_items=max_items,
            deployment_id=deployment_id,
            name=name,
            name_like=name_like,
            category=category,
            category_not_equals=category_not_equals,
            key=key,
            key_like=key_like,
            resource_name=resource_name,
            resource_name_like=resource_name_like,
            version=version,
            latest=latest,
            suspended=suspended,
            sort=sort,
            properties=properties,
            include=include,
            client=self._get_raw_client()
        )
    
    async def list_process_definitions_async(self, skip_count: Union[Unset, int] = UNSET, max_items: Union[Unset, int] = UNSET, deployment_id: Union[Unset, str] = UNSET, name: Union[Unset, str] = UNSET, name_like: Union[Unset, str] = UNSET, category: Union[Unset, str] = UNSET, category_not_equals: Union[Unset, str] = UNSET, key: Union[Unset, str] = UNSET, key_like: Union[Unset, str] = UNSET, resource_name: Union[Unset, str] = UNSET, resource_name_like: Union[Unset, str] = UNSET, version: Union[Unset, int] = UNSET, latest: Union[Unset, bool] = UNSET, suspended: Union[Unset, bool] = UNSET, sort: Union[Unset, str] = UNSET, properties: Union[Unset, Any] = UNSET, include: Union[Unset, List[str]] = UNSET) -> Any:
        """
        List Process Definitions operation (async).
        
        Perfect for async MCP servers and process_definitions workflows.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise RuntimeError("Raw operations not available - check client installation")
        
        return await self._list_process_definitions.asyncio(
            skip_count=skip_count,
            max_items=max_items,
            deployment_id=deployment_id,
            name=name,
            name_like=name_like,
            category=category,
            category_not_equals=category_not_equals,
            key=key,
            key_like=key_like,
            resource_name=resource_name,
            resource_name_like=resource_name_like,
            version=version,
            latest=latest,
            suspended=suspended,
            sort=sort,
            properties=properties,
            include=include,
            client=self._get_raw_client()
        )
    
    def list_process_definitions_detailed(self, skip_count: Union[Unset, int] = UNSET, max_items: Union[Unset, int] = UNSET, deployment_id: Union[Unset, str] = UNSET, name: Union[Unset, str] = UNSET, name_like: Union[Unset, str] = UNSET, category: Union[Unset, str] = UNSET, category_not_equals: Union[Unset, str] = UNSET, key: Union[Unset, str] = UNSET, key_like: Union[Unset, str] = UNSET, resource_name: Union[Unset, str] = UNSET, resource_name_like: Union[Unset, str] = UNSET, version: Union[Unset, int] = UNSET, latest: Union[Unset, bool] = UNSET, suspended: Union[Unset, bool] = UNSET, sort: Union[Unset, str] = UNSET, properties: Union[Unset, Any] = UNSET, include: Union[Unset, List[str]] = UNSET) -> Response:
        """
        List Process Definitions operation (detailed sync).
        
        Returns the full HTTP response for advanced processing.
        Perfect for MCP servers needing response headers, status codes, etc.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise RuntimeError("Raw operations not available - check client installation")
        
        return self._list_process_definitions.sync_detailed(
            skip_count=skip_count,
            max_items=max_items,
            deployment_id=deployment_id,
            name=name,
            name_like=name_like,
            category=category,
            category_not_equals=category_not_equals,
            key=key,
            key_like=key_like,
            resource_name=resource_name,
            resource_name_like=resource_name_like,
            version=version,
            latest=latest,
            suspended=suspended,
            sort=sort,
            properties=properties,
            include=include,
            client=self._get_raw_client()
        )
    
    async def list_process_definitions_detailed_async(self, skip_count: Union[Unset, int] = UNSET, max_items: Union[Unset, int] = UNSET, deployment_id: Union[Unset, str] = UNSET, name: Union[Unset, str] = UNSET, name_like: Union[Unset, str] = UNSET, category: Union[Unset, str] = UNSET, category_not_equals: Union[Unset, str] = UNSET, key: Union[Unset, str] = UNSET, key_like: Union[Unset, str] = UNSET, resource_name: Union[Unset, str] = UNSET, resource_name_like: Union[Unset, str] = UNSET, version: Union[Unset, int] = UNSET, latest: Union[Unset, bool] = UNSET, suspended: Union[Unset, bool] = UNSET, sort: Union[Unset, str] = UNSET, properties: Union[Unset, Any] = UNSET, include: Union[Unset, List[str]] = UNSET) -> Response:
        """
        List Process Definitions operation (detailed async).
        
        Returns the full HTTP response for advanced processing.
        Perfect for async MCP servers needing response headers, status codes, etc.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise RuntimeError("Raw operations not available - check client installation")
        
        return await self._list_process_definitions.asyncio_detailed(
            skip_count=skip_count,
            max_items=max_items,
            deployment_id=deployment_id,
            name=name,
            name_like=name_like,
            category=category,
            category_not_equals=category_not_equals,
            key=key,
            key_like=key_like,
            resource_name=resource_name,
            resource_name_like=resource_name_like,
            version=version,
            latest=latest,
            suspended=suspended,
            sort=sort,
            properties=properties,
            include=include,
            client=self._get_raw_client()
        ) 