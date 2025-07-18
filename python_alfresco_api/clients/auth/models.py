"""
Level 2: Auth API Models - Shared within Auth API

This module contains models and structures that are specific to the
Alfresco Auth API but shared across multiple Auth operations.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs
- Level 2 (This file): Auth API models shared within Auth API  
- Level 3: Operation-specific models for specific Auth operations

Benefits:
- Perfect locality (Auth-specific models in Auth namespace)
- Clean imports (from .models import AuthResponse)
- Logical organization (API-level grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from pydantic import BaseModel, Field, ConfigDict
from enum import Enum

# Import global models
from ..models import BaseEntry, PagingInfo


class AuthResponse(BaseModel):
    """Base response wrapper for Auth API operations."""
    model_config = ConfigDict(extra='forbid')
    
    entries: List[BaseEntry] = Field(default_factory=list, description="Auth result entries")
    pagination: Optional[PagingInfo] = Field(None, description="Pagination information")


class AuthRequest(BaseModel):
    """Base request model for Auth operations."""
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
    'AuthResponse', 'AuthRequest'
]