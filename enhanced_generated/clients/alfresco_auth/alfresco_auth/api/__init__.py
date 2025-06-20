from __future__ import absolute_import

# flake8: noqa

# import apis into api package
from .authentication_api import AuthenticationApi

# Import base classes
from ..api_client import ApiClient
from ..configuration import Configuration

class AuthClient:
    """Alfresco Authentication API client that provides access to all Alfresco Auth API endpoints."""
    
    def __init__(self, base_url: str, username: str, password: str, verify_ssl: bool = True):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.verify_ssl = verify_ssl
        
        # Create configuration
        config = Configuration()
        config.host = f"{base_url}/alfresco/api/-default-/public/authentication/versions/1"
        config.username = username
        config.password = password
        config.verify_ssl = verify_ssl
        
        # Create API client
        self.api_client = ApiClient(configuration=config)
        
        # Initialize API endpoints
        self.authentication = AuthenticationApi(self.api_client)
    
    def get_api_info(self) -> dict:
        """Get information about the Alfresco Authentication API."""
        return {
            'name': 'Alfresco Authentication API',
            'version': '1.0',
            'description': 'Alfresco Authentication API endpoints',
            'endpoints': ['authentication']
        }
