# Search Sql API Models - V1.1 Hierarchical Architecture

Auto-generated from actual V1.1 models on 2025-07-15 00:36:44

## Overview

Pydantic v2 models for the Search Sql API following the V1.1 three-tier architecture:

- **Level 2**: API-level shared models (`python_alfresco_api.clients.search_sql.models`)
- **Level 3**: Operation-specific models (e.g., `python_alfresco_api.clients.search_sql.nodes.models`)

## Level 2: API-Level Models

**Module**: `python_alfresco_api.clients.search_sql.models`

```python
from python_alfresco_api.clients.search_sql.models import *
```

### Available Models

#### `BaseEntry`
Base entry model used across all Alfresco APIs.

**Fields:**
- `id`: typing.Optional[str] - Unique identifier

#### `BaseModel`
Base class for creating Pydantic models with validation and serialization capabilities.

This is the foundation class for all data models in the python-alfresco-api library, providing:
- Automatic validation of field types and values
- JSON serialization and deserialization
- Type hints and IDE support
- Immutable data structures by default

**Usage:**
```python
from python_alfresco_api.clients.search_sql.models import BaseModel

class MyModel(BaseModel):
    name: str
    value: int
```

#### `PagingInfo`
Pagination information used across all APIs.

**Fields:**
- `count`: typing.Optional[int] - Number of items in this page
- `has_more_items`: typing.Optional[bool] - Whether there are more items available
- `total_items`: typing.Optional[int] - Total number of items available
- `skip_count`: typing.Optional[int] - Number of items skipped
- `max_items`: typing.Optional[int] - Maximum number of items per page

#### `SearchSqlRequest`
Base request model for SearchSql operations.

**Fields:**
- `max_items`: <class 'int'> - Maximum number of results to return
- `skip_count`: <class 'int'> - Number of results to skip for pagination

#### `SearchSqlResponse`
Base response wrapper for SearchSql API operations.

**Fields:**
- `entries`: typing.List[python_alfresco_api.clients.models.BaseEntry] - SearchSql result entries
- `pagination`: typing.Optional[python_alfresco_api.clients.models.PagingInfo] - Pagination information

## Level 3: Operation-Specific Models

### Sql Models

**Module**: `python_alfresco_api.clients.search_sql.sql.models`

Could not load models: No module named 'python_alfresco_api.raw_clients.alfresco_search_sql_client.search_sql_client.models.sqlresultsetpaging'

## Usage Patterns

### Basic Model Usage

```python
from python_alfresco_api.clients.search_sql.models import *

# API-level models (shared across operations)
response = SomeResponse(...)
entry = SomeEntry(...)
```

### Operation-Specific Models

```python
from python_alfresco_api.clients.search_sql.nodes.models import (
    Node,
    NodeResponse,
    CreateNodeRequest
)

# Create request models
request = CreateNodeRequest(name="My File", node_type="cm:content")

# Work with response models  
response: NodeResponse = api_result
node: Node = response.entry
```

### Model Validation

All models use Pydantic v2 for validation:

```python
# Automatic validation
try:
    model = SomeModel(field1="value", field2=123)
except ValidationError as e:
    print(f"Validation failed: {e}")

# Manual validation
data = {"field1": "value", "field2": "invalid"}
try:
    model = SomeModel.model_validate(data)
except ValidationError as e:
    print(f"Validation failed: {e}")
```

## Related Documentation

- [Search Sql API Overview](search_sql_api.md)
- [V1.1 Architecture](../clients_doc.md)
