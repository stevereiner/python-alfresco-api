# API Reference

Complete API reference for Python Alfresco API client library.

## Table of Contents

- [Client Factory](#client-factory)
- [Authentication](#authentication)
- [Individual Clients](#individual-clients)
- [Core API](#core-api)
- [Search API](#search-api)
- [Discovery API](#discovery-api)
- [Workflow API](#workflow-api)
- [Model API](#model-api)
- [Search SQL API](#search-sql-api)
- [Pydantic Models](#pydantic-models)
- [Event System](#event-system)
- [Exception Classes](#exception-classes)

## Client Factory

### ClientFactory

The main entry point for creating and managing API clients.

```python
class ClientFactory:
    def __init__(
        self,
        base_url: str,
        auth_util: Optional[AuthUtil] = None,
        verify_ssl: bool = True,
        timeout: int = 30,
        session: Optional[aiohttp.ClientSession] = None
    )
```

**Parameters:**
- `base_url`: Alfresco server URL (e.g., "http://localhost:8080")
- `auth_util`: Optional authentication utility instance
- `verify_ssl`: Whether to verify SSL certificates (default: True)
- `timeout`: Request timeout in seconds (default: 30)
- `session`: Optional aiohttp session for connection pooling

**Methods:**

#### create_all_clients() → Dict[str, AlfrescoClient]
Creates all available API clients.

```python
factory = ClientFactory("http://localhost:8080")
clients = factory.create_all_clients()

# Access individual clients
auth_client = clients["auth"]
core_client = clients["core"]
search_client = clients["search"]
```

#### create_client(api_name: str) → AlfrescoClient
Creates a specific API client.

```python
auth_client = factory.create_client("auth")
core_client = factory.create_client("core")
```

#### Direct Factory Creation
Creates factory with parameters.

```python
factory = ClientFactory(
    base_url="http://localhost:8080",
    username="admin",
    password="admin"
)
```

## Authentication

### AuthUtil

Handles authentication and ticket management.

```python
class AuthUtil:
    def __init__(
        self,
        base_url: str,
        username: str,
        password: str,
        verify_ssl: bool = True
    )
```

**Methods:**

#### authenticate() → str
Authenticates and returns ticket.

```python
auth_util = AuthUtil("http://localhost:8080", "admin", "admin")
ticket = await auth_util.authenticate()
```

#### ensure_authenticated() → None
Ensures valid authentication (creates ticket if needed).

#### is_authenticated() → bool
Checks if currently authenticated.

#### get_headers() → Dict[str, str]
Gets headers with authentication ticket.

## Individual Clients

All clients share common methods and patterns.

### Base Client Interface

```python
class AlfrescoClient:
    def is_available() → bool
    def get_client_info() → Dict[str, Any]
    async def _ensure_auth() → None
```

## Core API

### AlfrescoCoreClient

Comprehensive API for nodes, sites, people, and more.

```python
from python_alfresco_api.clients.core_client import AlfrescoCoreClient

core_client = AlfrescoCoreClient("http://localhost:8080")
```

#### Node Operations

##### get_node(node_id: str) → NodeEntry
Gets node by ID.

```python
node = await core_client.get_node("-root-")
print(f"Node: {node.name}")
```

##### get_node_children(node_id: str, **params) → NodePaging
Gets child nodes.

```python
children = await core_client.get_node_children(
    "-root-",
    maxItems=10,
    skipCount=0,
    orderBy="name"
)
```

##### create_node(parent_id: str, node_data: dict) → NodeEntry
Creates new node.

```python
new_folder = await core_client.create_node(
    "-root-",
    {
        "name": "My Folder",
        "nodeType": "cm:folder",
        "properties": {
            "cm:title": "My Test Folder"
        }
    }
)
```

##### update_node(node_id: str, node_data: dict) → NodeEntry
Updates existing node.

##### delete_node(node_id: str) → None
Deletes node.

##### copy_node(node_id: str, target_parent_id: str) → NodeEntry
Copies node to new location.

##### move_node(node_id: str, target_parent_id: str) → NodeEntry
Moves node to new location.

#### Site Operations

##### get_sites(**params) → SitePaging
Gets all sites.

```python
sites = await core_client.get_sites(maxItems=50)
for site in sites.entries:
    print(f"Site: {site.entry.title}")
```

##### get_site(site_id: str) → SiteEntry
Gets specific site.

##### create_site(site_data: dict) → SiteEntry
Creates new site.

```python
new_site = await core_client.create_site({
    "title": "My Site",
    "description": "Test site",
    "visibility": "PUBLIC"
})
```

##### update_site(site_id: str, site_data: dict) → SiteEntry
Updates site.

##### delete_site(site_id: str) → None
Deletes site.

#### People Operations

##### get_people(**params) → PersonPaging
Gets all people.

##### get_person(person_id: str) → PersonEntry
Gets specific person.

```python
person = await core_client.get_person("admin")
print(f"Person: {person.firstName} {person.lastName}")
```

##### create_person(person_data: dict) → PersonEntry
Creates new person.

##### update_person(person_id: str, person_data: dict) → PersonEntry
Updates person.

#### Group Operations

##### get_groups(**params) → GroupPaging
Gets all groups.

##### get_group(group_id: str) → GroupEntry
Gets specific group.

##### create_group(group_data: dict) → GroupEntry
Creates new group.

## Search API

### AlfrescoSearchClient

Full-text search capabilities.

```python
from python_alfresco_api.clients.search_client import AlfrescoSearchClient

search_client = AlfrescoSearchClient("http://localhost:8080")
```

#### search(query_data: dict) → SearchResults
Performs search query.

```python
# Simple text search
results = await search_client.search({
    "query": {
        "query": "test document"
    }
})

# Advanced search with AFTS
results = await search_client.search({
    "query": {
        "query": "TYPE:cm:content AND cm:modified:[NOW-7DAYS TO NOW]",
        "language": "afts"
    },
    "filterQueries": [
        {"query": "PATH:'/app:company_home//*'"}
    ],
    "sort": [
        {"field": "cm:modified", "ascending": False}
    ],
    "paging": {
        "maxItems": 20,
        "skipCount": 0
    },
    "include": ["path", "properties"]
})

for entry in results.entries:
    node = entry.entry
    print(f"Found: {node.name} ({node.nodeType})")
```

## Discovery API

### AlfrescoDiscoveryClient

Repository information and capabilities.

```python
from python_alfresco_api.clients.discovery_client import AlfrescoDiscoveryClient

discovery_client = AlfrescoDiscoveryClient("http://localhost:8080")
```

#### get_repository_info() → DiscoveryEntry
Gets repository information.

```python
repo_info = await discovery_client.get_repository_info()
print(f"Version: {repo_info.version.display}")
print(f"Edition: {repo_info.edition}")
print(f"License: {repo_info.license}")
```

## Workflow API

### AlfrescoWorkflowClient

Process and task management.

```python
from python_alfresco_api.clients.workflow_client import AlfrescoWorkflowClient

workflow_client = AlfrescoWorkflowClient("http://localhost:8080")
```

#### Process Operations

##### get_processes(**params) → ProcessPaging
Gets all processes.

##### get_process(process_id: str) → ProcessEntry
Gets specific process.

##### start_process(process_data: dict) → ProcessEntry
Starts new process.

```python
new_process = await workflow_client.start_process({
    "processDefinitionKey": "activitiAdhoc",
    "variables": [
        {"name": "bpm_assignee", "value": "admin"}
    ]
})
```

#### Task Operations

##### get_tasks(**params) → TaskPaging
Gets all tasks.

##### get_task(task_id: str) → TaskEntry
Gets specific task.

##### complete_task(task_id: str, task_data: dict) → TaskEntry
Completes task.

## Model API

### AlfrescoModelClient

Content model introspection.

```python
from python_alfresco_api.clients.model_client import AlfrescoModelClient

model_client = AlfrescoModelClient("http://localhost:8080")
```

#### get_types(**params) → TypePaging
Gets content types.

#### get_type(type_id: str) → TypeEntry
Gets specific type.

#### get_aspects(**params) → AspectPaging
Gets aspects.

#### get_aspect(aspect_id: str) → AspectEntry
Gets specific aspect.

## Search SQL API

### AlfrescoSearchSQLClient

SQL-like search queries.

```python
from python_alfresco_api.clients.search_sql_client import AlfrescoSearchSQLClient

search_sql_client = AlfrescoSearchSQLClient("http://localhost:8080")
```

#### search_sql(query: str) → SearchSQLResults
Executes SQL query.

```python
results = await search_sql_client.search_sql(
    "SELECT * FROM alfresco WHERE CONTAINS('test')"
)
```

## Pydantic Models

All API responses use Pydantic v2 models for type safety and validation.

### Core Models

#### NodeEntry
Represents a node in the repository.

```python
class NodeEntry(BaseModel):
    id: str
    name: str
    nodeType: str
    isFolder: bool
    isFile: bool
    createdAt: datetime
    modifiedAt: datetime
    createdByUser: UserInfo
    modifiedByUser: UserInfo
    content: Optional[ContentInfo] = None
    path: Optional[PathInfo] = None
    properties: Optional[Dict[str, Any]] = None
```

#### SiteEntry
Represents a site.

```python
class SiteEntry(BaseModel):
    id: str
    guid: str
    title: str
    description: Optional[str] = None
    visibility: str
    preset: Optional[str] = None
    role: Optional[str] = None
```

#### PersonEntry
Represents a person.

```python
class PersonEntry(BaseModel):
    id: str
    firstName: str
    lastName: str
    displayName: str
    email: str
    enabled: bool
    emailNotificationsEnabled: bool
    company: Optional[CompanyInfo] = None
    properties: Optional[Dict[str, Any]] = None
```

### Search Models

#### SearchResults
Search query results.

```python
class SearchResults(BaseModel):
    entries: List[SearchResultEntry]
    pagination: Pagination
    context: Optional[SearchContext] = None
    facetQueries: Optional[List[FacetQuery]] = None
    facets: Optional[List[Facet]] = None
```

#### SearchResultEntry
Individual search result.

```python
class SearchResultEntry(BaseModel):
    entry: NodeEntry
    location: Optional[str] = None
    search: Optional[SearchMatch] = None
```

### Pagination Models

#### Pagination
Pagination information.

```python
class Pagination(BaseModel):
    count: int
    hasMoreItems: bool
    totalItems: Optional[int] = None
    skipCount: int
    maxItems: int
```

## Event System

### AlfrescoEventClient

Event subscription and handling (Enterprise/Community support).

```python
from python_alfresco_api.events import AlfrescoEventClient

event_client = AlfrescoEventClient("http://localhost:8080")
```

#### create_subscription(name: str, events: List[str]) → SubscriptionEntry
Creates event subscription.

#### register_event_handler(event_type: str)
Decorator for event handlers.

```python
@event_client.register_event_handler("org.alfresco.event.node.Created")
async def handle_node_created(event: EventNotification):
    print(f"Node created: {event.data.resource.name}")
```

#### start_listening() → None
Starts event listening.

## Exception Classes

### AlfrescoAPIError
Base exception for API errors.

```python
class AlfrescoAPIError(Exception):
    def __init__(self, message: str, status_code: int = None, response: dict = None):
        self.message = message
        self.status_code = status_code
        self.response = response
```

### AuthenticationError
Authentication-related errors.

### PermissionError
Permission-denied errors.

### NotFoundError
Resource not found errors.

### ValidationError
Request validation errors.

## Type Hints

The library provides complete type hints for all methods and models:

```python
from typing import Optional, List, Dict, Any
from python_alfresco_api.models import NodeEntry, SearchResults

async def search_nodes(query: str) -> List[NodeEntry]:
    results: SearchResults = await search_client.search({
        "query": {"query": query}
    })
    
    return [entry.entry for entry in results.entries]
```

## Configuration Reference

The library uses direct factory configuration:

```python
factory = ClientFactory(
    base_url="http://localhost:8080",
    username="admin", 
    password="admin",
    verify_ssl=False,
    timeout=30
)
```

### Environment Variables

- `ALFRESCO_BASE_URL`: Server URL
- `ALFRESCO_USERNAME`: Username
- `ALFRESCO_PASSWORD`: Password
- `ALFRESCO_VERIFY_SSL`: SSL verification (true/false)
- `ALFRESCO_TIMEOUT`: Request timeout (seconds)

---

This API reference covers all public methods and classes. For implementation details and examples, see the [main documentation](README.md). 