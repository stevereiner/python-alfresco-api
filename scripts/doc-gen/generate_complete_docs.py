#!/usr/bin/env python3
"""
Generate Complete Documentation Structure

This script generates hierarchical documentation for all Core API operation groups
following the established pattern:
- Separate model and API documentation files
- Mirrors code directory structure
- Consistent formatting and navigation

Usage:
    python scripts/generate_complete_docs.py
"""

import os
from pathlib import Path
from typing import List, Dict, Any


def get_operation_groups() -> List[Dict[str, Any]]:
    """Get all Core API operation groups with their metadata."""
    return [
        {
            "name": "actions",
            "title": "Actions",
            "description": "Action execution and management operations",
            "key_features": [
                "Execute custom actions",
                "Action parameter validation",
                "Async action execution",
                "Action result tracking"
            ]
        },
        {
            "name": "activities",
            "title": "Activities",
            "description": "Activity feeds and user activity tracking",
            "key_features": [
                "Activity feed retrieval",
                "User activity tracking",
                "Activity filtering",
                "Activity notifications"
            ]
        },
        {
            "name": "audit",
            "title": "Audit",
            "description": "Audit trail and compliance operations",
            "key_features": [
                "Audit log retrieval",
                "Compliance reporting",
                "Audit trail filtering",
                "Audit event tracking"
            ]
        },
        {
            "name": "comments",
            "title": "Comments",
            "description": "Content commenting and discussion operations",
            "key_features": [
                "Add/edit/delete comments",
                "Comment threading",
                "Comment moderation",
                "Comment notifications"
            ]
        },
        {
            "name": "content",
            "title": "Content",
            "description": "Content upload, download, and streaming operations",
            "key_features": [
                "Content upload/download",
                "Content streaming",
                "Content versioning",
                "Content transformation"
            ]
        },
        {
            "name": "downloads",
            "title": "Downloads",
            "description": "Bulk download and archive operations",
            "key_features": [
                "Bulk download creation",
                "Download status tracking",
                "Archive management",
                "Download expiration"
            ]
        },
        {
            "name": "favorites",
            "title": "Favorites",
            "description": "User favorites and bookmark operations",
            "key_features": [
                "Add/remove favorites",
                "Favorites management",
                "Bookmark organization",
                "Favorites sync"
            ]
        },
        {
            "name": "folders",
            "title": "Folders",
            "description": "Folder-specific operations and hierarchy management",
            "key_features": [
                "Folder creation",
                "Folder path management",
                "Folder contents filtering",
                "Folder hierarchy operations"
            ]
        },
        {
            "name": "groups",
            "title": "Groups",
            "description": "Group management and membership operations",
            "key_features": [
                "Group creation/management",
                "Group membership",
                "Group permissions",
                "Group hierarchy"
            ]
        },
        {
            "name": "networks",
            "title": "Networks",
            "description": "Network and tenant management operations",
            "key_features": [
                "Network information",
                "Tenant management",
                "Network policies",
                "Network monitoring"
            ]
        },
        {
            "name": "nodes",
            "title": "Nodes",
            "description": "Complete file and folder management with CRUD operations",
            "key_features": [
                "File and folder CRUD",
                "Metadata management",
                "Copy/move operations",
                "Node relationships"
            ]
        },
        {
            "name": "people",
            "title": "People",
            "description": "User management and profile operations",
            "key_features": [
                "User profile management",
                "User preferences",
                "User avatar management",
                "User activity tracking"
            ]
        },
        {
            "name": "preferences",
            "title": "Preferences",
            "description": "User preferences and settings management",
            "key_features": [
                "User preferences",
                "Application settings",
                "Preference synchronization",
                "Default preferences"
            ]
        },
        {
            "name": "probes",
            "title": "Probes",
            "description": "Health check and monitoring operations",
            "key_features": [
                "Health checks",
                "System monitoring",
                "Performance metrics",
                "System diagnostics"
            ]
        },
        {
            "name": "queries",
            "title": "Queries",
            "description": "Saved queries and search operations",
            "key_features": [
                "Saved query management",
                "Query execution",
                "Query results",
                "Query optimization"
            ]
        },
        {
            "name": "ratings",
            "title": "Ratings",
            "description": "Content rating and review operations",
            "key_features": [
                "Content rating",
                "Rating aggregation",
                "Review management",
                "Rating statistics"
            ]
        },
        {
            "name": "renditions",
            "title": "Renditions",
            "description": "Content rendition and transformation operations",
            "key_features": [
                "Content renditions",
                "Transformation jobs",
                "Rendition management",
                "Format conversion"
            ]
        },
        {
            "name": "shared_links",
            "title": "Shared Links",
            "description": "Shared link creation and management operations",
            "key_features": [
                "Shared link creation",
                "Link expiration",
                "Link permissions",
                "Link analytics"
            ]
        },
        {
            "name": "sites",
            "title": "Sites",
            "description": "Site management and collaboration operations",
            "key_features": [
                "Site creation/management",
                "Site membership",
                "Site permissions",
                "Site collaboration"
            ]
        },
        {
            "name": "tags",
            "title": "Tags",
            "description": "Content tagging and categorization operations",
            "key_features": [
                "Tag management",
                "Content tagging",
                "Tag hierarchies",
                "Tag-based search"
            ]
        },
        {
            "name": "trashcan",
            "title": "Trashcan",
            "description": "Deleted content management and restoration operations",
            "key_features": [
                "Deleted content retrieval",
                "Content restoration",
                "Permanent deletion",
                "Trash management"
            ]
        },
        {
            "name": "versions",
            "title": "Versions",
            "description": "Content versioning and history operations",
            "key_features": [
                "Version management",
                "Version history",
                "Version comparison",
                "Version restoration"
            ]
        }
    ]


def generate_operation_models_doc(operation: Dict[str, Any]) -> str:
    """Generate models documentation for an operation group."""
    name = operation["name"]
    title = operation["title"]
    description = operation["description"]
    
    return f"""# {title} Models Documentation

**Location:** `python_alfresco_api.clients.core.{name}.models`

Level 3 models specific to {name} operations - {description.lower()}.

## 🏗️ Architecture

```
python_alfresco_api.clients.core.{name}/
├── models.py              # This file - {title} operation-specific models
└── {name}.py              # {title}Operations class (see {name}-api.md)
```

## 📚 Available Models

### Import Statement

```python
from python_alfresco_api.clients.core.{name}.models import (
    {title}Response,           # Single {name} response wrapper
    {title}ListResponse,       # {title} list response wrapper
    Create{title}Request,      # {title} creation parameters
    Update{title}Request,      # {title} update parameters
    # ... other {name}-specific models
)
```

## 🔧 Core Models

### 1. {title}Response

Response wrapper for single {name} operations.

```python
class {title}Response(BaseModel):
    \"\"\"Response wrapper for single {name} operations.\"\"\"
    
    entry: {title}Entry = Field(..., description="{title} data")
    
    # Additional {name}-specific fields
    metadata: Optional[Dict[str, Any]] = Field(
        description="Additional {name} metadata",
        default=None
    )
```

**Example Usage:**
```python
response = core_client.{name}.get("{name}-id")
{name}_data = response.entry
print(f"{title} ID: {{response.entry.id}}")
```

### 2. {title}ListResponse

Response wrapper for {name} list operations.

```python
class {title}ListResponse(BaseModel):
    \"\"\"Response wrapper for {name} list operations.\"\"\"
    
    list: Dict[str, Any] = Field(..., description="List data with pagination")
```

**Example Usage:**
```python
{name}_list = core_client.{name}.list()
entries = {name}_list.list['entries']
pagination = {name}_list.list.get('pagination', {{}})

for entry_wrapper in entries:
    {name}_item = entry_wrapper['entry']
    print(f"{title}: {{{name}_item['name']}}")
```

## 📝 Request Models

### 3. Create{title}Request

Parameters for creating new {name} items.

```python
class Create{title}Request(BaseModel):
    \"\"\"Request model for creating new {name} items with validation.\"\"\"
    
    # Required fields
    name: str = Field(..., description="{title} name")
    
    # Optional fields with defaults
    description: Optional[str] = Field(
        description="{title} description",
        default=None
    )
    
    properties: Optional[Dict[str, Any]] = Field(
        description="Custom properties and metadata",
        default=None
    )
```

**Example Usage:**
```python
from python_alfresco_api.clients.core.{name}.models import Create{title}Request

# Create {name} item
request = Create{title}Request(
    name="My {title}",
    description="Description for {name}",
    properties={{
        "custom:category": "example",
        "custom:priority": "high"
    }}
)

{name}_item = core_client.{name}.create(request)
```

### 4. Update{title}Request

Parameters for updating existing {name} items.

```python
class Update{title}Request(BaseModel):
    \"\"\"Request model for updating existing {name} items.\"\"\"
    
    # All fields optional - update only what's provided
    name: Optional[str] = Field(description="New {name} name", default=None)
    description: Optional[str] = Field(description="New {name} description", default=None)
    properties: Optional[Dict[str, Any]] = Field(description="Properties to update", default=None)
```

**Example Usage:**
```python
# Update {name} item
update_request = Update{title}Request(
    name="Updated {title} Name",
    properties={{
        "custom:status": "updated",
        "custom:modified": "2024-01-15"
    }}
)

updated_{name} = core_client.{name}.update("{name}-id", update_request)
```

## 🔗 Model Dependencies

### Level 1 Dependencies (Global Models)
```python
from python_alfresco_api.models import (
    BaseEntry,      # Base class for {title}Entry
    PagingInfo,     # Pagination information
    UserInfo        # User information
)
```

### Level 2 Dependencies (Core API Models)
```python
from python_alfresco_api.clients.core.models import (
    Permission,             # Permission levels
    IncludeOption,          # Include options
    CoreResponse            # Core response wrapper
)
```

## 💡 Usage Examples

### Complete {title} Management Workflow
```python
from python_alfresco_api.clients.core.{name}.models import Create{title}Request, Update{title}Request

# 1. Create {name} item
create_request = Create{title}Request(
    name="Example {title}",
    description="Example {name} for demonstration",
    properties={{
        "custom:category": "example",
        "custom:created_by": "demo_user"
    }}
)
{name}_item = core_client.{name}.create(create_request)

# 2. Update {name} item
update_request = Update{title}Request(
    description="Updated description",
    properties={{
        "custom:status": "active",
        "custom:last_modified": "2024-01-15"
    }}
)
updated_{name} = core_client.{name}.update({name}_item.entry.id, update_request)

# 3. Get {name} item details
{name}_details = core_client.{name}.get({name}_item.entry.id, include=["properties"])
```

## 🔗 Related Documentation

- **[{title} API]({name}-api.md)** - {title} operations and methods
- **[Core API Models](../core-doc.md#level-2-core-api-models)** - Level 2 shared models
- **[Global Models](../../clients_doc.md#level-1-global-models)** - Level 1 shared models
- **[Core API Overview](../core-doc.md)** - Level 2 Core API documentation
"""


def generate_operation_api_doc(operation: Dict[str, Any]) -> str:
    """Generate API documentation for an operation group."""
    name = operation["name"]
    title = operation["title"]
    description = operation["description"]
    features = operation["key_features"]
    
    features_text = "\\n".join([f"- {feature}" for feature in features])
    
    return f"""# {title} API Documentation

**Location:** `python_alfresco_api.clients.core.{name}`

{description} with comprehensive operations for {name} management.

## 🏗️ Architecture

```
python_alfresco_api.clients.core.{name}/
├── models.py              # {title} operation-specific models (see {name}-models.md)
└── {name}.py              # {title}Operations class - This file
```

## 🚀 Quick Start

```python
from python_alfresco_api import ClientFactory
from python_alfresco_api.clients.core.{name}.models import Create{title}Request, Update{title}Request

# Setup
factory = ClientFactory(base_url="http://localhost:8080")
core_client = factory.create_core_client()

# Access {name} operations (lazy loaded)
{name}_ops = core_client.{name}

# Basic operations
{name}_item = {name}_ops.get("{name}-id")
new_{name} = {name}_ops.create(request=...)
updated_{name} = {name}_ops.update("{name}-id", request=...)
{name}_ops.delete("{name}-id")
```

## 📚 Key Features

{features_text}

## 📚 Available Operations

### 1. Get {title} Information

Retrieve comprehensive {name} information by ID.

#### `get({name}_id, include=None, fields=None) -> {title}Response`

**Synchronous Method:**
```python
{name}_item = core_client.{name}.get(
    {name}_id="{name}-123",
    include=["properties", "permissions"],
    fields=["id", "name", "description", "properties"]
)

print(f"{title}: {{{name}_item.entry.name}}")
print(f"Description: {{{name}_item.entry.description}}")
```

#### `get_async({name}_id, include=None, fields=None) -> {title}Response`

**Asynchronous Method:**
```python
{name}_item = await core_client.{name}.get_async(
    {name}_id="{name}-123",
    include=["properties"]
)
```

**Parameters:**
- `{name}_id` (str): {title} identifier
- `include` (Optional[List]): Additional data to include
  - `"properties"` - Custom properties and metadata
  - `"permissions"` - Permission information
- `fields` (Optional[List]): Specific fields to return (limits response size)

**Returns:** `{title}Response` with comprehensive {name} information

**Raises:**
- `ValueError`: {title} not found
- `PermissionError`: Access denied
- `ValidationError`: Invalid parameters

### 2. Create {title}

Create new {name} items.

#### `create(request) -> {title}Response`

**Synchronous Method:**
```python
from python_alfresco_api.clients.core.{name}.models import Create{title}Request

# Create {name} item
{name}_item = core_client.{name}.create(
    request=Create{title}Request(
        name="New {title}",
        description="Description for {name}",
        properties={{
            "custom:category": "example",
            "custom:priority": "high"
        }}
    )
)
```

#### `create_async(request) -> {title}Response`

**Asynchronous Method:**
```python
{name}_item = await core_client.{name}.create_async(
    request=Create{title}Request(
        name="Async {title}",
        description="Created asynchronously"
    )
)
```

**Parameters:**
- `request` (Create{title}Request): {title} creation parameters

**Returns:** `{title}Response` with created {name} information

**Raises:**
- `ValueError`: Creation failed
- `PermissionError`: No permission to create {name}
- `ValidationError`: Invalid request parameters

### 3. Update {title}

Update {name} properties and metadata.

#### `update({name}_id, request, include=None) -> {title}Response`

**Synchronous Method:**
```python
from python_alfresco_api.clients.core.{name}.models import Update{title}Request

updated_{name} = core_client.{name}.update(
    {name}_id="{name}-123",
    request=Update{title}Request(
        name="Updated {title} Name",
        properties={{
            "custom:status": "updated",
            "custom:modified": "2024-01-15"
        }}
    ),
    include=["properties"]
)
```

#### `update_async({name}_id, request, include=None) -> {title}Response`

**Asynchronous Method:**
```python
updated_{name} = await core_client.{name}.update_async(
    {name}_id="{name}-123",
    request=Update{title}Request(name="New Name"),
    include=["properties"]
)
```

**Parameters:**
- `{name}_id` (str): {title} identifier to update
- `request` (Update{title}Request): Update parameters
- `include` (Optional[List]): Additional data to include in response

**Returns:** `{title}Response` with updated {name} information

### 4. Delete {title}

Delete {name} items.

#### `delete({name}_id) -> None`

**Synchronous Method:**
```python
# Delete {name} item
core_client.{name}.delete("{name}-123")
```

#### `delete_async({name}_id) -> None`

**Asynchronous Method:**
```python
# Delete {name} item
await core_client.{name}.delete_async("{name}-123")
```

**Parameters:**
- `{name}_id` (str): {title} identifier to delete

**Returns:** None

### 5. List {title}

List {name} items with pagination and filtering.

#### `list(skip_count=0, max_items=100, order_by=None, where=None, include=None, fields=None) -> {title}ListResponse`

**Synchronous Method:**
```python
{name}_list = core_client.{name}.list(
    skip_count=0,
    max_items=25,
    order_by=["name ASC", "createdAt DESC"],
    where="(status='active')",
    include=["properties"],
    fields=["id", "name", "description", "createdAt"]
)

# Access results
for item in {name}_list.list['entries']:
    print(f"Name: {{item['entry']['name']}}")
```

#### `list_async(skip_count=0, max_items=100, order_by=None, where=None, include=None, fields=None) -> {title}ListResponse`

**Asynchronous Method:**
```python
{name}_list = await core_client.{name}.list_async(
    max_items=50,
    order_by=["createdAt DESC"]
)
```

**Parameters:**
- `skip_count` (int): Number of items to skip (for pagination)
- `max_items` (int): Maximum items to return (1-1000)
- `order_by` (Optional[List[str]]): Sort order
- `where` (Optional[str]): Filter criteria
- `include` (Optional[List]): Additional data to include
- `fields` (Optional[List]): Specific fields to return

**Returns:** `{title}ListResponse` with {name} list and pagination info

## 🔄 Sync vs Async APIs

All {name} operations provide both synchronous and asynchronous variants:

**Synchronous (Perfect for scripts, MCP servers):**
```python
{name}_item = core_client.{name}.get("{name}-123")
new_{name} = core_client.{name}.create(request=...)
updated_{name} = core_client.{name}.update("{name}-123", request=...)
```

**Asynchronous (Perfect for web apps, high performance):**
```python
{name}_item = await core_client.{name}.get_async("{name}-123")
new_{name} = await core_client.{name}.create_async(request=...)
updated_{name} = await core_client.{name}.update_async("{name}-123", request=...)
```

## 🛠️ Raw Client Access

Access the underlying raw client for advanced operations:

```python
# Get raw client for direct HTTP access
raw_client = core_client._get_raw_client()

# Get httpx client
httpx_client = raw_client.get_httpx_client()

# Direct HTTP calls
response = httpx_client.get("/{name}/{{id}}")
response = httpx_client.post("/{name}", json={{"name": "example"}})
```

## 📋 Error Handling

```python
from pydantic import ValidationError

def safe_{name}_operation({name}_id: str):
    \"\"\"Safely perform {name} operations with comprehensive error handling.\"\"\"
    try:
        return core_client.{name}.get({name}_id, include=["properties"])
    except ValueError as e:
        print(f"{title} {{{name}_id}} not found: {{e}}")
        return None
    except PermissionError as e:
        print(f"Access denied to {name} {{{name}_id}}: {{e}}")
        return None
    except ValidationError as e:
        print(f"Invalid request parameters: {{e}}")
        return None
    except Exception as e:
        print(f"Unexpected error: {{e}}")
        return None
```

## 💡 Best Practices

### 1. Choose Appropriate API Style
```python
# For scripts, MCP servers, CLI tools - use sync
{name}_item = core_client.{name}.get("{name}-123")

# For web apps, high-performance systems - use async
{name}_item = await core_client.{name}.get_async("{name}-123")
```

### 2. Optimize Response Size
```python
# Minimize response size with fields
{name}_item = core_client.{name}.get(
    "{name}-123",
    fields=["id", "name", "description"]  # Only essential fields
)

# Include additional data only when needed
{name}_item = core_client.{name}.get(
    "{name}-123",
    include=["properties", "permissions"]
)
```

### 3. Batch Operations
```python
# Process multiple {name} items efficiently
{name}_ids = ["{name}1", "{name}2", "{name}3"]

# Synchronous batch
for {name}_id in {name}_ids:
    try:
        {name}_item = core_client.{name}.get({name}_id)
        process_{name}({name}_item)
    except ValueError:
        print(f"Skipped missing {name}: {{{name}_id}}")

# Asynchronous batch
import asyncio

async def process_{name}_items_async({name}_ids):
    tasks = [
        core_client.{name}.get_async({name}_id)
        for {name}_id in {name}_ids
    ]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    for {name}_id, result in zip({name}_ids, results):
        if isinstance(result, Exception):
            print(f"Error processing {{{name}_id}}: {{result}}")
        else:
            process_{name}(result)
```

## 🔗 Related Documentation

- **[{title} Models]({name}-models.md)** - {title} operation-specific models
- **[Core API Overview](../core-doc.md)** - Level 2 Core API documentation
- **[Global Models](../../clients_doc.md#level-1-global-models)** - Level 1 shared models
- **[Authentication Guide](../../AUTHENTICATION_GUIDE.md)** - Setup and authentication
"""


def update_core_doc_with_all_operations(operations: List[Dict[str, Any]]) -> str:
    """Update the core-doc.md with all operation groups."""
    
    # Generate operation group links
    operation_links = []
    for op in operations:
        name = op["name"]
        title = op["title"]
        description = op["description"]
        features = op["key_features"][:2]  # First 2 features
        
        features_text = "\\n".join([f"- {feature}" for feature in features])
        
        operation_links.append(f"""### {title} Operations
**Location:** `python_alfresco_api.clients.core.{name}`

{description}.

- **[{title} Models]({name}/{name}-models.md)** - {title}-specific models and data structures
- **[{title} API]({name}/{name}-api.md)** - {title} operations and methods

**Key Features:**
{features_text}""")
    
    return "\\n\\n".join(operation_links)


def main():
    """Generate complete documentation structure."""
    print("🚀 Generating complete documentation structure...")
    
    # Create docs directories
    docs_dir = Path("docs")
    core_dir = docs_dir / "core"
    
    # Get all operation groups
    operations = get_operation_groups()
    
    # Generate documentation for each operation group
    for operation in operations:
        name = operation["name"]
        print(f"📝 Generating docs for {name}...")
        
        # Create operation directory
        op_dir = core_dir / name
        op_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate models documentation
        models_doc = generate_operation_models_doc(operation)
        (op_dir / f"{name}-models.md").write_text(models_doc, encoding='utf-8')
        
        # Generate API documentation
        api_doc = generate_operation_api_doc(operation)
        (op_dir / f"{name}-api.md").write_text(api_doc, encoding='utf-8')
        
        print(f"✅ Generated {name}-models.md and {name}-api.md")
    
    # Update core-doc.md with all operations
    print("📝 Updating core-doc.md with all operations...")
    
    # Read current core-doc.md
    core_doc_path = core_dir / "core-doc.md"
    if core_doc_path.exists():
        content = core_doc_path.read_text(encoding='utf-8')
        
        # Find the operation groups section and replace it
        operation_links = update_core_doc_with_all_operations(operations)
        
        # Replace the nodes operations section with all operations
        start_marker = "### Nodes Operations"
        end_marker = "## 🔄 Sync vs Async APIs"
        
        if start_marker in content and end_marker in content:
            start_idx = content.find(start_marker)
            end_idx = content.find(end_marker)
            
            new_content = (
                content[:start_idx] + 
                operation_links + 
                "\\n\\n" + 
                content[end_idx:]
            )
            
            core_doc_path.write_text(new_content, encoding='utf-8')
            print("✅ Updated core-doc.md with all operations")
        else:
            print("⚠️  Could not find markers to update core-doc.md")
    
    print("🎉 Documentation generation complete!")
    print(f"📊 Generated documentation for {len(operations)} operation groups")
    print("📁 Structure:")
    print("   docs/core/")
    for op in operations:
        print(f"   ├── {op['name']}/")
        print(f"   │   ├── {op['name']}-models.md")
        print(f"   │   └── {op['name']}-api.md")


if __name__ == "__main__":
    main() 