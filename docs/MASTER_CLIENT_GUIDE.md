# Master Client Guide - Python Alfresco API v1.0

## Overview

The Master Client provides a unified interface to all 7 Alfresco APIs through a single client instance. This guide covers both the modern ClientFactory pattern (recommended) and the legacy Master Client pattern.

## Quick Start

### Modern ClientFactory Pattern (Recommended)

```python
from python_alfresco_api import ClientFactory

# Create client factory with authentication
factory = ClientFactory(
    base_url="http://localhost:8080",
    username="admin",
    password="admin"
)

# Get all clients at once
clients = factory.create_all_clients()

# Use individual APIs
repo_info = clients['discovery'].get_repository_info()
search_results = clients['search'].search({"query": {"query": "*", "language": "afts"}})
nodes = clients['core'].get_nodes()
```

### Legacy Master Client Pattern

```python
from python_alfresco_api import AlfrescoMasterClient

# Single unified client
master = AlfrescoMasterClient(
    base_url="http://localhost:8080",
    username="admin",
    password="admin"
)

# Access APIs through properties
repo_info = master.discovery.get_repository_info()
search_results = master.search.search({"query": {"query": "*", "language": "afts"}})
nodes = master.core.get_nodes()
```

## Complete API Reference

### 1. Authentication API

```python
# ClientFactory pattern
auth_client = factory.create_auth_client()
ticket = auth_client.create_ticket({"userId": "admin", "password": "admin"})

# Master client pattern
ticket = master.auth.create_ticket({"userId": "admin", "password": "admin"})
```

### 2. Core API - Content Management

```python
# ClientFactory pattern
core_client = factory.create_core_client()
nodes = core_client.get_nodes()
sites = core_client.get_sites()
people = core_client.get_people()

# Master client pattern
nodes = master.core.get_nodes()
sites = master.core.get_sites()
people = master.core.get_people()
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
# Get repository information
repo_info = clients['discovery'].get_repository_info()
# or
repo_info = master.discovery.get_repository_info()

print(f"Alfresco version: {repo_info.entry.repository.version.major}.{repo_info.entry.repository.version.minor}")
```

### 4. Search API

```python
from python_alfresco_api.models.alfresco_search_models import SearchRequest

# Type-safe search request
search_request = SearchRequest(
    query={
        "query": "test document",
        "language": "afts"
    },
    paging={
        "maxItems": 10,
        "skipCount": 0
    }
)

# Execute search
results = clients['search'].search(search_request)
# or
results = master.search.search(search_request)
```

### 5. Workflow API

```python
# Get process definitions
processes = clients['workflow'].get_process_definitions()
# or
processes = master.workflow.get_process_definitions()

# Get tasks
tasks = clients['workflow'].get_tasks()
# or
tasks = master.workflow.get_tasks()
```

### 6. Model API

```python
# Get content models
models = clients['model'].get_models()
# or
models = master.model.get_models()

# Get types and aspects
types = clients['model'].get_types()
aspects = clients['model'].get_aspects()
```

### 7. Search SQL API

```python
from python_alfresco_api.models.alfresco_search_sql_models import SQLSearchRequest

# SQL-based search
sql_request = SQLSearchRequest(
    stmt="SELECT * FROM alfresco WHERE CONTAINS('test')",
    locales=["en"],
    timezone="GMT"
)

results = clients['search_sql'].search(sql_request)
# or
results = master.search_sql.search(sql_request)
```

## Error Handling

### Comprehensive Error Handling

```python
from python_alfresco_api import ClientFactory
from python_alfresco_api.exceptions import AlfrescoAPIException

try:
    factory = ClientFactory(
        base_url="http://localhost:8080",
        username="admin",
        password="admin"
    )
    
    clients = factory.create_all_clients()
    
    # Test each API
    apis_to_test = {
        'auth': lambda: clients['auth'].get_current_user(),
        'discovery': lambda: clients['discovery'].get_repository_info(),
        'search': lambda: clients['search'].search({"query": {"query": "*", "language": "afts"}}),
        'core': lambda: clients['core'].get_nodes(),
        'workflow': lambda: clients['workflow'].get_process_definitions(),
        'model': lambda: clients['model'].get_models(),
        'search_sql': lambda: clients['search_sql'].search({"stmt": "SELECT * FROM alfresco LIMIT 1"})
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

### Using Type-Safe Models

```python
from python_alfresco_api.models.alfresco_core_models import NodeBodyCreate
from python_alfresco_api.models.alfresco_search_models import SearchRequest

# Type-safe node creation
node_data = NodeBodyCreate(
    name="my-document.txt",
    nodeType="cm:content",
    properties={
        "cm:title": "My Document",
        "cm:description": "Created via Python API"
    }
)

# Type-safe search
search_request = SearchRequest(
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

# Execute with type safety
results = clients['search'].search(search_request)
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
    
    clients = factory.create_all_clients()
    
    # 1. Get repository info
    repo_info = clients['discovery'].get_repository_info()
    print(f"Connected to Alfresco {repo_info.entry.repository.version.major}.{repo_info.entry.repository.version.minor}")
    
    # 2. List root nodes
    nodes = clients['core'].get_nodes()
    print(f"Found {len(nodes.list.entries)} root nodes")
    
    # 3. Search for content
    search_results = clients['search'].search({
        "query": {"query": "TYPE:'cm:content'", "language": "afts"},
        "paging": {"maxItems": 5}
    })
    print(f"Found {search_results.list.pagination.totalItems} content items")
    
    # 4. Get workflow processes
    processes = clients['workflow'].get_process_definitions()
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
    
    clients = factory.create_all_clients()
    
    # Batch search across different content types
    content_types = ["cm:content", "cm:folder", "st:site"]
    search_results = {}
    
    for content_type in content_types:
        try:
            results = clients['search'].search({
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

### 1. Choose the Right Pattern

**Use ClientFactory when**:
- You need individual control over each API client
- You want to pass different clients to different parts of your application
- You're building a modular application with separation of concerns

**Use Master Client when**:
- You want a simple, unified interface
- You're doing exploratory work or prototyping
- You need all APIs in a single object

### 2. Error Handling

```python
def safe_api_call(api_function, *args, **kwargs):
    """Safely call any API function with error handling"""
    try:
        return {"success": True, "data": api_function(*args, **kwargs)}
    except Exception as e:
        return {"success": False, "error": str(e)}

# Usage
result = safe_api_call(clients['core'].get_nodes)
if result["success"]:
    nodes = result["data"]
else:
    print(f"Error getting nodes: {result['error']}")
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

# Usage
factory = create_configured_factory()
clients = factory.create_all_clients()
```

## Migration Guide

### From Old Enhanced Generated to New Architecture

**Old Code (deprecated)**:
```python

client = AlfrescoClient(
    host="http://localhost:8080",
    username="admin",
    password="admin"
)

# Old bracket notation
if isinstance(client.core, dict) and 'actions' in client.core:
    actions = client.core['actions'].list_actions()
```

**New Code (python_alfresco_api)**:
```python
from python_alfresco_api import ClientFactory

factory = ClientFactory(
    base_url="http://localhost:8080",
    username="admin",
    password="admin"
)

clients = factory.create_all_clients()

# Modern attribute access
actions = clients['core'].get_actions()  # or appropriate method
```

## Complete Working Example

```python
#!/usr/bin/env python3
"""
Complete Master Client Example
Demonstrates all 7 APIs working together
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
        # Get all clients
        clients = factory.create_all_clients()
        print("✅ All clients initialized successfully")
        
        # Test each API
        print("\n🔍 Testing APIs:")
        
        # 1. Discovery API
        repo_info = clients['discovery'].get_repository_info()
        print(f"✅ Discovery: Alfresco {repo_info.entry.repository.version.major}.{repo_info.entry.repository.version.minor}")
        
        # 2. Authentication API
        current_user = clients['auth'].get_current_user()
        print(f"✅ Auth: Connected as {current_user.entry.id}")
        
        # 3. Core API
        nodes = clients['core'].get_nodes()
        print(f"✅ Core: Found {len(nodes.list.entries)} root nodes")
        
        # 4. Search API
        search_request = SearchRequest(
            query={"query": "*", "language": "afts"},
            paging={"maxItems": 5}
        )
        search_results = clients['search'].search(search_request)
        print(f"✅ Search: Found {search_results.list.pagination.totalItems} total items")
        
        # 5. Workflow API
        processes = clients['workflow'].get_process_definitions()
        print(f"✅ Workflow: {len(processes.data)} process definitions available")
        
        # 6. Model API
        models = clients['model'].get_models()
        print(f"✅ Model: {len(models.list.entries)} content models")
        
        # 7. Search SQL API
        sql_results = clients['search_sql'].search({
            "stmt": "SELECT * FROM alfresco LIMIT 1",
            "locales": ["en"]
        })
        print(f"✅ Search SQL: Query executed successfully")
        
        print("\n🎉 All APIs working perfectly!")
        
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

The Master Client provides powerful unified access to all Alfresco APIs. Choose the ClientFactory pattern for modern applications, or use the Master Client for simpler use cases. Both patterns provide:

- ✅ **Complete API Coverage** - All 7 APIs fully functional
- ✅ **Type Safety** - Pydantic v2 models for perfect IDE support
- ✅ **Error Handling** - Comprehensive exception management
- ✅ **Live Integration** - Tested with Alfresco Community 23.2.0 and 25.1
- ✅ **Production Ready** - 80% test coverage, 106/106 tests passing

Start with the [Quick Start](#quick-start) section and explore the patterns that work best for your use case!
