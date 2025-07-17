# Search API - V1.1 Hierarchical Architecture

Auto-generated from actual V1.1 code on 2025-07-15 00:36:43

## Overview

Search operations client with lazy-loaded subsections.

Provides high-level methods for Content and metadata search
that are essential for MCP servers and search workflows.

**Client Class**: `AlfrescoSearchClient`

## Quick Start

```python
from python_alfresco_api import ClientFactory

# Create factory
factory = ClientFactory(base_url="http://localhost:8080")

# Get search client
search_client = factory.create_search_client()

# Real method examples:
result = search_client.search.get_httpx_client()
result = await search_client.search.get_httpx_client_async()
```

## Architecture

This API follows the V1.1 three-tier hierarchical architecture:

- **Level 1**: Global models shared across all APIs
- **Level 2**: API-level models and client (`AlfrescoSearchClient`) 
- **Level 3**: Operation-specific subsections with focused functionality

## Subsections

This API is organized into the following operation groups:

### [Search](search/search_api.md)
Operations for search management.

**Available Methods:**
- `get_httpx_client(self)` - Get direct access to raw httpx client for advanced operations
- `search(self, body: Union[python_alfresco_api.raw_clients.alfresco_search_client.search_client.models.search_request.SearchRequest, python_alfresco_api.raw_clients.alfresco_search_client.search_client.types.Unset] = <python_alfresco_api.raw_clients.alfresco_search_client.search_client.types.Unset object at 0x000001D8C2F29730>) -> Any` - Search operation (sync)
- `search_async(self, body: Union[python_alfresco_api.raw_clients.alfresco_search_client.search_client.models.search_request.SearchRequest, python_alfresco_api.raw_clients.alfresco_search_client.search_client.types.Unset] = <python_alfresco_api.raw_clients.alfresco_search_client.search_client.types.Unset object at 0x000001D8C2F29730>) -> Any` - Search operation (async)
- *...and 2 more methods*

## Client Properties

Lazy-loaded subsection clients:

### `available`
Check if the search client is available and functional.

### `httpx_client`
Get direct access to httpx client for raw HTTP operations.

This is the STANDARD way to access the HTTP client.
Perfect for MCP servers that need raw HTTP access.

### `is_initialized`
Check if the client is initialized and functional.

This is the STANDARD way to check initialization status.

### `raw_client`
Get the raw authenticated client for advanced operations.

This is the STANDARD way to access the underlying client.

### `search`
Get the search operations client.

## Direct Methods

### `get_httpx_client(self)`
DEPRECATED: Use httpx_client property instead.

This method is kept for backward compatibility only.

### `search_content(self, *args, **kwargs)`
Search for content using SYNC operations.

**Parameters:**
- `args`: Any (required)
- `kwargs`: Any (required)

### `search_content_async(self, *args, **kwargs)`
Search for content using ASYNC operations.

**Parameters:**
- `args`: Any (required)
- `kwargs`: Any (required)

## Sync/Async Patterns

All operations support both synchronous and asynchronous execution:

```python
# Synchronous (perfect for scripts, MCP servers)
result = search_client.search.get_httpx_client()

# Asynchronous (perfect for web apps)
result = await search_client.search.get_httpx_client_async()
```

## 4-Pattern Method Examples

Each operation provides 4 execution patterns:

```python
# 1. Basic sync
result = search_client.search.get_httpx_client()

# 2. Basic async  
result = await search_client.search.get_httpx_client_async()

# 3. Detailed sync (with full HTTP response)
result = search_client.search.get_httpx_client_detailed()

# 4. Detailed async (with full HTTP response)
result = await search_client.search.get_httpx_client_async_detailed_async()
```

## Raw Client Access

For advanced operations, access the underlying HTTP client:

```python
# Get raw client
raw_client = search_client._get_raw_client()

# Get HTTPx client for custom requests
httpx_client = raw_client.get_httpx_client()
response = httpx_client.get("/custom-endpoint")
```

## Related Documentation

- [V1.1 Architecture Overview](../clients_doc.md)
- [Authentication Guide](../AUTHENTICATION_GUIDE.md)
- [MCP Integration Guide](../V11_MCP_SYNC_MIGRATION_GUIDE.md)
