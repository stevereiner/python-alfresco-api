# Essential Alfresco Operations Guide

**Complete guide to performing essential Alfresco operations using python-alfresco-api with both V1.1 Hierarchical APIs and High-Level Utilities.**

## 📋 Quick Reference

| Operation Category | High-Level Utilities | V1.1 Hierarchical APIs | Best For |
|-------------------|---------------------|------------------------|----------|
| **Content Management** | `content_utils_highlevel.*` | `core_client.nodes.*` | Rapid development |
| **Node Operations** | `node_utils_highlevel.*` | `core_client.nodes.*` | Fine control |
| **Search Operations** | `search_utils.simple_search()` | `search_client.search()` | Already optimized |
| **Versioning** | `version_utils_highlevel.*` | `core_client.versions.*` | Document workflows |

## 🧪 Complete Test Coverage

For comprehensive examples and validation patterns, see:
- **[`tests/test_mcp_v11_true_high_level_apis_fixed.py`](../tests/test_mcp_v11_true_high_level_apis_fixed.py)** - 15 MCP operations with both sync and async patterns
- **[`tests/test_highlevel_utils.py`](../tests/test_highlevel_utils.py)** - High-level utilities testing with real Alfresco integration

## 🎯 Production-Ready Examples

Complete, copy-paste examples available in:
- **[`examples/operations/`](../examples/operations/)** - Windows-compatible, production-ready code
  - `upload_document.py` - Document upload with automatic versioning
  - `versioning_workflow.py` - Complete checkout → edit → checkin workflow  
  - `basic_operations.py` - Folder management and CRUD operations
  - `search_operations.py` - Content search and metadata queries
  - `README.md` - Setup patterns and usage guide

---

## 📁 Content Management Operations

### Setup
```python
from python_alfresco_api import ClientFactory
from python_alfresco_api.utils import content_utils_highlevel, node_utils_highlevel

# Initialize clients
factory = ClientFactory(base_url="http://localhost:8080", username="admin", password="admin")
core_client = factory.create_core_client()
```

### Create Folder
```python
# High-Level Utility (Recommended)
folder_result = content_utils_highlevel.create_folder_highlevel(
    core_client=core_client,
    name="My Project Folder",
    parent_id="-my-",  # User's home directory
    description="Project documents folder"
)
folder_id = folder_result['id']

# V1.1 Hierarchical API (Fine Control)
from python_alfresco_api.clients.core.nodes.models import CreateNodeRequest, NodeType

folder_request = CreateNodeRequest(
    name="Project Folder",
    node_type=NodeType.FOLDER,
    properties={
        "cm:title": "My Project Folder",
        "cm:description": "Project documents folder"
    }
)
folder_result = core_client.nodes.create(parent_id="-my-", request=folder_request)
```

### Upload Document
```python
# High-Level Utility (Recommended)
document_result = content_utils_highlevel.create_and_upload_file_highlevel(
    core_client=core_client,
    file_path="/path/to/document.pdf",
    parent_id=folder_id,
    filename="Important Document.pdf",
    description="Uploaded via Python API"
)

# V1.1 Hierarchical API (Fine Control)
import tempfile

# Create document node first
doc_request = CreateNodeRequest(
    name="document.pdf",
    node_type=NodeType.CONTENT,
    properties={"cm:title": "Important Document"}
)
doc_result = core_client.nodes.create(parent_id=folder_id, request=doc_request)

# Then upload content
with open("/path/to/document.pdf", "rb") as file:
    content_result = core_client.nodes.update_content(
        node_id=doc_result.entry.id,
        content=file.read()
    )
```

### Download Document
```python
# V1.1 Hierarchical API
content_response = core_client.nodes.get_content(node_id=document_id)

# Save to file
with open("downloaded_document.pdf", "wb") as file:
    file.write(content_response.content)

# Or get as bytes for processing
document_bytes = content_response.content
```

### Get Node Properties
```python
# High-Level Utility
node_info = content_utils_highlevel.get_node_info_highlevel(
    core_client=core_client,
    node_id=document_id
)
print(f"Document: {node_info['name']}")
print(f"Size: {node_info.get('content', {}).get('sizeInBytes', 0)}")
print(f"Modified: {node_info.get('modifiedAt', 'Unknown')}")

# V1.1 Hierarchical API
node_details = core_client.nodes.get(
    node_id=document_id,
    include=["properties", "path", "permissions"]
)
properties = node_details.entry.properties
```

### Update Node Properties
```python
# V1.1 Hierarchical API
update_request = {
    "properties": {
        "cm:title": "Updated Document Title",
        "cm:description": "Updated via Python API",
        "cm:author": "Python Script"
    }
}
updated_node = core_client.nodes.update(node_id=document_id, request=update_request)

# High-Level Utility (using update content)
content_utils_highlevel.update_content_from_string_highlevel(
    core_client=core_client,
    node_id=document_id,
    content_text="Updated document content"
)
```

### Delete Node
```python
# High-Level Utility (Move to trash)
delete_result = node_utils_highlevel.delete_node_highlevel(
    core_client=core_client,
    node_id=document_id
)

# V1.1 Hierarchical API (Move to trash)
core_client.nodes.delete(node_id=document_id)

# V1.1 Hierarchical API (Permanent deletion)
core_client.nodes.delete(node_id=document_id, permanent=True)

# Bulk deletion (High-Level Utility)
node_ids = [document_id1, document_id2, folder_id]
bulk_result = node_utils_highlevel.bulk_delete_nodes_highlevel(
    core_client=core_client,
    node_ids=node_ids
)
```

---

## 🗂️ Node Management Operations

### Browse Repository
```python
# High-Level Utility
children = node_utils_highlevel.list_children_highlevel(
    core_client=core_client,
    parent_id="-my-"  # User's home directory
)
print(f"Found {len(children)} items in folder")

# V1.1 Hierarchical API
children = core_client.nodes.list_children("-my-", max_items=10)
for entry in children.list.entries:
    print(f"{entry.entry.name} ({entry.entry.node_type})")
```

### Get Node Path
```python
# High-Level Utility
path_info = node_utils_highlevel.get_node_path_highlevel(
    core_client=core_client,
    node_id=document_id
)
print(f"Document path: {path_info['path']}")

# V1.1 Hierarchical API
node_with_path = core_client.nodes.get(node_id=document_id, include=["path"])
path_elements = node_with_path.entry.path.elements
full_path = "/".join([elem.name for elem in path_elements])
```

### Create Simple Operations
```python
# High-Level Utilities for Quick Operations
simple_folder = node_utils_highlevel.create_folder_simple_highlevel(
    core_client=core_client,
    name="Quick Folder",
    parent_id="-my-"
)

simple_doc = node_utils_highlevel.create_document_simple_highlevel(
    core_client=core_client,
    name="Quick Document.txt",
    parent_id=folder_id
)
```

---

## 🔍 Search Operations

### Simple Text Search
```python
from python_alfresco_api.utils import search_utils

# Setup search client
search_client = factory.create_search_client()

# High-Level Utility (Recommended - already optimized!)
search_results = search_utils.simple_search(
    search_client=search_client,
    query_str="finance AND reports",
    max_items=25
)

# Process results
if search_results and hasattr(search_results, 'list'):
    entries = search_results.list.entries
    for entry in entries:
        node = entry.entry
        print(f"Found: {node.name} (ID: {node.id})")
```

### Advanced Search
```python
from python_alfresco_api.models.alfresco_search_models import SearchRequest

# V1.1 Hierarchical API with Pydantic Models
advanced_search = SearchRequest(
    query={
        "query": "TYPE:'cm:content' AND cm:modified:[2024-01-01T00:00:00 TO NOW]",
        "language": "afts"
    },
    paging={"maxItems": 50},
    include=["properties", "path"]
)

results = search_client.search(advanced_search.model_dump())
```

### CMIS Search
```python
# Structured Query Language
cmis_results = search_utils.simple_search(
    search_client=search_client,
    query_str="SELECT * FROM cmis:document WHERE cmis:contentStreamMimeType = 'application/pdf'",
    query_language="cmis",
    max_items=20
)
```

### Metadata Search
```python
# Search by specific properties
metadata_search = search_utils.simple_search(
    search_client=search_client,
    query_str="cm:title:'project report' AND cm:author:'john.doe'",
    max_items=10
)
```

---

## 📝 Document Versioning & Locking

### Checkout → Edit → Checkin Workflow
```python
from python_alfresco_api.utils import version_utils_highlevel

# 1. Check out document (lock for editing)
checkout_result = version_utils_highlevel.checkout_document_highlevel(
    core_client=core_client,
    node_id=document_id
)

# 2. Update content and check in (create new version)
checkin_result = version_utils_highlevel.checkin_document_highlevel(
    core_client=core_client,
    node_id=document_id,
    content="Updated document content with new information",
    comment="Fixed formatting and added new section"
)

# 3. Alternative: Cancel checkout (discard changes)
cancel_result = version_utils_highlevel.cancel_checkout_highlevel(
    core_client=core_client,
    node_id=document_id
)
```

### Auto-Versioning
```python
# One-call checkout → update → checkin
auto_version_result = version_utils_highlevel.auto_version_document_highlevel(
    core_client=core_client,
    node_id=document_id,
    content="Updated via auto-versioning utility",
    comment="Automated content update"
)
```

### Version History
```python
# Get all versions of a document
version_history = version_utils_highlevel.get_version_history_highlevel(
    core_client=core_client,
    node_id=document_id
)

# Process version information
for version in version_history.get('entries', []):
    version_entry = version['entry']
    print(f"Version {version_entry['name']}: {version_entry.get('properties', {}).get('cm:versionLabel', 'Unknown')}")
```

### Lock Status and Management
```python
# Check if document is locked
lock_status = version_utils_highlevel.check_lock_status_highlevel(
    core_client=core_client,
    node_id=document_id
)
print(f"Document locked: {lock_status.get('is_locked', False)}")

# Manual lock/unlock operations
lock_result = version_utils_highlevel.lock_document_highlevel(
    core_client=core_client,
    node_id=document_id,
    lock_type="ALLOW_OWNER_CHANGES"
)

unlock_result = version_utils_highlevel.unlock_document_highlevel(
    core_client=core_client,
    node_id=document_id
)
```

---

## ⚡ Async Operations (Web Applications)

### Async Pattern Example
```python
import asyncio

async def async_operations_example():
    # Async search
    async_search_results = await search_client.search_async(search_request.model_dump())
    
    # Async node operations
    async_node = await core_client.nodes.get_async(node_id)
    async_children = await core_client.nodes.list_children_async("-my-")
    
    # Async content operations
    async_content = await core_client.nodes.get_content_async(document_id)
    
    return {
        'search_results': async_search_results,
        'node_details': async_node,
        'children': async_children,
        'content': async_content
    }

# Run async operations
results = asyncio.run(async_operations_example())
```

---

## 🏭 Production Patterns

### Error Handling
```python
try:
    folder_result = content_utils_highlevel.create_folder_highlevel(
        core_client=core_client,
        name="Production Folder",
        parent_id="-my-"
    )
except Exception as e:
    print(f"Folder creation failed: {e}")
    # High-level utilities include comprehensive error handling
```

### Batch Operations
```python
# Batch folder creation
folders_to_create = ["Folder1", "Folder2", "Folder3"]
created_folders = []

for folder_name in folders_to_create:
    try:
        result = content_utils_highlevel.create_folder_highlevel(
            core_client=core_client,
            name=folder_name,
            parent_id=parent_folder_id
        )
        created_folders.append(result)
    except Exception as e:
        print(f"Failed to create {folder_name}: {e}")

# Batch deletion
if created_folders:
    folder_ids = [folder['id'] for folder in created_folders]
    node_utils_highlevel.bulk_delete_nodes_highlevel(
        core_client=core_client,
        node_ids=folder_ids
    )
```

### Type Safety with Pydantic Models
```python
from python_alfresco_api.models.alfresco_core_models import NodeBodyCreate
from python_alfresco_api.clients.conversion_utils import pydantic_to_attrs_dict

# Create and validate with Pydantic
node_model = NodeBodyCreate(
    name="validated_document.pdf",
    nodeType="cm:content",
    properties={
        "cm:title": "Validated Document",
        "cm:description": "Created with type safety"
    }
)

# Convert for API use
attrs_dict = pydantic_to_attrs_dict(node_model, target_class_name="NodeBodyCreate")
result = core_client.nodes.create(parent_id="-my-", request=attrs_dict)
```

---

## 📊 Performance Recommendations

| Operation Type | Recommended Pattern | Reason |
|----------------|-------------------|---------|
| **Quick Scripts** | High-Level Utilities | 1-2 lines per operation, built-in error handling |
| **Complex Workflows** | V1.1 Hierarchical APIs | Fine control, flexible parameters |
| **Web Applications** | Async V1.1 APIs | Concurrent execution, better performance |
| **Type Safety** | Pydantic Models + Conversion | Validation, IDE support, maintainability |
| **Batch Operations** | Mixed approach | High-level for individual ops, V1.1 for coordination |

---

## 🔗 Additional Resources

- **[Main README](../README.md)** - Package overview and quick start
- **[Authentication Guide](AUTHENTICATION_GUIDE.md)** - Complete authentication patterns  
- **[Pydantic Models Guide](PYDANTIC_MODELS_GUIDE.md)** - Type safety and model usage
- **[Client Types Guide](CLIENT_TYPES_GUIDE.md)** - Choosing the right client approach
- **[API Documentation Index](API_DOCUMENTATION_INDEX.md)** - Complete API reference

---

**💡 Quick Start**: Begin with the [`examples/operations/`](../examples/operations/) folder for immediate, copy-paste examples, then use this guide for comprehensive operation coverage and advanced patterns. 