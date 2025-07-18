"""
Level 3: Tags Operation Models - Specific to Tags Operations

This module contains models that are specific to tags operations
within the Core API.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs  
- Level 2: Core API models shared within Core API
- Level 3 (This file): Tags operation-specific models

Benefits:
- Perfect locality (tags models exactly where tags operations are)
- Clean imports (from .models import TagsResponse)
- Logical organization (operation-specific grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

# Import from Level 1 (global)
from ...models import BaseEntry, ContentInfo, UserInfo

# Import from Level 2 (Core API)
from ..models import CoreResponse


class TagsResponse(CoreResponse):
    """Response wrapper for tags operations."""
    entry: BaseEntry = Field(..., description="Tags data")


class TagsListResponse(BaseModel):
    """Response wrapper for tags list operations."""
    model_config = ConfigDict(extra='forbid')
    
    list: Dict[str, Any] = Field(..., description="List data with pagination")


# Operation-specific models will be added here based on analysis
# Example models for common patterns:


class CreateTagsRequest(BaseModel):
    """Request model for creating tags."""
    model_config = ConfigDict(extra='forbid')
    
    name: Annotated[str, Field(
        description="Tags name",
        min_length=1,
        max_length=255
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Custom properties",
        default=None
    )]


class UpdateTagsRequest(BaseModel):
    """Request model for updating tags."""
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
    'TagsResponse', 
    'TagsListResponse',
    'CreateTagsRequest',
    'UpdateTagsRequest'
]