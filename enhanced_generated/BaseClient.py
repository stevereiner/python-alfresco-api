"""
Alfresco Base Client

Base client functionality for the enhanced generated Alfresco API package.
"""

import sys
from pathlib import Path
from typing import Dict, Any, Optional

class AlfrescoBaseClient:
    """
    Base client for Alfresco API operations.
    
    Provides common functionality for all Alfresco API clients including
    configuration, path management, and utility methods.
    """
    
    def __init__(
        self, 
        host: str = "http://localhost:8080", 
        username: str = "admin", 
        password: str = "admin",
        verify_ssl: bool = True
    ):
        """
        Initialize the base client.
        
        Args:
            host (str): The base URL of the Alfresco instance
            username (str): Alfresco username  
            password (str): Alfresco password
            verify_ssl (bool): Whether to verify SSL certificates
        """
        self.host = host.rstrip('/')
        self.username = username
        self.password = password
        self.verify_ssl = verify_ssl
        
        # Setup paths for generated clients and models
        self._setup_paths()
    
    def _setup_paths(self):
        """Setup Python paths for generated clients and models."""
        base_dir = Path(__file__).parent
        
        # Add individual client directories to Python path
        clients_base = base_dir / "clients"
        # Map client directories to their actual names (True Option A structure)
        client_dirs = [
            'alfresco-auth',      # New OpenAPI generation (alfresco_auth_client)
            'alfresco-core',      # New OpenAPI generation (alfresco_core_client)
            'alfresco-discovery', # New OpenAPI generation (alfresco_discovery_client) 
            'alfresco-search',    # New OpenAPI generation (alfresco_search_client)
            'alfresco-search-sql', # New OpenAPI generation (alfresco_search_sql_client)
            'alfresco-workflow',  # New OpenAPI generation (alfresco_workflow_api - unique name)
            'alfresco-model'      # New OpenAPI generation (openapi_client structure)
        ]
        
        for client_dir in client_dirs:
            client_path = clients_base / client_dir
            if client_path.exists() and str(client_path) not in sys.path:
                sys.path.insert(0, str(client_path))
            
        # Add models directory to Python path
        models_dir = base_dir / "models"
        if str(models_dir) not in sys.path:
            sys.path.insert(0, str(models_dir))
    
    def get_api_url(self, api_name: str) -> str:
        """
        Get the correct API URL for a specific API.
        
        Args:
            api_name (str): Name of the API (auth, core, discovery, etc.)
            
        Returns:
            str: Full API URL
        """
        # For single-tenant (Community Edition) Alfresco, try URLs without -default- network
        base_urls = {
            'auth': f"{self.host}/alfresco/api/-default-/public/authentication/versions/1",
            'auth_simple': f"{self.host}/alfresco/service/api/login",  # Alternative auth endpoint
            'core': f"{self.host}/alfresco/api/-default-/public/alfresco/versions/1", 
            'discovery': f"{self.host}/alfresco/api",  # Discovery uses different URL
            'search': f"{self.host}/alfresco/api/-default-/public/search/versions/1",
            'search_sql': f"{self.host}/alfresco/api/-default-/public/search/versions/1",  # Search SQL same as search
            'search-sql': f"{self.host}/alfresco/api/-default-/public/search/versions/1",  # Handle both formats
            'workflow': f"{self.host}/alfresco/api/-default-/public/workflow/versions/1",
            'model': f"{self.host}/alfresco/api/-default-/public/model/versions/1"
        }
        
        return base_urls.get(api_name, f"{self.host}/alfresco/api")
    
    def get_api_url_simple(self, api_name: str) -> str:
        """
        Get alternative API URLs for single-tenant Alfresco without -default- network.
        
        Args:
            api_name (str): Name of the API
            
        Returns:
            str: Alternative API URL without network identifier
        """
        simple_urls = {
            'auth': f"{self.host}/alfresco/service/api/login",
            'core': f"{self.host}/alfresco/api/public/alfresco/versions/1",
            'discovery': f"{self.host}/alfresco/api",
            'search': f"{self.host}/alfresco/api/public/search/versions/1",
            'search_sql': f"{self.host}/alfresco/api/public/search/versions/1",
            'search-sql': f"{self.host}/alfresco/api/public/search/versions/1",
            'workflow': f"{self.host}/alfresco/api/public/workflow/versions/1",
            'model': f"{self.host}/alfresco/api/public/model/versions/1"
        }
        
        return simple_urls.get(api_name, f"{self.host}/alfresco/api")
    
    def create_configuration(self, api_name: str):
        """
        Create configuration for a specific API.
        
        Args:
            api_name (str): Name of the API
            
        Returns:
            Configuration: Configured API configuration
        """
        try:
            # Handle consistent alfresco_*_client structure for True Option A (OpenAPI Generator 7.13.0)
            client_package = api_name.replace('-', '_') + '_client'
            config_module = __import__(f"{client_package}.configuration", fromlist=['Configuration'])
            Configuration = config_module.Configuration
            
            # Create configuration with parameters (modern style)
            config = Configuration(
                host=self.get_api_url(api_name),
                username=self.username,
                password=self.password
            )
            
            return config
            
        except ImportError as e:
            print(f"❌ Could not import configuration for {api_name}: {e}")
            return None
    
    def create_api_client(self, api_name: str):
        """
        Create an API client for a specific API.
        
        Args:
            api_name (str): Name of the API
            
        Returns:
            ApiClient: Configured API client
        """
        try:
            # Handle consistent alfresco_*_client structure for True Option A (OpenAPI Generator 7.13.0)
            client_package = api_name.replace('-', '_') + '_client'
            client_module = __import__(f"{client_package}.api_client", fromlist=['ApiClient'])
            
            ApiClient = client_module.ApiClient
            
            # Create configuration
            config = self.create_configuration(api_name)
            if not config:
                return None
                
            # Create client
            client = ApiClient(configuration=config)
            
            # Special handling for discovery API - set Authorization header manually like working example
            if api_name == 'discovery':
                import base64
                auth_string = f"{self.username}:{self.password}"
                auth_bytes = auth_string.encode('ascii')
                auth_b64 = base64.b64encode(auth_bytes).decode('ascii')
                client.set_default_header('Authorization', f'Basic {auth_b64}')
                print(f"🔧 Set Authorization header for discovery API")
            
            return client
            
        except ImportError as e:
            print(f"❌ Could not import API client for {api_name}: {e}")
            return None
    
    def share_authentication(self, source_client, target_client):
        """
        Share authentication from one API client to another.
        
        Args:
            source_client: The client that has authentication
            target_client: The client that needs authentication
        """
        if hasattr(source_client, 'configuration') and hasattr(target_client, 'configuration'):
            # Copy authentication settings
            target_client.configuration.username = source_client.configuration.username
            target_client.configuration.password = source_client.configuration.password
            
            # Copy any auth tokens or headers
            if hasattr(source_client, 'api_client') and hasattr(target_client, 'api_client'):
                if hasattr(source_client.api_client, 'default_headers'):
                    target_client.api_client.default_headers.update(
                        source_client.api_client.default_headers
                    )
    
    def get_client_info(self) -> Dict[str, Any]:
        """
        Get information about this client instance.
        
        Returns:
            dict: Client configuration information
        """
        return {
            'host': self.host,
            'username': self.username,
            'verify_ssl': self.verify_ssl,
            'client_type': 'Enhanced Generated (OpenAPI)',
            'python_version': sys.version,
            'available_apis': [
                'auth', 'core', 'discovery', 'search', 
                'workflow', 'model', 'search-sql'
            ]
        } 
