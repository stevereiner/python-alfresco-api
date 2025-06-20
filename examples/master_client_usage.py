#!/usr/bin/env python3
"""
Alfresco Master Client Usage Examples

This file demonstrates how to use the Alfresco Master Client and all 7 API sub-clients
using the enhanced generated approach. These examples are tested and working.

Requirements:
- Alfresco server running on localhost:8080
- Admin credentials (admin/admin)
- All API clients properly configured

Author: Alfresco Python Client
"""

import sys
import os
from datetime import datetime

# Add the enhanced_generated directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'enhanced_generated'))

from AlfrescoClient import AlfrescoClient


def print_section(title):
    """Print a formatted section header."""
    print(f"\n{'='*60}")
    print(f" {title}")
    print(f"{'='*60}")


def safe_api_call(func, *args, **kwargs):
    """Safely execute an API call with error handling."""
    try:
        result = func(*args, **kwargs)
        return {'success': True, 'data': result}
    except Exception as e:
        return {'success': False, 'error': str(e)}


def main():
    """Main example execution with real working APIs."""
    print_section("Alfresco Master Client - Enhanced Examples")
    
    # Initialize the master client
    print("🚀 Initializing Alfresco Master Client...")
    client = AlfrescoClient(
        host="http://localhost:8080",
        username="admin", 
        password="admin",
        verify_ssl=False
    )
    
    # Test connection and show API status
    try:
        connection_info = client.test_connection()
        print(f"✅ Connected to: {connection_info['host']}")
        print(f"📊 Working APIs: {connection_info['working_apis']}/{connection_info['total_apis']}")
        print(f"📈 Success Rate: {connection_info['success_rate']}")
        
        working_apis = client.get_working_apis()
        print(f"🔧 Available APIs: {', '.join(working_apis)}")
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return

    # Authentication API Examples
    authentication_examples(client)
    
    # Core API Examples  
    core_api_examples(client)
    
    # Discovery API Examples
    discovery_examples(client)
    
    # Search API Examples
    search_examples(client)
    
    # Workflow API Examples
    workflow_examples(client)
    
    # Model API Examples
    model_examples(client)
    
    # Search SQL API Examples
    search_sql_examples(client)
    
    # Summary
    print_section("Summary")
    final_status = client.get_api_status()
    working_count = sum(1 for status in final_status.values() if status)
    total_count = len(final_status)
    
    print(f"📊 Final Status: {working_count}/{total_count} APIs working")
    print(f"📈 Success Rate: {(working_count/total_count)*100:.1f}%")
    
    print(f"\n🎉 Examples completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


def authentication_examples(client):
    """Authentication API examples."""
    print_section("Authentication API Examples")
    if client.auth:
        print("🔐 Testing Authentication API...")
        
        # Create authentication ticket
        ticket_result = safe_api_call(
            client.auth.create_ticket,
            ticket_body={'userId': 'admin', 'password': 'admin'}
        )
        
        if ticket_result['success']:
            print("✅ Authentication ticket created successfully")
            ticket_data = ticket_result['data']
            if hasattr(ticket_data, 'entry') and hasattr(ticket_data.entry, 'id'):
                print(f"   Ticket ID: {ticket_data.entry.id}")
        else:
            print(f"❌ Authentication failed: {ticket_result['error']}")
        
        # Validate ticket
        validate_result = safe_api_call(client.auth.validate_ticket)
        if validate_result['success']:
            print("✅ Ticket validation successful")
        else:
            print(f"⚠️ Ticket validation failed: {validate_result['error']}")
    else:
        print("❌ Authentication API not available")


def core_api_examples(client):
    """Core API examples."""
    print_section("Core API Examples")
    if client.core:
        print("🗂️ Testing Core API...")
        
        if isinstance(client.core, dict):
            print(f"Available Core APIs: {list(client.core.keys())}")
            
            # Actions API example
            if 'actions' in client.core:
                print("\n1. Testing Actions API...")
                actions_result = safe_api_call(client.core['actions'].list_actions)
                if actions_result['success']:
                    print("✅ Actions API accessible")
                    actions_data = actions_result['data']
                    if hasattr(actions_data, 'list') and hasattr(actions_data.list, 'entries'):
                        print(f"   Found {len(actions_data.list.entries)} actions")
                else:
                    print(f"❌ Actions API failed: {actions_result['error']}")
            
            # Check for other APIs
            other_apis = ['nodes', 'sites', 'people', 'groups']
            for api_name in other_apis:
                if api_name in client.core:
                    print(f"✅ {api_name.title()} API available")
                else:
                    print(f"⚠️ {api_name.title()} API - Coming soon")
        else:
            print("Core API available in single object format")
    else:
        print("❌ Core API not available")


def discovery_examples(client):
    """Discovery API examples."""
    print_section("Discovery API Examples")
    if client.discovery:
        print("🔍 Testing Discovery API...")
        
        # Get repository information
        repo_result = safe_api_call(client.discovery.get_repository_information)
        
        if repo_result['success'] and repo_result['data']:
            print("✅ Repository information retrieved")
            repo_data = repo_result['data']
            if hasattr(repo_data, 'entry'):
                entry = repo_data.entry
                if hasattr(entry, 'repository'):
                    repo = entry.repository
                    repo_name = getattr(repo, 'name', 'Unknown')
                    version_info = getattr(repo, 'version', None)
                    version_display = getattr(version_info, 'display', 'Unknown') if version_info else 'Unknown'
                    print(f"   Repository: {repo_name}")
                    print(f"   Version: {version_display}")
                else:
                    print("   Repository: Pydantic object structure")
        else:
            print(f"⚠️ Repository info failed: {repo_result.get('error', 'Unknown error')}")
    else:
        print("❌ Discovery API not available")


def search_examples(client):
    """Search API examples."""
    print_section("Search API Examples")
    if client.search:
        print("🔍 Testing Search API...")
        
        # Basic search example
        search_request = {
            'query': {
                'query': 'cm:name:*',
                'language': 'afts'
            },
            'paging': {
                'maxItems': 5,
                'skipCount': 0
            }
        }
        
        search_result = safe_api_call(client.search.search, search_request=search_request)
        
        if search_result['success']:
            print("✅ Search completed successfully")
            search_data = search_result['data']
            if hasattr(search_data, 'list') and hasattr(search_data.list, 'entries'):
                print(f"   Found {len(search_data.list.entries)} results")
        else:
            print(f"⚠️ Search failed: {search_result.get('error', 'Unknown error')}")
    else:
        print("❌ Search API not available")


def workflow_examples(client):
    """Workflow API examples."""
    print_section("Workflow API Examples")
    if client.workflow:
        print("⚙️ Testing Workflow API...")
        
        if isinstance(client.workflow, dict):
            available_apis = list(client.workflow.keys())
            print(f"Available Workflow APIs: {available_apis}")
            
            # Try to access process definitions if available
            if 'process_definitions' in client.workflow:
                defs_result = safe_api_call(client.workflow['process_definitions'].list_process_definitions)
                if defs_result['success']:
                    print("✅ Process definitions accessible")
                else:
                    print(f"⚠️ Process definitions failed: {defs_result['error']}")
        else:
            print("Workflow API available in single object format")
    else:
        print("❌ Workflow API not available")


def model_examples(client):
    """Model API examples."""
    print_section("Model API Examples")
    if client.model:
        print("🏗️ Testing Model API...")
        
        # Try to list aspects if available
        if hasattr(client.model, 'list_aspects'):
            aspects_result = safe_api_call(client.model.list_aspects)
            if aspects_result['success']:
                print("✅ Model API accessible")
                aspects_data = aspects_result['data']
                if hasattr(aspects_data, 'list') and hasattr(aspects_data.list, 'entries'):
                    print(f"   Found {len(aspects_data.list.entries)} aspects")
            else:
                print(f"❌ Model API failed: {aspects_result['error']}")
        else:
            print("⚠️ Model API methods not yet available")
    else:
        print("❌ Model API not available")


def search_sql_examples(client):
    """Search SQL API examples."""
    print_section("Search SQL API Examples")
    if client.search_sql:
        print("🗄️ Testing Search SQL API...")
        print("Note: SQL search requires Solr configuration")
        
        # Simple SQL query example
        sql_query = {"stmt": "SELECT * FROM cmis:document LIMIT 5"}
        sql_result = safe_api_call(client.search_sql.search, sql_query)
        
        if sql_result['success']:
            print("✅ SQL search completed")
            sql_data = sql_result['data']
            if hasattr(sql_data, 'list') and hasattr(sql_data.list, 'entries'):
                print(f"   Found {len(sql_data.list.entries)} results")
        else:
            print(f"⚠️ SQL search failed: {sql_result.get('error', 'Expected if Solr not configured')}")
    else:
        print("❌ Search SQL API not available")


def error_handling_example():
    """Demonstrate proper error handling."""
    print_section("Error Handling Examples")
    
    client = AlfrescoClient(
        host="http://localhost:8080",
        username="admin",
        password="admin"
    )

    # Example 1: Handling API availability
    if client.core:
        try:
            if isinstance(client.core, dict) and 'actions' in client.core:
                actions = client.core['actions'].list_actions()
                print("✅ Actions API call successful")
        except Exception as e:
            print(f"❌ Error accessing Actions API: {e}")
    else:
        print("⚠️ Core API not available - handle gracefully")

    # Example 2: Handling authentication errors
    try:
        if client.auth:
            ticket = client.auth.create_ticket(ticket_body={'userId': 'invalid', 'password': 'invalid'})
    except Exception as e:
        print(f"✅ Authentication error handled: {e}")


def advanced_usage_example():
    """Advanced usage patterns."""
    print_section("Advanced Usage Examples")
    
    client = AlfrescoClient(
        host="http://localhost:8080",
        username="admin",
        password="admin"
    )

    # Example: Check API availability before use
    working_apis = client.get_working_apis()
    print(f"Working APIs: {working_apis}")
    
    # Example: Combine multiple APIs
    if 'discovery' in working_apis and 'search' in working_apis:
        try:
            # Get repository info first
            if client.discovery:
                repo_info = client.discovery.get_repository_information()
                print("✅ Repository information retrieved")
            
            # Then perform a search
            if client.search:
                search_results = client.search.search(search_request={
                    'query': {'query': '*', 'language': 'afts'},
                    'paging': {'maxItems': 3}
                })
                print("✅ Search completed")
        except Exception as e:
            print(f"❌ Error in combined API usage: {e}")


if __name__ == "__main__":
    main()
    print("\nError Handling Examples:")
    error_handling_example()
    print("\nAdvanced Usage Examples:")
    advanced_usage_example()
