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

# Test configuration
TEST_CONFIG = {
    'host': 'http://localhost:8080',
    'username': 'admin',
    'password': 'admin',
    'verify_ssl': True
}

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
def enhanced_client():
    """Enhanced Alfresco client for testing."""
    try:
        from enhanced_generated import AlfrescoClient
        return AlfrescoClient(**TEST_CONFIG)
    except ImportError:
        pytest.skip("Enhanced client not available")

@pytest.fixture
def live_client():
    """Live Alfresco client for integration testing."""
    try:
        from enhanced_generated import AlfrescoClient
        client = AlfrescoClient(**TEST_CONFIG)
        
        # Test connection
        try:
            client.test_connection()
            return client
        except Exception:
            pytest.skip("Live Alfresco server not available")
            
    except ImportError:
        pytest.skip("Enhanced client not available")

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