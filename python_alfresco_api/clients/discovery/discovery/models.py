"""
Level 3: Discovery Operation Models - Specific to Discovery Operations

This module contains models that are specific to discovery operations
within the Discovery API.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs  
- Level 2: Discovery API models shared within Discovery API
- Level 3 (This file): Discovery operation-specific models

Benefits:
- Perfect locality (discovery models exactly where discovery operations are)
- Clean imports (from .models import DiscoveryResponse)
- Logical organization (operation-specific grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

# Import from Level 1 (global)
from ...models import BaseEntry, ContentInfo, UserInfo

# Import from Level 2 (Discovery API)
from ..models import DiscoveryResponse


class DiscoveryResponse(DiscoveryResponse):
    """Response wrapper for discovery operations."""
    entry: BaseEntry = Field(..., description="Discovery data")


class DiscoveryListResponse(BaseModel):
    """Response wrapper for discovery list operations."""
    model_config = ConfigDict(extra='forbid')
    
    list: Dict[str, Any] = Field(..., description="List data with pagination")


class CreateDiscoveryRequest(BaseModel):
    """Request model for creating discovery."""
    model_config = ConfigDict(extra='forbid')
    
    name: Annotated[str, Field(
        description="Discovery name",
        min_length=1,
        max_length=255
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Custom properties",
        default=None
    )]


class UpdateDiscoveryRequest(BaseModel):
    """Request model for updating discovery."""
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
    'DiscoveryResponse', 
    'DiscoveryListResponse',
    'CreateDiscoveryRequest',
    'UpdateDiscoveryRequest'
]