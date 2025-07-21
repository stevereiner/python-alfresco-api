# Downloads Operations - Core API

Auto-generated from V1.1 hierarchical code on 2025-07-15 00:36:43

## Overview

Downloads operations for the Core API.

## Usage

```python
from python_alfresco_api import ClientFactory

# Create factory and client
factory = ClientFactory(base_url="http://localhost:8080")
core_client = factory.create_core_client()

# Access downloads operations
downloads_ops = core_client.downloads

# Real method examples (sync):
result = downloads_ops.cancel_download(download_id="abc123-def456")
result = downloads_ops.cancel_download_async(download_id="abc123-def456")
result = downloads_ops.cancel_download_detailed(download_id="abc123-def456")

# Real method examples (async):
result = await downloads_ops.cancel_download_async(download_id="abc123-def456")
result = await downloads_ops.cancel_download_async_async(download_id="abc123-def456")
result = await downloads_ops.cancel_download_detailed_async(download_id="abc123-def456")
```

## Available Methods

This subsection provides 15 operations:

### `cancel_download(self, download_id: Any) -> python_alfresco_api.clients.core.downloads.models.DownloadsResponse`

Cancel Download operation.

Perfect for MCP servers and downloads workflows.
Returns simplified response for common use cases.

**Parameters:**
- `download_id`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = downloads_ops.cancel_download(download_id="abc123-def456")

# 2. Basic async
result = await downloads_ops.cancel_download_async(download_id="abc123-def456")

# 3. Detailed sync (with full HTTP response)
result = downloads_ops.cancel_download_detailed(download_id="abc123-def456")

# 4. Detailed async (with full HTTP response)
result = await downloads_ops.cancel_download_detailed_async(download_id="abc123-def456")
```

### `cancel_download_async(self, download_id: Any) -> python_alfresco_api.clients.core.downloads.models.DownloadsResponse`

Cancel Download operation (async).

Perfect for MCP servers and downloads workflows.
Returns simplified response for common use cases.

**Parameters:**
- `download_id`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = downloads_ops.cancel_download_async(download_id="abc123-def456")

# 2. Basic async
result = await downloads_ops.cancel_download_async_async(download_id="abc123-def456")

# 3. Detailed sync (with full HTTP response)
result = downloads_ops.cancel_download_async_detailed(download_id="abc123-def456")

# 4. Detailed async (with full HTTP response)
result = await downloads_ops.cancel_download_async_detailed_async(download_id="abc123-def456")
```

### `cancel_download_detailed(self, download_id: Any)`

Cancel Download operation (detailed).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `download_id`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = downloads_ops.cancel_download_detailed(download_id="abc123-def456")

# 2. Basic async
result = await downloads_ops.cancel_download_detailed_async(download_id="abc123-def456")

# 3. Detailed sync (with full HTTP response)
result = downloads_ops.cancel_download_detailed_detailed(download_id="abc123-def456")

# 4. Detailed async (with full HTTP response)
result = await downloads_ops.cancel_download_detailed_detailed_async(download_id="abc123-def456")
```

### `cancel_download_detailed_async(self, download_id: Any)`

Cancel Download operation (detailed, async).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `download_id`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = downloads_ops.cancel_download_detailed_async(download_id="abc123-def456")

# 2. Basic async
result = await downloads_ops.cancel_download_detailed_async_async(download_id="abc123-def456")

# 3. Detailed sync (with full HTTP response)
result = downloads_ops.cancel_download_detailed_async_detailed(download_id="abc123-def456")

# 4. Detailed async (with full HTTP response)
result = await downloads_ops.cancel_download_detailed_async_detailed_async(download_id="abc123-def456")
```

### `create_download(self, body: Any, fields: Any) -> python_alfresco_api.clients.core.downloads.models.DownloadsResponse`

Create Download operation.

Perfect for MCP servers and downloads workflows.
Returns simplified response for common use cases.

**Parameters:**
- `body`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = downloads_ops.create_download(body=request_data, fields=...)

# 2. Basic async
result = await downloads_ops.create_download_async(body=request_data, fields=...)

# 3. Detailed sync (with full HTTP response)
result = downloads_ops.create_download_detailed(body=request_data, fields=...)

# 4. Detailed async (with full HTTP response)
result = await downloads_ops.create_download_detailed_async(body=request_data, fields=...)
```

### `create_download_async(self, body: Any, fields: Any) -> python_alfresco_api.clients.core.downloads.models.DownloadsResponse`

Create Download operation (async).

Perfect for MCP servers and downloads workflows.
Returns simplified response for common use cases.

**Parameters:**
- `body`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = downloads_ops.create_download_async(body=request_data, fields=...)

# 2. Basic async
result = await downloads_ops.create_download_async_async(body=request_data, fields=...)

# 3. Detailed sync (with full HTTP response)
result = downloads_ops.create_download_async_detailed(body=request_data, fields=...)

# 4. Detailed async (with full HTTP response)
result = await downloads_ops.create_download_async_detailed_async(body=request_data, fields=...)
```

### `create_download_detailed(self, body: Any, fields: Any)`

Create Download operation (detailed).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `body`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = downloads_ops.create_download_detailed(body=request_data, fields=...)

# 2. Basic async
result = await downloads_ops.create_download_detailed_async(body=request_data, fields=...)

# 3. Detailed sync (with full HTTP response)
result = downloads_ops.create_download_detailed_detailed(body=request_data, fields=...)

# 4. Detailed async (with full HTTP response)
result = await downloads_ops.create_download_detailed_detailed_async(body=request_data, fields=...)
```

### `create_download_detailed_async(self, body: Any, fields: Any)`

Create Download operation (detailed, async).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `body`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = downloads_ops.create_download_detailed_async(body=request_data, fields=...)

# 2. Basic async
result = await downloads_ops.create_download_detailed_async_async(body=request_data, fields=...)

# 3. Detailed sync (with full HTTP response)
result = downloads_ops.create_download_detailed_async_detailed(body=request_data, fields=...)

# 4. Detailed async (with full HTTP response)
result = await downloads_ops.create_download_detailed_async_detailed_async(body=request_data, fields=...)
```

### `get_download(self, download_id: Any, fields: Any) -> python_alfresco_api.clients.core.downloads.models.DownloadsResponse`

Get Download operation.

Perfect for MCP servers and downloads workflows.
Returns simplified response for common use cases.

**Parameters:**
- `download_id`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = downloads_ops.get_download(download_id="abc123-def456", fields=...)

# 2. Basic async
result = await downloads_ops.get_download_async(download_id="abc123-def456", fields=...)

# 3. Detailed sync (with full HTTP response)
result = downloads_ops.get_download_detailed(download_id="abc123-def456", fields=...)

# 4. Detailed async (with full HTTP response)
result = await downloads_ops.get_download_detailed_async(download_id="abc123-def456", fields=...)
```

### `get_download_async(self, download_id: Any, fields: Any) -> python_alfresco_api.clients.core.downloads.models.DownloadsResponse`

Get Download operation (async).

Perfect for MCP servers and downloads workflows.
Returns simplified response for common use cases.

**Parameters:**
- `download_id`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = downloads_ops.get_download_async(download_id="abc123-def456", fields=...)

# 2. Basic async
result = await downloads_ops.get_download_async_async(download_id="abc123-def456", fields=...)

# 3. Detailed sync (with full HTTP response)
result = downloads_ops.get_download_async_detailed(download_id="abc123-def456", fields=...)

# 4. Detailed async (with full HTTP response)
result = await downloads_ops.get_download_async_detailed_async(download_id="abc123-def456", fields=...)
```

### `get_download_detailed(self, download_id: Any, fields: Any)`

Get Download operation (detailed).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `download_id`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = downloads_ops.get_download_detailed(download_id="abc123-def456", fields=...)

# 2. Basic async
result = await downloads_ops.get_download_detailed_async(download_id="abc123-def456", fields=...)

# 3. Detailed sync (with full HTTP response)
result = downloads_ops.get_download_detailed_detailed(download_id="abc123-def456", fields=...)

# 4. Detailed async (with full HTTP response)
result = await downloads_ops.get_download_detailed_detailed_async(download_id="abc123-def456", fields=...)
```

### `get_download_detailed_async(self, download_id: Any, fields: Any)`

Get Download operation (detailed, async).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `download_id`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = downloads_ops.get_download_detailed_async(download_id="abc123-def456", fields=...)

# 2. Basic async
result = await downloads_ops.get_download_detailed_async_async(download_id="abc123-def456", fields=...)

# 3. Detailed sync (with full HTTP response)
result = downloads_ops.get_download_detailed_async_detailed(download_id="abc123-def456", fields=...)

# 4. Detailed async (with full HTTP response)
result = await downloads_ops.get_download_detailed_async_detailed_async(download_id="abc123-def456", fields=...)
```

### `get_httpx_client(self)`

Get direct access to raw httpx client for advanced operations.

Perfect for MCP servers that need raw HTTP access.

**Usage Patterns:**
```python
# 1. Basic sync
result = downloads_ops.get_httpx_client()

# 2. Basic async
result = await downloads_ops.get_httpx_client_async()

# 3. Detailed sync (with full HTTP response)
result = downloads_ops.get_httpx_client_detailed()

# 4. Detailed async (with full HTTP response)
result = await downloads_ops.get_httpx_client_detailed_async()
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
result = downloads_ops.get_httpx_client_detailed()

# 2. Basic async
result = await downloads_ops.get_httpx_client_detailed_async()

# 3. Detailed sync (with full HTTP response)
result = downloads_ops.get_httpx_client_detailed_detailed()

# 4. Detailed async (with full HTTP response)
result = await downloads_ops.get_httpx_client_detailed_detailed_async()
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
result = downloads_ops.get_httpx_client_detailed_async()

# 2. Basic async
result = await downloads_ops.get_httpx_client_detailed_async_async()

# 3. Detailed sync (with full HTTP response)
result = downloads_ops.get_httpx_client_detailed_async_detailed()

# 4. Detailed async (with full HTTP response)
result = await downloads_ops.get_httpx_client_detailed_async_detailed_async()
```

## Models

Operation-specific Pydantic models are available in:
```python
from python_alfresco_api.clients.core.downloads.models import *
```

## Related Documentation

- [Core API Overview](../core_api.md)
- [V1.1 Architecture](../../clients_doc.md)
