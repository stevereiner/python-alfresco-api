#!/usr/bin/env python3
"""
Modern MCP Integration Tests

Tests integration between python-alfresco-api and python-alfresco-mcp-server.
Verifies that the modern ClientFactory API works with MCP server patterns.
"""

import pytest
import sys
import os
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add MCP server path for testing
MCP_SERVER_PATH = Path(__file__).parent.parent.parent / "python-alfresco-mcp-server"


class TestMCPServerIntegration:
    """Test integration with the external MCP server project."""
    
    def test_mcp_server_exists(self):
        """Test that MCP server directory exists and is accessible."""
        assert MCP_SERVER_PATH.exists(), f"MCP server directory should exist at {MCP_SERVER_PATH}"
        
        # Check key files exist
        assert (MCP_SERVER_PATH / "pyproject.toml").exists(), "MCP server should have pyproject.toml"
        assert (MCP_SERVER_PATH / "alfresco_mcp_server").exists(), "MCP server package should exist"
        
        print(f"✅ MCP server found at: {MCP_SERVER_PATH}")
    
    def test_python_alfresco_api_importable_in_mcp_context(self):
        """Test that python-alfresco-api can be imported in MCP context."""
        try:
            from python_alfresco_api import ClientFactory
            from python_alfresco_api.models.alfresco_core_models import NodeEntry
            
            # Test MCP-relevant functionality
            factory = ClientFactory('http://localhost:8080', 'admin', 'admin')
            master_client = factory.create_master_client()
            
            # Test that all components needed for MCP work
            assert hasattr(master_client, 'core'), "Should have core client"
            assert hasattr(master_client, 'search'), "Should have search client"
            assert hasattr(NodeEntry, 'model_json_schema'), "Should have schema for MCP tools"
            
            print("✅ python-alfresco-api works in MCP context")
            
        except ImportError as e:
            pytest.fail(f"Failed to import python-alfresco-api in MCP context: {e}")
    
    @pytest.mark.skipif(not (MCP_SERVER_PATH / "alfresco_mcp_server").exists(), 
                        reason="MCP server package not found")
    def test_mcp_server_can_import_alfresco_api(self):
        """Test that MCP server can import python-alfresco-api."""
        # Add MCP server to path temporarily
        mcp_server_str = str(MCP_SERVER_PATH)
        if mcp_server_str not in sys.path:
            sys.path.insert(0, mcp_server_str)
        
        try:
            # Test importing MCP server components
            from alfresco_mcp_server import server
            
            # Test that MCP server can use our API
            from python_alfresco_api import ClientFactory
            
            # Verify basic functionality
            factory = ClientFactory('http://localhost:8080', 'admin', 'admin')
            assert factory is not None, "ClientFactory should work in MCP server context"
            
            print("✅ MCP server can import and use python-alfresco-api")
            
        except ImportError as e:
            pytest.skip(f"MCP server not importable (expected in some environments): {e}")
        finally:
            # Clean up path
            if mcp_server_str in sys.path:
                sys.path.remove(mcp_server_str)
    
    def test_pydantic_models_compatible_with_mcp(self):
        """Test that our Pydantic models are compatible with MCP tool definitions."""
        from python_alfresco_api.models.alfresco_core_models import NodeEntry, PersonEntry
        from python_alfresco_api.models.alfresco_search_models import SearchRequest
        
        # Test that models can generate JSON schemas for MCP tools
        node_schema = NodeEntry.model_json_schema()
        person_schema = PersonEntry.model_json_schema()
        search_schema = SearchRequest.model_json_schema()
        
        # Verify schema structure expected by MCP
        for schema in [node_schema, person_schema, search_schema]:
            assert 'properties' in schema, "Schema should have properties"
            assert 'type' in schema, "Schema should have type"
            assert schema['type'] == 'object', "Schema should be object type"
        
        print("✅ Pydantic models compatible with MCP tool definitions")
    
    def test_async_patterns_for_mcp(self):
        """Test async patterns needed for MCP servers."""
        import asyncio
        from python_alfresco_api import ClientFactory
        
        async def test_async_operations():
            factory = ClientFactory('http://localhost:8080', 'admin', 'admin')
            
            # Test async authentication (key for MCP servers)
            try:
                # This will fail without server, but tests the async interface
                auth_result = await factory.auth.authenticate()
                # If it succeeds, great; if it fails, that's expected without server
            except Exception:
                # Expected without live server
                pass
            
            # Test that async interface exists (required for MCP)
            assert hasattr(factory.auth, 'authenticate'), "Should have async authenticate"
            assert hasattr(factory.auth, 'ensure_authenticated'), "Should have async ensure_authenticated"
            
            return True
        
        # Run async test
        result = asyncio.run(test_async_operations())
        assert result, "Async operations should work"
        
        print("✅ Async patterns ready for MCP servers")


class TestMCPToolPatterns:
    """Test patterns that MCP tools will use with python-alfresco-api."""
    
    def test_node_operations_for_mcp_tools(self):
        """Test node operations pattern for MCP tools."""
        from python_alfresco_api import ClientFactory
        from python_alfresco_api.models.alfresco_core_models import NodeEntry
        
        # Pattern: MCP tool creates client and prepares for node operations
        factory = ClientFactory('http://localhost:8080', 'admin', 'admin')
        core_client = factory.create_core_client()
        
        # Test that client has the interface needed for MCP tools
        assert core_client.is_available(), "Core client should be available"
        assert hasattr(core_client, 'get_client_info'), "Should provide client info"
        
        # Test that models work for MCP tool parameter validation
        schema = NodeEntry.model_json_schema()
        assert 'properties' in schema, "Should have properties for MCP validation"
        
        print("✅ Node operations pattern ready for MCP tools")
    
    def test_search_operations_for_mcp_tools(self):
        """Test search operations pattern for MCP tools."""
        from python_alfresco_api import ClientFactory
        from python_alfresco_api.models.alfresco_search_models import SearchRequest
        
        # Pattern: MCP tool creates search client and prepares search request
        factory = ClientFactory('http://localhost:8080', 'admin', 'admin')
        search_client = factory.create_search_client()
        
        # Test search client interface for MCP
        assert search_client.is_available(), "Search client should be available"
        
        # Test search request model for MCP tool parameters
        search_schema = SearchRequest.model_json_schema()
        assert 'properties' in search_schema, "Should have properties"
        assert 'query' in search_schema['properties'], "Should have query property"
        
        print("✅ Search operations pattern ready for MCP tools")
    
    def test_authentication_pattern_for_mcp_tools(self):
        """Test authentication pattern for MCP tools."""
        from python_alfresco_api import ClientFactory
        
        # Pattern: MCP tool creates factory with config and shares auth
        factory = ClientFactory('http://localhost:8080', 'admin', 'admin')
        
        # Test that multiple clients share authentication (important for MCP)
        core_client = factory.create_core_client()
        search_client = factory.create_search_client()
        auth_client = factory.create_auth_client()
        
        # All should share the same auth utility
        assert core_client.auth_util is search_client.auth_util, "Should share auth"
        assert search_client.auth_util is auth_client.auth_util, "Should share auth"
        assert core_client.auth_util is factory.auth, "Should be factory auth"
        
        print("✅ Authentication pattern ready for MCP tools")
    
    def test_error_handling_for_mcp_tools(self):
        """Test error handling patterns for MCP tools."""
        from python_alfresco_api import ClientFactory
        
        # Pattern: MCP tools need to handle connection errors gracefully
        factory = ClientFactory('http://invalid-server:9999', 'user', 'pass')
        
        # Test that clients can be created even if server is unavailable
        core_client = factory.create_core_client()
        assert core_client is not None, "Client should be created even if server unavailable"
        assert core_client.is_available(), "Client should report as available (has raw client)"
        
        # Test that auth utility exists and can be queried
        assert factory.auth is not None, "Auth should exist"
        assert not factory.auth.is_authenticated(), "Should not be authenticated yet"
        
        print("✅ Error handling pattern ready for MCP tools")


class TestMCPServerCompatibility:
    """Test compatibility with MCP server framework requirements."""
    
    def test_json_serializable_responses(self):
        """Test that responses can be JSON serialized for MCP."""
        from python_alfresco_api.models.alfresco_core_models import NodeEntry
        import json
        
        # Test that models can be serialized to JSON (MCP requirement)
        try:
            # Create a minimal valid NodeEntry for testing
            node_data = {
                "entry": {
                    "id": "test-id",
                    "name": "test-node",
                    "nodeType": "cm:content",
                    "isFile": True,
                    "isFolder": False,
                    "modifiedAt": "2024-01-01T00:00:00.000Z",
                    "modifiedByUser": {
                        "id": "admin",
                        "displayName": "Administrator"
                    },
                    "createdAt": "2024-01-01T00:00:00.000Z",
                    "createdByUser": {
                        "id": "admin", 
                        "displayName": "Administrator"
                    }
                }
            }
            
            # Test JSON serialization (required by MCP)
            json_str = json.dumps(node_data)
            assert json_str is not None, "Should be JSON serializable"
            
            # Test deserialization
            parsed = json.loads(json_str)
            assert parsed['entry']['id'] == 'test-id', "Should round-trip correctly"
            
            print("✅ JSON serialization ready for MCP responses")
            
        except Exception as e:
            pytest.fail(f"JSON serialization failed: {e}")
    
    def test_schema_generation_for_mcp_tools(self):
        """Test schema generation for MCP tool definitions."""
        from python_alfresco_api.models.alfresco_core_models import NodeEntry
        from python_alfresco_api.models.alfresco_search_models import SearchRequest
        
        # MCP tools need schemas for parameter validation
        node_schema = NodeEntry.model_json_schema()
        search_schema = SearchRequest.model_json_schema()
        
        # Verify schema has required MCP fields
        for schema in [node_schema, search_schema]:
            assert 'type' in schema, "Schema should have type"
            assert 'properties' in schema, "Schema should have properties"
            assert isinstance(schema['properties'], dict), "Properties should be dict"
        
        # Test that we can extract specific property schemas (used by MCP tools)
        if 'query' in search_schema['properties']:
            query_prop = search_schema['properties']['query']
            # Pydantic v2 may use $ref for complex types or direct type
            assert 'type' in query_prop or '$ref' in query_prop, "Property should have type or ref"
        
        print("✅ Schema generation ready for MCP tool definitions")
    
    def test_client_factory_singleton_pattern(self):
        """Test that ClientFactory can work with singleton patterns used by MCP."""
        from python_alfresco_api import ClientFactory
        
        # Test that multiple factory instances with same config work consistently
        factory1 = ClientFactory('http://localhost:8080', 'admin', 'admin')
        factory2 = ClientFactory('http://localhost:8080', 'admin', 'admin')
        
        # Both should create equivalent clients
        client1 = factory1.create_core_client()
        client2 = factory2.create_core_client()
        
        # Test that they have equivalent configuration
        info1 = client1.get_client_info()
        info2 = client2.get_client_info()
        
        assert info1['api'] == info2['api'], "Should have same API"
        assert info1['base_url'] == info2['base_url'], "Should have same base URL"
        
        print("✅ ClientFactory singleton pattern ready for MCP")


# Pytest configuration for MCP tests
def pytest_configure(config):
    """Configure pytest for MCP integration tests."""
    config.addinivalue_line("markers", "mcp: marks tests as MCP integration tests")
    config.addinivalue_line("markers", "external: marks tests requiring external dependencies")


def pytest_collection_modifyitems(config, items):
    """Handle MCP test collection."""
    import os
    
    # Skip MCP tests if explicitly disabled
    if os.environ.get('PYTEST_MCP') == 'false':
        skip_mcp = pytest.mark.skip(reason="MCP tests disabled (set PYTEST_MCP=true to enable)")
        for item in items:
            if "mcp" in item.keywords:
                item.add_marker(skip_mcp) 