# Utility Functions - V1.1 Compatible

Auto-generated from actual utility code on 2025-07-15 00:36:44

## Overview

High-level utility functions optimized for V1.1 hierarchical clients and MCP server integration.

## Available Utilities

### Content Utils
**Module**: `python_alfresco_api.utils.content_utils`

Content utility functions for the Alfresco API.

This module provides convenient utility functions for content operations
that MCP servers and other applications need, using authenticated HTTP client
patterns that won't be overwritten by codegen.

**Functions:**
- **`download_file(core_client: python_alfresco_api.clients.core.core_client.AlfrescoCoreClient, node_id: str, output_path: Union[str, pathlib.Path, NoneType] = None, as_attachment: bool = False) -> Union[bytes, str]`** - Download a file from Alfresco repository.
- **`get_content_info(core_client: python_alfresco_api.clients.core.core_client.AlfrescoCoreClient, node_id: str) -> Dict[str, Any]`** - Get content information for a file node.
- **`update_content(core_client: python_alfresco_api.clients.core.core_client.AlfrescoCoreClient, node_id: str, file_path: Union[str, pathlib.Path, bytes], major_version: bool = False, comment: Optional[str] = None, filename: Optional[str] = None) -> Any`** - Update content of an existing file.
- **`upload_file(core_client: python_alfresco_api.clients.core.core_client.AlfrescoCoreClient, file_path: Union[str, pathlib.Path], parent_id: str = '-my-', filename: Optional[str] = None, description: Optional[str] = None, properties: Optional[Dict[str, Any]] = None, auto_rename: bool = True) -> Any`** - Upload a file to Alfresco repository using authenticated HTTP client.

### Mcp Formatters
**Module**: `python_alfresco_api.utils.mcp_formatters`

MCP Formatters for Alfresco API responses.

This module provides formatters that convert raw API responses into MCP-compatible
formatted strings that match the expected output schema for MCP tools.

These formatters are designed to work with the utility functions and provide
human-readable output for AI models and MCP servers.

**Functions:**
- **`format_browse_results(browse_result: Any, node_id: str = '-my-') -> str`** - Format browse/repository listing results for MCP compatibility.
- **`format_delete_result(delete_result: Any, node_id: str) -> str`** - Format node deletion results for MCP compatibility.
- **`format_discovery_result(discovery_result: Any) -> str`** - Format repository discovery/info results for MCP compatibility.
- **`format_download_result(download_content: Any, node_id: str) -> str`** - Format download results for MCP compatibility.
- **`format_folder_creation_result(creation_result: Any, folder_name: str) -> str`** - Format folder creation results for MCP compatibility.
- **`format_node_properties_result(properties_result: Any, node_id: str) -> str`** - Format node properties retrieval results for MCP compatibility.
- **`format_search_results(search_result: Any, query: str, max_results: int = 25) -> str`** -     Format search results for MCP compatibility.
- **`format_upload_result(upload_result: Any, filename: str) -> str`** - Format document upload results for MCP compatibility.
- **`format_version_operation_result(operation_result: Dict[str, Any], operation_name: str) -> str`** - Format version operations (checkout/checkin/cancel) for MCP compatibility.

### Node Utils
**Module**: `python_alfresco_api.utils.node_utils`

Node utility functions for the Alfresco API.

This module provides convenient utility functions for common node operations
that MCP servers and other applications need, using the v1.1 hierarchical
client methods consistently (no raw httpx mixing).

**Functions:**
- **`browse_repository(core_client: python_alfresco_api.clients.core.core_client.AlfrescoCoreClient, parent_id: str = '-my-', max_items: int = 100, skip_count: int = 0, include_properties: bool = True) -> Any`** - Browse repository contents (list folders/files).
- **`cancel_checkout(core_client: python_alfresco_api.clients.core.core_client.AlfrescoCoreClient, node_id: str) -> Any`** - Cancel checkout of a document (unlock without creating version).
- **`checkin_document(core_client: python_alfresco_api.clients.core.core_client.AlfrescoCoreClient, node_id: str, content: Union[str, bytes, pathlib.Path, NoneType] = None, comment: Optional[str] = None, major_version: bool = False) -> Any`** - Checkin a document (create new version and unlock).
- **`checkout_document(core_client: python_alfresco_api.clients.core.core_client.AlfrescoCoreClient, node_id: str) -> Any`** - Checkout a document for editing (lock it).
- **`create_folder(core_client: python_alfresco_api.clients.core.core_client.AlfrescoCoreClient, name: str, parent_id: str = '-my-', title: Optional[str] = None, description: Optional[str] = None, properties: Optional[Dict[str, Any]] = None) -> Any`** - Create a new folder.
- **`delete_node(core_client: python_alfresco_api.clients.core.core_client.AlfrescoCoreClient, node_id: str, permanent: bool = False) -> Any`** - Delete a node (move to trash or permanent deletion).
- **`download_document(core_client: python_alfresco_api.clients.core.core_client.AlfrescoCoreClient, node_id: str, output_path: Union[str, pathlib.Path, NoneType] = None, attachment: bool = False) -> Any`** - Download a document from Alfresco.
- **`find_nodes(core_client: python_alfresco_api.clients.core.core_client.AlfrescoCoreClient, search_term: str, max_items: int = 100, skip_count: int = 0, node_type: Optional[str] = None, parent_id: Optional[str] = None) -> Any`** - Find nodes by search term (simple node search).
- **`get_node_properties(core_client: python_alfresco_api.clients.core.core_client.AlfrescoCoreClient, node_id: str, include_path: bool = True, include_permissions: bool = False) -> Any`** - Get node properties and metadata.
- **`update_node_properties(core_client: python_alfresco_api.clients.core.core_client.AlfrescoCoreClient, node_id: str, properties: Dict[str, Any], name: Optional[str] = None) -> Any`** - Update node properties and metadata.
- **`upload_document(core_client: python_alfresco_api.clients.core.core_client.AlfrescoCoreClient, file_path: Union[str, pathlib.Path], parent_id: str = '-my-', name: Optional[str] = None, title: Optional[str] = None, description: Optional[str] = None, properties: Optional[Dict[str, Any]] = None, major_version: bool = False) -> Any`** - Upload a document to Alfresco.

### Search Utils
**Module**: `python_alfresco_api.utils.search_utils`

Search utility functions for the Alfresco API.

This module provides convenient utility functions for common search operations,
using the proper Pydantic models from the raw search client for type safety.

**Functions:**
- **`advanced_search(search_client: Any, query_str: str, max_items: int = 100, skip_count: int = 0, sort_by: Optional[str] = None, sort_ascending: bool = True, filter_queries: Optional[List[str]] = None, include_fields: Optional[List[str]] = None, scope_location: Optional[str] = None) -> Any`** - Advanced search with sorting, filtering, and scoping options.
- **`build_query(term: Optional[str] = None, content_type: Optional[str] = None, site: Optional[str] = None, creator: Optional[str] = None, modifier: Optional[str] = None, folder_path: Optional[str] = None, created_after: Optional[str] = None, created_before: Optional[str] = None, modified_after: Optional[str] = None, modified_before: Optional[str] = None) -> str`** - Build an AFTS query string from common search criteria.
- **`pattern_search(search_client: Any, pattern: str, username: Optional[str] = None, max_items: int = 20) -> Any`** - Execute a predefined search pattern.
- **`search_by_creator(search_client: Any, creator: str, max_items: int = 20) -> Any`** - Search for content by creator.
- **`search_by_type(search_client: Any, content_type: str, max_items: int = 20) -> Any`** - Search for content by type.
- **`search_in_site(search_client: Any, site_id: str, search_term: Optional[str] = None, max_items: int = 20) -> Any`** - Search for content in a specific site.
- **`simple_search(search_client: Any, query_str: str, max_items: int = 20, skip_count: int = 0, include_fields: Optional[List[str]] = None) -> Any`** - Simple search utility function that mimics the original MCP server pattern.

### Version Utils
**Module**: `python_alfresco_api.utils.version_utils`

Version utility functions for the Alfresco API.

This module provides convenient utility functions for document versioning operations
that MCP servers and other applications need, using authenticated HTTP client
patterns that won't be overwritten by codegen.

**Functions:**
- **`cancel_checkout(core_client: python_alfresco_api.clients.core.core_client.AlfrescoCoreClient, node_id: str) -> Dict[str, Any]`** - Cancel checkout (unlock) a document without creating a version.
- **`checkin_document(core_client: python_alfresco_api.clients.core.core_client.AlfrescoCoreClient, node_id: str, content_file: Union[str, pathlib.Path, NoneType] = None, content_bytes: Optional[bytes] = None, comment: Optional[str] = None, major_version: bool = False) -> Dict[str, Any]`** - Checkin a document (create new version and unlock).
- **`checkout_document(core_client: python_alfresco_api.clients.core.core_client.AlfrescoCoreClient, node_id: str) -> Dict[str, Any]`** - Checkout (lock) a document for editing.
- **`get_version_content(core_client: python_alfresco_api.clients.core.core_client.AlfrescoCoreClient, node_id: str, version_id: str, output_path: Union[str, pathlib.Path, NoneType] = None) -> Union[bytes, str]`** - Download content of a specific version.
- **`get_version_history(core_client: python_alfresco_api.clients.core.core_client.AlfrescoCoreClient, node_id: str, include_content: bool = False) -> Dict[str, Any]`** - Get version history for a document.
- **`revert_to_version(core_client: python_alfresco_api.clients.core.core_client.AlfrescoCoreClient, node_id: str, version_id: str, comment: Optional[str] = None, major_version: bool = False) -> Dict[str, Any]`** - Revert document to a previous version.

## Usage Patterns

### With V1.1 Hierarchical Clients

```python
from python_alfresco_api import ClientFactory
from python_alfresco_api.utils import search_utils, node_utils

# Create client
factory = ClientFactory(base_url="http://localhost:8080")
core_client = factory.create_core_client()

# Use utilities with V1.1 client - real method examples:
results = search_utils.simple_search(core_client.search, "admin OR test", max_items=10)
folder = node_utils.create_folder(core_client, "My New Folder", parent_id="-my-")
document = node_utils.upload_document(core_client, "document.pdf", "/path/to/file.pdf")
```

### With MCP Servers

Utilities are optimized for MCP (Model Context Protocol) server patterns:

```python
# MCP-compatible search with real method signatures
async def search_content_impl(query: str, ctx: Context) -> str:
    client = await ensure_connection()
    results = search_utils.simple_search(client.search, query, max_items=20)
    return mcp_formatters.format_search_results(results, query)

# MCP-compatible node operations
async def create_folder_impl(name: str, parent_id: str, ctx: Context) -> str:
    client = await ensure_connection()
    result = node_utils.create_folder(client, name, parent_id)
    return mcp_formatters.format_folder_creation_result(result, name, parent_id)
```

## Related Documentation

- [V1.1 Architecture](clients_doc.md)
- [MCP Integration Guide](V11_MCP_SYNC_MIGRATION_GUIDE.md)
