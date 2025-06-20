"""
Enhanced Alfresco-Auth API Client

Provides convenience methods and enhanced functionality for the generated API client.
"""

import sys
from pathlib import Path
from typing import Dict, Any, Optional

# Add generated client to path
client_dir = Path(__file__).parent.parent / "clients" / "alfresco-auth"
if str(client_dir) not in sys.path:
    sys.path.insert(0, str(client_dir))

# Add Pydantic models to path  
models_dir = Path(__file__).parent.parent / "models"
if str(models_dir) not in sys.path:
    sys.path.insert(0, str(models_dir))

try:
    from alfresco_auth_client.api_client import ApiClient
    from alfresco_auth_client.configuration import Configuration
    from alfresco_auth_client.api.authentication_api import AuthenticationApi
    print("✅ Successfully imported Alfresco Auth API client")
except ImportError as e:
    print(f"❌ Failed to import Alfresco Auth API client: {e}")
    ApiClient = None
    Configuration = None
    AuthenticationApi = None

try:
    from alfresco_auth_models import *
    print("✅ Successfully imported Alfresco Auth Pydantic models")
except ImportError as e:
    print(f"❌ Failed to import Alfresco Auth Pydantic models: {e}")

class AuthClient:
    """Alfresco Authentication API client that provides access to all Alfresco Auth API endpoints."""
    
    def __init__(self, base_url: str, username: str, password: str, verify_ssl: bool = True):
        if not ApiClient or not Configuration or not AuthenticationApi:
            raise ImportError("Alfresco Auth API client not available")
            
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

def create_client(host: str = "http://localhost:8080", username: str = "admin", password: str = "admin") -> AuthClient:
    """Convenience function to create an auth client"""
    return AuthClient(host, username, password)

if __name__ == "__main__":
    # Test the enhanced client
    try:
        client = create_client()
        print("✅ Enhanced Alfresco Auth client is working!")
    except Exception as e:
        print(f"❌ Enhanced Alfresco Auth client test failed: {e}")
