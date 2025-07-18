"""
Level 3: Authentication Operation Models - Specific to Authentication Operations

This module contains models that are specific to authentication operations
within the Auth API.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs  
- Level 2: Auth API models shared within Auth API
- Level 3 (This file): Authentication operation-specific models

Benefits:
- Perfect locality (authentication models exactly where authentication operations are)
- Clean imports (from .models import AuthenticationResponse)
- Logical organization (operation-specific grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

# Import from Level 1 (global)
from ...models import BaseEntry, ContentInfo, UserInfo

# Import from Level 2 (Auth API)
from ..models import AuthResponse


class AuthenticationResponse(AuthResponse):
    """Response wrapper for authentication operations."""
    entry: BaseEntry = Field(..., description="Authentication data")


class AuthenticationListResponse(BaseModel):
    """Response wrapper for authentication list operations."""
    model_config = ConfigDict(extra='forbid')
    
    list: Dict[str, Any] = Field(..., description="List data with pagination")


class CreateAuthenticationRequest(BaseModel):
    """Request model for creating authentication."""
    model_config = ConfigDict(extra='forbid')
    
    name: Annotated[str, Field(
        description="Authentication name",
        min_length=1,
        max_length=255
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Custom properties",
        default=None
    )]


class UpdateAuthenticationRequest(BaseModel):
    """Request model for updating authentication."""
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
    'AuthenticationResponse', 
    'AuthenticationListResponse',
    'CreateAuthenticationRequest',
    'UpdateAuthenticationRequest'
]