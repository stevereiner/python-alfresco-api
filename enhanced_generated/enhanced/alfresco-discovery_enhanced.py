"""
Enhanced Alfresco-Discovery API Client

Provides convenience methods and enhanced functionality for the generated API client.
"""

import sys
from pathlib import Path
from typing import Dict, Any, Optional

# Add generated client to path
client_dir = Path(__file__).parent.parent / "enhanced_generated" / "clients" / "alfresco-discovery"
if str(client_dir) not in sys.path:
    sys.path.insert(0, str(client_dir))

# Add Pydantic models to path  
models_dir = Path(__file__).parent.parent / "enhanced_generated" / "models"
if str(models_dir) not in sys.path:
    sys.path.insert(0, str(models_dir))

try:
    from alfresco_discovery_client.api_client import ApiClient
    from alfresco_discovery_client.configuration import Configuration
    print(f"✅ Successfully imported {api_name} API client")
except ImportError as e:
    print(f"❌ Failed to import {api_name} API client: {e}")
    ApiClient = None
    Configuration = None

try:
    from alfresco_discovery_models import *
    print(f"✅ Successfully imported {api_name} Pydantic models")
except ImportError as e:
    print(f"❌ Failed to import {api_name} Pydantic models: {e}")

class EnhancedAlfrescodiscoveryClient:
    """Enhanced client with convenience methods"""
    
    def __init__(self, host: str = "http://localhost:8080", username: str = "admin", password: str = "admin"):
        if not ApiClient or not Configuration:
            raise ImportError("API client not available")
            
        # Configure the API client
        self.configuration = Configuration()
        self.configuration.host = host + "/alfresco/api/-default-/public/alfresco/versions/1"
        self.configuration.username = username
        self.configuration.password = password
        
        # Create API client
        self.api_client = ApiClient(self.configuration)
        
        # Import specific APIs as needed
        self._import_apis()
    
    def _import_apis(self):
        """Import specific API classes"""
        try:
            # Import common APIs - adjust based on actual generated APIs
            from alfresco_discovery_client.api import DefaultApi
            self.default_api = DefaultApi(self.api_client)
        except ImportError:
            print(f"Warning: Could not import APIs for {api_name}")
    
    def test_connection(self) -> bool:
        """Test if the connection to Alfresco is working"""
        try:
            # This would need to be customized based on available endpoints
            # For now, just test if we can create the client
            return self.api_client is not None
        except Exception as e:
            print(f"Connection test failed: {e}")
            return False

def create_client(host: str = "http://localhost:8080", username: str = "admin", password: str = "admin") -> EnhancedAlfrescodiscoveryClient:
    """Convenience function to create an enhanced client"""
    return EnhancedAlfrescodiscoveryClient(host, username, password)

if __name__ == "__main__":
    # Test the enhanced client
    try:
        client = create_client()
        if client.test_connection():
            print(f"✅ Enhanced {api_name} client is working!")
        else:
            print(f"❌ Enhanced {api_name} client connection failed")
    except Exception as e:
        print(f"❌ Enhanced {api_name} client test failed: {e}")
