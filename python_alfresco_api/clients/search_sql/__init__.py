"""
Alfresco Search SQL API Client - V1.1 Three-Tier Architecture

Provides access to Search SQL API operations with lazy loading and hierarchical organization.
"""

# Import from Level 2 models
from .models import SearchSqlResponse, SearchSqlRequest

# Import the main client class
from .search_sql_client import AlfrescoSearchSqlClient

# Import all submodules to ensure they get packaged
from . import sql, models

# Export the client class and submodules
__all__ = [
    'AlfrescoSearchSqlClient', 'SearchSqlResponse', 'SearchSqlRequest',
    # Lazy-loaded submodules and models
    'sql', 'models'
]