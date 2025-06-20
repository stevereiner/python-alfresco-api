from __future__ import absolute_import

# flake8: noqa

# import apis into api package
from .actions_api import ActionsApi
from .activities_api import ActivitiesApi
from .audit_api import AuditApi
from .comments_api import CommentsApi
from .downloads_api import DownloadsApi
from .favorites_api import FavoritesApi
from .groups_api import GroupsApi
from .networks_api import NetworksApi
from .nodes_api import NodesApi
from .people_api import PeopleApi
from .preferences_api import PreferencesApi
from .probes_api import ProbesApi
from .queries_api import QueriesApi
from .ratings_api import RatingsApi
from .renditions_api import RenditionsApi
from .shared_links_api import SharedLinksApi
from .sites_api import SitesApi
from .tags_api import TagsApi
from .trashcan_api import TrashcanApi
from .versions_api import VersionsApi

# Import base classes
from ..api_client import ApiClient
from ..configuration import Configuration

class CoreClient:
    """Core API client that provides access to all Alfresco Core API endpoints."""
    
    def __init__(self, base_url: str, username: str, password: str, verify_ssl: bool = True):
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
        
        # Initialize all API endpoints
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
    
    # ENHANCED METHODS ADDED BY enhance_generated_api.py
    # These methods provide convenient interfaces for common operations
    
    def create_folder(self, parent_node_id: str, name: str, title: str = None, description: str = None):
        """
        Create a folder with a simple, stable interface.
        
        Args:
            parent_node_id: ID of the parent node (e.g., '-root-')
            name: Folder name
            title: Optional folder title
            description: Optional folder description
            
        Returns:
            Created folder node information
            
        Example:
            folder = client.create_folder('-root-', 'My Folder', 
                                        title='Important Folder')
        """
        return self.nodes.create_folder_simple(parent_node_id, name, title, description)
    
    def create_document(self, parent_node_id: str, name: str, title: str = None, description: str = None):
        """
        Create an empty document with a simple, stable interface.
        
        Args:
            parent_node_id: ID of the parent node
            name: Document name  
            title: Optional document title
            description: Optional document description
            
        Returns:
            Created document node information
            
        Example:
            doc = client.create_document(folder_id, 'document.txt',
                                       title='My Document')
        """
        return self.nodes.create_document_simple(parent_node_id, name, title, description)
    
    def upload_text_file(self, parent_node_id: str, filename: str, content: str, 
                        title: str = None, description: str = None):
        """
        Upload text content as a file with a simple, stable interface.
        
        Args:
            parent_node_id: ID of the parent node
            filename: Name for the created file
            content: Text content to upload
            title: Optional file title
            description: Optional file description
            
        Returns:
            Created file node information
            
        Example:
            file_node = client.upload_text_file(folder_id, 'test.txt', 
                                               'Hello World!',
                                               title='Test File')
        """
        return self.nodes.upload_file_content(parent_node_id, filename, content, 
                                            'text/plain', title, description)

    def get_api_info(self) -> dict:
        """Get information about the Core API."""
        return {
            'name': 'Alfresco Core API',
            'version': '1.0',
            'description': 'Core Alfresco Content Services API',
            'endpoints': [
                'actions', 'activities', 'audit', 'comments', 'downloads',
                'favorites', 'groups', 'networks', 'nodes', 'people',
                'preferences', 'probes', 'queries', 'ratings', 'renditions',
                'shared_links', 'sites', 'tags', 'trashcan', 'versions'
            ]
        }
