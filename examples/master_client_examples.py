#!/usr/bin/env python3
"""
Alfresco Master Client Examples

This file demonstrates how to use the Alfresco Master Client and all 7 API sub-clients.
Examples include authentication, content management, search, workflows, and more.

Requirements:
- Alfresco server running on localhost:8080
- Admin credentials (admin/admin)
- All API clients properly configured

Author: Alfresco Python Client
"""

import sys
import os
import json
from datetime import datetime

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
    """Main example execution."""
    print_section("Alfresco Master Client Examples")
    
    # Initialize the master client
    print("🚀 Initializing Alfresco Master Client...")
    client = AlfrescoClient(
        host="http://localhost:8080",
        username="admin", 
        password="admin",
        verify_ssl=False
    )
    
    # Test connection
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
    print_section("Authentication API Examples")
    if client.auth:
        print("🔐 Testing Authentication API...")
        ticket_result = safe_api_call(
            client.auth.create_ticket,
            ticket_body={'userId': 'admin', 'password': 'admin'}
        )
        
        if ticket_result['success']:
            print("✅ Authentication ticket created successfully")
        else:
            print(f"❌ Authentication failed: {ticket_result['error']}")
    
    # Discovery API Examples
    print_section("Discovery API Examples")
    if client.discovery:
        print("🔍 Testing Discovery API...")
        repo_result = safe_api_call(client.discovery.get_repository_information)
        
        if repo_result['success'] and repo_result['data']:
            print("✅ Repository information retrieved")
        else:
            print(f"⚠️ Repository info failed: {repo_result.get('error', 'Unknown error')}")
    
    # Search API Examples
    print_section("Search API Examples")
    if client.search:
        print("🔍 Testing Search API...")
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
        else:
            print(f"⚠️ Search failed: {search_result.get('error', 'Unknown error')}")
    
    # Core API Examples
    print_section("Core API Examples")
    if client.core:
        print("🗂️ Testing Core API...")
        if isinstance(client.core, dict):
            print(f"Available Core APIs: {list(client.core.keys())}")
            
            if 'actions' in client.core:
                actions_result = safe_api_call(client.core['actions'].list_actions)
                if actions_result['success']:
                    print("✅ Actions API accessible")
                else:
                    print(f"❌ Actions API failed: {actions_result['error']}")
    
    # Workflow API Examples
    print_section("Workflow API Examples")
    if client.workflow:
        print("⚙️ Testing Workflow API...")
        if isinstance(client.workflow, dict):
            available_apis = list(client.workflow.keys())
            print(f"Available Workflow APIs: {available_apis}")
    
    # Model API Examples
    print_section("Model API Examples")
    if client.model:
        print("🏗️ Testing Model API...")
        if hasattr(client.model, 'list_aspects'):
            aspects_result = safe_api_call(client.model.list_aspects)
            if aspects_result['success']:
                print("✅ Model API accessible")
            else:
                print(f"❌ Model API failed: {aspects_result['error']}")
    
    # Search SQL API Examples  
    print_section("Search SQL API Examples")
    if client.search_sql:
        print("🗄️ Testing Search SQL API...")
        print("Note: SQL search requires Solr configuration")
        
        sql_query = {"stmt": "SELECT * FROM cmis:document LIMIT 5"}
        sql_result = safe_api_call(client.search_sql.search, sql_query)
        
        if sql_result['success']:
            print("✅ SQL search completed")
        else:
            print(f"⚠️ SQL search failed: {sql_result.get('error', 'Expected if Solr not configured')}")
    
    # Summary
    print_section("Summary")
    final_status = client.get_api_status()
    working_count = sum(1 for status in final_status.values() if status)
    total_count = len(final_status)
    
    print(f"📊 Final Status: {working_count}/{total_count} APIs working")
    print(f"📈 Success Rate: {(working_count/total_count)*100:.1f}%")
    
    print(f"\n🎉 Examples completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main() 