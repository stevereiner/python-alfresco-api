"""
Alfresco Master Client

Master client that provides unified access to all 7 Alfresco APIs using
the enhanced generated approach with OpenAPI Generator and Pydantic models.
"""

from typing import Dict, Any, Optional
import sys
from pathlib import Path
try:
    from .BaseClient import AlfrescoBaseClient
except ImportError:
    from BaseClient import AlfrescoBaseClient

class AlfrescoClient(AlfrescoBaseClient):
    """
    Master client for all Alfresco APIs.
    
    Provides unified access to all 7 Alfresco APIs:
    - Authentication API (auth)
    - Core API (core) - nodes, sites, people, groups, etc.
    - Discovery API (discovery)
    - Search API (search)
    - Workflow API (workflow) 
    - Model API (model)
    - Search SQL API (search_sql)
    """
    
    def __init__(
        self,
        host: str = "http://localhost:8080",
        username: str = "admin", 
        password: str = "admin",
        verify_ssl: bool = True
    ):
        """
        Initialize the master Alfresco client.
        
        Args:
            host (str): The base URL of the Alfresco instance
            username (str): Alfresco username
            password (str): Alfresco password
            verify_ssl (bool): Whether to verify SSL certificates
        """
        super().__init__(host, username, password, verify_ssl)
        
        # Set up clients path
        self.clients_path = Path(__file__).parent / "clients"
        
        # Initialize all API sub-clients
        self._initialize_sub_clients()
    
    def _apply_enhanced_fixes(self):
        """Apply enhanced fixes for generated code issues."""
        try:
            from enhanced.search_fixes import apply_all_fixes
            fixes = apply_all_fixes()
            if fixes:
                print(f"🔧 Applied enhanced fixes: {', '.join(fixes)}")
        except ImportError:
            print("⚠️  Enhanced fixes not available")
        except Exception as e:
            print(f"⚠️  Enhanced fixes failed: {e}")
    
    def _initialize_sub_clients(self):
        """Initialize all 7 API sub-clients."""
        print("🚀 Initializing Alfresco APIs...")
        
        # Apply enhanced fixes for generated code issues
        self._apply_enhanced_fixes()
        
        # Authentication API (restored structure)
        self.auth_client = self.create_api_client('alfresco_auth')
        self.auth = self._create_auth_api()
        if self.auth:
            print("   ✅ Authentication API ready")
        else:
            print("   ❌ Authentication API failed")
        
        # Core API (restored structure)
        self.core_client = self.create_api_client('alfresco_core')
        self.core = self._create_core_apis()
        if self.core:
            print("   ✅ Core API ready")
        else:
            print("   ❌ Core API failed")
        
        # Discovery API (restored structure)
        self.discovery_client = self.create_api_client('alfresco_discovery')
        self.discovery = self._create_discovery_api()
        if self.discovery:
            print("   ✅ Discovery API ready")
        else:
            print("   ❌ Discovery API failed")
        
        # Search API (restored structure)
        self.search_client = self.create_api_client('alfresco_search')
        self.search = self._create_search_api()
        if self.search:
            print("   ✅ Search API ready")
        else:
            print("   ❌ Search API failed")
        
        # Workflow API
        self.workflow_client = self.create_api_client('alfresco-workflow')
        self.workflow = self._create_workflow_apis()
        if self.workflow:
            print("   ✅ Workflow API ready")
        else:
            print("   ❌ Workflow API failed")
        
        # Model API
        self.model_client = self.create_api_client('alfresco-model')
        self.model = self._create_model_apis()
        if self.model:
            print("   ✅ Model API ready")
        else:
            print("   ❌ Model API failed")
        
        # Search SQL API (restored structure)
        self.search_sql_client = self.create_api_client('alfresco_search-sql')
        self.search_sql = self._create_search_sql_api()
        if self.search_sql:
            print("   ✅ Search SQL API ready")
        else:
            print("   ❌ Search SQL API failed")
    
    def _create_auth_api(self):
        """Create Authentication API."""
        if not self.auth_client:
            return None
        try:
            from alfresco_auth_client.api.authentication_api import AuthenticationApi
            return AuthenticationApi(self.auth_client)
        except ImportError:
            return None
    
    def _create_core_apis(self):
        """Create Core API endpoints."""
        if not self.core_client:
            return None
        try:
            # Import available Core API classes
            available_apis = {}
            
            try:
                from alfresco_core_client.api.actions_api import ActionsApi
                available_apis['actions'] = ActionsApi(self.core_client)
            except ImportError:
                print("   ⚠️  Core API: actions_api not available")
            
            # Check for other Core APIs that might be available
            core_apis = [
                ('nodes', 'nodes_api', 'NodesApi'),
                ('sites', 'sites_api', 'SitesApi'),
                ('people', 'people_api', 'PeopleApi'),
                ('groups', 'groups_api', 'GroupsApi'),
                ('activities', 'activities_api', 'ActivitiesApi'),
                ('comments', 'comments_api', 'CommentsApi'),
                ('ratings', 'ratings_api', 'RatingsApi'),
                ('tags', 'tags_api', 'TagsApi'),
                ('favorites', 'favorites_api', 'FavoritesApi'),
                ('renditions', 'renditions_api', 'RenditionsApi'),
                ('shared_links', 'shared_links_api', 'SharedLinksApi'),
                ('versions', 'versions_api', 'VersionsApi'),
                ('downloads', 'downloads_api', 'DownloadsApi'),
                ('queries', 'queries_api', 'QueriesApi'),
                ('preferences', 'preferences_api', 'PreferencesApi'),
                ('audit', 'audit_api', 'AuditApi'),
                ('probes', 'probes_api', 'ProbesApi'),
                ('trashcan', 'trashcan_api', 'TrashcanApi')
            ]
            
            for api_name, module_name, class_name in core_apis:
                try:
                    module = __import__(f'alfresco_core_client.api.{module_name}', fromlist=[class_name])
                    api_class = getattr(module, class_name)
                    available_apis[api_name] = api_class(self.core_client)
                except (ImportError, AttributeError):
                    pass  # API not available, continue
            
            # If we only have actions API, return it directly for backward compatibility
            if len(available_apis) == 1 and 'actions' in available_apis:
                return available_apis['actions']
            elif available_apis:
                return available_apis
            else:
                print("   ⚠️  Core API: No APIs available")
                return None
                
        except ImportError as e:
            print(f"   ❌ Core API import error: {e}")
            return None
    
    def _create_discovery_api(self):
        """Create Discovery API."""
        if not self.discovery_client:
            return None
        try:
            from alfresco_discovery_client.api.discovery_api import DiscoveryApi
            return DiscoveryApi(self.discovery_client)
        except ImportError:
            return None
    
    def _create_search_api(self):
        """Create Search API."""
        if not self.search_client:
            return None
        try:
            from alfresco_search_client.api.search_api import SearchApi
            return SearchApi(self.search_client)
        except ImportError:
            return None
    
    def _create_workflow_apis(self):
        """Create workflow API clients using alfresco_workflow_client structure"""
        try:
            workflow_client_path = self.clients_path / "alfresco-workflow"
            workflow_api_path = workflow_client_path / "alfresco_workflow_client" / "api"
            
            if workflow_api_path.exists():
                # Ensure the workflow client path is in Python path
                workflow_path_str = str(workflow_client_path)
                if workflow_path_str not in sys.path:
                    sys.path.insert(0, workflow_path_str)
                
                # Import using BaseClient method for consistent configuration
                workflow_config = self.create_configuration('alfresco-workflow')
                workflow_api_client = self.create_api_client('alfresco-workflow')
                
                if workflow_config and workflow_api_client:
                    # Use the consistent alfresco_workflow_client package structure
                    from alfresco_workflow_client.api.deployments_api import DeploymentsApi
                    from alfresco_workflow_client.api.process_definitions_api import ProcessDefinitionsApi
                    from alfresco_workflow_client.api.processes_api import ProcessesApi
                    from alfresco_workflow_client.api.tasks_api import TasksApi
                    
                    return {
                        'deployments': DeploymentsApi(workflow_api_client),
                        'process_definitions': ProcessDefinitionsApi(workflow_api_client),
                        'processes': ProcessesApi(workflow_api_client),
                        'tasks': TasksApi(workflow_api_client)
                    }
                else:
                    print("Failed to create workflow configuration or API client")
                    return {}
            else:
                print(f"Workflow API path not found: {workflow_api_path}")
                return {}
        except Exception as e:
            print(f"Failed to create workflow APIs: {e}")
            return {}
    
    def _create_model_apis(self):
        """Create model API clients using alfresco_model_client structure"""
        try:
            model_client_path = self.clients_path / "alfresco-model"
            model_api_path = model_client_path / "alfresco_model_client" / "api"
            
            if model_api_path.exists():
                # Add the model client path to Python path temporarily
                model_path_str = str(model_client_path)
                if model_path_str not in sys.path:
                    sys.path.insert(0, model_path_str)
                
                # Import using BaseClient method for consistent configuration
                model_config = self.create_configuration('alfresco-model')
                model_api_client = self.create_api_client('alfresco-model')
                
                if model_config and model_api_client:
                    from alfresco_model_client.api.aspects_api import AspectsApi
                    from alfresco_model_client.api.types_api import TypesApi
                    
                    return {
                        'aspects': AspectsApi(model_api_client),
                        'types': TypesApi(model_api_client)
                    }
                else:
                    print("Failed to create model configuration or API client")
                    return {}
            else:
                print(f"Model API path not found: {model_api_path}")
                return {}
        except Exception as e:
            print(f"Failed to create model APIs: {e}")
            return {}
    
    def _create_search_sql_api(self):
        """Create Search SQL API."""
        if not self.search_sql_client:
            return None
        try:
            # Use importlib to handle hyphen in package name
            import importlib
            sql_api_module = importlib.import_module('alfresco_search_sql_client.api.sql_api')
            SqlApi = getattr(sql_api_module, 'SqlApi')
            return SqlApi(self.search_sql_client)
        except ImportError:
            return None
    
    def get_api_status(self) -> Dict[str, bool]:
        """
        Get the status of all API sub-clients.
        
        Returns:
            dict: Status of each API (True if available, False if not)
        """
        return {
            'auth': self.auth is not None,
            'core': self.core is not None,
            'discovery': self.discovery is not None,
            'search': self.search is not None,
            'workflow': self.workflow is not None and bool(self.workflow),
            'model': self.model is not None and bool(self.model),
            'search_sql': self.search_sql is not None
        }
    
    def get_working_apis(self) -> list:
        """
        Get list of successfully initialized APIs.
        
        Returns:
            list: Names of working APIs
        """
        status = self.get_api_status()
        return [api for api, working in status.items() if working]
    
    def test_connection(self) -> Dict[str, Any]:
        """
        Test connection to Alfresco server.
        
        Returns:
            dict: Connection test results
        """
        working_apis = self.get_working_apis()
        
        results = {
            'host': self.host,
            'username': self.username,
            'total_apis': 7,
            'working_apis': len(working_apis),
            'working_api_list': working_apis,
            'success_rate': f"{len(working_apis)}/7 ({len(working_apis)/7*100:.1f}%)"
        }
        
        # Test Discovery API if available
        if self.discovery:
            try:
                info = self.discovery.get_repository_information()
                results['discovery_test'] = '✅ Success'
            except Exception as e:
                results['discovery_test'] = f'❌ Failed: {e}'
        
        return results 
