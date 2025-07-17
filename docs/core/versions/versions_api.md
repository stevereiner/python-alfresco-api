# Versions Operations - Core API

Auto-generated from V1.1 hierarchical code on 2025-07-15 00:36:43

## Overview

Versions operations for the Core API.

## Usage

```python
from python_alfresco_api import ClientFactory

# Create factory and client
factory = ClientFactory(base_url="http://localhost:8080")
core_client = factory.create_core_client()

# Access versions operations
versions_ops = core_client.versions

# Real method examples (sync):
result = versions_ops.cancel_checkout(node_id="abc123-def456", kwargs=...)
result = versions_ops.cancel_checkout_async(node_id="abc123-def456")
result = versions_ops.cancel_checkout_detailed(node_id="abc123-def456", kwargs=...)

# Real method examples (async):
result = await versions_ops.cancel_checkout_async(node_id="abc123-def456", kwargs=...)
result = await versions_ops.cancel_checkout_async_async(node_id="abc123-def456")
result = await versions_ops.cancel_checkout_detailed_async(node_id="abc123-def456", kwargs=...)
```

## Available Methods

This subsection provides 14 operations:

### `cancel_checkout(self, node_id: str, **kwargs) -> python_alfresco_api.clients.core.versions.models.CheckoutResponse`

Cancel checkout (unlock) a document.

Perfect for canceling editing sessions without creating versions.
Unlocks the document and discards any working copy.

Args:
    node_id: ID of the document to unlock
    
Returns:
    CheckoutResponse: Response with unlock details

**Parameters:**
- `node_id`: <class 'str'> (required)
- `kwargs`: Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = versions_ops.cancel_checkout(node_id="abc123-def456", kwargs=...)

# 2. Basic async
result = await versions_ops.cancel_checkout_async(node_id="abc123-def456", kwargs=...)

# 3. Detailed sync (with full HTTP response)
result = versions_ops.cancel_checkout_detailed(node_id="abc123-def456", kwargs=...)

# 4. Detailed async (with full HTTP response)
result = await versions_ops.cancel_checkout_detailed_async(node_id="abc123-def456", kwargs=...)
```

### `cancel_checkout_async(self, node_id: str) -> python_alfresco_api.clients.core.versions.models.CheckoutResponse`

Async version of cancel_checkout.

**Parameters:**
- `node_id`: <class 'str'> (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = versions_ops.cancel_checkout_async(node_id="abc123-def456")

# 2. Basic async
result = await versions_ops.cancel_checkout_async_async(node_id="abc123-def456")

# 3. Detailed sync (with full HTTP response)
result = versions_ops.cancel_checkout_async_detailed(node_id="abc123-def456")

# 4. Detailed async (with full HTTP response)
result = await versions_ops.cancel_checkout_async_detailed_async(node_id="abc123-def456")
```

### `cancel_checkout_detailed(self, node_id: str, **kwargs)`

Cancel checkout operation (detailed sync).

Returns complete Response object with status_code, headers, content, parsed.

Returns:
    Response: Complete response with status_code, headers, content, parsed

**Parameters:**
- `node_id`: <class 'str'> (required)
- `kwargs`: Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = versions_ops.cancel_checkout_detailed(node_id="abc123-def456", kwargs=...)

# 2. Basic async
result = await versions_ops.cancel_checkout_detailed_async(node_id="abc123-def456", kwargs=...)

# 3. Detailed sync (with full HTTP response)
result = versions_ops.cancel_checkout_detailed_detailed(node_id="abc123-def456", kwargs=...)

# 4. Detailed async (with full HTTP response)
result = await versions_ops.cancel_checkout_detailed_detailed_async(node_id="abc123-def456", kwargs=...)
```

### `cancel_checkout_detailed_async(self, node_id: str, **kwargs)`

Cancel checkout operation (detailed async).

Returns complete Response object with status_code, headers, content, parsed.

Returns:
    Response: Complete response with status_code, headers, content, parsed

**Parameters:**
- `node_id`: <class 'str'> (required)
- `kwargs`: Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = versions_ops.cancel_checkout_detailed_async(node_id="abc123-def456", kwargs=...)

# 2. Basic async
result = await versions_ops.cancel_checkout_detailed_async_async(node_id="abc123-def456", kwargs=...)

# 3. Detailed sync (with full HTTP response)
result = versions_ops.cancel_checkout_detailed_async_detailed(node_id="abc123-def456", kwargs=...)

# 4. Detailed async (with full HTTP response)
result = await versions_ops.cancel_checkout_detailed_async_detailed_async(node_id="abc123-def456", kwargs=...)
```

### `checkin(self, node_id: str, comment: Optional[str] = None, major_version: bool = False, **kwargs) -> python_alfresco_api.clients.core.versions.models.CheckinResponse`

Checkin (save) document changes as new version.

Perfect for finalizing document edits and creating versions.
Creates a new version and unlocks the document.

Args:
    node_id: ID of the document to checkin
    comment: Version comment
    major_version: Create major version (default: minor)
    
Returns:
    CheckinResponse: Response with new version details

**Parameters:**
- `node_id`: <class 'str'> (required)
- `comment`: typing.Optional[str] (default: None)
- `major_version`: <class 'bool'> (default: False)
- `kwargs`: Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = versions_ops.checkin(node_id="abc123-def456", comment="example", major_version=True, kwargs=...)

# 2. Basic async
result = await versions_ops.checkin_async(node_id="abc123-def456", comment="example", major_version=True, kwargs=...)

# 3. Detailed sync (with full HTTP response)
result = versions_ops.checkin_detailed(node_id="abc123-def456", comment="example", major_version=True, kwargs=...)

# 4. Detailed async (with full HTTP response)
result = await versions_ops.checkin_detailed_async(node_id="abc123-def456", comment="example", major_version=True, kwargs=...)
```

### `checkin_async(self, node_id: str, comment: Optional[str] = None, major_version: bool = False) -> python_alfresco_api.clients.core.versions.models.CheckinResponse`

Async version of checkin.

**Parameters:**
- `node_id`: <class 'str'> (required)
- `comment`: typing.Optional[str] (default: None)
- `major_version`: <class 'bool'> (default: False)

**Usage Patterns:**
```python
# 1. Basic sync
result = versions_ops.checkin_async(node_id="abc123-def456", comment="example", major_version=True)

# 2. Basic async
result = await versions_ops.checkin_async_async(node_id="abc123-def456", comment="example", major_version=True)

# 3. Detailed sync (with full HTTP response)
result = versions_ops.checkin_async_detailed(node_id="abc123-def456", comment="example", major_version=True)

# 4. Detailed async (with full HTTP response)
result = await versions_ops.checkin_async_detailed_async(node_id="abc123-def456", comment="example", major_version=True)
```

### `checkin_detailed(self, node_id: str, comment: Optional[str] = None, major_version: bool = False, **kwargs)`

Checkin operation (detailed sync).

Returns complete Response object with status_code, headers, content, parsed.

Returns:
    Response: Complete response with status_code, headers, content, parsed

**Parameters:**
- `node_id`: <class 'str'> (required)
- `comment`: typing.Optional[str] (default: None)
- `major_version`: <class 'bool'> (default: False)
- `kwargs`: Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = versions_ops.checkin_detailed(node_id="abc123-def456", comment="example", major_version=True, kwargs=...)

# 2. Basic async
result = await versions_ops.checkin_detailed_async(node_id="abc123-def456", comment="example", major_version=True, kwargs=...)

# 3. Detailed sync (with full HTTP response)
result = versions_ops.checkin_detailed_detailed(node_id="abc123-def456", comment="example", major_version=True, kwargs=...)

# 4. Detailed async (with full HTTP response)
result = await versions_ops.checkin_detailed_detailed_async(node_id="abc123-def456", comment="example", major_version=True, kwargs=...)
```

### `checkin_detailed_async(self, node_id: str, comment: Optional[str] = None, major_version: bool = False, **kwargs)`

Checkin operation (detailed async).

Returns complete Response object with status_code, headers, content, parsed.

Returns:
    Response: Complete response with status_code, headers, content, parsed

**Parameters:**
- `node_id`: <class 'str'> (required)
- `comment`: typing.Optional[str] (default: None)
- `major_version`: <class 'bool'> (default: False)
- `kwargs`: Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = versions_ops.checkin_detailed_async(node_id="abc123-def456", comment="example", major_version=True, kwargs=...)

# 2. Basic async
result = await versions_ops.checkin_detailed_async_async(node_id="abc123-def456", comment="example", major_version=True, kwargs=...)

# 3. Detailed sync (with full HTTP response)
result = versions_ops.checkin_detailed_async_detailed(node_id="abc123-def456", comment="example", major_version=True, kwargs=...)

# 4. Detailed async (with full HTTP response)
result = await versions_ops.checkin_detailed_async_detailed_async(node_id="abc123-def456", comment="example", major_version=True, kwargs=...)
```

### `checkout(self, node_id: str, **kwargs) -> python_alfresco_api.clients.core.versions.models.CheckoutResponse`

Checkout (lock) a document for editing.

Perfect for MCP servers and collaborative document workflows.
Locks the document to prevent concurrent modifications.

Args:
    node_id: ID of the document to checkout
    
Returns:
    CheckoutResponse: Response with checkout details

**Parameters:**
- `node_id`: <class 'str'> (required)
- `kwargs`: Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = versions_ops.checkout(node_id="abc123-def456", kwargs=...)

# 2. Basic async
result = await versions_ops.checkout_async(node_id="abc123-def456", kwargs=...)

# 3. Detailed sync (with full HTTP response)
result = versions_ops.checkout_detailed(node_id="abc123-def456", kwargs=...)

# 4. Detailed async (with full HTTP response)
result = await versions_ops.checkout_detailed_async(node_id="abc123-def456", kwargs=...)
```

### `checkout_async(self, node_id: str) -> python_alfresco_api.clients.core.versions.models.CheckoutResponse`

Async version of checkout.

**Parameters:**
- `node_id`: <class 'str'> (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = versions_ops.checkout_async(node_id="abc123-def456")

# 2. Basic async
result = await versions_ops.checkout_async_async(node_id="abc123-def456")

# 3. Detailed sync (with full HTTP response)
result = versions_ops.checkout_async_detailed(node_id="abc123-def456")

# 4. Detailed async (with full HTTP response)
result = await versions_ops.checkout_async_detailed_async(node_id="abc123-def456")
```

### `checkout_detailed(self, node_id: str, **kwargs)`

Checkout operation (detailed sync).

Returns complete Response object with status_code, headers, content, parsed.

Returns:
    Response: Complete response with status_code, headers, content, parsed

**Parameters:**
- `node_id`: <class 'str'> (required)
- `kwargs`: Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = versions_ops.checkout_detailed(node_id="abc123-def456", kwargs=...)

# 2. Basic async
result = await versions_ops.checkout_detailed_async(node_id="abc123-def456", kwargs=...)

# 3. Detailed sync (with full HTTP response)
result = versions_ops.checkout_detailed_detailed(node_id="abc123-def456", kwargs=...)

# 4. Detailed async (with full HTTP response)
result = await versions_ops.checkout_detailed_detailed_async(node_id="abc123-def456", kwargs=...)
```

### `checkout_detailed_async(self, node_id: str, **kwargs)`

Checkout operation (detailed async).

Returns complete Response object with status_code, headers, content, parsed.

Returns:
    Response: Complete response with status_code, headers, content, parsed

**Parameters:**
- `node_id`: <class 'str'> (required)
- `kwargs`: Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = versions_ops.checkout_detailed_async(node_id="abc123-def456", kwargs=...)

# 2. Basic async
result = await versions_ops.checkout_detailed_async_async(node_id="abc123-def456", kwargs=...)

# 3. Detailed sync (with full HTTP response)
result = versions_ops.checkout_detailed_async_detailed(node_id="abc123-def456", kwargs=...)

# 4. Detailed async (with full HTTP response)
result = await versions_ops.checkout_detailed_async_detailed_async(node_id="abc123-def456", kwargs=...)
```

### `enable_versioning(self, node_id: str, major_version: bool = True, **kwargs) -> dict`

Enable versioning on an existing node.

Perfect for MCP servers that need to enable versioning after node creation.
This method creates an initial version for the node.

Args:
    node_id (str): ID of the node to enable versioning for
    major_version (bool): Whether to create as major version (default: True)
    **kwargs: Additional parameters passed to the raw client
    
Returns:
    dict: Response containing version information
    
Examples:
    ```python
    # Enable versioning with major version
    version_info = client.versions.enable_versioning(
        node_id="abc123-def456",
        major_version=True
    )
    
    # Enable versioning with minor version
    version_info = client.versions.enable_versioning(
        node_id="abc123-def456", 
        major_version=False
    )
    ```
    
Raises:
    NodeNotFoundError: Node doesn't exist
    PermissionError: User lacks permission to modify versioning
    ValidationError: Invalid node for versioning

**Parameters:**
- `node_id`: <class 'str'> (required)
- `major_version`: <class 'bool'> (default: True)
- `kwargs`: Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = versions_ops.enable_versioning(node_id="abc123-def456", major_version=True, kwargs=...)

# 2. Basic async
result = await versions_ops.enable_versioning_async(node_id="abc123-def456", major_version=True, kwargs=...)

# 3. Detailed sync (with full HTTP response)
result = versions_ops.enable_versioning_detailed(node_id="abc123-def456", major_version=True, kwargs=...)

# 4. Detailed async (with full HTTP response)
result = await versions_ops.enable_versioning_detailed_async(node_id="abc123-def456", major_version=True, kwargs=...)
```

### `enable_versioning_async(self, node_id: str, major_version: bool = True, **kwargs) -> dict`

Enable versioning on an existing node (async).

Perfect for web applications that need to enable versioning after node creation.
This method creates an initial version for the node.

Args:
    node_id (str): ID of the node to enable versioning for
    major_version (bool): Whether to create as major version (default: True)
    **kwargs: Additional parameters passed to the raw client
    
Returns:
    dict: Response containing version information
    
Examples:
    ```python
    # Enable versioning with major version
    version_info = await client.versions.enable_versioning_async(
        node_id="abc123-def456",
        major_version=True
    )
    ```
    
Raises:
    NodeNotFoundError: Node doesn't exist
    PermissionError: User lacks permission to modify versioning
    ValidationError: Invalid node for versioning

**Parameters:**
- `node_id`: <class 'str'> (required)
- `major_version`: <class 'bool'> (default: True)
- `kwargs`: Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = versions_ops.enable_versioning_async(node_id="abc123-def456", major_version=True, kwargs=...)

# 2. Basic async
result = await versions_ops.enable_versioning_async_async(node_id="abc123-def456", major_version=True, kwargs=...)

# 3. Detailed sync (with full HTTP response)
result = versions_ops.enable_versioning_async_detailed(node_id="abc123-def456", major_version=True, kwargs=...)

# 4. Detailed async (with full HTTP response)
result = await versions_ops.enable_versioning_async_detailed_async(node_id="abc123-def456", major_version=True, kwargs=...)
```

## Models

Operation-specific Pydantic models are available in:
```python
from python_alfresco_api.clients.core.versions.models import *
```

## Related Documentation

- [Core API Overview](../core_api.md)
- [V1.1 Architecture](../../clients_doc.md)
