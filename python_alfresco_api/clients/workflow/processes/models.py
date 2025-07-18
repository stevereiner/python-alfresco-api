"""
Level 3: Processes Operation Models - Specific to Processes Operations

This module contains models that are specific to processes operations
within the Workflow API.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs  
- Level 2: Workflow API models shared within Workflow API
- Level 3 (This file): Processes operation-specific models

Benefits:
- Perfect locality (processes models exactly where processes operations are)
- Clean imports (from .models import ProcessesResponse)
- Logical organization (operation-specific grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

# Import from Level 1 (global)
from ...models import BaseEntry, ContentInfo, UserInfo

# Import from Level 2 (Workflow API)
from ..models import WorkflowResponse


class ProcessesResponse(WorkflowResponse):
    """Response wrapper for processes operations."""
    entry: BaseEntry = Field(..., description="Processes data")


class ProcessesListResponse(BaseModel):
    """Response wrapper for processes list operations."""
    model_config = ConfigDict(extra='forbid')
    
    list: Dict[str, Any] = Field(..., description="List data with pagination")


class CreateProcessesRequest(BaseModel):
    """Request model for creating processes."""
    model_config = ConfigDict(extra='forbid')
    
    name: Annotated[str, Field(
        description="Processes name",
        min_length=1,
        max_length=255
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Custom properties",
        default=None
    )]


class UpdateProcessesRequest(BaseModel):
    """Request model for updating processes."""
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
    'ProcessesResponse', 
    'ProcessesListResponse',
    'CreateProcessesRequest',
    'UpdateProcessesRequest'
]