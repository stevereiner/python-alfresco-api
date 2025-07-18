"""
Activities Operations Client - Level 3: Activities-Specific Operations

This module provides activities-specific operations within the Core API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.

Each operation provides 4 variants:
- operation(params) - basic sync with explicit parameters
- operation_async(params) - basic async with explicit parameters  
- operation_detailed(params) - detailed sync with explicit parameters
- operation_detailed_async(params) - detailed async with explicit parameters

Perfect for MCP servers and documentation generation.
"""

import asyncio
from typing import Optional, List, Union, Any
from httpx import Response

# Import from Level 3 (operation-specific models)
from .models import ActivitiesResponse, ActivitiesListResponse, CreateActivitiesRequest

# Import raw operations
try:
    from ....raw_clients.alfresco_core_client.core_client.api.activities import (
            list_activities_for_person as _list_activities_for_person
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class ActivitiesClient:
    """
    Activities operations client with 4-pattern detailed functions.
    
    Provides high-level methods for activities management operations
    that are essential for MCP servers and activities workflows.
    
    Each operation has 4 variants for maximum flexibility:
    - Basic sync/async for simple use cases
    - Detailed sync/async for full HTTP response access
    """
    
    def __init__(self, client_factory):
        """Initialize with client factory for raw client access."""
        self._client_factory = client_factory
        self._raw_client = None
        
        # Store raw operation references
        if RAW_OPERATIONS_AVAILABLE:
            self._list_activities_for_person = _list_activities_for_person
    
    def _get_raw_client(self):
        """Get or create the raw client."""
        if self._raw_client is None:
            # Import the raw core client directly
            from ....raw_clients.alfresco_core_client.core_client.client import AuthenticatedClient
            
            # Create the raw client with same auth setup
            self._raw_client = AuthenticatedClient(
                base_url=f"{self._client_factory.base_url}/alfresco/api/-default-/public/alfresco/versions/1",
                token=self._client_factory.auth.get_auth_token(),
                prefix=self._client_factory.auth.get_auth_prefix(),
                verify_ssl=self._client_factory.verify_ssl
            )
        return self._raw_client
    
    def get_httpx_client(self):
        """
        Get direct access to raw httpx client for advanced operations.
        
        Perfect for MCP servers that need raw HTTP access.
        """
        return self._get_raw_client().get_httpx_client()
    
    # ==================== 4-PATTERN OPERATIONS ====================

    # ==================== LIST_ACTIVITIES_FOR_PERSON OPERATION ====================
    
    def list_activities_for_person(self, person_id: Any, skip_count: Any, max_items: Any, who: Any, site_id: Any, fields: Any) -> ActivitiesResponse:
        """
        List Activities For Person operation.
        
        Perfect for MCP servers and activities workflows.
        Returns simplified response for common use cases.
        """
        if not hasattr(self, '_list_activities_for_person'):
            raise ImportError("Raw client operation not available")
        
        result = self._list_activities_for_person.sync(client=self._get_raw_client(), person_id=person_id, skip_count=skip_count, max_items=max_items, who=who, site_id=site_id, fields=fields)
        
        # Convert to standardized response
        from ..models import BaseEntry
        return ActivitiesResponse(entry=BaseEntry(id=f"result-activities"))
    
    async def list_activities_for_person_async(self, person_id: Any, skip_count: Any, max_items: Any, who: Any, site_id: Any, fields: Any) -> ActivitiesResponse:
        """
        List Activities For Person operation (async).
        
        Perfect for MCP servers and activities workflows.
        Returns simplified response for common use cases.
        """
        if not hasattr(self, '_list_activities_for_person'):
            raise ImportError("Raw client operation not available")
        
        result = await self._list_activities_for_person.asyncio(client=self._get_raw_client(), person_id=person_id, skip_count=skip_count, max_items=max_items, who=who, site_id=site_id, fields=fields)
        
        # Convert to standardized response
        from ..models import BaseEntry
        return ActivitiesResponse(entry=BaseEntry(id=f"result-activities"))
    
    def list_activities_for_person_detailed(self, person_id: Any, skip_count: Any, max_items: Any, who: Any, site_id: Any, fields: Any):
        """
        List Activities For Person operation (detailed).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        """
        if not hasattr(self, '_list_activities_for_person'):
            raise ImportError("Raw client operation not available")
        
        return self._list_activities_for_person.sync_detailed(client=self._get_raw_client(), person_id=person_id, skip_count=skip_count, max_items=max_items, who=who, site_id=site_id, fields=fields)
    
    async def list_activities_for_person_detailed_async(self, person_id: Any, skip_count: Any, max_items: Any, who: Any, site_id: Any, fields: Any):
        """
        List Activities For Person operation (detailed, async).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        """
        if not hasattr(self, '_list_activities_for_person'):
            raise ImportError("Raw client operation not available")
        
        return await self._list_activities_for_person.asyncio_detailed(client=self._get_raw_client(), person_id=person_id, skip_count=skip_count, max_items=max_items, who=who, site_id=site_id, fields=fields)

    
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self._client_factory, 'base_url', 'unknown')
        return f"AlfrescoActivitiesClient(base_url='{base_url}')" 