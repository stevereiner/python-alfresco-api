"""
Level 3: Content Operation Models - Specific to File Upload/Download Operations

This module contains models that are specific to content operations
(upload, download, update content) within the Core API.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs  
- Level 2: Core API models shared within Core API
- Level 3 (This file): Content operation-specific models

Benefits:
- Perfect locality (content models exactly where content operations are)
- Clean imports (from .models import UploadResponse)
- Logical organization (operation-specific grouping)
"""

from typing import Optional, Dict, Any, Union, Annotated
from pathlib import Path
from pydantic import BaseModel, Field, ConfigDict

# Import from Level 1 (global)
from ...models import BaseEntry

# Import from Level 2 (Core API) 
from ..models import CoreResponse

# Import from nodes models for reuse
from ..nodes.models import Node


class UploadRequest(BaseModel):
    """Request model for file upload operations."""
    model_config = ConfigDict(extra='forbid')
    
    file_name: Annotated[str, Field(
        description="Name for the uploaded file",
        examples=["report.pdf", "data.xlsx"]
    )]
    
    parent_id: Annotated[str, Field(
        description="Parent folder ID where to upload",
        examples=["-my-", "folder-abc123"],
        default="-my-"
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Custom properties to set on uploaded file",
        examples=[{"cm:title": "Annual Report", "cm:description": "Q4 financial data"}],
        default=None
    )]
    
    auto_rename: Annotated[bool, Field(
        description="Automatically rename if name conflicts exist",
        default=True
    )]


class UploadResponse(CoreResponse):
    """Response model for file upload operations."""
    entry: Node = Field(..., description="Uploaded file node details")
    
    # Additional upload-specific fields
    file_name: Annotated[str, Field(
        description="Name of the uploaded file"
    )]
    
    file_size: Annotated[int, Field(
        description="Size of uploaded file in bytes",
        ge=0
    )]


class DownloadRequest(BaseModel):
    """Request model for file download operations."""
    model_config = ConfigDict(extra='forbid')
    
    node_id: Annotated[str, Field(
        description="ID of the file node to download",
        examples=["file-abc123"]
    )]
    
    output_path: Annotated[Optional[str], Field(
        description="Local path where to save the downloaded file",
        examples=["/downloads/report.pdf", "./local_copy.pdf"],
        default=None
    )]


class DownloadResponse(BaseModel):
    """Response model for file download operations."""
    model_config = ConfigDict(extra='forbid')
    
    node_id: Annotated[str, Field(
        description="ID of the downloaded file node"
    )]
    
    file_path: Annotated[str, Field(
        description="Local path where file was saved"
    )]
    
    file_size: Annotated[int, Field(
        description="Size of downloaded file in bytes",
        ge=0
    )]
    
    content_type: Annotated[Optional[str], Field(
        description="MIME type of the downloaded file",
        examples=["application/pdf", "text/plain"],
        default=None
    )]


class UpdateContentRequest(BaseModel):
    """Request model for content update operations."""
    model_config = ConfigDict(extra='forbid')
    
    node_id: Annotated[str, Field(
        description="ID of the file node to update",
        examples=["file-abc123"]
    )]
    
    major_version: Annotated[bool, Field(
        description="Create major version (default: minor version)",
        default=False
    )]
    
    comment: Annotated[Optional[str], Field(
        description="Version comment for the update",
        examples=["Updated quarterly figures", "Final revision"],
        default=None
    )]


# Export all models
__all__ = [
    'UploadRequest', 'UploadResponse', 'DownloadRequest', 
    'DownloadResponse', 'UpdateContentRequest'
] 