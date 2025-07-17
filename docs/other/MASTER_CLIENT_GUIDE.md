# Master Client Guide - Python Alfresco API v1.0

## Overview

The Master Client provides unified access to all 6 main Alfresco APIs through elegant dot syntax, making it the most convenient way to work with multiple Alfresco APIs in a single application.

## ✨ Elegant Dot Syntax vs Dictionary Access

### ✅ **Master Client (Recommended) - Elegant Dot Syntax**
```python
from python_alfresco_api import ClientFactory

factory = ClientFactory(base_url="http://localhost:8080", username="admin", password="admin")
master_client = factory.create_master_client()

# Clean, intuitive dot syntax
repo_info = master_client.discovery.get_repository_info()
nodes = master_client.core.get_nodes()
search_results = master_client.search.search(search_request)
ticket = master_client.auth.create_ticket({"userId": "admin", "password": "admin"})
processes = master_client.workflow.get_process_definitions()
models = master_client.model.get_models()
```

### ⚠️ **Dictionary Access (Less Elegant)**
```python
# Compare to dictionary access - more verbose and less intuitive
clients = factory.create_all_clients()

repo_info = clients['discovery'].get_repository_info()
nodes = clients['core'].get_nodes()
search_results = clients['search'].search(search_request)
ticket = clients['auth'].create_ticket({"userId": "admin", "password": "admin"})
processes = clients['workflow'].get_process_definitions()
models = clients['model'].get_models()
```

**Why Dot Syntax is Better:**
- 🎯 **More Intuitive**: `master_client.core.get_nodes()` reads like natural language
- 🚀 **Better IDE Support**: Auto-completion works perfectly with dot syntax
- 📝 **Cleaner Code**: No string literals or dictionary brackets
- 🔍 **Easier to Read**: Immediate understanding of what API is being used
- 🛡️ **Type Safety**: Better static analysis and linting support

## 🏗️ Master Client Architecture

```python
master_client = factory.create_master_client()

# All 6 main APIs available with dot syntax:
master_client.auth        # Authentication API
master_client.core        # Core Repository API  
master_client.discovery   # Discovery API
master_client.search      # Search API (AFTS and CMIS)
master_client.workflow    # Workflow API
master_client.model       # Model API
```

## 🚀 Quick Start

```python
from python_alfresco_api import ClientFactory

# Step 1: Create factory with authentication
factory = ClientFactory(
    base_url="http://localhost:8080",
    username="admin", 
    password="admin"
)

# Step 2: Create master client
master_client = factory.create_master_client()

# Step 3: Use any API with dot syntax
print(f"Repository: {master_client.discovery.get_repository_info().entry.repository.name}")
```

## 📚 Real-World Examples

### Example 1: Document Management Workflow
```python
# Complete document workflow with dot syntax
master = factory.create_master_client()

# 1. Get repository info
repo = master.discovery.get_repository_info()
print(f"Connected to {repo.entry.repository.name}")

# 2. Search for documents (AFTS)
search_request = {"query": {"query": "important document", "language": "afts"}}
results = master.search.search(search_request)

# 3. Work with found documents
for result in results.list.entries:
    node_id = result.entry.id
    
    # Get detailed node info
    node = master.core.get_node(node_id)
    
    # Check out for editing
    checkout = master.core.checkout_node(node_id)
    
    # Update properties
    master.core.update_node(node_id, {"properties": {"cm:title": "Updated Title"}})
    
    # Check back in
    master.core.checkin_node(node_id)
```

### Example 2: User and Site Management
```python
master = factory.create_master_client()

# Create authentication ticket
ticket = master.auth.create_ticket({"userId": "admin", "password": "admin"})

# Get all people
people = master.core.get_people()

# Get all sites  
sites = master.core.get_sites()

# Create new site
new_site = master.core.create_site({
    "title": "My New Site",
    "description": "Created via Master Client"
})

# Add members to site
for person in people.list.entries[:5]:  # First 5 people
    master.core.create_site_membership(
        new_site.entry.id, 
        {"id": person.entry.id, "role": "SiteConsumer"}
    )
```

### Example 3: Content Search and Analysis
```python
master = factory.create_master_client()

# AFTS Search
afts_results = master.search.search({
    "query": {"query": "TYPE:\"cm:content\"", "language": "afts"},
    "paging": {"maxItems": 100}
})

# CMIS Search (SQL-like queries)
cmis_results = master.search.search({
    "query": {
        "query": "SELECT * FROM cmis:document WHERE cmis:name LIKE 'project%'",
        "language": "cmis"
    },
    "paging": {"maxItems": 50}
})

# Process results
total_content = len(afts_results.list.entries)
cmis_matches = len(cmis_results.list.entries) if cmis_results else 0

print(f"Found {total_content} content items with AFTS")
print(f"CMIS search matched {cmis_matches} items")

# Get content models
models = master.model.get_models()
content_model = next((m for m in models.list.entries if m.entry.name == "cm:contentmodel"), None)

if content_model:
    # Get types in content model
    types = master.model.get_types()
    print(f"Available content types: {len(types.list.entries)}")
```

## 🎯 Benefits Summary

**Master Client with Dot Syntax Advantages:**

1. **🎯 Intuitive API**: `master.core.get_nodes()` vs `clients['core'].get_nodes()`
2. **🚀 Better IDE Support**: Full auto-completion and type hints
3. **📝 Cleaner Code**: No dictionary access or string literals
4. **🔍 Readable**: Immediate understanding of API being used
5. **🛡️ Type Safe**: Better static analysis and error detection
6. **⚡ Single Authentication**: All APIs share the same session
7. **🔧 Simplified Management**: One object for all API operations

## 💡 When to Use Master Client

**Perfect for:**
- ✅ Applications using multiple Alfresco APIs
- ✅ Interactive development and prototyping  
- ✅ Complex workflows spanning multiple APIs
- ✅ When you want the most elegant syntax

**Consider Individual Clients for:**
- 🎯 Applications using only 1-2 specific APIs
- 🎯 Microservices with focused responsibilities
- 🎯 When you want explicit API separation

**Always Use Factory Pattern:**
- ⚠️ Never create clients directly - always use ClientFactory
- ⚠️ Factory pattern ensures proper shared authentication
- ⚠️ Required for Alfresco's ticket-based authentication flow

## Complete API Reference

### 1. Authentication API

```python
# Option 1: Individual client
auth_client = factory.create_auth_client()
ticket = auth_client.create_ticket({"userId": "admin", "password": "admin"})

# Option 2: Master client with dot syntax
master_client = factory.create_master_client()
ticket = master_client.auth.create_ticket({"userId": "admin", "password": "admin"})
```

### 2. Core API - Content Management

```python
# Option 1: Individual client
core_client = factory.create_core_client()
nodes = core_client.get_nodes()
sites = core_client.get_sites()
people = core_client.get_people()

# Option 2: Master client with dot syntax
master_client = factory.create_master_client()
nodes = master_client.core.get_nodes()
sites = master_client.core.get_sites()
people = master_client.core.get_people()
```

**Available Core Operations**:
- ✅ Nodes API - File/folder operations
- ✅ Sites API - Site management
- ✅ People API - User management
- ✅ Groups API - Group management
- ✅ Actions API - Content actions
- ✅ Comments, Ratings, Tags, Favorites
- ✅ Versions, Renditions, Shared Links
- ✅ Downloads, Audit, Activities
- ✅ Preferences, Queries, Trashcan
- ✅ Probes, Networks

### 3. Discovery API

```python
# Option 1: Individual client
discovery_client = factory.create_discovery_client()
repo_info = discovery_client.get_repository_info()

# Option 2: Master client with dot syntax
master_client = factory.create_master_client()
repo_info = master_client.discovery.get_repository_info()

print(f"Alfresco version: {repo_info.entry.repository.version.major}.{repo_info.entry.repository.version.minor}")
```

### 4. Search API

The Search API supports both AFTS (Alfresco Full Text Search) and CMIS queries.

**AFTS Search (Recommended):**
```python
from python_alfresco_api.models.alfresco_search_models import SearchRequest

# AFTS search (full text)
afts_request = SearchRequest(
    query={
        "query": "test document",
        "language": "afts"
    },
    paging={
        "maxItems": 10,
        "skipCount": 0
    }
)

# Option 1: Individual client
search_client = factory.create_search_client()
results = search_client.search(afts_request)

# Option 2: Master client with dot syntax
master_client = factory.create_master_client()
results = master_client.search.search(afts_request)
```

**CMIS Search (SQL-like queries):**
```python
# CMIS search for structured queries
cmis_request = {
    "query": {
        "query": "SELECT * FROM cmis:document WHERE cmis:name LIKE 'test%'",
        "language": "cmis"
    },
    "paging": {
        "maxItems": 25,
        "skipCount": 0
    }
}

# Use the same search methods
results = master_client.search.search(cmis_request)
```

### 5. Workflow API

```python
# Option 1: Individual client
workflow_client = factory.create_workflow_client()
processes = workflow_client.get_process_definitions()
tasks = workflow_client.get_tasks()

# Option 2: Master client with dot syntax
master_client = factory.create_master_client()
processes = master_client.workflow.get_process_definitions()
tasks = master_client.workflow.get_tasks()
```

### 6. Model API

```python
# Option 1: Individual client
model_client = factory.create_model_client()
models = model_client.get_models()
types = model_client.get_types()
aspects = model_client.get_aspects()

# Option 2: Master client with dot syntax
master_client = factory.create_master_client()
models = master_client.model.get_models()
types = master_client.model.get_types()
aspects = master_client.model.get_aspects()
```



## Error Handling

### Comprehensive Error Handling

```python
from python_alfresco_api import ClientFactory

try:
    factory = ClientFactory(
        base_url="http://localhost:8080",
        username="admin",
        password="admin"
    )
    
    # Option 1: Test with individual clients
    all_clients = factory.create_all_clients()
    
    # Test each API
    apis_to_test = {
        'discovery': lambda: all_clients['discovery'].get_repository_info(),
        'search': lambda: all_clients['search'].search({"query": {"query": "*", "language": "afts"}}),
        'core': lambda: all_clients['core'].get_nodes(),
        'workflow': lambda: all_clients['workflow'].get_process_definitions(),
        'model': lambda: all_clients['model'].get_models()
    }
    
    results = {}
    for api_name, api_call in apis_to_test.items():
        try:
            result = api_call()
            results[api_name] = {"status": "success", "data": result}
        except Exception as e:
            results[api_name] = {"status": "error", "error": str(e)}
    
    print("API Test Results:")
    for api_name, result in results.items():
        status = "✅" if result["status"] == "success" else "❌"
        print(f"{status} {api_name.upper()}: {result['status']}")
        
except Exception as e:
    print(f"Failed to initialize clients: {e}")
```

## Type Safety with Pydantic Models

### Using Type-Safe Models WITH Clients

⚠️ **Important**: Pydantic models are standalone (not integrated with clients). Use them for validation, then convert to dictionaries for client calls.

```python
from python_alfresco_api import ClientFactory
from python_alfresco_api.models.alfresco_core_models import NodeBodyCreate
from python_alfresco_api.models.alfresco_search_models import SearchRequest

# Initialize clients
factory = ClientFactory(base_url="http://localhost:8080", username="admin", password="admin")
master_client = factory.create_master_client()

# ✅ CORRECT: Use Pydantic for validation, convert to dict for client
node_model = NodeBodyCreate(
    name="my-document.txt",
    nodeType="cm:content",
    properties={
        "cm:title": "My Document",
        "cm:description": "Created via Python API"
    }
)

# Convert to dictionary for client call
node_dict = node_model.model_dump()
# Execute with client (uses dictionary)
created_node = master_client.core.create_node("root-folder-id", node_dict)

# ✅ CORRECT: Type-safe search validation
search_model = SearchRequest(
    query={
        "query": "TYPE:'cm:content'",
        "language": "afts"
    },
    paging={
        "maxItems": 25,
        "skipCount": 0
    },
    filterQueries=[
        {"query": "ASPECT:'cm:titled'"}
    ]
)

# Convert to dictionary for client call
search_dict = search_model.model_dump()
# Execute with client (uses dictionary)
results = master_client.search.search(search_dict)

print(f"✅ Type-safe validation + client execution: {len(results.list.entries)} results")
```

### Pattern: Validation + Execution Function

```python
def create_content_with_validation(master_client, parent_id: str, name: str, title: str):
    """Create content with Pydantic validation then client execution"""
    
    # Step 1: Use Pydantic for type-safe validation
    try:
        node_model = NodeBodyCreate(
            name=name,
            nodeType="cm:content",
            properties={
                "cm:title": title,
                "cm:description": f"Created: {name}"
            }
        )
        print(f"✅ Validation passed for: {name}")
    except Exception as e:
        print(f"❌ Validation failed: {e}")
        return None
    
    # Step 2: Convert to dictionary and execute with client
    try:
        node_dict = node_model.model_dump()
        created_node = master_client.core.create_node(parent_id, node_dict)
        print(f"✅ Node created: {created_node.entry.id}")
        return created_node
    except Exception as e:
        print(f"❌ Creation failed: {e}")
        return None

# Usage with both individual clients and master client
def demo_type_safe_workflow():
    factory = ClientFactory(base_url="http://localhost:8080", username="admin", password="admin")
    
    # Option 1: Individual clients
    core_client = factory.create_core_client()
    search_client = factory.create_search_client()
    
    # Option 2: Master client (recommended)
    master_client = factory.create_master_client()
    
    # Create content with validation
    result = create_content_with_validation(
        master_client, 
        "root-folder-id", 
        "validated-document.txt", 
        "Type-Safe Document"
    )
    
    if result:
        # Search for the created content with validation
        search_model = SearchRequest(
            query={"query": f"cm:name:'{result.entry.name}'", "language": "afts"},
            paging={"maxItems": 5}
        )
        search_dict = search_model.model_dump()
        search_results = master_client.search.search(search_dict)
        
        print(f"✅ Found created document: {len(search_results.list.entries)} results")

# Execute the demo
demo_type_safe_workflow()
```

### AI/LLM Integration Pattern

```python
def ai_content_management():
    """Perfect pattern for AI/LLM integration with type safety"""
    
    factory = ClientFactory(base_url="http://localhost:8080", username="admin", password="admin")
    master_client = factory.create_master_client()
    
    # AI systems can work with Pydantic models for tool interfaces
    ai_request = {
        "action": "create_document",
        "name": "ai-generated-report.pdf",
        "title": "AI Analysis Report",
        "content_type": "application/pdf"
    }
    
    # Validate AI request with Pydantic
    node_model = NodeBodyCreate(
        name=ai_request["name"],
        nodeType="cm:content",
        properties={
            "cm:title": ai_request["title"],
            "cm:description": "Generated by AI system"
        }
    )
    
    # Convert to dict and execute with client
    node_dict = node_model.model_dump()
    # Client execution (dictionary-based)
    result = master_client.core.create_node("ai-folder-id", node_dict)
    
    # Return structured response for AI system
    return {
        "success": True,
        "node_id": result.entry.id,
        "name": result.entry.name,
        "created": result.entry.createdAt
    }

# This pattern is perfect for MCP servers and LLM tools
ai_result = ai_content_management()
print(f"AI created node: {ai_result}")
```

## Advanced Usage Patterns

### Pattern 1: Multi-API Workflow

```python
def content_management_workflow():
    """Complete content management workflow using multiple APIs"""
    
    factory = ClientFactory(
        base_url="http://localhost:8080",
        username="admin",
        password="admin"
    )
    
    master_client = factory.create_master_client()
    
    # 1. Get repository info
    repo_info = master_client.discovery.get_repository_info()
    print(f"Connected to Alfresco {repo_info.entry.repository.version.major}.{repo_info.entry.repository.version.minor}")
    
    # 2. List root nodes
    nodes = master_client.core.get_nodes()
    print(f"Found {len(nodes.list.entries)} root nodes")
    
    # 3. Search for content
    search_results = master_client.search.search({
        "query": {"query": "TYPE:'cm:content'", "language": "afts"},
        "paging": {"maxItems": 5}
    })
    print(f"Found {search_results.list.pagination.totalItems} content items")
    
    # 4. Get workflow processes
    processes = master_client.workflow.get_process_definitions()
    print(f"Available processes: {len(processes.data)}")
    
    return {
        "repository": repo_info,
        "nodes": nodes,
        "search_results": search_results,
        "processes": processes
    }

# Execute workflow
result = content_management_workflow()
```

### Pattern 2: Batch Operations

```python
def batch_content_operations():
    """Perform batch operations across multiple APIs"""
    
    factory = ClientFactory(
        base_url="http://localhost:8080",
        username="admin",
        password="admin"
    )
    
    all_clients = factory.create_all_clients()
    
    # Batch search across different content types
    content_types = ["cm:content", "cm:folder", "st:site"]
    search_results = {}
    
    for content_type in content_types:
        try:
            results = all_clients['search'].search({
                "query": {"query": f"TYPE:'{content_type}'", "language": "afts"},
                "paging": {"maxItems": 10}
            })
            search_results[content_type] = results.list.pagination.totalItems
        except Exception as e:
            search_results[content_type] = f"Error: {e}"
    
    return search_results

# Execute batch operations
batch_results = batch_content_operations()
print("Content Type Counts:", batch_results)
```

## Best Practices

### 1. Choose the Right ClientFactory Access Style

⚠️ **Important**: Both patterns use **ClientFactory** as the foundation. The choice is about **access style**, not different architectures.

**Use Individual Clients (via ClientFactory)**:
```python
factory = ClientFactory(base_url="...", username="...", password="...")
core_client = factory.create_core_client()      # Individual access
search_client = factory.create_search_client()  # Individual access
```
- ✅ You need individual control over each API client
- ✅ You want to pass different clients to different parts of your application  
- ✅ You're building a modular application with separation of concerns
- ✅ Enterprise applications with explicit API boundaries

**Use Master Client (via ClientFactory)**:
```python
factory = ClientFactory(base_url="...", username="...", password="...")
master_client = factory.create_master_client()  # Unified access
nodes = master_client.core.get_nodes()          # Dot syntax
```
- ✅ You want a simple, unified interface with dot syntax
- ✅ You're doing exploratory work or prototyping
- ✅ You need all APIs in a single object
- ✅ Rapid development and interactive use

**Both Patterns Provide**:
- ✅ Same ClientFactory authentication system
- ✅ Same shared session across all APIs  
- ✅ Same configuration management
- ✅ Same error handling capabilities

### 2. Error Handling

```python
def safe_api_call(api_function, *args, **kwargs):
    """Safely call any API function with error handling"""
    try:
        return {"success": True, "data": api_function(*args, **kwargs)}
    except Exception as e:
        return {"success": False, "error": str(e)}

# Usage with Master Client (recommended for this guide)
factory = ClientFactory(base_url="http://localhost:8080", username="admin", password="admin")
master_client = factory.create_master_client()
result = safe_api_call(master_client.core.get_nodes)
if result["success"]:
    nodes = result["data"]
else:
    print(f"Error getting nodes: {result['error']}")

# Alternative: Usage with individual clients
all_clients = factory.create_all_clients()
result = safe_api_call(all_clients['core'].get_nodes)  # Dictionary access
```

### 3. Configuration Management

```python
import os
from python_alfresco_api import ClientFactory

def create_configured_factory():
    """Create factory with environment-based configuration"""
    
    return ClientFactory(
        base_url=os.getenv("ALFRESCO_BASE_URL", "http://localhost:8080"),
        username=os.getenv("ALFRESCO_USERNAME", "admin"),
        password=os.getenv("ALFRESCO_PASSWORD", "admin"),
        verify_ssl=os.getenv("ALFRESCO_VERIFY_SSL", "true").lower() == "true"
    )

# Usage with Master Client (recommended for this guide)
factory = create_configured_factory()
master_client = factory.create_master_client()

# Alternative: Individual clients
clients = factory.create_all_clients()
```



## Complete Working Example

```python
#!/usr/bin/env python3
"""
Complete Master Client Example
Demonstrates all 6 main APIs working together with elegant dot syntax
"""

from python_alfresco_api import ClientFactory
from python_alfresco_api.models.alfresco_search_models import SearchRequest
import json

def main():
    # Initialize client factory
    factory = ClientFactory(
        base_url="http://localhost:8080",
        username="admin",
        password="admin"
    )
    
    try:
        # Create master client with dot syntax access
        master_client = factory.create_master_client()
        print("✅ Master client initialized successfully")
        
        # Test each API with elegant dot syntax
        print("\n🔍 Testing APIs with Master Client:")
        
        # 1. Discovery API
        repo_info = master_client.discovery.get_repository_info()
        print(f"✅ Discovery: Alfresco {repo_info.entry.repository.version.major}.{repo_info.entry.repository.version.minor}")
        
        # 2. Authentication API
        current_user = master_client.auth.get_current_user()
        print(f"✅ Auth: Connected as {current_user.entry.id}")
        
        # 3. Core API
        nodes = master_client.core.get_nodes()
        print(f"✅ Core: Found {len(nodes.list.entries)} root nodes")
        
        # 4. Search API (AFTS)
        search_request = SearchRequest(
            query={"query": "*", "language": "afts"},
            paging={"maxItems": 5}
        )
        search_results = master_client.search.search(search_request)
        print(f"✅ Search: Found {search_results.list.pagination.totalItems} total items")
        
        # CMIS Search example
        cmis_results = master_client.search.search({
            "query": {
                "query": "SELECT * FROM cmis:document",
                "language": "cmis"
            },
            "paging": {"maxItems": 3}
        })
        print(f"✅ CMIS Search: Found {len(cmis_results.list.entries)} documents")
        
        # 5. Workflow API
        processes = master_client.workflow.get_process_definitions()
        print(f"✅ Workflow: {len(processes.data)} process definitions available")
        
        # 6. Model API
        models = master_client.model.get_models()
        print(f"✅ Model: {len(models.list.entries)} content models")
        
        print("\n🎉 All 6 main APIs working perfectly with dot syntax!")
        
        # Demonstrate the elegant dot syntax advantage
        print("\n✨ Elegant Dot Syntax Examples:")
        print(f"Repository name: {master_client.discovery.get_repository_info().entry.repository.name}")
        print(f"Node count: {len(master_client.core.get_nodes().list.entries)}")
        print(f"Model count: {len(master_client.model.get_models().list.entries)}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
```

## Troubleshooting

### Common Issues

1. **Connection Issues**
   - Check base_url format: `http://localhost:8080` (server URL, not API endpoint)
   - Verify Alfresco is running
   - Check network connectivity

2. **Authentication Issues**
   - Verify username/password
   - Check user permissions
   - Review authentication logs

3. **API-Specific Issues**
   - Some APIs require specific Alfresco configurations
   - Search SQL requires Solr setup
   - Workflow requires process engine

### Getting Help

- **[Authentication Guide](AUTHENTICATION_GUIDE.md)** - Detailed auth setup
- **[API Documentation Index](API_DOCUMENTATION_INDEX.md)** - Complete API reference
- **[examples/](../examples/)** - Working code examples
- **[tests/](../tests/)** - Test cases and validation

## Summary

The Master Client provides powerful unified access to all main Alfresco APIs. Choose the ClientFactory pattern for modern applications, or use the Master Client for simpler use cases. Both patterns provide:

- ✅ **Complete API Coverage** - All 6 main APIs fully functional
- ✅ **Type Safety** - Pydantic v2 models for perfect IDE support
- ✅ **Error Handling** - Comprehensive exception management
- ✅ **Live Integration** - Tested with Alfresco Community 23.2.0 and 25.1
- ✅ **Production Ready** - ~78% test coverage, 106/106 tests passing

Start with the [Quick Start](#quick-start) section and explore the patterns that work best for your use case!
