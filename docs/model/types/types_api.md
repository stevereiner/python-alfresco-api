# Types Operations - Model API

Auto-generated from V1.1 hierarchical code on 2025-07-15 00:36:43

## Overview

Types operations for the Model API.

## Usage

```python
from python_alfresco_api import ClientFactory

# Create factory and client
factory = ClientFactory(base_url="http://localhost:8080")
model_client = factory.create_model_client()

# Access types operations
types_ops = model_client.types

# Real method examples (sync):
result = types_ops.get_httpx_client()

# Real method examples (async):
result = await types_ops.get_httpx_client_async()
```

## Available Methods

This subsection provides 1 operations:

### `get_httpx_client(self)`

Get direct access to raw httpx client for advanced operations.

Perfect for MCP servers that need raw HTTP access.

**Usage Patterns:**
```python
# 1. Basic sync
result = types_ops.get_httpx_client()

# 2. Basic async
result = await types_ops.get_httpx_client_async()

# 3. Detailed sync (with full HTTP response)
result = types_ops.get_httpx_client_detailed()

# 4. Detailed async (with full HTTP response)
result = await types_ops.get_httpx_client_detailed_async()
```

## Models

Operation-specific Pydantic models are available in:
```python
from python_alfresco_api.clients.model.types.models import *
```

## Related Documentation

- [Model API Overview](../model_api.md)
- [V1.1 Architecture](../../clients_doc.md)
