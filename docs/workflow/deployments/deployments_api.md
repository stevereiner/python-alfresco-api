# Deployments Operations - Workflow API

Auto-generated from V1.1 hierarchical code on 2025-07-15 00:36:43

## Overview

Deployments operations for the Workflow API.

## Usage

```python
from python_alfresco_api import ClientFactory

# Create factory and client
factory = ClientFactory(base_url="http://localhost:8080")
workflow_client = factory.create_workflow_client()

# Access deployments operations
deployments_ops = workflow_client.deployments

# Real method examples (sync):
result = deployments_ops.get_httpx_client()

# Real method examples (async):
result = await deployments_ops.get_httpx_client_async()
```

## Available Methods

This subsection provides 1 operations:

### `get_httpx_client(self)`

Get direct access to raw httpx client for advanced operations.

Perfect for MCP servers that need raw HTTP access.

**Usage Patterns:**
```python
# 1. Basic sync
result = deployments_ops.get_httpx_client()

# 2. Basic async
result = await deployments_ops.get_httpx_client_async()

# 3. Detailed sync (with full HTTP response)
result = deployments_ops.get_httpx_client_detailed()

# 4. Detailed async (with full HTTP response)
result = await deployments_ops.get_httpx_client_detailed_async()
```

## Models

Operation-specific Pydantic models are available in:
```python
from python_alfresco_api.clients.workflow.deployments.models import *
```

## Related Documentation

- [Workflow API Overview](../workflow_api.md)
- [V1.1 Architecture](../../clients_doc.md)
