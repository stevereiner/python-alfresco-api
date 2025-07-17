# V1.1 Request Types & Parameter Customization Guide

**Understanding Request Models, Body Parameters, and Advanced Customization in python-alfresco-api V1.1**

*📊 **V1.1 Achievement**: 46% code coverage with 100% test pass rate - comprehensive validation of GET operations, factory patterns, model imports, and MCP integration.*

## 🔍 Key Architecture Insights

### 1. "Detailed" Methods Explained

**IMPORTANT CLARIFICATION:** The "detailed" naming in our V1.1 architecture comes from the raw clients and refers to **HTTP Response details**, NOT more detailed content or parameters.

**The difference is in the return type:**

```python
# Non-detailed: Returns just the parsed content
result = client.nodes.create(parent_id, request)  # → NodeResponse
content = result.entry  # Direct access to Node data

# Detailed: Returns full HTTP Response with metadata  
response = client.nodes.create_detailed(parent_id, request)  # → Response[NodeEntry]
status = response.status_code  # 201
headers = response.headers    # {'Content-Type': 'application/json', ...}
content = response.parsed     # NodeEntry (if successful)
```

**When to Use Detailed:**
- MCP servers needing HTTP status validation
- Error handling requiring response headers
- Rate limiting based on response metadata
- Debugging API interactions

### 2. Four Method Patterns ✅

**All high-level methods map directly to raw client operations:**

```python
# Pattern mapping (confirmed working):
high-level sync           → raw_client.operation.sync()          # Returns: Optional[T]
high-level async          → raw_client.operation.asyncio()       # Returns: Optional[T]  
high-level detailed sync  → raw_client.operation.sync_detailed() # Returns: Response[T]
high-level detailed async → raw_client.operation.asyncio_detailed() # Returns: Response[T]
```

## 📝 Request Types Reference

### Core Node Operations

#### 1. CreateNodeRequest
**Purpose:** Create files, folders, and other content types

```python
from python_alfresco_api.clients.core.nodes.models import CreateNodeRequest, NodeType

# Simple folder creation
request = CreateNodeRequest(
    name="Project Documents",
    node_type=NodeType.FOLDER
)

# Advanced content creation with properties
request = CreateNodeRequest(
    name="annual-report-2024.pdf",
    node_type=NodeType.CONTENT,
    properties={
        "cm:title": "Annual Financial Report 2024",
        "cm:description": "Comprehensive financial analysis",
        "cm:author": "Finance Department",
        "custom:department": "Finance",
        "custom:confidentialityLevel": "Internal"
    },
    aspects=["cm:titled", "cm:author", "custom:confidential"],
    auto_rename=True,
    versioning_enabled=True,
    major_version=True
)

# Create the node
result = client.nodes.create(parent_id="-my-", request=request)
print(f"Created: {result.entry.name} with ID: {result.entry.id}")
```

**Available Fields:**
- `name` (required): Node display name
- `node_type` (required): `NodeType.CONTENT`, `NodeType.FOLDER`, etc.
- `properties` (optional): Custom metadata dictionary
- `aspects` (optional): List of aspect names to apply
- `auto_rename` (optional): Handle name conflicts automatically
- `versioning_enabled` (optional): Enable versioning for new content
- `major_version` (optional): Create as major (1.0) vs minor (0.1) version

#### 2. UpdateNodeRequest
**Purpose:** Modify existing node properties and metadata

```python
from python_alfresco_api.clients.core.nodes.models import UpdateNodeRequest

# Update node name and properties
request = UpdateNodeRequest(
    name="updated-filename.pdf",
    properties={
        "cm:title": "Updated Document Title",
        "cm:description": "Revised description",
        "custom:reviewStatus": "Approved",
        "custom:lastReviewDate": "2024-01-15"
    }
)

result = client.nodes.update(node_id="abc123", request=request)
```

**Available Fields:**
- `name` (optional): New node name
- `properties` (optional): Properties to update (merged with existing)

#### 3. CopyNodeRequest
**Purpose:** Copy nodes to different locations

```python
from python_alfresco_api.clients.core.nodes.models import CopyNodeRequest

request = CopyNodeRequest(
    target_parent_id="target-folder-456",
    name="copied-document.pdf"  # Optional: defaults to original name
)

result = client.nodes.copy(node_id="source-123", request=request)
```

#### 4. MoveNodeRequest
**Purpose:** Move nodes to different locations

```python
from python_alfresco_api.clients.core.nodes.models import MoveNodeRequest

request = MoveNodeRequest(
    target_parent_id="new-parent-789",
    name="moved-document.pdf"  # Optional: defaults to current name
)

result = client.nodes.move(node_id="node-123", request=request)
```

### Search API Operations

#### 1. SearchRequest (Raw Client Model)
**Purpose:** Advanced search operations with full Alfresco Search API power

```python
from python_alfresco_api.raw_clients.alfresco_search_client.search_client.models import SearchRequest, RequestQuery, RequestPagination, RequestQueryLanguage

# Simple text search
search_request = SearchRequest(
    query=RequestQuery(
        query="annual report",
        language=RequestQueryLanguage.AFTS  # Default: AFTS (Alfresco Full Text Search)
    )
)

# Advanced search with filters, facets, and pagination
search_request = SearchRequest(
    query=RequestQuery(
        query="TYPE:cm:content AND cm:title:*report*",
        language=RequestQueryLanguage.AFTS,
        user_query="annual report"  # Original user input
    ),
    paging=RequestPagination(
        max_items=50,
        skip_count=0
    ),
    fields=["id", "name", "cm:title", "cm:description", "content.size"],
    include=["properties", "path", "allowableOperations"],
    filter_queries=[
        {"query": "TYPE:'cm:content'"},
        {"query": "cm:creator:admin"},
        {"query": "content.size:[0 TO 1048576]"}  # Files under 1MB
    ],
    facet_fields={
        "facets": [
            {"field": "creator", "mincount": 1},
            {"field": "cm:modified", "mincount": 1}
        ]
    },
    sort=[
        {"type": "FIELD", "field": "cm:modified", "ascending": False}
    ]
)

# Execute search
result = client.search.search(body=search_request)
```

**Advanced SearchRequest Fields:**
- `query` (required): `RequestQuery` with search string and language
- `paging` (optional): `RequestPagination` for pagination control
- `fields` (optional): List of fields to return (saves bandwidth)
- `include` (optional): Additional node information (properties, path, etc.)
- `filter_queries` (optional): Constraints that don't affect scoring
- `facet_queries` (optional): Facet queries for result aggregation
- `facet_fields` (optional): Field-based faceting configuration
- `sort` (optional): Sorting specification
- `highlight` (optional): Search result highlighting
- `spellcheck` (optional): Spell checking configuration
- `scope` (optional): Search scope (nodes, versions, deleted-nodes)
- `defaults` (optional): Query defaults and operators
- `limits` (optional): Performance limits
- `localization` (optional): Locale and timezone settings
- `templates` (optional): Query expansion templates

#### 2. CMIS Search Example
**Purpose:** SQL-like queries using CMIS standard

```python
# CMIS query for structured searches
cmis_request = SearchRequest(
    query=RequestQuery(
        query="SELECT * FROM cmis:document WHERE cmis:contentStreamMimeType = 'application/pdf'",
        language=RequestQueryLanguage.CMIS
    ),
    paging=RequestPagination(max_items=25)
)

result = client.search.search(body=cmis_request)
```

#### 3. Faceted Search Example  
**Purpose:** Search with result categorization

```python
# Faceted search for analytics and filtering
faceted_request = SearchRequest(
    query=RequestQuery(query="presentation"),
    facet_queries=[
        {"query": "content.size:[0 TO 10240]", "label": "small"},
        {"query": "content.size:[10240 TO 102400]", "label": "medium"},
        {"query": "content.size:[102400 TO 1048576]", "label": "large"}
    ],
    facet_fields={
        "facets": [
            {"field": "creator", "mincount": 1},
            {"field": "cm:modified", "mincount": 1}
        ]
    }
)

result = client.search.search(body=faceted_request)
# Access facet results in result.context.facetQueries and result.context.facetFields
```

#### 4. Search with Highlighting
**Purpose:** Highlight matching terms in search results

```python
# Search with result highlighting
highlight_request = SearchRequest(
    query=RequestQuery(
        query="workflow",
        user_query="workflow"
    ),
    highlight={
        "prefix": "<mark>",
        "postfix": "</mark>",
        "mergeContiguous": True,
        "fields": [
            {"field": "cm:title"},
            {"field": "cm:description", "prefix": "**", "postfix": "**"}
        ]
    }
)

result = client.search.search(body=highlight_request)
# Access highlighting in result.entries[i].search.highlight
```

#### 5. Query Languages Reference

**Alfresco supports three query languages:**

**AFTS (Alfresco Full Text Search) - Default & Recommended:**
```python
# Text searches
"annual report"
"cm:title:budget AND cm:description:2024"

# Type and property searches  
"TYPE:cm:content AND cm:creator:admin"
"PATH:\"/app:company_home/cm:Budget/*\""

# Content searches
"TEXT:\"financial analysis\" AND TYPE:cm:content"
```

**CMIS (Content Management Interoperability Services):**
```python
# SQL-like syntax
"SELECT * FROM cmis:document WHERE cmis:name LIKE '%report%'"
"SELECT cmis:objectId, cmis:name FROM cmis:folder WHERE IN_FOLDER('workspace://SpacesStore/abc123')"
"SELECT * FROM cmis:document WHERE cmis:contentStreamMimeType = 'application/pdf'"
```

**Lucene (Advanced Users):**
```python
# Raw Lucene syntax
"cm\\:title:budget AND cm\\:creator:admin"
"+TYPE:cm\\:content +TEXT:report"
```

**When to Use Each:**
- **AFTS**: Most use cases, best performance, supports all Alfresco features
- **CMIS**: Standards compliance, integration with other CMIS systems
- **Lucene**: Advanced power users, complex query requirements

## 🛠️ Advanced Parameter Patterns

### 1. Using Raw Client Parameters Directly

**All current V1.1 methods support the same parameters as raw clients:**

```python
# High-level method with raw client parameters
result = client.nodes.list_children(
    node_id="-my-",
    skip_count=0,          # Pagination offset
    max_items=25,          # Page size  
    order_by="name ASC",   # Sorting
    where="isFile=true",   # Filtering
    include=["properties", "path", "allowableOperations"],  # Response enrichment
    fields=["id", "name", "nodeType", "isFile", "properties"]  # Field selection
)

# The parameters map directly to raw client:
# list_node_children.sync(client, node_id, skip_count, max_items, order_by, where, include, fields)
```

### 2. Properties Customization

**Properties accept any valid Alfresco metadata:**

```python
# Standard Alfresco properties
properties = {
    # Content Model properties
    "cm:title": "Document Title",
    "cm:description": "Document description", 
    "cm:author": "John Doe",
    "cm:created": "2024-01-15T10:30:00.000Z",
    
    # Custom model properties (if defined in Alfresco)
    "custom:projectCode": "PROJ-2024-001",
    "custom:department": "Engineering",
    "custom:confidentiality": "Internal",
    
    # System properties (read-only, don't set these)
    # "sys:node-uuid": "...",  # Don't set - system managed
    # "sys:store-identifier": "...",  # Don't set - system managed
}
```

### 3. Aspects Customization

**Apply multiple behaviors to nodes:**

```python
# Common aspects
aspects = [
    "cm:titled",           # Adds title/description fields
    "cm:author",           # Adds author field
    "cm:geographic",       # Adds latitude/longitude
    "cm:complianceable",   # Adds compliance metadata
    "custom:projectInfo",  # Custom aspect (if defined)
]

request = CreateNodeRequest(
    name="project-doc.pdf",
    node_type=NodeType.CONTENT,
    aspects=aspects,
    properties={
        "cm:title": "Project Documentation",
        "cm:author": "Project Manager",
        "cm:latitude": 40.7128,
        "cm:longitude": -74.0060,
        "custom:projectPhase": "Planning"
    }
)
```

### 4. Include Options for Response Enrichment

**Control what additional data is returned:**

```python
# Available include options
include_options = [
    "properties",           # Node properties/metadata
    "allowableOperations", # What operations user can perform
    "path",                # Full path from repository root
    "isLink",              # Whether node is a link
    "isFavorite",          # Whether user has favorited
    "aspectNames",         # Applied aspects
    "association",         # Association information
    "permissions",         # Detailed permissions
]

# Use in any GET operation
result = client.nodes.get(
    node_id="abc123",
    include=["properties", "path", "allowableOperations"]
)

# Rich response with full metadata
print(f"Path: {result.entry.path.name}")
print(f"Properties: {result.entry.properties}")
print(f"Can delete: {'delete' in result.entry.allowable_operations}")
```

## 🚫 Current Limitations & Workarounds

### 1. Raw Body Objects
**Limited Support:** V1.1 primarily uses typed request models, not raw body dicts.

```python
# ❌ Not supported (raw body dict)
body = {"name": "test", "nodeType": "cm:folder"}
# client.some_method(body=body)  # Won't work

# ✅ Supported (typed request)
request = CreateNodeRequest(name="test", node_type=NodeType.FOLDER)
result = client.nodes.create(parent_id="-my-", request=request)
```

**Workaround for Raw Bodies:**
```python
# Access raw client for maximum flexibility
raw_client = client.nodes._get_raw_client()

# Use raw operations directly
from python_alfresco_api.raw_clients.alfresco_core_client.core_client.api.nodes import create_node
from python_alfresco_api.raw_clients.alfresco_core_client.core_client.models import NodeBodyCreate

body = NodeBodyCreate.from_dict({
    "name": "test-folder", 
    "nodeType": "cm:folder",
    "properties": {"cm:title": "Custom Title"}
})

result = create_node.sync(client=raw_client, node_id="-my-", body=body)
```

### 2. Advanced Search Bodies
**Current Support:** Search requires raw client models for full power

```python
# ✅ Supported - basic search via raw client models
from python_alfresco_api.raw_clients.alfresco_search_client.search_client.models import SearchRequest, RequestQuery

search_request = SearchRequest(
    query=RequestQuery(query="annual report")
)
result = client.search.search(body=search_request)

# ❌ Not yet supported - high-level search request models
# Simple search_request = SimpleSearchRequest(text="annual report", content_types=["pdf"])
# Use raw client SearchRequest for all search operations
```

### 3. File Upload Bodies
**Current Support:** Limited to basic parameters

```python
# ✅ Supported - basic file upload parameters
result = client.content.upload_file(
    parent_id="-my-",
    file_name="document.pdf",
    content_type="application/pdf",
    file_data=file_bytes
)

# ❌ Not yet supported - advanced multipart options
# Advanced file upload with custom headers, multiple files, etc.
# Use raw client for these cases
```

## 🔧 Raw Client Access Patterns

**When high-level methods aren't enough:**

```python
# Pattern 1: Get raw client from any high-level client
raw_client = client.nodes._get_raw_client()

# Pattern 2: Direct HTTPx access for maximum control
httpx_client = client.nodes._get_raw_client().get_httpx_client()
response = httpx_client.post("/nodes/-my-/children", json={...})

# Pattern 3: Raw operation imports
from python_alfresco_api.raw_clients.alfresco_core_client.core_client.api.nodes import create_node
result = create_node.sync(client=raw_client, node_id="-my-", body=typed_body)

# Pattern 4: Search-specific raw client access
from python_alfresco_api.raw_clients.alfresco_search_client.search_client.api.search import search
from python_alfresco_api.raw_clients.alfresco_search_client.search_client.models import SearchRequest, RequestQuery

search_raw_client = client.search._get_raw_client()
search_request = SearchRequest(query=RequestQuery(query="TYPE:cm:content"))
result = search.sync(client=search_raw_client, body=search_request)
```

## 📚 Documentation Integration

- **[📖 Client Types Guide](CLIENT_TYPES_GUIDE.md)** - Choose the right client level
- **[🏗️ V1.1 Architecture](arch/V1_1_HIERARCHICAL_ARCHITECTURE.md)** - Understanding the structure  
- **[🎯 Examples](../examples/)** - Working code examples
- **[🧪 Tests](../tests/)** - See parameters in action

## 🚀 Recommended Patterns

### 1. Start with High-Level Methods
```python
# Use typed requests for safety and intellisense
request = CreateNodeRequest(name="doc.pdf", node_type=NodeType.CONTENT)
result = client.nodes.create(parent_id="-my-", request=request)
```

### 2. Add Parameters Gradually  
```python
# Add include/fields for richer responses
result = client.nodes.list_children(
    node_id="-my-",
    include=["properties", "allowableOperations"],
    fields=["id", "name", "properties", "isFile"]
)
```

### 3. Use Raw Models for Search
```python
# Search requires raw client models for full power
from python_alfresco_api.raw_clients.alfresco_search_client.search_client.models import SearchRequest, RequestQuery

search_request = SearchRequest(
    query=RequestQuery(query="TYPE:cm:content AND cm:title:*report*"),
    fields=["id", "name", "cm:title"]
)
result = client.search.search(body=search_request)
```

### 4. Use Raw Clients for Advanced Cases
```python
# When you need maximum control
raw_client = client.nodes._get_raw_client()
# Direct raw operations...
```

This architecture provides **three clear levels**: high-level convenience → typed requests → raw client control, allowing you to choose the right abstraction level for each use case. 