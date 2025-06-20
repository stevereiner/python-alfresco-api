"""
Enhanced Alfresco-Search API Client

Provides convenience methods and enhanced functionality for the generated API client.
"""

import sys
from pathlib import Path
from typing import Dict, Any, Optional

# Add generated client to path
client_dir = Path(__file__).parent.parent / "clients" / "alfresco-search"
if str(client_dir) not in sys.path:
    sys.path.insert(0, str(client_dir))

# Add Pydantic models to path  
models_dir = Path(__file__).parent.parent / "models"
if str(models_dir) not in sys.path:
    sys.path.insert(0, str(models_dir))

try:
    from alfresco_search_client.api_client import ApiClient
    from alfresco_search_client.configuration import Configuration
    from alfresco_search_client.api.search_api import SearchApi
    print("✅ Successfully imported Alfresco Search API client")
except ImportError as e:
    print(f"❌ Failed to import Alfresco Search API client: {e}")
    ApiClient = None
    Configuration = None
    SearchApi = None

try:
    from alfresco_search_models import *
    print("✅ Successfully imported Alfresco Search Pydantic models")
except ImportError as e:
    print(f"❌ Failed to import Alfresco Search Pydantic models: {e}")

class SearchClient:
    """Alfresco Search API client that provides access to all Alfresco Search API endpoints."""
    
    def __init__(self, base_url: str, username: str, password: str, verify_ssl: bool = True):
        if not ApiClient or not Configuration or not SearchApi:
            raise ImportError("Alfresco Search API client not available")
            
        self.base_url = base_url
        self.username = username
        self.password = password
        self.verify_ssl = verify_ssl
        
        # Create configuration
        config = Configuration()
        config.host = f"{base_url}/alfresco/api/-default-/public/search/versions/1"
        config.username = username
        config.password = password
        config.verify_ssl = verify_ssl
        
        # Create API client
        self.api_client = ApiClient(configuration=config)
        
        # Initialize API endpoints
        self.search = SearchApi(self.api_client)
    
    def get_api_info(self) -> dict:
        """Get information about the Alfresco Search API."""
        return {
            'name': 'Alfresco Search API',
            'version': '1.0',
            'description': 'Alfresco Search API endpoints',
            'endpoints': ['search']
        }

def create_client(host: str = "http://localhost:8080", username: str = "admin", password: str = "admin") -> SearchClient:
    """Convenience function to create a search client"""
    return SearchClient(host, username, password)

if __name__ == "__main__":
    # Test the enhanced client
    try:
        client = create_client()
        print("✅ Enhanced Alfresco Search client is working!")
    except Exception as e:
        print(f"❌ Enhanced Alfresco Search client test failed: {e}")
