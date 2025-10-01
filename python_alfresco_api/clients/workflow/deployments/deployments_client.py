"""
Deployments Operations Client - Level 3: Deployments-Specific Operations

This module provides deployments-specific operations within the Workflow API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.
"""

import asyncio
from typing import Optional, List, Union, Any, Awaitable
from httpx import Response

# Import required types for proper parameter handling
from ....raw_clients.alfresco_workflow_client.workflow_client.types import UNSET, Unset
from httpx import Response

# Import model types for proper parameter signatures
from ....raw_clients.alfresco_workflow_client.workflow_client.models.deployment_entry import DeploymentEntry
from ....raw_clients.alfresco_workflow_client.workflow_client.models.deployment_paging import DeploymentPaging

# Import from Level 3 (operation-specific models)
from .models import DeploymentsResponse, DeploymentsListResponse, CreateDeploymentsRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_workflow_client.workflow_client.api.deployments import (
            delete_deployment as _delete_deployment,
            get_deployment as _get_deployment,
            list_deployments as _list_deployments
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class DeploymentsClient:
    """
    Deployments operations client with 4-pattern detailed functions.
    
    Provides high-level methods for deployments management operations
    that are essential for MCP servers and deployments workflows.
    
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
            self._delete_deployment = _delete_deployment
            self._get_deployment = _get_deployment
            self._list_deployments = _list_deployments
    
    @property
    def raw_client(self):
        """Delegate to parent client's raw client."""
        return self.parent_client.raw_client
    
    @property
    def httpx_client(self):
        """Delegate to parent client's httpx client."""
        return self.parent_client.httpx_client
    
    # =================================================================
    # DEPLOYMENT OPERATIONS - 4-PATTERN IMPLEMENTATION
    # =================================================================
    
    def list_deployments(
        self,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        properties: Optional[List[str]] = None
    ) -> Optional[Any]:
        """
        List deployments (sync).
        
        Gets a list of deployments. Requires admin role.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw deployment operations not available")
        
        from ....raw_clients.alfresco_workflow_client.workflow_client.types import UNSET
        
        return self._list_deployments.sync(
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            properties=properties if properties is not None else UNSET
        )
    
    async def list_deployments_async(
        self,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        properties: Optional[List[str]] = None
    ) -> Optional[Any]:
        """
        List deployments (async).
        
        Gets a list of deployments. Requires admin role.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw deployment operations not available")
        
        from ....raw_clients.alfresco_workflow_client.workflow_client.types import UNSET
        
        return await self._list_deployments.asyncio(
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            properties=properties if properties is not None else UNSET
        )
    
    def list_deployments_detailed(
        self,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        properties: Optional[List[str]] = None
    ) -> Response:
        """
        List deployments (detailed sync).
        
        Gets a list of deployments with full HTTP response.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw deployment operations not available")
        
        from ....raw_clients.alfresco_workflow_client.workflow_client.types import UNSET
        
        return self._list_deployments.sync_detailed(
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            properties=properties if properties is not None else UNSET
        )
    
    async def list_deployments_detailed_async(
        self,
        skip_count: Optional[int] = None,
        max_items: Optional[int] = None,
        properties: Optional[List[str]] = None
    ) -> Response:
        """
        List deployments (detailed async).
        
        Gets a list of deployments with full HTTP response.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw deployment operations not available")
        
        from ....raw_clients.alfresco_workflow_client.workflow_client.types import UNSET
        
        return await self._list_deployments.asyncio_detailed(
            client=self.raw_client,
            skip_count=skip_count if skip_count is not None else UNSET,
            max_items=max_items if max_items is not None else UNSET,
            properties=properties if properties is not None else UNSET
        )
    
    def get_deployment(
        self,
        deployment_id: str,
        properties: Optional[List[str]] = None
    ) -> Optional[Any]:
        """
        Get deployment details (sync).
        
        Gets details for a specific deployment.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw deployment operations not available")
        
        from ....raw_clients.alfresco_workflow_client.workflow_client.types import UNSET
        
        return self._get_deployment.sync(
            deployment_id=deployment_id,
            client=self.raw_client,
            properties=properties if properties is not None else UNSET
        )
    
    async def get_deployment_async(
        self,
        deployment_id: str,
        properties: Optional[List[str]] = None
    ) -> Optional[Any]:
        """
        Get deployment details (async).
        
        Gets details for a specific deployment.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw deployment operations not available")
        
        from ....raw_clients.alfresco_workflow_client.workflow_client.types import UNSET
        
        return await self._get_deployment.asyncio(
            deployment_id=deployment_id,
            client=self.raw_client,
            properties=properties if properties is not None else UNSET
        )
    
    def get_deployment_detailed(
        self,
        deployment_id: str,
        properties: Optional[List[str]] = None
    ) -> Response:
        """
        Get deployment details (detailed sync).
        
        Gets details for a specific deployment with full HTTP response.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw deployment operations not available")
        
        from ....raw_clients.alfresco_workflow_client.workflow_client.types import UNSET
        
        return self._get_deployment.sync_detailed(
            deployment_id=deployment_id,
            client=self.raw_client,
            properties=properties if properties is not None else UNSET
        )
    
    async def get_deployment_detailed_async(
        self,
        deployment_id: str,
        properties: Optional[List[str]] = None
    ) -> Response:
        """
        Get deployment details (detailed async).
        
        Gets details for a specific deployment with full HTTP response.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw deployment operations not available")
        
        from ....raw_clients.alfresco_workflow_client.workflow_client.types import UNSET
        
        return await self._get_deployment.asyncio_detailed(
            deployment_id=deployment_id,
            client=self.raw_client,
            properties=properties if properties is not None else UNSET
        )
    
    def delete_deployment(
        self,
        deployment_id: str
    ) -> Optional[Any]:
        """
        Delete deployment (sync).
        
        Deletes a specific deployment. Requires admin role.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw deployment operations not available")
        
        return self._delete_deployment.sync(
            deployment_id=deployment_id,
            client=self.raw_client
        )
    
    async def delete_deployment_async(
        self,
        deployment_id: str
    ) -> Optional[Any]:
        """
        Delete deployment (async).
        
        Deletes a specific deployment. Requires admin role.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw deployment operations not available")
        
        return await self._delete_deployment.asyncio(
            deployment_id=deployment_id,
            client=self.raw_client
        )
    
    def delete_deployment_detailed(
        self,
        deployment_id: str
    ) -> Response:
        """
        Delete deployment (detailed sync).
        
        Deletes a specific deployment with full HTTP response.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw deployment operations not available")
        
        return self._delete_deployment.sync_detailed(
            deployment_id=deployment_id,
            client=self.raw_client
        )
    
    async def delete_deployment_detailed_async(
        self,
        deployment_id: str
    ) -> Response:
        """
        Delete deployment (detailed async).
        
        Deletes a specific deployment with full HTTP response.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw deployment operations not available")
        
        return await self._delete_deployment.asyncio_detailed(
            deployment_id=deployment_id,
            client=self.raw_client
        )
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self.parent_client._client_factory, 'base_url', 'unknown')
        return f"AlfrescoDeploymentsClient(base_url='{base_url}')" 