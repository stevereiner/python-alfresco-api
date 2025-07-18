"""
Level 2: SearchSql API Models - Shared within SearchSql API

This module contains models and structures that are specific to the
Alfresco SearchSql API but shared across multiple SearchSql operations.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs
- Level 2 (This file): SearchSql API models shared within SearchSql API  
- Level 3: Operation-specific models for specific SearchSql operations

Benefits:
- Perfect locality (SearchSql-specific models in SearchSql namespace)
- Clean imports (from .models import SearchSqlResponse)
- Logical organization (API-level grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from pydantic import BaseModel, Field, ConfigDict
from enum import Enum

# Import global models
from ..models import BaseEntry, PagingInfo


class SearchSqlResponse(BaseModel):
    """Base response wrapper for SearchSql API operations."""
    model_config = ConfigDict(extra='forbid')
    
    entries: List[BaseEntry] = Field(default_factory=list, description="SearchSql result entries")
    pagination: Optional[PagingInfo] = Field(None, description="Pagination information")


class SearchSqlRequest(BaseModel):
    """Base request model for SearchSql operations."""
    model_config = ConfigDict(extra='forbid')
    
    max_items: Annotated[int, Field(
        description="Maximum number of results to return",
        default=100,
        ge=1,
        le=1000
    )]
    
    skip_count: Annotated[int, Field(
        description="Number of results to skip for pagination",
        default=0,
        ge=0
    )]


# Export all models
__all__ = [
    'SearchSqlResponse', 'SearchSqlRequest'
]