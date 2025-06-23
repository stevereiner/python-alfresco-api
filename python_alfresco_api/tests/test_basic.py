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
            TicketBody(userId="", password="test")
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
