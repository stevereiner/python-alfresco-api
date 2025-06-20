"""
Test Authentication Strategies for Alfresco APIs

This module tests different authentication methods to help understand and debug
401 authentication errors that can occur with different Alfresco API endpoints.

Based on research, Alfresco supports multiple authentication methods:
1. Basic Authentication (username/password)
2. Ticket-based Authentication 
3. Different URL endpoints that may have different auth requirements

Common 401 causes:
- Invalid credentials
- Expired tickets
- Wrong authentication method for specific endpoint
- Missing authentication headers
- Server configuration issues
"""

import pytest
import base64
import json
from unittest.mock import Mock, patch, MagicMock
import urllib3


class TestAuthenticationStrategies:
    """Test different authentication strategies for Alfresco APIs."""
    
    @pytest.fixture
    def mock_server_config(self):
        """Mock server configuration."""
        return {
            'server_url': 'http://localhost:8080',
            'username': 'admin',
            'password': 'admin'
        }
    
    def test_basic_auth_header_creation(self, mock_server_config):
        """Test creation of Basic Authentication headers."""
        username = mock_server_config['username']
        password = mock_server_config['password']
        
        # Create basic auth header
        credentials = f"{username}:{password}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()
        auth_header = f"Basic {encoded_credentials}"
        
        assert auth_header.startswith("Basic ")
        assert len(encoded_credentials) > 0
        print(f"✅ Basic Auth header created: {auth_header[:20]}...")
    
    def test_ticket_based_auth_header(self):
        """Test creation of ticket-based authentication headers."""
        # Simulate a ticket from Alfresco
        mock_ticket = "TICKET_12345abcdef67890"
        encoded_ticket = base64.b64encode(mock_ticket.encode()).decode()
        ticket_auth_header = f"Basic {encoded_ticket}"
        
        assert ticket_auth_header.startswith("Basic ")
        print(f"✅ Ticket Auth header created: {ticket_auth_header[:20]}...")
    
    @patch('urllib3.PoolManager')
    def test_authentication_endpoint_simulation(self, mock_pool_manager, mock_server_config):
        """Test simulated authentication to get a ticket."""
        # Mock the HTTP response for authentication
        mock_response = Mock()
        mock_response.status = 200
        mock_response.data = json.dumps({
            "entry": {
                "id": "TICKET_12345abcdef67890",
                "userId": "admin"
            }
        }).encode()
        
        mock_http = Mock()
        mock_http.request.return_value = mock_response
        mock_pool_manager.return_value = mock_http
        
        # Simulate authentication request
        auth_url = f"{mock_server_config['server_url']}/alfresco/api/-default-/public/authentication/versions/1/tickets"
        auth_data = {
            "userId": mock_server_config['username'],
            "password": mock_server_config['password']
        }
        
        http = urllib3.PoolManager()
        response = http.request(
            'POST',
            auth_url,
            body=json.dumps(auth_data),
            headers={'Content-Type': 'application/json'}
        )
        
        assert response.status == 200
        response_data = json.loads(response.data.decode())
        ticket = response_data['entry']['id']
        assert ticket.startswith('TICKET_')
        print(f"✅ Authentication simulation successful, ticket: {ticket[:15]}...")
    
    def test_different_api_endpoints_auth_requirements(self, mock_server_config):
        """Test understanding of different API endpoints and their auth requirements."""
        base_url = mock_server_config['server_url']
        
        # Different API endpoints that may have different auth requirements
        endpoints = {
            'discovery': f"{base_url}/alfresco/api/discovery",
            'auth_tickets': f"{base_url}/alfresco/api/-default-/public/authentication/versions/1/tickets",
            'core_nodes': f"{base_url}/alfresco/api/-default-/public/alfresco/versions/1/nodes",
            'search': f"{base_url}/alfresco/api/-default-/public/search/versions/1/search",
            'sites': f"{base_url}/alfresco/api/-default-/public/alfresco/versions/1/sites"
        }
        
        # Discovery API may not require authentication
        assert 'discovery' in endpoints
        
        # Authentication endpoint obviously needs to be accessible without prior auth
        assert 'auth_tickets' in endpoints
        
        # Core APIs typically require authentication
        assert 'core_nodes' in endpoints
        assert 'search' in endpoints
        assert 'sites' in endpoints
        
        print("✅ API endpoint mapping understood")
        for name, url in endpoints.items():
            print(f"   {name}: {url}")
    
    def test_common_401_error_scenarios(self):
        """Test scenarios that commonly cause 401 errors."""
        scenarios = [
            {
                'name': 'Invalid username/password',
                'cause': 'Wrong credentials provided',
                'solution': 'Verify username and password are correct'
            },
            {
                'name': 'Expired ticket',
                'cause': 'Ticket has exceeded its lifetime',
                'solution': 'Reauthenticate to get a new ticket'
            },
            {
                'name': 'Missing Authorization header',
                'cause': 'No authentication header sent with request',
                'solution': 'Include proper Authorization header'
            },
            {
                'name': 'Wrong auth method for endpoint',
                'cause': 'Using ticket auth on endpoint that requires basic auth',
                'solution': 'Use appropriate auth method for specific endpoint'
            },
            {
                'name': 'Server configuration',
                'cause': 'Alfresco server auth configuration issues',
                'solution': 'Check server logs and authentication subsystem config'
            }
        ]
        
        assert len(scenarios) == 5
        print("✅ Common 401 error scenarios identified:")
        for scenario in scenarios:
            print(f"   • {scenario['name']}: {scenario['cause']}")
            print(f"     Solution: {scenario['solution']}")
    
    @patch('urllib3.PoolManager')
    def test_discovery_api_no_auth_requirement(self, mock_pool_manager, mock_server_config):
        """Test that Discovery API may not require authentication."""
        # Mock response for discovery API
        mock_response = Mock()
        mock_response.status = 200
        mock_response.data = json.dumps({
            "entry": {
                "repository": {
                    "edition": "Community",
                    "version": {
                        "major": "7",
                        "minor": "0",
                        "patch": "0"
                    }
                }
            }
        }).encode()
        
        mock_http = Mock()
        mock_http.request.return_value = mock_response
        mock_pool_manager.return_value = mock_http
        
        # Make request to discovery API without authentication
        discovery_url = f"{mock_server_config['server_url']}/alfresco/api/discovery"
        
        http = urllib3.PoolManager()
        response = http.request('GET', discovery_url)
        
        assert response.status == 200
        print("✅ Discovery API accessible without authentication")
    
    def test_auth_header_formats(self):
        """Test different authentication header formats."""
        
        # Basic Auth with username:password
        basic_creds = base64.b64encode(b"admin:admin").decode()
        basic_header = f"Basic {basic_creds}"
        
        # Basic Auth with ticket
        ticket = "TICKET_12345abcdef67890"
        ticket_encoded = base64.b64encode(ticket.encode()).decode()
        ticket_header = f"Basic {ticket_encoded}"
        
        # Verify formats
        assert basic_header.startswith("Basic ")
        assert ticket_header.startswith("Basic ")
        assert basic_creds != ticket_encoded
        
        print("✅ Different auth header formats tested:")
        print(f"   Basic Auth: {basic_header[:30]}...")
        print(f"   Ticket Auth: {ticket_header[:30]}...")
    
    def test_auth_debugging_checklist(self):
        """Provide a debugging checklist for 401 errors."""
        checklist = [
            "✓ Verify server is running and accessible",
            "✓ Check username and password are correct",
            "✓ Ensure proper Content-Type header for auth requests",
            "✓ Verify Authorization header format",
            "✓ Check if ticket has expired",
            "✓ Test with Discovery API first (may not need auth)",
            "✓ Check server logs for authentication errors",
            "✓ Verify Alfresco authentication subsystem configuration",
            "✓ Test with curl command line tool first",
            "✓ Check for any firewall or proxy issues"
        ]
        
        assert len(checklist) >= 10
        print("✅ 401 Error Debugging Checklist:")
        for item in checklist:
            print(f"   {item}")
    
    @pytest.mark.parametrize("endpoint_type,auth_required", [
        ("discovery", False),
        ("authentication", False),  # To get tickets
        ("nodes", True),
        ("sites", True),
        ("search", True),
        ("people", True),
        ("groups", True)
    ])
    def test_endpoint_auth_requirements(self, endpoint_type, auth_required):
        """Test understanding of which endpoints require authentication."""
        if auth_required:
            print(f"✅ {endpoint_type} API requires authentication")
        else:
            print(f"✅ {endpoint_type} API may not require authentication")
        
        # This helps document which APIs need auth
        assert isinstance(auth_required, bool)
    
    def test_create_comprehensive_auth_example(self, mock_server_config):
        """Create a comprehensive example of proper authentication flow."""
        
        example_flow = [
            {
                'step': 1,
                'action': 'Test connectivity',
                'url': f"{mock_server_config['server_url']}/alfresco/api/discovery",
                'method': 'GET',
                'auth': None,
                'expected': '200 OK - Repository info'
            },
            {
                'step': 2,
                'action': 'Authenticate and get ticket',
                'url': f"{mock_server_config['server_url']}/alfresco/api/-default-/public/authentication/versions/1/tickets",
                'method': 'POST',
                'auth': None,
                'body': {'userId': 'admin', 'password': 'admin'},
                'expected': '201 Created - Ticket returned'
            },
            {
                'step': 3,
                'action': 'Use ticket for authenticated request',
                'url': f"{mock_server_config['server_url']}/alfresco/api/-default-/public/alfresco/versions/1/sites",
                'method': 'GET',
                'auth': 'Basic <base64-encoded-ticket>',
                'expected': '200 OK - Sites list'
            }
        ]
        
        assert len(example_flow) == 3
        print("✅ Comprehensive Authentication Flow Example:")
        for step in example_flow:
            print(f"   Step {step['step']}: {step['action']}")
            print(f"      {step['method']} {step['url']}")
            if step.get('auth'):
                print(f"      Auth: {step['auth']}")
            if step.get('body'):
                print(f"      Body: {step['body']}")
            print(f"      Expected: {step['expected']}")
            print()


if __name__ == "__main__":
    # If run directly, execute some basic authentication tests
    print("=== Alfresco Authentication Strategy Tests ===")
    
    test_instance = TestAuthenticationStrategies()
    
    # Run some basic tests
    test_instance.test_basic_auth_header_creation({'username': 'admin', 'password': 'admin'})
    test_instance.test_ticket_based_auth_header()
    test_instance.test_common_401_error_scenarios()
    test_instance.test_auth_debugging_checklist()
    
    print("\n=== Authentication Testing Complete ===") 