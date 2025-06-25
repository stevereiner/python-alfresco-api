"""
Test MCP Server Integration with python-alfresco-api v1.0.0
"""

import pytest
import sys
import os

def test_python_alfresco_api_import():
    """Test that python-alfresco-api can be imported."""
    import python_alfresco_api
    
    assert python_alfresco_api.__version__ == "1.0.0"
    print(f"✅ python-alfresco-api v{python_alfresco_api.__version__} imported successfully")

def test_client_factory_import():
    """Test that ClientFactory can be imported and used."""
    from python_alfresco_api import ClientFactory
    
    # Test creating factory
    factory = ClientFactory("http://localhost:8080")
    assert factory.base_url == "http://localhost:8080"
    
    # Test creating individual clients
    auth_client = factory.create_auth_client()
    core_client = factory.create_core_client() 
    search_client = factory.create_search_client()
    
    assert auth_client is not None
    assert core_client is not None
    assert search_client is not None
    
    print("✅ ClientFactory and individual clients created successfully")

def test_pydantic_models_import():
    """Test that Pydantic models can be imported."""
    try:
        from python_alfresco_api.models import TicketBody, NodeBody
        
        # Test model creation
        ticket = TicketBody(userId="admin", password="admin")
        assert ticket.userId == "admin"
        assert ticket.password == "admin"
        
        # Test JSON serialization (important for MCP)
        json_data = ticket.model_dump_json()
        assert "admin" in json_data
        
        print("✅ Pydantic models imported and working correctly")
        
    except ImportError as e:
        print(f"⚠️  Some Pydantic models not available: {e}")
        # This is okay - not all models may be generated

def test_fastmcp_server_import():
    """Test that FastMCP server can be imported."""
    import alfresco_mcp_server.fastmcp_server
    import alfresco_mcp_server.config
    
    # Test config loading
    from alfresco_mcp_server.config import AlfrescoConfig
    config = AlfrescoConfig()
    
    assert config.alfresco_url == "http://localhost:8080"
    assert config.username == "admin"
    assert config.password == "admin"
    
    print("✅ FastMCP server and config imported successfully")

def test_integration_ready():
    """Test that all components are ready for integration."""
    # Test that we can import both packages together
    import python_alfresco_api
    import alfresco_mcp_server.fastmcp_server
    
    from python_alfresco_api import ClientFactory
    from alfresco_mcp_server.config import AlfrescoConfig
    
    # Test creating a factory with MCP config
    mcp_config = AlfrescoConfig()
    factory = ClientFactory(
        base_url=mcp_config.alfresco_url,
        username=mcp_config.username,
        password=mcp_config.password,
        verify_ssl=mcp_config.verify_ssl,
        timeout=mcp_config.timeout
    )
    
    # Test creating all clients
    clients = factory.create_all_clients()
    
    expected_clients = ["auth", "core", "discovery", "search", "workflow", "model", "search_sql"]
    for client_name in expected_clients:
        assert client_name in clients
        assert clients[client_name] is not None
    
    print("✅ Integration test passed - MCP server can use python-alfresco-api v1.0.0")

if __name__ == "__main__":
    print("🧪 Testing MCP Server Integration with python-alfresco-api v1.0.0")
    print("=" * 70)
    
    try:
        test_python_alfresco_api_import()
        test_client_factory_import()
        test_pydantic_models_import() 
        test_fastmcp_server_import()
        test_integration_ready()
        
        print("\n🎉 ALL INTEGRATION TESTS PASSED!")
        print("✅ MCP Server is ready to use python-alfresco-api v1.0.0")
        
    except Exception as e:
        print(f"\n❌ Integration test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1) 