# Nodes Create Operations

Auto-generated from V1.1 hierarchical code on 2025-07-15 00:36:43

## Overview

Create operations for making new nodes, folders, and associations.

## Usage

```python
from python_alfresco_api import ClientFactory
from python_alfresco_api.clients.core.nodes.models import CreateNodeRequest

# Create factory and client
factory = ClientFactory(base_url="http://localhost:8080")
core_client = factory.create_core_client()

# Access nodes operations
nodes_ops = core_client.nodes

# Create operations
folder = nodes_ops.create_folder(name="My Folder", parent_id="-my-")
request = CreateNodeRequest(name="My Document", nodeType="cm:content")
document = nodes_ops.create(parent_id="-my-", request=request)
```

## Available Operations

### Basic Create Operations

#### `create(parent_id: str, request: CreateNodeRequest)`
Create a new node with full control over properties.

**Parameters:**
- `parent_id`: str - Parent folder identifier
- `request`: CreateNodeRequest - Node creation request with name, type, properties, etc.

**Usage Patterns:**
```python
from python_alfresco_api.clients.core.nodes.models import CreateNodeRequest

# Create document
request = CreateNodeRequest(
    name="My Document.txt",
    nodeType="cm:content",
    properties={"cm:title": "My Document Title"}
)
result = nodes_ops.create(parent_id="-my-", request=request)

# Async
result = await nodes_ops.create_async(parent_id="-my-", request=request)

# Detailed (with full HTTP response)
result = nodes_ops.create_detailed(parent_id="-my-", request=request)
```

#### `create_folder(name: str, parent_id: str = '-my-', properties: Optional[dict] = None)`
Convenience method for creating folders.

**Parameters:**
- `name`: str - Folder name
- `parent_id`: str (default: '-my-') - Parent folder identifier
- `properties`: Optional[dict] - Additional properties

**Usage Patterns:**
```python
# Simple folder creation
folder = nodes_ops.create_folder(name="My Folder")

# With parent and properties
folder = nodes_ops.create_folder(
    name="Project Docs",
    parent_id="specific-parent-id",
    properties={"cm:title": "Project Documentation"}
)

# Async
folder = await nodes_ops.create_folder_async(name="My Folder")

# Convenience with auto-rename
folder = nodes_ops.create_folder_convenience(
    name="My Folder",
    auto_rename=True,
    fields=["id", "name", "properties"]
)
```

### Association Operations

#### `create_association(node_id: str, target_id: str, assoc_type: str, fields: Optional[List[str]] = None)`
Create an association between two nodes.

**Parameters:**
- `node_id`: str - Source node identifier
- `target_id`: str - Target node identifier
- `assoc_type`: str - Association type (e.g., 'cm:references')
- `fields`: Optional[List[str]] - Fields to return

**Usage Patterns:**
```python
# Create reference association
nodes_ops.create_association(
    node_id="source-node-id",
    target_id="target-node-id",
    assoc_type="cm:references"
)

# With specific fields
nodes_ops.create_association(
    node_id="source-node-id",
    target_id="target-node-id",
    assoc_type="cm:references",
    fields=["id", "name", "assocType"]
)

# Async
await nodes_ops.create_association_async(
    node_id="source-node-id",
    target_id="target-node-id",
    assoc_type="cm:references"
)
```

#### `create_secondary_child_association(node_id: str, child_id: str, assoc_type: str, fields: Optional[List[str]] = None)`
Create a secondary child association.

**Parameters:**
- `node_id`: str - Parent node identifier
- `child_id`: str - Child node identifier
- `assoc_type`: str - Association type
- `fields`: Optional[List[str]] - Fields to return

**Usage Patterns:**
```python
# Create secondary child association
nodes_ops.create_secondary_child_association(
    node_id="parent-node-id",
    child_id="child-node-id",
    assoc_type="cm:contains"
)

# Async
await nodes_ops.create_secondary_child_association_async(
    node_id="parent-node-id",
    child_id="child-node-id",
    assoc_type="cm:contains"
)
```

## Return Types

- **create/create_folder**: `NodeResponse` - Contains created node information
- **create_association**: Association information
- **Detailed versions**: Full HTTP response with additional metadata

## Common Patterns

### Folder Creation with Error Handling
```python
try:
    folder = nodes_ops.create_folder(
        name="My Project",
        parent_id="-my-",
        properties={"cm:description": "Project workspace"}
    )
    print(f"Created folder: {folder.entry.id}")
except Exception as e:
    print(f"Failed to create folder: {e}")
```

### Bulk Node Creation
```python
async def create_multiple_nodes(parent_id: str, node_names: List[str]):
    tasks = []
    for name in node_names:
        task = nodes_ops.create_folder_async(name=name, parent_id=parent_id)
        tasks.append(task)
    
    results = await asyncio.gather(*tasks)
    return results
```

### Document Creation with Content
```python
from python_alfresco_api.clients.core.nodes.models import CreateNodeRequest

# Create document node first
request = CreateNodeRequest(
    name="document.txt",
    nodeType="cm:content",
    properties={"cm:title": "My Document"}
)
document = nodes_ops.create(parent_id="-my-", request=request)

# Then upload content (see CRUD operations for update_content)
content = b"This is my document content"
nodes_ops.update_content(
    node_id=document.entry.id,
    content=content,
    filename="document.txt"
)
```

### Association Management
```python
# Create multiple associations
def link_related_documents(main_doc_id: str, related_doc_ids: List[str]):
    for related_id in related_doc_ids:
        nodes_ops.create_association(
            node_id=main_doc_id,
            target_id=related_id,
            assoc_type="cm:references"
        )
```

## See Also

- [Browse Operations](browse_operations.md) - Exploring folder contents and relationships
- [CRUD Operations](crud_operations.md) - Get, update, delete operations
- [Move & Copy Operations](move_copy_operations.md) - Moving and copying nodes
- [Lock Operations](lock_operations.md) - Locking and unlocking nodes
- [Main Nodes API](nodes_api.md) - Overview of all operations 