# Python Alfresco API - Hybrid Architecture

The perfect Python client for Alfresco Content Services, built with the proven **hybrid approach**:

- **Pydantic v2 models** - Perfect for LLM integration & MCP servers
- **Professional HTTP clients** - Full async support with HTTPX
- **Individual clients** - Enterprise-ready modular architecture  
- **Factory pattern** - Easy configuration and instantiation

## Why Hybrid Architecture?

This library combines the best of both worlds:

| Feature | Benefit |
|---------|---------|
| **Pydantic Models** | Perfect for LLM tool interfaces, data validation, JSON serialization |
| **HTTP Clients** | Professional async/sync support, error handling, type safety |
| **Individual Clients** | Modular, enterprise-ready, microservice-friendly |
| **Factory Pattern** | Easy configuration, shared authentication, clean APIs |

## Quick Start

### Installation

```bash
pip install python-alfresco-api
```

### Basic Usage

```python
from python_alfresco_api import ClientFactory

# Create factory with authentication
factory = ClientFactory(
    base_url="https://alfresco.example.com",
    username="admin",
    password="admin123"
)

# Use individual clients
core_client = factory.create_core_client()
search_client = factory.create_search_client()

# Or create all clients at once
clients = factory.create_all_clients()
```

### LLM Integration with Pydantic Models

```python
from python_alfresco_api.models import TicketBody, NodeBody, SearchRequest

# Perfect for LLM tool interfaces
def create_document_tool(data: NodeBody) -> dict:
    """LLM tool for creating documents"""
    core_client = factory.create_core_client()
    return core_client.create_node(data)

def search_documents_tool(query: SearchRequest) -> dict:
    """LLM tool for searching documents"""
    search_client = factory.create_search_client()
    return search_client.search(query)
```

### MCP Server Integration

```python
# Perfect for Model Context Protocol servers
from mcp.server import Server
from python_alfresco_api import ClientFactory
from python_alfresco_api.models import *

server = Server("alfresco-mcp")

@server.tool("search_documents")
async def search_documents(query: str) -> dict:
    """Search Alfresco documents"""
    search_client = factory.create_search_client()
    return await search_client.search(query)
```

## Available APIs

- **Authentication API** - Login, logout, ticket management
- **Core API** - Nodes, sites, people, groups, activities
- **Discovery API** - Repository information and capabilities  
- **Search API** - Full-text search, faceted search, queries
- **Workflow API** - Process definitions, tasks, workflows
- **Model API** - Content models, types, aspects
- **Search SQL API** - SQL-like queries for content

## Architecture Benefits

### Individual Clients (Not Master Files)
```python
# Each client works independently
auth_client = AlfrescoAuthClient("https://alfresco.com")
core_client = AlfrescoCoreClient("https://alfresco.com")

# Perfect for microservices
document_service = AlfrescoCoreClient("https://docs.alfresco.com")
search_service = AlfrescoSearchClient("https://search.alfresco.com")
```

### Shared Authentication (Optional)
```python
# Shared auth across clients
auth = AuthUtil("https://alfresco.com", "admin", "admin123")
await auth.authenticate()

core_client = AlfrescoCoreClient("https://alfresco.com", auth)
search_client = AlfrescoSearchClient("https://alfresco.com", auth)
```

### Factory Pattern (Convenient)
```python
# Factory for easy setup
factory = ClientFactory("https://alfresco.com", "admin", "admin123")
clients = factory.create_all_clients()

# Use any client
clients['core'].get_node('node-id')
clients['search'].search('query')
```

## Generated with Proven Tools

This library is generated using industry-proven tools:

- **datamodel-code-generator** - Generates Pydantic v2 models
- **openapi-python-client** - Generates professional HTTP clients
- **Hybrid approach** - Combines the best of both worlds

## Enterprise Ready

- ✅ **Type Safety** - Full TypeScript-like type hints
- ✅ **Async Support** - Modern async/await patterns
- ✅ **Error Handling** - Comprehensive error management  
- ✅ **Authentication** - Ticket-based auth with auto-renewal
- ✅ **Documentation** - Auto-generated docs for all APIs
- ✅ **Testing** - Comprehensive test suite included

## Contributing

This project follows the proven patterns used by successful enterprise platforms like Unstructured.io, Swirl, and MindsDB.

## License

MIT License - see LICENSE file for details.
