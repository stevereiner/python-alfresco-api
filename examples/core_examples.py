#!/usr/bin/env python3
"""
Alfresco Core API Examples

This file demonstrates how to use the Core API with the master client.
The Core API provides access to nodes, sites, people, groups, and actions.

Current Status:
- Actions API: ✅ Working
- Nodes API: ✅ Working (see examples/alfresco_client_usage.py)
- Sites API: ✅ Available
- People API: ✅ Available
- Groups API: ✅ Available

Requirements:
- Alfresco server running on localhost:8080
- Admin credentials (admin/admin)

Note: For the latest working examples, see examples/alfresco_client_usage.py
which demonstrates all APIs including the improved Core API functionality.
"""

import sys
import os

from AlfrescoClient import AlfrescoClient

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
    """Core API examples."""
    print_section("Alfresco Core API Examples")
    
    # Initialize client
    print("🚀 Initializing Alfresco Client...")
    client = AlfrescoClient(
        host="http://localhost:8080", 
        username="admin", 
        password="admin",
        verify_ssl=False
    )
    
    if not client.core:
        print("❌ Core API not available")
        return
    
    print("✅ Core API initialized successfully")
    
    # Show API structure
    print_section("Core API Structure")
    show_api_structure(client)
    
    # Test Actions API (currently working)
    print_section("Actions API Examples")
    test_actions_api(client)
    
    # Show planned APIs
    print_section("Planned Core APIs")
    show_planned_apis(client)
    
    # Advanced examples
    print_section("Advanced Usage")
    advanced_examples(client)

def show_api_structure(client):
    """Show the current Core API structure."""
    if isinstance(client.core, dict):
        print(f"📋 Available Core APIs: {list(client.core.keys())}")
        
        for api_name in client.core.keys():
            api_obj = client.core[api_name]
            print(f"   ✅ {api_name}: {type(api_obj).__name__}")
    else:
        print(f"📋 Core API Type: {type(client.core).__name__}")
        
        # Check for available methods
        methods = [method for method in dir(client.core) if not method.startswith('_')]
        if methods:
            print(f"   Available methods: {methods[:5]}...")  # Show first 5
        else:
            print("   No public methods found")

def test_actions_api(client):
    """Test the Actions API functionality."""
    if isinstance(client.core, dict) and 'actions' in client.core:
        actions_api = client.core['actions']
        
        print("🔧 Testing Actions API...")
        
        # Test 1: List all actions
        print("\n1. Listing all available actions...")
        actions_result = safe_api_call(actions_api.list_actions)
        
        if actions_result['success']:
            actions_data = actions_result['data']
            print("✅ Actions retrieved successfully")
            
            if hasattr(actions_data, 'list') and hasattr(actions_data.list, 'entries'):
                actions_list = actions_data.list.entries
                print(f"   Found {len(actions_list)} actions")
                
                # Show first few actions
                for i, action in enumerate(actions_list[:5]):
                    if hasattr(action, 'entry'):
                        entry = action.entry
                        action_id = getattr(entry, 'id', 'Unknown')
                        action_title = getattr(entry, 'title', 'No title')
                        print(f"   {i+1}. {action_id}: {action_title}")
                
                if len(actions_list) > 5:
                    print(f"   ... and {len(actions_list) - 5} more")
            else:
                print("   ⚠️ Actions data format unexpected")
        else:
            print(f"❌ Failed to retrieve actions: {actions_result['error']}")
        
        # Test 2: Get specific action (if we have any)
        print("\n2. Testing specific action retrieval...")
        if actions_result['success'] and hasattr(actions_result['data'], 'list'):
            actions_list = actions_result['data'].list.entries
            if actions_list and hasattr(actions_list[0], 'entry'):
                first_action_id = actions_list[0].entry.id
                
                specific_result = safe_api_call(actions_api.get_action, action_id=first_action_id)
                
                if specific_result['success']:
                    print(f"✅ Retrieved specific action: {first_action_id}")
                else:
                    print(f"⚠️ Failed to get specific action: {specific_result['error']}")
            else:
                print("⚠️ No actions available to test individual retrieval")
        else:
            print("⚠️ Skipping specific action test due to list failure")
    else:
        print("❌ Actions API not available in expected format")

def show_planned_apis(client):
    """Show the planned Core APIs that are in development."""
    planned_apis = {
        'nodes': 'File and folder operations, content management',
        'sites': 'Site creation, management, and membership',
        'people': 'User management and profile operations',
        'groups': 'Group management and membership',
        'comments': 'Comments on content and nodes',
        'ratings': 'Rating and like functionality',
        'tags': 'Tag management and assignment',
        'favorites': 'User favorites management',
        'renditions': 'Content renditions and thumbnails',
        'versions': 'Version history and management',
        'shared_links': 'Shared link creation and management',
        'downloads': 'Download archive creation',
        'audit': 'Audit trail and logging',
        'trashcan': 'Deleted items management'
    }
    
    print("🚧 Planned Core APIs (coming soon):")
    
    if isinstance(client.core, dict):
        for api_name, description in planned_apis.items():
            if api_name in client.core:
                print(f"   ✅ {api_name}: {description} (Available)")
            else:
                print(f"   🚧 {api_name}: {description} (Planned)")
    else:
        # Single object format - check for methods
        for api_name, description in planned_apis.items():
            method_name = f"list_{api_name}" if api_name.endswith('s') else f"get_{api_name}"
            if hasattr(client.core, method_name):
                print(f"   ✅ {api_name}: {description} (Available)")
            else:
                print(f"   🚧 {api_name}: {description} (Planned)")

def advanced_examples(client):
    """Advanced usage examples."""
    print("🎯 Advanced Core API Usage:")
    
    # Example 1: Error handling patterns
    print("\n1. Error handling patterns...")
    if isinstance(client.core, dict) and 'actions' in client.core:
        try:
            # Try to get a non-existent action
            result = client.core['actions'].get_action(action_id="non-existent-action")
            print("⚠️ Unexpected success for non-existent action")
        except Exception as e:
            print(f"✅ Proper error handling: {type(e).__name__}")
    
    # Example 2: API availability checking
    print("\n2. API availability checking...")
    available_apis = []
    if isinstance(client.core, dict):
        available_apis = list(client.core.keys())
    else:
        # Check for common methods
        common_methods = ['list_actions', 'list_nodes', 'list_sites']
        available_apis = [method for method in common_methods if hasattr(client.core, method)]
    
    print(f"   Available: {available_apis}")
    
    # Example 3: Future usage patterns
    print("\n3. Future usage patterns (when more APIs are available):")
    print("   # Create a folder")
    print("   folder = client.core['nodes'].create_node(parent_id='-root-', body={'nodeType': 'cm:folder', 'name': 'MyFolder'})")
    print("   ")
    print("   # Upload a file")
    print("   file = client.core['nodes'].create_node(parent_id=folder_id, files={'filedata': file_content})")
    print("   ")
    print("   # Create a site")
    print("   site = client.core['sites'].create_site(body={'id': 'mysite', 'title': 'My Site'})")
    print("   ")
    print("   # Add user to site")
    print("   client.core['sites'].create_site_membership(site_id='mysite', body={'id': 'user1', 'role': 'SiteConsumer'})")

def demonstrate_real_usage():
    """Demonstrate real-world usage patterns."""
    print_section("Real-World Usage Example")
    
    # This shows how you would typically use the Core API
    client = AlfrescoClient(
        host="http://localhost:8080", 
        username="admin", 
        password="admin"
    )
    
    if not client.core:
        print("❌ Core API not available")
        return
    
    print("🌍 Real-world usage scenario:")
    print("1. Check available actions")
    print("2. Prepare for content operations")
    print("3. Handle errors gracefully")
    
    # Step 1: Check what's available
    if isinstance(client.core, dict):
        available_apis = list(client.core.keys())
        print(f"\n✅ Available Core APIs: {available_apis}")
        
        # Use what's available
        if 'actions' in client.core:
            print("🔧 Using Actions API for demonstration...")
            try:
                actions = client.core['actions'].list_actions()
                print("✅ Successfully retrieved actions list")
            except Exception as e:
                print(f"❌ Error: {e}")
    
    print("\n💡 Tip: Always check API availability before use!")
    print("💡 Tip: Use safe_api_call() wrapper for production code!")

if __name__ == "__main__":
    main()
    demonstrate_real_usage() 