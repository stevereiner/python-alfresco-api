# Pydantic Models Guide - Python Alfresco API v1.0

The Python Alfresco API v1.0 provides comprehensive type-safe Pydantic v2 models for all 7 Alfresco APIs. This guide covers model usage, type safety, and integration patterns.

## 📋 Table of Contents

- [Model Overview](#model-overview)
- [Core API Models](#core-api-models)
- [Search API Models](#search-api-models)
- [Authentication Models](#authentication-models)
- [Type Safety Benefits](#type-safety-benefits)
- [AI/LLM Integration](#aillm-integration)
- [Advanced Usage](#advanced-usage)

## 🎯 Model Overview

### Available Model Sets

| API | Model Location | Key Models |
|-----|---------------|------------|
| **Core API** | `python_alfresco_api/models/alfresco_core_models.py` | `Node`, `NodeEntry`, `NodePaging`, `NodeBodyCreate` |
| **Search API** | `python_alfresco_api/models/alfresco_search_models.py` | `SearchRequest`, `ResultSetPaging`, `ResultNode` |
| **Auth API** | `python_alfresco_api/models/alfresco_auth_models.py` | `TicketBody`, `TicketEntry`, `ValidTicket` |
| **Discovery API** | `python_alfresco_api/models/alfresco_discovery_models.py` | `DiscoveryEntry`, `RepositoryInfo` |
| **Workflow API** | `python_alfresco_api/models/alfresco_workflow_models.py` | `ProcessDefinition`, `Task`, `Variable` |
| **Model API** | `python_alfresco_api/models/alfresco_model_models.py` | `CustomModel`, `CustomType`, `CustomAspect` |
| **Search SQL API** | `python_alfresco_api/models/alfresco_search_sql_models.py` | `SqlQuery`, `SqlResultSet` |

## 🏗️ Core API Models - Most Important

### Essential Imports

```python
from python_alfresco_api.models.alfresco_core_models import (
    Node,
    NodeEntry,
    NodePaging,
    NodeBodyCreate,
    NodeBodyUpdate,
    ContentInfo,
    UserInfo,
    PathInfo,
    PermissionsInfo
)
```

### Working with Master Client

```python
from python_alfresco_api import ClientFactory
from python_alfresco_api.models.alfresco_core_models import NodeBodyCreate

# Initialize client
factory = ClientFactory(
    base_url="http://localhost:8080",
    username="admin",
    password="admin"
)

clients = factory.create_all_clients()

# Get nodes with full type safety
nodes_response = clients['core'].get_nodes()
print(f"Found {len(nodes_response.list.entries)} root nodes")

# Access individual nodes
for node_entry in nodes_response.list.entries:
    node = node_entry.entry
    print(f"Node: {node.name} (Type: {node.nodeType})")
    print(f"  ID: {node.id}")
    print(f"  Created: {node.createdAt}")
    print(f"  Modified: {node.modifiedAt}")
    print(f"  Size: {node.content.sizeInBytes if node.content else 'N/A'}")
```

### Creating Content with Type Safety

```python
from python_alfresco_api.models.alfresco_core_models import NodeBodyCreate

# Type-safe node creation
new_node = NodeBodyCreate(
    name="my-document.txt",
    nodeType="cm:content",
    properties={
        "cm:title": "My Document",
        "cm:description": "Created via Python API with type safety"
    },
    aspectNames=["cm:titled", "cm:author"]
)

# Create the node (when create_node method is available)
# created_node = clients['core'].create_node(parent_id="-root-", node_body=new_node)
```

## 🔍 Search API Models

### Search Request Models

```python
from python_alfresco_api.models.alfresco_search_models import (
    SearchRequest,
    RequestQuery,
    RequestPaging,
    RequestFilterQuery,
    RequestSort,
    RequestHighlight
)

# Type-safe search request
search_request = SearchRequest(
    query=RequestQuery(
        query="TYPE:'cm:content' AND ASPECT:'cm:titled'",
        language="afts"
    ),
    paging=RequestPaging(
        maxItems=25,
        skipCount=0
    ),
    filterQueries=[
        RequestFilterQuery(
            query="ASPECT:'cm:author'"
        )
    ],
    sort=[
        RequestSort(
            field="cm:modified",
            ascending=False
        )
    ]
)

# Execute search with full type safety
search_results = clients['search'].search(search_request)

# Access results with type safety
for result_entry in search_results.list.entries:
    result_node = result_entry.entry
    print(f"Found: {result_node.name}")
    print(f"  Score: {result_node.search.score}")
    print(f"  Location: {result_node.location}")
```

## 🔐 Authentication Models

### Ticket Management

```python
from python_alfresco_api.models.alfresco_auth_models import (
    TicketBody,
    TicketEntry,
    ValidTicket
)

# Type-safe ticket creation
ticket_request = TicketBody(
    userId="admin",
    password="admin"
)

# Create ticket
ticket_response = clients['auth'].create_ticket(ticket_request)
ticket_id = ticket_response.entry.id

# Validate ticket
validation_response = clients['auth'].validate_ticket(ticket_id)
if validation_response.entry.id:
    print(f"Ticket {ticket_id} is valid")
```

## ✅ Type Safety Benefits

### 1. IDE Support and Autocomplete

```python
from python_alfresco_api.models.alfresco_core_models import Node

# Full IDE autocomplete and type hints
def process_node(node: Node):
    # IDE knows all available properties
    print(f"Node ID: {node.id}")
    print(f"Name: {node.name}")
    print(f"Type: {node.nodeType}")
    print(f"Created: {node.createdAt}")
    print(f"Modified: {node.modifiedAt}")
    
    # IDE knows content might be None
    if node.content:
        print(f"Size: {node.content.sizeInBytes}")
        print(f"MIME Type: {node.content.mimeType}")
    
    # IDE knows properties is a dict
    if node.properties:
        title = node.properties.get("cm:title")
        if title:
            print(f"Title: {title}")
```

### 2. Validation and Error Prevention

```python
from python_alfresco_api.models.alfresco_search_models import SearchRequest
from pydantic import ValidationError

try:
    # This will validate all fields
    search_request = SearchRequest(
        query={
            "query": "TYPE:'cm:content'",
            "language": "afts"
        },
        paging={
            "maxItems": 25,  # Must be positive integer
            "skipCount": 0   # Must be non-negative
        }
    )
    
    # Guaranteed to be valid when it reaches here
    results = clients['search'].search(search_request)
    
except ValidationError as e:
    print(f"Validation error: {e}")
    # Handle validation errors appropriately
```

### 3. JSON Serialization

```python
from python_alfresco_api.models.alfresco_core_models import NodeBodyCreate

# Create model
node_data = NodeBodyCreate(
    name="test-document.txt",
    nodeType="cm:content",
    properties={"cm:title": "Test Document"}
)

# Perfect JSON serialization
json_data = node_data.model_dump_json()
print(json_data)
# Output: {"name":"test-document.txt","nodeType":"cm:content","properties":{"cm:title":"Test Document"}}

# Deserialize back to model
recreated_node = NodeBodyCreate.model_validate_json(json_data)
```

## 🤖 AI/LLM Integration

### Perfect for AI Tools

```python
from python_alfresco_api.models.alfresco_core_models import NodeBodyCreate
from python_alfresco_api.models.alfresco_search_models import SearchRequest

def create_ai_content_tool(name: str, content_type: str, title: str, description: str) -> dict:
    """AI tool function for creating Alfresco content"""
    
    # Type-safe model creation
    node_data = NodeBodyCreate(
        name=name,
        nodeType=content_type,
        properties={
            "cm:title": title,
            "cm:description": description
        }
    )
    
    # Return serialized data for AI systems
    return node_data.model_dump()

def search_content_tool(query: str, max_items: int = 10) -> dict:
    """AI tool function for searching Alfresco content"""
    
    # Type-safe search request
    search_request = SearchRequest(
        query={"query": query, "language": "afts"},
        paging={"maxItems": max_items, "skipCount": 0}
    )
    
    return search_request.model_dump()

# Usage in AI applications
ai_node_data = create_ai_content_tool(
    name="ai-generated-report.pdf",
    content_type="cm:content", 
    title="AI Generated Report",
    description="Automatically generated report from AI analysis"
)

ai_search_data = search_content_tool(
    query="TYPE:'cm:content' AND ASPECT:'cm:titled'",
    max_items=20
)
```

### FastMCP 2.0 Integration

```python
from fastmcp import FastMCP
from python_alfresco_api import ClientFactory
from python_alfresco_api.models.alfresco_core_models import Node, NodeBodyCreate
from python_alfresco_api.models.alfresco_search_models import SearchRequest
import json

# Create FastMCP 2.0 server
mcp = FastMCP("Alfresco Content Manager")

# Initialize Alfresco clients
factory = ClientFactory(
    base_url="http://localhost:8080",
    username="admin",
    password="admin"
)
clients = factory.create_all_clients()

@mcp.tool()
def search_content(query: str, max_items: int = 10) -> str:
    """Search Alfresco content with type-safe models"""
    # Create type-safe search request
    search_request = SearchRequest(
        query={"query": query, "language": "afts"},
        paging={"maxItems": max_items, "skipCount": 0}
    )
    
    # Execute search
    results = clients['search'].search(search_request)
    
    # Return structured data for AI consumption
    return json.dumps({
        "total_items": results.list.pagination.totalItems,
        "results": [
            {
                "id": entry.entry.id,
                "name": entry.entry.name,
                "type": entry.entry.nodeType,
                "created": entry.entry.createdAt.isoformat() if entry.entry.createdAt else None,
                "modified": entry.entry.modifiedAt.isoformat() if entry.entry.modifiedAt else None,
                "size": entry.entry.content.sizeInBytes if entry.entry.content else None
            }
            for entry in results.list.entries
        ]
    })

@mcp.tool()
def create_content_spec(name: str, node_type: str, title: str, description: str = "") -> str:
    """Create type-safe content specification"""
    # Create validated model
    node_data = NodeBodyCreate(
        name=name,
        nodeType=node_type,
        properties={
            "cm:title": title,
            "cm:description": description
        }
    )
    
    # Return validated JSON for content creation
    return node_data.model_dump_json(indent=2)

@mcp.tool()
def get_node_info(node_id: str) -> str:
    """Get detailed node information with type safety"""
    try:
        # Get node (when available)
        # node_response = clients['core'].get_node(node_id)
        # node = node_response.entry
        
        # For demo, return structure
        return json.dumps({
            "message": "Node info requires get_node API endpoint",
            "node_id": node_id,
            "structure": {
                "id": "string",
                "name": "string", 
                "nodeType": "string",
                "properties": "dict",
                "content": {
                    "mimeType": "string",
                    "sizeInBytes": "number"
                }
            }
        }, indent=2)
        
    except Exception as e:
        return f"Error getting node info: {str(e)}"

if __name__ == "__main__":
    mcp.run()
```

## 🚀 Advanced Usage

### Model Composition

```python
from python_alfresco_api.models.alfresco_core_models import NodeBodyCreate
from python_alfresco_api.models.alfresco_search_models import SearchRequest
from typing import List, Optional

class ContentManager:
    """Advanced content management with type safety"""
    
    def __init__(self, clients):
        self.clients = clients
    
    def create_structured_content(
        self,
        base_name: str,
        content_items: List[dict],
        folder_properties: Optional[dict] = None
    ) -> List[NodeBodyCreate]:
        """Create multiple related content items"""
        
        nodes = []
        
        # Create folder
        folder_node = NodeBodyCreate(
            name=f"{base_name}-folder",
            nodeType="cm:folder",
            properties=folder_properties or {"cm:title": f"{base_name} Folder"}
        )
        nodes.append(folder_node)
        
        # Create content items
        for i, item in enumerate(content_items):
            content_node = NodeBodyCreate(
                name=f"{base_name}-{i+1}.txt",
                nodeType="cm:content",
                properties={
                    "cm:title": item.get("title", f"{base_name} Item {i+1}"),
                    "cm:description": item.get("description", "")
                }
            )
            nodes.append(content_node)
        
        return nodes
    
    def advanced_search(
        self,
        content_type: str,
        aspects: List[str],
        date_range: Optional[tuple] = None,
        max_items: int = 50
    ) -> SearchRequest:
        """Build complex search queries with type safety"""
        
        # Build query parts
        query_parts = [f"TYPE:'{content_type}'"]
        
        # Add aspect filters
        for aspect in aspects:
            query_parts.append(f"ASPECT:'{aspect}'")
        
        # Add date range if provided
        if date_range:
            start_date, end_date = date_range
            query_parts.append(f"cm:modified:[{start_date} TO {end_date}]")
        
        # Create type-safe search request
        search_request = SearchRequest(
            query={
                "query": " AND ".join(query_parts),
                "language": "afts"
            },
            paging={
                "maxItems": max_items,
                "skipCount": 0
            },
            sort=[
                {"field": "cm:modified", "ascending": False}
            ]
        )
        
        return search_request
```

### Error Handling with Models

```python
from python_alfresco_api.models.alfresco_core_models import Node
from pydantic import ValidationError
from typing import Optional

def safe_node_processing(node_data: dict) -> Optional[Node]:
    """Safely process node data with validation"""
    try:
        # Validate and create Node model
        node = Node.model_validate(node_data)
        
        # Process with type safety
        print(f"Processing node: {node.name}")
        print(f"Type: {node.nodeType}")
        
        if node.content:
            print(f"Content size: {node.content.sizeInBytes}")
        
        return node
        
    except ValidationError as e:
        print(f"Invalid node data: {e}")
        return None
    except Exception as e:
        print(f"Processing error: {e}")
        return None

# Usage
node_data = {"id": "123", "name": "test.txt", "nodeType": "cm:content"}
processed_node = safe_node_processing(node_data)
```

## 📝 Best Practices

### 1. Always Use Type Hints

```python
from python_alfresco_api.models.alfresco_core_models import Node, NodeEntry
from typing import List, Optional

def process_nodes(node_entries: List[NodeEntry]) -> List[str]:
    """Process node entries and return names"""
    return [entry.entry.name for entry in node_entries if entry.entry.name]

def get_node_title(node: Node) -> Optional[str]:
    """Safely get node title"""
    if node.properties:
        return node.properties.get("cm:title")
    return None
```

### 2. Validate External Data

```python
from python_alfresco_api.models.alfresco_search_models import SearchRequest
from pydantic import ValidationError

def create_search_from_user_input(user_query: str, max_items: str) -> Optional[SearchRequest]:
    """Create search request from user input with validation"""
    try:
        search_request = SearchRequest(
            query={"query": user_query, "language": "afts"},
            paging={"maxItems": int(max_items), "skipCount": 0}
        )
        return search_request
    except (ValidationError, ValueError) as e:
        print(f"Invalid search parameters: {e}")
        return None
```

### 3. Use Model Methods

```python
from python_alfresco_api.models.alfresco_core_models import NodeBodyCreate

# Create model
node_data = NodeBodyCreate(
    name="document.pdf",
    nodeType="cm:content",
    properties={"cm:title": "Important Document"}
)

# Use built-in methods
json_str = node_data.model_dump_json()          # Serialize to JSON
dict_data = node_data.model_dump()              # Convert to dict
copy_data = node_data.model_copy()              # Create a copy

# Validation
try:
    NodeBodyCreate.model_validate({"name": "test"})  # Will fail - missing required fields
except ValidationError as e:
    print("Validation failed:", e)
```

## 🎯 Summary

The Pydantic v2 models in Python Alfresco API v1.0 provide:

- ✅ **Complete Type Safety** - Full IDE support and error prevention
- ✅ **Perfect AI Integration** - Ideal for LLM tools and MCP servers  
- ✅ **Validation** - Automatic data validation and error handling
- ✅ **Serialization** - JSON serialization for API calls and storage
- ✅ **Documentation** - Self-documenting code with type hints
- ✅ **1,400+ Models** - Comprehensive coverage of all Alfresco APIs

Start with the Core API models for most use cases, then explore Search API models for advanced querying. The type safety ensures your code is robust and maintainable!

For more information:
- **[API Documentation Index](API_DOCUMENTATION_INDEX.md)** - Complete API reference
- **[Master Client Guide](MASTER_CLIENT_GUIDE.md)** - Using models with clients
- **[examples/llm_integration.py](../examples/llm_integration.py)** - AI integration examples 