# Queries Operations - Core API

Auto-generated from V1.1 hierarchical code on 2025-07-15 00:36:43

## Overview

Queries operations for the Core API.

## Usage

```python
from python_alfresco_api import ClientFactory

# Create factory and client
factory = ClientFactory(base_url="http://localhost:8080")
core_client = factory.create_core_client()

# Access queries operations
queries_ops = core_client.queries

# Real method examples (sync):
result = queries_ops.find_nodes(term=..., root_node_id="abc123-def456", skip_count=..., max_items=..., node_type=..., include=..., order_by=..., fields=...)
result = queries_ops.find_nodes_async(term=..., root_node_id="abc123-def456", skip_count=..., max_items=..., node_type=..., include=..., order_by=..., fields=...)
result = queries_ops.find_nodes_detailed(term=..., root_node_id="abc123-def456", skip_count=..., max_items=..., node_type=..., include=..., order_by=..., fields=...)

# Real method examples (async):
result = await queries_ops.find_nodes_async(term=..., root_node_id="abc123-def456", skip_count=..., max_items=..., node_type=..., include=..., order_by=..., fields=...)
result = await queries_ops.find_nodes_async_async(term=..., root_node_id="abc123-def456", skip_count=..., max_items=..., node_type=..., include=..., order_by=..., fields=...)
result = await queries_ops.find_nodes_detailed_async(term=..., root_node_id="abc123-def456", skip_count=..., max_items=..., node_type=..., include=..., order_by=..., fields=...)
```

## Available Methods

This subsection provides 15 operations:

### `find_nodes(self, term: Any, root_node_id: Any, skip_count: Any, max_items: Any, node_type: Any, include: Any, order_by: Any, fields: Any) -> python_alfresco_api.clients.core.queries.models.QueriesResponse`

Find Nodes operation.

Perfect for MCP servers and queries workflows.
Returns simplified response for common use cases.

**Parameters:**
- `term`: typing.Any (required)
- `root_node_id`: typing.Any (required)
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `node_type`: typing.Any (required)
- `include`: typing.Any (required)
- `order_by`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = queries_ops.find_nodes(term=..., root_node_id="abc123-def456", skip_count=..., max_items=..., node_type=..., include=..., order_by=..., fields=...)

# 2. Basic async
result = await queries_ops.find_nodes_async(term=..., root_node_id="abc123-def456", skip_count=..., max_items=..., node_type=..., include=..., order_by=..., fields=...)

# 3. Detailed sync (with full HTTP response)
result = queries_ops.find_nodes_detailed(term=..., root_node_id="abc123-def456", skip_count=..., max_items=..., node_type=..., include=..., order_by=..., fields=...)

# 4. Detailed async (with full HTTP response)
result = await queries_ops.find_nodes_detailed_async(term=..., root_node_id="abc123-def456", skip_count=..., max_items=..., node_type=..., include=..., order_by=..., fields=...)
```

### `find_nodes_async(self, term: Any, root_node_id: Any, skip_count: Any, max_items: Any, node_type: Any, include: Any, order_by: Any, fields: Any) -> python_alfresco_api.clients.core.queries.models.QueriesResponse`

Find Nodes operation (async).

Perfect for MCP servers and queries workflows.
Returns simplified response for common use cases.

**Parameters:**
- `term`: typing.Any (required)
- `root_node_id`: typing.Any (required)
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `node_type`: typing.Any (required)
- `include`: typing.Any (required)
- `order_by`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = queries_ops.find_nodes_async(term=..., root_node_id="abc123-def456", skip_count=..., max_items=..., node_type=..., include=..., order_by=..., fields=...)

# 2. Basic async
result = await queries_ops.find_nodes_async_async(term=..., root_node_id="abc123-def456", skip_count=..., max_items=..., node_type=..., include=..., order_by=..., fields=...)

# 3. Detailed sync (with full HTTP response)
result = queries_ops.find_nodes_async_detailed(term=..., root_node_id="abc123-def456", skip_count=..., max_items=..., node_type=..., include=..., order_by=..., fields=...)

# 4. Detailed async (with full HTTP response)
result = await queries_ops.find_nodes_async_detailed_async(term=..., root_node_id="abc123-def456", skip_count=..., max_items=..., node_type=..., include=..., order_by=..., fields=...)
```

### `find_nodes_detailed(self, term: Any, root_node_id: Any, skip_count: Any, max_items: Any, node_type: Any, include: Any, order_by: Any, fields: Any)`

Find Nodes operation (detailed).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `term`: typing.Any (required)
- `root_node_id`: typing.Any (required)
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `node_type`: typing.Any (required)
- `include`: typing.Any (required)
- `order_by`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = queries_ops.find_nodes_detailed(term=..., root_node_id="abc123-def456", skip_count=..., max_items=..., node_type=..., include=..., order_by=..., fields=...)

# 2. Basic async
result = await queries_ops.find_nodes_detailed_async(term=..., root_node_id="abc123-def456", skip_count=..., max_items=..., node_type=..., include=..., order_by=..., fields=...)

# 3. Detailed sync (with full HTTP response)
result = queries_ops.find_nodes_detailed_detailed(term=..., root_node_id="abc123-def456", skip_count=..., max_items=..., node_type=..., include=..., order_by=..., fields=...)

# 4. Detailed async (with full HTTP response)
result = await queries_ops.find_nodes_detailed_detailed_async(term=..., root_node_id="abc123-def456", skip_count=..., max_items=..., node_type=..., include=..., order_by=..., fields=...)
```

### `find_nodes_detailed_async(self, term: Any, root_node_id: Any, skip_count: Any, max_items: Any, node_type: Any, include: Any, order_by: Any, fields: Any)`

Find Nodes operation (detailed, async).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `term`: typing.Any (required)
- `root_node_id`: typing.Any (required)
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `node_type`: typing.Any (required)
- `include`: typing.Any (required)
- `order_by`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = queries_ops.find_nodes_detailed_async(term=..., root_node_id="abc123-def456", skip_count=..., max_items=..., node_type=..., include=..., order_by=..., fields=...)

# 2. Basic async
result = await queries_ops.find_nodes_detailed_async_async(term=..., root_node_id="abc123-def456", skip_count=..., max_items=..., node_type=..., include=..., order_by=..., fields=...)

# 3. Detailed sync (with full HTTP response)
result = queries_ops.find_nodes_detailed_async_detailed(term=..., root_node_id="abc123-def456", skip_count=..., max_items=..., node_type=..., include=..., order_by=..., fields=...)

# 4. Detailed async (with full HTTP response)
result = await queries_ops.find_nodes_detailed_async_detailed_async(term=..., root_node_id="abc123-def456", skip_count=..., max_items=..., node_type=..., include=..., order_by=..., fields=...)
```

### `find_people(self, term: Any, skip_count: Any, max_items: Any, fields: Any, order_by: Any) -> python_alfresco_api.clients.core.queries.models.QueriesResponse`

Find People operation.

Perfect for MCP servers and queries workflows.
Returns simplified response for common use cases.

**Parameters:**
- `term`: typing.Any (required)
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `fields`: typing.Any (required)
- `order_by`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = queries_ops.find_people(term=..., skip_count=..., max_items=..., fields=..., order_by=...)

# 2. Basic async
result = await queries_ops.find_people_async(term=..., skip_count=..., max_items=..., fields=..., order_by=...)

# 3. Detailed sync (with full HTTP response)
result = queries_ops.find_people_detailed(term=..., skip_count=..., max_items=..., fields=..., order_by=...)

# 4. Detailed async (with full HTTP response)
result = await queries_ops.find_people_detailed_async(term=..., skip_count=..., max_items=..., fields=..., order_by=...)
```

### `find_people_async(self, term: Any, skip_count: Any, max_items: Any, fields: Any, order_by: Any) -> python_alfresco_api.clients.core.queries.models.QueriesResponse`

Find People operation (async).

Perfect for MCP servers and queries workflows.
Returns simplified response for common use cases.

**Parameters:**
- `term`: typing.Any (required)
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `fields`: typing.Any (required)
- `order_by`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = queries_ops.find_people_async(term=..., skip_count=..., max_items=..., fields=..., order_by=...)

# 2. Basic async
result = await queries_ops.find_people_async_async(term=..., skip_count=..., max_items=..., fields=..., order_by=...)

# 3. Detailed sync (with full HTTP response)
result = queries_ops.find_people_async_detailed(term=..., skip_count=..., max_items=..., fields=..., order_by=...)

# 4. Detailed async (with full HTTP response)
result = await queries_ops.find_people_async_detailed_async(term=..., skip_count=..., max_items=..., fields=..., order_by=...)
```

### `find_people_detailed(self, term: Any, skip_count: Any, max_items: Any, fields: Any, order_by: Any)`

Find People operation (detailed).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `term`: typing.Any (required)
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `fields`: typing.Any (required)
- `order_by`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = queries_ops.find_people_detailed(term=..., skip_count=..., max_items=..., fields=..., order_by=...)

# 2. Basic async
result = await queries_ops.find_people_detailed_async(term=..., skip_count=..., max_items=..., fields=..., order_by=...)

# 3. Detailed sync (with full HTTP response)
result = queries_ops.find_people_detailed_detailed(term=..., skip_count=..., max_items=..., fields=..., order_by=...)

# 4. Detailed async (with full HTTP response)
result = await queries_ops.find_people_detailed_detailed_async(term=..., skip_count=..., max_items=..., fields=..., order_by=...)
```

### `find_people_detailed_async(self, term: Any, skip_count: Any, max_items: Any, fields: Any, order_by: Any)`

Find People operation (detailed, async).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `term`: typing.Any (required)
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `fields`: typing.Any (required)
- `order_by`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = queries_ops.find_people_detailed_async(term=..., skip_count=..., max_items=..., fields=..., order_by=...)

# 2. Basic async
result = await queries_ops.find_people_detailed_async_async(term=..., skip_count=..., max_items=..., fields=..., order_by=...)

# 3. Detailed sync (with full HTTP response)
result = queries_ops.find_people_detailed_async_detailed(term=..., skip_count=..., max_items=..., fields=..., order_by=...)

# 4. Detailed async (with full HTTP response)
result = await queries_ops.find_people_detailed_async_detailed_async(term=..., skip_count=..., max_items=..., fields=..., order_by=...)
```

### `find_sites(self, term: Any, skip_count: Any, max_items: Any, order_by: Any, fields: Any) -> python_alfresco_api.clients.core.queries.models.QueriesResponse`

Find Sites operation.

Perfect for MCP servers and queries workflows.
Returns simplified response for common use cases.

**Parameters:**
- `term`: typing.Any (required)
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `order_by`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = queries_ops.find_sites(term=..., skip_count=..., max_items=..., order_by=..., fields=...)

# 2. Basic async
result = await queries_ops.find_sites_async(term=..., skip_count=..., max_items=..., order_by=..., fields=...)

# 3. Detailed sync (with full HTTP response)
result = queries_ops.find_sites_detailed(term=..., skip_count=..., max_items=..., order_by=..., fields=...)

# 4. Detailed async (with full HTTP response)
result = await queries_ops.find_sites_detailed_async(term=..., skip_count=..., max_items=..., order_by=..., fields=...)
```

### `find_sites_async(self, term: Any, skip_count: Any, max_items: Any, order_by: Any, fields: Any) -> python_alfresco_api.clients.core.queries.models.QueriesResponse`

Find Sites operation (async).

Perfect for MCP servers and queries workflows.
Returns simplified response for common use cases.

**Parameters:**
- `term`: typing.Any (required)
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `order_by`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = queries_ops.find_sites_async(term=..., skip_count=..., max_items=..., order_by=..., fields=...)

# 2. Basic async
result = await queries_ops.find_sites_async_async(term=..., skip_count=..., max_items=..., order_by=..., fields=...)

# 3. Detailed sync (with full HTTP response)
result = queries_ops.find_sites_async_detailed(term=..., skip_count=..., max_items=..., order_by=..., fields=...)

# 4. Detailed async (with full HTTP response)
result = await queries_ops.find_sites_async_detailed_async(term=..., skip_count=..., max_items=..., order_by=..., fields=...)
```

### `find_sites_detailed(self, term: Any, skip_count: Any, max_items: Any, order_by: Any, fields: Any)`

Find Sites operation (detailed).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `term`: typing.Any (required)
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `order_by`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = queries_ops.find_sites_detailed(term=..., skip_count=..., max_items=..., order_by=..., fields=...)

# 2. Basic async
result = await queries_ops.find_sites_detailed_async(term=..., skip_count=..., max_items=..., order_by=..., fields=...)

# 3. Detailed sync (with full HTTP response)
result = queries_ops.find_sites_detailed_detailed(term=..., skip_count=..., max_items=..., order_by=..., fields=...)

# 4. Detailed async (with full HTTP response)
result = await queries_ops.find_sites_detailed_detailed_async(term=..., skip_count=..., max_items=..., order_by=..., fields=...)
```

### `find_sites_detailed_async(self, term: Any, skip_count: Any, max_items: Any, order_by: Any, fields: Any)`

Find Sites operation (detailed, async).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `term`: typing.Any (required)
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `order_by`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = queries_ops.find_sites_detailed_async(term=..., skip_count=..., max_items=..., order_by=..., fields=...)

# 2. Basic async
result = await queries_ops.find_sites_detailed_async_async(term=..., skip_count=..., max_items=..., order_by=..., fields=...)

# 3. Detailed sync (with full HTTP response)
result = queries_ops.find_sites_detailed_async_detailed(term=..., skip_count=..., max_items=..., order_by=..., fields=...)

# 4. Detailed async (with full HTTP response)
result = await queries_ops.find_sites_detailed_async_detailed_async(term=..., skip_count=..., max_items=..., order_by=..., fields=...)
```

### `get_httpx_client(self)`

Get direct access to raw httpx client for advanced operations.

Perfect for MCP servers that need raw HTTP access.

**Usage Patterns:**
```python
# 1. Basic sync
result = queries_ops.get_httpx_client()

# 2. Basic async
result = await queries_ops.get_httpx_client_async()

# 3. Detailed sync (with full HTTP response)
result = queries_ops.get_httpx_client_detailed()

# 4. Detailed async (with full HTTP response)
result = await queries_ops.get_httpx_client_detailed_async()
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
result = queries_ops.get_httpx_client_detailed()

# 2. Basic async
result = await queries_ops.get_httpx_client_detailed_async()

# 3. Detailed sync (with full HTTP response)
result = queries_ops.get_httpx_client_detailed_detailed()

# 4. Detailed async (with full HTTP response)
result = await queries_ops.get_httpx_client_detailed_detailed_async()
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
result = queries_ops.get_httpx_client_detailed_async()

# 2. Basic async
result = await queries_ops.get_httpx_client_detailed_async_async()

# 3. Detailed sync (with full HTTP response)
result = queries_ops.get_httpx_client_detailed_async_detailed()

# 4. Detailed async (with full HTTP response)
result = await queries_ops.get_httpx_client_detailed_async_detailed_async()
```

## Models

Operation-specific Pydantic models are available in:
```python
from python_alfresco_api.clients.core.queries.models import *
```

## Related Documentation

- [Core API Overview](../core_api.md)
- [V1.1 Architecture](../../clients_doc.md)
