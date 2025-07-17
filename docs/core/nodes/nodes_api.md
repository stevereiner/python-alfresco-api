# Nodes API - Core Operations

Auto-generated from V1.1 hierarchical code on 2025-07-15 00:36:43

## Overview

The Nodes API provides comprehensive operations for managing nodes (files, folders, and other content) in the Alfresco repository. This API is organized into logical operation groups for better navigation and maintainability.

## Quick Start

```python
from python_alfresco_api import ClientFactory

# Create factory and client
factory = ClientFactory(base_url="http://localhost:8080")
core_client = factory.create_core_client()

# Access nodes operations
nodes_ops = core_client.nodes

# Common operations
folder = nodes_ops.create_folder(name="My Folder", parent_id="-my-")
children = nodes_ops.list_children(folder.entry.id)
node = nodes_ops.get(node_id="abc123-def456")
```

## Operation Groups

The Nodes API contains **80+ operations** organized into 5 main groups:

### 🗂️ [Browse & List Operations](browse_operations.md)
**6 operations** for exploring folder contents, relationships, and hierarchies.

- `browse()` - Convenience method for browsing folder contents
- `list_children()` - List child nodes of a parent
- `list_parents()` - List parent nodes of a child
- `list_secondary_children()` - List secondary child associations
- `list_source_associations()` - List incoming relationships
- `list_target_associations()` - List outgoing relationships

**[→ View Browse Operations Documentation](browse_operations.md)**

### ➕ [Create Operations](create_operations.md)
**12+ operations** for creating new nodes, folders, and associations.

- `create()` - Create a new node with full control
- `create_folder()` - Convenience method for creating folders
- `create_association()` - Create associations between nodes
- `create_secondary_child_association()` - Create secondary child associations
- Plus convenience variants and detailed operations

**[→ View Create Operations Documentation](create_operations.md)**

### 🔧 [CRUD Operations](crud_operations.md)
**20+ operations** for getting, updating, and deleting nodes.

- `get()` - Get a node by identifier
- `update()` - Update node properties and metadata
- `update_content()` - Update node content (file data)
- `delete()` - Delete nodes (trash or permanent)
- `delete_association()` - Delete associations
- `delete_secondary_child_association()` - Delete secondary associations
- Plus async and detailed variants

**[→ View CRUD Operations Documentation](crud_operations.md)**

### 📁 [Move & Copy Operations](move_copy_operations.md)
**8 operations** for relocating and duplicating nodes.

- `move()` - Move a node to a new parent location
- `copy()` - Copy a node to a new location
- Plus async and detailed variants

**[→ View Move & Copy Operations Documentation](move_copy_operations.md)**

### 🔒 [Lock Operations](lock_operations.md)
**8 operations** for controlling concurrent access to nodes.

- `lock()` - Lock a node to prevent concurrent modifications
- `unlock()` - Unlock a previously locked node
- Plus async and detailed variants

**[→ View Lock Operations Documentation](lock_operations.md)**

## Operation Patterns

All operations follow consistent patterns:

### 4-Pattern Implementation
Each operation is available in 4 variants:
1. **Basic Sync**: `operation()`
2. **Basic Async**: `operation_async()`
3. **Detailed Sync**: `operation_detailed()` (with full HTTP response)
4. **Detailed Async**: `operation_detailed_async()`

### Common Parameters
- `node_id`: str - Node identifier
- `include`: Optional[List[str]] - Include additional information (e.g., 'properties', 'permissions')
- `fields`: Optional[List[str]] - Specific fields to return

### Return Types
- **Basic operations**: Pydantic models (NodeResponse, NodeListResponse, etc.)
- **Detailed operations**: Full HTTP response with additional metadata

## Authentication & Setup

```python
from python_alfresco_api import ClientFactory
from python_alfresco_api.auth_util import AuthUtil

# Setup authentication
auth = AuthUtil('username', 'password')
factory = ClientFactory(
    base_url='http://localhost:8080',
    auth_util=auth,
    verify_ssl=False
)

# Create client
core_client = factory.create_core_client()
nodes_ops = core_client.nodes
```

## Error Handling

```python
try:
    result = nodes_ops.get(node_id="abc123-def456")
except Exception as e:
    print(f"Operation failed: {e}")
    # Handle error appropriately
```

## Async Usage

```python
import asyncio

async def async_operations():
    # Async operations
    node = await nodes_ops.get_async(node_id="abc123-def456")
    children = await nodes_ops.list_children_async(node.entry.id)
    
    # Concurrent operations
    tasks = [
        nodes_ops.get_async(node_id="node1"),
        nodes_ops.get_async(node_id="node2"),
        nodes_ops.get_async(node_id="node3")
    ]
    results = await asyncio.gather(*tasks)

# Run async operations
asyncio.run(async_operations())
```

## Performance Tips

1. **Use async operations** for concurrent processing
2. **Batch operations** when possible to reduce API calls
3. **Use pagination** for large result sets
4. **Cache node IDs** to avoid repeated lookups
5. **Use include parameters** to get additional data in one call

## Related Documentation

- [Core API Overview](../core_api.md) - Main Core API documentation
- [Models Documentation](../core_models.md) - Pydantic models and data structures
- [Authentication Guide](../../AUTHENTICATION_GUIDE.md) - Authentication setup
- [V1.1 Architecture](../../clients_doc.md) - Overall client architecture

## Operation Summary

| Operation Group | Operations | Description |
|---|---|---|
| [Browse & List](browse_operations.md) | 6 | Explore folder contents, relationships, hierarchies |
| [Create](create_operations.md) | 12+ | Create new nodes, folders, and associations |
| [CRUD](crud_operations.md) | 20+ | Get, update, delete nodes and content |
| [Move & Copy](move_copy_operations.md) | 8 | Relocate and duplicate nodes |
| [Lock](lock_operations.md) | 8 | Control concurrent access to nodes |
| **Total** | **80+** | **Complete node management operations** |

---

*This documentation is auto-generated from the V1.1 hierarchical architecture. For the most up-to-date information, refer to the operation-specific documentation files.*
