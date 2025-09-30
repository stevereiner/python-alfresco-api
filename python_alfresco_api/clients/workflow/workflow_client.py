"""
Alfresco Workflow API Client - V1.1 Three-Tier Architecture

Provides access to Workflow API operations with lazy loading and hierarchical organization.
"""

import asyncio
from typing import Optional
from httpx import Response

# Import from Level 2 models
from .models import WorkflowResponse, WorkflowRequest


class AlfrescoWorkflowClient:
    """
    Workflow operations client with lazy-loaded subsections.
    
    Provides high-level methods for Process and task management
    that are essential for MCP servers and workflow workflows.
    """
    
    def __init__(self, client_factory):
        """Initialize with client factory for raw client access."""
        self._client_factory = client_factory
        
        # Lazy-loaded subsection clients
        self._deployments = None
        self._process_definitions = None
        self._processes = None
        self._tasks = None
        
        # Client instances - initialized on first access
        self._raw_client = None
        self._httpx_client = None
    
    # =================================================================
    # STANDARD CLIENT ACCESS PATTERN - V1.1
    # =================================================================
    
    @property
    def raw_client(self):
        """
        Get the raw authenticated client for advanced operations.
        
        This is the STANDARD way to access the underlying client.
        """
        if self._raw_client is None:
            self._raw_client = self._create_raw_client()
        return self._raw_client
    
    @property
    def httpx_client(self):
        """
        Get direct access to httpx client for raw HTTP operations.
        
        This is the STANDARD way to access the HTTP client.
        Perfect for MCP servers that need raw HTTP access.
        """
        if self._httpx_client is None:
            self._httpx_client = self._create_httpx_client()
        return self._httpx_client
    
    @property
    def is_initialized(self) -> bool:
        """
        Check if the client is initialized and functional.
        
        This is the STANDARD way to check initialization status.
        """
        try:
            # Try to access raw client to test initialization
            _ = self.raw_client
            return True
        except Exception:
            return False
    
    def _create_raw_client(self):
        """
        Create the raw authenticated client.
        
        This is INTERNAL - use raw_client property instead.
        """
        from ...raw_clients.alfresco_workflow_client.workflow_client.client import AuthenticatedClient
        
        # Prepare client arguments
        client_kwargs = {
            "base_url": f"{self._client_factory.base_url}/alfresco/api/-default-/public/workflow/versions/1",
            "token": self._client_factory.auth.get_auth_token(),
            "prefix": self._client_factory.auth.get_auth_prefix(),
            "verify_ssl": self._client_factory.verify_ssl
        }
        
        # Only add timeout if specified (not None)
        if self._client_factory.timeout is not None:
            client_kwargs["timeout"] = self._client_factory.timeout
        
        return AuthenticatedClient(**client_kwargs)
    
    def _create_httpx_client(self):
        """
        Create the httpx client for direct HTTP operations.
        
        This is INTERNAL - use httpx_client property instead.
        """
        return self.raw_client.get_httpx_client()

    # =================================================================
    # DEPRECATED METHODS - FOR BACKWARD COMPATIBILITY
    # =================================================================
    
    def get_httpx_client(self):
        """
        DEPRECATED: Use httpx_client property instead.
        
        This method is kept for backward compatibility only.
        """
        return self.httpx_client

    def get_httpx_client_detailed(self):
        """
        DEPRECATED: Use httpx_client property instead.
        
        This method is kept for backward compatibility only.
        """
        return self.httpx_client

    async def get_httpx_client_detailed_async(self):
        """
        DEPRECATED: Use httpx_client property instead.
        
        This method is kept for backward compatibility only.
        """
        return self.httpx_client

    # =================================================================
    # SUBSECTION PROPERTIES
    # =================================================================
    
    @property
    def available(self) -> bool:
        """Check if the workflow client is available and functional."""
        return self.is_initialized
    
    @property
    def deployments(self):
        """Get the deployments operations client."""
        if self._deployments is None:
            # Lazy load the deployments client with graceful error handling
            try:
                from .deployments import DeploymentsClient
                self._deployments = DeploymentsClient(self._client_factory)
            except ImportError as e:
                print(f"⚠️  Deployments subclient unavailable: {e}")
                return None
        return self._deployments
    
    @property
    def process_definitions(self):
        """Get the process definitions operations client."""
        if self._process_definitions is None:
            # Lazy load the process definitions client with graceful error handling
            try:
                from .process_definitions import ProcessDefinitionsClient
                self._process_definitions = ProcessDefinitionsClient(self._client_factory)
            except ImportError as e:
                print(f"⚠️  Process definitions subclient unavailable: {e}")
                return None
        return self._process_definitions
    
    @property
    def processes(self):
        """Get the processes operations client."""
        if self._processes is None:
            # Lazy load the processes client with graceful error handling
            try:
                from .processes import ProcessesClient
                self._processes = ProcessesClient(self._client_factory)
            except ImportError as e:
                print(f"⚠️  Processes subclient unavailable: {e}")
                return None
        return self._processes
    
    @property
    def tasks(self):
        """Get the tasks operations client."""
        if self._tasks is None:
            # Lazy load the tasks client with graceful error handling
            try:
                from .tasks import TasksClient
                self._tasks = TasksClient(self._client_factory)
            except ImportError as e:
                print(f"⚠️  Tasks subclient unavailable: {e}")
                return None
        return self._tasks
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self._client_factory, 'base_url', 'unknown')
        return f"AlfrescoWorkflowClient(base_url='{base_url}')"

# Export the main client class and all lazy-loaded sub-modules
__all__ = [
    'AlfrescoWorkflowClient',
    # Lazy-loaded sub-clients (accessed via properties)
    'deployments', 'process_definitions', 'processes', 'tasks'
] 