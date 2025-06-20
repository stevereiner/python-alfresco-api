#!/usr/bin/env python3
"""
Alfresco Search SQL API Examples

This file demonstrates how to use the Search SQL API with the master client.
The Search SQL API provides SQL pass-through querying to Solr for structured data queries.

This is different from the main Search API which supports:
- Full text search across content
- AFTS (Alfresco Full Text Search) language
- Complex filtering and advanced search capabilities

The Search SQL API is designed for:
- Administrative reporting and other users.
- A Solr SQL passthrough, provides the ability to use SQL to query Solr.

Note: This API requires Solr to be properly configured with Alfresco.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'enhanced_generated'))

from AlfrescoClient import AlfrescoClient


def main():
    """Search SQL API examples."""
    print("🗄️ Search SQL API Examples")
    print("Note: This API requires Solr configuration")
    
    # Initialize client
    client = AlfrescoClient(host="http://localhost:8080", username="admin", password="admin")
    
    if not client.search_sql:
        print("❌ Search SQL API not available")
        return
    
    # Example 1: Simple CMIS SQL query
    print("\n1. Simple document query...")
    try:
        sql_query = {
            "stmt": "SELECT * FROM cmis:document LIMIT 5"
        }
        
        results = client.search_sql.search(sql_query)
        if results and hasattr(results, 'entries'):
            print(f"✅ Found {len(results.entries)} documents")
            for i, doc in enumerate(results.entries[:3]):
                if hasattr(doc, 'entry'):
                    print(f"  {i+1}. {getattr(doc.entry, 'name', 'No name')}")
        else:
            print("✅ SQL search completed")
    except Exception as e:
        print(f"❌ Simple document query failed: {e}")
    
    # Example 2: Query with WHERE clause
    print("\n2. Query with WHERE clause...")
    try:
        sql_query = {
            "stmt": "SELECT cmis:name, cmis:objectTypeId FROM cmis:document WHERE cmis:name LIKE '%.pdf' LIMIT 3"
        }
        
        results = client.search_sql.search(sql_query)
        if results:
            print("✅ PDF documents query completed")
        else:
            print("✅ WHERE clause query completed")
    except Exception as e:
        print(f"❌ WHERE clause query failed: {e}")
    
    # Example 3: Query folders
    print("\n3. Folder query...")
    try:
        sql_query = {
            "stmt": "SELECT cmis:name, cmis:path FROM cmis:folder LIMIT 5"
        }
        
        results = client.search_sql.search(sql_query)
        if results and hasattr(results, 'entries'):
            print(f"✅ Found {len(results.entries)} folders")
            for i, folder in enumerate(results.entries[:3]):
                if hasattr(folder, 'entry'):
                    print(f"  {i+1}. {getattr(folder.entry, 'name', 'No name')}")
        else:
            print("✅ Folder query completed")
    except Exception as e:
        print(f"❌ Folder query failed: {e}")
    
    # Example 4: Query with ORDER BY
    print("\n4. Query with ORDER BY...")
    try:
        sql_query = {
            "stmt": "SELECT cmis:name, cmis:creationDate FROM cmis:document ORDER BY cmis:creationDate DESC LIMIT 3"
        }
        
        results = client.search_sql.search(sql_query)
        if results:
            print("✅ ORDER BY query completed")
        else:
            print("✅ Ordered query completed")
    except Exception as e:
        print(f"❌ ORDER BY query failed: {e}")
    
    # Example 5: Query specific properties
    print("\n5. Query specific properties...")
    try:
        sql_query = {
            "stmt": "SELECT cmis:objectId, cmis:name, cmis:contentStreamLength FROM cmis:document WHERE cmis:contentStreamLength IS NOT NULL LIMIT 3"
        }
        
        results = client.search_sql.search(sql_query)
        if results:
            print("✅ Properties query completed")
        else:
            print("✅ Specific properties query completed")
    except Exception as e:
        print(f"❌ Properties query failed: {e}")
    
    # Example 6: Count query
    print("\n6. Count query...")
    try:
        sql_query = {
            "stmt": "SELECT COUNT(*) as total FROM cmis:document"
        }
        
        results = client.search_sql.search(sql_query)
        if results:
            print("✅ Count query completed")
        else:
            print("✅ Count query completed")
    except Exception as e:
        print(f"❌ Count query failed: {e}")
    
    print("\n💡 Tips for Search SQL API:")
    print("- Ensure Solr is properly configured and indexed")
    print("- Use CMIS SQL syntax (not regular SQL)")
    print("- Common tables: cmis:document, cmis:folder")
    print("- Use LIMIT to avoid large result sets")
    print("- Check Alfresco logs if queries fail")


if __name__ == "__main__":
    main() 