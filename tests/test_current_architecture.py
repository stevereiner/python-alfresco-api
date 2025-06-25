"""
Current Architecture Tests

Tests for the updated python-alfresco-api with query parameter authentication.
Works with the current ClientFactory, AuthUtil, and individual clients.
"""

import pytest
import asyncio
import sys
from pathlib import Path

# Add python_alfresco_api to path
sys.path.insert(0, str(Path(__file__).parent.parent / "python_alfresco_api"))

class TestCurrentArchitecture:
    """Test the current working architecture."""
    
    @pytest.fixture
    def alfresco_config(self):
        """Alfresco configuration for testing."""
        return {
            'base_url': 'http://localhost:8080',
            'username': 'admin',
            'password': 'admin'
        }
    
    @pytest.fixture
    def auth_util(self, alfresco_config):
        """Create AuthUtil instance."""
        from python_alfresco_api.auth_util import AuthUtil
        return AuthUtil(
            base_url=alfresco_config['base_url'],
            username=alfresco_config['username'],
            password=alfresco_config['password']
        )
    
    @pytest.fixture
    def client_factory(self, alfresco_config):
        """Create ClientFactory instance."""
        from python_alfresco_api import ClientFactory
        return ClientFactory(
            base_url=alfresco_config['base_url'],
            username=alfresco_config['username'],
            password=alfresco_config['password']
        )
    
    @pytest.mark.asyncio
    async def test_auth_util_authentication(self, auth_util):
        """Test AuthUtil authentication."""
        # Test authentication
        auth_success = await auth_util.authenticate()
        assert auth_success, "Authentication should succeed"
        
        # Test ticket generation
        assert auth_util.ticket is not None, "Ticket should be generated"
        assert auth_util.ticket.startswith("TICKET_"), "Ticket should have correct format"
        
        # Test authentication state
        assert auth_util.is_authenticated(), "Should be authenticated"
        
        # Test URL parameter addition
        test_url = "http://localhost:8080/alfresco/api/discovery"
        auth_url = auth_util.add_auth_params(test_url)
        assert "alf_ticket=" in auth_url, "URL should contain ticket parameter"
        assert auth_util.ticket in auth_url, "URL should contain the actual ticket"
    
    @pytest.mark.asyncio
    async def test_client_factory_creation(self, client_factory):
        """Test ClientFactory creates all clients correctly."""
        # Test factory has auth
        assert client_factory.auth is not None, "Factory should have auth utility"
        
        # Test authentication
        auth_success = await client_factory.auth.ensure_authenticated()
        assert auth_success, "Factory authentication should succeed"
        
        # Test individual client creation
        clients = client_factory.create_all_clients()
        
        expected_clients = ['auth', 'core', 'discovery', 'search', 'workflow', 'model', 'search_sql']
        assert set(clients.keys()) == set(expected_clients), "Should create all expected clients"
        
        # Test each client has correct info
        for client_name, client in clients.items():
            info = client.get_client_info()
            assert info['api'] == client_name, f"Client {client_name} should have correct API name"
            assert info['base_url'] == client_factory.base_url, f"Client {client_name} should have correct base URL"
    
    def test_individual_client_creation(self, client_factory):
        """Test individual client creation methods."""
        # Test each creation method
        auth_client = client_factory.create_auth_client()
        core_client = client_factory.create_core_client()
        discovery_client = client_factory.create_discovery_client()
        search_client = client_factory.create_search_client()
        workflow_client = client_factory.create_workflow_client()
        model_client = client_factory.create_model_client()
        search_sql_client = client_factory.create_search_sql_client()
        
        # Test client info
        assert auth_client.get_client_info()['api'] == 'auth'
        assert core_client.get_client_info()['api'] == 'core'
        assert discovery_client.get_client_info()['api'] == 'discovery'
        assert search_client.get_client_info()['api'] == 'search'
        assert workflow_client.get_client_info()['api'] == 'workflow'
        assert model_client.get_client_info()['api'] == 'model'
        assert search_sql_client.get_client_info()['api'] == 'search_sql'
    
    def test_client_availability(self, client_factory):
        """Test that clients report their availability correctly."""
        clients = client_factory.create_all_clients()
        
        for client_name, client in clients.items():
            # All clients should be available (raw clients exist)
            assert client.is_available(), f"Client {client_name} should be available"
    
    def test_master_client_creation(self, client_factory):
        """Test MasterClient creation and dot syntax access."""
        # Test MasterClient creation
        master_client = client_factory.create_master_client()
        
        # Test MasterClient type
        assert master_client is not None, "MasterClient should be created"
        assert hasattr(master_client, 'auth'), "MasterClient should have auth attribute"
        assert hasattr(master_client, 'core'), "MasterClient should have core attribute"
        assert hasattr(master_client, 'discovery'), "MasterClient should have discovery attribute"
        assert hasattr(master_client, 'search'), "MasterClient should have search attribute"
        assert hasattr(master_client, 'workflow'), "MasterClient should have workflow attribute"
        assert hasattr(master_client, 'model'), "MasterClient should have model attribute"
        assert hasattr(master_client, 'search_sql'), "MasterClient should have search_sql attribute"
    
    def test_master_client_dot_syntax(self, client_factory):
        """Test MasterClient dot syntax access returns correct client types."""
        master_client = client_factory.create_master_client()
        
        # Test that dot syntax returns the correct client types
        from python_alfresco_api.clients.auth_client import AlfrescoAuthClient
        from python_alfresco_api.clients.core_client import AlfrescoCoreClient
        from python_alfresco_api.clients.discovery_client import AlfrescoDiscoveryClient
        from python_alfresco_api.clients.search_client import AlfrescoSearchClient
        from python_alfresco_api.clients.workflow_client import AlfrescoWorkflowClient
        from python_alfresco_api.clients.model_client import AlfrescoModelClient
        from python_alfresco_api.clients.search_sql_client import AlfrescoSearchSqlClient
        
        assert isinstance(master_client.auth, AlfrescoAuthClient), "master_client.auth should be AlfrescoAuthClient"
        assert isinstance(master_client.core, AlfrescoCoreClient), "master_client.core should be AlfrescoCoreClient"
        assert isinstance(master_client.discovery, AlfrescoDiscoveryClient), "master_client.discovery should be AlfrescoDiscoveryClient"
        assert isinstance(master_client.search, AlfrescoSearchClient), "master_client.search should be AlfrescoSearchClient"
        assert isinstance(master_client.workflow, AlfrescoWorkflowClient), "master_client.workflow should be AlfrescoWorkflowClient"
        assert isinstance(master_client.model, AlfrescoModelClient), "master_client.model should be AlfrescoModelClient"
        assert isinstance(master_client.search_sql, AlfrescoSearchSqlClient), "master_client.search_sql should be AlfrescoSearchSqlClient"
    
    def test_master_client_vs_individual_clients(self, client_factory):
        """Test that MasterClient provides same clients as individual creation."""
        # Create clients both ways
        master_client = client_factory.create_master_client()
        individual_auth = client_factory.create_auth_client()
        individual_core = client_factory.create_core_client()
        
        # Test that they're the same type of clients
        assert type(master_client.auth) == type(individual_auth), "MasterClient.auth should be same type as individual auth client"
        assert type(master_client.core) == type(individual_core), "MasterClient.core should be same type as individual core client"
        
        # Test that they have the same configuration
        master_auth_info = master_client.auth.get_client_info()
        individual_auth_info = individual_auth.get_client_info()
        
        assert master_auth_info['api'] == individual_auth_info['api'], "Both auth clients should have same API name"
        assert master_auth_info['base_url'] == individual_auth_info['base_url'], "Both auth clients should have same base URL"
    
    def test_master_client_shared_auth(self, client_factory):
        """Test that MasterClient clients share the same auth utility."""
        master_client = client_factory.create_master_client()
        
        # All clients in master should share the same auth utility
        auth_util_1 = master_client.auth.auth_util
        auth_util_2 = master_client.core.auth_util
        auth_util_3 = master_client.search.auth_util
        
        assert auth_util_1 is auth_util_2, "Auth and Core clients should share same auth utility"
        assert auth_util_2 is auth_util_3, "Core and Search clients should share same auth utility"
        assert auth_util_1 is client_factory.auth, "Master client auth should be same as factory auth"

class TestLiveServerIntegration:
    """Integration tests against live Alfresco server."""
    
    @pytest.fixture
    def alfresco_config(self):
        """Alfresco configuration for live testing."""
        return {
            'base_url': 'http://localhost:8080',
            'username': 'admin',
            'password': 'admin'
        }
    
    @pytest.fixture
    def client_factory(self, alfresco_config):
        """Create ClientFactory instance for live testing."""
        from python_alfresco_api import ClientFactory
        return ClientFactory(
            base_url=alfresco_config['base_url'],
            username=alfresco_config['username'],
            password=alfresco_config['password']
        )
    
    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_live_authentication(self, client_factory):
        """Test authentication against live server."""
        auth_success = await client_factory.auth.ensure_authenticated()
        assert auth_success, "Live authentication should succeed"
        
        ticket = client_factory.auth.ticket
        assert ticket is not None, "Should have authentication ticket"
        assert ticket.startswith("TICKET_"), "Ticket should have correct format"
    
    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_live_api_calls(self, client_factory):
        """Test actual API calls against live server."""
        import requests
        
        # Ensure authentication
        await client_factory.auth.ensure_authenticated()
        
        # Test Discovery API (publicly available)
        discovery_url = "http://localhost:8080/alfresco/api/discovery"
        auth_url = client_factory.auth.add_auth_params(discovery_url)
        
        response = requests.get(auth_url, timeout=10)
        assert response.status_code == 200, "Discovery API should return 200"
        
        data = response.json()
        assert 'entry' in data, "Discovery response should have entry"
        assert 'repository' in data['entry'], "Discovery should have repository info"
        
        # Test Core API - Get current user
        people_url = "http://localhost:8080/alfresco/api/-default-/public/alfresco/versions/1/people/-me-"
        auth_people_url = client_factory.auth.add_auth_params(people_url)
        
        response = requests.get(auth_people_url, timeout=10)
        assert response.status_code == 200, "People API should return 200"
        
        user_data = response.json()
        assert 'entry' in user_data, "User response should have entry"
        assert user_data['entry']['id'] == 'admin', "Should return admin user"
    
    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_live_crud_operations(self, client_factory):
        """Test CRUD operations against live server."""
        import requests
        from datetime import datetime
        
        # Ensure authentication
        await client_factory.auth.ensure_authenticated()
        
        # Create a test folder
        create_url = "http://localhost:8080/alfresco/api/-default-/public/alfresco/versions/1/nodes/-root-/children"
        auth_create_url = client_factory.auth.add_auth_params(create_url)
        
        folder_name = f"test_folder_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        folder_data = {
            "name": folder_name,
            "nodeType": "cm:folder",
            "properties": {
                "cm:title": "Test Folder",
                "cm:description": "Created by integration test"
            }
        }
        
        # Create folder
        response = requests.post(auth_create_url, json=folder_data, timeout=10)
        assert response.status_code == 201, "Folder creation should return 201"
        
        folder_info = response.json()
        folder_id = folder_info['entry']['id']
        assert folder_info['entry']['name'] == folder_name, "Folder should have correct name"
        
        # Read folder
        read_url = f"http://localhost:8080/alfresco/api/-default-/public/alfresco/versions/1/nodes/{folder_id}"
        auth_read_url = client_factory.auth.add_auth_params(read_url)
        
        response = requests.get(auth_read_url, timeout=10)
        assert response.status_code == 200, "Folder read should return 200"
        
        # Clean up - delete folder
        delete_url = f"http://localhost:8080/alfresco/api/-default-/public/alfresco/versions/1/nodes/{folder_id}"
        auth_delete_url = client_factory.auth.add_auth_params(delete_url)
        
        response = requests.delete(auth_delete_url, timeout=10)
        assert response.status_code == 204, "Folder deletion should return 204"

# Test configuration for pytest
def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line("markers", "integration: mark test as integration test requiring live server")
    config.addinivalue_line("markers", "asyncio: mark test as async test")

# Skip integration tests if no live server
def pytest_collection_modifyitems(config, items):
    """Skip integration tests if live server is not available."""
    import requests
    
    # Check if live server is available
    try:
        response = requests.get("http://localhost:8080/alfresco/api/-default-/public/alfresco/versions/1/probes/-ready-", timeout=5)
        server_available = response.status_code == 200
    except:
        server_available = False
    
    if not server_available:
        skip_integration = pytest.mark.skip(reason="Live Alfresco server not available at localhost:8080")
        for item in items:
            if "integration" in item.keywords:
                item.add_marker(skip_integration) 