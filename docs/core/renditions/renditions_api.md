# Renditions Operations - Core API

Auto-generated from V1.1 hierarchical code on 2025-07-15 00:36:43

## Overview

Renditions operations for the Core API.

## Usage

```python
from python_alfresco_api import ClientFactory

# Create factory and client
factory = ClientFactory(base_url="http://localhost:8080")
core_client = factory.create_core_client()

# Access renditions operations
renditions_ops = core_client.renditions

# Real method examples (sync):
result = renditions_ops.create_rendition(node_id="abc123-def456", body=request_data)
result = renditions_ops.create_rendition_async(node_id="abc123-def456", body=request_data)
result = renditions_ops.create_rendition_detailed(node_id="abc123-def456", body=request_data)

# Real method examples (async):
result = await renditions_ops.create_rendition_async(node_id="abc123-def456", body=request_data)
result = await renditions_ops.create_rendition_async_async(node_id="abc123-def456", body=request_data)
result = await renditions_ops.create_rendition_detailed_async(node_id="abc123-def456", body=request_data)
```

## Available Methods

This subsection provides 15 operations:

### `create_rendition(self, node_id: Any, body: Any) -> python_alfresco_api.clients.core.renditions.models.RenditionsResponse`

Create Rendition operation.

Perfect for MCP servers and renditions workflows.
Returns simplified response for common use cases.

**Parameters:**
- `node_id`: typing.Any (required)
- `body`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = renditions_ops.create_rendition(node_id="abc123-def456", body=request_data)

# 2. Basic async
result = await renditions_ops.create_rendition_async(node_id="abc123-def456", body=request_data)

# 3. Detailed sync (with full HTTP response)
result = renditions_ops.create_rendition_detailed(node_id="abc123-def456", body=request_data)

# 4. Detailed async (with full HTTP response)
result = await renditions_ops.create_rendition_detailed_async(node_id="abc123-def456", body=request_data)
```

### `create_rendition_async(self, node_id: Any, body: Any) -> python_alfresco_api.clients.core.renditions.models.RenditionsResponse`

Create Rendition operation (async).

Perfect for MCP servers and renditions workflows.
Returns simplified response for common use cases.

**Parameters:**
- `node_id`: typing.Any (required)
- `body`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = renditions_ops.create_rendition_async(node_id="abc123-def456", body=request_data)

# 2. Basic async
result = await renditions_ops.create_rendition_async_async(node_id="abc123-def456", body=request_data)

# 3. Detailed sync (with full HTTP response)
result = renditions_ops.create_rendition_async_detailed(node_id="abc123-def456", body=request_data)

# 4. Detailed async (with full HTTP response)
result = await renditions_ops.create_rendition_async_detailed_async(node_id="abc123-def456", body=request_data)
```

### `create_rendition_detailed(self, node_id: Any, body: Any)`

Create Rendition operation (detailed).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `node_id`: typing.Any (required)
- `body`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = renditions_ops.create_rendition_detailed(node_id="abc123-def456", body=request_data)

# 2. Basic async
result = await renditions_ops.create_rendition_detailed_async(node_id="abc123-def456", body=request_data)

# 3. Detailed sync (with full HTTP response)
result = renditions_ops.create_rendition_detailed_detailed(node_id="abc123-def456", body=request_data)

# 4. Detailed async (with full HTTP response)
result = await renditions_ops.create_rendition_detailed_detailed_async(node_id="abc123-def456", body=request_data)
```

### `create_rendition_detailed_async(self, node_id: Any, body: Any)`

Create Rendition operation (detailed, async).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `node_id`: typing.Any (required)
- `body`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = renditions_ops.create_rendition_detailed_async(node_id="abc123-def456", body=request_data)

# 2. Basic async
result = await renditions_ops.create_rendition_detailed_async_async(node_id="abc123-def456", body=request_data)

# 3. Detailed sync (with full HTTP response)
result = renditions_ops.create_rendition_detailed_async_detailed(node_id="abc123-def456", body=request_data)

# 4. Detailed async (with full HTTP response)
result = await renditions_ops.create_rendition_detailed_async_detailed_async(node_id="abc123-def456", body=request_data)
```

### `get_httpx_client(self)`

Get direct access to raw httpx client for advanced operations.

Perfect for MCP servers that need raw HTTP access.

**Usage Patterns:**
```python
# 1. Basic sync
result = renditions_ops.get_httpx_client()

# 2. Basic async
result = await renditions_ops.get_httpx_client_async()

# 3. Detailed sync (with full HTTP response)
result = renditions_ops.get_httpx_client_detailed()

# 4. Detailed async (with full HTTP response)
result = await renditions_ops.get_httpx_client_detailed_async()
```

### `get_httpx_client_detailed(self)`

Get Httpx Client operation (detailed sync).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

Returns:
    Response: Complete response with status_code, headers, content, parsed

**Usage Patterns:**
```python
# 1. Basic sync
result = renditions_ops.get_httpx_client_detailed()

# 2. Basic async
result = await renditions_ops.get_httpx_client_detailed_async()

# 3. Detailed sync (with full HTTP response)
result = renditions_ops.get_httpx_client_detailed_detailed()

# 4. Detailed async (with full HTTP response)
result = await renditions_ops.get_httpx_client_detailed_detailed_async()
```

### `get_httpx_client_detailed_async(self)`

Get Httpx Client operation (detailed async).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

Returns:
    Response: Complete response with status_code, headers, content, parsed

**Usage Patterns:**
```python
# 1. Basic sync
result = renditions_ops.get_httpx_client_detailed_async()

# 2. Basic async
result = await renditions_ops.get_httpx_client_detailed_async_async()

# 3. Detailed sync (with full HTTP response)
result = renditions_ops.get_httpx_client_detailed_async_detailed()

# 4. Detailed async (with full HTTP response)
result = await renditions_ops.get_httpx_client_detailed_async_detailed_async()
```

### `get_rendition(self, node_id: Any, rendition_id: Any) -> python_alfresco_api.clients.core.renditions.models.RenditionsResponse`

Get Rendition operation.

Perfect for MCP servers and renditions workflows.
Returns simplified response for common use cases.

**Parameters:**
- `node_id`: typing.Any (required)
- `rendition_id`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = renditions_ops.get_rendition(node_id="abc123-def456", rendition_id="abc123-def456")

# 2. Basic async
result = await renditions_ops.get_rendition_async(node_id="abc123-def456", rendition_id="abc123-def456")

# 3. Detailed sync (with full HTTP response)
result = renditions_ops.get_rendition_detailed(node_id="abc123-def456", rendition_id="abc123-def456")

# 4. Detailed async (with full HTTP response)
result = await renditions_ops.get_rendition_detailed_async(node_id="abc123-def456", rendition_id="abc123-def456")
```

### `get_rendition_async(self, node_id: Any, rendition_id: Any) -> python_alfresco_api.clients.core.renditions.models.RenditionsResponse`

Get Rendition operation (async).

Perfect for MCP servers and renditions workflows.
Returns simplified response for common use cases.

**Parameters:**
- `node_id`: typing.Any (required)
- `rendition_id`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = renditions_ops.get_rendition_async(node_id="abc123-def456", rendition_id="abc123-def456")

# 2. Basic async
result = await renditions_ops.get_rendition_async_async(node_id="abc123-def456", rendition_id="abc123-def456")

# 3. Detailed sync (with full HTTP response)
result = renditions_ops.get_rendition_async_detailed(node_id="abc123-def456", rendition_id="abc123-def456")

# 4. Detailed async (with full HTTP response)
result = await renditions_ops.get_rendition_async_detailed_async(node_id="abc123-def456", rendition_id="abc123-def456")
```

### `get_rendition_detailed(self, node_id: Any, rendition_id: Any)`

Get Rendition operation (detailed).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `node_id`: typing.Any (required)
- `rendition_id`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = renditions_ops.get_rendition_detailed(node_id="abc123-def456", rendition_id="abc123-def456")

# 2. Basic async
result = await renditions_ops.get_rendition_detailed_async(node_id="abc123-def456", rendition_id="abc123-def456")

# 3. Detailed sync (with full HTTP response)
result = renditions_ops.get_rendition_detailed_detailed(node_id="abc123-def456", rendition_id="abc123-def456")

# 4. Detailed async (with full HTTP response)
result = await renditions_ops.get_rendition_detailed_detailed_async(node_id="abc123-def456", rendition_id="abc123-def456")
```

### `get_rendition_detailed_async(self, node_id: Any, rendition_id: Any)`

Get Rendition operation (detailed, async).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `node_id`: typing.Any (required)
- `rendition_id`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = renditions_ops.get_rendition_detailed_async(node_id="abc123-def456", rendition_id="abc123-def456")

# 2. Basic async
result = await renditions_ops.get_rendition_detailed_async_async(node_id="abc123-def456", rendition_id="abc123-def456")

# 3. Detailed sync (with full HTTP response)
result = renditions_ops.get_rendition_detailed_async_detailed(node_id="abc123-def456", rendition_id="abc123-def456")

# 4. Detailed async (with full HTTP response)
result = await renditions_ops.get_rendition_detailed_async_detailed_async(node_id="abc123-def456", rendition_id="abc123-def456")
```

### `list_renditions(self, node_id: Any, where: Any) -> python_alfresco_api.clients.core.renditions.models.RenditionsResponse`

List Renditions operation.

Perfect for MCP servers and renditions workflows.
Returns simplified response for common use cases.

**Parameters:**
- `node_id`: typing.Any (required)
- `where`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = renditions_ops.list_renditions(node_id="abc123-def456", where=...)

# 2. Basic async
result = await renditions_ops.list_renditions_async(node_id="abc123-def456", where=...)

# 3. Detailed sync (with full HTTP response)
result = renditions_ops.list_renditions_detailed(node_id="abc123-def456", where=...)

# 4. Detailed async (with full HTTP response)
result = await renditions_ops.list_renditions_detailed_async(node_id="abc123-def456", where=...)
```

### `list_renditions_async(self, node_id: Any, where: Any) -> python_alfresco_api.clients.core.renditions.models.RenditionsResponse`

List Renditions operation (async).

Perfect for MCP servers and renditions workflows.
Returns simplified response for common use cases.

**Parameters:**
- `node_id`: typing.Any (required)
- `where`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = renditions_ops.list_renditions_async(node_id="abc123-def456", where=...)

# 2. Basic async
result = await renditions_ops.list_renditions_async_async(node_id="abc123-def456", where=...)

# 3. Detailed sync (with full HTTP response)
result = renditions_ops.list_renditions_async_detailed(node_id="abc123-def456", where=...)

# 4. Detailed async (with full HTTP response)
result = await renditions_ops.list_renditions_async_detailed_async(node_id="abc123-def456", where=...)
```

### `list_renditions_detailed(self, node_id: Any, where: Any)`

List Renditions operation (detailed).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `node_id`: typing.Any (required)
- `where`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = renditions_ops.list_renditions_detailed(node_id="abc123-def456", where=...)

# 2. Basic async
result = await renditions_ops.list_renditions_detailed_async(node_id="abc123-def456", where=...)

# 3. Detailed sync (with full HTTP response)
result = renditions_ops.list_renditions_detailed_detailed(node_id="abc123-def456", where=...)

# 4. Detailed async (with full HTTP response)
result = await renditions_ops.list_renditions_detailed_detailed_async(node_id="abc123-def456", where=...)
```

### `list_renditions_detailed_async(self, node_id: Any, where: Any)`

List Renditions operation (detailed, async).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `node_id`: typing.Any (required)
- `where`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = renditions_ops.list_renditions_detailed_async(node_id="abc123-def456", where=...)

# 2. Basic async
result = await renditions_ops.list_renditions_detailed_async_async(node_id="abc123-def456", where=...)

# 3. Detailed sync (with full HTTP response)
result = renditions_ops.list_renditions_detailed_async_detailed(node_id="abc123-def456", where=...)

# 4. Detailed async (with full HTTP response)
result = await renditions_ops.list_renditions_detailed_async_detailed_async(node_id="abc123-def456", where=...)
```

## Models

Operation-specific Pydantic models are available in:
```python
from python_alfresco_api.clients.core.renditions.models import *
```

## Related Documentation

- [Core API Overview](../core_api.md)
- [V1.1 Architecture](../../clients_doc.md)
