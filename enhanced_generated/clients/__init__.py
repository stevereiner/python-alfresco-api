from typing import Optional
from .base import AlfrescoBaseClient
from .alfresco_core.alfresco_core.api import CoreClient
from .alfresco_search.alfresco_search.api import SearchClient
from .alfresco_workflow.alfresco_workflow.api import WorkflowClient
from .alfresco_auth.alfresco_auth.api import AuthClient
from .alfresco_discovery.alfresco_discovery.api import DiscoveryClient
from .alfresco_model.alfresco_model.api import ModelClient
# Import using alternative method due to hyphen in package name
import importlib
SearchSQLClient = getattr(importlib.import_module('alfresco_client.alfresco_search-sql.alfresco_search-sql.api'), 'SearchSQLClient')

class AlfrescoClient:
    def __init__(
        self,
        base_url: str,
        username: str,
        password: str,
        verify_ssl: bool = True
    ):
        """
        Initialize the master Alfresco client that manages all API clients.
        
        Args:
            base_url (str): The base URL of the Alfresco instance
            username (str): Alfresco username
            password (str): Alfresco password
            verify_ssl (bool): Whether to verify SSL certificates
        """
        self.base_url = base_url
        self.username = username
        self.password = password
        self.verify_ssl = verify_ssl
        
        # Initialize all API clients
        self.alfresco_core = CoreClient(base_url, username, password, verify_ssl)
        self.alfresco_search = SearchClient(base_url, username, password, verify_ssl)
        self.alfresco_workflow = WorkflowClient(base_url, username, password, verify_ssl)
        self.alfresco_auth = AuthClient(base_url, username, password, verify_ssl)
        self.alfresco_discovery = DiscoveryClient(base_url, username, password, verify_ssl)
        self.alfresco_model = ModelClient(base_url, username, password, verify_ssl)
        self.alfresco_search_sql = SearchSQLClient(base_url, username, password, verify_ssl)

    def get_api_info(self) -> dict:
        """
        Get information about all available APIs.
        
        Returns:
            dict: Dictionary containing information about all APIs
        """
        return {
            'alfresco_core': self.alfresco_core.get_api_info(),
            'alfresco_search': self.alfresco_search.get_api_info(),
            'alfresco_workflow': self.alfresco_workflow.get_api_info(),
            'alfresco_auth': self.alfresco_auth.get_api_info(),
            'alfresco_discovery': self.alfresco_discovery.get_api_info(),
            'alfresco_model': self.alfresco_model.get_api_info(),
            'alfresco_search_sql': self.alfresco_search_sql.get_api_info()
        } 