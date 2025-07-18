"""
Search utility functions for the Alfresco API.

This module provides convenient utility functions for common search operations,
using the proper Pydantic models from the raw search client for type safety.
"""

from typing import Optional, List, Dict, Any, Union
from python_alfresco_api.clients.search import AlfrescoSearchClient

# Import proper models from raw search client
from python_alfresco_api.raw_clients.alfresco_search_client.search_client.models import (
    SearchRequest,
    RequestQuery,
    RequestPagination,
    RequestQueryLanguage,
    RequestIncludeItem,
    RequestSortDefinitionItem,
    RequestSortDefinitionItemType,
    RequestFilterQueriesItem,
    RequestScope,
    RequestScopeLocations
)
from python_alfresco_api.raw_clients.alfresco_search_client.search_client.types import UNSET


def _create_empty_search_result():
    """Create an empty search result structure for fallback cases."""
    return type('SearchResult', (), {
        'list': type('SearchList', (), {
            'entries': [],
            'pagination': type('Pagination', (), {
                'count': 0,
                'has_more_items': False,
                'total_items': 0,
                'skip_count': 0,
                'max_items': 0
            })()
        })()
    })()


def _normalize_search_response(search_results):
    """
    Normalize search response to handle different response structures.
    
    Args:
        search_results: Raw search response from API
        
    Returns:
        Normalized search results with consistent structure
    """
    # Handle detailed search response (Response object with parsed attribute)
    if hasattr(search_results, 'parsed') and search_results.parsed is not None:
        search_results = search_results.parsed
    
    # Ensure we have the expected structure
    if not hasattr(search_results, 'list_'):
        print(f"⚠️ Unexpected search response structure: {type(search_results)}")
        print(f"⚠️ Available attributes: {[attr for attr in dir(search_results) if not attr.startswith('_')]}")
        return None
    
    return search_results


def simple_search(
    search_client: Any,  # More flexible type to handle V1.1 hierarchical clients
    query_str: str,
    max_items: int = 20,
    skip_count: int = 0,
    include_fields: Optional[List[str]] = None
) -> Any:
    """
    Simple search utility function that mimics the original MCP server pattern.
    
    Args:
        search_client: The v1.1 hierarchical search client (operation-specific)
        query_str: The search query string
        max_items: Maximum number of results to return
        skip_count: Number of results to skip for pagination
        include_fields: Optional list of fields to include in results
        
    Returns:
        Search results from the Alfresco API
    """
    try:
        # Create proper SearchRequest using attrs models
        request_query = RequestQuery(
            query=query_str,
            language=RequestQueryLanguage.AFTS
        )
        
        request_pagination = RequestPagination(
            max_items=max_items,
            skip_count=skip_count
        )
        
        # Build include list if specified
        include_list = []
        if include_fields:
            for field in include_fields:
                include_list.append(RequestIncludeItem(field))
        
        # Create the main search request
        search_request = SearchRequest(
            query=request_query,
            paging=request_pagination,
            include=include_list if include_list else UNSET
        )
        
        # Execute search using the v1.1 client
        # Try detailed search first, then fall back to standard search
        try:
            # Try NEW detailed search for richer results when available
            if hasattr(search_client, 'search') and hasattr(search_client.search, 'search_detailed'):
                print("🔍 Using detailed search API")
                
                # Use the detailed search method (sync version)
                result = search_client.search.search_detailed(search_request)
                print("✅ Used detailed search API successfully")
                
                # Normalize the response to handle different structures
                normalized_result = _normalize_search_response(result)
                if normalized_result is not None:
                    return normalized_result
                else:
                    # If normalization failed, return the original result
                    return result
            else:
                raise Exception("Detailed search API not available, using fallback")
                
        except Exception as e:
            # Fall back to standard search methods
            print(f"⚠️ Detailed search failed: {e}")
            print("🔄 Falling back to standard search...")
            
            # Handle both cases: main search client and operation-specific client
            if hasattr(search_client, 'search_content'):
                # This is the main search client - use its convenience method
                result = search_client.search_content(body=search_request)
                return result
            elif hasattr(search_client, 'search') and callable(getattr(search_client, 'search')):
                # This is the operation-specific client - call search method directly
                result = search_client.search(body=search_request)
                return result
            else:
                # Fallback: log available methods for debugging
                print(f"⚠️ search_client does not have usable search method")
                print(f"Available methods: {[attr for attr in dir(search_client) if not attr.startswith('_')]}")
                return None
            
    except Exception as e:
        # Only log exceptions for debugging
        print(f"❌ Exception in simple_search: {e}")
        return None


def build_query(
    term: Optional[str] = None,
    content_type: Optional[str] = None,
    site: Optional[str] = None,
    creator: Optional[str] = None,
    modifier: Optional[str] = None,
    folder_path: Optional[str] = None,
    created_after: Optional[str] = None,
    created_before: Optional[str] = None,
    modified_after: Optional[str] = None,
    modified_before: Optional[str] = None
) -> str:
    """
    Build an AFTS query string from common search criteria.
    
    Args:
        term: Text to search for
        content_type: Content type to filter by
        site: Site to search in
        creator: Content creator to filter by
        modifier: Content modifier to filter by
        folder_path: Folder path to search in
        created_after: Created after date (ISO format)
        created_before: Created before date (ISO format)
        modified_after: Modified after date (ISO format)
        modified_before: Modified before date (ISO format)
        
    Returns:
        AFTS query string
    """
    query_parts = []
    
    if term:
        query_parts.append(f'TEXT:"{term}"')
    
    if content_type:
        query_parts.append(f'TYPE:"{content_type}"')
    
    if site:
        query_parts.append(f'SITE:"{site}"')
    
    if creator:
        query_parts.append(f'cm:creator:"{creator}"')
    
    if modifier:
        query_parts.append(f'cm:modifier:"{modifier}"')
    
    if folder_path:
        query_parts.append(f'PATH:"{folder_path}"')
    
    if created_after:
        query_parts.append(f'cm:created:[{created_after} TO MAX]')
    
    if created_before:
        query_parts.append(f'cm:created:[MIN TO {created_before}]')
    
    if modified_after:
        query_parts.append(f'cm:modified:[{modified_after} TO MAX]')
    
    if modified_before:
        query_parts.append(f'cm:modified:[MIN TO {modified_before}]')
    
    return ' AND '.join(query_parts) if query_parts else '*'


def advanced_search(
    search_client: Any,  # More flexible type to handle V1.1 hierarchical clients
    query_str: str,
    max_items: int = 100,
    skip_count: int = 0,
    sort_by: Optional[str] = None,
    sort_ascending: bool = True,
    filter_queries: Optional[List[str]] = None,
    include_fields: Optional[List[str]] = None,
    scope_location: Optional[str] = None
) -> Any:
    """
    Advanced search with sorting, filtering, and scoping options.
    
    Args:
        search_client: The v1.1 hierarchical search client (operation-specific)
        query_str: The search query string
        max_items: Maximum number of results to return
        skip_count: Number of results to skip for pagination
        sort_by: Field to sort by (e.g., 'cm:name', 'cm:modified')
        sort_ascending: Whether to sort ascending (True) or descending (False)
        filter_queries: List of filter query strings
        include_fields: List of fields to include in results
        scope_location: Location to scope search to ('nodes', 'deleted-nodes', 'versions')
        
    Returns:
        Search results from the Alfresco API
    """
    # Create query
    request_query = RequestQuery(
        query=query_str,
        language=RequestQueryLanguage.AFTS
    )
    
    # Create pagination
    request_pagination = RequestPagination(
        max_items=max_items,
        skip_count=skip_count
    )
    
    # Create sort definition if specified
    sort_list = []
    if sort_by:
        sort_item = RequestSortDefinitionItem(
            field=sort_by,
            ascending=sort_ascending,
            type_=RequestSortDefinitionItemType.FIELD
        )
        sort_list.append(sort_item)
    
    # Create filter queries if specified
    filter_list = []
    if filter_queries:
        for fq in filter_queries:
            filter_item = RequestFilterQueriesItem(query=fq)
            filter_list.append(filter_item)
    
    # Create include list if specified
    include_list = []
    if include_fields:
        for field in include_fields:
            include_list.append(RequestIncludeItem(field))
    
    # Create scope if specified
    scope = UNSET
    if scope_location:
        if scope_location == 'nodes':
            scope = RequestScope(locations=RequestScopeLocations.NODES)
        elif scope_location == 'deleted-nodes':
            scope = RequestScope(locations=RequestScopeLocations.DELETED_NODES)
        elif scope_location == 'versions':
            scope = RequestScope(locations=RequestScopeLocations.VERSIONS)
    
    # Create the main search request
    search_request = SearchRequest(
        query=request_query,
        paging=request_pagination,
        sort=sort_list if sort_list else UNSET,
        filter_queries=filter_list if filter_list else UNSET,
        include=include_list if include_list else UNSET,
        scope=scope
    )
    
    # Execute search using the v1.1 client
    try:
        return search_client.search(body=search_request)
    except Exception as e:
        # Log the error and return a simple search fallback
        print(f"Advanced search failed: {e}")
        # Fall back to simple search - but catch exceptions there too
        try:
            return simple_search(search_client, query_str, max_items, skip_count)
        except Exception as e2:
            # If both fail, return empty results structure
            print(f"Fallback simple search also failed: {e2}")
            return _create_empty_search_result()


def search_by_type(
    search_client: Any,  # More flexible type for V1.1 clients
    content_type: str,
    max_items: int = 20
) -> Any:
    """
    Search for content by type.
    
    Args:
        search_client: The v1.1 hierarchical search client (operation-specific)
        content_type: The content type to search for
        max_items: Maximum number of results to return
        
    Returns:
        Search results from the Alfresco API
    """
    query_str = f'TYPE:"{content_type}"'
    return simple_search(search_client, query_str, max_items)


def search_in_site(
    search_client: Any,  # More flexible type for V1.1 clients
    site_id: str,
    search_term: Optional[str] = None,
    max_items: int = 20
) -> Any:
    """
    Search for content in a specific site.
    
    Args:
        search_client: The v1.1 hierarchical search client (operation-specific)
        site_id: The site ID to search in
        search_term: Optional search term
        max_items: Maximum number of results to return
        
    Returns:
        Search results from the Alfresco API
    """
    if search_term:
        query_str = f'SITE:"{site_id}" AND TEXT:"{search_term}"'
    else:
        query_str = f'SITE:"{site_id}"'
    
    return simple_search(search_client, query_str, max_items)


def search_by_creator(
    search_client: Any,  # More flexible type for V1.1 clients
    creator: str,
    max_items: int = 20
) -> Any:
    """
    Search for content by creator.
    
    Args:
        search_client: The v1.1 hierarchical search client (operation-specific)
        creator: The creator username to search for
        max_items: Maximum number of results to return
        
    Returns:
        Search results from the Alfresco API
    """
    query_str = f'cm:creator:"{creator}"'
    return simple_search(search_client, query_str, max_items)


# Common search patterns
SEARCH_PATTERNS = {
    'documents': 'TYPE:"cm:content"',
    'folders': 'TYPE:"cm:folder"',
    'images': 'TYPE:"cm:content" AND (cm:name:"*.jpg" OR cm:name:"*.png" OR cm:name:"*.gif")',
    'recent': 'cm:modified:[NOW-7DAYS TO NOW]',
    'pdf_files': 'TYPE:"cm:content" AND cm:name:"*.pdf"',
    'large_files': 'TYPE:"cm:content" AND cm:content.size:[10485760 TO MAX]',  # > 10MB
    'shared_links': 'TYPE:"app:filelink"',
    'my_files': 'cm:creator:"{username}"'
}


def pattern_search(
    search_client: Any,  # More flexible type for V1.1 clients
    pattern: str,
    username: Optional[str] = None,
    max_items: int = 20
) -> Any:
    """
    Execute a predefined search pattern.
    
    Args:
        search_client: The v1.1 hierarchical search client (operation-specific)
        pattern: The pattern name from SEARCH_PATTERNS
        username: Username for patterns that require it (like 'my_files')
        max_items: Maximum number of results to return
        
    Returns:
        Search results from the Alfresco API
        
    Raises:
        ValueError: If pattern is not found or username is required but not provided
    """
    if pattern not in SEARCH_PATTERNS:
        raise ValueError(f"Unknown search pattern: {pattern}")
    
    query_str = SEARCH_PATTERNS[pattern]
    
    # Handle patterns that require username substitution
    if '{username}' in query_str:
        if not username:
            raise ValueError(f"Pattern '{pattern}' requires username parameter")
        query_str = query_str.format(username=username)
    
    return simple_search(search_client, query_str, max_items)


# Export all functions
__all__ = [
    'simple_search',
    'build_query', 
    'advanced_search',
    'search_by_type',
    'search_in_site',
    'search_by_creator',
    'pattern_search',
    'SEARCH_PATTERNS'
] 