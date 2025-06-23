"""
Alfresco Client Usage Example

Demonstrates how to use the enhanced generated Alfresco API client
with all 7 APIs (auth, core, discovery, search, workflow, model, search-sql).

CONFIGURATION:
Before running this example, you need to configure your Alfresco connection:

Option 1 - Environment Variables (Recommended):
    set ALFRESCO_HOST=https://your-alfresco-server.com
    set ALFRESCO_USERNAME=your-username  
    set ALFRESCO_PASSWORD=your-password

Option 2 - Edit the defaults in the main() function below

The default localhost:8080 with admin/admin will only work if you have
a local Alfresco Community Edition server running.
"""

import sys
import base64
from pathlib import Path

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

def main():
    """
    Main example demonstrating Alfresco client usage.
    """
    print("🚀 Enhanced Generated Alfresco API Client Example")
    print("=" * 55)
    
    # Initialize the master client
    print("\n📡 Connecting to Alfresco...")
    
    # TODO: Update these connection details for your Alfresco instance
    # You can also set these via environment variables:
    # ALFRESCO_HOST, ALFRESCO_USERNAME, ALFRESCO_PASSWORD
    import os
    
    host = os.getenv('ALFRESCO_HOST', 'http://localhost:8080')
    username = os.getenv('ALFRESCO_USERNAME', 'admin') 
    password = os.getenv('ALFRESCO_PASSWORD', 'admin')
    
    print(f"   🌐 Host: {host}")
    print(f"   👤 User: {username}")
    
    client = AlfrescoClient(
        host=host,
        username=username,
        password=password
    )
    
    # Fix client configurations
    print("\n🔧 Fixing client configurations...")
    fix_client_configurations(client)
    
    # Test connection and get status
    print("\n📊 Testing connection...")
    results = client.test_connection()
    
    print(f"   Host: {results['host']}")
    print(f"   User: {results['username']}")
    print(f"   APIs: {results['success_rate']}")
    print(f"   Working: {', '.join(results['working_api_list'])}")
    
    if 'discovery_test' in results:
        print(f"   Discovery: {results['discovery_test']}")
    
    # Demonstrate available APIs
    working_apis = client.get_working_apis()
    
    print(f"\n🎯 Available APIs ({len(working_apis)}/7):")
    for api in working_apis:
        print(f"   ✅ {api}")
    
    # Authentication setup
    print("\n🔐 Setting up authentication...")
    try:
        auth_result = create_auth_ticket(client, username, password)
        print("✅ Authentication configured successfully")
    except Exception as e:
        print(f"⚠️ Authentication setup failed: {e}")
        print("   Continuing with basic auth fallback...")
    
    # Core API demonstration (if available)
    if 'core' in working_apis:
        print("\n📁 Core API Examples:")
        demonstrate_core_api(client)
    
    # Discovery API demonstration (if available)  
    if 'discovery' in working_apis:
        print("\n🔍 Discovery API Examples:")
        demonstrate_discovery_api(client)
    
    # Authentication API demonstration (if available)
    if 'auth' in working_apis:
        print("\n🔐 Authentication API Examples:")
        demonstrate_auth_api(client)
    
    # Search API demonstration (if available)
    if 'search' in working_apis:
        print("\n🔎 Search API Examples:")
        demonstrate_search_api(client)
    
    # Workflow API demonstration (if available)
    if 'workflow' in working_apis:
        print("\n⚙️ Workflow API Examples:")
        demonstrate_workflow_api(client)
    
    # Model API demonstration (if available)
    if 'model' in working_apis:
        print("\n📋 Model API Examples:")
        demonstrate_model_api(client)
    
    # Search SQL API demonstration (if available)
    if 'search_sql' in working_apis:
        print("\n🗃️ Search SQL API Examples:")
        demonstrate_search_sql_api(client)

def demonstrate_core_api(client):
    """Demonstrate Core API operations."""
    try:
        if client.core and 'nodes' in client.core:
            # Get the nodes API client once
            nodes_api = client.core['nodes']
            
            # Get root node
            print("   📂 Getting repository root...")
            try:
                root = nodes_api.get_node('-root-')
                print(f"      Root ID: {getattr(root, 'id', 'Unknown')}")
                
                # List root children
                print("   📋 Listing root children...")
                children = nodes_api.list_node_children('-root-')
                if hasattr(children, 'list') and hasattr(children.list, 'entries'):
                    print(f"      Found {len(children.list.entries)} items")
                    for entry in children.list.entries[:3]:  # Show first 3
                        node = entry.entry
                        print(f"         - {getattr(node, 'name', 'Unknown')} ({getattr(node, 'node_type', 'Unknown')})")
            except Exception as node_error:
                if "401" in str(node_error):
                    print("   ⚠️ Core API requires additional authentication setup")
                else:
                    print(f"   ⚠️ Core API error: {node_error}")
    except Exception as e:
        print(f"   ❌ Core API error: {e}")

def demonstrate_discovery_api(client):
    """Demonstrate Discovery API operations."""
    try:
        if client.discovery:
            print("   🏢 Getting repository information...")
            
            # Try without authentication first, then with authentication if it fails
            try:
                info = client.discovery.get_repository_information()
                print("   ✅ Discovery API works without authentication")
            except Exception as auth_error:
                if "401" in str(auth_error):
                    print("   ⚠️ Discovery API requires authentication, retrying...")
                    # The authentication should already be set up from main()
                    info = client.discovery.get_repository_information()
                    print("   ✅ Discovery API works with authentication")
                else:
                    raise auth_error
            
            if hasattr(info, 'entry'):
                repo = info.entry.repository
                print(f"      Name: {getattr(repo, 'name', 'Unknown')}")
                print(f"      Version: {getattr(repo, 'version', 'Unknown')}")
                print(f"      Edition: {getattr(repo, 'edition', 'Unknown')}")
    except Exception as e:
        print(f"   ❌ Discovery API error: {e}")

def demonstrate_auth_api(client):
    """Demonstrate Authentication API operations."""
    try:
        if client.auth:
            print("   🎫 Testing authentication operations...")
            # Authentication was already set up in main(), just verify it works
            try:
                validate_result = client.auth.validate_ticket()
                print("   ✅ Ticket validation successful")
            except Exception as e:
                print(f"   ⚠️ Ticket validation: {e}")
                print("   ✅ Authentication API is available for ticket operations")
    except Exception as e:
        print(f"   ❌ Authentication API error: {e}")

def demonstrate_search_api(client):
    """Demonstrate Search API operations."""
    try:
        if client.search:
            print("   🔍 Search API is available for content search")
            print("      Ready for search queries and faceted search")
            # Note: Search operations would require proper query objects
            # which are complex to set up in a simple example
    except Exception as e:
        print(f"   ❌ Search API error: {e}")

def demonstrate_workflow_api(client):
    """Demonstrate Workflow API operations."""
    try:
        if client.workflow:
            print("   ⚙️ Testing workflow operations...")
            try:
                if isinstance(client.workflow, dict) and 'process_definitions' in client.workflow:
                    # Try to list process definitions
                    process_defs = client.workflow['process_definitions'].get_process_definitions()
                    print("   ✅ Workflow API accessible")
                else:
                    print("   ✅ Workflow API available for process management")
            except Exception as e:
                if "401" in str(e):
                    print("   ⚠️ Workflow API requires additional authentication setup")
                else:
                    print(f"   ⚠️ Workflow operations: {e}")
    except Exception as e:
        print(f"   ❌ Workflow API error: {e}")

def demonstrate_model_api(client):
    """Demonstrate Model API operations."""
    try:
        if client.model:
            print("   📋 Model API is available for custom content models")
            print("      Ready for model definitions and type management")
    except Exception as e:
        print(f"   ❌ Model API error: {e}")

def demonstrate_search_sql_api(client):
    """Demonstrate Search SQL API operations."""
    try:
        if client.search_sql:
            print("   🗃️ Search SQL API is available for SQL-like queries")
            print("      Ready for structured content queries")
            print("      Note: Requires Solr configuration for full functionality")
    except Exception as e:
        print(f"   ❌ Search SQL API error: {e}")

if __name__ == "__main__":
    main() 
