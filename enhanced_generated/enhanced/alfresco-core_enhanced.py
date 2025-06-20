"""
Enhanced Alfresco-Core API Client

Provides convenience methods and enhanced functionality for the generated API client.
"""

import sys
from pathlib import Path
from typing import Dict, Any, Optional

# Add generated client to path
client_dir = Path(__file__).parent.parent / "clients" / "alfresco-core"
if str(client_dir) not in sys.path:
    sys.path.insert(0, str(client_dir))

# Add Pydantic models to path  
models_dir = Path(__file__).parent.parent / "models"
if str(models_dir) not in sys.path:
    sys.path.insert(0, str(models_dir))

try:
    from alfresco_core_client.api_client import ApiClient
    from alfresco_core_client.configuration import Configuration
    from alfresco_core_client.api.actions_api import ActionsApi
    from alfresco_core_client.api.activities_api import ActivitiesApi
    from alfresco_core_client.api.audit_api import AuditApi
    from alfresco_core_client.api.comments_api import CommentsApi
    from alfresco_core_client.api.downloads_api import DownloadsApi
    from alfresco_core_client.api.favorites_api import FavoritesApi
    from alfresco_core_client.api.groups_api import GroupsApi
    from alfresco_core_client.api.networks_api import NetworksApi
    from alfresco_core_client.api.nodes_api import NodesApi
    from alfresco_core_client.api.people_api import PeopleApi
    from alfresco_core_client.api.preferences_api import PreferencesApi
    from alfresco_core_client.api.probes_api import ProbesApi
    from alfresco_core_client.api.queries_api import QueriesApi
    from alfresco_core_client.api.ratings_api import RatingsApi
    from alfresco_core_client.api.renditions_api import RenditionsApi
    from alfresco_core_client.api.shared_links_api import SharedLinksApi
    from alfresco_core_client.api.sites_api import SitesApi
    from alfresco_core_client.api.tags_api import TagsApi
    from alfresco_core_client.api.trashcan_api import TrashcanApi
    from alfresco_core_client.api.versions_api import VersionsApi
    print("✅ Successfully imported Alfresco Core API client")
except ImportError as e:
    print(f"❌ Failed to import Alfresco Core API client: {e}")
    ApiClient = None
    Configuration = None

try:
    from alfresco_core_models import *
    print("✅ Successfully imported Alfresco Core Pydantic models")
except ImportError as e:
    print(f"❌ Failed to import Alfresco Core Pydantic models: {e}")

class CoreClient:
    """Alfresco Core API client that provides access to all Alfresco Core API endpoints."""
    
    def __init__(self, base_url: str, username: str, password: str, verify_ssl: bool = True):
        if not ApiClient or not Configuration:
            raise ImportError("Alfresco Core API client not available")
            
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
        self.actions = ActionsApi(self.api_client)
        self.activities = ActivitiesApi(self.api_client)
        self.audit = AuditApi(self.api_client)
        self.comments = CommentsApi(self.api_client)
        self.downloads = DownloadsApi(self.api_client)
        self.favorites = FavoritesApi(self.api_client)
        self.groups = GroupsApi(self.api_client)
        self.networks = NetworksApi(self.api_client)
        self.nodes = NodesApi(self.api_client)
        self.people = PeopleApi(self.api_client)
        self.preferences = PreferencesApi(self.api_client)
        self.probes = ProbesApi(self.api_client)
        self.queries = QueriesApi(self.api_client)
        self.ratings = RatingsApi(self.api_client)
        self.renditions = RenditionsApi(self.api_client)
        self.shared_links = SharedLinksApi(self.api_client)
        self.sites = SitesApi(self.api_client)
        self.tags = TagsApi(self.api_client)
        self.trashcan = TrashcanApi(self.api_client)
        self.versions = VersionsApi(self.api_client)
    
    def get_api_info(self) -> dict:
        """Get information about the Alfresco Core API."""
        return {
            'name': 'Alfresco Core API',
            'version': '1.0',
            'description': 'Alfresco Core API endpoints',
            'endpoints': [
                'actions', 'activities', 'audit', 'comments', 'downloads', 
                'favorites', 'groups', 'networks', 'nodes', 'people', 
                'preferences', 'probes', 'queries', 'ratings', 'renditions', 
                'shared_links', 'sites', 'tags', 'trashcan', 'versions'
            ]
        }

def create_client(host: str = "http://localhost:8080", username: str = "admin", password: str = "admin") -> CoreClient:
    """Convenience function to create a core client"""
    return CoreClient(host, username, password)

if __name__ == "__main__":
    # Test the enhanced client
    try:
        client = create_client()
        print("✅ Enhanced Alfresco Core client is working!")
    except Exception as e:
        print(f"❌ Enhanced Alfresco Core client test failed: {e}")
