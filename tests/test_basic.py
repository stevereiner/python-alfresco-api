"""
Basic tests for python-alfresco-api package functionality.
"""

import pytest


def test_package_import():
    """Test that the main package can be imported."""
    import python_alfresco_api
    assert hasattr(python_alfresco_api, 'ClientFactory')
    assert hasattr(python_alfresco_api, 'AuthUtil')


def test_client_factory_basic():
    """Test basic ClientFactory functionality."""
    from python_alfresco_api import ClientFactory
    
    factory = ClientFactory(base_url="http://localhost:8080")
    assert factory.base_url == "http://localhost:8080"
    
    # Test individual client creation
    auth_client = factory.create_auth_client()
    core_client = factory.create_core_client()
    
    assert auth_client is not None
    assert core_client is not None


def test_all_clients_creation():
    """Test that all clients can be created."""
    from python_alfresco_api import ClientFactory
    
    factory = ClientFactory(
        base_url="http://localhost:8080",
        username="admin",
        password="admin"
    )
    
    clients = factory.create_all_clients()
    
    expected_clients = ["auth", "core", "discovery", "search", "workflow", "model", "search_sql"]
    for client_name in expected_clients:
        assert client_name in clients
        assert clients[client_name] is not None


def test_master_client():
    """Test master client with dot syntax."""
    from python_alfresco_api import ClientFactory
    
    factory = ClientFactory(base_url="http://localhost:8080")
    master = factory.create_master_client()
    
    # Test dot syntax access
    assert hasattr(master, 'auth')
    assert hasattr(master, 'core')
    assert hasattr(master, 'search')
    assert hasattr(master, 'workflow')


def test_pydantic_models():
    """Test that Pydantic models can be imported and used."""
    from python_alfresco_api.models.alfresco_auth_models import TicketBody
    from python_alfresco_api.models.alfresco_core_models import NodeBodyCreate
    
    # Test model creation
    ticket = TicketBody(userId="admin", password="admin")
    assert ticket.userId == "admin"
    
    node = NodeBodyCreate(name="test.txt", nodeType="cm:content")
    assert node.name == "test.txt"


def test_events_module():
    """Test that events module is preserved and importable."""
    from python_alfresco_api.events import AlfrescoEventClient
    
    # Should be able to create client (even if it fails to connect)
    try:
        client = AlfrescoEventClient()
        # Creation successful (connection may fail without server)
    except Exception:
        # Expected if no ActiveMQ/Event Gateway available
        pass 