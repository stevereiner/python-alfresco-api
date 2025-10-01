"""
Sql Operations Client - Level 3: Sql-Specific Operations

This module provides sql-specific operations within the SearchSql API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.

Each operation provides 4 variants:
- operation(params) - basic sync with explicit parameters
- operation_async(params) - basic async with explicit parameters  
- operation_detailed(params) - detailed sync with explicit parameters
- operation_detailed_async(params) - detailed async with explicit parameters

Perfect for MCP servers and documentation generation.
"""

import asyncio
from typing import Optional, List, Union, Any, Awaitable
from httpx import Response

# Import required types for proper parameter handling
from ....raw_clients.alfresco_search_sql_client.search_sql_client.types import UNSET, Unset
from httpx import Response

# Import model types for proper parameter signatures
# Fixed import naming: sqlresultsetpaging -> sql_result_set_paging, sqlsearchrequest -> sql_search_request
from ....raw_clients.alfresco_search_sql_client.search_sql_client.models.sql_result_set_paging import SQLResultSetPaging
from ....raw_clients.alfresco_search_sql_client.search_sql_client.models.sql_search_request import SQLSearchRequest

# Import from Level 3 (operation-specific models)
from .models import SqlResponse, SqlListResponse, CreateSqlRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_search_sql_client.search_sql_client.api.sql import (
            search as _search
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class SqlClient:
    """
    Sql operations client with 4-pattern detailed functions.
    
    Provides high-level methods for sql management operations
    that are essential for MCP servers and sql workflows.
    
    Each operation has 4 variants for maximum flexibility:
    - Basic sync/async for simple use cases
    - Detailed sync/async for full HTTP response access
    """
    
    def __init__(self, parent_client):
        """Initialize with client factory for raw client access."""
        self.parent_client = parent_client
        self._raw_client = None
        
        # Store raw operation references
        if RAW_OPERATIONS_AVAILABLE:
            self._search = _search
    
    @property
    def raw_client(self):
        """Delegate to parent client's raw client."""
        return self.parent_client.raw_client
    
    @property
    def httpx_client(self):
        """Delegate to parent client's httpx client."""
        return self.parent_client.httpx_client
    
    # =================================================================
    # SQL SEARCH OPERATIONS - 4-PATTERN IMPLEMENTATION
    # =================================================================
    
    def search(
        self,
        query: str,
        language: str = "cmis",
        include_request: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """
        Execute SQL search query (sync).
        
        Executes a SQL search query against the repository.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw SQL search operations not available")
        
        from ....raw_clients.alfresco_search_sql_client.search_sql_client.models.search_sql_query import SearchSqlQuery
        from ....raw_clients.alfresco_search_sql_client.search_sql_client.types import UNSET
        
        search_query = SearchSqlQuery(
            query=query,
            language=language
        )
        
        return self._search.sync(
            client=self.raw_client,
            body=search_query,
            include=include_request if include_request is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    async def search_async(
        self,
        query: str,
        language: str = "cmis",
        include_request: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Optional[Any]:
        """
        Execute SQL search query (async).
        
        Executes a SQL search query against the repository.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw SQL search operations not available")
        
        from ....raw_clients.alfresco_search_sql_client.search_sql_client.models.search_sql_query import SearchSqlQuery
        from ....raw_clients.alfresco_search_sql_client.search_sql_client.types import UNSET
        
        search_query = SearchSqlQuery(
            query=query,
            language=language
        )
        
        return await self._search.asyncio(
            client=self.raw_client,
            body=search_query,
            include=include_request if include_request is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    def search_detailed(
        self,
        query: str,
        language: str = "cmis",
        include_request: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Response:
        """
        Execute SQL search query (detailed sync).
        
        Executes a SQL search query with full HTTP response.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw SQL search operations not available")
        
        from ....raw_clients.alfresco_search_sql_client.search_sql_client.models.search_sql_query import SearchSqlQuery
        from ....raw_clients.alfresco_search_sql_client.search_sql_client.types import UNSET
        
        search_query = SearchSqlQuery(
            query=query,
            language=language
        )
        
        return self._search.sync_detailed(
            client=self.raw_client,
            body=search_query,
            include=include_request if include_request is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    async def search_detailed_async(
        self,
        query: str,
        language: str = "cmis",
        include_request: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Response:
        """
        Execute SQL search query (detailed async).
        
        Executes a SQL search query with full HTTP response.
        """
        if not RAW_OPERATIONS_AVAILABLE:
            raise ImportError("Raw SQL search operations not available")
        
        from ....raw_clients.alfresco_search_sql_client.search_sql_client.models.search_sql_query import SearchSqlQuery
        from ....raw_clients.alfresco_search_sql_client.search_sql_client.types import UNSET
        
        search_query = SearchSqlQuery(
            query=query,
            language=language
        )
        
        return await self._search.asyncio_detailed(
            client=self.raw_client,
            body=search_query,
            include=include_request if include_request is not None else UNSET,
            fields=fields if fields is not None else UNSET
        )
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self.parent_client._client_factory, 'base_url', 'unknown')
        return f"AlfrescoSqlClient(base_url='{base_url}')" 