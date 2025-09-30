"""
Client Factory for Alfresco APIs

Provides easy instantiation of individual clients with shared configuration.
Perfect for enterprise applications and microservices.
"""

import os
from typing import Optional, Dict, Any, Union
from .auth_util import AuthUtil, SimpleAuthUtil
from .clients.auth import AlfrescoAuthClient
from .clients.core import AlfrescoCoreClient
from .clients.discovery import AlfrescoDiscoveryClient
from .clients.search import AlfrescoSearchClient
from .clients.workflow import AlfrescoWorkflowClient
from .clients.model import AlfrescoModelClient
from .clients.search_sql import AlfrescoSearchSqlClient

# Try to import python-dotenv for .env file support (optional)
try:
    from dotenv import load_dotenv
    DOTENV_AVAILABLE = True
except ImportError:
    DOTENV_AVAILABLE = False

class MasterClient:
    """
    Master client with dot syntax access to all APIs.
    Provides unified interface: master_client.core.something()
    """
    
    def __init__(self, clients_dict: Dict[str, Any]):
        """Initialize master client with all API clients."""
        self.auth = clients_dict['auth']
        self.core = clients_dict['core'] 
        self.discovery = clients_dict['discovery']
        self.search = clients_dict['search']
        self.workflow = clients_dict['workflow']
        self.model = clients_dict['model']
        self.search_sql = clients_dict['search_sql']

class ClientFactory:
    """
    Factory for creating Alfresco API clients with centralized authentication.
    
    Handles ALL authentication complexity - clients are simple and focused.
    Supports multiple authentication strategies: Basic, OAuth2, Custom.
    """
    
    def __init__(
        self,
        base_url: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        auth_util = None,  # Pass existing auth_util (any type)
        verify_ssl: Optional[Union[bool, str]] = None,
        timeout: Optional[int] = None,
        load_env: bool = True,
        env_file: Optional[str] = None
    ):
        """
        Initialize the client factory with centralized authentication management.
        
        This is the ONLY place in the entire package that handles authentication complexity.
        All clients receive a simple, ready-to-use auth_util.
        
        Args:
            base_url: Base URL of Alfresco instance (overrides env)
            username: Username for authentication (overrides env)
            password: Password for authentication (overrides env)
            auth_util: Pre-configured auth util (SimpleAuthUtil, AuthUtil, OAuth2AuthUtil, etc.)
                      If provided, its parameters (timeout, base_url, verify_ssl) take priority
            verify_ssl: SSL verification - True, False, or path to certificate bundle (overrides env)
            timeout: Request timeout in seconds (overrides env, but auth_util.timeout takes precedence)
            load_env: Whether to automatically load from environment/env file
            env_file: Specific .env file path (default: .env in current directory)
        """
        # Centralized environment loading (ONLY place in entire package)
        from .auth_util import load_env_config
        config = load_env_config(
            base_url=base_url,
            username=username, 
            password=password,
            verify_ssl=verify_ssl,
            timeout=timeout,
            load_env=load_env,
            env_file=env_file
        )
        
        # Store resolved configuration
        self._base_url = config['base_url']
        self.verify_ssl = config['verify_ssl']
        self.timeout = config['timeout']  # May be None if not specified
        
        # Handle authentication centrally - support all patterns
        if auth_util is not None:
            # Use provided auth_util (any type: SimpleAuthUtil, AuthUtil, OAuth2AuthUtil)
            # Respect auth_util's existing configuration if it has parameters
            self.auth = auth_util
            
            # If auth_util has its own timeout, use it; otherwise use our resolved timeout
            if hasattr(auth_util, 'timeout') and auth_util.timeout is not None:
                self.timeout = auth_util.timeout
            
            # If auth_util has its own base_url, use it; otherwise keep our resolved base_url
            if hasattr(auth_util, 'base_url') and auth_util.base_url:
                self._base_url = auth_util.base_url
                
            # If auth_util has its own verify_ssl, use it; otherwise keep our resolved verify_ssl
            if hasattr(auth_util, 'verify_ssl') and auth_util.verify_ssl is not None:
                self.verify_ssl = auth_util.verify_ssl
                
            # Store auth_util credentials for access (don't override the auth_util itself)
            self._auth_username = getattr(auth_util, 'username', None)
            self._auth_password = getattr(auth_util, 'password', None)
        elif config['username'] and config['password']:
            # Create full AuthUtil with query parameter support (including from env)
            # Only pass timeout if it's specified (not None)
            auth_kwargs = {
                'base_url': config['base_url'],
                'username': config['username'], 
                'password': config['password'],
                'verify_ssl': config['verify_ssl']
            }
            if config['timeout'] is not None:
                auth_kwargs['timeout'] = config['timeout']
            
            self.auth = AuthUtil(**auth_kwargs)
            # Store credentials for access
            self._auth_username = config['username']
            self._auth_password = config['password']
        else:
            # No authentication available
            raise ValueError(
                f"Authentication required: provide 'auth_util' or both 'username' and 'password'\n"
                f"Current config: username={config['username']}, password={'***' if config['password'] else None}\n"
                f"Try setting ALFRESCO_USERNAME and ALFRESCO_PASSWORD environment variables\n"
                f"Or pass auth_util=SimpleAuthUtil('user', 'pass') to ClientFactory"
            )
    
    @property
    def base_url(self) -> str:
        """Get the server base URL."""
        return self._base_url
    
    @property
    def username(self) -> Optional[str]:
        """Get the authentication username."""
        return getattr(self, '_auth_username', None)
    
    @property
    def password(self) -> Optional[str]:
        """Get the authentication password."""
        return getattr(self, '_auth_password', None)
    
    @classmethod
    def from_env(cls, env_file: Optional[str] = None) -> 'ClientFactory':
        """
        Create ClientFactory entirely from environment variables/.env file.
        
        Args:
            env_file: Optional path to .env file
            
        Returns:
            ClientFactory instance configured from environment
        """
        return cls(load_env=True, env_file=env_file)
    
    def get_config_info(self) -> Dict[str, Any]:
        """Get current configuration information for debugging."""
        # Get auth info safely
        auth_type = type(self.auth).__name__
        if hasattr(self.auth, 'username'):
            auth_info = f"{auth_type} (user: {self.auth.username})"
        elif hasattr(self.auth, 'client_id'):
            # This is for OAuth2AuthUtil
            auth_info = f"{auth_type} (client: {getattr(self.auth, 'client_id', 'unknown')})"
        else:
            auth_info = auth_type
            
        return {
            "base_url": self._base_url,
            "auth_type": auth_info,
            "verify_ssl": self.verify_ssl,
            "timeout": self.timeout,
            "has_auth": self.auth is not None,
            "dotenv_available": DOTENV_AVAILABLE
        }
    
    def create_auth_client(self) -> AlfrescoAuthClient:
        """Create Authentication API client with shared authentication"""
        return AlfrescoAuthClient(self)
    
    def create_core_client(self) -> AlfrescoCoreClient:
        """Create Core API client with shared authentication"""
        return AlfrescoCoreClient(self)
    
    def create_discovery_client(self) -> AlfrescoDiscoveryClient:
        """Create Discovery API client with shared authentication"""
        return AlfrescoDiscoveryClient(self)
    
    def create_discovery_client_v11(self):
        """Create Discovery Client v1.1 with clean, high-level methods - now uses hierarchical structure"""
        # V1.1 is now the hierarchical structure, so just return the regular discovery client
        return self.create_discovery_client()
    
    def create_search_client(self) -> AlfrescoSearchClient:
        """Create Search API client with shared authentication"""
        return AlfrescoSearchClient(self)
    
    def create_workflow_client(self) -> AlfrescoWorkflowClient:
        """Create Workflow API client with shared authentication"""
        return AlfrescoWorkflowClient(self)
    
    def create_model_client(self) -> AlfrescoModelClient:
        """Create Model API client with shared authentication"""
        return AlfrescoModelClient(self)
    
    def create_search_sql_client(self) -> AlfrescoSearchSqlClient:
        """Create Search SQL API client with shared authentication"""
        return AlfrescoSearchSqlClient(self)
    
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
    
    def create_master_client(self) -> MasterClient:
        """Create master client with dot syntax access"""
        clients = self.create_all_clients()
        return MasterClient(clients)

    def create_lazy_master_client(self):
        """
        Create master client with lazy-loaded API access.
        
        Provides unified dot-syntax access to all Alfresco APIs while maintaining
        high performance through lazy loading - sub-clients are only created
        when first accessed.
        
        Returns:
            AlfrescoMasterClient: Master client with lazy-loaded API access
            
        Examples:
            ```python
            # Create master client
            factory = ClientFactory(base_url="http://localhost:8080")
            client = factory.create_lazy_master_client()
            
            # Access Core API (lazy loaded)
            node = client.core.nodes.get("abc123-def456")
            
            # Access other APIs (lazy loaded)
            results = client.search.search.search("annual report")
            info = client.discovery.discovery.get_info()
            ```
        """
        from .clients import AlfrescoMasterClient
        return AlfrescoMasterClient(self)
