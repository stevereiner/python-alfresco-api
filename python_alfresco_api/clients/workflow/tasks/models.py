"""
Level 3: Tasks Operation Models - Specific to Tasks Operations

This module contains models that are specific to tasks operations
within the Workflow API.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs  
- Level 2: Workflow API models shared within Workflow API
- Level 3 (This file): Tasks operation-specific models

Benefits:
- Perfect locality (tasks models exactly where tasks operations are)
- Clean imports (from .models import TasksResponse)
- Logical organization (operation-specific grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

# Import from Level 1 (global)
from ...models import BaseEntry, ContentInfo, UserInfo

# Import from Level 2 (Workflow API)
from ..models import WorkflowResponse


class TasksResponse(WorkflowResponse):
    """Response wrapper for tasks operations."""
    entry: BaseEntry = Field(..., description="Tasks data")


class TasksListResponse(BaseModel):
    """Response wrapper for tasks list operations."""
    model_config = ConfigDict(extra='forbid')
    
    list: Dict[str, Any] = Field(..., description="List data with pagination")


class CreateTasksRequest(BaseModel):
    """Request model for creating tasks."""
    model_config = ConfigDict(extra='forbid')
    
    name: Annotated[str, Field(
        description="Tasks name",
        min_length=1,
        max_length=255
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Custom properties",
        default=None
    )]


class UpdateTasksRequest(BaseModel):
    """Request model for updating tasks."""
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
    'TasksResponse', 
    'TasksListResponse',
    'CreateTasksRequest',
    'UpdateTasksRequest'
]