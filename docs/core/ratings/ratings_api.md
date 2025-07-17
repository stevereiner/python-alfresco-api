# Ratings Operations - Core API

Auto-generated from V1.1 hierarchical code on 2025-07-15 00:36:43

## Overview

Ratings operations for the Core API.

## Usage

```python
from python_alfresco_api import ClientFactory

# Create factory and client
factory = ClientFactory(base_url="http://localhost:8080")
core_client = factory.create_core_client()

# Access ratings operations
ratings_ops = core_client.ratings

# Real method examples (sync):
result = ratings_ops.create_rating(node_id="abc123-def456", body=request_data, fields=...)
result = ratings_ops.create_rating_async(node_id="abc123-def456", body=request_data, fields=...)
result = ratings_ops.create_rating_detailed(node_id="abc123-def456", body=request_data, fields=...)

# Real method examples (async):
result = await ratings_ops.create_rating_async(node_id="abc123-def456", body=request_data, fields=...)
result = await ratings_ops.create_rating_async_async(node_id="abc123-def456", body=request_data, fields=...)
result = await ratings_ops.create_rating_detailed_async(node_id="abc123-def456", body=request_data, fields=...)
```

## Available Methods

This subsection provides 19 operations:

### `create_rating(self, node_id: Any, body: Any, fields: Any) -> python_alfresco_api.clients.core.ratings.models.RatingsResponse`

Create Rating operation.

Perfect for MCP servers and ratings workflows.
Returns simplified response for common use cases.

**Parameters:**
- `node_id`: typing.Any (required)
- `body`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = ratings_ops.create_rating(node_id="abc123-def456", body=request_data, fields=...)

# 2. Basic async
result = await ratings_ops.create_rating_async(node_id="abc123-def456", body=request_data, fields=...)

# 3. Detailed sync (with full HTTP response)
result = ratings_ops.create_rating_detailed(node_id="abc123-def456", body=request_data, fields=...)

# 4. Detailed async (with full HTTP response)
result = await ratings_ops.create_rating_detailed_async(node_id="abc123-def456", body=request_data, fields=...)
```

### `create_rating_async(self, node_id: Any, body: Any, fields: Any) -> python_alfresco_api.clients.core.ratings.models.RatingsResponse`

Create Rating operation (async).

Perfect for MCP servers and ratings workflows.
Returns simplified response for common use cases.

**Parameters:**
- `node_id`: typing.Any (required)
- `body`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = ratings_ops.create_rating_async(node_id="abc123-def456", body=request_data, fields=...)

# 2. Basic async
result = await ratings_ops.create_rating_async_async(node_id="abc123-def456", body=request_data, fields=...)

# 3. Detailed sync (with full HTTP response)
result = ratings_ops.create_rating_async_detailed(node_id="abc123-def456", body=request_data, fields=...)

# 4. Detailed async (with full HTTP response)
result = await ratings_ops.create_rating_async_detailed_async(node_id="abc123-def456", body=request_data, fields=...)
```

### `create_rating_detailed(self, node_id: Any, body: Any, fields: Any)`

Create Rating operation (detailed).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `node_id`: typing.Any (required)
- `body`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = ratings_ops.create_rating_detailed(node_id="abc123-def456", body=request_data, fields=...)

# 2. Basic async
result = await ratings_ops.create_rating_detailed_async(node_id="abc123-def456", body=request_data, fields=...)

# 3. Detailed sync (with full HTTP response)
result = ratings_ops.create_rating_detailed_detailed(node_id="abc123-def456", body=request_data, fields=...)

# 4. Detailed async (with full HTTP response)
result = await ratings_ops.create_rating_detailed_detailed_async(node_id="abc123-def456", body=request_data, fields=...)
```

### `create_rating_detailed_async(self, node_id: Any, body: Any, fields: Any)`

Create Rating operation (detailed, async).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `node_id`: typing.Any (required)
- `body`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = ratings_ops.create_rating_detailed_async(node_id="abc123-def456", body=request_data, fields=...)

# 2. Basic async
result = await ratings_ops.create_rating_detailed_async_async(node_id="abc123-def456", body=request_data, fields=...)

# 3. Detailed sync (with full HTTP response)
result = ratings_ops.create_rating_detailed_async_detailed(node_id="abc123-def456", body=request_data, fields=...)

# 4. Detailed async (with full HTTP response)
result = await ratings_ops.create_rating_detailed_async_detailed_async(node_id="abc123-def456", body=request_data, fields=...)
```

### `delete_rating(self, node_id: Any, rating_id: Any) -> python_alfresco_api.clients.core.ratings.models.RatingsResponse`

Delete Rating operation.

Perfect for MCP servers and ratings workflows.
Returns simplified response for common use cases.

**Parameters:**
- `node_id`: typing.Any (required)
- `rating_id`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = ratings_ops.delete_rating(node_id="abc123-def456", rating_id="abc123-def456")

# 2. Basic async
result = await ratings_ops.delete_rating_async(node_id="abc123-def456", rating_id="abc123-def456")

# 3. Detailed sync (with full HTTP response)
result = ratings_ops.delete_rating_detailed(node_id="abc123-def456", rating_id="abc123-def456")

# 4. Detailed async (with full HTTP response)
result = await ratings_ops.delete_rating_detailed_async(node_id="abc123-def456", rating_id="abc123-def456")
```

### `delete_rating_async(self, node_id: Any, rating_id: Any) -> python_alfresco_api.clients.core.ratings.models.RatingsResponse`

Delete Rating operation (async).

Perfect for MCP servers and ratings workflows.
Returns simplified response for common use cases.

**Parameters:**
- `node_id`: typing.Any (required)
- `rating_id`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = ratings_ops.delete_rating_async(node_id="abc123-def456", rating_id="abc123-def456")

# 2. Basic async
result = await ratings_ops.delete_rating_async_async(node_id="abc123-def456", rating_id="abc123-def456")

# 3. Detailed sync (with full HTTP response)
result = ratings_ops.delete_rating_async_detailed(node_id="abc123-def456", rating_id="abc123-def456")

# 4. Detailed async (with full HTTP response)
result = await ratings_ops.delete_rating_async_detailed_async(node_id="abc123-def456", rating_id="abc123-def456")
```

### `delete_rating_detailed(self, node_id: Any, rating_id: Any)`

Delete Rating operation (detailed).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `node_id`: typing.Any (required)
- `rating_id`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = ratings_ops.delete_rating_detailed(node_id="abc123-def456", rating_id="abc123-def456")

# 2. Basic async
result = await ratings_ops.delete_rating_detailed_async(node_id="abc123-def456", rating_id="abc123-def456")

# 3. Detailed sync (with full HTTP response)
result = ratings_ops.delete_rating_detailed_detailed(node_id="abc123-def456", rating_id="abc123-def456")

# 4. Detailed async (with full HTTP response)
result = await ratings_ops.delete_rating_detailed_detailed_async(node_id="abc123-def456", rating_id="abc123-def456")
```

### `delete_rating_detailed_async(self, node_id: Any, rating_id: Any)`

Delete Rating operation (detailed, async).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `node_id`: typing.Any (required)
- `rating_id`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = ratings_ops.delete_rating_detailed_async(node_id="abc123-def456", rating_id="abc123-def456")

# 2. Basic async
result = await ratings_ops.delete_rating_detailed_async_async(node_id="abc123-def456", rating_id="abc123-def456")

# 3. Detailed sync (with full HTTP response)
result = ratings_ops.delete_rating_detailed_async_detailed(node_id="abc123-def456", rating_id="abc123-def456")

# 4. Detailed async (with full HTTP response)
result = await ratings_ops.delete_rating_detailed_async_detailed_async(node_id="abc123-def456", rating_id="abc123-def456")
```

### `get_httpx_client(self)`

Get direct access to raw httpx client for advanced operations.

Perfect for MCP servers that need raw HTTP access.

**Usage Patterns:**
```python
# 1. Basic sync
result = ratings_ops.get_httpx_client()

# 2. Basic async
result = await ratings_ops.get_httpx_client_async()

# 3. Detailed sync (with full HTTP response)
result = ratings_ops.get_httpx_client_detailed()

# 4. Detailed async (with full HTTP response)
result = await ratings_ops.get_httpx_client_detailed_async()
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
result = ratings_ops.get_httpx_client_detailed()

# 2. Basic async
result = await ratings_ops.get_httpx_client_detailed_async()

# 3. Detailed sync (with full HTTP response)
result = ratings_ops.get_httpx_client_detailed_detailed()

# 4. Detailed async (with full HTTP response)
result = await ratings_ops.get_httpx_client_detailed_detailed_async()
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
result = ratings_ops.get_httpx_client_detailed_async()

# 2. Basic async
result = await ratings_ops.get_httpx_client_detailed_async_async()

# 3. Detailed sync (with full HTTP response)
result = ratings_ops.get_httpx_client_detailed_async_detailed()

# 4. Detailed async (with full HTTP response)
result = await ratings_ops.get_httpx_client_detailed_async_detailed_async()
```

### `get_rating(self, node_id: Any, rating_id: Any, fields: Any) -> python_alfresco_api.clients.core.ratings.models.RatingsResponse`

Get Rating operation.

Perfect for MCP servers and ratings workflows.
Returns simplified response for common use cases.

**Parameters:**
- `node_id`: typing.Any (required)
- `rating_id`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = ratings_ops.get_rating(node_id="abc123-def456", rating_id="abc123-def456", fields=...)

# 2. Basic async
result = await ratings_ops.get_rating_async(node_id="abc123-def456", rating_id="abc123-def456", fields=...)

# 3. Detailed sync (with full HTTP response)
result = ratings_ops.get_rating_detailed(node_id="abc123-def456", rating_id="abc123-def456", fields=...)

# 4. Detailed async (with full HTTP response)
result = await ratings_ops.get_rating_detailed_async(node_id="abc123-def456", rating_id="abc123-def456", fields=...)
```

### `get_rating_async(self, node_id: Any, rating_id: Any, fields: Any) -> python_alfresco_api.clients.core.ratings.models.RatingsResponse`

Get Rating operation (async).

Perfect for MCP servers and ratings workflows.
Returns simplified response for common use cases.

**Parameters:**
- `node_id`: typing.Any (required)
- `rating_id`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = ratings_ops.get_rating_async(node_id="abc123-def456", rating_id="abc123-def456", fields=...)

# 2. Basic async
result = await ratings_ops.get_rating_async_async(node_id="abc123-def456", rating_id="abc123-def456", fields=...)

# 3. Detailed sync (with full HTTP response)
result = ratings_ops.get_rating_async_detailed(node_id="abc123-def456", rating_id="abc123-def456", fields=...)

# 4. Detailed async (with full HTTP response)
result = await ratings_ops.get_rating_async_detailed_async(node_id="abc123-def456", rating_id="abc123-def456", fields=...)
```

### `get_rating_detailed(self, node_id: Any, rating_id: Any, fields: Any)`

Get Rating operation (detailed).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `node_id`: typing.Any (required)
- `rating_id`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = ratings_ops.get_rating_detailed(node_id="abc123-def456", rating_id="abc123-def456", fields=...)

# 2. Basic async
result = await ratings_ops.get_rating_detailed_async(node_id="abc123-def456", rating_id="abc123-def456", fields=...)

# 3. Detailed sync (with full HTTP response)
result = ratings_ops.get_rating_detailed_detailed(node_id="abc123-def456", rating_id="abc123-def456", fields=...)

# 4. Detailed async (with full HTTP response)
result = await ratings_ops.get_rating_detailed_detailed_async(node_id="abc123-def456", rating_id="abc123-def456", fields=...)
```

### `get_rating_detailed_async(self, node_id: Any, rating_id: Any, fields: Any)`

Get Rating operation (detailed, async).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `node_id`: typing.Any (required)
- `rating_id`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = ratings_ops.get_rating_detailed_async(node_id="abc123-def456", rating_id="abc123-def456", fields=...)

# 2. Basic async
result = await ratings_ops.get_rating_detailed_async_async(node_id="abc123-def456", rating_id="abc123-def456", fields=...)

# 3. Detailed sync (with full HTTP response)
result = ratings_ops.get_rating_detailed_async_detailed(node_id="abc123-def456", rating_id="abc123-def456", fields=...)

# 4. Detailed async (with full HTTP response)
result = await ratings_ops.get_rating_detailed_async_detailed_async(node_id="abc123-def456", rating_id="abc123-def456", fields=...)
```

### `list_ratings(self, node_id: Any, skip_count: Any, max_items: Any, fields: Any) -> python_alfresco_api.clients.core.ratings.models.RatingsResponse`

List Ratings operation.

Perfect for MCP servers and ratings workflows.
Returns simplified response for common use cases.

**Parameters:**
- `node_id`: typing.Any (required)
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = ratings_ops.list_ratings(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)

# 2. Basic async
result = await ratings_ops.list_ratings_async(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)

# 3. Detailed sync (with full HTTP response)
result = ratings_ops.list_ratings_detailed(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)

# 4. Detailed async (with full HTTP response)
result = await ratings_ops.list_ratings_detailed_async(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)
```

### `list_ratings_async(self, node_id: Any, skip_count: Any, max_items: Any, fields: Any) -> python_alfresco_api.clients.core.ratings.models.RatingsResponse`

List Ratings operation (async).

Perfect for MCP servers and ratings workflows.
Returns simplified response for common use cases.

**Parameters:**
- `node_id`: typing.Any (required)
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = ratings_ops.list_ratings_async(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)

# 2. Basic async
result = await ratings_ops.list_ratings_async_async(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)

# 3. Detailed sync (with full HTTP response)
result = ratings_ops.list_ratings_async_detailed(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)

# 4. Detailed async (with full HTTP response)
result = await ratings_ops.list_ratings_async_detailed_async(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)
```

### `list_ratings_detailed(self, node_id: Any, skip_count: Any, max_items: Any, fields: Any)`

List Ratings operation (detailed).

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
result = ratings_ops.list_ratings_detailed(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)

# 2. Basic async
result = await ratings_ops.list_ratings_detailed_async(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)

# 3. Detailed sync (with full HTTP response)
result = ratings_ops.list_ratings_detailed_detailed(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)

# 4. Detailed async (with full HTTP response)
result = await ratings_ops.list_ratings_detailed_detailed_async(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)
```

### `list_ratings_detailed_async(self, node_id: Any, skip_count: Any, max_items: Any, fields: Any)`

List Ratings operation (detailed, async).

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
result = ratings_ops.list_ratings_detailed_async(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)

# 2. Basic async
result = await ratings_ops.list_ratings_detailed_async_async(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)

# 3. Detailed sync (with full HTTP response)
result = ratings_ops.list_ratings_detailed_async_detailed(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)

# 4. Detailed async (with full HTTP response)
result = await ratings_ops.list_ratings_detailed_async_detailed_async(node_id="abc123-def456", skip_count=..., max_items=..., fields=...)
```

## Models

Operation-specific Pydantic models are available in:
```python
from python_alfresco_api.clients.core.ratings.models import *
```

## Related Documentation

- [Core API Overview](../core_api.md)
- [V1.1 Architecture](../../clients_doc.md)
