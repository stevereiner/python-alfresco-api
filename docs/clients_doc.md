# Python Alfresco API v1.1 - Clients Documentation
<!-- Auto-generated docs updated: 2025-07-15 00:36:44 -->

Welcome to the Python Alfresco API v1.1 clients documentation! This covers the modern, three-tier hierarchical architecture for integrating with Alfresco Content Services.

## 🏗️ Three-Tier Architecture Overview

**Level 1: Global Models** (`python_alfresco_api.models`)
- Shared across ALL APIs
- BaseEntry, PagingInfo, ErrorResponse, UserInfo, ContentInfo

**Level 2: API-Level Models & Clients** (e.g., `python_alfresco_api.clients.core`)  
- Shared within ONE API (Core, Search, Discovery, etc.)
- CoreResponse, Permission, NodeType, IncludeOption

**Level 3: Operation-Specific Models & APIs** (e.g., `python_alfresco_api.clients.core.nodes`)
- Specific to ONE operation group
- Node, NodeResponse, CreateNodeRequest, UpdateNodeRequest

## 🚀 Quick Start

```python
from python_alfresco_api import ClientFactory
from python_alfresco_api.auth_util import AuthUtil

# Factory Pattern (Recommended)
auth = AuthUtil('username', 'password')
factory = ClientFactory(base_url="http://localhost:8080", auth_util=auth)
core_client = factory.create_core_client()

# Three-tier access
node = core_client.nodes.get("abc123-def456")        # Level 3 operation
folder = core_client.nodes.create_folder(name="My Folder", parent_id="-my-")

# Raw client access when needed
httpx_client = core_client.get_httpx_client()
response = httpx_client.get(f"/nodes/{node_id}")
```

## 📚 API Documentation

### [Core API](core/core_api.md)
Complete content management - nodes, sites, people, groups, and more.

**Key Operations:**
- [Nodes](core/nodes/nodes_api.md) - File and folder management (80+ operations)
- [Sites](core/sites/sites_api.md) - Site collaboration and membership
- [People](core/people/people_api.md) - User management and profiles
- [Groups](core/groups/groups_api.md) - Group management and membership
- [Content](core/content/content_api.md) - Content upload, download, and versioning

### [Search API](search/search_api.md) 
Content and metadata search using AFTS and CMIS queries.

**Key Operations:**
- AFTS (Alfresco Full Text Search) queries
- CMIS (Content Management Interoperability Services) queries
- Metadata and content searches
- **Models**: [Search Models](search/search_models.md)

### [Discovery API](discovery/discovery_api.md)
Repository information, server capabilities, system status.

**Key Operations:**
- Repository information and capabilities
- Server version and status
- System configuration details
- **Models**: [Discovery Models](discovery/discovery_models.md)

### [Workflow API](workflow/workflow_api.md)
Process and task management for business workflows.

**Key Operations:**
- Process definitions and deployments
- Task management and assignment
- Workflow instance tracking
- **Models**: [Workflow Models](workflow/workflow_models.md)

### [Model API](model/model_api.md)  
Content model introspection - types, aspects, properties.

**Key Operations:**
- Content type definitions
- Aspect and property inspection
- Model validation and structure
- **Models**: [Model Models](model/model_models.md)

### [Search SQL API](search_sql/search_sql_api.md)
SQL-based search for Solr admin operations.

**Key Operations:**
- Direct Solr query execution
- Advanced search configurations
- Administrative search operations
- **Models**: [Search SQL Models](search_sql/search_sql_models.md)

### [Authentication API](auth/auth_api.md)
Authentication and session management.

**Key Operations:**
- Ticket-based authentication
- Session management
- User authentication validation
- **Models**: [Auth Models](auth/auth_models.md)

## 🔄 Sync vs Async APIs

All operations provide both synchronous and asynchronous variants:

**Synchronous (Perfect for scripts, MCP servers):**
```python
node = core_client.nodes.get("abc123-def456")
folder = core_client.nodes.create_folder(name="My Folder", parent_id="-my-")
children = core_client.nodes.list_children("folder-123")
```

**Asynchronous (Perfect for web apps, high performance):**
```python
node = await core_client.nodes.get_async("abc123-def456")
folder = await core_client.nodes.create_folder_async(name="My Folder", parent_id="-my-")
children = await core_client.nodes.list_children_async("folder-123")
```

## 🛠️ Raw Client Access

When you need direct access to the underlying HTTP client:

```python
# Get httpx client for custom operations  
httpx_client = core_client.get_httpx_client()

# Custom HTTP requests
response = httpx_client.get("/custom-endpoint")
response = httpx_client.post("/nodes/-root-/children", json={"name": "test"})
```

## 💡 Common Usage Patterns

### File Management
```python
# Create folder
folder = core_client.nodes.create_folder(name="Projects", parent_id="-my-")

# Upload file
with open("document.pdf", "rb") as f:
    document = core_client.content.upload(
        parent_id=folder.entry.id,
        file=f,
        name="document.pdf"
    )

# Download file
content = core_client.content.download(document.entry.id)
```

### Site Management
```python
# Create site
site = core_client.sites.create(
    title="My Project Site",
    visibility="PRIVATE"
)

# Add members
core_client.sites.add_member(
    site_id=site.entry.id,
    user_id="john.doe",
    role="SiteCollaborator"
)
```

### Search Operations
```python
# Search content
search_client = factory.create_search_client()
results = search_client.search.query(
    query="TYPE:cm:content AND cm:name:*.pdf",
    max_items=100
)

# CMIS search
cmis_results = search_client.search.cmis_query(
    query="SELECT * FROM cm:content WHERE cm:name LIKE '%.pdf'"
)
```

## 📋 Features

- ✅ **Three-tier architecture** with perfect locality
- ✅ **Sync and async APIs** - use what fits your use case
- ✅ **Lazy loading** - 20x performance improvement
- ✅ **Rich Pydantic v2 models** - perfect for AI/LLM integration
- ✅ **Type safety** - full IDE support with auto-completion
- ✅ **Raw client access** - escape hatch for advanced operations
- ✅ **MCP compatibility** - optimized for Model Context Protocol servers

## 🔗 Navigation

- **[API Reference Index](API_DOCUMENTATION_INDEX.md)** - Complete v1.0 documentation
- **[Authentication Guide](AUTHENTICATION_GUIDE.md)** - Setup and authentication  
- **[Installation Guide](INSTALLATION.md)** - Installation and configuration
- **[Examples](../examples/)** - Working code examples 