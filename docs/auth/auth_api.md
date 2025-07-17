# Auth API - V1.1 Hierarchical Architecture

Auto-generated from actual V1.1 code on 2025-07-15 00:36:43

## Overview

Auth operations client with lazy-loaded subsections.

Provides high-level methods for Authentication and ticket management
that are essential for MCP servers and auth workflows.

**Client Class**: `AlfrescoAuthClient`

## Quick Start

```python
from python_alfresco_api import ClientFactory

# Create factory
factory = ClientFactory(base_url="http://localhost:8080")

# Get auth client
auth_client = factory.create_auth_client()

# Real method examples:
# Example method calls
# Example async method calls
```

## Architecture

This API follows the V1.1 three-tier hierarchical architecture:

- **Level 1**: Global models shared across all APIs
- **Level 2**: API-level models and client (`AlfrescoAuthClient`) 
- **Level 3**: Operation-specific subsections with focused functionality

## Subsections

This API is organized into the following operation groups:

### [Authentication](authentication/authentication_api.md)
Operations for authentication management.

## Client Properties

Lazy-loaded subsection clients:

### `authentication`
Get the authentication operations client.

### `available`
Check if the auth client is available and functional.

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

## Direct Methods

### `create_ticket(self, *args, **kwargs)`
Create authentication ticket using SYNC operations.

**Parameters:**
- `args`: Any (required)
- `kwargs`: Any (required)

### `create_ticket_async(self, *args, **kwargs)`
Create authentication ticket using ASYNC operations.

**Parameters:**
- `args`: Any (required)
- `kwargs`: Any (required)

### `delete_ticket(self, *args, **kwargs)`
Delete authentication ticket using SYNC operations.

**Parameters:**
- `args`: Any (required)
- `kwargs`: Any (required)

### `delete_ticket_async(self, *args, **kwargs)`
Delete authentication ticket using ASYNC operations.

**Parameters:**
- `args`: Any (required)
- `kwargs`: Any (required)

### `get_httpx_client(self)`
DEPRECATED: Use httpx_client property instead.

This method is kept for backward compatibility only.

### `validate_ticket(self, *args, **kwargs)`
Validate authentication ticket using SYNC operations.

**Parameters:**
- `args`: Any (required)
- `kwargs`: Any (required)

### `validate_ticket_async(self, *args, **kwargs)`
Validate authentication ticket using ASYNC operations.

**Parameters:**
- `args`: Any (required)
- `kwargs`: Any (required)

## Sync/Async Patterns

All operations support both synchronous and asynchronous execution:

```python
# Synchronous (perfect for scripts, MCP servers)
result = client.operation.method()

# Asynchronous (perfect for web apps)
result = await client.operation.method_async()
```

## 4-Pattern Method Examples

Each operation provides 4 execution patterns:

```python
# 1. Basic sync
result = client.operation.method()

# 2. Basic async  
result = await client.operation.method_async()

# 3. Detailed sync (with full HTTP response)
result = client.operation.method_detailed()

# 4. Detailed async (with full HTTP response)
result = await client.operation.method_async_detailed_async()
```

## Raw Client Access

For advanced operations, access the underlying HTTP client:

```python
# Get raw client
raw_client = auth_client._get_raw_client()

# Get HTTPx client for custom requests
httpx_client = raw_client.get_httpx_client()
response = httpx_client.get("/custom-endpoint")
```

## Related Documentation

- [V1.1 Architecture Overview](../clients_doc.md)
- [Authentication Guide](../AUTHENTICATION_GUIDE.md)
- [MCP Integration Guide](../V11_MCP_SYNC_MIGRATION_GUIDE.md)
