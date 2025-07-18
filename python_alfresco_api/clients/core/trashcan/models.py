"""
Level 3: Trashcan Operation Models - Specific to Trashcan Operations

This module contains models that are specific to trashcan operations
within the Core API.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs  
- Level 2: Core API models shared within Core API
- Level 3 (This file): Trashcan operation-specific models

Benefits:
- Perfect locality (trashcan models exactly where trashcan operations are)
- Clean imports (from .models import TrashcanResponse)
- Logical organization (operation-specific grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

# Import from Level 1 (global)
from ...models import BaseEntry, ContentInfo, UserInfo

# Import from Level 2 (Core API)
from ..models import CoreResponse


class TrashcanResponse(CoreResponse):
    """Response wrapper for trashcan operations."""
    entry: BaseEntry = Field(..., description="Trashcan data")


class TrashcanListResponse(BaseModel):
    """Response wrapper for trashcan list operations."""
    model_config = ConfigDict(extra='forbid')
    
    list: Dict[str, Any] = Field(..., description="List data with pagination")


# Operation-specific models will be added here based on analysis
# Example models for common patterns:


class CreateTrashcanRequest(BaseModel):
    """Request model for creating trashcan."""
    model_config = ConfigDict(extra='forbid')
    
    name: Annotated[str, Field(
        description="Trashcan name",
        min_length=1,
        max_length=255
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Custom properties",
        default=None
    )]


class UpdateTrashcanRequest(BaseModel):
    """Request model for updating trashcan."""
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
    'TrashcanResponse', 
    'TrashcanListResponse',
    'CreateTrashcanRequest',
    'UpdateTrashcanRequest'
]