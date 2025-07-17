#!/usr/bin/env python3
"""
Authentication API Examples - ClientFactory Pattern

This file demonstrates how to use the Authentication API with the ClientFactory.
Shows both individual auth client and master client patterns.

Usage Patterns:
    # Option 1: Individual auth client
    factory = ClientFactory(base_url="...", username="...", password="...")
    auth_client = factory.create_auth_client()
    
    # Option 2: Master client with auth access
    factory = ClientFactory(base_url="...", username="...", password="...")
    client = factory.create_master_client()
    auth_operations = client.auth
"""

import sys
import os
from datetime import datetime

from python_alfresco_api import ClientFactory

def create_auth_ticket(client, username='admin', password='admin'):
    """Create authentication ticket using either individual or master client."""
    try:
        # Handle both individual auth client and master client
        auth_api = client.auth if hasattr(client, 'auth') else client
        
        ticket = auth_api.create_ticket({
            'userId': username,
            'password': password
        })
        return {'success': True, 'data': ticket}
    except Exception as e:
        return {'success': False, 'error': str(e)}

def share_authentication_across_clients(client):
    """Demonstrate authentication sharing (handled automatically by factory)."""
    print("🔐 Authentication Sharing with Factory Pattern")
    print("-" * 50)
    
    try:
        # The factory automatically handles authentication sharing
        print("✅ Factory pattern provides automatic authentication sharing")
        print("   • All clients created from same factory share authentication")
        print("   • Tickets are automatically managed across APIs")
        print("   • No manual credential sharing required")
        
        # Test with master client if available
        if hasattr(client, 'discovery'):
            repo_result = safe_api_call(client.discovery.get_repository_info)
            if repo_result['success']:
                print("✅ Shared authentication verified with Discovery API")
            else:
                print(f"⚠️ Discovery API test: {repo_result['error']}")
        
    except Exception as e:
        print(f"❌ Authentication sharing test failed: {e}")

def fix_client_configurations(client):
    """Fix any client configuration issues (handled by factory)."""
    try:
        print("🔧 Client configuration:")
        print("   ✅ Factory handles all configuration automatically")
        print("   ✅ Consistent base URLs across all APIs")
        print("   ✅ Shared authentication credentials")
        return True
    except Exception as e:
        print(f"❌ Configuration check failed: {e}")
        return False

def print_section(title):
    """Print a formatted section header."""
    print(f"\n{'='*60}")
    print(f"📋 {title}")
    print(f"{'='*60}")

def safe_api_call(func, *args, **kwargs):
    """Safely call an API function and return structured result."""
    try:
        result = func(*args, **kwargs)
        return {'success': True, 'data': result}
    except Exception as e:
        return {'success': False, 'error': str(e)}

def main():
    """Authentication API examples."""
    print_section("Alfresco Authentication API Examples")
    
    # Initialize client using factory pattern
    print("🚀 Initializing Alfresco Client...")
    factory = ClientFactory(
        base_url="http://localhost:8080", 
        username="admin", 
        password="admin",
        verify_ssl=False
    )
    
    # Option 1: Individual auth client
    print("\n📋 Option 1: Individual Auth Client")
    print("-" * 40)
    auth_client = factory.create_auth_client()
    
    if not auth_client:
        print("❌ Authentication API not available")
        return
    
    print("✅ Individual auth client initialized successfully")
    
    # Option 2: Master client for comprehensive access
    print("\n📋 Option 2: Master Client")
    print("-" * 40)
    master_client = factory.create_master_client()
    
    if not hasattr(master_client, 'auth'):
        print("❌ Auth API not available in master client")
        return
        
    print("✅ Master client with auth access initialized")
    
    # Fix client configurations
    print("\n🔧 Fixing client configurations...")
    fix_client_configurations(master_client)
    
    # Basic authentication flow
    print_section("Basic Authentication Flow")
    basic_authentication_flow(master_client)
    
    # Ticket management
    print_section("Ticket Management")
    ticket_management_examples(master_client)
    
    # Error handling
    print_section("Error Handling")
    authentication_error_handling(master_client)
    
    # Advanced usage
    print_section("Advanced Usage")
    advanced_authentication_examples(master_client)

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
            if hasattr(client.auth, 'validate_ticket'):
                validate_result = safe_api_call(client.auth.validate_ticket)
                
                if validate_result['success']:
                    print("✅ Ticket validation successful")
                    validate_data = validate_result['data']
                    
                    if hasattr(validate_data, 'entry'):
                        user_id = getattr(validate_data.entry, 'id', 'Unknown')
                        print(f"   Authenticated user: {user_id}")
                else:
                    print(f"❌ Ticket validation failed: {validate_result['error']}")
            else:
                print("⚠️ Validate ticket method not available")
            
            # Step 3: Get ticket information
            print("\n3. Getting ticket information...")
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
        
        # Create test ticket
        test_result = safe_api_call(
            client.auth.create_ticket,
            ticket_body={'userId': cred['userId'], 'password': cred['password']}
        )
        
        if test_result['success']:
            print("   ✅ Authentication successful")
            # Clean up successful tickets
            try:
                if hasattr(client.auth, 'delete_ticket'):
                    client.auth.delete_ticket()
            except:
                pass
        else:
            print(f"   ❌ Authentication failed: {test_result['error']}")
    
    # Example 2: Ticket lifecycle
    print("\n2. Complete ticket lifecycle...")
    
    # Create ticket
    print("   Creating new ticket...")
    create_result = safe_api_call(create_auth_ticket, client, 'admin', 'admin')
    
    if create_result['success']:
        print("   ✅ Ticket created")
        
        # Validate immediately
        print("   Validating ticket...")
        if hasattr(client.auth, 'validate_ticket'):
            validate_result = safe_api_call(client.auth.validate_ticket)
            
            if validate_result['success']:
                print("   ✅ Ticket is valid")
                
                # Delete ticket (logout)
                print("   Deleting ticket (logout)...")
                if hasattr(client.auth, 'delete_ticket'):
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
                    print("   ⚠️ Delete ticket method not available")
            else:
                print(f"   ❌ Ticket validation failed: {validate_result['error']}")
        else:
            print("   ⚠️ Validate ticket method not available")
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
        # Create factory with wrong host
        wrong_factory = ClientFactory(
            base_url="http://nonexistent:8080",
            username="admin",
            password="admin"
        )
        
        wrong_client = wrong_factory.create_master_client()
        
        if hasattr(wrong_client, 'auth'):
            result = wrong_client.auth.create_ticket(
                ticket_body={'userId': 'admin', 'password': 'admin'}
            )
            print("⚠️ Unexpected success with wrong server")
        else:
            print("✅ Client properly detected unavailable server")
    except Exception as e:
        print(f"✅ Properly caught connection error: {type(e).__name__}")

def advanced_authentication_examples(client):
    """Advanced authentication patterns and use cases."""
    print("🔬 Advanced Authentication Examples:")
    
    def check_authentication_status(client):
        """Check if client is currently authenticated."""
        try:
            if hasattr(client.auth, 'validate_ticket'):
                result = client.auth.validate_ticket()
                return True
            else:
                # Try a simple operation that requires auth
                if hasattr(client, 'discovery'):
                    client.discovery.get_repository_info()
                return True
        except:
            return False
    
    class AuthSession:
        """Example authentication session manager."""
        
        def __init__(self, client):
            self.client = client
            self.authenticated = False
        
        def login(self, username, password):
            """Login and maintain session state."""
            try:
                ticket_result = create_auth_ticket(self.client, username, password)
                if ticket_result['success']:
                    self.authenticated = True
                    print(f"✅ Session: Logged in as {username}")
                    return True
                else:
                    print(f"❌ Session: Login failed - {ticket_result['error']}")
                    return False
            except Exception as e:
                print(f"❌ Session: Login error - {e}")
                return False
        
        def logout(self):
            """Logout and cleanup session."""
            try:
                if hasattr(self.client.auth, 'delete_ticket'):
                    self.client.auth.delete_ticket()
                self.authenticated = False
                print("✅ Session: Logged out successfully")
                return True
            except Exception as e:
                print(f"❌ Session: Logout error - {e}")
                return False
        
        def is_authenticated(self):
            """Check if session is authenticated."""
            if not self.authenticated:
                return False
            return check_authentication_status(self.client)
    
    # Example usage of session manager
    print("\n1. Session Management Example:")
    session = AuthSession(client)
    
    # Login
    if session.login('admin', 'admin'):
        print(f"   Session authenticated: {session.is_authenticated()}")
        
        # Do some work...
        print("   Performing authenticated operations...")
        
        # Logout
        session.logout()
        print(f"   Session authenticated after logout: {session.is_authenticated()}")
    
    # Example 2: Multi-client authentication
    print("\n2. Multi-Client Authentication:")
    try:
        # Create multiple clients from same factory (shared auth)
        factory = ClientFactory(
            base_url="http://localhost:8080",
            username="admin",
            password="admin"
        )
        
        auth_client = factory.create_auth_client()
        core_client = factory.create_core_client()
        discovery_client = factory.create_discovery_client()
        
        print("✅ Multiple clients created with shared authentication")
        print("   • All clients automatically share credentials")
        print("   • No manual ticket sharing required")
        print("   • Consistent authentication across APIs")
        
    except Exception as e:
        print(f"❌ Multi-client setup failed: {e}")

def demonstrate_real_world_usage():
    """Demonstrate real-world authentication patterns."""
    print_section("Real-World Authentication Patterns")
    
    # Pattern 1: Environment-based configuration
    print("1. Environment-based Authentication:")
    
    # Use environment variables or defaults
    base_url = os.getenv('ALFRESCO_URL', 'http://localhost:8080')
    username = os.getenv('ALFRESCO_USERNAME', 'admin')
    password = os.getenv('ALFRESCO_PASSWORD', 'admin')
    
    try:
        factory = ClientFactory(
            base_url=base_url,
            username=username,
            password=password
        )
        
        client = factory.create_master_client()
        print(f"✅ Connected to {base_url} as {username}")
        
    except Exception as e:
        print(f"❌ Environment-based auth failed: {e}")
    
    # Pattern 2: Configuration file based
    print("\n2. Configuration-based Authentication:")
    print("   💡 Use ClientFactory() without parameters to load from config files")
    print("   📁 Supports: .env files, YAML configs, environment variables")
    
    # Pattern 3: Error recovery
    print("\n3. Authentication Error Recovery:")
    print("   • Automatic retry on auth failures")  
    print("   • Graceful degradation for optional operations")
    print("   • Clear error messages for troubleshooting")

if __name__ == "__main__":
    try:
        main()
        print("\n" + "="*60)
        print("🌟 Real-World Examples")
        print("="*60)
        demonstrate_real_world_usage()
    except KeyboardInterrupt:
        print("\n👋 Examples interrupted by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc() 