"""
Level 3: Groups Operation Models - Specific to Groups Operations

This module contains models that are specific to groups operations
within the Core API.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs  
- Level 2: Core API models shared within Core API
- Level 3 (This file): Groups operation-specific models

Benefits:
- Perfect locality (groups models exactly where groups operations are)
- Clean imports (from .models import GroupsResponse)
- Logical organization (operation-specific grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

# Import from Level 1 (global)
from ...models import BaseEntry, ContentInfo, UserInfo

# Import from Level 2 (Core API)
from ..models import CoreResponse


class GroupsResponse(CoreResponse):
    """Response wrapper for groups operations."""
    entry: BaseEntry = Field(..., description="Groups data")


class GroupsListResponse(BaseModel):
    """Response wrapper for groups list operations."""
    model_config = ConfigDict(extra='forbid')
    
    list: Dict[str, Any] = Field(..., description="List data with pagination")


# Operation-specific models will be added here based on analysis
# Example models for common patterns:


class CreateGroupsRequest(BaseModel):
    """Request model for creating groups."""
    model_config = ConfigDict(extra='forbid')
    
    name: Annotated[str, Field(
        description="Groups name",
        min_length=1,
        max_length=255
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Custom properties",
        default=None
    )]


class UpdateGroupsRequest(BaseModel):
    """Request model for updating groups."""
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
    'GroupsResponse', 
    'GroupsListResponse',
    'CreateGroupsRequest',
    'UpdateGroupsRequest'
]