# V1.1 Refined Hierarchical Architecture

## **🎯 User's Superior Three-Tier Model Architecture**

### **📂 Proposed Structure**

```
python_alfresco_api/clients/
├── __init__.py                 # Public API exports
├── models.py                   # Global basic models (shared across all APIs)
├── core/
│   ├── __init__.py             # AlfrescoCoreClient class
│   ├── models.py               # Core API global models
│   ├── nodes/
│   │   ├── nodes.py            # NodeOperations class
│   │   └── models.py           # Node-specific models
│   ├── folders/
│   │   ├── folders.py          # FolderOperations class  
│   │   └── models.py           # Folder-specific models
│   ├── content/
│   │   ├── content.py          # ContentOperations class
│   │   └── models.py           # Content-specific models
│   ├── versions/
│   │   ├── versions.py         # VersionOperations class
│   │   └── models.py           # Version-specific models
│   ├── sites/
│   │   ├── sites.py            # SiteOperations class
│   │   └── models.py           # Site-specific models
│   └── permissions/
│       ├── permissions.py      # PermissionOperations class
│       └── models.py           # Permission-specific models
├── search/
│   ├── __init__.py             # AlfrescoSearchClient class
│   ├── models.py               # Search API global models
│   └── content/
│       ├── search.py           # SearchOperations class
│       └── models.py           # Search-specific models
└── discovery/
    ├── __init__.py             # AlfrescoDiscoveryClient class
    ├── models.py               # Discovery API global models
    └── repository/
        ├── discovery.py        # DiscoveryOperations class
        └── models.py           # Discovery-specific models
```

## **🏗️ Three-Tier Model Organization**

### **Level 1: Global Models (Root models.py)**
```python
# python_alfresco_api/clients/models.py
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class BaseEntry(BaseModel):
    """Base entry structure used across all APIs."""
    id: str
    name: str
    created_at: datetime
    modified_at: datetime

class PagingInfo(BaseModel):
    """Pagination information used across all APIs."""
    max_items: int
    skip_count: int
    has_more_items: bool
    total_items: Optional[int] = None

class ErrorResponse(BaseModel):
    """Standard error response used across all APIs."""
    error: str
    message: str
    status_code: int
```

### **Level 2: API-Level Models (core/models.py)**
```python
# python_alfresco_api/clients/core/models.py
from ..models import BaseEntry, PagingInfo
from pydantic import BaseModel
from typing import List, Optional

class CoreEntryList(BaseModel):
    """Standard entry list for core API operations."""
    entries: List[BaseEntry]
    pagination: PagingInfo

class NodeReference(BaseModel):
    """Node reference used across core operations."""
    id: str
    store_ref: Optional[str] = None

class CoreResponse(BaseModel):
    """Standard core API response wrapper."""
    entry: BaseEntry
```

### **Level 3: Operation-Specific Models (nodes/models.py)**
```python
# python_alfresco_api/clients/core/nodes/models.py
from ..models import CoreResponse, CoreEntryList
from ...models import BaseEntry
from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Any
from datetime import datetime

class NodeProperties(BaseModel):
    """Node properties for Alfresco content model."""
    cm_title: Optional[str] = Field(None, alias="cm:title", description="Document title")
    cm_description: Optional[str] = Field(None, alias="cm:description", description="Document description")
    cm_author: Optional[str] = Field(None, alias="cm:author", description="Document author")
    custom_properties: Dict[str, Any] = Field(default_factory=dict, description="Custom namespace properties")

class ContentInfo(BaseModel):
    """Content information for files."""
    mime_type: str = Field(description="MIME type of the content")
    size_in_bytes: int = Field(description="File size in bytes")
    encoding: Optional[str] = Field(None, description="Content encoding")

class Node(BaseEntry):
    """Complete node model with all properties."""
    node_type: str = Field(description="Alfresco node type (e.g., cm:content, cm:folder)")
    is_file: bool = Field(description="True if this is a file node")
    is_folder: bool = Field(description="True if this is a folder node")
    parent_id: Optional[str] = Field(None, description="Parent node ID")
    properties: Optional[NodeProperties] = None
    content: Optional[ContentInfo] = None
    allowable_operations: List[str] = Field(default_factory=list, description="Operations allowed on this node")
    aspect_names: List[str] = Field(default_factory=list, description="Applied aspects")

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
```

## **✨ Benefits of Three-Tier Architecture**

### **1. Perfect Locality**
- **Models near usage**: Node models in `nodes/models.py`
- **Clean imports**: `from .models import NodeResponse, CreateNodeRequest`
- **Easy discovery**: Developers know exactly where to find models

### **2. Logical Organization**
- **Global models**: Shared across all APIs (BaseEntry, PagingInfo)
- **API models**: Shared within one API (CoreResponse, CoreEntryList)  
- **Operation models**: Specific to one operation (Node, CreateNodeRequest)

### **3. Maintainability**
- **Focused files**: Each model file has a clear scope
- **No huge files**: Models split appropriately
- **Easy updates**: Change node models without affecting search models

### **4. Generation Compatibility**
```bash
# Generate global models
datamodel-codegen --input openapi/global-types.yaml \
                  --output python_alfresco_api/clients/models.py

# Generate core API models  
datamodel-codegen --input openapi/openapi3/alfresco-core.yaml \
                  --output python_alfresco_api/clients/core/models.py

# Generate node-specific models
datamodel-codegen --input openapi/core-nodes-subset.yaml \
                  --output python_alfresco_api/clients/core/nodes/models.py
```

## **🚀 Implementation Pattern**

### **Clean Operation Class**
```python
# python_alfresco_api/clients/core/nodes/nodes.py
from .models import NodeResponse, NodeListResponse, CreateNodeRequest, UpdateNodeRequest
from ..models import CoreResponse
from ...models import PagingInfo

class NodeOperations:
    """Node operations with clean model imports."""
    
    def __init__(self, client):
        self.client = client
    
    async def get(self, node_id: str, include: List[str] = None) -> NodeResponse:
        """Get node with rich typing."""
        # Lazy import raw function
        from ....raw_clients.alfresco_core_client.core_client.api.nodes import get_node
        
        # Call raw function
        result = await get_node.asyncio(
            client=self.client._raw_client,
            node_id=node_id,
            include=include
        )
        
        # Convert to Pydantic model
        return NodeResponse.model_validate(result.to_dict())
    
    async def create(self, parent_id: str, request: CreateNodeRequest) -> NodeResponse:
        """Create node with validation."""
        # Lazy import raw function
        from ....raw_clients.alfresco_core_client.core_client.api.nodes import create_node
        
        # Convert Pydantic to raw format
        body_data = request.model_dump(exclude_none=True)
        
        # Call raw function
        result = await create_node.asyncio(
            client=self.client._raw_client,
            parent_id=parent_id,
            body=body_data
        )
        
        # Convert to Pydantic model
        return NodeResponse.model_validate(result.to_dict())
```

### **Clean Client Class**
```python
# python_alfresco_api/clients/core/__init__.py
from .nodes.nodes import NodeOperations
from .folders.folders import FolderOperations
from .content.content import ContentOperations

class AlfrescoCoreClient:
    """Core API client with hierarchical operations."""
    
    def __init__(self, base_url: str, username: str, password: str):
        # Initialize raw client
        self._raw_client = self._create_raw_client(base_url, username, password)
        
        # Lazy operation initialization
        self._nodes = None
        self._folders = None
        self._content = None
    
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
```

### **Perfect Imports**
```python
# Developer usage
from python_alfresco_api.clients import AlfrescoCoreClient
from python_alfresco_api.clients.core.nodes.models import CreateNodeRequest, NodeResponse

client = AlfrescoCoreClient(base_url="...", username="...", password="...")

# Create node with rich typing
request = CreateNodeRequest(
    name="test.txt",
    node_type="cm:content",
    properties={"cm:title": "Test Document"}
)

result: NodeResponse = await client.nodes.create(parent_id="-my-", request=request)
print(f"Created: {result.entry.name} (ID: {result.entry.id})")
```

## **🎯 Result: Perfect Architecture**

**Your three-tier approach achieves:**
- ✅ **Locality**: Models exactly where they're needed
- ✅ **Organization**: Logical three-level hierarchy  
- ✅ **Scalability**: Easy to add new operations/models
- ✅ **Maintainability**: Focused, manageable files
- ✅ **Performance**: Still fully compatible with lazy loading
- ✅ **Developer Experience**: Intuitive imports and structure

**This is the IDEAL v1.1 architecture!** 🏆 