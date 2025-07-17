#!/usr/bin/env python3
"""
V1.1 Three-Tier Model Architecture Prototype

Demonstrates the user's IDEAL architecture:
- Global models (shared across all APIs)
- API-level models (shared within one API)  
- Operation-specific models (specific to one operation)

This prototype shows how the structure would work in practice.
"""

from typing import List, Optional, Dict, Any, Union
from datetime import datetime
from pydantic import BaseModel, Field

# =============================================================================
# LEVEL 1: GLOBAL MODELS (clients/models.py)
# =============================================================================

class BaseEntry(BaseModel):
    """Base entry structure used across all APIs."""
    id: str
    name: str
    created_at: datetime = Field(alias="createdAt")
    modified_at: datetime = Field(alias="modifiedAt")

class PagingInfo(BaseModel):
    """Pagination information used across all APIs."""
    max_items: int = Field(alias="maxItems")
    skip_count: int = Field(alias="skipCount") 
    has_more_items: bool = Field(alias="hasMoreItems")
    total_items: Optional[int] = Field(None, alias="totalItems")

class ErrorResponse(BaseModel):
    """Standard error response used across all APIs."""
    error: str
    message: str
    status_code: int

# =============================================================================
# LEVEL 2: CORE API MODELS (clients/core/models.py)
# =============================================================================

class CoreEntryList(BaseModel):
    """Standard entry list for core API operations."""
    entries: List[BaseEntry]
    pagination: PagingInfo

class NodeReference(BaseModel):
    """Node reference used across core operations."""
    id: str
    store_ref: Optional[str] = Field(None, alias="storeRef")

class CoreResponse(BaseModel):
    """Standard core API response wrapper."""
    entry: BaseEntry

# =============================================================================
# LEVEL 3: NODE-SPECIFIC MODELS (clients/core/nodes/models.py)
# =============================================================================

class NodeProperties(BaseModel):
    """Node properties for Alfresco content model."""
    cm_title: Optional[str] = Field(None, description="Document title")
    cm_description: Optional[str] = Field(None, description="Document description") 
    cm_author: Optional[str] = Field(None, description="Document author")
    custom_properties: Dict[str, Any] = Field(default_factory=dict, description="Custom namespace properties")

class ContentInfo(BaseModel):
    """Content information for files."""
    mime_type: str = Field(alias="mimeType", description="MIME type of the content")
    size_in_bytes: int = Field(alias="sizeInBytes", description="File size in bytes")
    encoding: Optional[str] = Field(None, description="Content encoding")

class Node(BaseEntry):
    """Complete node model with all properties."""
    node_type: str = Field(alias="nodeType", description="Alfresco node type (e.g., cm:content, cm:folder)")
    is_file: bool = Field(alias="isFile", description="True if this is a file node")
    is_folder: bool = Field(alias="isFolder", description="True if this is a folder node")
    parent_id: Optional[str] = Field(None, alias="parentId", description="Parent node ID")
    properties: Optional[NodeProperties] = None
    content: Optional[ContentInfo] = None
    allowable_operations: Optional[List[str]] = Field(default=None, alias="allowableOperations")
    aspect_names: Optional[List[str]] = Field(default=None, alias="aspectNames")

class NodeResponse(CoreResponse):
    """Node operation response."""
    entry: Node

class NodeListResponse(CoreEntryList):
    """Node list response."""
    entries: List[Node]

class CreateNodeRequest(BaseModel):
    """Request model for creating nodes."""
    name: str = Field(description="Node name", min_length=1, max_length=255)
    node_type: str = Field(description="Node type", examples=["cm:content", "cm:folder"])
    properties: Optional[NodeProperties] = None

class UpdateNodeRequest(BaseModel):
    """Request model for updating nodes."""
    name: Optional[str] = Field(None, description="New node name")
    properties: Optional[NodeProperties] = None

# =============================================================================
# LEVEL 3: FOLDER-SPECIFIC MODELS (clients/core/folders/models.py)
# =============================================================================

class FolderProperties(BaseModel):
    """Folder-specific properties."""
    cm_title: Optional[str] = Field(None, description="Folder title")
    cm_description: Optional[str] = Field(None, description="Folder description")

class Folder(BaseEntry):
    """Folder model extending base entry."""
    node_type: str = Field(alias="nodeType", default="cm:folder")
    is_folder: bool = Field(alias="isFolder", default=True)
    is_file: bool = Field(alias="isFile", default=False)
    properties: Optional[FolderProperties] = None

class FolderResponse(CoreResponse):
    """Folder operation response."""
    entry: Folder

class CreateFolderRequest(BaseModel):
    """Request model for creating folders."""
    name: str = Field(description="Folder name", min_length=1, max_length=255)
    node_type: str = Field(default="cm:folder", description="Node type")
    properties: Optional[FolderProperties] = None

# =============================================================================
# OPERATION CLASSES DEMONSTRATION
# =============================================================================

class NodeOperations:
    """Node operations using local models."""
    
    def __init__(self, client):
        self.client = client
    
    async def get(self, node_id: str, include: Optional[List[str]] = None) -> NodeResponse:
        """Get node with perfect typing from local models."""
        print(f"📄 Getting node {node_id}")
        print(f"   ✅ Using local NodeResponse model")
        print(f"   ✅ Clean import: from .models import NodeResponse")
        
        # Simulate API response
        mock_data = {
            "entry": {
                "id": node_id,
                "name": "test-document.txt",
                "createdAt": "2024-01-15T10:30:00Z",
                "modifiedAt": "2024-01-15T10:30:00Z",
                "nodeType": "cm:content",
                "isFile": True,
                "isFolder": False,
                "properties": {
                    "cm_title": "Test Document",
                    "cm_description": "A test document"
                },
                "content": {
                    "mimeType": "text/plain",
                    "sizeInBytes": 1024
                }
            }
        }
        
        return NodeResponse.model_validate(mock_data)
    
    async def create(self, parent_id: str, request: CreateNodeRequest) -> NodeResponse:
        """Create node with validation from local models."""
        print(f"📁 Creating node in {parent_id}")
        print(f"   ✅ Using local CreateNodeRequest model")
        print(f"   ✅ Request validation: {request.name} ({request.node_type})")
        
        # Simulate created node
        mock_data = {
            "entry": {
                "id": "new-node-123",
                "name": request.name,
                "createdAt": "2024-01-15T10:30:00Z",
                "modifiedAt": "2024-01-15T10:30:00Z", 
                "nodeType": request.node_type,
                "isFile": request.node_type == "cm:content",
                "isFolder": request.node_type == "cm:folder",
                "properties": request.properties.model_dump() if request.properties else {}
            }
        }
        
        return NodeResponse.model_validate(mock_data)

class FolderOperations:
    """Folder operations using local models."""
    
    def __init__(self, client):
        self.client = client
    
    async def create(self, parent_id: str, request: CreateFolderRequest) -> FolderResponse:
        """Create folder with folder-specific models."""
        print(f"📂 Creating folder in {parent_id}")
        print(f"   ✅ Using local CreateFolderRequest model")
        print(f"   ✅ Folder-specific validation: {request.name}")
        
        # Simulate created folder
        mock_data = {
            "entry": {
                "id": "new-folder-456",
                "name": request.name,
                "createdAt": "2024-01-15T10:30:00Z",
                "modifiedAt": "2024-01-15T10:30:00Z",
                "nodeType": "cm:folder",
                "isFile": False,
                "isFolder": True,
                "properties": request.properties.model_dump() if request.properties else {}
            }
        }
        
        return FolderResponse.model_validate(mock_data)

class AlfrescoCoreClient:
    """Core client demonstrating three-tier architecture."""
    
    def __init__(self, base_url: str):
        self.base_url = base_url
        self._nodes = None
        self._folders = None
    
    @property  
    def nodes(self) -> NodeOperations:
        """Node operations (lazy loaded)."""
        if self._nodes is None:
            self._nodes = NodeOperations(self)
        return self._nodes
    
    @property
    def folders(self) -> FolderOperations:
        """Folder operations (lazy loaded)."""
        if self._folders is None:
            self._folders = FolderOperations(self)
        return self._folders

# =============================================================================
# DEMONSTRATION
# =============================================================================

async def demonstrate_three_tier_architecture():
    """Demonstrate the three-tier model architecture."""
    print("🎯 V1.1 THREE-TIER MODEL ARCHITECTURE DEMONSTRATION")
    print("=" * 60)
    
    # Initialize client
    client = AlfrescoCoreClient("http://localhost:8080")
    
    print(f"\n📂 THREE-TIER MODEL ORGANIZATION:")
    print(f"   Level 1: Global models (BaseEntry, PagingInfo, ErrorResponse)")
    print(f"   Level 2: API models (CoreResponse, CoreEntryList, NodeReference)")
    print(f"   Level 3: Operation models (Node, CreateNodeRequest, NodeResponse)")
    
    print(f"\n🏗️ PERFECT LOCALITY DEMONSTRATION:")
    
    # Demonstrate node operations
    print(f"\n1. 📄 NODE OPERATIONS")
    node_request = CreateNodeRequest(
        name="test-document.txt",
        node_type="cm:content",
        properties=NodeProperties(
            cm_title="Test Document",
            cm_description="Created with three-tier architecture",
            cm_author=None
        )
    )
    
    node_result = await client.nodes.create(parent_id="-my-", request=node_request)
    print(f"   📋 Created: {node_result.entry.name} (ID: {node_result.entry.id})")
    print(f"   📊 Type safety: {type(node_result).__name__}")
    
    # Get the created node
    get_result = await client.nodes.get(node_id=node_result.entry.id)
    print(f"   📋 Retrieved: {get_result.entry.name}")
    if get_result.entry.content:
        print(f"   📄 Content: {get_result.entry.content.mime_type}")
    
    # Demonstrate folder operations  
    print(f"\n2. 📁 FOLDER OPERATIONS")
    folder_request = CreateFolderRequest(
        name="test-folder",
        properties=FolderProperties(
            cm_title="Test Folder",
            cm_description="Created with dedicated folder models"
        )
    )
    
    folder_result = await client.folders.create(parent_id="-my-", request=folder_request)
    print(f"   📋 Created: {folder_result.entry.name} (ID: {folder_result.entry.id})")
    print(f"   📊 Type safety: {type(folder_result).__name__}")
    
    print(f"\n✨ ARCHITECTURE BENEFITS:")
    print(f"   ✅ Perfect locality: Models exactly where they're used")
    print(f"   ✅ Clean imports: from .models import NodeResponse")
    print(f"   ✅ Type safety: Full Pydantic validation")
    print(f"   ✅ Maintainability: Focused, manageable files")
    print(f"   ✅ Scalability: Easy to add new operations")
    print(f"   ✅ Developer experience: Intuitive structure")

if __name__ == "__main__":
    import asyncio
    asyncio.run(demonstrate_three_tier_architecture()) 