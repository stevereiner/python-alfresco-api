# Actions Operations - Core API

Auto-generated from V1.1 hierarchical code on 2025-07-15 00:36:43

## Overview

Actions operations for the Core API.

## Usage

```python
from python_alfresco_api import ClientFactory

# Create factory and client
factory = ClientFactory(base_url="http://localhost:8080")
core_client = factory.create_core_client()

# Access actions operations
actions_ops = core_client.actions

# Real method examples (sync):
result = actions_ops.action_details(action_definition_id="abc123-def456")
result = actions_ops.action_details_async(action_definition_id="abc123-def456")
result = actions_ops.action_details_detailed(action_definition_id="abc123-def456")

# Real method examples (async):
result = await actions_ops.action_details_async(action_definition_id="abc123-def456")
result = await actions_ops.action_details_async_async(action_definition_id="abc123-def456")
result = await actions_ops.action_details_detailed_async(action_definition_id="abc123-def456")
```

## Available Methods

This subsection provides 17 operations:

### `action_details(self, action_definition_id: Any) -> python_alfresco_api.clients.core.actions.models.ActionsResponse`

Action Details operation.

Perfect for MCP servers and actions workflows.
Returns simplified response for common use cases.

**Parameters:**
- `action_definition_id`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = actions_ops.action_details(action_definition_id="abc123-def456")

# 2. Basic async
result = await actions_ops.action_details_async(action_definition_id="abc123-def456")

# 3. Detailed sync (with full HTTP response)
result = actions_ops.action_details_detailed(action_definition_id="abc123-def456")

# 4. Detailed async (with full HTTP response)
result = await actions_ops.action_details_detailed_async(action_definition_id="abc123-def456")
```

### `action_details_async(self, action_definition_id: Any) -> python_alfresco_api.clients.core.actions.models.ActionsResponse`

Action Details operation (async).

Perfect for MCP servers and actions workflows.
Returns simplified response for common use cases.

**Parameters:**
- `action_definition_id`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = actions_ops.action_details_async(action_definition_id="abc123-def456")

# 2. Basic async
result = await actions_ops.action_details_async_async(action_definition_id="abc123-def456")

# 3. Detailed sync (with full HTTP response)
result = actions_ops.action_details_async_detailed(action_definition_id="abc123-def456")

# 4. Detailed async (with full HTTP response)
result = await actions_ops.action_details_async_detailed_async(action_definition_id="abc123-def456")
```

### `action_details_detailed(self, action_definition_id: Any)`

Action Details operation (detailed).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `action_definition_id`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = actions_ops.action_details_detailed(action_definition_id="abc123-def456")

# 2. Basic async
result = await actions_ops.action_details_detailed_async(action_definition_id="abc123-def456")

# 3. Detailed sync (with full HTTP response)
result = actions_ops.action_details_detailed_detailed(action_definition_id="abc123-def456")

# 4. Detailed async (with full HTTP response)
result = await actions_ops.action_details_detailed_detailed_async(action_definition_id="abc123-def456")
```

### `action_details_detailed_async(self, action_definition_id: Any)`

Action Details operation (detailed, async).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `action_definition_id`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = actions_ops.action_details_detailed_async(action_definition_id="abc123-def456")

# 2. Basic async
result = await actions_ops.action_details_detailed_async_async(action_definition_id="abc123-def456")

# 3. Detailed sync (with full HTTP response)
result = actions_ops.action_details_detailed_async_detailed(action_definition_id="abc123-def456")

# 4. Detailed async (with full HTTP response)
result = await actions_ops.action_details_detailed_async_detailed_async(action_definition_id="abc123-def456")
```

### `action_exec(self, body: Any) -> python_alfresco_api.clients.core.actions.models.ActionsResponse`

Action Exec operation.

Perfect for MCP servers and actions workflows.
Returns simplified response for common use cases.

**Parameters:**
- `body`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = actions_ops.action_exec(body=request_data)

# 2. Basic async
result = await actions_ops.action_exec_async(body=request_data)

# 3. Detailed sync (with full HTTP response)
result = actions_ops.action_exec_detailed(body=request_data)

# 4. Detailed async (with full HTTP response)
result = await actions_ops.action_exec_detailed_async(body=request_data)
```

### `action_exec_async(self, body: Any) -> python_alfresco_api.clients.core.actions.models.ActionsResponse`

Action Exec operation (async).

Perfect for MCP servers and actions workflows.
Returns simplified response for common use cases.

**Parameters:**
- `body`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = actions_ops.action_exec_async(body=request_data)

# 2. Basic async
result = await actions_ops.action_exec_async_async(body=request_data)

# 3. Detailed sync (with full HTTP response)
result = actions_ops.action_exec_async_detailed(body=request_data)

# 4. Detailed async (with full HTTP response)
result = await actions_ops.action_exec_async_detailed_async(body=request_data)
```

### `action_exec_detailed(self, body: Any)`

Action Exec operation (detailed).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `body`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = actions_ops.action_exec_detailed(body=request_data)

# 2. Basic async
result = await actions_ops.action_exec_detailed_async(body=request_data)

# 3. Detailed sync (with full HTTP response)
result = actions_ops.action_exec_detailed_detailed(body=request_data)

# 4. Detailed async (with full HTTP response)
result = await actions_ops.action_exec_detailed_detailed_async(body=request_data)
```

### `action_exec_detailed_async(self, body: Any)`

Action Exec operation (detailed, async).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `body`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = actions_ops.action_exec_detailed_async(body=request_data)

# 2. Basic async
result = await actions_ops.action_exec_detailed_async_async(body=request_data)

# 3. Detailed sync (with full HTTP response)
result = actions_ops.action_exec_detailed_async_detailed(body=request_data)

# 4. Detailed async (with full HTTP response)
result = await actions_ops.action_exec_detailed_async_detailed_async(body=request_data)
```

### `get_httpx_client(self)`

Get direct access to raw httpx client for advanced operations.

Perfect for MCP servers that need raw HTTP access.

**Usage Patterns:**
```python
# 1. Basic sync
result = actions_ops.get_httpx_client()

# 2. Basic async
result = await actions_ops.get_httpx_client_async()

# 3. Detailed sync (with full HTTP response)
result = actions_ops.get_httpx_client_detailed()

# 4. Detailed async (with full HTTP response)
result = await actions_ops.get_httpx_client_detailed_async()
```

### `list_actions(self, skip_count: Any, max_items: Any, order_by: Any, fields: Any) -> python_alfresco_api.clients.core.actions.models.ActionsResponse`

List Actions operation.

Perfect for MCP servers and actions workflows.
Returns simplified response for common use cases.

**Parameters:**
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `order_by`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = actions_ops.list_actions(skip_count=..., max_items=..., order_by=..., fields=...)

# 2. Basic async
result = await actions_ops.list_actions_async(skip_count=..., max_items=..., order_by=..., fields=...)

# 3. Detailed sync (with full HTTP response)
result = actions_ops.list_actions_detailed(skip_count=..., max_items=..., order_by=..., fields=...)

# 4. Detailed async (with full HTTP response)
result = await actions_ops.list_actions_detailed_async(skip_count=..., max_items=..., order_by=..., fields=...)
```

### `list_actions_async(self, skip_count: Any, max_items: Any, order_by: Any, fields: Any) -> python_alfresco_api.clients.core.actions.models.ActionsResponse`

List Actions operation (async).

Perfect for MCP servers and actions workflows.
Returns simplified response for common use cases.

**Parameters:**
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `order_by`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = actions_ops.list_actions_async(skip_count=..., max_items=..., order_by=..., fields=...)

# 2. Basic async
result = await actions_ops.list_actions_async_async(skip_count=..., max_items=..., order_by=..., fields=...)

# 3. Detailed sync (with full HTTP response)
result = actions_ops.list_actions_async_detailed(skip_count=..., max_items=..., order_by=..., fields=...)

# 4. Detailed async (with full HTTP response)
result = await actions_ops.list_actions_async_detailed_async(skip_count=..., max_items=..., order_by=..., fields=...)
```

### `list_actions_detailed(self, skip_count: Any, max_items: Any, order_by: Any, fields: Any)`

List Actions operation (detailed).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `order_by`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = actions_ops.list_actions_detailed(skip_count=..., max_items=..., order_by=..., fields=...)

# 2. Basic async
result = await actions_ops.list_actions_detailed_async(skip_count=..., max_items=..., order_by=..., fields=...)

# 3. Detailed sync (with full HTTP response)
result = actions_ops.list_actions_detailed_detailed(skip_count=..., max_items=..., order_by=..., fields=...)

# 4. Detailed async (with full HTTP response)
result = await actions_ops.list_actions_detailed_detailed_async(skip_count=..., max_items=..., order_by=..., fields=...)
```

### `list_actions_detailed_async(self, skip_count: Any, max_items: Any, order_by: Any, fields: Any)`

List Actions operation (detailed, async).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `order_by`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = actions_ops.list_actions_detailed_async(skip_count=..., max_items=..., order_by=..., fields=...)

# 2. Basic async
result = await actions_ops.list_actions_detailed_async_async(skip_count=..., max_items=..., order_by=..., fields=...)

# 3. Detailed sync (with full HTTP response)
result = actions_ops.list_actions_detailed_async_detailed(skip_count=..., max_items=..., order_by=..., fields=...)

# 4. Detailed async (with full HTTP response)
result = await actions_ops.list_actions_detailed_async_detailed_async(skip_count=..., max_items=..., order_by=..., fields=...)
```

### `node_actions(self, node_id: Any, skip_count: Any, max_items: Any, order_by: Any, fields: Any) -> python_alfresco_api.clients.core.actions.models.ActionsResponse`

Node Actions operation.

Perfect for MCP servers and actions workflows.
Returns simplified response for common use cases.

**Parameters:**
- `node_id`: typing.Any (required)
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `order_by`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = actions_ops.node_actions(node_id="abc123-def456", skip_count=..., max_items=..., order_by=..., fields=...)

# 2. Basic async
result = await actions_ops.node_actions_async(node_id="abc123-def456", skip_count=..., max_items=..., order_by=..., fields=...)

# 3. Detailed sync (with full HTTP response)
result = actions_ops.node_actions_detailed(node_id="abc123-def456", skip_count=..., max_items=..., order_by=..., fields=...)

# 4. Detailed async (with full HTTP response)
result = await actions_ops.node_actions_detailed_async(node_id="abc123-def456", skip_count=..., max_items=..., order_by=..., fields=...)
```

### `node_actions_async(self, node_id: Any, skip_count: Any, max_items: Any, order_by: Any, fields: Any) -> python_alfresco_api.clients.core.actions.models.ActionsResponse`

Node Actions operation (async).

Perfect for MCP servers and actions workflows.
Returns simplified response for common use cases.

**Parameters:**
- `node_id`: typing.Any (required)
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `order_by`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = actions_ops.node_actions_async(node_id="abc123-def456", skip_count=..., max_items=..., order_by=..., fields=...)

# 2. Basic async
result = await actions_ops.node_actions_async_async(node_id="abc123-def456", skip_count=..., max_items=..., order_by=..., fields=...)

# 3. Detailed sync (with full HTTP response)
result = actions_ops.node_actions_async_detailed(node_id="abc123-def456", skip_count=..., max_items=..., order_by=..., fields=...)

# 4. Detailed async (with full HTTP response)
result = await actions_ops.node_actions_async_detailed_async(node_id="abc123-def456", skip_count=..., max_items=..., order_by=..., fields=...)
```

### `node_actions_detailed(self, node_id: Any, skip_count: Any, max_items: Any, order_by: Any, fields: Any)`

Node Actions operation (detailed).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `node_id`: typing.Any (required)
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `order_by`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = actions_ops.node_actions_detailed(node_id="abc123-def456", skip_count=..., max_items=..., order_by=..., fields=...)

# 2. Basic async
result = await actions_ops.node_actions_detailed_async(node_id="abc123-def456", skip_count=..., max_items=..., order_by=..., fields=...)

# 3. Detailed sync (with full HTTP response)
result = actions_ops.node_actions_detailed_detailed(node_id="abc123-def456", skip_count=..., max_items=..., order_by=..., fields=...)

# 4. Detailed async (with full HTTP response)
result = await actions_ops.node_actions_detailed_detailed_async(node_id="abc123-def456", skip_count=..., max_items=..., order_by=..., fields=...)
```

### `node_actions_detailed_async(self, node_id: Any, skip_count: Any, max_items: Any, order_by: Any, fields: Any)`

Node Actions operation (detailed, async).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `node_id`: typing.Any (required)
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `order_by`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = actions_ops.node_actions_detailed_async(node_id="abc123-def456", skip_count=..., max_items=..., order_by=..., fields=...)

# 2. Basic async
result = await actions_ops.node_actions_detailed_async_async(node_id="abc123-def456", skip_count=..., max_items=..., order_by=..., fields=...)

# 3. Detailed sync (with full HTTP response)
result = actions_ops.node_actions_detailed_async_detailed(node_id="abc123-def456", skip_count=..., max_items=..., order_by=..., fields=...)

# 4. Detailed async (with full HTTP response)
result = await actions_ops.node_actions_detailed_async_detailed_async(node_id="abc123-def456", skip_count=..., max_items=..., order_by=..., fields=...)
```

## Models

Operation-specific Pydantic models are available in:
```python
from python_alfresco_api.clients.core.actions.models import *
```

## Related Documentation

- [Core API Overview](../core_api.md)
- [V1.1 Architecture](../../clients_doc.md)
