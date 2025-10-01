"""
Alfresco Search SQL API Client - V1.1 Three-Tier Architecture

Provides access to Search SQL API operations with lazy loading and hierarchical organization.
"""

import asyncio
from typing import Optional
from httpx import Response

# Import from Level 2 models
from .models import SearchSqlResponse, SearchSqlRequest


class AlfrescoSearchSqlClient:
    """
    Search SQL operations client with lazy-loaded subsections.
    
    Provides high-level methods for SQL search and query management
    that are essential for MCP servers and search sql workflows.
    """
    
    def __init__(self, client_factory):
        """Initialize with client factory for raw client access."""
        self._client_factory = client_factory
        
        # Lazy-loaded subsection clients
        self._sql = None
        
        # Client instances - initialized on first access
        self._raw_client = None
        self._httpx_client = None
    
    # =================================================================
    # STANDARD CLIENT ACCESS PATTERN - V1.1
    # =================================================================
    
    @property
    def raw_client(self):
        """
        Get the raw authenticated client for advanced operations.
        
        This is the STANDARD way to access the underlying client.
        """
        if self._raw_client is None:
            self._raw_client = self._create_raw_client()
        return self._raw_client
    
    @property
    def httpx_client(self):
        """
        Get direct access to httpx client for raw HTTP operations.
        
        This is the STANDARD way to access the HTTP client.
        Perfect for MCP servers that need raw HTTP access.
        """
        if self._httpx_client is None:
            self._httpx_client = self._create_httpx_client()
        return self._httpx_client
    
    @property
    def is_initialized(self) -> bool:
        """
        Check if the client is initialized and functional.
        
        This is the STANDARD way to check initialization status.
        """
        try:
            # Try to access raw client to test initialization
            _ = self.raw_client
            return True
        except Exception:
            return False
    
    def _create_raw_client(self):
        """
        Create the raw authenticated client.
        
        This is INTERNAL - use raw_client property instead.
        """
        from ...raw_clients.alfresco_search_sql_client.search_sql_client.client import AuthenticatedClient
        
        # Prepare client arguments
        client_kwargs = {
            "base_url": f"{self._client_factory.base_url}/alfresco/api/-default-/public/search/sql/versions/1",
            "token": self._client_factory.auth.get_auth_token(),
            "prefix": self._client_factory.auth.get_auth_prefix(),
            "verify_ssl": self._client_factory.verify_ssl
        }
        
        # Only add timeout if specified (not None)
        if self._client_factory.timeout is not None:
            client_kwargs["timeout"] = self._client_factory.timeout
        
        return AuthenticatedClient(**client_kwargs)
    
    def _create_httpx_client(self):
        """
        Create the httpx client for direct HTTP operations.
        
        This is INTERNAL - use httpx_client property instead.
        """
        return self.raw_client.get_httpx_client()

    # =================================================================
    # DEPRECATED METHODS - FOR BACKWARD COMPATIBILITY
    # =================================================================
    
    def get_httpx_client(self):
        """
        DEPRECATED: Use httpx_client property instead.
        
        This method is kept for backward compatibility only.
        """
        return self.httpx_client

    def _get_raw_client(self):
        """
        DEPRECATED: Use raw_client property instead.
        
        This method is kept for backward compatibility only.
        """
        return self.raw_client

    # =================================================================
    # SUBSECTION PROPERTIES
    # =================================================================
    
    @property
    def available(self) -> bool:
        """Check if the search SQL client is available and functional."""
        return self.is_initialized
    
    @property
    def sql(self):
        """Get the SQL operations client."""
        if self._sql is None:
            # Lazy load the SQL client
            from .sql import SqlClient
            self._sql = SqlClient(self)
        return self._sql
    
    # =================================================================
    # CONVENIENCE METHODS
    # =================================================================
    
    def search(self, *args, **kwargs):
        """Execute SQL search using SYNC operations."""
        return self.sql.search(*args, **kwargs)
    
    async def search_async(self, *args, **kwargs):
        """Execute SQL search using ASYNC operations."""
        return await self.sql.search_async(*args, **kwargs)
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self._client_factory, 'base_url', 'unknown')
        return f"AlfrescoSearchSqlClient(base_url='{base_url}')" 