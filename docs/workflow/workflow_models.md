# Workflow API Models - V1.1 Hierarchical Architecture

Auto-generated from actual V1.1 models on 2025-07-15 00:36:43

## Overview

Pydantic v2 models for the Workflow API following the V1.1 three-tier architecture:

- **Level 2**: API-level shared models (`python_alfresco_api.clients.workflow.models`)
- **Level 3**: Operation-specific models (e.g., `python_alfresco_api.clients.workflow.nodes.models`)

## Level 2: API-Level Models

**Module**: `python_alfresco_api.clients.workflow.models`

```python
from python_alfresco_api.clients.workflow.models import *
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
from python_alfresco_api.clients.workflow.models import BaseModel

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

#### `WorkflowRequest`
Base request model for Workflow operations.

**Fields:**
- `max_items`: <class 'int'> - Maximum number of results to return
- `skip_count`: <class 'int'> - Number of results to skip for pagination

#### `WorkflowResponse`
Base response wrapper for Workflow API operations.

**Fields:**
- `entries`: typing.List[python_alfresco_api.clients.models.BaseEntry] - Workflow result entries
- `pagination`: typing.Optional[python_alfresco_api.clients.models.PagingInfo] - Pagination information

## Level 3: Operation-Specific Models

### Deployments Models

**Module**: `python_alfresco_api.clients.workflow.deployments.models`

```python
from python_alfresco_api.clients.workflow.deployments.models import (
    BaseEntry,
    BaseModel,
    ContentInfo,
    CreateDeploymentsRequest,
    DeploymentsListResponse,
    DeploymentsResponse,
    UpdateDeploymentsRequest,
    UserInfo,
    WorkflowResponse
)
```

**Available Models:**
- **`BaseEntry`** - Base entry model used across all Alfresco APIs.
- **`BaseModel`** - !!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
