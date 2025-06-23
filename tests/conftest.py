"""
Pytest configuration and fixtures for Alfresco API testing.

Provides:
- Mock Alfresco server fixtures
- Test client fixtures
- Configuration fixtures
"""

import pytest
from unittest.mock import Mock, patch
from typing import Dict, Any
import asyncio

# Test configuration
TEST_CONFIG = {
    'host': 'http://localhost:8080',
    'username': 'admin',
    'password': 'admin',
    'verify_ssl': True
}

# Configure pytest markers
def pytest_configure(config):
    """Configure pytest with custom markers"""
    config.addinivalue_line("markers", "integration: mark test as integration test requiring live server")
    config.addinivalue_line("markers", "asyncio: mark test as async test")

# Configure asyncio event loop for tests
@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
def mock_alfresco_server():
    """Mock Alfresco server responses."""
    mock_server = Mock()
    
    # Mock repository information
    mock_server.get_repository_information.return_value = Mock(
        entry=Mock(
            repository=Mock(
                name="Alfresco Test Repository",
                version="7.4.0",
                edition="Community"
            )
        )
    )
    
    # Mock node responses
    mock_server.get_node.return_value = Mock(
        id="test-node-id",
        name="test-node",
        node_type="cm:content",
        is_file=True,
        is_folder=False
    )
    
    # Mock search responses
    mock_server.search.return_value = Mock(
        list=Mock(
            entries=[
                Mock(entry=Mock(id="search-result-1", name="result1")),
                Mock(entry=Mock(id="search-result-2", name="result2"))
            ],
            pagination=Mock(count=2, total_items=2)
        )
    )
    
    return mock_server

@pytest.fixture
def test_client_config():
    """Test client configuration."""
    return TEST_CONFIG.copy()

@pytest.fixture
def mock_api_client():
    """Mock API client for unit testing."""
    mock_client = Mock()
    
    # Mock configuration
    mock_client.configuration = Mock(
        host=TEST_CONFIG['host'],
        username=TEST_CONFIG['username'],
        password=TEST_CONFIG['password'],
        verify_ssl=TEST_CONFIG['verify_ssl']
    )
    
    return mock_client

@pytest.fixture
def alfresco_client():
    """Fixture providing an AlfrescoClient for testing."""
    try:
        from python_alfresco_api import AlfrescoMasterClient
        return AlfrescoMasterClient(
            base_url="http://localhost:8080",
            verify_ssl=False
        )
    except Exception as e:
        pytest.skip(f"AlfrescoMasterClient not available: {e}")

@pytest.fixture
def live_client():
    """Live Alfresco client for integration testing."""
    try:
        from python_alfresco_api import AlfrescoMasterClient
        # Convert TEST_CONFIG to match AlfrescoMasterClient parameters
        client = AlfrescoMasterClient(
            base_url=TEST_CONFIG['host'],
            verify_ssl=TEST_CONFIG['verify_ssl']
        )
        
        # Test connection
        try:
            result = asyncio.run(client.test_connection())
            return client
        except Exception:
            pytest.skip("Live Alfresco server not available")
            
    except ImportError:
        pytest.skip("Master client not available")

@pytest.fixture
def mock_responses():
    """Common mock responses for testing."""
    return {
        'auth_ticket': {
            'entry': {
                'id': 'TICKET_1234567890abcdef',
                'userId': 'admin'
            }
        },
        'node_list': {
            'list': {
                'entries': [
                    {
                        'entry': {
                            'id': 'node-1',
                            'name': 'test-file.txt',
                            'nodeType': 'cm:content',
                            'isFile': True,
                            'isFolder': False
                        }
                    },
                    {
                        'entry': {
                            'id': 'node-2', 
                            'name': 'test-folder',
                            'nodeType': 'cm:folder',
                            'isFile': False,
                            'isFolder': True
                        }
                    }
                ],
                'pagination': {
                    'count': 2,
                    'totalItems': 2
                }
            }
        },
        'site_list': {
            'list': {
                'entries': [
                    {
                        'entry': {
                            'id': 'test-site',
                            'title': 'Test Site',
                            'visibility': 'PUBLIC'
                        }
                    }
                ],
                'pagination': {
                    'count': 1,
                    'totalItems': 1
                }
            }
        }
    }

@pytest.fixture  
def master_client():
    """Fixture providing master client for integration tests."""
    try:
        from python_alfresco_api import AlfrescoMasterClient
        return AlfrescoMasterClient("http://localhost:8080")
    except Exception as e:
        pytest.skip(f"Master client not available: {e}") 