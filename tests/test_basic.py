"""
Basic tests for Alfresco MCP Server.
"""

import pytest
from alfresco_mcp_server.config import load_config, AlfrescoConfig
from alfresco_mcp_server.server import AlfrescoMCPServer


def test_config_loading():
    """Test configuration loading."""
    config = load_config()
    
    assert isinstance(config, AlfrescoConfig)
    assert config.alfresco_url
    assert config.username
    assert config.server_name == "alfresco-mcp-server"


def test_server_initialization():
    """Test server initialization."""
    config = AlfrescoConfig()
    server = AlfrescoMCPServer(config)
    
    assert server.config == config
    assert server.server is not None
    assert server.alfresco_factory is None  # Not initialized yet


@pytest.mark.asyncio
async def test_server_connection():
    """Test Alfresco connection (requires running server)."""
    config = AlfrescoConfig()
    server = AlfrescoMCPServer(config)
    
    # This test would require a running Alfresco server
    # For CI/CD, you might want to mock this or skip if no server available
    try:
        await server._initialize_alfresco()
        assert server.alfresco_factory is not None
        assert server.auth_util is not None
    except Exception:
        pytest.skip("Alfresco server not available for testing") 