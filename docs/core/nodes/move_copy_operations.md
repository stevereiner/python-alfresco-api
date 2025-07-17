# Nodes Move & Copy Operations

Auto-generated from V1.1 hierarchical code on 2025-07-15 00:36:43

## Overview

Move and copy operations for relocating and duplicating nodes within the repository.

## Usage

```python
from python_alfresco_api import ClientFactory
from python_alfresco_api.clients.core.nodes.models import MoveNodeRequest, CopyNodeRequest

# Create factory and client
factory = ClientFactory(base_url="http://localhost:8080")
core_client = factory.create_core_client()

# Access nodes operations
nodes_ops = core_client.nodes

# Move and copy operations
move_request = MoveNodeRequest(targetParentId="new-parent-id")
copy_request = CopyNodeRequest(targetParentId="target-parent-id")

nodes_ops.move(node_id="abc123-def456", request=move_request)
nodes_ops.copy(node_id="abc123-def456", request=copy_request)
```

## Available Operations

### Move Operations

#### `move(node_id: str, request: MoveNodeRequest, include: Optional[List[str]] = None)`
Move a node to a new parent location.

**Parameters:**
- `node_id`: str - Node identifier to move
- `request`: MoveNodeRequest - Move request with target parent and optional new name
- `include`: Optional[List[str]] - Include additional information in response

**Usage Patterns:**
```python
from python_alfresco_api.clients.core.nodes.models import MoveNodeRequest

# Basic move
move_request = MoveNodeRequest(targetParentId="new-parent-id")
result = nodes_ops.move(node_id="abc123-def456", request=move_request)

# Move with rename
move_request = MoveNodeRequest(
    targetParentId="new-parent-id",
    name="new-name.txt"
)
result = nodes_ops.move(node_id="abc123-def456", request=move_request)

# With include
result = nodes_ops.move(
    node_id="abc123-def456",
    request=move_request,
    include=["properties", "path"]
)

# Async
result = await nodes_ops.move_async(node_id="abc123-def456", request=move_request)

# Detailed (with full HTTP response)
response = nodes_ops.move_detailed(node_id="abc123-def456", request=move_request)
```

### Copy Operations

#### `copy(node_id: str, request: CopyNodeRequest, include: Optional[List[str]] = None)`
Copy a node to a new location.

**Parameters:**
- `node_id`: str - Node identifier to copy
- `request`: CopyNodeRequest - Copy request with target parent and optional new name
- `include`: Optional[List[str]] - Include additional information in response

**Usage Patterns:**
```python
from python_alfresco_api.clients.core.nodes.models import CopyNodeRequest

# Basic copy
copy_request = CopyNodeRequest(targetParentId="target-parent-id")
result = nodes_ops.copy(node_id="abc123-def456", request=copy_request)

# Copy with rename
copy_request = CopyNodeRequest(
    targetParentId="target-parent-id",
    name="copied-file.txt"
)
result = nodes_ops.copy(node_id="abc123-def456", request=copy_request)

# Copy with include children (for folders)
copy_request = CopyNodeRequest(
    targetParentId="target-parent-id",
    includeChildren=True
)
result = nodes_ops.copy(node_id="folder-id", request=copy_request)

# Async
result = await nodes_ops.copy_async(node_id="abc123-def456", request=copy_request)

# Detailed (with full HTTP response)
response = nodes_ops.copy_detailed(node_id="abc123-def456", request=copy_request)
```

## Return Types

- **move/copy**: `NodeResponse` - Contains information about the moved/copied node
- **Detailed versions**: Full HTTP response with additional metadata

## Common Patterns

### Bulk Move Operations
```python
async def move_multiple_nodes(node_ids: List[str], target_parent_id: str):
    """Move multiple nodes to the same parent."""
    tasks = []
    for node_id in node_ids:
        request = MoveNodeRequest(targetParentId=target_parent_id)
        task = nodes_ops.move_async(node_id, request)
        tasks.append(task)
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return results
```

### Bulk Copy Operations
```python
async def copy_multiple_nodes(node_ids: List[str], target_parent_id: str):
    """Copy multiple nodes to the same parent."""
    tasks = []
    for node_id in node_ids:
        request = CopyNodeRequest(targetParentId=target_parent_id)
        task = nodes_ops.copy_async(node_id, request)
        tasks.append(task)
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return results
```

### Safe Move with Conflict Resolution
```python
def move_with_conflict_resolution(node_id: str, target_parent_id: str, new_name: str = None):
    """Move node with automatic conflict resolution."""
    try:
        # Get original node info
        original_node = nodes_ops.get(node_id)
        
        # Prepare move request
        request = MoveNodeRequest(
            targetParentId=target_parent_id,
            name=new_name or original_node.entry.name
        )
        
        # Attempt move
        result = nodes_ops.move(node_id, request)
        return result
        
    except Exception as e:
        if "already exists" in str(e).lower():
            # Handle name conflict
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            base_name = new_name or original_node.entry.name
            name_parts = base_name.rsplit('.', 1)
            
            if len(name_parts) == 2:
                conflict_name = f"{name_parts[0]}_{timestamp}.{name_parts[1]}"
            else:
                conflict_name = f"{base_name}_{timestamp}"
            
            request.name = conflict_name
            return nodes_ops.move(node_id, request)
        else:
            raise
```

### Copy with Property Updates
```python
def copy_and_update_properties(node_id: str, target_parent_id: str, new_properties: dict):
    """Copy node and update properties in one operation."""
    
    # Copy the node
    copy_request = CopyNodeRequest(targetParentId=target_parent_id)
    copied_node = nodes_ops.copy(node_id, copy_request)
    
    # Update properties on the copy
    if new_properties:
        from python_alfresco_api.clients.core.nodes.models import UpdateNodeRequest
        update_request = UpdateNodeRequest(properties=new_properties)
        nodes_ops.update(copied_node.entry.id, update_request)
    
    return copied_node
```

### Folder Structure Migration
```python
def migrate_folder_structure(source_folder_id: str, target_parent_id: str):
    """Migrate entire folder structure to new location."""
    
    # Get folder contents
    children = nodes_ops.list_children(source_folder_id, max_items=1000)
    
    # Move the folder itself
    move_request = MoveNodeRequest(targetParentId=target_parent_id)
    moved_folder = nodes_ops.move(source_folder_id, move_request)
    
    print(f"Moved folder {source_folder_id} to {moved_folder.entry.id}")
    return moved_folder
```

### Backup Copy Pattern
```python
def create_backup_copy(node_id: str, backup_folder_id: str):
    """Create a backup copy of a node with timestamp."""
    
    # Get original node
    original_node = nodes_ops.get(node_id)
    
    # Create backup name with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    original_name = original_node.entry.name
    
    if '.' in original_name:
        name_parts = original_name.rsplit('.', 1)
        backup_name = f"{name_parts[0]}_backup_{timestamp}.{name_parts[1]}"
    else:
        backup_name = f"{original_name}_backup_{timestamp}"
    
    # Copy to backup folder
    copy_request = CopyNodeRequest(
        targetParentId=backup_folder_id,
        name=backup_name
    )
    
    return nodes_ops.copy(node_id, copy_request)
```

### Error Handling
```python
def safe_move_operation(node_id: str, target_parent_id: str):
    """Move operation with comprehensive error handling."""
    
    try:
        # Verify source node exists
        source_node = nodes_ops.get(node_id)
        
        # Verify target parent exists
        target_parent = nodes_ops.get(target_parent_id)
        
        # Perform move
        request = MoveNodeRequest(targetParentId=target_parent_id)
        result = nodes_ops.move(node_id, request)
        
        return {
            "success": True,
            "result": result,
            "message": f"Successfully moved {source_node.entry.name}"
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": f"Failed to move node {node_id}"
        }
```

## Performance Considerations

### Large Folder Operations
```python
def move_large_folder_with_progress(folder_id: str, target_parent_id: str, 
                                   progress_callback=None):
    """Move large folder with progress tracking."""
    
    # Get folder size first
    folder_info = nodes_ops.get(folder_id, include=["properties"])
    
    if progress_callback:
        progress_callback(f"Starting move of {folder_info.entry.name}")
    
    # Perform move (Alfresco handles children automatically)
    request = MoveNodeRequest(targetParentId=target_parent_id)
    result = nodes_ops.move(folder_id, request)
    
    if progress_callback:
        progress_callback(f"Move completed: {result.entry.id}")
    
    return result
```

## See Also

- [Browse Operations](browse_operations.md) - Exploring folder contents and relationships
- [Create Operations](create_operations.md) - Creating new nodes and associations
- [CRUD Operations](crud_operations.md) - Get, update, delete operations
- [Lock Operations](lock_operations.md) - Locking and unlocking nodes
- [Main Nodes API](nodes_api.md) - Overview of all operations 