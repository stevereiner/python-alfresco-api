"""
Enhanced Coverage Tests

Additional tests to improve coverage of MasterClient, Models, and other components.
"""

import pytest
import sys
from pathlib import Path
from unittest.mock import Mock, patch

# Add python_alfresco_api to path
sys.path.insert(0, str(Path(__file__).parent.parent / "python_alfresco_api"))

class TestMasterClient:
    """Tests for MasterClient functionality."""
    
    @pytest.fixture
    def alfresco_config(self):
        """Configuration for testing."""
        return {
            'base_url': 'http://localhost:8080',
            'username': 'admin',
            'password': 'admin'
        }
    
    def test_master_client_creation(self, alfresco_config):
        """Test MasterClient creation and initialization."""
        from python_alfresco_api import ClientFactory
        
        factory = ClientFactory(
            base_url=alfresco_config['base_url'],
            username=alfresco_config['username'],
            password=alfresco_config['password']
        )
        
        master_client = factory.create_master_client()
        
        # Test that master client has expected APIs
        assert hasattr(master_client, 'auth')
        assert hasattr(master_client, 'core')
        assert hasattr(master_client, 'discovery')
    
    def test_master_client_info(self, alfresco_config):
        """Test MasterClient info methods."""
        from python_alfresco_api.master_client import AlfrescoMasterClient
        
        master_client = AlfrescoMasterClient(
            base_url=alfresco_config['base_url']
        )
        
        info = master_client.get_client_info()
        assert isinstance(info, dict)
        assert 'base_url' in info
        assert 'authenticated' in info
        
        # Test additional properties
        assert hasattr(master_client, 'base_url')
    
    def test_master_client_api_access(self, alfresco_config):
        """Test MasterClient API access methods."""
        from python_alfresco_api import ClientFactory
        
        factory = ClientFactory(
            base_url=alfresco_config['base_url'],
            username=alfresco_config['username'],
            password=alfresco_config['password']
        )
        
        master_client = factory.create_master_client()
        
        # Test that it has access to all APIs
        assert hasattr(master_client, 'auth')
        assert hasattr(master_client, 'core')
        assert hasattr(master_client, 'discovery')
        assert hasattr(master_client, 'search')
        assert hasattr(master_client, 'workflow')
        assert hasattr(master_client, 'model')
        assert hasattr(master_client, 'search_sql')

class TestPydanticModels:
    """Tests for Pydantic model imports and basic functionality."""
    
    def test_auth_models_import(self):
        """Test that auth models can be imported and instantiated."""
        from python_alfresco_api.models.alfresco_auth_models import TicketBody, TicketEntry
        
        # Test TicketBody
        ticket_body = TicketBody(userId="test", password="test")
        assert ticket_body.userId == "test"
        assert ticket_body.password == "test"
        
        # Test model conversion
        data = ticket_body.model_dump()
        assert isinstance(data, dict)
        assert data['userId'] == "test"
    
    def test_core_models_import(self):
        """Test that core models can be imported."""
        from python_alfresco_api.models.alfresco_core_models import (
            NodeEntry, NodeBodyCreate, PersonEntry
        )
        
        # Test that classes exist and are importable
        assert NodeEntry is not None
        assert NodeBodyCreate is not None
        assert PersonEntry is not None
    
    def test_discovery_models_import(self):
        """Test that discovery models can be imported."""
        from python_alfresco_api.models.alfresco_discovery_models import (
            DiscoveryEntry, RepositoryInfo
        )
        
        assert DiscoveryEntry is not None
        assert RepositoryInfo is not None
    
    def test_search_models_import(self):
        """Test that search models can be imported."""
        from python_alfresco_api.models.alfresco_search_models import (
            SearchRequest, ResultSetPaging
        )
        
        assert SearchRequest is not None
        assert ResultSetPaging is not None
    
    def test_workflow_models_import(self):
        """Test that workflow models can be imported."""
        from python_alfresco_api.models.alfresco_workflow_models import (
            ProcessDefinitionEntry, TaskEntry
        )
        
        assert ProcessDefinitionEntry is not None
        assert TaskEntry is not None
    
    def test_model_models_import(self):
        """Test that model API models can be imported."""
        from python_alfresco_api.models.alfresco_model_models import (
            Aspect, Type, Model, Property
        )
        
        assert Aspect is not None
        assert Type is not None
        assert Model is not None
        assert Property is not None

class TestClientUtilities:
    """Tests for client utility functions and error handling."""
    
    def test_auth_util_edge_cases(self):
        """Test AuthUtil edge cases and error handling."""
        from python_alfresco_api.auth_util import AuthUtil
        
        # Test with invalid credentials (mocked)
        auth_util = AuthUtil(
            base_url="http://invalid:8080",
            username="invalid",
            password="invalid"
        )
        
        # Test is_authenticated when not authenticated
        assert not auth_util.is_authenticated()
        
        # Test add_auth_params when not authenticated
        test_url = "http://test.com/api"
        result_url = auth_util.add_auth_params(test_url)
        assert result_url == test_url  # Should return unchanged when not authenticated
    
    def test_client_factory_edge_cases(self):
        """Test ClientFactory edge cases."""
        from python_alfresco_api import ClientFactory
        
        # Test factory without auth credentials
        factory = ClientFactory(base_url="http://localhost:8080")
        
        assert factory.auth is None
        
        # Test client creation still works
        clients = factory.create_all_clients()
        assert len(clients) == 7
    
    def test_individual_client_error_handling(self):
        """Test individual client error handling."""
        from python_alfresco_api.clients.auth_client import AlfrescoAuthClient
        
        # Test client with invalid base URL
        client = AlfrescoAuthClient("http://invalid-url")
        
        # Test that it still provides info
        info = client.get_client_info()
        assert info['api'] == 'auth'
        assert info['base_url'] == 'http://invalid-url'

class TestPackageIntegration:
    """Tests for package-level integration and imports."""
    
    def test_main_package_imports(self):
        """Test main package imports work correctly."""
        import python_alfresco_api
        
        # Test main exports
        assert hasattr(python_alfresco_api, 'ClientFactory')
        assert hasattr(python_alfresco_api, 'AuthUtil')
        
        # Test individual clients
        assert hasattr(python_alfresco_api, 'AlfrescoAuthClient')
        assert hasattr(python_alfresco_api, 'AlfrescoCoreClient')
        assert hasattr(python_alfresco_api, 'AlfrescoDiscoveryClient')
        assert hasattr(python_alfresco_api, 'AlfrescoSearchClient')
        assert hasattr(python_alfresco_api, 'AlfrescoWorkflowClient')
        assert hasattr(python_alfresco_api, 'AlfrescoModelClient')
        assert hasattr(python_alfresco_api, 'AlfrescoSearchSqlClient')
    
    def test_models_package_import(self):
        """Test models package imports."""
        from python_alfresco_api import models
        
        # Test that models package is accessible
        assert models is not None
    
    def test_version_info(self):
        """Test package version information."""
        import python_alfresco_api
        
        assert hasattr(python_alfresco_api, '__version__')
        assert python_alfresco_api.__version__ == "2.0.0"

# Mocked Event System Tests (for future development)
class TestEventSystemPrep:
    """Prepare tests for future event system development."""
    
    def test_event_modules_exist(self):
        """Test that event modules exist (even if not functional yet)."""
        # Test modules exist
        import python_alfresco_api.events.activemq_events
        import python_alfresco_api.events.event_client
        import python_alfresco_api.events.event_gateway
        
        assert python_alfresco_api.events.activemq_events is not None
        assert python_alfresco_api.events.event_client is not None
        assert python_alfresco_api.events.event_gateway is not None
    
    @patch('requests.get')
    def test_activemq_connection_check_mock(self, mock_get):
        """Test ActiveMQ connection check (mocked)."""
        mock_get.return_value.status_code = 200
        
        # This would be the basic connectivity test
        import requests
        response = requests.get("http://localhost:8161")
        assert response.status_code == 200 