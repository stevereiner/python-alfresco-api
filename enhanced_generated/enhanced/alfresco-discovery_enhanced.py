"""
Enhanced Alfresco-Discovery API Client

Provides convenience methods and enhanced functionality for the generated API client.
"""

import sys
from pathlib import Path
from typing import Dict, Any, Optional

# Add generated client to path
client_dir = Path(__file__).parent.parent / "clients" / "alfresco-discovery"
if str(client_dir) not in sys.path:
    sys.path.insert(0, str(client_dir))

# Add Pydantic models to path  
models_dir = Path(__file__).parent.parent / "models"
if str(models_dir) not in sys.path:
    sys.path.insert(0, str(models_dir))

try:
    from alfresco_discovery_client.api_client import ApiClient
    from alfresco_discovery_client.configuration import Configuration
    from alfresco_discovery_client.api.discovery_api import DiscoveryApi
    print("✅ Successfully imported Alfresco Discovery API client")
except ImportError as e:
    print(f"❌ Failed to import Alfresco Discovery API client: {e}")
    ApiClient = None
    Configuration = None
    DiscoveryApi = None

try:
    from alfresco_discovery_models import *
    print("✅ Successfully imported Alfresco Discovery Pydantic models")
except ImportError as e:
    print(f"❌ Failed to import Alfresco Discovery Pydantic models: {e}")

class DiscoveryClient:
    """Alfresco Discovery API client that provides access to all Alfresco Discovery API endpoints."""
    
    def __init__(self, base_url: str, username: str, password: str, verify_ssl: bool = True):
        if not ApiClient or not Configuration or not DiscoveryApi:
            raise ImportError("Alfresco Discovery API client not available")
            
        self.base_url = base_url
        self.username = username
        self.password = password
        self.verify_ssl = verify_ssl
        
        # Create configuration
        config = Configuration()
        config.host = f"{base_url}/alfresco/api/-default-/public/alfresco/versions/1"
        config.username = username
        config.password = password
        config.verify_ssl = verify_ssl
        
        # Create API client
        self.api_client = ApiClient(configuration=config)
        
        # Initialize API endpoints
        self.discovery = DiscoveryApi(self.api_client)
    
    def get_api_info(self) -> dict:
        """Get information about the Alfresco Discovery API."""
        return {
            'name': 'Alfresco Discovery API',
            'version': '1.0',
            'description': 'Alfresco Discovery API endpoints',
            'endpoints': ['discovery']
        }

def create_client(host: str = "http://localhost:8080", username: str = "admin", password: str = "admin") -> DiscoveryClient:
    """Convenience function to create a discovery client"""
    return DiscoveryClient(host, username, password)

if __name__ == "__main__":
    # Test the enhanced client
    try:
        client = create_client()
        print("✅ Enhanced Alfresco Discovery client is working!")
    except Exception as e:
        print(f"❌ Enhanced Alfresco Discovery client test failed: {e}")
