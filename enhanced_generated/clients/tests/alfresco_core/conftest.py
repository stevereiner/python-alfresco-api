import pytest
import os
from unittest.mock import Mock, patch
from alfresco_client.alfresco_core.alfresco_core.api import CoreClient

@pytest.fixture
def api_client():
    """Create a test CoreClient instance"""
    base_url = os.getenv('ALFRESCO_BASE_URL', 'http://localhost:8080')
    username = os.getenv('ALFRESCO_USERNAME', 'admin')
    password = os.getenv('ALFRESCO_PASSWORD', 'admin')
    
    client = CoreClient(
        base_url=base_url,
        username=username,
        password=password,
        verify_ssl=False  # Disable SSL verification for testing
    )
    return client

@pytest.fixture
def mock_api_client():
    """Create a mocked CoreClient for unit tests that don't require actual API calls"""
    with patch('alfresco_client.alfresco_core.alfresco_core.api.CoreClient') as mock_client:
        # Configure mock behavior
        mock_instance = Mock()
        mock_client.return_value = mock_instance
        yield mock_instance

@pytest.fixture
def sample_node_data():
    """Sample node data for testing"""
    return {
        'entry': {
            'id': 'bbcd31c7-4918-4384-8d31-c74918538410',
            'name': 'Company Home',
            'nodeType': 'cm:folder',
            'isFolder': True,
            'isFile': False,
            'createdAt': '2025-06-01T16:33:44.945+0000',
            'modifiedAt': '2025-06-01T16:33:49.309+0000',
            'createdByUser': {'id': 'System', 'displayName': 'System'},
            'modifiedByUser': {'id': 'System', 'displayName': 'System'},
            'properties': {
                'cm:title': 'Company Home',
                'cm:description': 'The company root space'
            }
        }
    }

@pytest.fixture
def sample_node_children_data():
    """Sample node children data for testing"""
    return {
        'list': {
            'entries': [
                {
                    'entry': {
                        'id': '450aa41c-86de-493b-8aa4-1c86dee93b76',
                        'name': 'Data Dictionary',
                        'nodeType': 'cm:folder',
                        'isFolder': True,
                        'isFile': False,
                        'parentId': 'bbcd31c7-4918-4384-8d31-c74918538410'
                    }
                },
                {
                    'entry': {
                        'id': 'fab38862-f6ce-470e-b388-62f6ce570e30',
                        'name': 'Sites',
                        'nodeType': 'st:sites',
                        'isFolder': True,
                        'isFile': False,
                        'parentId': 'bbcd31c7-4918-4384-8d31-c74918538410'
                    }
                }
            ],
            'pagination': {
                'count': 2,
                'hasMoreItems': False,
                'totalItems': 2,
                'skipCount': 0,
                'maxItems': 100
            }
        }
    }

@pytest.fixture
def sample_comment_data():
    """Sample comment data for testing"""
    return {
        'entry': {
            'id': 'comment-123',
            'content': 'This is a test comment',
            'createdAt': '2025-06-18T10:00:00.000+0000',
            'createdBy': {'id': 'admin', 'displayName': 'Administrator'},
            'modifiedAt': '2025-06-18T10:00:00.000+0000',
            'modifiedBy': {'id': 'admin', 'displayName': 'Administrator'},
            'canEdit': True,
            'canDelete': True
        }
    }

