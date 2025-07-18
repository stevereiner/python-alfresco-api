"""
Level 3: Comments Operation Models - Specific to Comments Operations

This module contains models that are specific to comments operations
within the Core API.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs  
- Level 2: Core API models shared within Core API
- Level 3 (This file): Comments operation-specific models

Benefits:
- Perfect locality (comments models exactly where comments operations are)
- Clean imports (from .models import CommentsResponse)
- Logical organization (operation-specific grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

# Import from Level 1 (global)
from ...models import BaseEntry, ContentInfo, UserInfo

# Import from Level 2 (Core API)
from ..models import CoreResponse


class CommentsResponse(CoreResponse):
    """Response wrapper for comments operations."""
    entry: BaseEntry = Field(..., description="Comments data")


class CommentsListResponse(BaseModel):
    """Response wrapper for comments list operations."""
    model_config = ConfigDict(extra='forbid')
    
    list: Dict[str, Any] = Field(..., description="List data with pagination")


# Operation-specific models will be added here based on analysis
# Example models for common patterns:


class CreateCommentsRequest(BaseModel):
    """Request model for creating comments."""
    model_config = ConfigDict(extra='forbid')
    
    name: Annotated[str, Field(
        description="Comments name",
        min_length=1,
        max_length=255
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Custom properties",
        default=None
    )]


class UpdateCommentsRequest(BaseModel):
    """Request model for updating comments."""
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
    'CommentsResponse', 
    'CommentsListResponse',
    'CreateCommentsRequest',
    'UpdateCommentsRequest'
]