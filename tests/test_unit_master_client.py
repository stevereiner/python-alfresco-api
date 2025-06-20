"""
Unit Tests for Enhanced Alfresco Master Client

Tests the master client functionality with mocked dependencies.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from typing import Dict, Any

class TestAlfrescoMasterClient:
    """Unit tests for the Alfresco master client."""
    
    def test_client_initialization(self, test_client_config):
        """Test client initialization with config."""
        with patch('enhanced_generated.BaseClient.AlfrescoBaseClient.__init__', return_value=None) as mock_base:
            with patch('enhanced_generated.AlfrescoClient.AlfrescoClient._initialize_sub_clients') as mock_init:
                # Import after patching
                from enhanced_generated import AlfrescoClient
                
                client = AlfrescoClient(**test_client_config)
                
                # Verify base client was called
                mock_base.assert_called_once_with(
                    test_client_config['host'],
                    test_client_config['username'], 
                    test_client_config['password'],
                    test_client_config['verify_ssl']
                )
                
                # Verify sub-clients were initialized
                mock_init.assert_called_once()
    
    def test_api_status_check(self, enhanced_client):
        """Test API status checking."""
        # Mock the API status
        enhanced_client.auth = Mock()
        enhanced_client.core = Mock()
        enhanced_client.discovery = Mock()
        enhanced_client.search = Mock()
        enhanced_client.workflow = None  # Simulate missing API
        enhanced_client.model = Mock()
        enhanced_client.search_sql = Mock()
        
        status = enhanced_client.get_api_status()
        
        assert status['auth'] is True
        assert status['core'] is True
        assert status['discovery'] is True
        assert status['search'] is True
        assert status['workflow'] is False
        assert status['model'] is True
        assert status['search_sql'] is True
    
    def test_working_apis_list(self, enhanced_client):
        """Test getting list of working APIs."""
        # Mock some APIs as available, some as missing
        enhanced_client.auth = Mock()
        enhanced_client.core = None
        enhanced_client.discovery = Mock()
        enhanced_client.search = None
        enhanced_client.workflow = Mock()
        enhanced_client.model = None
        enhanced_client.search_sql = Mock()
        
        working_apis = enhanced_client.get_working_apis()
        
        assert 'auth' in working_apis
        assert 'core' not in working_apis
        assert 'discovery' in working_apis
        assert 'search' not in working_apis
        assert 'workflow' in working_apis
        assert 'model' not in working_apis
        assert 'search_sql' in working_apis
        assert len(working_apis) == 4
    
    def test_connection_test_mock(self, enhanced_client):
        """Test connection testing with mocked discovery."""
        # Mock discovery API
        mock_discovery = Mock()
        mock_discovery.get_repository_information.return_value = Mock(
            entry=Mock(
                repository=Mock(
                    name="Test Repository",
                    version="7.4.0",
                    edition="Community"
                )
            )
        )
        enhanced_client.discovery = mock_discovery
        
        # Mock working APIs
        enhanced_client.get_working_apis = Mock(return_value=['auth', 'discovery', 'search'])
        
        results = enhanced_client.test_connection()
        
        assert results['host'] == 'http://localhost:8080'
        assert results['username'] == 'admin'
        assert results['total_apis'] == 7
        assert results['working_apis'] == 3
        assert results['success_rate'] == '3/7 (42.9%)'
        assert results['discovery_test'] == '✅ Success'
    
    def test_connection_test_failure(self, enhanced_client):
        """Test connection testing when discovery fails."""
        # Mock discovery API to fail
        mock_discovery = Mock()
        mock_discovery.get_repository_information.side_effect = Exception("Connection failed")
        enhanced_client.discovery = mock_discovery
        
        # Mock working APIs
        enhanced_client.get_working_apis = Mock(return_value=['auth', 'discovery'])
        
        results = enhanced_client.test_connection()
        
        assert results['discovery_test'] == '❌ Failed: Connection failed'
    
    def test_enhanced_fixes_application(self, enhanced_client):
        """Test that enhanced fixes are applied."""
        with patch('enhanced_generated.AlfrescoClient.AlfrescoClient._apply_enhanced_fixes') as mock_fixes:
            # Re-initialize to trigger fixes
            enhanced_client._apply_enhanced_fixes()
            
            mock_fixes.assert_called_once()
    
    def test_api_url_generation(self, enhanced_client):
        """Test API URL generation for different APIs."""
        urls = {
            'auth': enhanced_client.get_api_url('auth'),
            'core': enhanced_client.get_api_url('core'),
            'discovery': enhanced_client.get_api_url('discovery'),
            'search': enhanced_client.get_api_url('search'),
            'workflow': enhanced_client.get_api_url('workflow'),
            'model': enhanced_client.get_api_url('model'),
            'search-sql': enhanced_client.get_api_url('search-sql')
        }
        
        assert urls['auth'] == 'http://localhost:8080/alfresco/api/-default-/public/authentication/versions/1'
        assert urls['core'] == 'http://localhost:8080/alfresco/api/-default-/public/alfresco/versions/1'
        assert urls['discovery'] == 'http://localhost:8080/alfresco/api'
        assert urls['search'] == 'http://localhost:8080/alfresco/api/-default-/public/search/versions/1'
        assert urls['workflow'] == 'http://localhost:8080/alfresco/api/-default-/public/workflow/versions/1'
        assert urls['model'] == 'http://localhost:8080/alfresco/api/-default-/public/model/versions/1'
        assert urls['search-sql'] == 'http://localhost:8080/alfresco/api/-default-/public/search/versions/1'
    
    def test_client_info(self, enhanced_client):
        """Test client information retrieval."""
        info = enhanced_client.get_client_info()
        
        assert info['host'] == 'http://localhost:8080'
        assert info['username'] == 'admin'
        assert info['verify_ssl'] is True
        assert info['client_type'] == 'Enhanced Generated (OpenAPI)'
        assert 'available_apis' in info
        assert len(info['available_apis']) == 7
    
    def test_configuration_creation(self, enhanced_client):
        """Test configuration creation for APIs."""
        with patch('enhanced_generated.AlfrescoClient.AlfrescoClient.create_configuration') as mock_config:
            mock_config.return_value = Mock(
                host='http://localhost:8080/alfresco/api',
                username='admin',
                password='admin',
                verify_ssl=True
            )
            
            config = enhanced_client.create_configuration('auth')
            
            assert config is not None
            assert config.host == 'http://localhost:8080/alfresco/api'
            assert config.username == 'admin'
            assert config.password == 'admin'
    
    def test_api_client_creation(self, enhanced_client):
        """Test API client creation."""
        with patch('enhanced_generated.AlfrescoClient.AlfrescoClient.create_api_client') as mock_client:
            mock_client.return_value = Mock()
            
            client = enhanced_client.create_api_client('auth')
            
            assert client is not None
            mock_client.assert_called_once_with('auth')

class TestAlfrescoBaseClient:
    """Unit tests for the Alfresco base client."""
    
    def test_base_client_initialization(self, test_client_config):
        """Test base client initialization."""
        with patch('enhanced_generated.BaseClient.AlfrescoBaseClient._setup_paths') as mock_setup:
            from enhanced_generated import AlfrescoBaseClient
            
            client = AlfrescoBaseClient(**test_client_config)
            
            assert client.host == 'http://localhost:8080'
            assert client.username == 'admin'
            assert client.password == 'admin'
            assert client.verify_ssl is True
            
            mock_setup.assert_called_once()
    
    def test_path_setup(self):
        """Test path setup for generated clients."""
        with patch('sys.path') as mock_path:
            from enhanced_generated import AlfrescoBaseClient
            
            client = AlfrescoBaseClient()
            
            # Verify paths were added
            assert mock_path.insert.called 