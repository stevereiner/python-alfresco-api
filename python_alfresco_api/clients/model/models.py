"""
Level 2: Model API Models - Shared within Model API

This module contains models and structures that are specific to the
Alfresco Model API but shared across multiple Model operations.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs
- Level 2 (This file): Model API models shared within Model API  
- Level 3: Operation-specific models for specific Model operations

Benefits:
- Perfect locality (Model-specific models in Model namespace)
- Clean imports (from .models import ModelResponse)
- Logical organization (API-level grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from pydantic import BaseModel, Field, ConfigDict
from enum import Enum

# Import global models
from ..models import BaseEntry, PagingInfo


class ModelResponse(BaseModel):
    """Base response wrapper for Model API operations."""
    model_config = ConfigDict(extra='forbid')
    
    entries: List[BaseEntry] = Field(default_factory=list, description="Model result entries")
    pagination: Optional[PagingInfo] = Field(None, description="Pagination information")


class ModelRequest(BaseModel):
    """Base request model for Model operations."""
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
    'ModelResponse', 'ModelRequest'
]