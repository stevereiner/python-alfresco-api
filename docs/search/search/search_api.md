# Search Operations - Search API

Auto-generated from V1.1 hierarchical code on 2025-07-15 00:36:43

## Overview

Search operations for the Search API.

## Usage

```python
from python_alfresco_api import ClientFactory

# Create factory and client
factory = ClientFactory(base_url="http://localhost:8080")
search_client = factory.create_search_client()

# Access search operations
search_ops = search_client.search

# Real method examples (sync):
result = search_ops.get_httpx_client()
result = search_ops.search(body=request_data)
result = search_ops.search_async(body=request_data)

# Real method examples (async):
result = await search_ops.get_httpx_client_async()
result = await search_ops.search_async(body=request_data)
result = await search_ops.search_async_async(body=request_data)
```

## Available Methods

This subsection provides 5 operations:

### `get_httpx_client(self)`

Get direct access to raw httpx client for advanced operations.

Perfect for MCP servers that need raw HTTP access.

**Usage Patterns:**
```python
# 1. Basic sync
result = search_ops.get_httpx_client()

# 2. Basic async
result = await search_ops.get_httpx_client_async()

# 3. Detailed sync (with full HTTP response)
result = search_ops.get_httpx_client_detailed()

# 4. Detailed async (with full HTTP response)
result = await search_ops.get_httpx_client_detailed_async()
```

### `search(self, body: Union[python_alfresco_api.raw_clients.alfresco_search_client.search_client.models.search_request.SearchRequest, python_alfresco_api.raw_clients.alfresco_search_client.search_client.types.Unset] = <python_alfresco_api.raw_clients.alfresco_search_client.search_client.types.Unset object at 0x000001D8C2F29730>) -> Any`

Search operation (sync).

Perfect for MCP servers and search workflows.
Returns parsed response for common use cases.

Args:
    body: Union[SearchRequest, Unset] = UNSET

Returns:
    Parsed response object

**Parameters:**
- `body`: typing.Union[python_alfresco_api.raw_clients.alfresco_search_client.search_client.models.search_request.SearchRequest, python_alfresco_api.raw_clients.alfresco_search_client.search_client.types.Unset] (default: <python_alfresco_api.raw_clients.alfresco_search_client.search_client.types.Unset object at 0x000001D8C2F29730>)

**Usage Patterns:**
```python
# 1. Basic sync
result = search_ops.search(body=request_data)

# 2. Basic async
result = await search_ops.search_async(body=request_data)

# 3. Detailed sync (with full HTTP response)
result = search_ops.search_detailed(body=request_data)

# 4. Detailed async (with full HTTP response)
result = await search_ops.search_detailed_async(body=request_data)
```

### `search_async(self, body: Union[python_alfresco_api.raw_clients.alfresco_search_client.search_client.models.search_request.SearchRequest, python_alfresco_api.raw_clients.alfresco_search_client.search_client.types.Unset] = <python_alfresco_api.raw_clients.alfresco_search_client.search_client.types.Unset object at 0x000001D8C2F29730>) -> Any`

Search operation (async).

Perfect for MCP servers and search workflows.
Returns parsed response for common use cases.

Args:
    body: Union[SearchRequest, Unset] = UNSET

Returns:
    Parsed response object

**Parameters:**
- `body`: typing.Union[python_alfresco_api.raw_clients.alfresco_search_client.search_client.models.search_request.SearchRequest, python_alfresco_api.raw_clients.alfresco_search_client.search_client.types.Unset] (default: <python_alfresco_api.raw_clients.alfresco_search_client.search_client.types.Unset object at 0x000001D8C2F29730>)

**Usage Patterns:**
```python
# 1. Basic sync
result = search_ops.search_async(body=request_data)

# 2. Basic async
result = await search_ops.search_async_async(body=request_data)

# 3. Detailed sync (with full HTTP response)
result = search_ops.search_async_detailed(body=request_data)

# 4. Detailed async (with full HTTP response)
result = await search_ops.search_async_detailed_async(body=request_data)
```

### `search_detailed(self, body: Union[python_alfresco_api.raw_clients.alfresco_search_client.search_client.models.search_request.SearchRequest, python_alfresco_api.raw_clients.alfresco_search_client.search_client.types.Unset] = <python_alfresco_api.raw_clients.alfresco_search_client.search_client.types.Unset object at 0x000001D8C2F29730>)`

Search operation (detailed sync).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

Args:
    body: Union[SearchRequest, Unset] = UNSET

Returns:
    Response: Complete response with status_code, headers, content, parsed

**Parameters:**
- `body`: typing.Union[python_alfresco_api.raw_clients.alfresco_search_client.search_client.models.search_request.SearchRequest, python_alfresco_api.raw_clients.alfresco_search_client.search_client.types.Unset] (default: <python_alfresco_api.raw_clients.alfresco_search_client.search_client.types.Unset object at 0x000001D8C2F29730>)

**Usage Patterns:**
```python
# 1. Basic sync
result = search_ops.search_detailed(body=request_data)

# 2. Basic async
result = await search_ops.search_detailed_async(body=request_data)

# 3. Detailed sync (with full HTTP response)
result = search_ops.search_detailed_detailed(body=request_data)

# 4. Detailed async (with full HTTP response)
result = await search_ops.search_detailed_detailed_async(body=request_data)
```

### `search_detailed_async(self, body: Union[python_alfresco_api.raw_clients.alfresco_search_client.search_client.models.search_request.SearchRequest, python_alfresco_api.raw_clients.alfresco_search_client.search_client.types.Unset] = <python_alfresco_api.raw_clients.alfresco_search_client.search_client.types.Unset object at 0x000001D8C2F29730>)`

Search operation (detailed async).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

Args:
    body: Union[SearchRequest, Unset] = UNSET

Returns:
    Response: Complete response with status_code, headers, content, parsed

**Parameters:**
- `body`: typing.Union[python_alfresco_api.raw_clients.alfresco_search_client.search_client.models.search_request.SearchRequest, python_alfresco_api.raw_clients.alfresco_search_client.search_client.types.Unset] (default: <python_alfresco_api.raw_clients.alfresco_search_client.search_client.types.Unset object at 0x000001D8C2F29730>)

**Usage Patterns:**
```python
# 1. Basic sync
result = search_ops.search_detailed_async(body=request_data)

# 2. Basic async
result = await search_ops.search_detailed_async_async(body=request_data)

# 3. Detailed sync (with full HTTP response)
result = search_ops.search_detailed_async_detailed(body=request_data)

# 4. Detailed async (with full HTTP response)
result = await search_ops.search_detailed_async_detailed_async(body=request_data)
```

## Models

Operation-specific Pydantic models are available in:
```python
from python_alfresco_api.clients.search.search.models import *
```

## Related Documentation

- [Search API Overview](../search_api.md)
- [V1.1 Architecture](../../clients_doc.md)
