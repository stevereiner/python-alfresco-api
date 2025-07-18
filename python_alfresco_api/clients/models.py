"""
Level 1: Global Models - Shared across ALL Alfresco APIs

This module contains base models and common structures that are used
across multiple Alfresco APIs (Core, Search, Discovery, etc.).

Three-Tier Architecture:
- Level 1 (This file): Global models shared across ALL APIs
- Level 2: API-specific models shared within ONE API  
- Level 3: Operation-specific models for ONE operation

Benefits:
- Perfect locality (models exactly where used)
- Clean imports (from .models import ResponseBase)
- Logical organization (three clear levels)
- Maintainability (focused files vs massive single files)
"""

from typing import Optional, List, Dict, Any, Union
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from enum import Enum


class BaseEntry(BaseModel):
    """Base entry model used across all Alfresco APIs."""
    model_config = ConfigDict(
        extra='forbid',
        validate_assignment=True,
        str_strip_whitespace=True
    )
    
    id: Optional[str] = Field(None, description="Unique identifier")
    

class PagingInfo(BaseModel):
    """Pagination information used across all APIs."""
    model_config = ConfigDict(extra='forbid')
    
    count: Optional[int] = Field(None, description="Number of items in this page")
    has_more_items: Optional[bool] = Field(None, description="Whether there are more items available")
    total_items: Optional[int] = Field(None, description="Total number of items available")
    skip_count: Optional[int] = Field(None, description="Number of items skipped")
    max_items: Optional[int] = Field(None, description="Maximum number of items per page")


class ErrorResponse(BaseModel):
    """Standard error response structure across all APIs."""
    model_config = ConfigDict(extra='forbid')
    
    error: "ErrorDetail" = Field(..., description="Error details")


class ErrorDetail(BaseModel):
    """Error detail information."""
    model_config = ConfigDict(extra='forbid')
    
    error_key: Optional[str] = Field(None, description="Error key for programmatic handling")
    status_code: Optional[int] = Field(None, description="HTTP status code")
    brief_summary: Optional[str] = Field(None, description="Brief error summary")
    stack_trace: Optional[str] = Field(None, description="Detailed stack trace")
    description_url: Optional[str] = Field(None, description="URL with more error information")


class RequestStatus(str, Enum):
    """Standard request status enumeration."""
    PENDING = "pending"
    IN_PROGRESS = "inProgress" 
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class ContentInfo(BaseModel):
    """Basic content information shared across APIs."""
    model_config = ConfigDict(extra='forbid')
    
    mime_type: Optional[str] = Field(
        alias="mimeType",
        default=None, 
        description="MIME type of the content"
    )
    mime_type_name: Optional[str] = Field(
        alias="mimeTypeName",
        default=None, 
        description="Human-readable MIME type name"
    )
    size_in_bytes: Optional[int] = Field(
        alias="sizeInBytes", 
        default=None, 
        description="Size of content in bytes"
    )
    encoding: Optional[str] = Field(None, description="Content encoding")


class UserInfo(BaseModel):
    """Basic user information shared across APIs."""
    model_config = ConfigDict(extra='forbid')
    
    id: str = Field(..., description="User identifier")
    display_name: Optional[str] = Field(
        alias="displayName",
        default=None, 
        description="User display name"
    )
    email: Optional[str] = Field(None, description="User email address")


# Forward reference resolution
ErrorResponse.model_rebuild()
