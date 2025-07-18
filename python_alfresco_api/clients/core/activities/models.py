"""
Level 3: Activities Operation Models - Specific to Activities Operations

This module contains models that are specific to activities operations
within the Core API.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs  
- Level 2: Core API models shared within Core API
- Level 3 (This file): Activities operation-specific models

Benefits:
- Perfect locality (activities models exactly where activities operations are)
- Clean imports (from .models import ActivitiesResponse)
- Logical organization (operation-specific grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

# Import from Level 1 (global)
from ...models import BaseEntry, ContentInfo, UserInfo

# Import from Level 2 (Core API)
from ..models import CoreResponse


class ActivitiesResponse(CoreResponse):
    """Response wrapper for activities operations."""
    entry: BaseEntry = Field(..., description="Activities data")


class ActivitiesListResponse(BaseModel):
    """Response wrapper for activities list operations."""
    model_config = ConfigDict(extra='forbid')
    
    list: Dict[str, Any] = Field(..., description="List data with pagination")


# Operation-specific models will be added here based on analysis
# Example models for common patterns:


class CreateActivitiesRequest(BaseModel):
    """Request model for creating activities."""
    model_config = ConfigDict(extra='forbid')
    
    name: Annotated[str, Field(
        description="Activities name",
        min_length=1,
        max_length=255
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Custom properties",
        default=None
    )]


class UpdateActivitiesRequest(BaseModel):
    """Request model for updating activities."""
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
    'ActivitiesResponse', 
    'ActivitiesListResponse',
    'CreateActivitiesRequest',
    'UpdateActivitiesRequest'
]