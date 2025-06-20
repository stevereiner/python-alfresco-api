#!/usr/bin/env python3
"""
Alfresco Authentication API Examples

This file demonstrates how to use the Authentication API with the master client.
The Authentication API provides user authentication, ticket management, and session handling.

Current Status: ✅ Fully Working

Features:
- Create authentication tickets (login)
- Validate existing tickets
- Get current ticket information  
- Delete tickets (logout)

Requirements:
- Alfresco server running on localhost:8080
- Valid user credentials (admin/admin)
"""

import sys
import os
import base64

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'enhanced_generated'))

from AlfrescoClient import AlfrescoClient

def create_auth_ticket(client, username='admin', password='admin'):
    """
    Helper function to create authentication tickets and share them across all API clients.
    
    Args:
        client: The Alfresco client instance
        username: Username for authentication
        password: Password for authentication
        
    Returns:
        Authentication ticket response
    """
    # Fix the auth configuration if needed
    expected_url = client.get_api_url('auth')
    if client.auth_client.configuration.host != expected_url:
        print(f"🔧 Fixing auth config host from {client.auth_client.configuration.host} to {expected_url}")
        client.auth_client.configuration.host = expected_url
        client.auth_client.configuration.ignore_operation_servers = True
    
    # Use dict format that we know works
    auth_result = client.auth.create_ticket(
        ticket_body={'userId': username, 'password': password}
    )
    
    # After successful authentication, share credentials with all API clients
    share_authentication_across_clients(client)
    
    return auth_result

def share_authentication_across_clients(client):
    """
    Share authentication state from auth client to all other API clients.
    
    Args:
        client: The Alfresco client instance with authenticated auth client
    """
    if not client.auth_client:
        return
    
    # Get the auth client's configuration and headers
    auth_config = client.auth_client.configuration
    auth_headers = getattr(client.auth_client, 'default_headers', {})
    
    # List of all API clients that need authentication
    api_clients = [
        ('discovery', client.discovery_client),
        ('search', client.search_client),
        ('core', client.core_client),
        ('workflow', client.workflow_client),
        ('model', client.model_client),
        ('search_sql', client.search_sql_client),
    ]
    
    for api_name, api_client in api_clients:
        if api_client and hasattr(api_client, 'configuration'):
            # Share basic auth credentials
            api_client.configuration.username = auth_config.username
            api_client.configuration.password = auth_config.password
            
            # Copy authentication headers (including any tickets)
            if hasattr(api_client, 'default_headers') and auth_headers:
                api_client.default_headers.update(auth_headers)
                print(f"🔗 Shared auth headers with {api_name} client")
            
            # For ticket-based auth, we also need to set basic auth as fallback
            # Set authorization header directly
            auth_string = f"{auth_config.username}:{auth_config.password}"
            auth_bytes = auth_string.encode('ascii')
            auth_b64 = base64.b64encode(auth_bytes).decode('ascii')
            
            if hasattr(api_client, 'set_default_header'):
                api_client.set_default_header('Authorization', f'Basic {auth_b64}')
                print(f"🔐 Set Basic auth header for {api_name} client")
            elif hasattr(api_client, 'default_headers'):
                api_client.default_headers['Authorization'] = f'Basic {auth_b64}'
                print(f"🔐 Set Basic auth header for {api_name} client (direct)")

def fix_client_configurations(client):
    """Fix URL configurations for all API clients."""
    api_configs = [
        ('auth', client.auth_client),
        ('discovery', client.discovery_client),
        ('core', client.core_client),
        ('search', client.search_client),
        ('workflow', client.workflow_client),
        ('model', client.model_client),
        ('search_sql', client.search_sql_client),
    ]
    
    for api_name, api_client in api_configs:
        if api_client and hasattr(api_client, 'configuration'):
            expected_url = client.get_api_url(api_name)
            if api_client.configuration.host != expected_url:
                print(f"🔧 Fixing {api_name} config host from {api_client.configuration.host} to {expected_url}")
                api_client.configuration.host = expected_url
                api_client.configuration.ignore_operation_servers = True

def print_section(title):
    """Print a formatted section header."""
    print(f"\n{'='*50}")
    print(f" {title}")
    print(f"{'='*50}")


def safe_api_call(func, *args, **kwargs):
    """Safely execute an API call with error handling."""
    try:
        result = func(*args, **kwargs)
        return {'success': True, 'data': result}
    except Exception as e:
        return {'success': False, 'error': str(e)}


def main():
    """Authentication API examples."""
    print_section("Alfresco Authentication API Examples")
    
    # Initialize client
    print("🚀 Initializing Alfresco Client...")
    client = AlfrescoClient(
        host="http://localhost:8080", 
        username="admin", 
        password="admin",
        verify_ssl=False
    )
    
    if not client.auth:
        print("❌ Authentication API not available")
        return
    
    print("✅ Authentication API initialized successfully")
    
    # Fix client configurations
    print("\n🔧 Fixing client configurations...")
    fix_client_configurations(client)
    
    # Basic authentication flow
    print_section("Basic Authentication Flow")
    basic_authentication_flow(client)
    
    # Ticket management
    print_section("Ticket Management")
    ticket_management_examples(client)
    
    # Error handling
    print_section("Error Handling")
    authentication_error_handling(client)
    
    # Advanced usage
    print_section("Advanced Usage")
    advanced_authentication_examples(client)


def basic_authentication_flow(client):
    """Demonstrate basic authentication flow."""
    print("🔐 Basic Authentication Flow:")
    
    # Step 1: Create authentication ticket (login)
    print("\n1. Creating authentication ticket (login)...")
    ticket_result = safe_api_call(create_auth_ticket, client, 'admin', 'admin')
    
    if ticket_result['success']:
        print("✅ Authentication ticket created successfully")
        ticket_data = ticket_result['data']
        
        if hasattr(ticket_data, 'entry') and hasattr(ticket_data.entry, 'id'):
            ticket_id = ticket_data.entry.id
            print(f"   Ticket ID: {ticket_id}")
            
            # Step 2: Validate the ticket
            print("\n2. Validating ticket...")
            validate_result = safe_api_call(client.auth.validate_ticket)
            
            if validate_result['success']:
                print("✅ Ticket validation successful")
                validate_data = validate_result['data']
                
                if hasattr(validate_data, 'entry'):
                    user_id = getattr(validate_data.entry, 'id', 'Unknown')
                    print(f"   Authenticated user: {user_id}")
            else:
                print(f"❌ Ticket validation failed: {validate_result['error']}")
            
            # Step 3: Get ticket information
            print("\n3. Getting ticket information...")
            # Note: Some implementations may not have get_ticket method
            if hasattr(client.auth, 'get_ticket'):
                get_result = safe_api_call(client.auth.get_ticket)
                if get_result['success']:
                    print("✅ Ticket information retrieved")
                else:
                    print(f"⚠️ Get ticket failed: {get_result['error']}")
            else:
                print("⚠️ Get ticket method not available in this implementation")
                
        else:
            print("⚠️ Ticket data format unexpected")
    else:
        print(f"❌ Authentication failed: {ticket_result['error']}")


def ticket_management_examples(client):
    """Demonstrate ticket management operations."""
    print("🎫 Ticket Management Examples:")
    
    # Example 1: Multiple login attempts
    print("\n1. Testing multiple authentication attempts...")
    
    credentials_to_test = [
        {'userId': 'admin', 'password': 'admin', 'description': 'Valid admin credentials'},
        {'userId': 'admin', 'password': 'wrong', 'description': 'Invalid password'},
        {'userId': 'nonexistent', 'password': 'password', 'description': 'Non-existent user'},
    ]
    
    for cred in credentials_to_test:
        print(f"\n   Testing: {cred['description']}")
        result = safe_api_call(
            client.auth.create_ticket,
            ticket_body={'userId': cred['userId'], 'password': cred['password']}
        )
        
        if result['success']:
            print("   ✅ Authentication successful")
            # Clean up successful tickets
            try:
                client.auth.delete_ticket()
            except:
                pass
        else:
            print(f"   ❌ Authentication failed: {result['error']}")
    
    # Example 2: Ticket lifecycle
    print("\n2. Complete ticket lifecycle...")
    
    # Create ticket
    print("   Creating new ticket...")
    create_result = safe_api_call(create_auth_ticket, client, 'admin', 'admin')
    
    if create_result['success']:
        print("   ✅ Ticket created")
        
        # Validate immediately
        print("   Validating ticket...")
        validate_result = safe_api_call(client.auth.validate_ticket)
        
        if validate_result['success']:
            print("   ✅ Ticket is valid")
            
            # Delete ticket (logout)
            print("   Deleting ticket (logout)...")
            delete_result = safe_api_call(client.auth.delete_ticket)
            
            if delete_result['success']:
                print("   ✅ Ticket deleted successfully")
                
                # Try to validate deleted ticket
                print("   Trying to validate deleted ticket...")
                post_delete_validate = safe_api_call(client.auth.validate_ticket)
                
                if post_delete_validate['success']:
                    print("   ⚠️ Ticket still valid after deletion (unexpected)")
                else:
                    print("   ✅ Ticket properly invalidated")
            else:
                print(f"   ❌ Failed to delete ticket: {delete_result['error']}")
        else:
            print(f"   ❌ Ticket validation failed: {validate_result['error']}")
    else:
        print(f"   ❌ Failed to create ticket: {create_result['error']}")


def authentication_error_handling(client):
    """Demonstrate proper error handling for authentication."""
    print("🚨 Authentication Error Handling:")
    
    # Example 1: Handle invalid credentials gracefully
    print("\n1. Handling invalid credentials...")
    try:
        result = client.auth.create_ticket(
            ticket_body={'userId': 'invaliduser', 'password': 'wrongpassword'}
        )
        print("⚠️ Unexpected success with invalid credentials")
    except Exception as e:
        print(f"✅ Properly caught authentication error: {type(e).__name__}")
        print(f"   Error message: {str(e)}")
    
    # Example 2: Handle missing parameters
    print("\n2. Handling missing parameters...")
    try:
        # Try with incomplete ticket body
        result = client.auth.create_ticket(ticket_body={'userId': 'admin'})
        print("⚠️ Unexpected success with incomplete data")
    except Exception as e:
        print(f"✅ Properly caught parameter error: {type(e).__name__}")
    
    # Example 3: Handle network issues (simulated)
    print("\n3. Testing with wrong server...")
    try:
        # Create client with wrong host
        wrong_client = AlfrescoClient(
            host="http://nonexistent:8080",
            username="admin",
            password="admin"
        )
        
        if wrong_client.auth:
            result = wrong_client.auth.create_ticket(
                ticket_body={'userId': 'admin', 'password': 'admin'}
            )
        else:
            print("✅ Client properly detected unavailable server")
    except Exception as e:
        print(f"✅ Properly caught connection error: {type(e).__name__}")


def advanced_authentication_examples(client):
    """Advanced authentication usage patterns."""
    print("🎯 Advanced Authentication Patterns:")
    
    # Example 1: Authentication status checking
    print("\n1. Authentication status checking...")
    
    def check_authentication_status(client):
        """Check if user is currently authenticated."""
        if not client.auth:
            return {'authenticated': False, 'reason': 'Auth API not available'}
        
        validate_result = safe_api_call(client.auth.validate_ticket)
        return {
            'authenticated': validate_result['success'],
            'reason': validate_result.get('error', 'Valid ticket') if not validate_result['success'] else 'Valid ticket'
        }
    
    status = check_authentication_status(client)
    print(f"   Authenticated: {status['authenticated']}")
    print(f"   Reason: {status['reason']}")
    
    # Example 2: Session management pattern
    print("\n2. Session management pattern...")
    
    class AuthSession:
        """Simple session management class."""
        
        def __init__(self, client):
            self.client = client
            self.authenticated = False
            self.ticket_id = None
            
        def login(self, username, password):
            """Login and establish session."""
            if not self.client.auth:
                return {'success': False, 'error': 'Auth API not available'}
            
            result = safe_api_call(
                self.client.auth.create_ticket,
                ticket_body={'userId': username, 'password': password}
            )
            
            if result['success']:
                self.authenticated = True
                ticket_data = result['data']
                if hasattr(ticket_data, 'entry') and hasattr(ticket_data.entry, 'id'):
                    self.ticket_id = ticket_data.entry.id
                return {'success': True, 'ticket_id': self.ticket_id}
            else:
                return result
        
        def logout(self):
            """Logout and clear session."""
            if self.authenticated and self.client.auth:
                result = safe_api_call(self.client.auth.delete_ticket)
                self.authenticated = False
                self.ticket_id = None
                return result
            return {'success': True, 'message': 'Not authenticated'}
        
        def is_authenticated(self):
            """Check if session is authenticated."""
            if not self.authenticated or not self.client.auth:
                return False
            
            result = safe_api_call(self.client.auth.validate_ticket)
            if not result['success']:
                self.authenticated = False
                self.ticket_id = None
            
            return result['success']
    
    # Demonstrate session management
    session = AuthSession(client)
    
    print("   Creating session and logging in...")
    login_result = session.login('admin', 'admin')
    if login_result['success']:
        print(f"   ✅ Session established: {login_result.get('ticket_id', 'Unknown')}")
        
        print("   Checking authentication status...")
        if session.is_authenticated():
            print("   ✅ Session is authenticated")
        else:
            print("   ❌ Session not authenticated")
        
        print("   Logging out...")
        logout_result = session.logout()
        if logout_result['success']:
            print("   ✅ Session ended")
        else:
            print(f"   ❌ Logout failed: {logout_result['error']}")
    else:
        print(f"   ❌ Failed to establish session: {login_result['error']}")
    
    # Example 3: Best practices
    print("\n3. Authentication best practices:")
    print("   ✅ Always validate tickets before important operations")
    print("   ✅ Handle authentication errors gracefully")
    print("   ✅ Implement proper session management")
    print("   ✅ Log out properly to clean up resources")
    print("   ✅ Use secure credential storage (environment variables)")
    print("   ✅ Implement retry logic for network issues")


def demonstrate_real_world_usage():
    """Show real-world authentication patterns."""
    print_section("Real-World Authentication Patterns")
    
    print("🌍 Real-world authentication scenarios:")
    
    # Scenario 1: Web application login
    print("\n1. Web application login flow:")
    print("   - User submits login form")
    print("   - Create authentication ticket")
    print("   - Store ticket ID in session")
    print("   - Validate ticket on each request")
    print("   - Handle token expiration")
    
    # Scenario 2: API client authentication
    print("\n2. API client authentication:")
    print("   - Authenticate once at startup")
    print("   - Reuse ticket for multiple operations")
    print("   - Refresh ticket when needed")
    print("   - Clean logout on shutdown")
    
    # Scenario 3: Batch processing
    print("\n3. Batch processing authentication:")
    print("   - Authenticate before batch starts")
    print("   - Validate ticket periodically")
    print("   - Handle authentication failures")
    print("   - Clean up on completion")
    
    # Example implementation
    print("\n4. Example implementation:")
    client = AlfrescoClient(
        host="http://localhost:8080",
        username="admin",
        password="admin"
    )
    
    if client.auth:
        # Simple batch operation pattern
        print("   Implementing batch operation with authentication...")
        
        # Authenticate
        auth_result = safe_api_call(
            client.auth.create_ticket,
            ticket_body={'userId': 'admin', 'password': 'admin'}
        )
        
        if auth_result['success']:
            print("   ✅ Authenticated for batch operation")
            
            # Simulate batch operations
            for i in range(3):
                print(f"   Processing item {i+1}...")
                
                # Validate ticket before each operation
                if safe_api_call(client.auth.validate_ticket)['success']:
                    print(f"   ✅ Item {i+1} processed")
                else:
                    print(f"   ❌ Authentication lost at item {i+1}")
                    break
            
            # Cleanup
            clean_result = safe_api_call(client.auth.delete_ticket)
            if clean_result['success']:
                print("   ✅ Batch operation completed, cleaned up")
        else:
            print("   ❌ Failed to authenticate for batch operation")


if __name__ == "__main__":
    main()
    demonstrate_real_world_usage() 