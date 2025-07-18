"""
Level 2: Search API Models - Shared within Search API

This module contains models and structures that are specific to the
Alfresco Search API but shared across multiple Search operations.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs
- Level 2 (This file): Search API models shared within Search API  
- Level 3: Operation-specific models for specific Search operations

Benefits:
- Perfect locality (Search-specific models in Search namespace)
- Clean imports (from .models import SearchResponse)
- Logical organization (API-level grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from pydantic import BaseModel, Field, ConfigDict
from enum import Enum

# Import global models
from ..models import BaseEntry, PagingInfo


class SearchResponse(BaseModel):
    """Base response wrapper for Search API operations."""
    model_config = ConfigDict(extra='forbid')
    
    entries: List[BaseEntry] = Field(default_factory=list, description="Search result entries")
    pagination: Optional[PagingInfo] = Field(None, description="Pagination information")


class SearchRequest(BaseModel):
    """Base request model for Search operations."""
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
    'SearchResponse', 'SearchRequest'
]