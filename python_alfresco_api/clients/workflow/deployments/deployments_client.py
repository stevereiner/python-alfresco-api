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
    
    def __init__(self, client_factory):
        """Initialize with client factory for raw client access."""
        self._client_factory = client_factory
        self._raw_client = None
        
        # Store raw operation references
        if RAW_OPERATIONS_AVAILABLE:
            self._delete_deployment = _delete_deployment
            self._get_deployment = _get_deployment
            self._list_deployments = _list_deployments
    
    def _get_raw_client(self):
        """Get or create the raw client."""
        if self._raw_client is None:
            # Import the raw workflow client directly
            from ....raw_clients.alfresco_workflow_client.workflow_client.client import AuthenticatedClient
            
            # Create the raw client with same auth setup
            self._raw_client = AuthenticatedClient(
                base_url=f"{self._client_factory.base_url}/alfresco/api/-default-/public/workflow/versions/1",
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
    
    # Placeholder for deployments operations - will be populated from the original file
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self._client_factory, 'base_url', 'unknown')
        return f"AlfrescoDeploymentsClient(base_url='{base_url}')" 