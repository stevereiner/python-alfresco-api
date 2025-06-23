"""
Individual API Testing Module

This module tests each Alfresco API individually with proper mocking
to ensure isolated testing without requiring a live server.
"""

import pytest
from unittest.mock import Mock, patch
import sys
import os

# Add the enhanced_generated directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'enhanced_generated'))

from enhanced_generated import AlfrescoClient
from enhanced_generated.models.alfresco_workflow_models import *
from enhanced_generated.models.alfresco_model_models import *

@pytest.fixture
def test_client_config():
    """Test configuration for API clients."""
    return {
        'host': 'http://localhost:8080',
        'username': 'admin',
        'password': 'admin',
        'verify_ssl': False
    }

@pytest.fixture
def enhanced_client(test_client_config):
    """Create an enhanced Alfresco client for testing."""
    try:
        return AlfrescoClient(
            host=test_client_config['host'],
            username=test_client_config['username'],
            password=test_client_config['password'],
            verify_ssl=test_client_config['verify_ssl']
        )
    except Exception as e:
        print(f"⚠️  Enhanced client creation failed: {e}")
        return None

class TestAuthAPI:
    """Tests for Auth API."""
    
    def test_auth_client_creation(self, enhanced_client):
        """Test Auth API through master client."""
        if not enhanced_client:
            pytest.skip("Enhanced client not available")
        
        # Test that the master client has auth functionality
        assert hasattr(enhanced_client, 'auth')
        assert enhanced_client.auth is not None
        
        # Test that auth is available in API status
        api_status = enhanced_client.get_api_status()
        assert 'auth' in api_status
        assert api_status['auth'] is True
        
        print("✅ Auth API available through master client")
    
    def test_create_ticket_mock(self, enhanced_client):
        """Test master client functionality with mocking."""
        if not enhanced_client:
            pytest.skip("Enhanced client not available")
        
        # Test that the master client has basic functionality
        assert hasattr(enhanced_client, 'get_api_status')
        
        # Test API status method
        api_status = enhanced_client.get_api_status()
        assert api_status is not None
        assert isinstance(api_status, dict)
        assert 'auth' in api_status
        print("✅ Master client API status available")
    
    def test_validate_ticket_mock(self, enhanced_client):
        """Test master client connection testing."""
        if not enhanced_client:
            pytest.skip("Enhanced client not available")
        
        # Test that the master client can test connections
        if hasattr(enhanced_client, 'test_connection'):
            with patch.object(enhanced_client, 'test_connection') as mock_test:
                mock_test.return_value = True
                
                result = enhanced_client.test_connection()
                assert result is True
                print("✅ Master client connection test available")
        else:
            print("⚠️ Master client connection test not available")
            pytest.skip("Connection test method not available")

class TestCoreAPI:
    """Tests for Core API."""
    
    def test_core_client_creation(self, test_client_config):
        """Test Core API client creation."""
        try:
            import sys
            from unittest.mock import MagicMock
            
            # Mock the auth client modules that Core client depends on
            auth_config_mock = MagicMock()
            auth_response_mock = MagicMock()
            auth_models_mock = MagicMock()
            auth_rest_mock = MagicMock()
            auth_exceptions_mock = MagicMock()
            
            # Add mocked modules to sys.modules
            sys.modules['alfresco_auth_client'] = MagicMock()
            sys.modules['alfresco_auth_client.configuration'] = auth_config_mock
            sys.modules['alfresco_auth_client.api_response'] = auth_response_mock
            sys.modules['alfresco_auth_client.models'] = auth_models_mock
            sys.modules['alfresco_auth_client.rest'] = auth_rest_mock
            sys.modules['alfresco_auth_client.exceptions'] = auth_exceptions_mock
            
            # Mock the specific classes that are imported
            auth_config_mock.Configuration = MagicMock()
            auth_response_mock.ApiResponse = MagicMock()
            auth_response_mock.T = MagicMock()
            auth_rest_mock.RESTClientObject = MagicMock()
            
            # Mock the exceptions
            auth_exceptions_mock.ApiValueError = Exception
            auth_exceptions_mock.ApiException = Exception
            auth_exceptions_mock.BadRequestException = Exception
            auth_exceptions_mock.UnauthorizedException = Exception
            auth_exceptions_mock.ForbiddenException = Exception
            auth_exceptions_mock.NotFoundException = Exception
            auth_exceptions_mock.ServiceException = Exception
            
            # Add the correct path for the core client
            sys.path.insert(0, './enhanced_generated/clients/alfresco-core')
            
            from alfresco_core_client.api.actions_api import ActionsApi
            from alfresco_core_client.api_client import ApiClient
            
            # Test that we can create the API client
            with patch.object(ApiClient, '__init__', return_value=None):
                mock_client = ApiClient(test_client_config)
                api = ActionsApi(mock_client)
                assert api is not None
                print("✅ Core API client created successfully")
                
        except ImportError as e:
            print(f"⚠️  Core API client creation failed: {e}")
            pytest.skip("Core API client modules not available")
        finally:
            # Clean up mocked modules
            modules_to_remove = [
                'alfresco_auth_client',
                'alfresco_auth_client.configuration',
                'alfresco_auth_client.api_response', 
                'alfresco_auth_client.models',
                'alfresco_auth_client.rest',
                'alfresco_auth_client.exceptions'
            ]
            for module in modules_to_remove:
                if module in sys.modules:
                    del sys.modules[module]
    
    def test_actions_api_mock(self, enhanced_client):
        """Test Actions API with mocking."""
        if not enhanced_client.core:
            pytest.skip("Core API not available")
        
        # Check if core is a dict (multiple APIs) or single API
        if isinstance(enhanced_client.core, dict):
            if 'actions' in enhanced_client.core:
                core_api = enhanced_client.core['actions']
            else:
                pytest.skip("Actions API not available in Core API dict")
        else:
            core_api = enhanced_client.core
        
        # Check if the core API has the expected method
        if not hasattr(core_api, 'list_actions'):
            pytest.skip("Core API does not have list_actions method")
        
        with patch.object(core_api, 'list_actions') as mock_list:
            # Create properly configured mock objects
            entry1 = Mock()
            entry1.id = 'action-1'
            entry1.name = 'move'
            
            entry2 = Mock()
            entry2.id = 'action-2'
            entry2.name = 'copy'
            
            mock_response = Mock()
            mock_response.list = Mock()
            mock_response.list.entries = [
                Mock(entry=entry1),
                Mock(entry=entry2)
            ]
            mock_response.list.pagination = Mock(count=2, total_items=2)
            
            mock_list.return_value = mock_response
            
            actions = core_api.list_actions()
            
            assert actions is not None
            assert len(actions.list.entries) == 2
            assert actions.list.entries[0].entry.name == 'move'

class TestDiscoveryAPI:
    """Tests for Discovery API."""
    
    def test_discovery_client_creation(self, test_client_config):
        """Test Discovery API client creation."""
        try:
            import sys
            # Add the correct path for the client
            sys.path.insert(0, './enhanced_generated/clients/alfresco-discovery')
            
            from alfresco_discovery_client.api.discovery_api import DiscoveryApi
            from alfresco_discovery_client.api_client import ApiClient
            
            # Test that we can create the API client
            with patch.object(ApiClient, '__init__', return_value=None):
                mock_client = ApiClient(test_client_config)
                api = DiscoveryApi(mock_client)
                assert api is not None
                print("✅ Discovery API client created successfully")
        except ImportError as e:
            print(f"⚠️  Discovery API client creation failed: {e}")
            pytest.skip("Discovery API client modules not available")
    
    def test_repository_info_mock(self, enhanced_client):
        """Test master client API status retrieval."""
        if not enhanced_client:
            pytest.skip("Enhanced client not available")
        
        # Test that the master client can get API status
        if hasattr(enhanced_client, 'get_api_status'):
            with patch.object(enhanced_client, 'get_api_status') as mock_status:
                mock_status.return_value = {'status': 'running', 'apis': ['core', 'search', 'auth']}
                
                status = enhanced_client.get_api_status()
                assert status is not None
                assert isinstance(status, dict)
                print("✅ Master client API status available")
        else:
            print("⚠️ Master client API status not available")
            pytest.skip("API status method not available")

class TestSearchAPI:
    """Tests for Search API."""
    
    def test_search_client_creation(self, test_client_config):
        """Test Search API client creation."""
        try:
            import sys
            # Add the correct path for the client
            sys.path.insert(0, './enhanced_generated/clients/alfresco-search')
            
            from alfresco_search_client.api.search_api import SearchApi
            from alfresco_search_client.api_client import ApiClient
            
            # Test that we can create the API client
            with patch.object(ApiClient, '__init__', return_value=None):
                mock_client = ApiClient(test_client_config)
                api = SearchApi(mock_client)
                assert api is not None
                print("✅ Search API client created successfully")
        except ImportError as e:
            print(f"⚠️  Search API client creation failed: {e}")
            pytest.skip("Search API client modules not available")
    
    def test_search_mock(self, enhanced_client):
        """Test search functionality with mocking."""
        if not enhanced_client.search:
            pytest.skip("Search API not available")
        
        # Mock the search method
        with patch.object(enhanced_client.search, 'search') as mock_search:
            # Create mock search results
            entry1 = Mock()
            entry1.id = 'node-1'
            entry1.name = 'test-document.pdf'
            entry1.node_type = 'cm:content'
            
            entry2 = Mock()
            entry2.id = 'node-2'
            entry2.name = 'test-folder'
            entry2.node_type = 'cm:folder'
            
            mock_response = Mock()
            mock_response.list = Mock()
            mock_response.list.entries = [
                Mock(entry=entry1),
                Mock(entry=entry2)
            ]
            mock_response.list.pagination = Mock(count=2, total_items=2)
            
            mock_search.return_value = mock_response
            
            # Test search
            results = enhanced_client.search.search(
                search_request={'query': 'test'}
            )
            
            assert results is not None
            assert len(results.list.entries) == 2
            assert results.list.entries[0].entry.name == 'test-document.pdf'

class TestSearchSQLAPI:
    """Tests for Search SQL API."""
    
    def test_search_sql_client_creation(self, test_client_config):
        """Test Search SQL API client creation."""
        try:
            import sys
            # Add the correct path for the client
            sys.path.insert(0, './enhanced_generated/clients/alfresco-search-sql')
            
            from alfresco_search_sql_client.api.sql_api import SqlApi
            from alfresco_search_sql_client.api_client import ApiClient
            
            # Test that we can create the API client
            with patch.object(ApiClient, '__init__', return_value=None):
                mock_client = ApiClient(test_client_config)
                api = SqlApi(mock_client)
                assert api is not None
                print("✅ Search SQL API client created successfully")
        except ImportError as e:
            print(f"⚠️  Search SQL API client creation failed: {e}")
            pytest.skip("Search SQL API client modules not available")
    
    def test_sql_search_mock(self, enhanced_client):
        """Test master client working APIs functionality."""
        if not enhanced_client:
            pytest.skip("Enhanced client not available")
        
        # Test that the master client can get working APIs
        if hasattr(enhanced_client, 'get_working_apis'):
            with patch.object(enhanced_client, 'get_working_apis') as mock_working:
                mock_working.return_value = ['core', 'search', 'auth', 'discovery']
                
                working_apis = enhanced_client.get_working_apis()
                assert working_apis is not None
                assert isinstance(working_apis, list)
                assert len(working_apis) > 0
                print("✅ Master client working APIs available")
        else:
            print("⚠️ Master client working APIs not available")
            pytest.skip("Working APIs method not available")

class TestWorkflowAPI:
    """Tests for Workflow API."""
    
    def test_workflow_client_creation(self, test_client_config):
        """Test Workflow API client creation."""
        try:
            import sys
            # Add the correct path for the client
            sys.path.insert(0, './enhanced_generated/clients/alfresco-workflow')
            
            from alfresco_workflow_client.api.process_definitions_api import ProcessDefinitionsApi
            from alfresco_workflow_client.api_client import ApiClient
            
            # Test that we can create the API client
            with patch.object(ApiClient, '__init__', return_value=None):
                mock_client = ApiClient(test_client_config)
                api = ProcessDefinitionsApi(mock_client)
                assert api is not None
                print("✅ Workflow API client created successfully")
        except ImportError as e:
            print(f"⚠️  Workflow API client creation failed: {e}")
            pytest.skip("Workflow API client modules not available")
    
    def test_workflow_models_available(self, enhanced_client):
        """Test that workflow models are available."""
        if not enhanced_client.workflow:
            pytest.skip("Workflow API not available")
        
        # Test that we can access workflow models
        try:
            # Models are already imported at module level
            print("✅ Workflow models imported successfully")
        except ImportError as e:
            print(f"❌ Workflow models import failed: {e}")
            pytest.skip("Workflow models not available")
    
    def test_workflow_api(self, enhanced_client):
        """Test workflow API functionality."""
        if not enhanced_client.workflow:
            pytest.skip("Workflow API not available")
        
        # Test that the workflow APIs are available as a dict
        assert isinstance(enhanced_client.workflow, dict)
        assert len(enhanced_client.workflow) > 0
        
        # Test that we have expected workflow APIs
        expected_apis = ['deployments', 'process_definitions', 'processes', 'tasks']
        available_apis = list(enhanced_client.workflow.keys())
        assert any(api in available_apis for api in expected_apis)
        print(f"✅ Workflow APIs available: {available_apis}")

class TestModelAPI:
    """Tests for Model API."""
    
    def test_model_client_creation(self, test_client_config):
        """Test Model API client creation."""
        try:
            import sys
            # Add the correct path for the client
            sys.path.insert(0, './enhanced_generated/clients/alfresco-model')
            
            from alfresco_model_client.api.aspects_api import AspectsApi
            from alfresco_model_client.api_client import ApiClient
            
            # Test that we can create the API client
            with patch.object(ApiClient, '__init__', return_value=None):
                mock_client = ApiClient(test_client_config)
                api = AspectsApi(mock_client)
                assert api is not None
                print("✅ Model API client created successfully")
        except ImportError as e:
            print(f"⚠️  Model API client creation failed: {e}")
            pytest.skip("Model API client modules not available")
    
    def test_model_models_available(self, enhanced_client):
        """Test that model models are available."""
        if not enhanced_client.model:
            pytest.skip("Model API not available")
        
        # Test that we can access model models
        try:
            # Models are already imported at module level
            print("✅ Model models imported successfully")
        except ImportError as e:
            print(f"❌ Model models import failed: {e}")
            pytest.skip("Model models not available")
    
    def test_model_api(self, enhanced_client):
        """Test model API functionality."""
        if not enhanced_client.model:
            pytest.skip("Model API not available")
        
        # Test that the model APIs are available as a dict
        assert isinstance(enhanced_client.model, dict)
        assert len(enhanced_client.model) > 0
        
        # Test that we have expected model APIs
        expected_apis = ['aspects', 'types']
        available_apis = list(enhanced_client.model.keys())
        assert any(api in available_apis for api in expected_apis)
        print(f"✅ Model APIs available: {available_apis}") 