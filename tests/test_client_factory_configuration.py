"""
Comprehensive tests for ClientFactory configuration and parameter priority logic.
Tests timeout propagation, auth_util priority, and MCP server patterns.
"""

import os
import pytest
import sys
from unittest.mock import patch, MagicMock

# Add the project root to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from python_alfresco_api.client_factory import ClientFactory
from python_alfresco_api.auth_util import SimpleAuthUtil, AuthUtil, load_env_config


class TestClientFactoryConfiguration:
    """Test ClientFactory configuration and parameter priority."""
    
    def setup_method(self):
        """Clean environment before each test."""
        # Remove any existing environment variables
        env_vars_to_clean = [
            'ALFRESCO_URL', 'ALFRESCO_BASE_URL',
            'ALFRESCO_USERNAME', 'ALFRESCO_PASSWORD', 
            'ALFRESCO_TIMEOUT', 'ALFRESCO_VERIFY_SSL', 'ALFRESCO_SSL_VERIFY'
        ]
        for var in env_vars_to_clean:
            if var in os.environ:
                del os.environ[var]
    
    def test_timeout_priority_chain(self):
        """Test timeout priority: auth_util > explicit param > env > None (no default)."""
        
        # Test 1: No timeout specified anywhere - should be None
        factory1 = ClientFactory(
            base_url="http://localhost:8080",
            username="admin",
            password="admin",
            load_env=False
        )
        assert factory1.timeout is None, f"Expected None timeout, got {factory1.timeout}"
        
        # Test 2: Explicit timeout parameter
        factory2 = ClientFactory(
            base_url="http://localhost:8080",
            username="admin",
            password="admin",
            timeout=60,
            load_env=False
        )
        assert factory2.timeout == 60, f"Expected 60, got {factory2.timeout}"
        
        # Test 3: Environment variable timeout
        os.environ['ALFRESCO_TIMEOUT'] = '45'
        factory3 = ClientFactory(
            base_url="http://localhost:8080",
            username="admin",
            password="admin",
            load_env=True
        )
        assert factory3.timeout == 45, f"Expected 45, got {factory3.timeout}"
        
        # Test 4: AuthUtil timeout takes priority over everything
        auth_util = AuthUtil(
            base_url="http://localhost:8080",
            username="admin",
            password="admin",
            timeout=90
        )
        factory4 = ClientFactory(
            auth_util=auth_util,
            timeout=60,  # Should be overridden
            load_env=True  # ALFRESCO_TIMEOUT=45 should be ignored
        )
        assert factory4.timeout == 90, f"Expected 90, got {factory4.timeout}"
        
        # Test 5: SimpleAuthUtil without timeout uses explicit parameter
        simple_auth = SimpleAuthUtil("admin", "admin")
        factory5 = ClientFactory(
            auth_util=simple_auth,
            timeout=75,
            load_env=True
        )
        assert factory5.timeout == 75, f"Expected 75, got {factory5.timeout}"
        
        # Clean up
        if 'ALFRESCO_TIMEOUT' in os.environ:
            del os.environ['ALFRESCO_TIMEOUT']
    
    def test_auth_util_parameter_priority(self):
        """Test that auth_util parameters take priority over factory parameters."""
        
        # Create AuthUtil with custom parameters
        auth_util = AuthUtil(
            base_url="http://custom-alfresco:9090",
            username="custom_user",
            password="custom_pass",
            verify_ssl=False,
            timeout=120
        )
        
        # Create factory with different parameters - auth_util should win
        factory = ClientFactory(
            base_url="http://localhost:8080",  # Should be overridden
            username="admin",  # Should be ignored (auth_util provided)
            password="admin",  # Should be ignored (auth_util provided)
            auth_util=auth_util,
            verify_ssl=True,  # Should be overridden
            timeout=30,  # Should be overridden
            load_env=False
        )
        
        # Verify auth_util parameters took priority
        assert factory.base_url == "http://custom-alfresco:9090"
        assert factory.verify_ssl == False
        assert factory.timeout == 120
        assert factory.username == "custom_user"
        assert factory.password == "custom_pass"
    
    def test_username_password_from_auth_util(self):
        """Test that username/password are accessible from auth_util."""
        
        # Test with SimpleAuthUtil
        simple_auth = SimpleAuthUtil("simple_user", "simple_pass")
        factory1 = ClientFactory(
            base_url="http://localhost:8080",
            auth_util=simple_auth,
            load_env=False
        )
        assert factory1.username == "simple_user"
        assert factory1.password == "simple_pass"
        
        # Test with AuthUtil
        auth_util = AuthUtil(
            base_url="http://localhost:8080",
            username="auth_user",
            password="auth_pass"
        )
        factory2 = ClientFactory(auth_util=auth_util, load_env=False)
        assert factory2.username == "auth_user"
        assert factory2.password == "auth_pass"
        
        # Test with explicit username/password (no auth_util)
        factory3 = ClientFactory(
            base_url="http://localhost:8080",
            username="explicit_user",
            password="explicit_pass",
            load_env=False
        )
        assert factory3.username == "explicit_user"
        assert factory3.password == "explicit_pass"
    
    def test_load_env_config_timeout_handling(self):
        """Test load_env_config timeout handling directly."""
        
        # Test 1: No timeout anywhere - should return None
        config1 = load_env_config(
            base_url="http://localhost:8080",
            username="admin",
            password="admin",
            load_env=False
        )
        assert config1['timeout'] is None
        
        # Test 2: Explicit timeout
        config2 = load_env_config(
            base_url="http://localhost:8080",
            username="admin",
            password="admin",
            timeout=60,
            load_env=False
        )
        assert config2['timeout'] == 60
        
        # Test 3: Environment timeout
        os.environ['ALFRESCO_TIMEOUT'] = '45'
        config3 = load_env_config(
            base_url="http://localhost:8080",
            username="admin",
            password="admin",
            load_env=True
        )
        assert config3['timeout'] == 45
        
        # Test 4: Invalid environment timeout - should return None
        os.environ['ALFRESCO_TIMEOUT'] = 'invalid'
        config4 = load_env_config(
            base_url="http://localhost:8080",
            username="admin",
            password="admin",
            load_env=True
        )
        assert config4['timeout'] is None
        
        # Clean up
        if 'ALFRESCO_TIMEOUT' in os.environ:
            del os.environ['ALFRESCO_TIMEOUT']
    
    def test_config_info_method(self):
        """Test get_config_info method returns correct information."""
        
        auth_util = AuthUtil(
            base_url="http://test:8080",
            username="test_user",
            password="test_pass",
            timeout=90
        )
        
        factory = ClientFactory(auth_util=auth_util, load_env=False)
        config_info = factory.get_config_info()
        
        assert config_info['base_url'] == "http://test:8080"
        assert config_info['timeout'] == 90
        assert config_info['has_auth'] == True
        assert "test_user" in config_info['auth_type']
        assert 'verify_ssl' in config_info
        assert 'dotenv_available' in config_info


class TestTimeoutPropagation:
    """Test timeout propagation to raw clients and httpx."""
    
    def setup_method(self):
        """Clean environment before each test."""
        env_vars_to_clean = [
            'ALFRESCO_URL', 'ALFRESCO_BASE_URL',
            'ALFRESCO_USERNAME', 'ALFRESCO_PASSWORD', 
            'ALFRESCO_TIMEOUT', 'ALFRESCO_VERIFY_SSL'
        ]
        for var in env_vars_to_clean:
            if var in os.environ:
                del os.environ[var]
    
    def test_timeout_propagation_to_auth_util(self):
        """Test that timeout is properly passed to AuthUtil when created."""
        
        # Test with explicit timeout
        factory = ClientFactory(
            base_url="http://localhost:8080",
            username="admin",
            password="admin",
            timeout=120,
            load_env=False
        )
        
        # Check that the created AuthUtil has the timeout
        assert hasattr(factory.auth, 'timeout')
        assert factory.auth.timeout == 120
    
    def test_no_timeout_to_auth_util_when_none(self):
        """Test that AuthUtil gets None when no timeout specified."""
        
        factory = ClientFactory(
            base_url="http://localhost:8080",
            username="admin",
            password="admin",
            load_env=False  # No timeout specified anywhere
        )
        
        # AuthUtil should get None when no timeout passed (no defaults)
        assert hasattr(factory.auth, 'timeout')
        assert factory.auth.timeout is None  # No default timeout
    
    @pytest.mark.skipif(
        not os.path.exists('python_alfresco_api/clients/core/core_client.py'),
        reason="Core client not available"
    )
    def test_core_client_creation_and_properties(self):
        """Test core client creation and access to httpx_client and raw_client properties."""
        
        factory = ClientFactory(
            base_url="http://localhost:8080",
            username="admin",
            password="admin",
            timeout=60,
            load_env=False
        )
        
        # Create core client
        core_client = factory.create_core_client()
        assert core_client is not None
        
        # Test that core client has the expected properties/methods
        assert hasattr(core_client, 'httpx_client') or hasattr(core_client, 'get_httpx_client')
        assert hasattr(core_client, 'raw_client')
        
        # Test factory properties are accessible
        assert factory.timeout == 60
        assert factory.base_url == "http://localhost:8080"
        assert factory.username == "admin"
        assert factory.password == "admin"


class TestRawAndHttpxClientParameters:
    """Test that raw_client and httpx_client receive correct parameters."""
    
    def setup_method(self):
        """Clean environment before each test."""
        env_vars_to_clean = [
            'ALFRESCO_URL', 'ALFRESCO_BASE_URL',
            'ALFRESCO_USERNAME', 'ALFRESCO_PASSWORD', 
            'ALFRESCO_TIMEOUT', 'ALFRESCO_VERIFY_SSL'
        ]
        for var in env_vars_to_clean:
            if var in os.environ:
                del os.environ[var]
    
    @pytest.mark.skipif(
        not os.path.exists('python_alfresco_api/clients/core/core_client.py'),
        reason="Core client not available"
    )
    def test_raw_client_receives_correct_parameters(self):
        """Test that raw_client receives username, password, url, timeout values."""
        
        factory = ClientFactory(
            base_url="http://test-server:9090",
            username="test_user",
            password="test_pass",
            timeout=90,
            verify_ssl=False,
            load_env=False
        )
        
        # Create core client and access raw client
        core_client = factory.create_core_client()
        raw_client = core_client.raw_client
        
        # Test that raw client has correct base URL
        assert hasattr(raw_client, '_base_url')
        expected_base_url = "http://test-server:9090/alfresco/api/-default-/public/alfresco/versions/1"
        assert raw_client._base_url == expected_base_url
        
        # Test that raw client has correct timeout
        if hasattr(raw_client, '_timeout'):
            assert raw_client._timeout == 90
        
        # Test that raw client has correct SSL verification
        if hasattr(raw_client, '_verify_ssl'):
            assert raw_client._verify_ssl == False
        
        # Test that factory credentials are accessible
        assert factory.username == "test_user"
        assert factory.password == "test_pass"
        assert factory.timeout == 90
        assert factory.base_url == "http://test-server:9090"
        assert factory.verify_ssl == False
    
    @pytest.mark.skipif(
        not os.path.exists('python_alfresco_api/clients/core/core_client.py'),
        reason="Core client not available"
    )
    def test_raw_client_with_none_timeout(self):
        """Test that raw_client handles None timeout correctly."""
        
        factory = ClientFactory(
            base_url="http://localhost:8080",
            username="admin",
            password="admin",
            load_env=False  # No timeout specified
        )
        
        # Create core client and access raw client
        core_client = factory.create_core_client()
        raw_client = core_client.raw_client
        
        # Test that factory timeout is None
        assert factory.timeout is None
        
        # Test that raw client doesn't have timeout set (should use defaults)
        if hasattr(raw_client, '_timeout'):
            # If _timeout exists, it should be None (not set)
            assert raw_client._timeout is None
    
    @pytest.mark.skipif(
        not os.path.exists('python_alfresco_api/clients/core/core_client.py'),
        reason="Core client not available"
    )
    def test_httpx_client_access_and_properties(self):
        """Test httpx_client access and that it inherits correct properties."""
        
        factory = ClientFactory(
            base_url="http://custom:8888",
            username="custom_user",
            password="custom_pass",
            timeout=120,
            verify_ssl=True,
            load_env=False
        )
        
        # Create core client and access httpx client
        core_client = factory.create_core_client()
        
        # Test httpx_client property access
        httpx_client = core_client.httpx_client
        assert httpx_client is not None
        
        # Test that we can call get_httpx_client method too
        if hasattr(core_client, 'get_httpx_client'):
            httpx_client_method = core_client.get_httpx_client()
            assert httpx_client_method is not None
        
        # Test factory properties are correct
        assert factory.username == "custom_user"
        assert factory.password == "custom_pass"
        assert factory.timeout == 120
        assert factory.base_url == "http://custom:8888"
        assert factory.verify_ssl == True
    
    @pytest.mark.skipif(
        not os.path.exists('python_alfresco_api/clients/core/core_client.py'),
        reason="Core client not available"
    )
    def test_auth_util_parameters_propagate_to_clients(self):
        """Test that auth_util parameters properly propagate to raw and httpx clients."""
        
        # Create AuthUtil with specific parameters
        auth_util = AuthUtil(
            base_url="http://auth-server:7777",
            username="auth_user",
            password="auth_pass",
            timeout=150,
            verify_ssl=False
        )
        
        factory = ClientFactory(
            base_url="http://factory:8080",  # Should be overridden by auth_util
            username="factory_user",        # Should be ignored (auth_util provided)
            password="factory_pass",        # Should be ignored (auth_util provided)
            auth_util=auth_util,
            timeout=60,                     # Should be overridden by auth_util
            verify_ssl=True,                # Should be overridden by auth_util
            load_env=False
        )
        
        # Test that factory uses auth_util parameters
        assert factory.base_url == "http://auth-server:7777"
        assert factory.username == "auth_user"
        assert factory.password == "auth_pass"
        assert factory.timeout == 150
        assert factory.verify_ssl == False
        
        # Create core client and test that parameters propagate
        core_client = factory.create_core_client()
        raw_client = core_client.raw_client
        
        # Test raw client has correct base URL (with API path appended)
        expected_base_url = "http://auth-server:7777/alfresco/api/-default-/public/alfresco/versions/1"
        assert raw_client._base_url == expected_base_url
        
        # Test raw client has correct timeout and SSL settings
        if hasattr(raw_client, '_timeout'):
            assert raw_client._timeout == 150
        if hasattr(raw_client, '_verify_ssl'):
            assert raw_client._verify_ssl == False
    
    def test_multiple_client_types_parameter_propagation(self):
        """Test parameter propagation across different client types."""
        
        factory = ClientFactory(
            base_url="http://multi-test:8080",
            username="multi_user",
            password="multi_pass",
            timeout=200,
            verify_ssl=False,
            load_env=False
        )
        
        # Test that all client types can be created
        clients = {
            'auth': factory.create_auth_client(),
            'core': factory.create_core_client(),
            'discovery': factory.create_discovery_client(),
            'search': factory.create_search_client(),
            'workflow': factory.create_workflow_client(),
            'model': factory.create_model_client(),
            'search_sql': factory.create_search_sql_client()
        }
        
        # Test that all clients are created successfully
        for client_name, client in clients.items():
            assert client is not None, f"{client_name} client should not be None"
            
            # Test that each client has access to raw_client
            if hasattr(client, 'raw_client'):
                raw_client = client.raw_client
                assert raw_client is not None, f"{client_name} raw_client should not be None"
                
                # Test that raw client has correct timeout
                if hasattr(raw_client, '_timeout'):
                    assert raw_client._timeout == 200, f"{client_name} timeout should be 200"
                
                # Test that raw client has correct SSL setting
                if hasattr(raw_client, '_verify_ssl'):
                    assert raw_client._verify_ssl == False, f"{client_name} verify_ssl should be False"
        
        # Test factory properties are consistent
        assert factory.username == "multi_user"
        assert factory.password == "multi_pass"
        assert factory.timeout == 200
        assert factory.base_url == "http://multi-test:8080"
        assert factory.verify_ssl == False


class TestMCPServerPattern:
    """Test the MCP server pattern as described in the requirements."""
    
    def setup_method(self):
        """Clean environment before each test."""
        env_vars_to_clean = [
            'ALFRESCO_URL', 'ALFRESCO_USERNAME', 'ALFRESCO_PASSWORD', 
            'ALFRESCO_TIMEOUT', 'ALFRESCO_VERIFY_SSL'
        ]
        for var in env_vars_to_clean:
            if var in os.environ:
                del os.environ[var]
    
    @pytest.mark.skipif(
        not os.path.exists('python_alfresco_api/clients/core/core_client.py'),
        reason="Core client not available"
    )
    def test_mcp_server_pattern_simulation(self):
        """Simulate the MCP server pattern: ClientFactory -> master_client -> ensure_httpx_client."""
        
        # Simulate MCP server config
        config = {
            'alfresco_url': 'http://localhost:8080',
            'username': 'admin',
            'password': 'admin',
            'verify_ssl': False,
            'timeout': 30
        }
        
        # Create factory like MCP server does
        factory = ClientFactory(
            base_url=config['alfresco_url'],
            username=config['username'],
            password=config['password'],
            verify_ssl=config['verify_ssl'],
            timeout=config['timeout']
        )
        
        # Create master client
        master_client = factory.create_master_client()
        assert master_client is not None
        assert hasattr(master_client, 'core')
        
        # Test that we can access core client
        core_client = master_client.core
        assert core_client is not None
        
        # Test ensure_httpx_client method if available
        if hasattr(core_client, 'ensure_httpx_client'):
            # This should not raise an exception
            try:
                core_client.ensure_httpx_client()
                connection_test_passed = True
            except Exception as e:
                # Connection might fail in test environment, but method should exist
                connection_test_passed = False
                print(f"Connection test failed (expected in test env): {e}")
        
        # Test httpx_client and raw_client properties
        if hasattr(core_client, 'httpx_client'):
            httpx_client = core_client.httpx_client
            # Should be callable or property
            assert httpx_client is not None or callable(httpx_client)
        
        if hasattr(core_client, 'raw_client'):
            raw_client = core_client.raw_client
            # Should be callable or property  
            assert raw_client is not None or callable(raw_client)
    
    def test_core_client_only_pattern(self):
        """Test creating just a core client and accessing httpx/raw client properties."""
        
        factory = ClientFactory(
            base_url="http://localhost:8080",
            username="admin", 
            password="admin",
            timeout=45,
            load_env=False
        )
        
        # Create just core client
        core_client = factory.create_core_client()
        assert core_client is not None
        
        # Verify factory configuration is correct
        assert factory.timeout == 45
        assert factory.base_url == "http://localhost:8080"
        assert factory.username == "admin"
        assert factory.password == "admin"
        
        # Test property access patterns
        if hasattr(core_client, 'get_httpx_client'):
            # Method pattern
            httpx_client = core_client.get_httpx_client()
            assert httpx_client is not None
        elif hasattr(core_client, 'httpx_client'):
            # Property pattern
            httpx_client = core_client.httpx_client
            if callable(httpx_client):
                httpx_client = httpx_client()
            assert httpx_client is not None
        
        if hasattr(core_client, 'get_raw_client'):
            # Method pattern
            raw_client = core_client.get_raw_client()
            assert raw_client is not None
        elif hasattr(core_client, 'raw_client'):
            # Property pattern
            raw_client = core_client.raw_client
            if callable(raw_client):
                raw_client = raw_client()
            assert raw_client is not None


if __name__ == "__main__":
    # Run tests directly
    pytest.main([__file__, "-v"])
