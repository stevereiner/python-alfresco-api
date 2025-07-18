"""
Level 3: Search Operation Models - Specific to Search Operations

This module contains models that are specific to search operations
within the Search API.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs  
- Level 2: Search API models shared within Search API
- Level 3 (This file): Search operation-specific models

Benefits:
- Perfect locality (search models exactly where search operations are)
- Clean imports (from .models import SearchResponse)
- Logical organization (operation-specific grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

# Import from Level 1 (global)
from ...models import BaseEntry, ContentInfo, UserInfo

# Import from Level 2 (Search API)
from ..models import SearchResponse


class SearchResponse(SearchResponse):
    """Response wrapper for search operations."""
    entry: BaseEntry = Field(..., description="Search data")


class SearchListResponse(BaseModel):
    """Response wrapper for search list operations."""
    model_config = ConfigDict(extra='forbid')
    
    list: Dict[str, Any] = Field(..., description="List data with pagination")


class CreateSearchRequest(BaseModel):
    """Request model for creating search."""
    model_config = ConfigDict(extra='forbid')
    
    name: Annotated[str, Field(
        description="Search name",
        min_length=1,
        max_length=255
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Custom properties",
        default=None
    )]


class UpdateSearchRequest(BaseModel):
    """Request model for updating search."""
    model_config = ConfigDict(extra='forbid')
    
    name: Annotated[Optional[str], Field(
        description="Updated name",
        min_length=1,
        max_length=255,
        default=None
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Updated properties",
        default=None
    )]


# Export all models
__all__ = [
    'SearchResponse', 
    'SearchListResponse',
    'CreateSearchRequest',
    'UpdateSearchRequest'
]