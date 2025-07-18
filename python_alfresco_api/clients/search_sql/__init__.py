"""
Alfresco Search SQL API Client - V1.1 Three-Tier Architecture

Provides access to Search SQL API operations with lazy loading and hierarchical organization.
"""

# Import from Level 2 models
from .models import SearchSqlResponse, SearchSqlRequest

# Import the main client class
from .search_sql_client import AlfrescoSearchSqlClient

# Export the client class
__all__ = ['AlfrescoSearchSqlClient', 'SearchSqlResponse', 'SearchSqlRequest']