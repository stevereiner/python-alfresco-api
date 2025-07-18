"""
Level 3: Sites Operation Models - Specific to Sites Operations

This module contains models that are specific to sites operations
within the Core API.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs  
- Level 2: Core API models shared within Core API
- Level 3 (This file): Sites operation-specific models

Benefits:
- Perfect locality (sites models exactly where sites operations are)
- Clean imports (from .models import SitesResponse)
- Logical organization (operation-specific grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

# Import from Level 1 (global)
from ...models import BaseEntry, ContentInfo, UserInfo

# Import from Level 2 (Core API)
from ..models import CoreResponse


class SitesResponse(CoreResponse):
    """Response wrapper for sites operations."""
    entry: BaseEntry = Field(..., description="Sites data")


class SitesListResponse(BaseModel):
    """Response wrapper for sites list operations."""
    model_config = ConfigDict(extra='forbid')
    
    list: Dict[str, Any] = Field(..., description="List data with pagination")


# Operation-specific models will be added here based on analysis
# Example models for common patterns:


class CreateSitesRequest(BaseModel):
    """Request model for creating sites."""
    model_config = ConfigDict(extra='forbid')
    
    name: Annotated[str, Field(
        description="Sites name",
        min_length=1,
        max_length=255
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Custom properties",
        default=None
    )]


class UpdateSitesRequest(BaseModel):
    """Request model for updating sites."""
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
    'SitesResponse', 
    'SitesListResponse',
    'CreateSitesRequest',
    'UpdateSitesRequest'
]