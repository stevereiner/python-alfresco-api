"""
Simple Tests for Alfresco API

Basic tests to verify the test infrastructure works.
"""

import pytest
from unittest.mock import Mock

def test_basic_import():
    """Test that we can import the enhanced client."""
    try:
        from enhanced_generated import AlfrescoClient
        assert AlfrescoClient is not None
    except ImportError as e:
        pytest.skip(f"Enhanced client not available: {e}")

def test_client_creation():
    """Test basic client creation."""
    try:
        from enhanced_generated import AlfrescoClient
        
        client = AlfrescoClient(
            host="http://localhost:8080",
            username="admin",
            password="admin"
        )
        
        assert client is not None
        assert client.host == "http://localhost:8080"
        assert client.username == "admin"
        assert client.password == "admin"
        
    except ImportError as e:
        pytest.skip(f"Enhanced client not available: {e}")

def test_api_status():
    """Test API status checking."""
    try:
        from enhanced_generated import AlfrescoClient
        
        client = AlfrescoClient(
            host="http://localhost:8080",
            username="admin",
            password="admin"
        )
        
        status = client.get_api_status()
        
        assert status is not None
        assert isinstance(status, dict)
        assert 'auth' in status
        assert 'core' in status
        assert 'discovery' in status
        assert 'search' in status
        assert 'workflow' in status
        assert 'model' in status
        assert 'search_sql' in status
        
    except ImportError as e:
        pytest.skip(f"Enhanced client not available: {e}")

def test_working_apis():
    """Test working APIs list."""
    try:
        from enhanced_generated import AlfrescoClient
        
        client = AlfrescoClient(
            host="http://localhost:8080",
            username="admin",
            password="admin"
        )
        
        working_apis = client.get_working_apis()
        
        assert working_apis is not None
        assert isinstance(working_apis, list)
        assert len(working_apis) >= 0
        assert len(working_apis) <= 7
        
    except ImportError as e:
        pytest.skip(f"Enhanced client not available: {e}")

def test_client_info():
    """Test client information."""
    try:
        from enhanced_generated import AlfrescoClient
        
        client = AlfrescoClient(
            host="http://localhost:8080",
            username="admin",
            password="admin"
        )
        
        info = client.get_client_info()
        
        assert info is not None
        assert isinstance(info, dict)
        assert info['host'] == "http://localhost:8080"
        assert info['username'] == "admin"
        assert info['client_type'] == "Enhanced Generated (OpenAPI)"
        
    except ImportError as e:
        pytest.skip(f"Enhanced client not available: {e}")

def test_api_urls():
    """Test API URL generation."""
    try:
        from enhanced_generated import AlfrescoClient
        
        client = AlfrescoClient(
            host="http://localhost:8080",
            username="admin",
            password="admin"
        )
        
        urls = {
            'auth': client.get_api_url('auth'),
            'core': client.get_api_url('core'),
            'discovery': client.get_api_url('discovery'),
            'search': client.get_api_url('search'),
            'workflow': client.get_api_url('workflow'),
            'model': client.get_api_url('model'),
            'search-sql': client.get_api_url('search-sql')
        }
        
        assert urls['auth'] == 'http://localhost:8080/alfresco/api/-default-/public/authentication/versions/1'
        assert urls['core'] == 'http://localhost:8080/alfresco/api/-default-/public/alfresco/versions/1'
        assert urls['discovery'] == 'http://localhost:8080/alfresco/api'
        assert urls['search'] == 'http://localhost:8080/alfresco/api/-default-/public/search/versions/1'
        assert urls['workflow'] == 'http://localhost:8080/alfresco/api/-default-/public/workflow/versions/1'
        assert urls['model'] == 'http://localhost:8080/alfresco/api/-default-/public/model/versions/1'
        assert urls['search-sql'] == 'http://localhost:8080/alfresco/api/-default-/public/search/versions/1'
        
    except ImportError as e:
        pytest.skip(f"Enhanced client not available: {e}")

def test_mock_example():
    """Test that mocking works."""
    mock_obj = Mock()
    mock_obj.method.return_value = "test_value"
    
    result = mock_obj.method()
    
    assert result == "test_value"
    mock_obj.method.assert_called_once() 