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
from pathlib import Path

# Add the parent directory to the path to import our client
sys.path.insert(0, str(Path(__file__).parent.parent))

from AlfrescoClient import AlfrescoClient

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
    except Exception as e:
        print(f"   ❌ Core API error: {e}")

def demonstrate_discovery_api(client):
    """Demonstrate Discovery API operations."""
    try:
        if client.discovery:
            print("   🏢 Getting repository information...")
            info = client.discovery.get_repository_information()
            
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
            print("   🎫 Getting authentication ticket...")
            # Note: This would typically require a proper login request
            print("      Authentication API is available for ticket operations")
    except Exception as e:
        print(f"   ❌ Authentication API error: {e}")

def demonstrate_search_api(client):
    """Demonstrate Search API operations."""
    try:
        if client.search:
            print("   🔍 Search API is available for content search")
            # Note: Search operations would require proper query objects
            print("      Ready for search queries and faceted search")
    except Exception as e:
        print(f"   ❌ Search API error: {e}")

def demonstrate_workflow_api(client):
    """Demonstrate Workflow API operations."""
    try:
        if client.workflow:
            print("   ⚙️ Workflow API is available for process management")
            print("      Ready for process definitions and task operations")
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
    except Exception as e:
        print(f"   ❌ Search SQL API error: {e}")

if __name__ == "__main__":
    main() 
