# Discovery Operations - Discovery API

Auto-generated from V1.1 hierarchical code on 2025-07-15 00:36:43

## Overview

Discovery operations for the Discovery API.

## Usage

```python
from python_alfresco_api import ClientFactory

# Create factory and client
factory = ClientFactory(base_url="http://localhost:8080")
discovery_client = factory.create_discovery_client()

# Access discovery operations
discovery_ops = discovery_client.discovery

# Real method examples (sync):
result = discovery_ops.get_httpx_client()
result = discovery_ops.get_repository_information()
result = discovery_ops.get_repository_information_async()

# Real method examples (async):
result = await discovery_ops.get_httpx_client_async()
result = await discovery_ops.get_repository_information_async()
result = await discovery_ops.get_repository_information_async_async()
```

## Available Methods

This subsection provides 5 operations:

### `get_httpx_client(self)`

Get direct access to raw httpx client for advanced operations.

Perfect for MCP servers that need raw HTTP access.

**Usage Patterns:**
```python
# 1. Basic sync
result = discovery_ops.get_httpx_client()

# 2. Basic async
result = await discovery_ops.get_httpx_client_async()

# 3. Detailed sync (with full HTTP response)
result = discovery_ops.get_httpx_client_detailed()

# 4. Detailed async (with full HTTP response)
result = await discovery_ops.get_httpx_client_detailed_async()
```

### `get_repository_information(self) -> Any`

Get Repository Information operation (sync).

Perfect for MCP servers and discovery workflows.
Returns parsed response for common use cases.

Args:
    No parameters

Returns:
    Parsed response object

**Usage Patterns:**
```python
# 1. Basic sync
result = discovery_ops.get_repository_information()

# 2. Basic async
result = await discovery_ops.get_repository_information_async()

# 3. Detailed sync (with full HTTP response)
result = discovery_ops.get_repository_information_detailed()

# 4. Detailed async (with full HTTP response)
result = await discovery_ops.get_repository_information_detailed_async()
```

### `get_repository_information_async(self) -> Any`

Get Repository Information operation (async).

Perfect for MCP servers and discovery workflows.
Returns parsed response for common use cases.

Args:
    No parameters

Returns:
    Parsed response object

**Usage Patterns:**
```python
# 1. Basic sync
result = discovery_ops.get_repository_information_async()

# 2. Basic async
result = await discovery_ops.get_repository_information_async_async()

# 3. Detailed sync (with full HTTP response)
result = discovery_ops.get_repository_information_async_detailed()

# 4. Detailed async (with full HTTP response)
result = await discovery_ops.get_repository_information_async_detailed_async()
```

### `get_repository_information_detailed(self)`

Get Repository Information operation (detailed sync).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

Args:
    No parameters

Returns:
    Response: Complete response with status_code, headers, content, parsed

**Usage Patterns:**
```python
# 1. Basic sync
result = discovery_ops.get_repository_information_detailed()

# 2. Basic async
result = await discovery_ops.get_repository_information_detailed_async()

# 3. Detailed sync (with full HTTP response)
result = discovery_ops.get_repository_information_detailed_detailed()

# 4. Detailed async (with full HTTP response)
result = await discovery_ops.get_repository_information_detailed_detailed_async()
```

### `get_repository_information_detailed_async(self)`

Get Repository Information operation (detailed async).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

Args:
    No parameters

Returns:
    Response: Complete response with status_code, headers, content, parsed

**Usage Patterns:**
```python
# 1. Basic sync
result = discovery_ops.get_repository_information_detailed_async()

# 2. Basic async
result = await discovery_ops.get_repository_information_detailed_async_async()

# 3. Detailed sync (with full HTTP response)
result = discovery_ops.get_repository_information_detailed_async_detailed()

# 4. Detailed async (with full HTTP response)
result = await discovery_ops.get_repository_information_detailed_async_detailed_async()
```

## Models

Operation-specific Pydantic models are available in:
```python
from python_alfresco_api.clients.discovery.discovery.models import *
```

## Related Documentation

- [Discovery API Overview](../discovery_api.md)
- [V1.1 Architecture](../../clients_doc.md)
