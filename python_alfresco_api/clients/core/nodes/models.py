"""
Level 3: Node Operation Models - Specific to Node Operations

This module contains models that are specific to node operations
(get, create, update, delete nodes) within the Core API.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs  
- Level 2: Core API models shared within Core API
- Level 3 (This file): Node operation-specific models

Benefits:
- Perfect locality (node models exactly where node operations are)
- Clean imports (from .models import NodeResponse)
- Logical organization (operation-specific grouping)
- Maintainability (focused, small files)
- Scalability (easy to add without affecting other operations)
"""

from typing import Optional, List, Dict, Any, Union, Annotated
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

# Import from Level 1 (global)
from ...models import BaseEntry, ContentInfo, UserInfo

# Import from Level 2 (Core API)
from ..models import (
    Permission, NodeType, IncludeOption, CorePermissionInfo, 
    CoreAspectInfo, CorePathInfo
)


class Node(BaseEntry):
    """
    Comprehensive node model with rich metadata.
    
    Represents any node in the Alfresco repository including files,
    folders, and other content types with full metadata support.
    """
    model_config = ConfigDict(extra='allow', validate_assignment=True)  # Allow extra fields from Alfresco
    
    name: Annotated[str, Field(
        description="Node display name (filename or folder name)",
        examples=["report.pdf", "Documents", "Annual Report 2024.docx"],
        max_length=255,
        min_length=1
    )]
    
    node_type: Annotated[str, Field(
        alias="nodeType",
        description="Alfresco content model type (e.g., 'cm:content', 'cm:folder', or custom types like 'my:customDocument')",
        examples=[NodeType.CONTENT, NodeType.FOLDER, "my:customDocument", "acme:invoice"]
    )]
    
    is_file: Annotated[bool, Field(
        alias="isFile",
        description="True if this is a file, False if folder"
    )]
    
    is_folder: Annotated[bool, Field(
        alias="isFolder",
        description="True if this is a folder, False if file"
    )]
    
    created_at: Annotated[datetime, Field(
        alias="createdAt",
        description="Creation timestamp",
        examples=["2024-01-15T10:30:00.000Z"]
    )]
    
    modified_at: Annotated[datetime, Field(
        alias="modifiedAt",
        description="Last modification timestamp", 
        examples=["2024-01-20T14:45:30.000Z"]
    )]
    
    created_by_user: Annotated[Optional[UserInfo], Field(
        alias="createdByUser",
        description="User who created this node",
        default=None
    )]
    
    modified_by_user: Annotated[Optional[UserInfo], Field(
        alias="modifiedByUser",
        description="User who last modified this node",
        default=None
    )]
    
    content: Annotated[Optional[ContentInfo], Field(
        description="Content information (for files)",
        default=None
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Custom properties and metadata",
        examples=[{
            "cm:title": "Annual Report",
            "cm:description": "Company annual financial report",
            "cm:author": "Finance Team"
        }],
        default=None
    )]
    
    parent_id: Annotated[Optional[str], Field(
        alias="parentId",
        description="Parent folder node ID",
        examples=["abc123-parent-456"],
        default=None
    )]
    
    path: Annotated[Optional[CorePathInfo], Field(
        description="Full repository path information",
        default=None
    )]
    
    permissions: Annotated[Optional[List[CorePermissionInfo]], Field(
        description="Permission information for this node",
        default=None
    )]
    
    aspects: Annotated[Optional[List[str]], Field(
        alias="aspectNames",
        description="Aspect names applied to this node",
        examples=[["cm:titled", "cm:auditable", "app:uifacets"]],
        default=None
    )]
    
    allowable_operations: Annotated[Optional[List[str]], Field(
        alias="allowableOperations",
        description="Operations allowed on this node",
        examples=[["create", "update", "delete"]],
        default=None
    )]
    
    is_locked: Annotated[Optional[bool], Field(
        alias="isLocked",
        description="Whether this node is locked",
        default=None
    )]


class NodeResponse(BaseModel):
    """Response wrapper for single node operations."""
    model_config = ConfigDict(extra='allow')  # Allow extra fields from Alfresco
    
    entry: Node = Field(..., description="Node data")


class NodeListResponse(BaseModel):
    """Response wrapper for node list operations."""
    model_config = ConfigDict(extra='allow')  # Allow extra fields from Alfresco
    
    list: Dict[str, Any] = Field(..., description="List data with pagination")


class CreateNodeRequest(BaseModel):
    """Request model for creating new nodes with validation."""
    model_config = ConfigDict(extra='forbid')
    
    name: Annotated[str, Field(
        description="Node name - will be used as filename or folder name",
        min_length=1,
        max_length=255,
        pattern=r"^[^<>:\"/\\|?*\x00-\x1f]+$",
        examples=["report.pdf", "My Folder", "data-2024.xlsx"]
    )]
    
    node_type: Annotated[str, Field(
        description="Alfresco content model type (e.g., 'cm:content', 'cm:folder', or custom types like 'my:customDocument')",
        examples=[NodeType.CONTENT, NodeType.FOLDER, "my:customDocument", "acme:invoice"],
        default=NodeType.CONTENT
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Custom properties and metadata to set on the node",
        examples=[{
            "cm:title": "Annual Report 2024",
            "cm:description": "Comprehensive annual financial report",
            "cm:author": "Finance Department"
        }],
        default=None
    )]
    
    auto_rename: Annotated[bool, Field(
        description="Automatically rename if name conflicts exist",
        default=True
    )]
    
    aspects: Annotated[Optional[List[str]], Field(
        description="Aspects to apply to the new node",
        examples=[["cm:titled", "cm:author"]],
        default=None
    )]
    
    versioning_enabled: Annotated[Optional[bool], Field(
        description="Enable versioning for the new node",
        examples=[True, False],
        default=None
    )]
    
    major_version: Annotated[Optional[bool], Field(
        description="Create as major version (true) or minor version (false)",
        examples=[True, False],
        default=None
    )]


class UpdateNodeRequest(BaseModel):
    """Request model for updating existing nodes."""
    model_config = ConfigDict(extra='forbid')
    
    name: Annotated[Optional[str], Field(
        description="New node name",
        min_length=1,
        max_length=255,
        pattern=r"^[^<>:\"/\\|?*\x00-\x1f]+$",
        default=None
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Properties to update",
        default=None
    )]


class CopyNodeRequest(BaseModel):
    """Request model for copying nodes."""
    model_config = ConfigDict(extra='forbid')
    
    target_parent_id: Annotated[str, Field(
        description="ID of the target parent folder",
        examples=["target-folder-123"]
    )]
    
    name: Annotated[Optional[str], Field(
        description="Name for the copied node (defaults to original name)",
        min_length=1,
        max_length=255,
        default=None
    )]


class MoveNodeRequest(BaseModel):
    """Request model for moving nodes."""
    model_config = ConfigDict(extra='forbid')
    
    target_parent_id: Annotated[str, Field(
        description="ID of the target parent folder",
        examples=["target-folder-123"]
    )]
    
    name: Annotated[Optional[str], Field(
        description="New name for the moved node (defaults to current name)",
        min_length=1,
        max_length=255,
        default=None
    )]


# Export all models
__all__ = [
    'Node', 'NodeResponse', 'NodeListResponse', 'CreateNodeRequest',
    'UpdateNodeRequest', 'CopyNodeRequest', 'MoveNodeRequest'
] 