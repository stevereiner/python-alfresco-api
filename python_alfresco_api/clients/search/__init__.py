"""
Alfresco Search API Client - V1.1 Three-Tier Architecture

Provides access to Search API operations with lazy loading and hierarchical organization.
"""

# Import from Level 2 models
from .models import SearchResponse, SearchRequest

# Import the main client class
from .search_client import AlfrescoSearchClient

# Export the client class
__all__ = ['AlfrescoSearchClient', 'SearchResponse', 'SearchRequest']