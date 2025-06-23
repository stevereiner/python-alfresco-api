"""
Client Factory for Alfresco APIs

Provides easy instantiation of individual clients with shared configuration.
Perfect for enterprise applications and microservices.
"""

from typing import Optional, Dict, Any
from .auth_util import AuthUtil
from .clients.auth_client import AlfrescoAuthClient
from .clients.core_client import AlfrescoCoreClient
from .clients.discovery_client import AlfrescoDiscoveryClient
from .clients.search_client import AlfrescoSearchClient
from .clients.workflow_client import AlfrescoWorkflowClient
from .clients.model_client import AlfrescoModelClient
from .clients.search_sql_client import AlfrescoSearchSQLClient

class ClientFactory:
    """
    Factory for creating Alfresco API clients.

    Supports both individual client creation and shared authentication.
    """

    def __init__(
        self,
        base_url: str,
        username: Optional[str] = None,
        password: Optional[str] = None,
        verify_ssl: bool = True,
        timeout: int = 30
    ):
        """
        Initialize the client factory.

        Args:
            base_url: Base URL of Alfresco instance
            username: Optional username for authentication
            password: Optional password for authentication
            verify_ssl: Whether to verify SSL certificates
            timeout: Request timeout in seconds
        """
        self.base_url = base_url
        self.verify_ssl = verify_ssl
        self.timeout = timeout

        # Initialize auth utility if credentials provided
        self.auth = None
        if username and password:
            self.auth = AuthUtil(base_url, username, password, verify_ssl, timeout)

    def create_auth_client(self) -> AlfrescoAuthClient:
        """Create Authentication API client"""
        return AlfrescoAuthClient(self.base_url, self.auth, self.verify_ssl, self.timeout)

    def create_core_client(self) -> AlfrescoCoreClient:
        """Create Core API client"""
        return AlfrescoCoreClient(self.base_url, self.auth, self.verify_ssl, self.timeout)

    def create_discovery_client(self) -> AlfrescoDiscoveryClient:
        """Create Discovery API client"""
        return AlfrescoDiscoveryClient(self.base_url, self.auth, self.verify_ssl, self.timeout)

    def create_search_client(self) -> AlfrescoSearchClient:
        """Create Search API client"""
        return AlfrescoSearchClient(self.base_url, self.auth, self.verify_ssl, self.timeout)

    def create_workflow_client(self) -> AlfrescoWorkflowClient:
        """Create Workflow API client"""
        return AlfrescoWorkflowClient(self.base_url, self.auth, self.verify_ssl, self.timeout)

    def create_model_client(self) -> AlfrescoModelClient:
        """Create Model API client"""
        return AlfrescoModelClient(self.base_url, self.auth, self.verify_ssl, self.timeout)

    def create_search_sql_client(self) -> AlfrescoSearchSQLClient:
        """Create Search SQL API client"""
        return AlfrescoSearchSQLClient(self.base_url, self.auth, self.verify_ssl, self.timeout)

    def create_all_clients(self) -> Dict[str, Any]:
        """Create all available clients"""
        return {
            "auth": self.create_auth_client(),
            "core": self.create_core_client(),
            "discovery": self.create_discovery_client(),
            "search": self.create_search_client(),
            "workflow": self.create_workflow_client(),
            "model": self.create_model_client(),
            "search_sql": self.create_search_sql_client()
        }
