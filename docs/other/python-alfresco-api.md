# Python Alfresco API v1.1 - Complete Documentation

Welcome to the Python Alfresco API v1.1 documentation! This library provides a modern, three-tier hierarchical architecture for integrating with Alfresco Content Services.

## 🏗️ Architecture Overview

### Three-Tier Hierarchical Structure

**Level 1: Global Models** (`python_alfresco_api.models`)
- Shared across ALL APIs
- BaseEntry, PagingInfo, ErrorResponse, UserInfo, ContentInfo

**Level 2: API-Level Models** (e.g., `python_alfresco_api.clients.core.models`)  
- Shared within ONE API (Core, Search, Discovery, etc.)
- CoreResponse, Permission, NodeType, IncludeOption

**Level 3: Operation-Specific Models** (e.g., `python_alfresco_api.clients.core.nodes.models`)
- Specific to ONE operation group
- Node, NodeResponse, CreateNodeRequest, UpdateNodeRequest

### Usage Patterns

```python
from python_alfresco_api import ClientFactory

# 1. Factory Pattern (Recommended)
factory = ClientFactory(base_url="http://localhost:8080")
core_client = factory.create_core_client()

# 2. Three-tier access
node = core_client.nodes.get("abc123-def456")        # Level 3 operation
folder = core_client.nodes.create(parent_id="-my-", request=...)

# 3. Raw client access when needed
raw_client = core_client._get_raw_client()
httpx_client = raw_client.get_httpx_client()
```

## 📚 API Documentation

### [Core API](core/core_api.md)
Complete content management - nodes, sites, people, groups, and more.

**Operation Groups:**
- **[Nodes Operations](core/nodes/nodes_operations.md)** - File/folder management, CRUD operations
- **[Folders Operations](core/folders/folders_operations.md)** - Folder-specific operations  
- **[Content Operations](core/content/content_operations.md)** - Upload/download, content management
- **[Sites Operations](core/sites/sites_operations.md)** - Site management and collaboration
- **[People Operations](core/people/people_operations.md)** - User management and profiles
- **[Groups Operations](core/groups/groups_operations.md)** - Group management and membership

### [Search API](search/search_api.md) 
Content and metadata search using AFTS and CMIS queries.

**Operation Groups:**
- **[Content Search](search/content/content_search.md)** - Full-text search, CMIS queries

### [Discovery API](discovery/discovery_api.md)
Repository information, server capabilities, system status.

**Operation Groups:**
- **[Repository Info](discovery/repository/repository_info.md)** - Server details, capabilities

### [Workflow API](workflow/workflow_api.md)
Process and task management for business workflows.

### [Model API](model/model_api.md)  
Content model introspection - types, aspects, properties.

### [Search SQL API](search_sql/search_sql_api.md)
SQL-based search for structured queries.

## 🔧 Global Models Reference

### Level 1 Models (`python_alfresco_api.models`)

```python
from python_alfresco_api.models import (
    BaseEntry,     # Base model for all entry types
    PagingInfo,    # Pagination information  
    ErrorResponse, # Error handling
    UserInfo,      # User information
    ContentInfo    # Content metadata
)
```

**BaseEntry** - Foundation for all Alfresco objects
```python
class BaseEntry(BaseModel):
    id: str                    # Unique identifier
    created_at: datetime       # Creation timestamp  
    modified_at: datetime      # Last modification
    # ... additional fields
```

**PagingInfo** - Pagination for list operations
```python
class PagingInfo(BaseModel):
    count: int           # Items in current page
    has_more_items: bool # More pages available
    total_items: int     # Total items available
    skip_count: int      # Items skipped
    max_items: int       # Max items per page
```

## 🚀 Quick Start Examples

### Basic Node Operations
```python
from python_alfresco_api import ClientFactory
from python_alfresco_api.clients.core.nodes.models import CreateNodeRequest
from python_alfresco_api.clients.core.models import NodeType

# Setup
factory = ClientFactory(base_url="http://localhost:8080")
client = factory.create_core_client()

# Get node
node = client.nodes.get("abc123-def456")

# Create folder
folder = client.nodes.create(
    parent_id="-my-",
    request=CreateNodeRequest(
        name="My Documents",
        node_type=NodeType.FOLDER,
        properties={"cm:title": "Document Collection"}
    )
)

# Async operations
node = await client.nodes.get_async("abc123-def456") 
```

### Search Operations
```python
# Search content
search_client = factory.create_search_client()
results = search_client.search("annual report")

# CMIS query
results = search_client.search(
    "SELECT * FROM cmis:document WHERE cmis:name LIKE '%report%'",
    language="cmis"
)
```

### Raw Client Access
```python
# Access raw httpx client when needed
raw_client = client._get_raw_client()
httpx_client = raw_client.get_httpx_client()

# Custom HTTP operations
response = httpx_client.get("/custom-endpoint")
```

## 🔗 Navigation

- **[API Reference Index](API_DOCUMENTATION_INDEX.md)** - Complete v1.0 documentation
- **[Authentication Guide](AUTHENTICATION_GUIDE.md)** - Setup and authentication  
- **[Installation Guide](INSTALLATION.md)** - Installation and configuration
- **[Examples](../examples/)** - Working code examples

## 📋 Features

- ✅ **Three-tier architecture** with perfect locality
- ✅ **Sync and async APIs** - use what fits your use case
- ✅ **Lazy loading** - 20x performance improvement
- ✅ **Rich Pydantic v2 models** - perfect for AI/LLM integration
- ✅ **Type safety** - full IDE support with auto-completion
- ✅ **Raw client access** - escape hatch for advanced operations
- ✅ **MCP compatibility** - optimized for Model Context Protocol servers 