"""
Level 2: Workflow API Models - Shared within Workflow API

This module contains models and structures that are specific to the
Alfresco Workflow API but shared across multiple Workflow operations.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs
- Level 2 (This file): Workflow API models shared within Workflow API  
- Level 3: Operation-specific models for specific Workflow operations

Benefits:
- Perfect locality (Workflow-specific models in Workflow namespace)
- Clean imports (from .models import WorkflowResponse)
- Logical organization (API-level grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from pydantic import BaseModel, Field, ConfigDict
from enum import Enum

# Import global models
from ..models import BaseEntry, PagingInfo


class WorkflowResponse(BaseModel):
    """Base response wrapper for Workflow API operations."""
    model_config = ConfigDict(extra='forbid')
    
    entries: List[BaseEntry] = Field(default_factory=list, description="Workflow result entries")
    pagination: Optional[PagingInfo] = Field(None, description="Pagination information")


class WorkflowRequest(BaseModel):
    """Base request model for Workflow operations."""
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
    'WorkflowResponse', 'WorkflowRequest'
]