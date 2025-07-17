# Nodes Browse & List Operations

Auto-generated from V1.1 hierarchical code on 2025-07-15 00:36:43

## Overview

Browse and list operations for exploring folder contents, relationships, and hierarchies.

## Usage

```python
from python_alfresco_api import ClientFactory

# Create factory and client
factory = ClientFactory(base_url="http://localhost:8080")
core_client = factory.create_core_client()

# Access nodes operations
nodes_ops = core_client.nodes

# Browse operations
result = nodes_ops.browse(node_id="abc123-def456", max_items=100)
result = nodes_ops.list_children(node_id="abc123-def456", max_items=100)
result = nodes_ops.list_parents(node_id="abc123-def456")
```

## Available Operations

### Browse Operations

#### `browse(node_id: str = '-my-', max_items: int = 100)`
Convenience method for browsing folder contents.

**Parameters:**
- `node_id`: str (default: '-my-') - Node identifier
- `max_items`: int (default: 100) - Maximum items to return

**Usage Patterns:**
```python
# Sync
result = nodes_ops.browse(node_id="abc123-def456", max_items=100)

# Async  
result = await nodes_ops.browse_async(node_id="abc123-def456", max_items=100)

# Detailed (with full HTTP response)
result = nodes_ops.browse_detailed(node_id="abc123-def456", max_items=100)

# Detailed async
result = await nodes_ops.browse_detailed_async(node_id="abc123-def456", max_items=100)
```

#### `list_children(node_id: str, skip_count: int = 0, max_items: int = 100)`
List child nodes of a parent node.

**Parameters:**
- `node_id`: str - Parent node identifier
- `skip_count`: int (default: 0) - Number of items to skip
- `max_items`: int (default: 100) - Maximum items to return

**Usage Patterns:**
```python
# Sync
result = nodes_ops.list_children(node_id="abc123-def456", max_items=50)

# Async
result = await nodes_ops.list_children_async(node_id="abc123-def456", max_items=50)

# With pagination
result = nodes_ops.list_children(node_id="abc123-def456", skip_count=10, max_items=20)
```

### Parent & Hierarchy Operations

#### `list_parents(node_id: str, where: Optional[str] = None, include: Optional[List[str]] = None, fields: Optional[List[str]] = None)`
List parent nodes of a child node.

**Parameters:**
- `node_id`: str - Child node identifier
- `where`: Optional[str] - Filter conditions
- `include`: Optional[List[str]] - Include additional information
- `fields`: Optional[List[str]] - Fields to return

**Usage Patterns:**
```python
# Basic parent listing
result = nodes_ops.list_parents(node_id="abc123-def456")

# With filtering
result = nodes_ops.list_parents(node_id="abc123-def456", where="nodeType='cm:folder'")

# Async
result = await nodes_ops.list_parents_async(node_id="abc123-def456")
```

### Association Operations

#### `list_secondary_children(node_id: str, where: Optional[str] = None, include: Optional[List[str]] = None, fields: Optional[List[str]] = None)`
List secondary child associations.

**Parameters:**
- `node_id`: str - Parent node identifier
- `where`: Optional[str] - Filter conditions
- `include`: Optional[List[str]] - Include additional information
- `fields`: Optional[List[str]] - Fields to return

#### `list_source_associations(node_id: str, where: Optional[str] = None, include: Optional[List[str]] = None, fields: Optional[List[str]] = None)`
List source associations (incoming relationships).

**Parameters:**
- `node_id`: str - Target node identifier
- `where`: Optional[str] - Filter conditions
- `include`: Optional[List[str]] - Include additional information
- `fields`: Optional[List[str]] - Fields to return

#### `list_target_associations(node_id: str, where: Optional[str] = None, include: Optional[List[str]] = None, fields: Optional[List[str]] = None)`
List target associations (outgoing relationships).

**Parameters:**
- `node_id`: str - Source node identifier
- `where`: Optional[str] - Filter conditions
- `include`: Optional[List[str]] - Include additional information
- `fields`: Optional[List[str]] - Fields to return

**Usage Patterns:**
```python
# List associations
source_assocs = nodes_ops.list_source_associations(node_id="abc123-def456")
target_assocs = nodes_ops.list_target_associations(node_id="abc123-def456")
secondary_children = nodes_ops.list_secondary_children(node_id="abc123-def456")

# With filtering
filtered_assocs = nodes_ops.list_source_associations(
    node_id="abc123-def456", 
    where="assocType='cm:references'"
)

# Async versions
source_assocs = await nodes_ops.list_source_associations_async(node_id="abc123-def456")
target_assocs = await nodes_ops.list_target_associations_async(node_id="abc123-def456")
```

## Return Types

All browse and list operations return:
- **Sync/Async**: `NodeListResponse` - Contains list of nodes and pagination info
- **Detailed**: Full HTTP response with additional metadata

## Common Patterns

### Pagination
```python
# Get first page
page1 = nodes_ops.list_children(node_id="folder-id", max_items=10)

# Get next page
page2 = nodes_ops.list_children(node_id="folder-id", skip_count=10, max_items=10)
```

### Filtering
```python
# Filter by node type
folders_only = nodes_ops.list_children(
    node_id="folder-id",
    where="nodeType='cm:folder'"
)

# Filter by name pattern
docs = nodes_ops.list_children(
    node_id="folder-id", 
    where="name LIKE '%.pdf'"
)
```

### Async Processing
```python
async def process_folder_contents(folder_id: str):
    children = await nodes_ops.list_children_async(folder_id)
    
    for child in children.entries:
        parents = await nodes_ops.list_parents_async(child.id)
        # Process child and parents...
```

## See Also

- [Create Operations](create_operations.md) - Creating new nodes and associations
- [CRUD Operations](crud_operations.md) - Get, update, delete operations
- [Move & Copy Operations](move_copy_operations.md) - Moving and copying nodes
- [Lock Operations](lock_operations.md) - Locking and unlocking nodes
- [Main Nodes API](nodes_api.md) - Overview of all operations 