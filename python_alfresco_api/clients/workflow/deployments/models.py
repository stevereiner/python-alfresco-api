"""
Level 3: Deployments Operation Models - Specific to Deployments Operations

This module contains models that are specific to deployments operations
within the Workflow API.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs  
- Level 2: Workflow API models shared within Workflow API
- Level 3 (This file): Deployments operation-specific models

Benefits:
- Perfect locality (deployments models exactly where deployments operations are)
- Clean imports (from .models import DeploymentsResponse)
- Logical organization (operation-specific grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

# Import from Level 1 (global)
from ...models import BaseEntry, ContentInfo, UserInfo

# Import from Level 2 (Workflow API)
from ..models import WorkflowResponse


class DeploymentsResponse(WorkflowResponse):
    """Response wrapper for deployments operations."""
    entry: BaseEntry = Field(..., description="Deployments data")


class DeploymentsListResponse(BaseModel):
    """Response wrapper for deployments list operations."""
    model_config = ConfigDict(extra='forbid')
    
    list: Dict[str, Any] = Field(..., description="List data with pagination")


class CreateDeploymentsRequest(BaseModel):
    """Request model for creating deployments."""
    model_config = ConfigDict(extra='forbid')
    
    name: Annotated[str, Field(
        description="Deployments name",
        min_length=1,
        max_length=255
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Custom properties",
        default=None
    )]


class UpdateDeploymentsRequest(BaseModel):
    """Request model for updating deployments."""
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
    'DeploymentsResponse', 
    'DeploymentsListResponse',
    'CreateDeploymentsRequest',
    'UpdateDeploymentsRequest'
]