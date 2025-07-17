# Nodes CRUD Operations

Auto-generated from V1.1 hierarchical code on 2025-07-15 00:36:43

## Overview

CRUD operations for getting, updating, and deleting nodes and their content.

## Usage

```python
from python_alfresco_api import ClientFactory
from python_alfresco_api.clients.core.nodes.models import UpdateNodeRequest

# Create factory and client
factory = ClientFactory(base_url="http://localhost:8080")
core_client = factory.create_core_client()

# Access nodes operations
nodes_ops = core_client.nodes

# CRUD operations
node = nodes_ops.get(node_id="abc123-def456")
nodes_ops.update(node_id="abc123-def456", request=update_request)
nodes_ops.delete(node_id="abc123-def456")
```

## Available Operations

### Get Operations

#### `get(node_id: str, include: Optional[List[str]] = None, fields: Optional[List[str]] = None)`
Get a node by its identifier.

**Parameters:**
- `node_id`: str - Node identifier
- `include`: Optional[List[str]] - Include additional information (e.g., 'properties', 'permissions')
- `fields`: Optional[List[str]] - Specific fields to return

**Usage Patterns:**
```python
# Basic get
node = nodes_ops.get(node_id="abc123-def456")

# With properties and permissions
node = nodes_ops.get(
    node_id="abc123-def456",
    include=["properties", "permissions"]
)

# Specific fields only
node = nodes_ops.get(
    node_id="abc123-def456",
    fields=["id", "name", "nodeType"]
)

# Async
node = await nodes_ops.get_async(node_id="abc123-def456")

# Detailed (with full HTTP response)
response = nodes_ops.get_detailed(node_id="abc123-def456")
```

### Update Operations

#### `update(node_id: str, request: UpdateNodeRequest, include: Optional[List[str]] = None)`
Update a node's properties and metadata.

**Parameters:**
- `node_id`: str - Node identifier
- `request`: UpdateNodeRequest - Update request with properties, name, etc.
- `include`: Optional[List[str]] - Include additional information in response

**Usage Patterns:**
```python
from python_alfresco_api.clients.core.nodes.models import UpdateNodeRequest

# Update properties
request = UpdateNodeRequest(
    name="Updated Document.txt",
    properties={"cm:title": "Updated Title", "cm:description": "New description"}
)
result = nodes_ops.update(node_id="abc123-def456", request=request)

# With include
result = nodes_ops.update(
    node_id="abc123-def456",
    request=request,
    include=["properties", "permissions"]
)

# Async
result = await nodes_ops.update_async(node_id="abc123-def456", request=request)
```

#### `update_content(node_id: str, content: Union[bytes, IO[bytes]], filename: Optional[str] = None, include: Optional[List[str]] = None)`
Update a node's content (file data).

**Parameters:**
- `node_id`: str - Node identifier
- `content`: Union[bytes, IO[bytes]] - File content as bytes or file-like object
- `filename`: Optional[str] - Filename for the content
- `include`: Optional[List[str]] - Include additional information in response

**Usage Patterns:**
```python
# Update with bytes
content = b"Updated file content"
result = nodes_ops.update_content(
    node_id="abc123-def456",
    content=content,
    filename="updated_document.txt"
)

# Update with file object
with open("local_file.txt", "rb") as f:
    result = nodes_ops.update_content(
        node_id="abc123-def456",
        content=f,
        filename="document.txt"
    )

# Async
result = await nodes_ops.update_content_async(
    node_id="abc123-def456",
    content=content,
    filename="document.txt"
)
```

### Delete Operations

#### `delete(node_id: str, permanent: bool = False)`
Delete a node.

**Parameters:**
- `node_id`: str - Node identifier
- `permanent`: bool (default: False) - If True, permanently delete; if False, move to trash

**Usage Patterns:**
```python
# Move to trash
nodes_ops.delete(node_id="abc123-def456")

# Permanent deletion
nodes_ops.delete(node_id="abc123-def456", permanent=True)

# Async
await nodes_ops.delete_async(node_id="abc123-def456")

# Detailed (with full HTTP response)
response = nodes_ops.delete_detailed(node_id="abc123-def456")
```

#### `delete_association(node_id: str, target_id: str, assoc_type: Optional[str] = None)`
Delete an association between nodes.

**Parameters:**
- `node_id`: str - Source node identifier
- `target_id`: str - Target node identifier
- `assoc_type`: Optional[str] - Association type to delete (if None, deletes all associations)

**Usage Patterns:**
```python
# Delete specific association type
nodes_ops.delete_association(
    node_id="source-id",
    target_id="target-id",
    assoc_type="cm:references"
)

# Delete all associations
nodes_ops.delete_association(
    node_id="source-id",
    target_id="target-id"
)

# Async
await nodes_ops.delete_association_async(
    node_id="source-id",
    target_id="target-id",
    assoc_type="cm:references"
)
```

#### `delete_secondary_child_association(node_id: str, child_id: str, assoc_type: Optional[str] = None)`
Delete a secondary child association.

**Parameters:**
- `node_id`: str - Parent node identifier
- `child_id`: str - Child node identifier
- `assoc_type`: Optional[str] - Association type to delete

**Usage Patterns:**
```python
# Delete secondary child association
nodes_ops.delete_secondary_child_association(
    node_id="parent-id",
    child_id="child-id",
    assoc_type="cm:contains"
)

# Async
await nodes_ops.delete_secondary_child_association_async(
    node_id="parent-id",
    child_id="child-id",
    assoc_type="cm:contains"
)
```

## Return Types

- **get/update/update_content**: `NodeResponse` - Contains node information
- **delete**: `None` - No return value
- **Detailed versions**: Full HTTP response with additional metadata

## Common Patterns

### Safe Node Updates
```python
def update_node_safely(node_id: str, new_properties: dict):
    try:
        # Get current node
        current_node = nodes_ops.get(node_id, include=["properties"])
        
        # Merge properties
        merged_props = current_node.entry.properties.copy()
        merged_props.update(new_properties)
        
        # Update
        request = UpdateNodeRequest(properties=merged_props)
        return nodes_ops.update(node_id, request)
    except Exception as e:
        print(f"Update failed: {e}")
        return None
```

### Bulk Operations
```python
async def bulk_delete_nodes(node_ids: List[str], permanent: bool = False):
    tasks = []
    for node_id in node_ids:
        task = nodes_ops.delete_async(node_id, permanent=permanent)
        tasks.append(task)
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return results
```

### Content Management
```python
def update_document_content(node_id: str, file_path: str):
    """Update document content from local file."""
    try:
        with open(file_path, "rb") as f:
            result = nodes_ops.update_content(
                node_id=node_id,
                content=f,
                filename=os.path.basename(file_path)
            )
        return result
    except Exception as e:
        print(f"Content update failed: {e}")
        return None
```

### Property Management
```python
def set_node_property(node_id: str, property_name: str, property_value: str):
    """Set a single property on a node."""
    request = UpdateNodeRequest(properties={property_name: property_value})
    return nodes_ops.update(node_id, request)

def remove_node_property(node_id: str, property_name: str):
    """Remove a property from a node."""
    request = UpdateNodeRequest(properties={property_name: None})
    return nodes_ops.update(node_id, request)
```

### Error Handling
```python
def delete_node_with_retry(node_id: str, max_retries: int = 3):
    """Delete node with retry logic."""
    for attempt in range(max_retries):
        try:
            nodes_ops.delete(node_id)
            return True
        except Exception as e:
            if attempt == max_retries - 1:
                print(f"Failed to delete after {max_retries} attempts: {e}")
                return False
            time.sleep(1)  # Wait before retry
    return False
```

## See Also

- [Browse Operations](browse_operations.md) - Exploring folder contents and relationships
- [Create Operations](create_operations.md) - Creating new nodes and associations
- [Move & Copy Operations](move_copy_operations.md) - Moving and copying nodes
- [Lock Operations](lock_operations.md) - Locking and unlocking nodes
- [Main Nodes API](nodes_api.md) - Overview of all operations 