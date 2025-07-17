# Core API Models - V1.1 Hierarchical Architecture

Auto-generated from actual V1.1 models on 2025-07-15 00:36:43

## Overview

Pydantic v2 models for the Core API following the V1.1 three-tier architecture:

- **Level 2**: API-level shared models (`python_alfresco_api.clients.core.models`)
- **Level 3**: Operation-specific models (e.g., `python_alfresco_api.clients.core.nodes.models`)

## Level 2: API-Level Models

**Module**: `python_alfresco_api.clients.core.models`

```python
from python_alfresco_api.clients.core.models import *
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
from python_alfresco_api.clients.core.models import BaseModel

class MyModel(BaseModel):
    name: str
    value: int
```

#### `ContentInfo`
Basic content information shared across APIs.

**Fields:**
- `mime_type`: typing.Optional[str] - MIME type of the content
- `mime_type_name`: typing.Optional[str] - Human-readable MIME type name
- `size_in_bytes`: typing.Optional[int] - Size of content in bytes
- `encoding`: typing.Optional[str] - Content encoding

#### `CoreAspectInfo`
Aspect information for Core API objects.

**Fields:**
- `aspect_name`: <class 'str'> - Aspect name (e.g., cm:titled)
- `title`: typing.Optional[str] - Aspect title
- `description`: typing.Optional[str] - Aspect description

#### `CoreEntryList`
List response wrapper for Core API operations.

**Fields:**
- `entries`: typing.List[python_alfresco_api.clients.models.BaseEntry] - List of entries
- `pagination`: typing.Optional[python_alfresco_api.clients.models.PagingInfo] - Pagination information

#### `CorePathElement`
Path element for Core API path structures.

**Fields:**
- `id`: <class 'str'> - Node ID
- `name`: <class 'str'> - Node name
- `node_type`: typing.Optional[str] - Node type
- `aspect_names`: typing.Optional[typing.List[str]] - Aspect names

#### `CorePathInfo`
Path information for Core API objects.

**Fields:**
- `elements`: typing.List[python_alfresco_api.clients.core.models.CorePathElement] - Path elements
- `name`: typing.Optional[str] - Display name
- `is_complete`: typing.Optional[bool] - Whether path is complete

#### `CorePermissionInfo`
Permission information for Core API objects.

**Fields:**
- `authority_id`: <class 'str'> - Authority (user/group) identifier
- `authority_type`: <class 'str'> - Type of authority (USER, GROUP)
- `permission`: <enum 'Permission'> - Permission level
- `access_status`: <class 'str'> - Access status (ALLOWED, DENIED)

#### `CoreResponse`
Base response wrapper for Core API operations.

**Fields:**
- `entry`: typing.Optional[python_alfresco_api.clients.models.BaseEntry] - Single entry response

#### `PagingInfo`
Pagination information used across all APIs.

**Fields:**
- `count`: typing.Optional[int] - Number of items in this page
- `has_more_items`: typing.Optional[bool] - Whether there are more items available
- `total_items`: typing.Optional[int] - Total number of items available
- `skip_count`: typing.Optional[int] - Number of items skipped
- `max_items`: typing.Optional[int] - Maximum number of items per page

#### `UserInfo`
Basic user information shared across APIs.

**Fields:**
- `id`: <class 'str'> - User identifier
- `display_name`: typing.Optional[str] - User display name
- `email`: typing.Optional[str] - User email address

## Level 3: Operation-Specific Models

### Actions Models

**Module**: `python_alfresco_api.clients.core.actions.models`

```python
from python_alfresco_api.clients.core.actions.models import (
    ActionsListResponse,
    ActionsResponse,
    BaseEntry,
    BaseModel,
    ContentInfo,
    CoreResponse,
    CreateActionsRequest,
    UpdateActionsRequest,
    UserInfo
)
```

**Available Models:**
- **`ActionsListResponse`** - Response wrapper for actions list operations.
- **`ActionsResponse`** - Response wrapper for actions operations.
- **`BaseEntry`** - Base entry model used across all Alfresco APIs.
- **`BaseModel`** - Base class for creating Pydantic models with validation and serialization capabilities.

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.
