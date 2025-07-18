"""
Level 3: Networks Operation Models - Specific to Networks Operations

This module contains models that are specific to networks operations
within the Core API.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs  
- Level 2: Core API models shared within Core API
- Level 3 (This file): Networks operation-specific models

Benefits:
- Perfect locality (networks models exactly where networks operations are)
- Clean imports (from .models import NetworksResponse)
- Logical organization (operation-specific grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

# Import from Level 1 (global)
from ...models import BaseEntry, ContentInfo, UserInfo

# Import from Level 2 (Core API)
from ..models import CoreResponse


class NetworksResponse(CoreResponse):
    """Response wrapper for networks operations."""
    entry: BaseEntry = Field(..., description="Networks data")


class NetworksListResponse(BaseModel):
    """Response wrapper for networks list operations."""
    model_config = ConfigDict(extra='forbid')
    
    list: Dict[str, Any] = Field(..., description="List data with pagination")


# Operation-specific models will be added here based on analysis
# Example models for common patterns:


class CreateNetworksRequest(BaseModel):
    """Request model for creating networks."""
    model_config = ConfigDict(extra='forbid')
    
    name: Annotated[str, Field(
        description="Networks name",
        min_length=1,
        max_length=255
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Custom properties",
        default=None
    )]


class UpdateNetworksRequest(BaseModel):
    """Request model for updating networks."""
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
    'NetworksResponse', 
    'NetworksListResponse',
    'CreateNetworksRequest',
    'UpdateNetworksRequest'
]