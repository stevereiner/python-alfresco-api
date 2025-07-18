"""
Level 3: Favorites Operation Models - Specific to Favorites Operations

This module contains models that are specific to favorites operations
within the Core API.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs  
- Level 2: Core API models shared within Core API
- Level 3 (This file): Favorites operation-specific models

Benefits:
- Perfect locality (favorites models exactly where favorites operations are)
- Clean imports (from .models import FavoritesResponse)
- Logical organization (operation-specific grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

# Import from Level 1 (global)
from ...models import BaseEntry, ContentInfo, UserInfo

# Import from Level 2 (Core API)
from ..models import CoreResponse


class FavoritesResponse(CoreResponse):
    """Response wrapper for favorites operations."""
    entry: BaseEntry = Field(..., description="Favorites data")


class FavoritesListResponse(BaseModel):
    """Response wrapper for favorites list operations."""
    model_config = ConfigDict(extra='forbid')
    
    list: Dict[str, Any] = Field(..., description="List data with pagination")


# Operation-specific models will be added here based on analysis
# Example models for common patterns:


class CreateFavoritesRequest(BaseModel):
    """Request model for creating favorites."""
    model_config = ConfigDict(extra='forbid')
    
    name: Annotated[str, Field(
        description="Favorites name",
        min_length=1,
        max_length=255
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Custom properties",
        default=None
    )]


class UpdateFavoritesRequest(BaseModel):
    """Request model for updating favorites."""
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
    'FavoritesResponse', 
    'FavoritesListResponse',
    'CreateFavoritesRequest',
    'UpdateFavoritesRequest'
]