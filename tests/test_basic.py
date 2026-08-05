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
        # Expected if no ActiveMQ available
        pass


def test_versions_client_checkout_uses_parent_client(monkeypatch):
    """VersionsClient must use parent_client, not missing _client_factory."""
    from python_alfresco_api.clients.core.versions.versions_client import VersionsClient

    parent = object()
    client = VersionsClient(parent)
    captured = {}

    def fake_checkout(core_client, node_id):
        captured["core_client"] = core_client
        captured["node_id"] = node_id
        return {"node_id": node_id, "locked": True}

    monkeypatch.setattr(
        "python_alfresco_api.utils.version_utils.checkout_document",
        fake_checkout,
    )

    result = client.checkout("abc-123")
    assert captured["core_client"] is parent
    assert captured["node_id"] == "abc-123"
    assert result.locked is True


def test_all_subclients_repr_uses_parent_client_factory():
    """Load every subclient and call repr() so __repr__ resolves parent_client._client_factory."""
    from python_alfresco_api import ClientFactory

    base_url = "http://localhost:8080"
    factory = ClientFactory(base_url=base_url, username="admin", password="admin")
    clients = factory.create_all_clients()

    subclient_attrs = {
        "core": [
            "actions", "activities", "audit", "comments", "content", "downloads",
            "favorites", "groups", "networks", "nodes", "people", "preferences",
            "probes", "queries", "ratings", "renditions", "shared_links", "sites",
            "tags", "trashcan", "versions",
        ],
        "workflow": ["tasks", "processes", "process_definitions", "deployments"],
        "auth": ["authentication"],
        "search": ["search"],
        "discovery": ["discovery"],
        "model": ["types", "aspects"],
        "search_sql": ["sql"],
    }

    for parent_name, attrs in subclient_attrs.items():
        parent = clients[parent_name]
        for attr in attrs:
            subclient = getattr(parent, attr)
            assert subclient is not None, f"{parent_name}.{attr} should load"

            # Exercise __repr__; AttributeError here means missing _client_factory.
            text = repr(subclient)
            assert text, f"{parent_name}.{attr} repr should be non-empty"

            # Most subclients include base_url=...; those must resolve via parent_client.
            if "base_url=" in text:
                assert "unknown" not in text, (
                    f"{parent_name}.{attr} __repr__ fell back to unknown "
                    f"(likely using self._client_factory instead of parent_client): {text}"
                )
                assert base_url in text, (
                    f"{parent_name}.{attr} repr should include {base_url}: {text}"
                ) 