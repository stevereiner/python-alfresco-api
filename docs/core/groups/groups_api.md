# Groups Operations - Core API

Auto-generated from V1.1 hierarchical code on 2025-07-15 00:36:43

## Overview

Groups operations for the Core API.

## Usage

```python
from python_alfresco_api import ClientFactory

# Create factory and client
factory = ClientFactory(base_url="http://localhost:8080")
core_client = factory.create_core_client()

# Access groups operations
groups_ops = core_client.groups

# Real method examples (sync):
result = groups_ops.get_httpx_client()

# Real method examples (async):
result = await groups_ops.get_httpx_client_async()
```

## Available Methods

This subsection provides 1 operations:

### `get_httpx_client(self)`

Get direct access to raw httpx client for advanced operations.

Perfect for MCP servers that need raw HTTP access.

**Usage Patterns:**
```python
# 1. Basic sync
result = groups_ops.get_httpx_client()

# 2. Basic async
result = await groups_ops.get_httpx_client_async()

# 3. Detailed sync (with full HTTP response)
result = groups_ops.get_httpx_client_detailed()

# 4. Detailed async (with full HTTP response)
result = await groups_ops.get_httpx_client_detailed_async()
```

## Models

Operation-specific Pydantic models are available in:
```python
from python_alfresco_api.clients.core.groups.models import *
```

## Related Documentation

- [Core API Overview](../core_api.md)
- [V1.1 Architecture](../../clients_doc.md)
