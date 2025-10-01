"""
Alfresco Core API Client - Main Repository Operations

Provides lazy-loaded access to all Core API operations including nodes,
folders, content, and other repository operations.
"""

from typing import TYPE_CHECKING, Optional, Any
from httpx import Response
import httpx

# Lazy imports to avoid circular dependencies and improve performance
if TYPE_CHECKING:
    from .nodes import NodesClient
    from ...client_factory import ClientFactory


class AlfrescoCoreClient:
    """
    Main client for Alfresco Core API operations.
    
    Provides lazy-loaded access to ALL 22 Core API operation groups:
    - nodes: Node management (files, folders, metadata)
    - folders: Folder-specific operations  
    - content: Content upload/download operations
    - versions: Version control (checkout, checkin, cancel)
    - sites: Site/collaboration management
    - people: User/person management
    - groups: Group management
    - shared_links: Public link sharing
    - comments: Node comments and discussions
    - tags: Content tagging
    - favorites: User favorites
    - activities: User and site activities
    - audit: Audit trail and logs
    - downloads: Download management
    - networks: Network/tenant management
    - preferences: User preferences
    - probes: System health probes
    - queries: Saved queries and search
    - ratings: Content ratings/likes
    - renditions: Thumbnail/preview generation
    - trashcan: Deleted items management
    - actions: Action execution and definitions
    
    Uses lazy loading for maximum performance - operations are
    only imported and initialized when first accessed.
    
    Examples:
        ```python
        # Create Core API client
        from python_alfresco_api import ClientFactory
        
        client_factory = ClientFactory(base_url="http://localhost:8080")
        core_client = client_factory.create_core_client()
        
        # Use node operations (lazy loaded)
        node = core_client.nodes.get("abc123-def456")
        
        # Use site operations (lazy loaded)
        sites = core_client.sites.list()
        
        # Use people operations (lazy loaded)
        people = core_client.people.list()
        
        # Operations are cached after first access
        children = core_client.nodes.get_children("folder-123")
        ```
        
    Note:
        This client uses lazy loading - operation modules are imported
        only when first accessed, providing maximum performance
        for applications that don't use all operations.
    """
    
    def __init__(self, client_factory: 'ClientFactory'):
        """
        Initialize Core API client.
        
        Args:
            client_factory: Factory instance for creating raw clients
        """
        self._client_factory = client_factory
        self._nodes: Optional['NodesClient'] = None
        self._folders: Optional[Any] = None
        
        # Client instances - initialized on first access
        self._raw_client: Optional[Any] = None
        self._httpx_client: Optional[Any] = None
    
    # =================================================================
    # STANDARD CLIENT ACCESS PATTERN - V1.1
    # =================================================================
    
    @property
    def raw_client(self):
        """
        Get the raw authenticated client for advanced operations.
        
        This is the STANDARD way to access the underlying client.
        """
        if self._raw_client is None:
            self._raw_client = self._create_raw_client()
        return self._raw_client
    
    @property
    def httpx_client(self):
        """
        Get direct access to httpx client for raw HTTP operations.
        
        This is the STANDARD way to access the HTTP client.
        Perfect for MCP servers that need raw HTTP access.
        """
        if self._httpx_client is None:
            self._httpx_client = self._create_httpx_client()
        return self._httpx_client
    
    @property
    def is_initialized(self) -> bool:
        """
        Check if the client is initialized and functional.
        
        This is the STANDARD way to check initialization status.
        """
        try:
            # Try to access raw client to test initialization
            _ = self.raw_client
            return True
        except Exception:
            return False
    
    def _create_raw_client(self):
        """
        Create the raw authenticated client.
        
        This is INTERNAL - use raw_client property instead.
        """
        # Import the raw core client directly
        from ...raw_clients.alfresco_core_client.core_client.client import AuthenticatedClient
        
        # Prepare client arguments
        client_kwargs = {
            "base_url": f"{self._client_factory.base_url}/alfresco/api/-default-/public/alfresco/versions/1",
            "token": self._client_factory.auth.get_auth_token(),
            "prefix": self._client_factory.auth.get_auth_prefix(),
            "verify_ssl": self._client_factory.verify_ssl
        }
        
        # Only add timeout if specified (not None)
        if self._client_factory.timeout is not None:
            client_kwargs["timeout"] = self._client_factory.timeout
        
        # Create the raw client with auth setup
        return AuthenticatedClient(**client_kwargs)
    
    def _create_httpx_client(self):
        """
        Create the httpx client for direct HTTP operations.
        
        This is INTERNAL - use httpx_client property instead.
        """
        return self.raw_client.get_httpx_client()

    # =================================================================
    # DEPRECATED METHODS - FOR BACKWARD COMPATIBILITY
    # =================================================================
    
    def _get_raw_client(self):
        """
        DEPRECATED: Use raw_client property instead.
        
        This method is kept for backward compatibility only.
        """
        return self.raw_client
    
    def ensure_httpx_client(self):
        """
        DEPRECATED: Use httpx_client property instead.
        
        This method is kept for backward compatibility only.
        """
        return self.httpx_client
    
    def get_httpx_client(self):
        """
        DEPRECATED: Use httpx_client property instead.
        
        This method is kept for backward compatibility only.
        """
        return self.httpx_client

    # =================================================================
    # SUBSECTION PROPERTIES
    # =================================================================
    
    @property
    def nodes(self) -> 'NodesClient':
        """
        Access node operations (lazy loaded).
        
        Provides comprehensive node management including:
        - Get node information by ID
        - Create files and folders
        - Update node properties and metadata
        - Delete nodes (trash or permanent)
        - Copy and move nodes between locations
        - List folder children with pagination
        
        Returns:
            NodesClient: Node operation interface
        """
        if self._nodes is None:
            # Lazy import and create
            from .nodes import NodesClient
            self._nodes = NodesClient(self)
        return self._nodes
    
    @property
    def versions(self):
        """Access to versions operations (checkout, checkin, cancel checkout)."""
        if not hasattr(self, '_versions_client'):
            from .versions import VersionsClient
            self._versions_client = VersionsClient(self)
            print(f"    [LOADED] versions operations (checkout, checkin, cancel checkout)")
        return self._versions_client
    
    @property  
    def content(self):
        """Access to content operations (upload, download, update content)."""
        if not hasattr(self, '_content_client'):
            from .content import ContentClient
            self._content_client = ContentClient(self)
            print(f"    [LOADED] content operations (upload, download, update)")
        return self._content_client
    
    @property
    def folders(self):
        """
        DEPRECATED: Use nodes.create_folder() instead.
        
        Folder operations are now part of the nodes client.
        """
        return self.nodes

    # NEW: All 18 additional subsections as properties
    
    @property
    def sites(self):
        """Access to sites operations (28 operations)."""
        if not hasattr(self, '_sites_client'):
            print("[LOADING] sites operations...")
            from .sites import SitesClient
            self._sites_client = SitesClient(self)
        return self._sites_client
        
    @property
    def people(self):
        """Access to people operations (8 operations)."""
        if not hasattr(self, '_people_client'):
            print("[LOADING] people operations...")
            from .people import PeopleClient
            self._people_client = PeopleClient(self)
        return self._people_client
        
    @property
    def groups(self):
        """Access to groups operations (9 operations)."""
        if not hasattr(self, '_groups_client'):
            print("[LOADING] groups operations...")
            from .groups import GroupsClient
            self._groups_client = GroupsClient(self)
        return self._groups_client
        
    @property
    def shared_links(self):
        """Access to shared_links operations (7 operations)."""
        if not hasattr(self, '_shared_links_client'):
            print("[LOADING] shared_links operations...")
            from .shared_links import SharedLinksClient
            self._shared_links_client = SharedLinksClient(self)
        return self._shared_links_client
        
    @property
    def comments(self):
        """Access to comments operations (4 operations)."""
        if not hasattr(self, '_comments_client'):
            print("[LOADING] comments operations...")
            from .comments import CommentsClient
            self._comments_client = CommentsClient(self)
        return self._comments_client
        
    @property
    def tags(self):
        """Access to tags operations (6 operations)."""
        if not hasattr(self, '_tags_client'):
            print("[LOADING] tags operations...")
            from .tags import TagsClient
            self._tags_client = TagsClient(self)
        return self._tags_client
        
    @property
    def favorites(self):
        """Access to favorites operations (8 operations)."""
        if not hasattr(self, '_favorites_client'):
            print("[LOADING] favorites operations...")
            from .favorites import FavoritesClient
            self._favorites_client = FavoritesClient(self)
        return self._favorites_client
        
    @property
    def activities(self):
        """Access to activities operations (1 operations)."""
        if not hasattr(self, '_activities_client'):
            print("[LOADING] activities operations...")
            from .activities import ActivitiesClient
            self._activities_client = ActivitiesClient(self)
        return self._activities_client
        
    @property
    def actions(self):
        """Access to actions operations (4 operations)."""
        if not hasattr(self, '_actions_client'):
            print("[LOADING] actions operations...")
            from .actions import ActionsClient
            self._actions_client = ActionsClient(self)
        return self._actions_client
        
    @property
    def audit(self):
        """Access to audit operations (8 operations)."""
        if not hasattr(self, '_audit_client'):
            print("[LOADING] audit operations...")
            from .audit import AuditClient
            self._audit_client = AuditClient(self)
        return self._audit_client
        
    @property
    def downloads(self):
        """Access to downloads operations (3 operations)."""
        if not hasattr(self, '_downloads_client'):
            print("[LOADING] downloads operations...")
            from .downloads import DownloadsClient
            self._downloads_client = DownloadsClient(self)
        return self._downloads_client
        
    @property
    def networks(self):
        """Access to networks operations (3 operations)."""
        if not hasattr(self, '_networks_client'):
            print("[LOADING] networks operations...")
            from .networks import NetworksClient
            self._networks_client = NetworksClient(self)
        return self._networks_client
        
    @property
    def preferences(self):
        """Access to preferences operations (2 operations)."""
        if not hasattr(self, '_preferences_client'):
            print("[LOADING] preferences operations...")
            from .preferences import PreferencesClient
            self._preferences_client = PreferencesClient(self)
        return self._preferences_client
        
    @property
    def probes(self):
        """Access to probes operations (1 operations)."""
        if not hasattr(self, '_probes_client'):
            print("[LOADING] probes operations...")
            from .probes import ProbesClient
            self._probes_client = ProbesClient(self)
        return self._probes_client
        
    @property
    def queries(self):
        """Access to queries operations (3 operations)."""
        if not hasattr(self, '_queries_client'):
            print("[LOADING] queries operations...")
            from .queries import QueriesClient
            self._queries_client = QueriesClient(self)
        return self._queries_client
        
    @property
    def ratings(self):
        """Access to ratings operations (4 operations)."""
        if not hasattr(self, '_ratings_client'):
            print("[LOADING] ratings operations...")
            from .ratings import RatingsClient
            self._ratings_client = RatingsClient(self)
        return self._ratings_client
        
    @property
    def renditions(self):
        """Access to renditions operations (3 operations)."""
        if not hasattr(self, '_renditions_client'):
            print("[LOADING] renditions operations...")
            from .renditions import RenditionsClient
            self._renditions_client = RenditionsClient(self)
        return self._renditions_client
        
    @property
    def trashcan(self):
        """Access to trashcan operations (6 operations)."""
        if not hasattr(self, '_trashcan_client'):
            print("[LOADING] trashcan operations...")
            from .trashcan import TrashcanClient
            self._trashcan_client = TrashcanClient(self)
        return self._trashcan_client
    
    @property
    def base_url(self) -> str:
        """Get the server base URL."""
        return self._client_factory.base_url
    
    @property
    def client_factory(self):
        """Get the client factory."""
        return self._client_factory
    
    @property
    def api(self) -> str:
        """Get the API name."""
        return "core"
    
    @property
    def auth_type(self) -> str:
        """Get the authentication type."""
        return type(self._client_factory.auth).__name__
    
    @property
    def verify_ssl(self) -> bool:
        """Get SSL verification setting."""
        return self._client_factory.verify_ssl
    
    @property
    def timeout(self) -> int:
        """Get request timeout."""
        return self._client_factory.timeout
    
    @property
    def available(self) -> bool:
        """Check if the client is available and functional."""
        return self.is_initialized
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self._client_factory, 'base_url', 'unknown')
        return f"AlfrescoCoreClient(base_url='{base_url}')"

# Export the main client class and all lazy-loaded sub-modules
# This ensures packaging systems include all dynamically accessed modules
__all__ = [
    'AlfrescoCoreClient',
    # Lazy-loaded sub-clients (accessed via properties)
    'actions', 'activities', 'audit', 'comments', 'content', 'downloads',
    'favorites', 'groups', 'networks', 'nodes', 'people', 'preferences', 
    'probes', 'queries', 'ratings', 'renditions', 'shared_links', 'sites',
    'tags', 'trashcan', 'versions'
] 