# Nodes Lock Operations

Auto-generated from V1.1 hierarchical code on 2025-07-15 00:36:43

## Overview

Lock operations for controlling concurrent access to nodes and implementing checkout/checkin workflows.

## Usage

```python
from python_alfresco_api import ClientFactory

# Create factory and client
factory = ClientFactory(base_url="http://localhost:8080")
core_client = factory.create_core_client()

# Access nodes operations
nodes_ops = core_client.nodes

# Lock operations
nodes_ops.lock(node_id="abc123-def456")
nodes_ops.unlock(node_id="abc123-def456")
```

## Available Operations

### Lock Operations

#### `lock(node_id: str, request: Optional[dict] = None, include: Optional[List[str]] = None)`
Lock a node to prevent concurrent modifications.

**Parameters:**
- `node_id`: str - Node identifier to lock
- `request`: Optional[dict] - Lock request with additional parameters
- `include`: Optional[List[str]] - Include additional information in response

**Usage Patterns:**
```python
# Basic lock
result = nodes_ops.lock(node_id="abc123-def456")

# Lock with specific request
lock_request = {
    "timeToExpire": 3600,  # 1 hour in seconds
    "type": "WRITE_LOCK"
}
result = nodes_ops.lock(node_id="abc123-def456", request=lock_request)

# Lock with include
result = nodes_ops.lock(
    node_id="abc123-def456",
    include=["properties", "permissions"]
)

# Async
result = await nodes_ops.lock_async(node_id="abc123-def456")

# Detailed (with full HTTP response)
response = nodes_ops.lock_detailed(node_id="abc123-def456")
```

### Unlock Operations

#### `unlock(node_id: str, include: Optional[List[str]] = None)`
Unlock a previously locked node.

**Parameters:**
- `node_id`: str - Node identifier to unlock
- `include`: Optional[List[str]] - Include additional information in response

**Usage Patterns:**
```python
# Basic unlock
result = nodes_ops.unlock(node_id="abc123-def456")

# Unlock with include
result = nodes_ops.unlock(
    node_id="abc123-def456",
    include=["properties", "permissions"]
)

# Async
result = await nodes_ops.unlock_async(node_id="abc123-def456")

# Detailed (with full HTTP response)
response = nodes_ops.unlock_detailed(node_id="abc123-def456")
```

## Return Types

- **lock/unlock**: `NodeResponse` - Contains updated node information with lock status
- **Detailed versions**: Full HTTP response with additional metadata

## Common Patterns

### Safe Lock/Unlock Pattern
```python
def safe_lock_operation(node_id: str, operation_func):
    """Perform operation with automatic lock/unlock."""
    
    try:
        # Lock the node
        lock_result = nodes_ops.lock(node_id)
        print(f"Locked node: {lock_result.entry.id}")
        
        # Perform the operation
        result = operation_func(node_id)
        
        return result
        
    except Exception as e:
        print(f"Operation failed: {e}")
        raise
        
    finally:
        # Always unlock, even if operation fails
        try:
            unlock_result = nodes_ops.unlock(node_id)
            print(f"Unlocked node: {unlock_result.entry.id}")
        except Exception as unlock_error:
            print(f"Warning: Failed to unlock node: {unlock_error}")
```

### Context Manager for Locking
```python
from contextlib import contextmanager

@contextmanager
def node_lock(node_id: str, lock_timeout: int = 3600):
    """Context manager for node locking."""
    
    lock_request = {"timeToExpire": lock_timeout}
    
    try:
        # Acquire lock
        lock_result = nodes_ops.lock(node_id, request=lock_request)
        print(f"Acquired lock on node: {lock_result.entry.id}")
        
        yield lock_result
        
    except Exception as e:
        print(f"Lock acquisition failed: {e}")
        raise
        
    finally:
        # Always release lock
        try:
            unlock_result = nodes_ops.unlock(node_id)
            print(f"Released lock on node: {unlock_result.entry.id}")
        except Exception as unlock_error:
            print(f"Warning: Failed to release lock: {unlock_error}")

# Usage
with node_lock("abc123-def456") as locked_node:
    # Perform operations on locked node
    update_request = UpdateNodeRequest(properties={"cm:title": "Updated Title"})
    nodes_ops.update(locked_node.entry.id, update_request)
```

### Bulk Lock Operations
```python
async def lock_multiple_nodes(node_ids: List[str], lock_timeout: int = 3600):
    """Lock multiple nodes concurrently."""
    
    lock_request = {"timeToExpire": lock_timeout}
    tasks = []
    
    for node_id in node_ids:
        task = nodes_ops.lock_async(node_id, request=lock_request)
        tasks.append(task)
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    # Process results
    successful_locks = []
    failed_locks = []
    
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            failed_locks.append({"node_id": node_ids[i], "error": str(result)})
        else:
            successful_locks.append(result)
    
    return {
        "successful_locks": successful_locks,
        "failed_locks": failed_locks
    }
```

### Document Checkout Workflow
```python
def checkout_document_workflow(document_id: str):
    """Implement document checkout workflow using locks."""
    
    try:
        # Lock the document for editing
        lock_result = nodes_ops.lock(document_id)
        
        # Check if lock was successful
        if lock_result.entry.properties.get("cm:lockType"):
            print(f"Document checked out: {lock_result.entry.name}")
            
            # Return checkout information
            return {
                "checked_out": True,
                "lock_owner": lock_result.entry.properties.get("cm:lockOwner"),
                "lock_type": lock_result.entry.properties.get("cm:lockType"),
                "node_id": document_id
            }
        else:
            return {"checked_out": False, "error": "Lock failed"}
            
    except Exception as e:
        return {"checked_out": False, "error": str(e)}

def checkin_document_workflow(document_id: str):
    """Implement document checkin workflow using unlock."""
    
    try:
        # Unlock the document
        unlock_result = nodes_ops.unlock(document_id)
        
        print(f"Document checked in: {unlock_result.entry.name}")
        
        return {
            "checked_in": True,
            "node_id": document_id
        }
        
    except Exception as e:
        return {"checked_in": False, "error": str(e)}
```

### Lock Status Check
```python
def check_lock_status(node_id: str):
    """Check if a node is locked and by whom."""
    
    try:
        node = nodes_ops.get(node_id, include=["properties"])
        
        properties = node.entry.properties
        
        lock_info = {
            "is_locked": bool(properties.get("cm:lockType")),
            "lock_type": properties.get("cm:lockType"),
            "lock_owner": properties.get("cm:lockOwner"),
            "lock_expires": properties.get("cm:expiryDate")
        }
        
        return lock_info
        
    except Exception as e:
        return {"error": str(e)}
```

### Force Unlock (Admin Operation)
```python
def force_unlock_node(node_id: str):
    """Force unlock a node (admin operation)."""
    
    try:
        # Check current lock status
        lock_status = check_lock_status(node_id)
        
        if not lock_status.get("is_locked"):
            return {"message": "Node is not locked"}
        
        # Force unlock
        result = nodes_ops.unlock(node_id)
        
        return {
            "success": True,
            "message": f"Force unlocked node {node_id}",
            "previous_owner": lock_status.get("lock_owner")
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
```

### Lock Timeout Handling
```python
def lock_with_timeout_handling(node_id: str, operation_func, max_wait_time: int = 300):
    """Lock node with timeout handling for busy resources."""
    
    import time
    
    start_time = time.time()
    
    while time.time() - start_time < max_wait_time:
        try:
            # Try to acquire lock
            lock_result = nodes_ops.lock(node_id)
            
            try:
                # Perform operation
                result = operation_func(node_id)
                return result
                
            finally:
                # Always unlock
                nodes_ops.unlock(node_id)
                
        except Exception as e:
            if "locked" in str(e).lower():
                # Node is locked, wait and retry
                print(f"Node is locked, waiting... ({int(time.time() - start_time)}s)")
                time.sleep(5)  # Wait 5 seconds before retry
                continue
            else:
                # Other error, re-raise
                raise
    
    raise TimeoutError(f"Could not acquire lock on node {node_id} within {max_wait_time} seconds")
```

## Best Practices

### 1. Always Use Try/Finally
```python
def safe_document_edit(document_id: str, new_content: bytes):
    """Safe document editing with proper lock handling."""
    
    try:
        # Lock document
        nodes_ops.lock(document_id)
        
        # Edit content
        nodes_ops.update_content(document_id, new_content)
        
    finally:
        # Always unlock
        try:
            nodes_ops.unlock(document_id)
        except:
            pass  # Ignore unlock errors
```

### 2. Check Lock Status Before Operations
```python
def smart_node_update(node_id: str, update_request):
    """Update node with smart lock handling."""
    
    # Check if already locked
    lock_status = check_lock_status(node_id)
    
    if lock_status.get("is_locked"):
        current_user = get_current_user()  # Your user detection logic
        
        if lock_status.get("lock_owner") == current_user:
            # We own the lock, proceed
            return nodes_ops.update(node_id, update_request)
        else:
            # Someone else owns the lock
            raise Exception(f"Node locked by {lock_status.get('lock_owner')}")
    
    # Not locked, acquire lock and update
    with node_lock(node_id):
        return nodes_ops.update(node_id, update_request)
```

### 3. Use Context Managers
```python
# Always prefer context managers for automatic cleanup
with node_lock("document-id") as locked_node:
    # Your operations here
    pass
```

## See Also

- [Browse Operations](browse_operations.md) - Exploring folder contents and relationships
- [Create Operations](create_operations.md) - Creating new nodes and associations
- [CRUD Operations](crud_operations.md) - Get, update, delete operations
- [Move & Copy Operations](move_copy_operations.md) - Moving and copying nodes
- [Main Nodes API](nodes_api.md) - Overview of all operations 