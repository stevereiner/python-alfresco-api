# Workflow API - V1.1 Hierarchical Architecture

Auto-generated from actual V1.1 code on 2025-07-15 00:36:43

## Overview

Workflow operations client with lazy-loaded subsections.

Provides high-level methods for Process and task management
that are essential for MCP servers and workflow workflows.

**Client Class**: `AlfrescoWorkflowClient`

## Quick Start

```python
from python_alfresco_api import ClientFactory

# Create factory
factory = ClientFactory(base_url="http://localhost:8080")

# Get workflow client
workflow_client = factory.create_workflow_client()

# Real method examples:
result = deployments_client.deployments.get_httpx_client()
result = await deployments_client.deployments.get_httpx_client_async()
```

## Architecture

This API follows the V1.1 three-tier hierarchical architecture:

- **Level 1**: Global models shared across all APIs
- **Level 2**: API-level models and client (`AlfrescoWorkflowClient`) 
- **Level 3**: Operation-specific subsections with focused functionality

## Subsections

This API is organized into the following operation groups:

### [Deployments](deployments/deployments_api.md)
Operations for deployments management.

**Available Methods:**
- `get_httpx_client(self)` - Get direct access to raw httpx client for advanced operations

### [Processes](processes/processes_api.md)
Operations for processes management.

### [Process Definitions](process_definitions/process_definitions_api.md)
Operations for process definitions management.

### [Tasks](tasks/tasks_api.md)
Operations for tasks management.

## Client Properties

Lazy-loaded subsection clients:

### `available`
Check if the workflow client is available and functional.

### `deployments`
Get the deployments operations client.

### `httpx_client`
Get direct access to httpx client for raw HTTP operations.

This is the STANDARD way to access the HTTP client.
Perfect for MCP servers that need raw HTTP access.

### `is_initialized`
Check if the client is initialized and functional.

This is the STANDARD way to check initialization status.

### `process_definitions`
Get the process definitions operations client.

### `processes`
Get the processes operations client.

### `raw_client`
Get the raw authenticated client for advanced operations.

This is the STANDARD way to access the underlying client.

### `tasks`
Get the tasks operations client.

## Direct Methods

### `get_httpx_client(self)`
DEPRECATED: Use httpx_client property instead.

This method is kept for backward compatibility only.

### `get_httpx_client_detailed(self)`
DEPRECATED: Use httpx_client property instead.

This method is kept for backward compatibility only.

### `get_httpx_client_detailed_async(self)`
DEPRECATED: Use httpx_client property instead.

This method is kept for backward compatibility only.

## Sync/Async Patterns

All operations support both synchronous and asynchronous execution:

```python
# Synchronous (perfect for scripts, MCP servers)
result = deployments_client.deployments.get_httpx_client()

# Asynchronous (perfect for web apps)
result = await deployments_client.deployments.get_httpx_client_async()
```

## 4-Pattern Method Examples

Each operation provides 4 execution patterns:

```python
# 1. Basic sync
result = deployments_client.deployments.get_httpx_client()

# 2. Basic async  
result = await deployments_client.deployments.get_httpx_client_async()

# 3. Detailed sync (with full HTTP response)
result = deployments_client.deployments.get_httpx_client_detailed()

# 4. Detailed async (with full HTTP response)
result = await deployments_client.deployments.get_httpx_client_async_detailed_async()
```

## Raw Client Access

For advanced operations, access the underlying HTTP client:

```python
# Get raw client
raw_client = workflow_client._get_raw_client()

# Get HTTPx client for custom requests
httpx_client = raw_client.get_httpx_client()
response = httpx_client.get("/custom-endpoint")
```

## Related Documentation

- [V1.1 Architecture Overview](../clients_doc.md)
- [Authentication Guide](../AUTHENTICATION_GUIDE.md)
- [MCP Integration Guide](../V11_MCP_SYNC_MIGRATION_GUIDE.md)
