# Activities Operations - Core API

Auto-generated from V1.1 hierarchical code on 2025-07-15 00:36:43

## Overview

Activities operations for the Core API.

## Usage

```python
from python_alfresco_api import ClientFactory

# Create factory and client
factory = ClientFactory(base_url="http://localhost:8080")
core_client = factory.create_core_client()

# Access activities operations
activities_ops = core_client.activities

# Real method examples (sync):
result = activities_ops.get_httpx_client()
result = activities_ops.list_activities_for_person(person_id="abc123-def456", skip_count=..., max_items=..., who=..., site_id="abc123-def456", fields=...)
result = activities_ops.list_activities_for_person_async(person_id="abc123-def456", skip_count=..., max_items=..., who=..., site_id="abc123-def456", fields=...)

# Real method examples (async):
result = await activities_ops.get_httpx_client_async()
result = await activities_ops.list_activities_for_person_async(person_id="abc123-def456", skip_count=..., max_items=..., who=..., site_id="abc123-def456", fields=...)
result = await activities_ops.list_activities_for_person_async_async(person_id="abc123-def456", skip_count=..., max_items=..., who=..., site_id="abc123-def456", fields=...)
```

## Available Methods

This subsection provides 5 operations:

### `get_httpx_client(self)`

Get direct access to raw httpx client for advanced operations.

Perfect for MCP servers that need raw HTTP access.

**Usage Patterns:**
```python
# 1. Basic sync
result = activities_ops.get_httpx_client()

# 2. Basic async
result = await activities_ops.get_httpx_client_async()

# 3. Detailed sync (with full HTTP response)
result = activities_ops.get_httpx_client_detailed()

# 4. Detailed async (with full HTTP response)
result = await activities_ops.get_httpx_client_detailed_async()
```

### `list_activities_for_person(self, person_id: Any, skip_count: Any, max_items: Any, who: Any, site_id: Any, fields: Any) -> python_alfresco_api.clients.core.activities.models.ActivitiesResponse`

List Activities For Person operation.

Perfect for MCP servers and activities workflows.
Returns simplified response for common use cases.

**Parameters:**
- `person_id`: typing.Any (required)
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `who`: typing.Any (required)
- `site_id`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = activities_ops.list_activities_for_person(person_id="abc123-def456", skip_count=..., max_items=..., who=..., site_id="abc123-def456", fields=...)

# 2. Basic async
result = await activities_ops.list_activities_for_person_async(person_id="abc123-def456", skip_count=..., max_items=..., who=..., site_id="abc123-def456", fields=...)

# 3. Detailed sync (with full HTTP response)
result = activities_ops.list_activities_for_person_detailed(person_id="abc123-def456", skip_count=..., max_items=..., who=..., site_id="abc123-def456", fields=...)

# 4. Detailed async (with full HTTP response)
result = await activities_ops.list_activities_for_person_detailed_async(person_id="abc123-def456", skip_count=..., max_items=..., who=..., site_id="abc123-def456", fields=...)
```

### `list_activities_for_person_async(self, person_id: Any, skip_count: Any, max_items: Any, who: Any, site_id: Any, fields: Any) -> python_alfresco_api.clients.core.activities.models.ActivitiesResponse`

List Activities For Person operation (async).

Perfect for MCP servers and activities workflows.
Returns simplified response for common use cases.

**Parameters:**
- `person_id`: typing.Any (required)
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `who`: typing.Any (required)
- `site_id`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = activities_ops.list_activities_for_person_async(person_id="abc123-def456", skip_count=..., max_items=..., who=..., site_id="abc123-def456", fields=...)

# 2. Basic async
result = await activities_ops.list_activities_for_person_async_async(person_id="abc123-def456", skip_count=..., max_items=..., who=..., site_id="abc123-def456", fields=...)

# 3. Detailed sync (with full HTTP response)
result = activities_ops.list_activities_for_person_async_detailed(person_id="abc123-def456", skip_count=..., max_items=..., who=..., site_id="abc123-def456", fields=...)

# 4. Detailed async (with full HTTP response)
result = await activities_ops.list_activities_for_person_async_detailed_async(person_id="abc123-def456", skip_count=..., max_items=..., who=..., site_id="abc123-def456", fields=...)
```

### `list_activities_for_person_detailed(self, person_id: Any, skip_count: Any, max_items: Any, who: Any, site_id: Any, fields: Any)`

List Activities For Person operation (detailed).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `person_id`: typing.Any (required)
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `who`: typing.Any (required)
- `site_id`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = activities_ops.list_activities_for_person_detailed(person_id="abc123-def456", skip_count=..., max_items=..., who=..., site_id="abc123-def456", fields=...)

# 2. Basic async
result = await activities_ops.list_activities_for_person_detailed_async(person_id="abc123-def456", skip_count=..., max_items=..., who=..., site_id="abc123-def456", fields=...)

# 3. Detailed sync (with full HTTP response)
result = activities_ops.list_activities_for_person_detailed_detailed(person_id="abc123-def456", skip_count=..., max_items=..., who=..., site_id="abc123-def456", fields=...)

# 4. Detailed async (with full HTTP response)
result = await activities_ops.list_activities_for_person_detailed_detailed_async(person_id="abc123-def456", skip_count=..., max_items=..., who=..., site_id="abc123-def456", fields=...)
```

### `list_activities_for_person_detailed_async(self, person_id: Any, skip_count: Any, max_items: Any, who: Any, site_id: Any, fields: Any)`

List Activities For Person operation (detailed, async).

Perfect for MCP servers needing full HTTP response details.
Returns complete Response object with status_code, headers, content, parsed.

**Parameters:**
- `person_id`: typing.Any (required)
- `skip_count`: typing.Any (required)
- `max_items`: typing.Any (required)
- `who`: typing.Any (required)
- `site_id`: typing.Any (required)
- `fields`: typing.Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = activities_ops.list_activities_for_person_detailed_async(person_id="abc123-def456", skip_count=..., max_items=..., who=..., site_id="abc123-def456", fields=...)

# 2. Basic async
result = await activities_ops.list_activities_for_person_detailed_async_async(person_id="abc123-def456", skip_count=..., max_items=..., who=..., site_id="abc123-def456", fields=...)

# 3. Detailed sync (with full HTTP response)
result = activities_ops.list_activities_for_person_detailed_async_detailed(person_id="abc123-def456", skip_count=..., max_items=..., who=..., site_id="abc123-def456", fields=...)

# 4. Detailed async (with full HTTP response)
result = await activities_ops.list_activities_for_person_detailed_async_detailed_async(person_id="abc123-def456", skip_count=..., max_items=..., who=..., site_id="abc123-def456", fields=...)
```

## Models

Operation-specific Pydantic models are available in:
```python
from python_alfresco_api.clients.core.activities.models import *
```

## Related Documentation

- [Core API Overview](../core_api.md)
- [V1.1 Architecture](../../clients_doc.md)
