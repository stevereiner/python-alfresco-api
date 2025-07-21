# Core API - V1.1 Hierarchical Architecture

Auto-generated from actual V1.1 code on 2025-07-15 00:36:43

## Overview

Main client for Alfresco Core API operations.

Provides lazy-loaded access to ALL 21 Core API operation groups:
- nodes: Node management (files, folders, metadata)
- content: Content upload/download operations
- versions: Version control (checkout, checkin, cancel)
- sites: Site/collaboration management
- people: User/person management
- groups: Group management
- shared_links: Public link sharing
- comments: Node comments and discussions
- tags: Content tagging
- favorites: User favorites
- activities: User and site activities
- audit: Audit trail and logs
- downloads: Download management
- networks: Network/tenant management
- preferences: User preferences
- probes: System health probes
- queries: Saved queries and search
- ratings: Content ratings/likes
- renditions: Thumbnail/preview generation
- trashcan: Deleted items management
- actions: Action execution and definitions

Uses lazy loading for maximum performance - operations are
only imported and initialized when first accessed.

Examples:
    ```python
    # Create Core API client
    from python_alfresco_api import ClientFactory
    
    client_factory = ClientFactory(base_url="http://localhost:8080")
    core_client = client_factory.create_core_client()
    
    # Use node operations (lazy loaded)
    node = core_client.nodes.get("abc123-def456")
    
    # Use site operations (lazy loaded)
    sites = core_client.sites.list()
    
    # Use people operations (lazy loaded)
    people = core_client.people.list()
    
    # Operations are cached after first access
    children = core_client.nodes.get_children("folder-123")
    ```
    
Note:
    This client uses lazy loading - operation modules are imported
    only when first accessed, providing maximum performance
    for applications that don't use all operations.

**Client Class**: `AlfrescoCoreClient`

## Quick Start

```python
from python_alfresco_api import ClientFactory

# Create factory
factory = ClientFactory(base_url="http://localhost:8080")

# Get core client
core_client = factory.create_core_client()

# Real method examples:
new_item = nodes_client.nodes.create(request_data)
new_item = await nodes_client.nodes.create_async(request_data)
```

## Architecture

This API follows the V1.1 three-tier hierarchical architecture:

- **Level 1**: Global models shared across all APIs
- **Level 2**: API-level models and client (`AlfrescoCoreClient`) 
- **Level 3**: Operation-specific subsections with focused functionality

## Subsections

This API is organized into the following operation groups:

### [Actions](actions/actions_api.md)
Operations for actions management.

**Available Methods:**
- `action_details(self, action_definition_id: Any) -> python_alfresco_api.clients.core.actions.models.ActionsResponse` - Action Details operation
- `action_details_async(self, action_definition_id: Any) -> python_alfresco_api.clients.core.actions.models.ActionsResponse` - Action Details operation (async)
- `action_details_detailed(self, action_definition_id: Any)` - Action Details operation (detailed)
- *...and 14 more methods*

### [Activities](activities/activities_api.md)
Operations for activities management.

**Available Methods:**
- `get_httpx_client(self)` - Get direct access to raw httpx client for advanced operations
- `list_activities_for_person(self, person_id: Any, skip_count: Any, max_items: Any, who: Any, site_id: Any, fields: Any) -> python_alfresco_api.clients.core.activities.models.ActivitiesResponse` - List Activities For Person operation
- `list_activities_for_person_async(self, person_id: Any, skip_count: Any, max_items: Any, who: Any, site_id: Any, fields: Any) -> python_alfresco_api.clients.core.activities.models.ActivitiesResponse` - List Activities For Person operation (async)
- *...and 2 more methods*

### [Audit](audit/audit_api.md)
Operations for audit management.

**Available Methods:**
- `get_httpx_client(self)` - Get direct access to raw httpx client for advanced operations

### [Comments](comments/comments_api.md)
Operations for comments management.

**Available Methods:**
- `create_comment(self, node_id: Any, body: Any, fields: Any) -> python_alfresco_api.clients.core.comments.models.CommentsResponse` - Create Comment operation
- `create_comment_async(self, node_id: Any, body: Any, fields: Any) -> python_alfresco_api.clients.core.comments.models.CommentsResponse` - Create Comment operation (async)
- `create_comment_detailed(self, node_id: Any, body: Any, fields: Any)` - Create Comment operation (detailed)
- *...and 14 more methods*

### [Content](content/content_api.md)
Operations for content management.

**Available Methods:**
- `download_file(self, node_id: str, output_path: Union[str, pathlib.Path, NoneType] = None, **kwargs) -> python_alfresco_api.clients.core.content.models.DownloadResponse` - Download a file from Alfresco repository
- `download_file_async(self, node_id: str, output_path: Union[str, pathlib.Path, NoneType] = None) -> python_alfresco_api.clients.core.content.models.DownloadResponse` - Async version of download_file
- `update_content(self, node_id: str, file_path: Union[str, pathlib.Path, IO[bytes]], major_version: bool = False, comment: Optional[str] = None, **kwargs) -> python_alfresco_api.clients.core.content.models.UploadResponse` - Update content of existing file
- *...and 3 more methods*

### [Downloads](downloads/downloads_api.md)
Operations for downloads management.

**Available Methods:**
- `cancel_download(self, download_id: Any) -> python_alfresco_api.clients.core.downloads.models.DownloadsResponse` - Cancel Download operation
- `cancel_download_async(self, download_id: Any) -> python_alfresco_api.clients.core.downloads.models.DownloadsResponse` - Cancel Download operation (async)
- `cancel_download_detailed(self, download_id: Any)` - Cancel Download operation (detailed)
- *...and 12 more methods*

### [Favorites](favorites/favorites_api.md)
Operations for favorites management.

**Available Methods:**
- `get_httpx_client(self)` - Get direct access to raw httpx client for advanced operations

### [Groups](groups/groups_api.md)
Operations for groups management.

**Available Methods:**
- `get_httpx_client(self)` - Get direct access to raw httpx client for advanced operations

### [Networks](networks/networks_api.md)
Operations for networks management.

**Available Methods:**
- `get_httpx_client(self)` - Get direct access to raw httpx client for advanced operations

### [Nodes](nodes/nodes_api.md)
Operations for nodes management.

**Available Methods:**
- `browse(self, node_id: str = '-my-', max_items: int = 100) -> python_alfresco_api.clients.core.nodes.models.NodeListResponse` - Convenience method: Browse folder contents
- `browse_async(self, node_id: str = '-my-', max_items: int = 100) -> python_alfresco_api.clients.core.nodes.models.NodeListResponse` - Convenience method: Browse folder contents (async)
- `copy(self, node_id: str, request: python_alfresco_api.clients.core.nodes.models.CopyNodeRequest, include: Optional[List[Union[str, python_alfresco_api.clients.core.models.IncludeOption]]] = None) -> python_alfresco_api.clients.core.nodes.models.NodeResponse` - Copy a node - clean and simple
- *...and 77 more methods*

### [People](people/people_api.md)
Operations for people management.

**Available Methods:**
- `get_httpx_client(self)` - Get direct access to raw httpx client for advanced operations

### [Preferences](preferences/preferences_api.md)
Operations for preferences management.

**Available Methods:**
- `get_httpx_client(self)` - Get direct access to raw httpx client for advanced operations

### [Probes](probes/probes_api.md)
Operations for probes management.

**Available Methods:**
- `get_httpx_client(self)` - Get direct access to raw httpx client for advanced operations
- `get_httpx_client_detailed(self)` - Get Httpx Client operation (detailed sync)
- `get_httpx_client_detailed_async(self)` - Get Httpx Client operation (detailed async)
- *...and 4 more methods*

### [Queries](queries/queries_api.md)
Operations for queries management.

**Available Methods:**
- `find_nodes(self, term: Any, root_node_id: Any, skip_count: Any, max_items: Any, node_type: Any, include: Any, order_by: Any, fields: Any) -> python_alfresco_api.clients.core.queries.models.QueriesResponse` - Find Nodes operation
- `find_nodes_async(self, term: Any, root_node_id: Any, skip_count: Any, max_items: Any, node_type: Any, include: Any, order_by: Any, fields: Any) -> python_alfresco_api.clients.core.queries.models.QueriesResponse` - Find Nodes operation (async)
- `find_nodes_detailed(self, term: Any, root_node_id: Any, skip_count: Any, max_items: Any, node_type: Any, include: Any, order_by: Any, fields: Any)` - Find Nodes operation (detailed)
- *...and 12 more methods*

### [Ratings](ratings/ratings_api.md)
Operations for ratings management.

**Available Methods:**
- `create_rating(self, node_id: Any, body: Any, fields: Any) -> python_alfresco_api.clients.core.ratings.models.RatingsResponse` - Create Rating operation
- `create_rating_async(self, node_id: Any, body: Any, fields: Any) -> python_alfresco_api.clients.core.ratings.models.RatingsResponse` - Create Rating operation (async)
- `create_rating_detailed(self, node_id: Any, body: Any, fields: Any)` - Create Rating operation (detailed)
- *...and 16 more methods*

### [Renditions](renditions/renditions_api.md)
Operations for renditions management.

**Available Methods:**
- `create_rendition(self, node_id: Any, body: Any) -> python_alfresco_api.clients.core.renditions.models.RenditionsResponse` - Create Rendition operation
- `create_rendition_async(self, node_id: Any, body: Any) -> python_alfresco_api.clients.core.renditions.models.RenditionsResponse` - Create Rendition operation (async)
- `create_rendition_detailed(self, node_id: Any, body: Any)` - Create Rendition operation (detailed)
- *...and 12 more methods*

### [Shared Links](shared_links/shared_links_api.md)
Operations for shared links management.

**Available Methods:**
- `get_httpx_client(self)` - Get direct access to raw httpx client for advanced operations

### [Sites](sites/sites_api.md)
Operations for sites management.

**Available Methods:**
- `get_httpx_client(self)` - Get direct access to raw httpx client for advanced operations

### [Tags](tags/tags_api.md)
Operations for tags management.

**Available Methods:**
- `get_httpx_client(self)` - Get direct access to raw httpx client for advanced operations

### [Trashcan](trashcan/trashcan_api.md)
Operations for trashcan management.

**Available Methods:**
- `get_httpx_client(self)` - Get direct access to raw httpx client for advanced operations

### [Versions](versions/versions_api.md)
Operations for versions management.

**Available Methods:**
- `cancel_checkout(self, node_id: str, **kwargs) -> python_alfresco_api.clients.core.versions.models.CheckoutResponse` - Cancel checkout (unlock) a document
- `cancel_checkout_async(self, node_id: str) -> python_alfresco_api.clients.core.versions.models.CheckoutResponse` - Async version of cancel_checkout
- `cancel_checkout_detailed(self, node_id: str, **kwargs)` - Cancel checkout operation (detailed sync)
- *...and 11 more methods*

## Client Properties

Lazy-loaded subsection clients:

### `actions`
Access to actions operations (4 operations).

### `activities`
Access to activities operations (1 operations).

### `api`
Get the API name.

### `audit`
Access to audit operations (8 operations).

### `auth_type`
Get the authentication type.

### `available`
Check if the client is available and functional.

### `base_url`
Get the server base URL.

### `client_factory`
Get the client factory.

### `comments`
Access to comments operations (4 operations).

### `content`
Access to content operations (upload, download, update content).

### `downloads`
Access to downloads operations (3 operations).

### `favorites`
Access to favorites operations (8 operations).



### `groups`
Access to groups operations (9 operations).

### `httpx_client`
Get direct access to httpx client for raw HTTP operations.

This is the STANDARD way to access the HTTP client.
Perfect for MCP servers that need raw HTTP access.

### `is_initialized`
Check if the client is initialized and functional.

This is the STANDARD way to check initialization status.

### `networks`
Access to networks operations (3 operations).

### `nodes`
Access node operations (lazy loaded).

Provides comprehensive node management including:
- Get node information by ID
- Create files and folders
- Update node properties and metadata
- Delete nodes (trash or permanent)
- Copy and move nodes between locations
- List folder children with pagination

Returns:
    NodesClient: Node operation interface

### `people`
Access to people operations (8 operations).

### `preferences`
Access to preferences operations (2 operations).

### `probes`
Access to probes operations (1 operations).

### `queries`
Access to queries operations (3 operations).

### `ratings`
Access to ratings operations (4 operations).

### `raw_client`
Get the raw authenticated client for advanced operations.

This is the STANDARD way to access the underlying client.

### `renditions`
Access to renditions operations (3 operations).

### `shared_links`
Access to shared_links operations (7 operations).

### `sites`
Access to sites operations (28 operations).

### `tags`
Access to tags operations (6 operations).

### `timeout`
Get request timeout.

### `trashcan`
Access to trashcan operations (6 operations).

### `verify_ssl`
Get SSL verification setting.

### `versions`
Access to versions operations (checkout, checkin, cancel checkout).

## Direct Methods

### `ensure_httpx_client(self)`
DEPRECATED: Use httpx_client property instead.

This method is kept for backward compatibility only.

### `get_httpx_client(self)`
DEPRECATED: Use httpx_client property instead.

This method is kept for backward compatibility only.

## Sync/Async Patterns

All operations support both synchronous and asynchronous execution:

```python
# Synchronous (perfect for scripts, MCP servers)
result = actions_client.actions.action_details()

# Asynchronous (perfect for web apps)
result = await actions_client.actions.action_details_async()
```

## 4-Pattern Method Examples

Each operation provides 4 execution patterns:

```python
# 1. Basic sync
result = actions_client.actions.action_details()

# 2. Basic async  
result = await actions_client.actions.action_details_async()

# 3. Detailed sync (with full HTTP response)
result = actions_client.actions.action_details_detailed()

# 4. Detailed async (with full HTTP response)
result = await actions_client.actions.action_details_async_detailed_async()
```

## Raw Client Access

For advanced operations, access the underlying HTTP client:

```python
# Get raw client
raw_client = core_client._get_raw_client()

# Get HTTPx client for custom requests
httpx_client = raw_client.get_httpx_client()
response = httpx_client.get("/custom-endpoint")
```

## Related Documentation

- [V1.1 Architecture Overview](../clients_doc.md)
- [Authentication Guide](../AUTHENTICATION_GUIDE.md)
- [MCP Integration Guide](../V11_MCP_SYNC_MIGRATION_GUIDE.md)
