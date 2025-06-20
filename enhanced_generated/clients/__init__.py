from typing import Optional
from .base import AlfrescoBaseClient
import importlib.util
import os

# Import from enhanced modules (which have hyphens in filenames)
def import_enhanced_module(module_name, class_name):
    """Import a module with hyphens in the filename."""
    enhanced_dir = os.path.join(os.path.dirname(__file__), '..', 'enhanced')
    module_path = os.path.join(enhanced_dir, f'{module_name}.py')
    spec = importlib.util.spec_from_file_location(module_name.replace('-', '_'), module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module {module_name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, class_name)

# Import all the enhanced clients
CoreClient = import_enhanced_module('alfresco-core_enhanced', 'CoreClient')
SearchClient = import_enhanced_module('alfresco-search_enhanced', 'SearchClient')
WorkflowClient = import_enhanced_module('alfresco-workflow_enhanced', 'EnhancedAlfrescoworkflowClient')
AuthClient = import_enhanced_module('alfresco-auth_enhanced', 'AuthClient')
DiscoveryClient = import_enhanced_module('alfresco-discovery_enhanced', 'DiscoveryClient')
ModelClient = import_enhanced_module('alfresco-model_enhanced', 'EnhancedAlfrescomodelClient')
SearchSQLClient = import_enhanced_module('alfresco-search-sql_enhanced', 'SearchSQLClient')

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
        
        # Initialize all API clients, handle failures gracefully for unit testing
        self._init_client('alfresco_core', CoreClient, base_url, username, password, verify_ssl)
        self._init_client('alfresco_search', SearchClient, base_url, username, password, verify_ssl)
        self._init_client('alfresco_workflow', WorkflowClient, base_url, username, password, verify_ssl)
        self._init_client('alfresco_auth', AuthClient, base_url, username, password, verify_ssl)
        self._init_client('alfresco_discovery', DiscoveryClient, base_url, username, password, verify_ssl)
        self._init_client('alfresco_model', ModelClient, base_url, username, password, verify_ssl)
        self._init_client('alfresco_search_sql', SearchSQLClient, base_url, username, password, verify_ssl)
    
    def _init_client(self, attr_name: str, client_class, *args):
        """Initialize a client gracefully, setting to None if it fails."""
        try:
            setattr(self, attr_name, client_class(*args))
        except Exception as e:
            print(f"⚠️ Failed to initialize {attr_name}: {e}")
            setattr(self, attr_name, None)
    
    # Property accessors for short names (for compatibility)
    @property
    def auth(self):
        """Get the auth client."""
        return self.alfresco_auth
    
    @property
    def core(self):
        """Get the core client."""
        return self.alfresco_core
    
    @property
    def discovery(self):
        """Get the discovery client."""
        return self.alfresco_discovery
    
    @property
    def search(self):
        """Get the search client."""
        return self.alfresco_search
    
    @property
    def search_sql(self):
        """Get the search SQL client."""
        return self.alfresco_search_sql
    
    @property
    def workflow(self):
        """Get the workflow client."""
        return self.alfresco_workflow
    
    @property
    def model(self):
        """Get the model client."""
        return self.alfresco_model
    
    # Property accessors for full names (for compatibility with integration tests)
    @property
    def auth_client(self):
        """Get the auth client."""
        return self.alfresco_auth
    
    @property
    def core_client(self):
        """Get the core client."""
        return self.alfresco_core
    
    @property
    def discovery_client(self):
        """Get the discovery client."""
        return self.alfresco_discovery
    
    @property
    def search_client(self):
        """Get the search client."""
        return self.alfresco_search
    
    @property
    def search_sql_client(self):
        """Get the search SQL client."""
        return self.alfresco_search_sql
    
    @property
    def workflow_client(self):
        """Get the workflow client."""
        return self.alfresco_workflow
    
    @property
    def model_client(self):
        """Get the model client."""
        return self.alfresco_model

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