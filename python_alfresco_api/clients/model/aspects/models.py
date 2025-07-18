"""
Level 3: Aspects Operation Models - Specific to Aspects Operations

This module contains models that are specific to aspects operations
within the Model API.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs  
- Level 2: Model API models shared within Model API
- Level 3 (This file): Aspects operation-specific models

Benefits:
- Perfect locality (aspects models exactly where aspects operations are)
- Clean imports (from .models import AspectsResponse)
- Logical organization (operation-specific grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

# Import from Level 1 (global)
from ...models import BaseEntry, ContentInfo, UserInfo

# Import from Level 2 (Model API)
from ..models import ModelResponse


class AspectsResponse(ModelResponse):
    """Response wrapper for aspects operations."""
    entry: BaseEntry = Field(..., description="Aspects data")


class AspectsListResponse(BaseModel):
    """Response wrapper for aspects list operations."""
    model_config = ConfigDict(extra='forbid')
    
    list: Dict[str, Any] = Field(..., description="List data with pagination")


class CreateAspectsRequest(BaseModel):
    """Request model for creating aspects."""
    model_config = ConfigDict(extra='forbid')
    
    name: Annotated[str, Field(
        description="Aspects name",
        min_length=1,
        max_length=255
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Custom properties",
        default=None
    )]


class UpdateAspectsRequest(BaseModel):
    """Request model for updating aspects."""
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
    'AspectsResponse', 
    'AspectsListResponse',
    'CreateAspectsRequest',
    'UpdateAspectsRequest'
]