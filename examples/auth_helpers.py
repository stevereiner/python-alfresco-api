"""
Authentication Helper Functions for Alfresco Examples

This module contains shared authentication and configuration functions
that are used across all example files. These functions are based on
the working patterns from the integration tests.

Author: Alfresco Python Client
"""

import base64

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
    """
    Fix URL configurations for all API clients.
    
    This function corrects the host URLs for each API client to use the proper
    versioned endpoints that Alfresco expects.
    
    Args:
        client: The Alfresco client instance
    """
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

def setup_authentication(client, username='admin', password='admin', verbose=True):
    """
    Complete authentication setup for an Alfresco client.
    
    This function:
    1. Fixes client configurations
    2. Creates authentication ticket
    3. Shares authentication across all clients
    
    Args:
        client: The Alfresco client instance
        username: Username for authentication
        password: Password for authentication
        verbose: Whether to print status messages
        
    Returns:
        dict: Result with success status and any error messages
    """
    try:
        # Step 1: Fix client configurations
        if verbose:
            print("🔧 Fixing client configurations...")
        fix_client_configurations(client)
        
        # Step 2: Set up authentication
        if verbose:
            print("🔐 Setting up authentication...")
        auth_result = create_auth_ticket(client, username, password)
        
        if verbose:
            print("✅ Authentication configured successfully")
            
        return {
            'success': True,
            'auth_result': auth_result,
            'message': 'Authentication setup completed successfully'
        }
        
    except Exception as e:
        error_msg = f"Authentication setup failed: {e}"
        if verbose:
            print(f"⚠️ {error_msg}")
            print("   Continuing with basic auth fallback...")
        
        return {
            'success': False,
            'error': str(e),
            'message': error_msg
        }

def safe_api_call(func, *args, **kwargs):
    """
    Safely execute an API call with error handling.
    
    Args:
        func: The API function to call
        *args: Positional arguments for the function
        **kwargs: Keyword arguments for the function
        
    Returns:
        dict: Result with success status and data or error
    """
    try:
        result = func(*args, **kwargs)
        return {'success': True, 'data': result}
    except Exception as e:
        return {'success': False, 'error': str(e)}

def cleanup_auth_ticket(client):
    """
    Helper function to safely delete auth ticket, ignoring cleanup errors.
    
    Args:
        client: The Alfresco client instance
    """
    try:
        client.auth.delete_ticket()
    except Exception:
        pass  # Ignore cleanup errors - ticket may already be invalid 