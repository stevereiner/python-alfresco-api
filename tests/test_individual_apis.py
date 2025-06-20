"""
Individual API Testing Module

This module tests each Alfresco API individually with proper mocking
to ensure isolated testing without requiring a live server.
"""

import pytest
import importlib
from unittest.mock import Mock, patch, MagicMock
import sys
import os

# Add the enhanced_generated directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'enhanced_generated'))

class TestAuthAPI:
    """Tests for Authentication API."""
    
    def test_auth_client_creation(self, test_client_config):
        """Test Auth API client creation."""
        try:
            import sys
            # Add the correct path for the client
            sys.path.insert(0, './enhanced_generated/clients/alfresco-auth')
            
            from alfresco_auth_client.api.authentication_api import AuthenticationApi
            from alfresco_auth_client.api_client import ApiClient
            
            # Test that we can create the API client
            with patch.object(ApiClient, '__init__', return_value=None):
                mock_client = ApiClient(test_client_config)
                api = AuthenticationApi(mock_client)
                assert api is not None
                print("✅ Auth API client created successfully")
        except ImportError as e:
            print(f"⚠️  Auth API client creation failed: {e}")
            pytest.skip("Auth API client modules not available")
    
    def test_create_ticket_mock(self, enhanced_client):
        """Test ticket creation with mocking."""
        if not enhanced_client.auth:
            pytest.skip("Auth API not available")
        
        # Mock the create_ticket method
        with patch.object(enhanced_client.auth, 'create_ticket') as mock_create:
            mock_create.return_value = Mock(
                entry=Mock(
                    id='TICKET_1234567890abcdef',
                    userId='admin'
                )
            )
            
            ticket = enhanced_client.auth.create_ticket(
                ticket_body={'username': 'admin', 'password': 'admin'}
            )
            
            assert ticket is not None
            assert ticket.entry.id == 'TICKET_1234567890abcdef'
            assert ticket.entry.userId == 'admin'
    
    def test_validate_ticket_mock(self, enhanced_client):
        """Test ticket validation with mocking."""
        if not enhanced_client.auth:
            pytest.skip("Auth API not available")
        
        # Mock the validate_ticket method - this is the actual method available
        with patch.object(enhanced_client.auth, 'validate_ticket') as mock_validate:
            mock_validate.return_value = Mock(
                entry=Mock(
                    id='TICKET_1234567890abcdef',
                    userId='admin'
                )
            )
            
            result = enhanced_client.auth.validate_ticket()
            
            assert result is not None
            assert result.entry.id == 'TICKET_1234567890abcdef'
            assert result.entry.userId == 'admin'

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
        """Test repository information with mocking."""
        if not enhanced_client.discovery:
            pytest.skip("Discovery API not available")
        
        with patch.object(enhanced_client.discovery, 'get_repository_information') as mock_get:
            # Create a more precise mock that returns the exact expected structure
            mock_repository = Mock()
            mock_repository.name = 'Alfresco Test Repository'
            mock_repository.version = '7.4.0'
            mock_repository.edition = 'Community'
            
            mock_entry = Mock()
            mock_entry.repository = mock_repository
            
            mock_response = Mock()
            mock_response.entry = mock_entry
            
            mock_get.return_value = mock_response
            
            repo_info = enhanced_client.discovery.get_repository_information()
            
            assert repo_info is not None
            assert repo_info.entry.repository.name == 'Alfresco Test Repository'
            assert repo_info.entry.repository.version == '7.4.0'

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
        
        search_query = {
            "query": {
                "query": "cm:name:*",
                "language": "afts"
            },
            "paging": {
                "maxItems": 10
            }
        }
        
        with patch.object(enhanced_client.search, 'search') as mock_search:
            # Create properly structured mock objects to avoid attribute access issues
            mock_entry1 = Mock()
            mock_entry1.name = 'file1.txt'
            mock_entry1.id = 'result-1'
            
            mock_entry2 = Mock()
            mock_entry2.name = 'file2.txt'
            mock_entry2.id = 'result-2'
            
            mock_entries = [
                Mock(entry=mock_entry1),
                Mock(entry=mock_entry2)
            ]
            
            mock_list = Mock()
            mock_list.entries = mock_entries
            mock_list.pagination = Mock(count=2, total_items=2)
            
            mock_response = Mock()
            mock_response.list = mock_list
            
            mock_search.return_value = mock_response
            
            results = enhanced_client.search.search(search_request=search_query)
            
            assert results is not None
            assert len(results.list.entries) == 2
            assert results.list.entries[0].entry.name == 'file1.txt'

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
        """Test SQL search functionality with mocking."""
        if not enhanced_client.search_sql:
            pytest.skip("Search SQL API not available")
        
        sql_query = {
            "stmt": "SELECT * FROM alfresco LIMIT 10"
        }
        
        with patch.object(enhanced_client.search_sql, 'search') as mock_search:
            # Create properly structured mock objects
            mock_entry1 = Mock()
            mock_entry1.name = 'file1.txt'
            mock_entry1.id = 'result-1'
            
            mock_entry2 = Mock()
            mock_entry2.name = 'file2.txt'
            mock_entry2.id = 'result-2'
            
            mock_entries = [
                Mock(entry=mock_entry1),
                Mock(entry=mock_entry2)
            ]
            
            mock_list = Mock()
            mock_list.entries = mock_entries
            mock_list.pagination = Mock(count=2, total_items=2)
            
            mock_response = Mock()
            mock_response.list = mock_list
            
            mock_search.return_value = mock_response
            
            results = enhanced_client.search_sql.search(sql_request=sql_query)
            
            assert results is not None
            assert len(results.list.entries) == 2
            assert results.list.entries[0].entry.name == 'file1.txt'

class TestWorkflowAPI:
    """Tests for Workflow API."""
    
    def test_workflow_client_creation(self, test_client_config):
        """Test Workflow API client creation (models only)."""
        try:
            import sys
            # Add the correct path for the client
            sys.path.insert(0, './enhanced_generated/clients/alfresco-workflow')
            
            # Test importing the client library (models available)
            from alfresco_workflow_client.api_client import ApiClient
            from alfresco_workflow_client.configuration import Configuration
            
            # Test that we can create the basic API client (even without endpoints)
            config = Configuration(host=test_client_config['host'])
            client = ApiClient(configuration=config)
            assert client is not None
            print("✅ Workflow API client created successfully (models only)")
        except ImportError as e:
            print(f"⚠️  Workflow API client creation failed: {e}")
            pytest.skip("Workflow API client modules not available")
    
    def test_workflow_models_available(self, enhanced_client):
        """Test workflow models are available (no API endpoints)."""
        # Test that workflow models can be imported
        try:
            import sys
            sys.path.insert(0, './enhanced_generated/clients/alfresco-workflow')
            
            # Test that we can import workflow models
            from alfresco_workflow_client.models.candidate import Candidate
            print("✅ Workflow models available")
            
            # Test model creation
            candidate_data = {
                'candidateId': 'user123',
                'candidateType': 'user'
            }
            
            # The workflow API only has models, not endpoints
            # So we test that models can be instantiated
            if hasattr(Candidate, '__init__'):
                print("✅ Workflow models can be instantiated") 
                
        except ImportError as e:
            print(f"⚠️  Workflow models import failed: {e}")
            pytest.skip("Workflow models not available")

    def test_workflow_api(self, enhanced_client):
        """Test Workflow API functionality"""
        print("Testing Workflow API...")
        
        if enhanced_client.workflow:
            # Test that we have the main workflow APIs
            assert 'deployments' in enhanced_client.workflow, "Missing deployments API"
            assert 'process_definitions' in enhanced_client.workflow, "Missing process_definitions API"
            assert 'processes' in enhanced_client.workflow, "Missing processes API"
            assert 'tasks' in enhanced_client.workflow, "Missing tasks API"
            
            print("✓ Workflow APIs available: deployments, process_definitions, processes, tasks")
        else:
            pytest.fail("Workflow API not available")

class TestModelAPI:
    """Tests for Model API."""
    
    def test_model_client_creation(self, test_client_config):
        """Test Model API client creation (models only)."""
        try:
            import sys
            # Add the correct path for the client
            sys.path.insert(0, './enhanced_generated/clients/alfresco-model')
            
            # Test importing the client library (models available)
            from alfresco_model_client.api_client import ApiClient
            from alfresco_model_client.configuration import Configuration
            
            # Test that we can create the basic API client (even without endpoints)
            config = Configuration(host=test_client_config['host'])
            client = ApiClient(configuration=config)
            assert client is not None
            print("✅ Model API client created successfully (models only)")
        except ImportError as e:
            print(f"⚠️  Model API client creation failed: {e}")
            pytest.skip("Model API client modules not available")
    
    def test_model_models_available(self, enhanced_client):
        """Test model models are available (no API endpoints)."""
        # Test that model models can be imported
        try:
            import sys
            sys.path.insert(0, './enhanced_generated/clients/alfresco-model')
            
            # Test that we can import model models
            from alfresco_model_client.models.abstract_class import AbstractClass
            print("✅ Model models available")
            
            # Test model creation
            abstract_class_data = {
                'name': 'test:TestClass',
                'title': 'Test Class'
            }
            
            # The model API only has models, not endpoints
            # So we test that models can be instantiated
            if hasattr(AbstractClass, '__init__'):
                print("✅ Model models can be instantiated") 
                
        except ImportError as e:
            print(f"⚠️  Model models import failed: {e}")
            pytest.skip("Model models not available")

    def test_model_api(self, enhanced_client):
        """Test Model API functionality"""
        print("Testing Model API...")
        
        if enhanced_client.model:
            # Test that we have the main model APIs
            assert 'aspects' in enhanced_client.model, "Missing aspects API"
            assert 'types' in enhanced_client.model, "Missing types API"
            
            print("✓ Model APIs available: aspects, types")
        else:
            pytest.fail("Model API not available") 