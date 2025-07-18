"""
Level 2: Discovery API Models - Shared within Discovery API

This module contains models and structures that are specific to the
Alfresco Discovery API but shared across multiple Discovery operations.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs
- Level 2 (This file): Discovery API models shared within Discovery API  
- Level 3: Operation-specific models for specific Discovery operations

Benefits:
- Perfect locality (Discovery-specific models in Discovery namespace)
- Clean imports (from .models import DiscoveryResponse)
- Logical organization (API-level grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from pydantic import BaseModel, Field, ConfigDict
from enum import Enum

# Import global models
from ..models import BaseEntry, PagingInfo


class DiscoveryResponse(BaseModel):
    """Base response wrapper for Discovery API operations."""
    model_config = ConfigDict(extra='forbid')
    
    entries: List[BaseEntry] = Field(default_factory=list, description="Discovery result entries")
    pagination: Optional[PagingInfo] = Field(None, description="Pagination information")


class DiscoveryRequest(BaseModel):
    """Base request model for Discovery operations."""
    model_config = ConfigDict(extra='forbid')
    
    max_items: Annotated[int, Field(
        description="Maximum number of results to return",
        default=100,
        ge=1,
        le=1000
    )]
    
    skip_count: Annotated[int, Field(
        description="Number of results to skip for pagination",
        default=0,
        ge=0
    )]


# Export all models
__all__ = [
    'DiscoveryResponse', 'DiscoveryRequest'
]