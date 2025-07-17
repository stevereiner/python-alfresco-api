# Folders Operations - Core API

Auto-generated from V1.1 hierarchical code on 2025-07-10 05:07:56

## Overview

Folders operations for the Core API.

## Usage

```python
from python_alfresco_api import ClientFactory

# Create factory and client
factory = ClientFactory(base_url="http://localhost:8080")
core_client = factory.create_core_client()

# Access folders operations
folders_ops = core_client.folders

# Real method examples (sync):
result = folders_ops.create(name="My Document", parent_id="abc123-def456", auto_rename="My Document")
result = folders_ops.create_async(name="My Document", parent_id="abc123-def456", auto_rename="My Document")
result = folders_ops.create_path(path="/path/to/file", parent_id="abc123-def456")

# Real method examples (async):
result = await folders_ops.create_async(name="My Document", parent_id="abc123-def456", auto_rename="My Document")
result = await folders_ops.create_async_async(name="My Document", parent_id="abc123-def456", auto_rename="My Document")
result = await folders_ops.create_path_async(path="/path/to/file", parent_id="abc123-def456")
```

## Available Methods

This subsection provides 7 operations:

### `create(self, name: str, parent_id: str = '-my-', properties: Optional[dict] = None, auto_rename: bool = True) -> python_alfresco_api.clients.core.folders.models.FolderResponse`

Create a new folder (synchronous).

Perfect for MCP servers, content organization, and workflows.
Specialized method for creating folders with folder-specific validation.

Args:
    name: Folder name
    parent_id: Parent folder ID (default: "-my-" for user's home)
    properties: Custom properties to set on the folder
    auto_rename: Automatically rename if name conflicts exist
    
Returns:
    FolderResponse: Response with created folder details
    
Examples:
    >>> # Create simple folder
    >>> folder = client.create("My Documents")
    >>> print(f"Created: {folder.entry.name}")
    
    >>> # Create folder with properties
    >>> folder = client.create(
    ...     "Project Files",
    ...     parent_id="workspace-123",
    ...     properties={"cm:title": "Project Documentation"}
    ... )
    
Raises:
    ValueError: If invalid folder name or parameters
    PermissionError: If insufficient permissions

**Parameters:**
- `name`: <class 'str'> (required)
- `parent_id`: <class 'str'> (default: -my-)
- `properties`: typing.Optional[dict] (default: None)
- `auto_rename`: <class 'bool'> (default: True)

**Usage Patterns:**
```python
# 1. Basic sync
result = folders_ops.create(name="My Document", parent_id="abc123-def456", auto_rename="My Document")

# 2. Basic async
result = await folders_ops.create_async(name="My Document", parent_id="abc123-def456", auto_rename="My Document")

# 3. Detailed sync (with full HTTP response)
result = folders_ops.create_detailed(name="My Document", parent_id="abc123-def456", auto_rename="My Document")

# 4. Detailed async (with full HTTP response)
result = await folders_ops.create_detailed_async(name="My Document", parent_id="abc123-def456", auto_rename="My Document")
```

### `create_async(self, name: str, parent_id: str = '-my-', properties: Optional[dict] = None, auto_rename: bool = True) -> python_alfresco_api.clients.core.folders.models.FolderResponse`

Async version of create.

**Parameters:**
- `name`: <class 'str'> (required)
- `parent_id`: <class 'str'> (default: -my-)
- `properties`: typing.Optional[dict] (default: None)
- `auto_rename`: <class 'bool'> (default: True)

**Usage Patterns:**
```python
# 1. Basic sync
result = folders_ops.create_async(name="My Document", parent_id="abc123-def456", auto_rename="My Document")

# 2. Basic async
result = await folders_ops.create_async_async(name="My Document", parent_id="abc123-def456", auto_rename="My Document")

# 3. Detailed sync (with full HTTP response)
result = folders_ops.create_async_detailed(name="My Document", parent_id="abc123-def456", auto_rename="My Document")

# 4. Detailed async (with full HTTP response)
result = await folders_ops.create_async_detailed_async(name="My Document", parent_id="abc123-def456", auto_rename="My Document")
```

### `create_path(self, path: str, parent_id: str = '-my-', properties: Optional[dict] = None) -> List[python_alfresco_api.clients.core.folders.models.FolderResponse]`

Create folder path (including intermediate folders) (synchronous).

Perfect for MCP servers that need to ensure folder structure exists.
Creates all intermediate folders if they don't exist.

Args:
    path: Folder path (e.g., "Documents/Projects/2024")
    parent_id: Parent folder ID where path starts
    properties: Properties to apply to created folders
    
Returns:
    List[FolderResponse]: Created folders (only new ones)
    
Examples:
    >>> # Create nested folder structure
    >>> folders = client.create_path("Documents/Projects/2024")
    >>> print(f"Created {len(folders)} folders")
    
    >>> # Create path with properties
    >>> folders = client.create_path(
    ...     "Teams/Engineering/Backend",
    ...     properties={"cm:description": "Auto-created by MCP"}
    ... )

**Parameters:**
- `path`: <class 'str'> (required)
- `parent_id`: <class 'str'> (default: -my-)
- `properties`: typing.Optional[dict] (default: None)

**Usage Patterns:**
```python
# 1. Basic sync
result = folders_ops.create_path(path="/path/to/file", parent_id="abc123-def456")

# 2. Basic async
result = await folders_ops.create_path_async(path="/path/to/file", parent_id="abc123-def456")

# 3. Detailed sync (with full HTTP response)
result = folders_ops.create_path_detailed(path="/path/to/file", parent_id="abc123-def456")

# 4. Detailed async (with full HTTP response)
result = await folders_ops.create_path_detailed_async(path="/path/to/file", parent_id="abc123-def456")
```

### `create_path_async(self, path: str, parent_id: str = '-my-', properties: Optional[dict] = None) -> List[python_alfresco_api.clients.core.folders.models.FolderResponse]`

Async version of create_path.

**Parameters:**
- `path`: <class 'str'> (required)
- `parent_id`: <class 'str'> (default: -my-)
- `properties`: typing.Optional[dict] (default: None)

**Usage Patterns:**
```python
# 1. Basic sync
result = folders_ops.create_path_async(path="/path/to/file", parent_id="abc123-def456")

# 2. Basic async
result = await folders_ops.create_path_async_async(path="/path/to/file", parent_id="abc123-def456")

# 3. Detailed sync (with full HTTP response)
result = folders_ops.create_path_async_detailed(path="/path/to/file", parent_id="abc123-def456")

# 4. Detailed async (with full HTTP response)
result = await folders_ops.create_path_async_detailed_async(path="/path/to/file", parent_id="abc123-def456")
```

### `get_contents(self, folder_id: str, skip_count: int = 0, max_items: int = 100, order_by: Optional[List[str]] = None, folders_only: bool = False, files_only: bool = False) -> python_alfresco_api.clients.core.nodes.models.NodeListResponse`

Get contents of a folder with folder-specific filtering (synchronous).

Perfect for MCP servers and folder browsing workflows.
Provides folder-specific filtering options.

Args:
    folder_id: Folder identifier
    skip_count: Number of items to skip (pagination)
    max_items: Maximum items to return per page
    order_by: Sort criteria (e.g., ["name ASC", "createdAt DESC"])
    folders_only: Return only subfolders
    files_only: Return only files
    
Returns:
    NodeListResponse: Folder contents with pagination
    
Examples:
    >>> # Get all contents
    >>> contents = client.get_contents("folder-123")
    
    >>> # Get only subfolders
    >>> folders = client.get_contents("folder-123", folders_only=True)
    
    >>> # Get only files, sorted by name
    >>> files = client.get_contents(
    ...     "folder-123", 
    ...     files_only=True,
    ...     order_by=["name ASC"]
    ... )

**Parameters:**
- `folder_id`: <class 'str'> (required)
- `skip_count`: <class 'int'> (default: 0)
- `max_items`: <class 'int'> (default: 100)
- `order_by`: typing.Optional[typing.List[str]] (default: None)
- `folders_only`: <class 'bool'> (default: False)
- `files_only`: <class 'bool'> (default: False)

**Usage Patterns:**
```python
# 1. Basic sync
result = folders_ops.get_contents(folder_id="abc123-def456", skip_count=100, max_items=100, order_by="example", folders_only=True, files_only=True)

# 2. Basic async
result = await folders_ops.get_contents_async(folder_id="abc123-def456", skip_count=100, max_items=100, order_by="example", folders_only=True, files_only=True)

# 3. Detailed sync (with full HTTP response)
result = folders_ops.get_contents_detailed(folder_id="abc123-def456", skip_count=100, max_items=100, order_by="example", folders_only=True, files_only=True)

# 4. Detailed async (with full HTTP response)
result = await folders_ops.get_contents_detailed_async(folder_id="abc123-def456", skip_count=100, max_items=100, order_by="example", folders_only=True, files_only=True)
```

### `get_contents_async(self, folder_id: str, skip_count: int = 0, max_items: int = 100, order_by: Optional[List[str]] = None, folders_only: bool = False, files_only: bool = False) -> python_alfresco_api.clients.core.nodes.models.NodeListResponse`

Async version of get_contents.

**Parameters:**
- `folder_id`: <class 'str'> (required)
- `skip_count`: <class 'int'> (default: 0)
- `max_items`: <class 'int'> (default: 100)
- `order_by`: typing.Optional[typing.List[str]] (default: None)
- `folders_only`: <class 'bool'> (default: False)
- `files_only`: <class 'bool'> (default: False)

**Usage Patterns:**
```python
# 1. Basic sync
result = folders_ops.get_contents_async(folder_id="abc123-def456", skip_count=100, max_items=100, order_by="example", folders_only=True, files_only=True)

# 2. Basic async
result = await folders_ops.get_contents_async_async(folder_id="abc123-def456", skip_count=100, max_items=100, order_by="example", folders_only=True, files_only=True)

# 3. Detailed sync (with full HTTP response)
result = folders_ops.get_contents_async_detailed(folder_id="abc123-def456", skip_count=100, max_items=100, order_by="example", folders_only=True, files_only=True)

# 4. Detailed async (with full HTTP response)
result = await folders_ops.get_contents_async_detailed_async(folder_id="abc123-def456", skip_count=100, max_items=100, order_by="example", folders_only=True, files_only=True)
```

### `get_httpx_client(self)`

Get direct access to raw httpx client for advanced operations.

Perfect for MCP servers that need raw HTTP access.

**Usage Patterns:**
```python
# 1. Basic sync
result = folders_ops.get_httpx_client()

# 2. Basic async
result = await folders_ops.get_httpx_client_async()

# 3. Detailed sync (with full HTTP response)
result = folders_ops.get_httpx_client_detailed()

# 4. Detailed async (with full HTTP response)
result = await folders_ops.get_httpx_client_detailed_async()
```

## Models

Operation-specific Pydantic models are available in:
```python
from python_alfresco_api.clients.core.folders.models import *
```

## Related Documentation

- [Core API Overview](../core_api.md)
- [V1.1 Architecture](../../clients_doc.md)
