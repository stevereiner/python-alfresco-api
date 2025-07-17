# Comments Operations - Core API

Auto-generated from V1.1 hierarchical code on 2025-07-15 00:36:43

## Overview

Comments operations for the Core API.

## Usage

```python
from python_alfresco_api import ClientFactory

# Create factory and client
factory = ClientFactory(base_url="http://localhost:8080")
core_client = factory.create_core_client()

# Access comments operations
comments_ops = core_client.comments

# Real method examples (sync):
result = comments_ops.create_comment(node_id="abc123-def456", body=request_data, fields=...)
result = comments_ops.create_comment_async(node_id="abc123-def456", body=request_data, fields=...)
result = comments_ops.create_comment_detailed(node_id="abc123-def456", body=request_data, fields=...)

# Real method examples (async):
result = await comments_ops.create_comment_async(node_id="abc123-def456", body=request_data, fields=...)
result = await comments_ops.create_comment_async_async(node_id="abc123-def456", body=request_data, fields=...)
result = await comments_ops.create_comment_detailed_async(node_id="abc123-def456", body=request_data, fields=...)
```

## Available Methods

This subsection provides 17 operations:

### `create_comment(self, node_id: Any, body: Any, fields: Any) -> python_alfresco_api.clients.core.comments.models.CommentsResponse`

Create Comment operation.

Perfect for MCP servers and comments workflows.
Returns simplified response for common use cases.

**Parameters:**
- `node_id`: typing.Any (required)
- `body`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = comments_ops.create_comment(node_id="abc123-def456", body=request_data, fields=...)

# 2. Basic async
result = await comments_ops.create_comment_async(node_id="abc123-def456", body=request_data, fields=...)

# 3. Detailed sync (with full HTTP response)
result = comments_ops.create_comment_detailed(node_id="abc123-def456", body=request_data, fields=...)

# 4. Detailed async (with full HTTP response)
result = await comments_ops.create_comment_detailed_async(node_id="abc123-def456", body=request_data, fields=...)
```

### `create_comment_async(self, node_id: Any, body: Any, fields: Any) -> python_alfresco_api.clients.core.comments.models.CommentsResponse`

Create Comment operation (async).

Perfect for MCP servers and comments workflows.
Returns simplified response for common use cases.

**Parameters:**
- `node_id`: typing.Any (required)
- `body`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = comments_ops.create_comment_async(node_id="abc123-def456", body=request_data, fields=...)

# 2. Basic async
result = await comments_ops.create_comment_async_async(node_id="abc123-def456", body=request_data, fields=...)

# 3. Detailed sync (with full HTTP response)
result = comments_ops.create_comment_async_detailed(node_id="abc123-def456", body=request_data, fields=...)

# 4. Detailed async (with full HTTP response)
result = await comments_ops.create_comment_async_detailed_async(node_id="abc123-def456", body=request_data, fields=...)
```

### `create_comment_detailed(self, node_id: Any, body: Any, fields: Any)`

Create Comment operation (detailed).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `node_id`: typing.Any (required)
- `body`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = comments_ops.create_comment_detailed(node_id="abc123-def456", body=request_data, fields=...)

# 2. Basic async
result = await comments_ops.create_comment_detailed_async(node_id="abc123-def456", body=request_data, fields=...)

# 3. Detailed sync (with full HTTP response)
result = comments_ops.create_comment_detailed_detailed(node_id="abc123-def456", body=request_data, fields=...)

# 4. Detailed async (with full HTTP response)
result = await comments_ops.create_comment_detailed_detailed_async(node_id="abc123-def456", body=request_data, fields=...)
```

### `create_comment_detailed_async(self, node_id: Any, body: Any, fields: Any)`

Create Comment operation (detailed, async).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `node_id`: typing.Any (required)
- `body`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = comments_ops.create_comment_detailed_async(node_id="abc123-def456", body=request_data, fields=...)

# 2. Basic async
result = await comments_ops.create_comment_detailed_async_async(node_id="abc123-def456", body=request_data, fields=...)

# 3. Detailed sync (with full HTTP response)
result = comments_ops.create_comment_detailed_async_detailed(node_id="abc123-def456", body=request_data, fields=...)

# 4. Detailed async (with full HTTP response)
result = await comments_ops.create_comment_detailed_async_detailed_async(node_id="abc123-def456", body=request_data, fields=...)
```

### `delete_comment(self, node_id: Any, comment_id: Any) -> python_alfresco_api.clients.core.comments.models.CommentsResponse`

Delete Comment operation.

Perfect for MCP servers and comments workflows.
Returns simplified response for common use cases.

**Parameters:**
- `node_id`: typing.Any (required)
- `comment_id`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = comments_ops.delete_comment(node_id="abc123-def456", comment_id="abc123-def456")

# 2. Basic async
result = await comments_ops.delete_comment_async(node_id="abc123-def456", comment_id="abc123-def456")

# 3. Detailed sync (with full HTTP response)
result = comments_ops.delete_comment_detailed(node_id="abc123-def456", comment_id="abc123-def456")

# 4. Detailed async (with full HTTP response)
result = await comments_ops.delete_comment_detailed_async(node_id="abc123-def456", comment_id="abc123-def456")
```

### `delete_comment_async(self, node_id: Any, comment_id: Any) -> python_alfresco_api.clients.core.comments.models.CommentsResponse`

Delete Comment operation (async).

Perfect for MCP servers and comments workflows.
Returns simplified response for common use cases.

**Parameters:**
- `node_id`: typing.Any (required)
- `comment_id`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = comments_ops.delete_comment_async(node_id="abc123-def456", comment_id="abc123-def456")

# 2. Basic async
result = await comments_ops.delete_comment_async_async(node_id="abc123-def456", comment_id="abc123-def456")

# 3. Detailed sync (with full HTTP response)
result = comments_ops.delete_comment_async_detailed(node_id="abc123-def456", comment_id="abc123-def456")

# 4. Detailed async (with full HTTP response)
result = await comments_ops.delete_comment_async_detailed_async(node_id="abc123-def456", comment_id="abc123-def456")
```

### `delete_comment_detailed(self, node_id: Any, comment_id: Any)`

Delete Comment operation (detailed).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `node_id`: typing.Any (required)
- `comment_id`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = comments_ops.delete_comment_detailed(node_id="abc123-def456", comment_id="abc123-def456")

# 2. Basic async
result = await comments_ops.delete_comment_detailed_async(node_id="abc123-def456", comment_id="abc123-def456")

# 3. Detailed sync (with full HTTP response)
result = comments_ops.delete_comment_detailed_detailed(node_id="abc123-def456", comment_id="abc123-def456")

# 4. Detailed async (with full HTTP response)
result = await comments_ops.delete_comment_detailed_detailed_async(node_id="abc123-def456", comment_id="abc123-def456")
```

### `delete_comment_detailed_async(self, node_id: Any, comment_id: Any)`

Delete Comment operation (detailed, async).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `node_id`: typing.Any (required)
- `comment_id`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = comments_ops.delete_comment_detailed_async(node_id="abc123-def456", comment_id="abc123-def456")

# 2. Basic async
result = await comments_ops.delete_comment_detailed_async_async(node_id="abc123-def456", comment_id="abc123-def456")

# 3. Detailed sync (with full HTTP response)
result = comments_ops.delete_comment_detailed_async_detailed(node_id="abc123-def456", comment_id="abc123-def456")

# 4. Detailed async (with full HTTP response)
result = await comments_ops.delete_comment_detailed_async_detailed_async(node_id="abc123-def456", comment_id="abc123-def456")
```

### `get_httpx_client(self)`

Get direct access to raw httpx client for advanced operations.

Perfect for MCP servers that need raw HTTP access.

**Usage Patterns:**
```python
# 1. Basic sync
result = comments_ops.get_httpx_client()

# 2. Basic async
result = await comments_ops.get_httpx_client_async()

# 3. Detailed sync (with full HTTP response)
result = comments_ops.get_httpx_client_detailed()

# 4. Detailed async (with full HTTP response)
result = await comments_ops.get_httpx_client_detailed_async()
```

### `list_comments(self, node_id: Any, skip_count: Any, max_items: Any, fields: Any) -> python_alfresco_api.clients.core.comments.models.CommentsResponse`

List Comments operation.

Perfect for MCP servers and comments workflows.
Returns simplified response for common use cases.

**Parameters:**
- `node_id`: typing.Any (required)
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = comments_ops.list_comments(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)

# 2. Basic async
result = await comments_ops.list_comments_async(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)

# 3. Detailed sync (with full HTTP response)
result = comments_ops.list_comments_detailed(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)

# 4. Detailed async (with full HTTP response)
result = await comments_ops.list_comments_detailed_async(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)
```

### `list_comments_async(self, node_id: Any, skip_count: Any, max_items: Any, fields: Any) -> python_alfresco_api.clients.core.comments.models.CommentsResponse`

List Comments operation (async).

Perfect for MCP servers and comments workflows.
Returns simplified response for common use cases.

**Parameters:**
- `node_id`: typing.Any (required)
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = comments_ops.list_comments_async(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)

# 2. Basic async
result = await comments_ops.list_comments_async_async(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)

# 3. Detailed sync (with full HTTP response)
result = comments_ops.list_comments_async_detailed(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)

# 4. Detailed async (with full HTTP response)
result = await comments_ops.list_comments_async_detailed_async(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)
```

### `list_comments_detailed(self, node_id: Any, skip_count: Any, max_items: Any, fields: Any)`

List Comments operation (detailed).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `node_id`: typing.Any (required)
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = comments_ops.list_comments_detailed(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)

# 2. Basic async
result = await comments_ops.list_comments_detailed_async(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)

# 3. Detailed sync (with full HTTP response)
result = comments_ops.list_comments_detailed_detailed(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)

# 4. Detailed async (with full HTTP response)
result = await comments_ops.list_comments_detailed_detailed_async(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)
```

### `list_comments_detailed_async(self, node_id: Any, skip_count: Any, max_items: Any, fields: Any)`

List Comments operation (detailed, async).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `node_id`: typing.Any (required)
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = comments_ops.list_comments_detailed_async(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)

# 2. Basic async
result = await comments_ops.list_comments_detailed_async_async(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)

# 3. Detailed sync (with full HTTP response)
result = comments_ops.list_comments_detailed_async_detailed(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)

# 4. Detailed async (with full HTTP response)
result = await comments_ops.list_comments_detailed_async_detailed_async(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)
```

### `update_comment(self, node_id: Any, comment_id: Any, body: Any, fields: Any) -> python_alfresco_api.clients.core.comments.models.CommentsResponse`

Update Comment operation.

Perfect for MCP servers and comments workflows.
Returns simplified response for common use cases.

**Parameters:**
- `node_id`: typing.Any (required)
- `comment_id`: typing.Any (required)
- `body`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = comments_ops.update_comment(node_id="abc123-def456", comment_id="abc123-def456", body=request_data, fields=...)

# 2. Basic async
result = await comments_ops.update_comment_async(node_id="abc123-def456", comment_id="abc123-def456", body=request_data, fields=...)

# 3. Detailed sync (with full HTTP response)
result = comments_ops.update_comment_detailed(node_id="abc123-def456", comment_id="abc123-def456", body=request_data, fields=...)

# 4. Detailed async (with full HTTP response)
result = await comments_ops.update_comment_detailed_async(node_id="abc123-def456", comment_id="abc123-def456", body=request_data, fields=...)
```

### `update_comment_async(self, node_id: Any, comment_id: Any, body: Any, fields: Any) -> python_alfresco_api.clients.core.comments.models.CommentsResponse`

Update Comment operation (async).

Perfect for MCP servers and comments workflows.
Returns simplified response for common use cases.

**Parameters:**
- `node_id`: typing.Any (required)
- `comment_id`: typing.Any (required)
- `body`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = comments_ops.update_comment_async(node_id="abc123-def456", comment_id="abc123-def456", body=request_data, fields=...)

# 2. Basic async
result = await comments_ops.update_comment_async_async(node_id="abc123-def456", comment_id="abc123-def456", body=request_data, fields=...)

# 3. Detailed sync (with full HTTP response)
result = comments_ops.update_comment_async_detailed(node_id="abc123-def456", comment_id="abc123-def456", body=request_data, fields=...)

# 4. Detailed async (with full HTTP response)
result = await comments_ops.update_comment_async_detailed_async(node_id="abc123-def456", comment_id="abc123-def456", body=request_data, fields=...)
```

### `update_comment_detailed(self, node_id: Any, comment_id: Any, body: Any, fields: Any)`

Update Comment operation (detailed).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `node_id`: typing.Any (required)
- `comment_id`: typing.Any (required)
- `body`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = comments_ops.update_comment_detailed(node_id="abc123-def456", comment_id="abc123-def456", body=request_data, fields=...)

# 2. Basic async
result = await comments_ops.update_comment_detailed_async(node_id="abc123-def456", comment_id="abc123-def456", body=request_data, fields=...)

# 3. Detailed sync (with full HTTP response)
result = comments_ops.update_comment_detailed_detailed(node_id="abc123-def456", comment_id="abc123-def456", body=request_data, fields=...)

# 4. Detailed async (with full HTTP response)
result = await comments_ops.update_comment_detailed_detailed_async(node_id="abc123-def456", comment_id="abc123-def456", body=request_data, fields=...)
```

### `update_comment_detailed_async(self, node_id: Any, comment_id: Any, body: Any, fields: Any)`

Update Comment operation (detailed, async).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `node_id`: typing.Any (required)
- `comment_id`: typing.Any (required)
- `body`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = comments_ops.update_comment_detailed_async(node_id="abc123-def456", comment_id="abc123-def456", body=request_data, fields=...)

# 2. Basic async
result = await comments_ops.update_comment_detailed_async_async(node_id="abc123-def456", comment_id="abc123-def456", body=request_data, fields=...)

# 3. Detailed sync (with full HTTP response)
result = comments_ops.update_comment_detailed_async_detailed(node_id="abc123-def456", comment_id="abc123-def456", body=request_data, fields=...)

# 4. Detailed async (with full HTTP response)
result = await comments_ops.update_comment_detailed_async_detailed_async(node_id="abc123-def456", comment_id="abc123-def456", body=request_data, fields=...)
```

## Models

Operation-specific Pydantic models are available in:
```python
from python_alfresco_api.clients.core.comments.models import *
```

## Related Documentation

- [Core API Overview](../core_api.md)
- [V1.1 Architecture](../../clients_doc.md)
