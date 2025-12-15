"""
Level 2: Core API Models - Shared within Core API

This module contains models and structures that are specific to the
Alfresco Core API but shared across multiple Core operations.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs
- Level 2 (This file): Core API models shared within Core API
- Level 3: Operation-specific models for specific operations

Benefits:
- Perfect locality (Core-specific models in Core namespace)
- Clean imports (from .models import CoreResponse)
- Logical organization (API-level grouping)
- Maintainability (focused scope)
"""

from typing import Optional, List, Dict, Any, Union
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from enum import Enum

# Import global models
from ..models import BaseEntry, PagingInfo, ContentInfo, UserInfo


class CoreResponse(BaseModel):
    """Base response wrapper for Core API operations."""
    model_config = ConfigDict(extra='forbid')
    
    entry: Optional[BaseEntry] = Field(None, description="Single entry response")
    
    
class CoreEntryList(BaseModel):
    """List response wrapper for Core API operations."""
    model_config = ConfigDict(extra='forbid')
    
    entries: List[BaseEntry] = Field(default_factory=list, description="List of entries")
    pagination: Optional[PagingInfo] = Field(None, description="Pagination information")


class Permission(str, Enum):
    """Alfresco permission levels for Core API."""
    READ = "Read"
    WRITE = "Write" 
    DELETE = "Delete"
    CHANGE_PERMISSIONS = "ChangePermissions"
    FULL_CONTROL = "FullControl"
    COORDINATOR = "SiteCoordinator"
    COLLABORATOR = "SiteCollaborator"
    CONTRIBUTOR = "SiteContributor"
    CONSUMER = "SiteConsumer"


class NodeType:
    """
    Alfresco content model node types.
    
    This class provides constants for common node types while allowing
    custom types (e.g., 'my:customDocument', 'acme:invoice').
    
    Use as a namespace for common types:
        NodeType.CONTENT  # "cm:content"
        NodeType.FOLDER   # "cm:folder"
    
    Or use any custom string directly:
        node_type = "my:customDocument"  # Works with custom content models
    """
    CONTENT = "cm:content"
    FOLDER = "cm:folder"
    PERSON = "cm:person"
    GROUP = "cm:authorityContainer"
    SITE = "st:site"
    
    # Common custom types (for reference)
    # Users can use any string value for their custom types
    

class VersionType(str, Enum):
    """Version types for Core API operations."""
    MAJOR = "MAJOR"
    MINOR = "MINOR"


class SortOrder(str, Enum):
    """Sort order options."""
    ASC = "ASC"
    DESC = "DESC"


class IncludeOption(str, Enum):
    """Include options for Core API requests."""
    PROPERTIES = "properties"
    PERMISSIONS = "permissions"
    PATH = "path"
    CHILDREN = "children"
    ASSOCIATION = "association"
    ASPECTS = "aspects"
    IS_LINK = "isLink"
    IS_LOCKED = "isLocked"
    ALLOW_ABLE_OPERATIONS = "allowableOperations"


class CorePermissionInfo(BaseModel):
    """Permission information for Core API objects."""
    model_config = ConfigDict(extra='forbid')
    
    authority_id: str = Field(..., description="Authority (user/group) identifier")
    authority_type: str = Field(..., description="Type of authority (USER, GROUP)")
    permission: Permission = Field(..., description="Permission level")
    access_status: str = Field(..., description="Access status (ALLOWED, DENIED)")


class CoreAspectInfo(BaseModel):
    """Aspect information for Core API objects."""
    model_config = ConfigDict(extra='forbid')
    
    aspect_name: str = Field(..., description="Aspect name (e.g., cm:titled)")
    title: Optional[str] = Field(None, description="Aspect title") 
    description: Optional[str] = Field(None, description="Aspect description")


class CorePathElement(BaseModel):
    """Path element for Core API path structures."""
    model_config = ConfigDict(extra='allow')  # Allow extra fields from Alfresco
    
    id: str = Field(..., description="Node ID")
    name: str = Field(..., description="Node name")
    node_type: Optional[str] = Field(None, alias="nodeType", description="Node type")
    aspect_names: Optional[List[str]] = Field(None, alias="aspectNames", description="Aspect names")


class CorePathInfo(BaseModel):
    """Path information for Core API objects."""
    model_config = ConfigDict(extra='allow')  # Allow extra fields from Alfresco
    
    elements: List[CorePathElement] = Field(default_factory=list, description="Path elements")
    name: Optional[str] = Field(None, description="Display name")
    is_complete: Optional[bool] = Field(None, alias="isComplete", description="Whether path is complete")


# Export all models
__all__ = [
    'CoreResponse', 'CoreEntryList', 'Permission', 'NodeType', 'VersionType',
    'SortOrder', 'IncludeOption', 'CorePermissionInfo', 'CoreAspectInfo', 
    'CorePathElement', 'CorePathInfo'
] 