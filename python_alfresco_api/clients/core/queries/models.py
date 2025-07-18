"""
Level 3: Queries Operation Models - Specific to Queries Operations

This module contains models that are specific to queries operations
within the Core API.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs  
- Level 2: Core API models shared within Core API
- Level 3 (This file): Queries operation-specific models

Benefits:
- Perfect locality (queries models exactly where queries operations are)
- Clean imports (from .models import QueriesResponse)
- Logical organization (operation-specific grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

# Import from Level 1 (global)
from ...models import BaseEntry, ContentInfo, UserInfo

# Import from Level 2 (Core API)
from ..models import CoreResponse


class QueriesResponse(CoreResponse):
    """Response wrapper for queries operations."""
    entry: BaseEntry = Field(..., description="Queries data")


class QueriesListResponse(BaseModel):
    """Response wrapper for queries list operations."""
    model_config = ConfigDict(extra='forbid')
    
    list: Dict[str, Any] = Field(..., description="List data with pagination")


# Operation-specific models will be added here based on analysis
# Example models for common patterns:


class CreateQueriesRequest(BaseModel):
    """Request model for creating queries."""
    model_config = ConfigDict(extra='forbid')
    
    name: Annotated[str, Field(
        description="Queries name",
        min_length=1,
        max_length=255
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Custom properties",
        default=None
    )]


class UpdateQueriesRequest(BaseModel):
    """Request model for updating queries."""
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
    'QueriesResponse', 
    'QueriesListResponse',
    'CreateQueriesRequest',
    'UpdateQueriesRequest'
]