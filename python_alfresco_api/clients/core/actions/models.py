"""
Level 3: Actions Operation Models - Specific to Actions Operations

This module contains models that are specific to actions operations
within the Core API.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs  
- Level 2: Core API models shared within Core API
- Level 3 (This file): Actions operation-specific models

Benefits:
- Perfect locality (actions models exactly where actions operations are)
- Clean imports (from .models import ActionsResponse)
- Logical organization (operation-specific grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

# Import from Level 1 (global)
from ...models import BaseEntry, ContentInfo, UserInfo

# Import from Level 2 (Core API)
from ..models import CoreResponse


class ActionsResponse(CoreResponse):
    """Response wrapper for actions operations."""
    entry: BaseEntry = Field(..., description="Actions data")


class ActionsListResponse(BaseModel):
    """Response wrapper for actions list operations."""
    model_config = ConfigDict(extra='forbid')
    
    list: Dict[str, Any] = Field(..., description="List data with pagination")


# Operation-specific models will be added here based on analysis
# Example models for common patterns:


class CreateActionsRequest(BaseModel):
    """Request model for creating actions."""
    model_config = ConfigDict(extra='forbid')
    
    name: Annotated[str, Field(
        description="Actions name",
        min_length=1,
        max_length=255
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Custom properties",
        default=None
    )]


class UpdateActionsRequest(BaseModel):
    """Request model for updating actions."""
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
    'ActionsResponse', 
    'ActionsListResponse',
    'CreateActionsRequest',
    'UpdateActionsRequest'
]