"""
Level 3: Versions Operation Models - Specific to Document Lifecycle Operations

This module contains models that are specific to version control operations
(checkout, checkin, cancel checkout) within the Core API.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs  
- Level 2: Core API models shared within Core API
- Level 3 (This file): Versions operation-specific models

Benefits:
- Perfect locality (version models exactly where version operations are)
- Clean imports (from .models import CheckoutResponse)
- Logical organization (operation-specific grouping)
"""

from typing import Optional, Annotated
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

# Import from Level 2 (Core API) 
from ..models import CoreResponse


class CheckoutResponse(BaseModel):
    """Response model for checkout/cancel checkout operations."""
    model_config = ConfigDict(extra='forbid')
    
    node_id: Annotated[str, Field(
        description="ID of the document that was checked out/unlocked"
    )]
    
    locked: Annotated[bool, Field(
        description="Whether the document is currently locked"
    )]
    
    working_copy_id: Annotated[Optional[str], Field(
        description="ID of the working copy (if checked out)",
        default=None
    )]
    
    locked_by: Annotated[Optional[str], Field(
        description="User who locked the document",
        default=None
    )]
    
    locked_at: Annotated[Optional[datetime], Field(
        description="When the document was locked",
        default=None
    )]


class CheckinResponse(BaseModel):
    """Response model for checkin operations.""" 
    model_config = ConfigDict(extra='forbid')
    
    node_id: Annotated[str, Field(
        description="ID of the document that was checked in"
    )]
    
    version_number: Annotated[str, Field(
        description="Version number of the new version",
        examples=["1.1", "2.0", "1.5"]
    )]
    
    comment: Annotated[str, Field(
        description="Version comment"
    )]
    
    major_version: Annotated[bool, Field(
        description="Whether this is a major version"
    )]
    
    created_at: Annotated[datetime, Field(
        description="When the version was created",
        default_factory=datetime.now
    )]
    
    created_by: Annotated[Optional[str], Field(
        description="User who created the version",
        default=None
    )]


class VersionInfo(BaseModel):
    """Version information model."""
    model_config = ConfigDict(extra='forbid')
    
    version_number: Annotated[str, Field(
        description="Version number",
        examples=["1.0", "1.1", "2.0"]
    )]
    
    comment: Annotated[Optional[str], Field(
        description="Version comment",
        default=None
    )]
    
    is_major: Annotated[bool, Field(
        description="Whether this is a major version"
    )]
    
    created_at: Annotated[datetime, Field(
        description="Version creation timestamp"
    )]
    
    created_by: Annotated[Optional[str], Field(
        description="User who created this version",
        default=None
    )]


# Export all models
__all__ = [
    'CheckoutResponse', 'CheckinResponse', 'VersionInfo'
] 