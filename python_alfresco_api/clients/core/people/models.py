"""
Level 3: People Operation Models - Specific to People Operations

This module contains models that are specific to people operations
within the Core API.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs  
- Level 2: Core API models shared within Core API
- Level 3 (This file): People operation-specific models

Benefits:
- Perfect locality (people models exactly where people operations are)
- Clean imports (from .models import PeopleResponse)
- Logical organization (operation-specific grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

# Import from Level 1 (global)
from ...models import BaseEntry, ContentInfo, UserInfo

# Import from Level 2 (Core API)
from ..models import CoreResponse


class PeopleResponse(CoreResponse):
    """Response wrapper for people operations."""
    entry: BaseEntry = Field(..., description="People data")


class PeopleListResponse(BaseModel):
    """Response wrapper for people list operations."""
    model_config = ConfigDict(extra='forbid')
    
    list: Dict[str, Any] = Field(..., description="List data with pagination")


# Operation-specific models will be added here based on analysis
# Example models for common patterns:


class CreatePeopleRequest(BaseModel):
    """Request model for creating people."""
    model_config = ConfigDict(extra='forbid')
    
    name: Annotated[str, Field(
        description="People name",
        min_length=1,
        max_length=255
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Custom properties",
        default=None
    )]


class UpdatePeopleRequest(BaseModel):
    """Request model for updating people."""
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
    'PeopleResponse', 
    'PeopleListResponse',
    'CreatePeopleRequest',
    'UpdatePeopleRequest'
]