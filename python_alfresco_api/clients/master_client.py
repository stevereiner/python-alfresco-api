"""
Alfresco Master Client - Main Entry Point

Provides lazy-loaded access to all Alfresco API clients with unified dot-syntax.
"""

from typing import TYPE_CHECKING, Optional

# Lazy imports to avoid circular dependencies and improve performance
if TYPE_CHECKING:
    from ..client_factory import ClientFactory
    from .search import AlfrescoSearchClient
    from .discovery import AlfrescoDiscoveryClient
    from .auth import AlfrescoAuthClient
    from .search_sql import AlfrescoSearchSqlClient
    from .workflow import AlfrescoWorkflowClient
    from .model import AlfrescoModelClient

# Modern clients with three-tier architecture and lazy loading
from .core import AlfrescoCoreClient


class AlfrescoMasterClient:
    """
    Master client providing lazy-loaded access to all Alfresco API clients.
    
    Provides unified dot-syntax access to all API areas while maintaining
    high performance through lazy loading - sub-clients are only created
    and imported when first accessed.
    
    Examples:
        ```python
        # Create master client
        from python_alfresco_api import ClientFactory
        from python_alfresco_api.clients import AlfrescoMasterClient
        
        factory = ClientFactory(base_url="http://localhost:8080")
        client = AlfrescoMasterClient(factory)
        
        # Access Core API (lazy loaded)
        node = client.core.nodes.get("abc123-def456")
        
        # Access Search API (lazy loaded when first used)
        results = client.search.content.search("annual report")
        
        # Access Discovery API (lazy loaded when first used) 
        info = client.discovery.repository.get_info()
        
        # Sub-clients are cached after first access
        folder = client.core.nodes.create(parent_id="-my-", request=...)
        ```
        
    Available APIs:
        - core: Node management, folders, content operations
        - search: Content and metadata search
        - discovery: Repository information and capabilities
        - workflow: Process and task management (future)
        - model: Content model introspection (future)
        
    Note:
        This master client uses lazy loading - API clients are imported
        and created only when first accessed, providing high performance
        improvement for applications that don't use all APIs.
    """
    
    def __init__(self, client_factory: 'ClientFactory'):
        """
        Initialize master client.
        
        Args:
            client_factory: Factory instance for creating individual API clients
        """
        self._client_factory = client_factory
        
        # Lazy-loaded client cache - None until first accessed
        self._core: Optional[AlfrescoCoreClient] = None
        self._search: Optional['AlfrescoSearchClient'] = None
        self._discovery: Optional['AlfrescoDiscoveryClient'] = None
        self._auth: Optional['AlfrescoAuthClient'] = None
        self._search_sql: Optional['AlfrescoSearchSqlClient'] = None
        self._workflow: Optional['AlfrescoWorkflowClient'] = None
        self._model: Optional['AlfrescoModelClient'] = None
    
    @property
    def core(self) -> AlfrescoCoreClient:
        """
        Access Core API client (lazy loaded).
        
        Provides comprehensive repository operations including:
        - Node management (files, folders, metadata)
        - Content upload/download
        - Permissions and security
        - Versioning and locking
        
        Returns:
            AlfrescoCoreClient: Core API interface
            
        Examples:
            ```python
            # Node operations
            node = client.core.nodes.get("abc123-def456")
            folder = client.core.nodes.create(parent_id="-my-", request=...)
            
            # Content operations (future)
            content = client.core.content.upload(file_path="report.pdf")
            
            # Folder operations (future)
            folders = client.core.folders.list(parent_id="folder-123")
            ```
        """
        if self._core is None:
            self._core = AlfrescoCoreClient(self._client_factory)
        return self._core
    
    @property
    def search(self) -> 'AlfrescoSearchClient':
        """
        Access Search API client (lazy loaded).
        
        Provides content and metadata search operations including:
        - Full-text search across repository content
        - CMIS queries for structured data
        - Advanced search with filters and facets
        
        Returns:
            AlfrescoSearchClient: Search API interface
            
        Examples:
            ```python
            # Simple search
            results = client.search.search("annual report")
            
            # CMIS query
            results = client.search.search(
                "SELECT * FROM cmis:document WHERE cmis:name LIKE '%report%'",
                language="cmis"
            )
            ```
        """
        if self._search is None:
            from .search import AlfrescoSearchClient
            self._search = AlfrescoSearchClient(self._client_factory)
        return self._search
    
    @property
    def discovery(self) -> 'AlfrescoDiscoveryClient':
        """
        Access Discovery API client (lazy loaded).
        
        Provides repository information and capabilities including:
        - Repository version and edition details
        - Available features and modules
        - System status and health information
        
        Returns:
            AlfrescoDiscoveryClient: Discovery API interface
            
        Examples:
            ```python
            # Get repository information
            info = client.discovery.get_repository_information()
            print(f"Alfresco version: {info.version}")
            print(f"Edition: {info.edition}")
            ```
        """
        if self._discovery is None:
            from .discovery import AlfrescoDiscoveryClient
            self._discovery = AlfrescoDiscoveryClient(self._client_factory)
        return self._discovery
    
    @property
    def auth(self) -> 'AlfrescoAuthClient':
        """
        Access Auth API client (lazy loaded).
        
        Provides authentication and ticket management operations including:
        - User authentication and session management
        - Ticket creation, validation, and logout
        - Authentication status checks
        
        Returns:
            AlfrescoAuthClient: Auth API interface
            
        Examples:
            ```python
            # Create authentication ticket
            ticket = client.auth.create_ticket("username", "password")
            
            # Validate existing ticket
            valid = client.auth.validate_ticket(ticket.entry.id)
            ```
        """
        if self._auth is None:
            from .auth import AlfrescoAuthClient
            self._auth = AlfrescoAuthClient(self._client_factory)
        return self._auth
    
    @property
    def search_sql(self) -> 'AlfrescoSearchSqlClient':
        """
        Access Search SQL API client (lazy loaded).
        
        Provides SQL-based search operations for Insight Engine including:
        - Solr SQL passthrough queries
        - Advanced SQL search capabilities
        - Structured query results
        
        Returns:
            AlfrescoSearchSqlClient: Search SQL API interface
            
        Examples:
            ```python
            # SQL-based search
            results = client.search_sql.search("SELECT * FROM alfresco WHERE SITE='mysite'")
            
            # Complex SQL query with parameters
            results = client.search_sql.search(
                "SELECT cmis:name, cmis:objectTypeId FROM cmis:document WHERE cmis:createdBy = 'admin'"
            )
            ```
        """
        if self._search_sql is None:
            from .search_sql import AlfrescoSearchSqlClient
            self._search_sql = AlfrescoSearchSqlClient(self._client_factory)
        return self._search_sql
    
    @property
    def workflow(self) -> 'AlfrescoWorkflowClient':
        """
        Access Workflow API client (lazy loaded).
        
        Provides process and task management operations including:
        - Process definition management
        - Process instance lifecycle
        - Task assignment and completion
        - Workflow variables and forms
        
        Returns:
            AlfrescoWorkflowClient: Workflow API interface
            
        Examples:
            ```python
            # List process definitions
            processes = client.workflow.process_definitions.list()
            
            # Start a new process
            instance = client.workflow.processes.start("myprocess", variables={"key": "value"})
            
            # Complete a task
            result = client.workflow.tasks.complete("task-123", variables={"approved": True})
            ```
        """
        if self._workflow is None:
            from .workflow import AlfrescoWorkflowClient
            self._workflow = AlfrescoWorkflowClient(self._client_factory)
        return self._workflow
    
    @property
    def model(self) -> 'AlfrescoModelClient':
        """
        Access Model API client (lazy loaded).
        
        Provides content model introspection operations including:
        - Custom type definitions and management
        - Aspect definitions and constraints
        - Property definitions and validation
        - Model deployment and activation
        
        Returns:
            AlfrescoModelClient: Model API interface
            
        Examples:
            ```python
            # List custom types
            types = client.model.types.list()
            
            # Get type definition
            type_def = client.model.types.get("my:customType")
            
            # List aspects
            aspects = client.model.aspects.list()
            ```
        """
        if self._model is None:
            from .model import AlfrescoModelClient
            self._model = AlfrescoModelClient(self._client_factory)
        return self._model

    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self._client_factory, 'base_url', 'unknown')
        loaded_apis = []
        if self._core is not None:
            loaded_apis.append('core')
        if self._search is not None:
            loaded_apis.append('search')
        if self._discovery is not None:
            loaded_apis.append('discovery')
        if self._auth is not None:
            loaded_apis.append('auth')
        if self._search_sql is not None:
            loaded_apis.append('search_sql')
        if self._workflow is not None:
            loaded_apis.append('workflow')
        if self._model is not None:
            loaded_apis.append('model')
        
        loaded_str = f" (loaded: {', '.join(loaded_apis)})" if loaded_apis else " (no APIs loaded yet)"
        return f"AlfrescoMasterClient(base_url='{base_url}'{loaded_str})" 