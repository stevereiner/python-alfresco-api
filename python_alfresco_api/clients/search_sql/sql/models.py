"""
Level 3: Sql Operation Models - Specific to Sql Operations

This module contains models that are specific to sql operations
within the SearchSql API.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs  
- Level 2: SearchSql API models shared within SearchSql API
- Level 3 (This file): Sql operation-specific models

Benefits:
- Perfect locality (sql models exactly where sql operations are)
- Clean imports (from .models import SqlResponse)
- Logical organization (operation-specific grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

# Import from Level 1 (global)
from ...models import BaseEntry, ContentInfo, UserInfo

# Import from Level 2 (SearchSql API)
from ..models import SearchSqlResponse


class SqlResponse(SearchSqlResponse):
    """Response wrapper for sql operations."""
    entry: BaseEntry = Field(..., description="Sql data")


class SqlListResponse(BaseModel):
    """Response wrapper for sql list operations."""
    model_config = ConfigDict(extra='forbid')
    
    list: Dict[str, Any] = Field(..., description="List data with pagination")


class CreateSqlRequest(BaseModel):
    """Request model for creating sql."""
    model_config = ConfigDict(extra='forbid')
    
    name: Annotated[str, Field(
        description="Sql name",
        min_length=1,
        max_length=255
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Custom properties",
        default=None
    )]


class UpdateSqlRequest(BaseModel):
    """Request model for updating sql."""
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
    'SqlResponse', 
    'SqlListResponse',
    'CreateSqlRequest',
    'UpdateSqlRequest'
]