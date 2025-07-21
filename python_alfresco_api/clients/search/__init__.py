"""
Alfresco Search API Client - V1.1 Three-Tier Architecture

Provides access to Search API operations with lazy loading and hierarchical organization.
"""

# Import from Level 2 models
from .models import SearchResponse, SearchRequest

# Import the main client class
from .search_client import AlfrescoSearchClient

# Import all submodules to ensure they get packaged
from . import search, models

# Export the client class and submodules
__all__ = [
    'AlfrescoSearchClient', 'SearchResponse', 'SearchRequest',
    # Lazy-loaded submodules and models
    'search', 'models'
]