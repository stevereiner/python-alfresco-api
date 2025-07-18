"""
Level 3: Types Operation Models - Specific to Types Operations

This module contains models that are specific to types operations
within the Model API.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs  
- Level 2: Model API models shared within Model API
- Level 3 (This file): Types operation-specific models

Benefits:
- Perfect locality (types models exactly where types operations are)
- Clean imports (from .models import TypesResponse)
- Logical organization (operation-specific grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

# Import from Level 1 (global)
from ...models import BaseEntry, ContentInfo, UserInfo

# Import from Level 2 (Model API)
from ..models import ModelResponse


class TypesResponse(ModelResponse):
    """Response wrapper for types operations."""
    entry: BaseEntry = Field(..., description="Types data")


class TypesListResponse(BaseModel):
    """Response wrapper for types list operations."""
    model_config = ConfigDict(extra='forbid')
    
    list: Dict[str, Any] = Field(..., description="List data with pagination")


class CreateTypesRequest(BaseModel):
    """Request model for creating types."""
    model_config = ConfigDict(extra='forbid')
    
    name: Annotated[str, Field(
        description="Types name",
        min_length=1,
        max_length=255
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Custom properties",
        default=None
    )]


class UpdateTypesRequest(BaseModel):
    """Request model for updating types."""
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
    'TypesResponse', 
    'TypesListResponse',
    'CreateTypesRequest',
    'UpdateTypesRequest'
]