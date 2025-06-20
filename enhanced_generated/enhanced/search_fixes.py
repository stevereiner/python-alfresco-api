"""
Search API fixes and enhancements for Alfresco Search API.

This module provides fixes and enhancements for the generated Alfresco Search API client.
"""

import sys
from pathlib import Path
from typing import Dict, Any, Optional, List

# Add generated client to path
client_dir = Path(__file__).parent.parent / "clients" / "alfresco-search"
if str(client_dir) not in sys.path:
    sys.path.insert(0, str(client_dir))

# Add Pydantic models to path  
models_dir = Path(__file__).parent.parent / "models"
if str(models_dir) not in sys.path:
    sys.path.insert(0, str(models_dir))

try:
    from alfresco_search_client.api_client import ApiClient
    from alfresco_search_client.configuration import Configuration
    from alfresco_search_client.api.search_api import SearchApi
    print("✅ Successfully imported Alfresco Search API client")
except ImportError as e:
    print(f"❌ Failed to import Alfresco Search API client: {e}")
    ApiClient = None
    Configuration = None
    SearchApi = None

try:
    from alfresco_search_models import *
    print("✅ Successfully imported Alfresco Search Pydantic models")
except ImportError as e:
    print(f"❌ Failed to import Alfresco Search Pydantic models: {e}")

try:
    from alfresco_search_client.models.node import Node
    print("✅ Successfully imported Node model from Search client")
except ImportError as e:
    print(f"❌ Failed to import Node model: {e}")
    Node = None

class SearchFixes:
    """Fixes and enhancements for Alfresco Search API."""
    
    def __init__(self, api_client: ApiClient):
        """Initialize with an API client."""
        self.api_client = api_client
        self.search_api = SearchApi(api_client)
    
    def enhanced_search(self, query: str, max_items: int = 10, skip_count: int = 0) -> Dict[str, Any]:
        """
        Enhanced search method with better error handling and result processing.
        
        Args:
            query: Search query string
            max_items: Maximum number of items to return
            skip_count: Number of items to skip
            
        Returns:
            Dictionary with search results and metadata
        """
        try:
            # Create search request
            search_request = {
                'query': {
                    'query': query,
                    'language': 'afts'
                },
                'paging': {
                    'maxItems': max_items,
                    'skipCount': skip_count
                }
            }
            
            # Perform search
            response = self.search_api.search(search_request=search_request)
            
            # Process results
            results = []
            if hasattr(response, 'list') and hasattr(response.list, 'entries'):
                for entry in response.list.entries:
                    if hasattr(entry, 'entry'):
                        node_data = {
                            'id': getattr(entry.entry, 'id', None),
                            'name': getattr(entry.entry, 'name', None),
                            'node_type': getattr(entry.entry, 'node_type', None),
                            'created_at': getattr(entry.entry, 'created_at', None),
                            'modified_at': getattr(entry.entry, 'modified_at', None),
                            'size': getattr(entry.entry, 'size', None),
                            'parent_id': getattr(entry.entry, 'parent_id', None)
                        }
                        results.append(node_data)
            
            # Extract pagination info
            pagination = {}
            if hasattr(response, 'list') and hasattr(response.list, 'pagination'):
                pagination = {
                    'count': getattr(response.list.pagination, 'count', 0),
                    'total_items': getattr(response.list.pagination, 'total_items', 0),
                    'skip_count': getattr(response.list.pagination, 'skip_count', 0),
                    'max_items': getattr(response.list.pagination, 'max_items', 0)
                }
            
            return {
                'results': results,
                'pagination': pagination,
                'query': query,
                'success': True
            }
            
        except Exception as e:
            return {
                'results': [],
                'pagination': {},
                'query': query,
                'success': False,
                'error': str(e)
            }
    
    def search_by_type(self, node_type: str, max_items: int = 10) -> Dict[str, Any]:
        """
        Search for nodes by type.
        
        Args:
            node_type: Node type to search for (e.g., 'cm:content', 'cm:folder')
            max_items: Maximum number of items to return
            
        Returns:
            Dictionary with search results
        """
        query = f"TYPE:\"{node_type}\""
        return self.enhanced_search(query, max_items)
    
    def search_by_name(self, name_pattern: str, max_items: int = 10) -> Dict[str, Any]:
        """
        Search for nodes by name pattern.
        
        Args:
            name_pattern: Name pattern to search for
            max_items: Maximum number of items to return
            
        Returns:
            Dictionary with search results
        """
        query = f"cm:name:*{name_pattern}*"
        return self.enhanced_search(query, max_items)

def create_search_fixes(host: str = "http://localhost:8080", username: str = "admin", password: str = "admin") -> SearchFixes:
    """Convenience function to create SearchFixes instance."""
    if not ApiClient or not Configuration:
        raise ImportError("Alfresco Search API client not available")
    
    config = Configuration()
    config.host = f"{host}/alfresco/api/-default-/public/search/versions/1"
    config.username = username
    config.password = password
    
    api_client = ApiClient(configuration=config)
    return SearchFixes(api_client)

if __name__ == "__main__":
    # Test the search fixes
    try:
        search_fixes = create_search_fixes()
        print("✅ Search fixes created successfully")
        
        # Test enhanced search
        results = search_fixes.enhanced_search("test", max_items=5)
        print(f"✅ Enhanced search test completed: {results['success']}")
        
    except Exception as e:
        print(f"❌ Search fixes test failed: {e}") 
