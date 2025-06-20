#!/usr/bin/env python3
"""
Alfresco Search API Examples

This file demonstrates how to use the Search API with the master client.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'enhanced_generated'))

from AlfrescoClient import AlfrescoClient


def main():
    """Search API examples."""
    print("🔍 Search API Examples")
    
    # Initialize client
    client = AlfrescoClient(host="http://localhost:8080", username="admin", password="admin")
    
    if not client.search:
        print("❌ Search API not available")
        return
    
    # Example 1: Basic search
    print("\n1. Basic content search...")
    search_request = {
        'query': {
            'query': 'cm:name:*',
            'language': 'afts'
        },
        'paging': {
            'maxItems': 10
        }
    }
    
    try:
        results = client.search.search(search_request=search_request)
        if results and hasattr(results, 'list'):
            print(f"✅ Found {len(results.list.entries)} results")
        else:
            print("✅ Search completed (results format may vary)")
    except Exception as e:
        print(f"❌ Search failed: {e}")
    
    # Example 2: Search by content type
    print("\n2. Search by content type...")
    type_search = {
        'query': {
            'query': 'TYPE:"cm:content"',
            'language': 'afts'
        },
        'paging': {
            'maxItems': 5
        }
    }
    
    try:
        results = client.search.search(search_request=type_search)
        print("✅ Content type search completed")
    except Exception as e:
        print(f"❌ Type search failed: {e}")
    
    # Example 3: Search with filters
    print("\n3. Search with date filter...")
    filtered_search = {
        'query': {
            'query': 'TYPE:"cm:content"',
            'language': 'afts'
        },
        'filterQueries': [
            {'query': 'cm:modified:[NOW-7DAYS TO NOW]'}
        ],
        'paging': {
            'maxItems': 10
        }
    }
    
    try:
        results = client.search.search(search_request=filtered_search)
        print("✅ Filtered search completed")
    except Exception as e:
        print(f"❌ Filtered search failed: {e}")
    
    # Example 4: Search with sorting
    print("\n4. Search with sorting...")
    sorted_search = {
        'query': {
            'query': '*',
            'language': 'afts'
        },
        'sort': [
            {'field': 'cm:modified', 'ascending': False}
        ],
        'paging': {
            'maxItems': 5
        }
    }
    
    try:
        results = client.search.search(search_request=sorted_search)
        print("✅ Sorted search completed")
    except Exception as e:
        print(f"❌ Sorted search failed: {e}")


if __name__ == "__main__":
    main() 