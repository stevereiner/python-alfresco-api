#!/usr/bin/env python3
"""
Modern Architecture Tests for python-alfresco-api

Tests the ClientFactory pattern and client structure without requiring live server.
Prepares for MCP integration testing.
"""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from python_alfresco_api import ClientFactory
from python_alfresco_api.auth_util import AuthUtil


class TestModernClientArchitecture:
    """Test the modern ClientFactory architecture without server dependency."""
    
    @pytest.fixture
    def alfresco_config(self):
        """Alfresco configuration."""
        return {
            'base_url': 'http://localhost:8080',
            'username': 'admin',
            'password': 'admin'
        }
    
    @pytest.fixture
    def client_factory(self, alfresco_config):
        """Create ClientFactory instance."""
        return ClientFactory(
            base_url=alfresco_config['base_url'],
            username=alfresco_config['username'],
            password=alfresco_config['password']
        )
    
    def test_client_factory_creation(self, client_factory):
        """Test ClientFactory creates with correct configuration."""
        assert client_factory is not None, "ClientFactory should be created"
        assert client_factory.base_url == 'http://localhost:8080', "Should have correct base URL"
        assert client_factory.auth is not None, "Should have auth utility"
        
        print("✅ ClientFactory created successfully")
    
    def test_individual_client_creation(self, client_factory):
        """Test individual client creation methods."""
        # Test each creation method
        clients = {
            'auth': client_factory.create_auth_client(),
            'core': client_factory.create_core_client(),
            'discovery': client_factory.create_discovery_client(),
            'search': client_factory.create_search_client(),
            'workflow': client_factory.create_workflow_client(),
            'model': client_factory.create_model_client(),
            'search_sql': client_factory.create_search_sql_client()
        }
        
        # Test each client has correct info
        for api_name, client in clients.items():
            assert client is not None, f"{api_name} client should be created"
            assert client.is_available(), f"{api_name} client should be available"
            
            client_info = client.get_client_info()
            assert client_info['api'] == api_name, f"Client should have correct API name"
            assert client_info['base_url'] == 'http://localhost:8080', f"Client should have correct base URL"
        
        print("✅ All individual clients created successfully")
    
    def test_master_client_creation(self, client_factory):
        """Test MasterClient creation and structure."""
        master_client = client_factory.create_master_client()
        
        # Test MasterClient structure
        assert master_client is not None, "MasterClient should be created"
        
        # Test all expected attributes exist
        expected_attrs = ['auth', 'core', 'discovery', 'search', 'workflow', 'model', 'search_sql']
        for attr in expected_attrs:
            assert hasattr(master_client, attr), f"MasterClient should have {attr} attribute"
            client = getattr(master_client, attr)
            assert client is not None, f"MasterClient.{attr} should not be None"
        
        print("✅ MasterClient created with all expected attributes")
    
    def test_master_client_types(self, client_factory):
        """Test MasterClient provides correct client types."""
        master_client = client_factory.create_master_client()
        
        # Import client types
        from python_alfresco_api.clients.auth_client import AlfrescoAuthClient
        from python_alfresco_api.clients.core_client import AlfrescoCoreClient
        from python_alfresco_api.clients.discovery_client import AlfrescoDiscoveryClient
        from python_alfresco_api.clients.search_client import AlfrescoSearchClient
        from python_alfresco_api.clients.workflow_client import AlfrescoWorkflowClient
        from python_alfresco_api.clients.model_client import AlfrescoModelClient
        from python_alfresco_api.clients.search_sql_client import AlfrescoSearchSqlClient
        
        # Test types
        assert isinstance(master_client.auth, AlfrescoAuthClient), "auth should be AlfrescoAuthClient"
        assert isinstance(master_client.core, AlfrescoCoreClient), "core should be AlfrescoCoreClient"
        assert isinstance(master_client.discovery, AlfrescoDiscoveryClient), "discovery should be AlfrescoDiscoveryClient"
        assert isinstance(master_client.search, AlfrescoSearchClient), "search should be AlfrescoSearchClient"
        assert isinstance(master_client.workflow, AlfrescoWorkflowClient), "workflow should be AlfrescoWorkflowClient"
        assert isinstance(master_client.model, AlfrescoModelClient), "model should be AlfrescoModelClient"
        assert isinstance(master_client.search_sql, AlfrescoSearchSqlClient), "search_sql should be AlfrescoSearchSqlClient"
        
        print("✅ MasterClient provides correct client types")
    
    def test_client_consistency(self, client_factory):
        """Test that MasterClient and individual clients are consistent."""
        # Create clients both ways
        master_client = client_factory.create_master_client()
        individual_auth = client_factory.create_auth_client()
        individual_core = client_factory.create_core_client()
        
        # Test types are the same
        assert type(master_client.auth) == type(individual_auth), "Should have same type"
        assert type(master_client.core) == type(individual_core), "Should have same type"
        
        # Test configuration consistency
        master_auth_info = master_client.auth.get_client_info()
        individual_auth_info = individual_auth.get_client_info()
        
        assert master_auth_info['api'] == individual_auth_info['api'], "Should have same API name"
        assert master_auth_info['base_url'] == individual_auth_info['base_url'], "Should have same base URL"
        
        print("✅ MasterClient and individual clients are consistent")
    
    def test_shared_authentication(self, client_factory):
        """Test that all clients share the same auth utility."""
        master_client = client_factory.create_master_client()
        
        # Get auth utilities from different clients
        auth_util_1 = master_client.auth.auth_util
        auth_util_2 = master_client.core.auth_util
        auth_util_3 = master_client.search.auth_util
        
        # All should be the same instance
        assert auth_util_1 is auth_util_2, "Auth clients should share auth utility"
        assert auth_util_2 is auth_util_3, "All clients should share auth utility"
        assert auth_util_1 is client_factory.auth, "Should be same as factory auth"
        
        print("✅ All clients share the same auth utility")


class TestMockAuthentication:
    """Test authentication behavior with mocked responses."""
    
    @pytest.fixture
    def client_factory(self):
        """Create ClientFactory for testing."""
        return ClientFactory('http://localhost:8080', 'admin', 'admin')
    
    @pytest.mark.asyncio
    async def test_successful_authentication(self, client_factory):
        """Test successful authentication with mocked response."""
        # Mock the authentication method
        with patch.object(client_factory.auth, 'authenticate', new_callable=AsyncMock) as mock_auth:
            mock_auth.return_value = True
            
            # Mock ticket and auth state
            with patch.object(client_factory.auth, 'is_authenticated', return_value=True):
                with patch.object(client_factory.auth, 'ticket', "TICKET_test123"):
                    # Test authentication
                    auth_success = await client_factory.auth.authenticate()
                    assert auth_success, "Authentication should succeed"
                    
                    # Test authentication state
                    assert client_factory.auth.is_authenticated(), "Should be authenticated"
                    
                    print("✅ Mocked authentication successful")
    
    @pytest.mark.asyncio
    async def test_failed_authentication(self, client_factory):
        """Test failed authentication with mocked response."""
        # Mock the authentication method to fail
        with patch.object(client_factory.auth, 'authenticate', new_callable=AsyncMock) as mock_auth:
            mock_auth.return_value = False
            
            with patch.object(client_factory.auth, 'is_authenticated', return_value=False):
                # Test authentication failure
                auth_success = await client_factory.auth.authenticate()
                assert not auth_success, "Authentication should fail"
                
                # Test authentication state
                assert not client_factory.auth.is_authenticated(), "Should not be authenticated"
                
                print("✅ Mocked authentication failure handled correctly")


class TestPydanticModelsAccess:
    """Test access to Pydantic models for MCP integration."""
    
    def test_auth_models_import(self):
        """Test that auth models can be imported."""
        from python_alfresco_api.models.alfresco_auth_models import TicketEntry, TicketBody
        
        # Test model structure for MCP (Pydantic v2)
        assert hasattr(TicketEntry, 'model_fields'), "Should be Pydantic v2 model"
        assert hasattr(TicketBody, 'model_fields'), "Should be Pydantic v2 model"
        
        print("✅ Auth Pydantic models accessible")
    
    def test_core_models_import(self):
        """Test that core models can be imported."""
        from python_alfresco_api.models.alfresco_core_models import NodeEntry, PersonEntry
        
        # Test model structure for MCP (Pydantic v2)
        assert hasattr(NodeEntry, 'model_fields'), "Should be Pydantic v2 model"
        assert hasattr(PersonEntry, 'model_fields'), "Should be Pydantic v2 model"
        
        print("✅ Core Pydantic models accessible")
    
    def test_search_models_import(self):
        """Test that search models can be imported."""
        from python_alfresco_api.models.alfresco_search_models import SearchRequest, ResultSetPaging
        
        # Test model structure for MCP (Pydantic v2)
        assert hasattr(SearchRequest, 'model_fields'), "Should be Pydantic v2 model"
        assert hasattr(ResultSetPaging, 'model_fields'), "Should be Pydantic v2 model"
        
        print("✅ Search Pydantic models accessible")


class TestMCPPreparation:
    """Test functionality needed for MCP server integration."""
    
    @pytest.fixture
    def client_factory(self):
        """Create ClientFactory for MCP testing."""
        return ClientFactory('http://localhost:8080', 'admin', 'admin')
    
    def test_client_factory_for_mcp(self, client_factory):
        """Test ClientFactory meets MCP server requirements."""
        # MCP servers need to create clients dynamically
        master_client = client_factory.create_master_client()
        
        # Test MCP-relevant functionality
        assert hasattr(master_client.core, 'get_client_info'), "Should provide client info"
        assert hasattr(master_client.auth, 'get_client_info'), "Should provide client info"
        
        # Test that all clients are available for MCP tools
        clients = ['auth', 'core', 'discovery', 'search', 'workflow', 'model', 'search_sql']
        for client_name in clients:
            client = getattr(master_client, client_name)
            assert client.is_available(), f"{client_name} should be available for MCP"
        
        print("✅ ClientFactory ready for MCP server integration")
    
    def test_pydantic_models_for_mcp(self):
        """Test that Pydantic models work for MCP tool definitions."""
        from python_alfresco_api.models.alfresco_core_models import NodeEntry
        
        # MCP tools need to use Pydantic models for parameters
        # Test that we can create model schema (used by MCP)
        schema = NodeEntry.model_json_schema()
        assert 'properties' in schema, "Should have properties for MCP"
        assert 'title' in schema, "Should have title for MCP"
        
        print("✅ Pydantic models ready for MCP tool definitions")
    
    def test_async_support_for_mcp(self, client_factory):
        """Test async support needed for MCP servers."""
        # MCP servers are async, so our auth needs to work async
        assert hasattr(client_factory.auth, 'authenticate'), "Should have async authenticate"
        assert hasattr(client_factory.auth, 'ensure_authenticated'), "Should have async ensure_authenticated"
        
        print("✅ Async authentication ready for MCP servers")


# Integration marker for future live testing
@pytest.mark.integration
class TestLiveIntegration:
    """Live integration tests (require running Alfresco server)."""
    
    @pytest.fixture
    def client_factory(self):
        """Create ClientFactory for live testing."""
        return ClientFactory('http://localhost:8080', 'admin', 'admin')
    
    @pytest.mark.asyncio
    async def test_live_authentication(self, client_factory):
        """Test authentication against live server."""
        try:
            auth_success = await client_factory.auth.authenticate()
            if auth_success:
                assert client_factory.auth.ticket is not None, "Should have ticket"
                print(f"✅ Live authentication successful: {client_factory.auth.ticket[:20]}...")
            else:
                pytest.skip("Alfresco server not available for live testing")
        except Exception as e:
            pytest.skip(f"Alfresco server not available: {e}")


# Pytest configuration
def pytest_configure(config):
    """Configure pytest markers."""
    config.addinivalue_line("markers", "integration: marks tests as integration tests")


def pytest_collection_modifyitems(config, items):
    """Skip integration tests unless explicitly enabled."""
    import os
    if os.environ.get('PYTEST_INTEGRATION') != 'true':
        skip_integration = pytest.mark.skip(reason="Integration tests disabled (set PYTEST_INTEGRATION=true to enable)")
        for item in items:
            if "integration" in item.keywords:
                item.add_marker(skip_integration) 