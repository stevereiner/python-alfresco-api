"""
Level 3: ProcessDefinitions Operation Models - Specific to ProcessDefinitions Operations

This module contains models that are specific to process_definitions operations
within the Workflow API.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs  
- Level 2: Workflow API models shared within Workflow API
- Level 3 (This file): ProcessDefinitions operation-specific models

Benefits:
- Perfect locality (process_definitions models exactly where process_definitions operations are)
- Clean imports (from .models import ProcessDefinitionsResponse)
- Logical organization (operation-specific grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

# Import from Level 1 (global)
from ...models import BaseEntry, ContentInfo, UserInfo

# Import from Level 2 (Workflow API)
from ..models import WorkflowResponse


class ProcessDefinitionsResponse(WorkflowResponse):
    """Response wrapper for process_definitions operations."""
    entry: BaseEntry = Field(..., description="ProcessDefinitions data")


class ProcessDefinitionsListResponse(BaseModel):
    """Response wrapper for process_definitions list operations."""
    model_config = ConfigDict(extra='forbid')
    
    list: Dict[str, Any] = Field(..., description="List data with pagination")


class CreateProcessDefinitionsRequest(BaseModel):
    """Request model for creating process_definitions."""
    model_config = ConfigDict(extra='forbid')
    
    name: Annotated[str, Field(
        description="ProcessDefinitions name",
        min_length=1,
        max_length=255
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Custom properties",
        default=None
    )]


class UpdateProcessDefinitionsRequest(BaseModel):
    """Request model for updating process_definitions."""
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
    'ProcessDefinitionsResponse', 
    'ProcessDefinitionsListResponse',
    'CreateProcessDefinitionsRequest',
    'UpdateProcessDefinitionsRequest'
]