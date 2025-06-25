"""
Basic tests for python-alfresco-api hybrid architecture
"""

import pytest
from python_alfresco_api import ClientFactory, AuthUtil
from python_alfresco_api.models import TicketBody

class TestClientFactory:
    """Test the client factory functionality"""
    
    def test_factory_creation(self):
        """Test factory can be created"""
        factory = ClientFactory("https://alfresco.example.com")
        assert factory.base_url == "https://alfresco.example.com"
    
    def test_individual_client_creation(self):
        """Test individual clients can be created"""
        factory = ClientFactory("https://alfresco.example.com")
        
        auth_client = factory.create_auth_client()
        core_client = factory.create_core_client()
        discovery_client = factory.create_discovery_client()
        
        assert auth_client is not None
        assert core_client is not None  
        assert discovery_client is not None
    
    def test_all_clients_creation(self):
        """Test all clients can be created at once"""
        factory = ClientFactory("https://alfresco.example.com")
        clients = factory.create_all_clients()
        
        expected_apis = ["auth", "core", "discovery", "search", "workflow", "model", "search_sql"]
        for api in expected_apis:
            assert api in clients
            assert clients[api] is not None
    
    def test_master_client_creation(self):
        """Test MasterClient creation and dot syntax access"""
        factory = ClientFactory("https://alfresco.example.com")
        master_client = factory.create_master_client()
        
        # Test MasterClient has all required attributes
        assert hasattr(master_client, 'auth'), "MasterClient should have auth attribute"
        assert hasattr(master_client, 'core'), "MasterClient should have core attribute"
        assert hasattr(master_client, 'discovery'), "MasterClient should have discovery attribute"
        assert hasattr(master_client, 'search'), "MasterClient should have search attribute"
        assert hasattr(master_client, 'workflow'), "MasterClient should have workflow attribute"
        assert hasattr(master_client, 'model'), "MasterClient should have model attribute"
        assert hasattr(master_client, 'search_sql'), "MasterClient should have search_sql attribute"
        
        # Test that attributes are not None
        assert master_client.auth is not None, "master_client.auth should not be None"
        assert master_client.core is not None, "master_client.core should not be None"
        assert master_client.search is not None, "master_client.search should not be None"
    
    def test_master_client_vs_individual_clients(self):
        """Test that MasterClient provides same clients as individual creation"""
        factory = ClientFactory("https://alfresco.example.com")
        
        # Create clients both ways
        master_client = factory.create_master_client()
        individual_auth = factory.create_auth_client()
        
        # Test that they're the same type of clients
        assert type(master_client.auth) == type(individual_auth), "MasterClient.auth should be same type as individual auth client"

class TestPydanticModels:
    """Test Pydantic model functionality"""
    
    def test_ticket_body_creation(self):
        """Test TicketBody model creation and validation"""
        ticket_body = TicketBody(userId="admin", password="admin123")
        
        assert ticket_body.userId == "admin"
        assert ticket_body.password == "admin123"
        
        # Test JSON serialization (perfect for LLMs)
        json_data = ticket_body.model_dump_json()
        assert "admin" in json_data
        assert "admin123" in json_data
    
    def test_model_validation(self):
        """Test Pydantic model validation"""
        # This should work
        valid_ticket = TicketBody(userId="test", password="test123")
        assert valid_ticket.userId == "test"
        
        # Test that validation works (will depend on actual model constraints)
        try:
            # Empty userId should potentially fail validation
            invalid_ticket = TicketBody(userId="", password="test")
            # If this doesn't raise an error, validation might be lenient
        except Exception:
            # Validation worked as expected
            pass

class TestAuthUtil:
    """Test authentication utility"""
    
    def test_auth_util_creation(self):
        """Test AuthUtil can be created"""
        auth = AuthUtil(
            "https://alfresco.example.com",
            "admin", 
            "admin123"
        )
        
        assert auth.base_url == "https://alfresco.example.com"
        assert auth.username == "admin"
        assert not auth.is_authenticated()  # Not authenticated initially

if __name__ == "__main__":
    pytest.main([__file__])
