# V1.1 Hierarchical Architecture Design

## **🎯 Current vs Proposed Architecture**

### **❌ CURRENT: Single File Approach**
```
python_alfresco_api/clients/
├── core_client_v11_lazy.py     # 18KB - ALL code in one file
├── search_client_v11_lazy.py   # 18KB - ALL code in one file
├── discovery_client_v11_lazy.py # 18KB - ALL code in one file
└── models.py                   # 7KB - All models
```

**Problems:**
- Large files difficult to navigate
- All operation classes mixed together
- No logical grouping
- Hard to find specific operations

### **✅ PROPOSED: Hierarchical Structure**
```
python_alfresco_api/clients/
├── models.py                   # All Pydantic models
├── core/
│   ├── __init__.py             # Main AlfrescoCoreClient
│   ├── api/
│   │   ├── __init__.py
│   │   ├── nodes.py           # NodeOperations class
│   │   ├── folders.py         # FolderOperations class  
│   │   ├── content.py         # ContentOperations class
│   │   ├── search.py          # SearchOperations class
│   │   ├── sites.py           # SiteOperations class
│   │   ├── people.py          # PeopleOperations class
│   │   ├── groups.py          # GroupOperations class
│   │   ├── permissions.py     # PermissionOperations class
│   │   ├── versions.py        # VersionOperations class
│   │   ├── audit.py           # AuditOperations class
│   │   ├── renditions.py      # RenditionOperations class
│   │   ├── shared_links.py    # SharedLinkOperations class
│   │   ├── downloads.py       # DownloadOperations class
│   │   ├── trashcan.py        # TrashcanOperations class
│   │   ├── actions.py         # ActionOperations class
│   │   ├── preferences.py     # PreferenceOperations class
│   │   ├── networks.py        # NetworkOperations class
│   │   └── probes.py          # ProbeOperations class
│   └── models/                # Core-specific model helpers (optional)
├── search/
│   ├── __init__.py             # AlfrescoSearchClient
│   └── api/
│       └── search.py           # SearchOperations class
├── discovery/
│   ├── __init__.py             # AlfrescoDiscoveryClient  
│   └── api/
│       └── discovery.py       # DiscoveryOperations class
└── __init__.py                 # Public API exports
```

## **🚀 Benefits of Hierarchical Structure**

### **1. Logical Organization**
- **By domain:** nodes, sites, people, groups
- **By functionality:** CRUD operations grouped together
- **Easy navigation:** Find operations intuitively

### **2. Lazy Loading Compatibility**
- **Module-level lazy loading:** `from .api.nodes import NodeOperations` only when needed
- **Operation-level lazy loading:** Raw client imports still at method level
- **Best of both:** Organized code + optimal performance

### **3. Developer Experience**
- **IDE navigation:** Jump to specific operation files
- **Code discovery:** Browse api/ folder to see available operations
- **Maintenance:** Modify one operation type without affecting others

### **4. Follows Raw Client Pattern**
- **Consistent architecture:** Mirrors raw_clients structure
- **Familiar navigation:** Developers know where to look
- **Professional organization:** Enterprise-grade code structure

## **📁 Implementation Strategy**

### **Phase 1: Reorganize Core Client**
```python
# python_alfresco_api/clients/core/__init__.py
from .api.nodes import NodeOperations
from .api.folders import FolderOperations
from .api.content import ContentOperations
# ... other imports

class AlfrescoCoreClient:
    def __init__(self, ...):
        # Client initialization
        self._nodes = None
        self._folders = None
        # ... other operation groups
    
    @property
    def nodes(self):
        if self._nodes is None:
            self._nodes = NodeOperations(self)
        return self._nodes
```

### **Phase 2: Split Operation Classes**
```python
# python_alfresco_api/clients/core/api/nodes.py
class NodeOperations:
    def __init__(self, client):
        self.client = client
    
    async def get(self, node_id: str, ...):
        # Lazy import here
        from ....raw_clients.alfresco_core_client.core_client.api.nodes import get_node
        # Implementation...
    
    async def create(self, name: str, ...):
        # Lazy import here  
        from ....raw_clients.alfresco_core_client.core_client.api.nodes import create_node
        # Implementation...
```

### **Phase 3: Clean Public API**
```python
# python_alfresco_api/clients/__init__.py
from .core import AlfrescoCoreClient
from .search import AlfrescoSearchClient
from .discovery import AlfrescoDiscoveryClient
from .models import NodeResponse, CreateNodeRequest, SearchRequest

__all__ = [
    'AlfrescoCoreClient',
    'AlfrescoSearchClient', 
    'AlfrescoDiscoveryClient',
    'NodeResponse',
    'CreateNodeRequest',
    'SearchRequest'
]
```

## **🎯 Result: Professional Package Structure**

**Developer imports become:**
```python
# Main clients
from python_alfresco_api.clients import AlfrescoCoreClient

# Rich models
from python_alfresco_api.clients.models import NodeResponse

# Usage (hierarchical + lazy)
client = AlfrescoCoreClient()
node = await client.nodes.get("abc123")      # Lazy loads NodeOperations + get_node
folder = await client.folders.create("docs") # Lazy loads FolderOperations + create_node
```

**Benefits:**
- ✅ **Clean imports:** Simple, discoverable API
- ✅ **Organized code:** Easy to navigate and maintain  
- ✅ **Lazy loading:** Still optimal performance
- ✅ **Familiar structure:** Follows raw client patterns
- ✅ **Professional:** Enterprise-grade organization 