# Content Operations - Core API

Auto-generated from V1.1 hierarchical code on 2025-07-15 00:36:43

## Overview

Content operations for the Core API.

## Usage

```python
from python_alfresco_api import ClientFactory

# Create factory and client
factory = ClientFactory(base_url="http://localhost:8080")
core_client = factory.create_core_client()

# Access content operations
content_ops = core_client.content

# Real method examples (sync):
result = content_ops.download_file(node_id="abc123-def456", output_path="/path/to/file", kwargs=...)
result = content_ops.download_file_async(node_id="abc123-def456", output_path="/path/to/file")
result = content_ops.update_content(node_id="abc123-def456", file_path="/path/to/file", major_version=True, comment="example", kwargs=...)

# Real method examples (async):
result = await content_ops.download_file_async(node_id="abc123-def456", output_path="/path/to/file", kwargs=...)
result = await content_ops.download_file_async_async(node_id="abc123-def456", output_path="/path/to/file")
result = await content_ops.update_content_async(node_id="abc123-def456", file_path="/path/to/file", major_version=True, comment="example", kwargs=...)
```

## Available Methods

This subsection provides 6 operations:

### `download_file(self, node_id: str, output_path: Union[str, pathlib.Path, NoneType] = None, **kwargs) -> python_alfresco_api.clients.core.content.models.DownloadResponse`

Download a file from Alfresco repository.

Perfect for MCP servers, backup scripts, and content workflows.
Downloads the content of the specified node to local storage.

Args:
    node_id: ID of the file node to download
    output_path: Where to save the file (default: current directory)
    
Returns:
    DownloadResponse: Response with download details and file path
    
Examples:
    >>> # Download to current directory
    >>> result = client.download_file("file-123")
    >>> print(f"Downloaded to: {result.file_path}")
    
    >>> # Download to specific location
    >>> result = client.download_file("file-123", "/downloads/report.pdf")
    
Raises:
    FileNotFoundError: If node doesn't exist
    PermissionError: If insufficient permissions
    IOError: If download fails

**Parameters:**
- `node_id`: <class 'str'> (required)
- `output_path`: typing.Union[str, pathlib.Path, NoneType] (default: None)
- `kwargs`: Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = content_ops.download_file(node_id="abc123-def456", output_path="/path/to/file", kwargs=...)

# 2. Basic async
result = await content_ops.download_file_async(node_id="abc123-def456", output_path="/path/to/file", kwargs=...)

# 3. Detailed sync (with full HTTP response)
result = content_ops.download_file_detailed(node_id="abc123-def456", output_path="/path/to/file", kwargs=...)

# 4. Detailed async (with full HTTP response)
result = await content_ops.download_file_detailed_async(node_id="abc123-def456", output_path="/path/to/file", kwargs=...)
```

### `download_file_async(self, node_id: str, output_path: Union[str, pathlib.Path, NoneType] = None) -> python_alfresco_api.clients.core.content.models.DownloadResponse`

Async version of download_file.

**Parameters:**
- `node_id`: <class 'str'> (required)
- `output_path`: typing.Union[str, pathlib.Path, NoneType] (default: None)

**Usage Patterns:**
```python
# 1. Basic sync
result = content_ops.download_file_async(node_id="abc123-def456", output_path="/path/to/file")

# 2. Basic async
result = await content_ops.download_file_async_async(node_id="abc123-def456", output_path="/path/to/file")

# 3. Detailed sync (with full HTTP response)
result = content_ops.download_file_async_detailed(node_id="abc123-def456", output_path="/path/to/file")

# 4. Detailed async (with full HTTP response)
result = await content_ops.download_file_async_detailed_async(node_id="abc123-def456", output_path="/path/to/file")
```

### `update_content(self, node_id: str, file_path: Union[str, pathlib.Path, IO[bytes]], major_version: bool = False, comment: Optional[str] = None, **kwargs) -> python_alfresco_api.clients.core.content.models.UploadResponse`

Update content of existing file.

Perfect for document revision workflows and content updates.
Replaces the content of an existing file node.

Args:
    node_id: ID of the file node to update
    file_path: Path to new content or binary stream
    major_version: Create major version (default: minor version)
    comment: Version comment
    
Returns:
    UploadResponse: Response with updated file details
    
Examples:
    >>> # Update with minor version
    >>> result = client.update_content("file-123", "updated_report.pdf")
    
    >>> # Update with major version and comment
    >>> result = client.update_content(
    ...     "file-123", 
    ...     "final_report.pdf",
    ...     major_version=True,
    ...     comment="Final version for Q4"
    ... )

**Parameters:**
- `node_id`: <class 'str'> (required)
- `file_path`: typing.Union[str, pathlib.Path, typing.IO[bytes]] (required)
- `major_version`: <class 'bool'> (default: False)
- `comment`: typing.Optional[str] (default: None)
- `kwargs`: Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = content_ops.update_content(node_id="abc123-def456", file_path="/path/to/file", major_version=True, comment="example", kwargs=...)

# 2. Basic async
result = await content_ops.update_content_async(node_id="abc123-def456", file_path="/path/to/file", major_version=True, comment="example", kwargs=...)

# 3. Detailed sync (with full HTTP response)
result = content_ops.update_content_detailed(node_id="abc123-def456", file_path="/path/to/file", major_version=True, comment="example", kwargs=...)

# 4. Detailed async (with full HTTP response)
result = await content_ops.update_content_detailed_async(node_id="abc123-def456", file_path="/path/to/file", major_version=True, comment="example", kwargs=...)
```

### `update_content_async(self, node_id: str, file_path: Union[str, pathlib.Path, IO[bytes]], major_version: bool = False, comment: Optional[str] = None) -> python_alfresco_api.clients.core.content.models.UploadResponse`

Async version of update_content.

**Parameters:**
- `node_id`: <class 'str'> (required)
- `file_path`: typing.Union[str, pathlib.Path, typing.IO[bytes]] (required)
- `major_version`: <class 'bool'> (default: False)
- `comment`: typing.Optional[str] (default: None)

**Usage Patterns:**
```python
# 1. Basic sync
result = content_ops.update_content_async(node_id="abc123-def456", file_path="/path/to/file", major_version=True, comment="example")

# 2. Basic async
result = await content_ops.update_content_async_async(node_id="abc123-def456", file_path="/path/to/file", major_version=True, comment="example")

# 3. Detailed sync (with full HTTP response)
result = content_ops.update_content_async_detailed(node_id="abc123-def456", file_path="/path/to/file", major_version=True, comment="example")

# 4. Detailed async (with full HTTP response)
result = await content_ops.update_content_async_detailed_async(node_id="abc123-def456", file_path="/path/to/file", major_version=True, comment="example")
```

### `upload_file(self, file_path: Union[str, pathlib.Path, IO[bytes]], parent_id: str = '-my-', filename: Optional[str] = None, properties: Optional[dict] = None, auto_rename: bool = True, **kwargs) -> python_alfresco_api.clients.core.content.models.UploadResponse`

Upload a file to Alfresco repository.

Perfect for MCP servers, scripts, and content workflows.
Creates a new file node with content in the specified parent folder.

Args:
    file_path: Path to file, Path object, or binary stream
    parent_id: Parent folder ID (default: "-my-" for user's home)
    filename: Custom filename (default: use file's name)
    properties: Custom properties to set on the file
    auto_rename: Automatically rename if name conflicts exist
    
Returns:
    UploadResponse: Response with uploaded file details
    
Examples:
    >>> # Upload a simple file
    >>> result = client.upload_file("report.pdf")
    >>> print(f"Uploaded: {result.entry.name}")
    
    >>> # Upload with custom properties
    >>> result = client.upload_file(
    ...     "data.xlsx",
    ...     parent_id="folder-123",
    ...     properties={"cm:title": "Monthly Report"}
    ... )
    
Raises:
    FileNotFoundError: If file_path doesn't exist
    PermissionError: If insufficient permissions
    ValueError: If invalid parameters

**Parameters:**
- `file_path`: typing.Union[str, pathlib.Path, typing.IO[bytes]] (required)
- `parent_id`: <class 'str'> (default: -my-)
- `filename`: typing.Optional[str] (default: None)
- `properties`: typing.Optional[dict] (default: None)
- `auto_rename`: <class 'bool'> (default: True)
- `kwargs`: Any (required)

**Usage Patterns:**
```python
# 1. Basic sync
result = content_ops.upload_file(file_path="/path/to/file", parent_id="abc123-def456", filename="My Document", auto_rename="My Document", kwargs=...)

# 2. Basic async
result = await content_ops.upload_file_async(file_path="/path/to/file", parent_id="abc123-def456", filename="My Document", auto_rename="My Document", kwargs=...)

# 3. Detailed sync (with full HTTP response)
result = content_ops.upload_file_detailed(file_path="/path/to/file", parent_id="abc123-def456", filename="My Document", auto_rename="My Document", kwargs=...)

# 4. Detailed async (with full HTTP response)
result = await content_ops.upload_file_detailed_async(file_path="/path/to/file", parent_id="abc123-def456", filename="My Document", auto_rename="My Document", kwargs=...)
```

### `upload_file_async(self, file_path: Union[str, pathlib.Path, IO[bytes]], parent_id: str = '-my-', filename: Optional[str] = None, properties: Optional[dict] = None, auto_rename: bool = True) -> python_alfresco_api.clients.core.content.models.UploadResponse`

Async version of upload_file.

**Parameters:**
- `file_path`: typing.Union[str, pathlib.Path, typing.IO[bytes]] (required)
- `parent_id`: <class 'str'> (default: -my-)
- `filename`: typing.Optional[str] (default: None)
- `properties`: typing.Optional[dict] (default: None)
- `auto_rename`: <class 'bool'> (default: True)

**Usage Patterns:**
```python
# 1. Basic sync
result = content_ops.upload_file_async(file_path="/path/to/file", parent_id="abc123-def456", filename="My Document", auto_rename="My Document")

# 2. Basic async
result = await content_ops.upload_file_async_async(file_path="/path/to/file", parent_id="abc123-def456", filename="My Document", auto_rename="My Document")

# 3. Detailed sync (with full HTTP response)
result = content_ops.upload_file_async_detailed(file_path="/path/to/file", parent_id="abc123-def456", filename="My Document", auto_rename="My Document")

# 4. Detailed async (with full HTTP response)
result = await content_ops.upload_file_async_detailed_async(file_path="/path/to/file", parent_id="abc123-def456", filename="My Document", auto_rename="My Document")
```

## Models

Operation-specific Pydantic models are available in:
```python
from python_alfresco_api.clients.core.content.models import *
```

## Related Documentation

- [Core API Overview](../core_api.md)
- [V1.1 Architecture](../../clients_doc.md)
