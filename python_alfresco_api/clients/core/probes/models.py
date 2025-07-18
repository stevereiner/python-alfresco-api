"""
Level 3: Probes Operation Models - Specific to Probes Operations

This module contains models that are specific to probes operations
within the Core API.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs  
- Level 2: Core API models shared within Core API
- Level 3 (This file): Probes operation-specific models

Benefits:
- Perfect locality (probes models exactly where probes operations are)
- Clean imports (from .models import ProbesResponse)
- Logical organization (operation-specific grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

# Import from Level 1 (global)
from ...models import BaseEntry, ContentInfo, UserInfo

# Import from Level 2 (Core API)
from ..models import CoreResponse


class ProbesResponse(CoreResponse):
    """Response wrapper for probes operations."""
    entry: BaseEntry = Field(..., description="Probes data")


class ProbesListResponse(BaseModel):
    """Response wrapper for probes list operations."""
    model_config = ConfigDict(extra='forbid')
    
    list: Dict[str, Any] = Field(..., description="List data with pagination")


# Operation-specific models will be added here based on analysis
# Example models for common patterns:


class CreateProbesRequest(BaseModel):
    """Request model for creating probes."""
    model_config = ConfigDict(extra='forbid')
    
    name: Annotated[str, Field(
        description="Probes name",
        min_length=1,
        max_length=255
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Custom properties",
        default=None
    )]


class UpdateProbesRequest(BaseModel):
    """Request model for updating probes."""
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
    'ProbesResponse', 
    'ProbesListResponse',
    'CreateProbesRequest',
    'UpdateProbesRequest'
]