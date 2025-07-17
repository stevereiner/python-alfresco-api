# Probes Operations - Core API

Auto-generated from V1.1 hierarchical code on 2025-07-15 00:36:43

## Overview

Probes operations for the Core API.

## Usage

```python
from python_alfresco_api import ClientFactory

# Create factory and client
factory = ClientFactory(base_url="http://localhost:8080")
core_client = factory.create_core_client()

# Access probes operations
probes_ops = core_client.probes

# Real method examples (sync):
result = probes_ops.get_httpx_client()
result = probes_ops.get_httpx_client_detailed()
result = probes_ops.get_httpx_client_detailed_async()

# Real method examples (async):
result = await probes_ops.get_httpx_client_async()
result = await probes_ops.get_httpx_client_detailed_async()
result = await probes_ops.get_httpx_client_detailed_async_async()
```

## Available Methods

This subsection provides 7 operations:

### `get_httpx_client(self)`

Get direct access to raw httpx client for advanced operations.

Perfect for MCP servers that need raw HTTP access.

**Usage Patterns:**
```python
# 1. Basic sync
result = probes_ops.get_httpx_client()

# 2. Basic async
result = await probes_ops.get_httpx_client_async()

# 3. Detailed sync (with full HTTP response)
result = probes_ops.get_httpx_client_detailed()

# 4. Detailed async (with full HTTP response)
result = await probes_ops.get_httpx_client_detailed_async()
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
result = probes_ops.get_httpx_client_detailed()

# 2. Basic async
result = await probes_ops.get_httpx_client_detailed_async()

# 3. Detailed sync (with full HTTP response)
result = probes_ops.get_httpx_client_detailed_detailed()

# 4. Detailed async (with full HTTP response)
result = await probes_ops.get_httpx_client_detailed_detailed_async()
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
result = probes_ops.get_httpx_client_detailed_async()

# 2. Basic async
result = await probes_ops.get_httpx_client_detailed_async_async()

# 3. Detailed sync (with full HTTP response)
result = probes_ops.get_httpx_client_detailed_async_detailed()

# 4. Detailed async (with full HTTP response)
result = await probes_ops.get_httpx_client_detailed_async_detailed_async()
```

### `get_probe(self, probe_id: Any) -> python_alfresco_api.clients.core.probes.models.ProbesResponse`

Get Probe operation.

Perfect for MCP servers and probes workflows.
Returns simplified response for common use cases.

**Parameters:**
- `probe_id`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = probes_ops.get_probe(probe_id="abc123-def456")

# 2. Basic async
result = await probes_ops.get_probe_async(probe_id="abc123-def456")

# 3. Detailed sync (with full HTTP response)
result = probes_ops.get_probe_detailed(probe_id="abc123-def456")

# 4. Detailed async (with full HTTP response)
result = await probes_ops.get_probe_detailed_async(probe_id="abc123-def456")
```

### `get_probe_async(self, probe_id: Any) -> python_alfresco_api.clients.core.probes.models.ProbesResponse`

Get Probe operation (async).

Perfect for MCP servers and probes workflows.
Returns simplified response for common use cases.

**Parameters:**
- `probe_id`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = probes_ops.get_probe_async(probe_id="abc123-def456")

# 2. Basic async
result = await probes_ops.get_probe_async_async(probe_id="abc123-def456")

# 3. Detailed sync (with full HTTP response)
result = probes_ops.get_probe_async_detailed(probe_id="abc123-def456")

# 4. Detailed async (with full HTTP response)
result = await probes_ops.get_probe_async_detailed_async(probe_id="abc123-def456")
```

### `get_probe_detailed(self, probe_id: Any)`

Get Probe operation (detailed).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `probe_id`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = probes_ops.get_probe_detailed(probe_id="abc123-def456")

# 2. Basic async
result = await probes_ops.get_probe_detailed_async(probe_id="abc123-def456")

# 3. Detailed sync (with full HTTP response)
result = probes_ops.get_probe_detailed_detailed(probe_id="abc123-def456")

# 4. Detailed async (with full HTTP response)
result = await probes_ops.get_probe_detailed_detailed_async(probe_id="abc123-def456")
```

### `get_probe_detailed_async(self, probe_id: Any)`

Get Probe operation (detailed, async).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `probe_id`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = probes_ops.get_probe_detailed_async(probe_id="abc123-def456")

# 2. Basic async
result = await probes_ops.get_probe_detailed_async_async(probe_id="abc123-def456")

# 3. Detailed sync (with full HTTP response)
result = probes_ops.get_probe_detailed_async_detailed(probe_id="abc123-def456")

# 4. Detailed async (with full HTTP response)
result = await probes_ops.get_probe_detailed_async_detailed_async(probe_id="abc123-def456")
```

## Models

Operation-specific Pydantic models are available in:
```python
from python_alfresco_api.clients.core.probes.models import *
```

## Related Documentation

- [Core API Overview](../core_api.md)
- [V1.1 Architecture](../../clients_doc.md)
