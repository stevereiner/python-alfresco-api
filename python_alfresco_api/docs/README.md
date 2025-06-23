# Python Alfresco API

A modern, type-safe Python client for Alfresco Content Services REST API with full async support and Pydantic v2 models.

## Features

### 🚀 **Modern Python Architecture**
- **Type-safe**: Complete type hints with Pydantic v2 models
- **Async/Sync**: Full support for both async and synchronous operations
- **Individual Clients**: Separate clients for each API (Auth, Core, Search, etc.)
- **Factory Pattern**: Easy client instantiation and management

### 🔌 **Complete API Coverage**
- **Authentication API**: Login, logout, ticket management
- **Core API**: Nodes, sites, people, groups, permissions
- **Search API**: Full-text search with advanced queries
- **Discovery API**: Repository information and capabilities
- **Workflow API**: Process and task management
- **Model API**: Content model introspection
- **Search SQL API**: SQL-like queries for advanced search

### 🤖 **AI & LLM Ready**
- **Pydantic Models**: Perfect for LLM tool integration
- **MCP Server Ready**: Model Context Protocol support
- **Clean Interfaces**: Ideal for AI agent development

## Quick Start

### Installation

```bash
pip install python-alfresco-api
```

### Basic Usage

```python
from python_alfresco_api import ClientFactory

# Create client factory
factory = ClientFactory("http://localhost:8080")

# Create all clients
clients = factory.create_all_clients()

# Use individual clients
auth_client = clients["auth"]
core_client = clients["core"]
search_client = clients["search"]

# Check availability
print(f"Auth available: {auth_client.is_available()}")
print(f"Core available: {core_client.is_available()}")
```

### With Authentication

```python
from python_alfresco_api import ClientFactory, AuthUtil

# Create authenticated factory
auth_util = AuthUtil("http://localhost:8080", "admin", "admin")
factory = ClientFactory("http://localhost:8080", auth_util=auth_util)

# Create clients with authentication
clients = factory.create_all_clients()
```

## Configuration

### Environment Variables

```bash
export ALFRESCO_BASE_URL="http://localhost:8080"
export ALFRESCO_USERNAME="admin"
export ALFRESCO_PASSWORD="admin"
export ALFRESCO_VERIFY_SSL=false
```

### Direct Configuration

```python
from python_alfresco_api import ClientFactory

# Direct factory configuration
factory = ClientFactory(
    base_url="http://localhost:8080",
    username="admin",
    password="admin",
    verify_ssl=False
)
```

### Dev-Friendly Defaults

The library uses development-friendly defaults for local testing:
- `base_url`: "http://localhost:8080"
- `username`: "admin"
- `password`: "admin"
- `verify_ssl`: False

## API Examples

### Authentication

```python
from python_alfresco_api.clients.auth_client import AlfrescoAuthClient

auth_client = AlfrescoAuthClient("http://localhost:8080")

# Create ticket (login)
ticket_response = await auth_client.create_ticket("admin", "admin")
print(f"Ticket: {ticket_response.id}")

# Validate ticket
ticket_info = await auth_client.validate_ticket()
print(f"User: {ticket_info.userId}")

# Delete ticket (logout)
await auth_client.delete_ticket()
```

### Core API - Nodes

```python
from python_alfresco_api.clients.core_client import AlfrescoCoreClient

core_client = AlfrescoCoreClient("http://localhost:8080")

# Get root node
root_node = await core_client.get_node("-root-")
print(f"Root node: {root_node.name}")

# Get node children
children = await core_client.get_node_children("-root-")
for child in children.entries:
    print(f"Child: {child.entry.name}")

# Create folder
new_folder = await core_client.create_node(
    "-root-",
    {
        "name": "My Folder",
        "nodeType": "cm:folder"
    }
)
print(f"Created: {new_folder.id}")
```

### Search API

```python
from python_alfresco_api.clients.search_client import AlfrescoSearchClient

search_client = AlfrescoSearchClient("http://localhost:8080")

# Simple search
results = await search_client.search({
    "query": {
        "query": "test"
    }
})

for item in results.entries:
    print(f"Found: {item.entry.name}")

# Advanced search with filters
advanced_results = await search_client.search({
    "query": {
        "query": "TYPE:cm:content",
        "language": "afts"
    },
    "filterQueries": [
        {"query": "cm:modified:[NOW-7DAYS TO NOW]"}
    ],
    "sort": [
        {"field": "cm:modified", "ascending": False}
    ]
})
```

### Discovery API

```python
from python_alfresco_api.clients.discovery_client import AlfrescoDiscoveryClient

discovery_client = AlfrescoDiscoveryClient("http://localhost:8080")

# Get repository information
repo_info = await discovery_client.get_repository_info()
print(f"Version: {repo_info.version.display}")
print(f"Edition: {repo_info.edition}")
```

## Pydantic Models

All API responses use Pydantic v2 models for type safety:

```python
from python_alfresco_api.models import NodeEntry, PersonEntry, SearchResults

# Type-safe model access
node: NodeEntry = await core_client.get_node("some-id")
print(f"Node name: {node.name}")
print(f"Created: {node.createdAt}")
print(f"Content type: {node.content.mimeType}")

# Full IntelliSense support
person: PersonEntry = await core_client.get_person("admin")
print(f"Email: {person.email}")
print(f"First name: {person.firstName}")
```

## Error Handling

```python
from python_alfresco_api.exceptions import AlfrescoAPIError

try:
    node = await core_client.get_node("invalid-id")
except AlfrescoAPIError as e:
    print(f"API Error: {e.status_code} - {e.message}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Async vs Sync

All clients support both async and sync operations:

```python
# Async (recommended)
async def async_example():
    auth_client = AlfrescoAuthClient("http://localhost:8080")
    ticket = await auth_client.create_ticket("admin", "admin")
    return ticket

# Sync
def sync_example():
    auth_client = AlfrescoAuthClient("http://localhost:8080")
    ticket = auth_client.create_ticket_sync("admin", "admin")
    return ticket
```

## Event Integration

Integration with Alfresco Event Gateway (Enterprise) and ActiveMQ (Community):

```python
from python_alfresco_api.events import AlfrescoEventClient

# Auto-detects available event system
event_client = AlfrescoEventClient("http://localhost:8080")

# Create subscription
subscription = await event_client.create_subscription(
    name="node-events",
    events=["org.alfresco.event.node.Created"]
)

# Register event handler
@event_client.register_event_handler("org.alfresco.event.node.Created")
async def handle_node_created(event):
    print(f"Node created: {event.data.resource.name}")

# Start listening
await event_client.start_listening()
```

## Performance Tips

### Connection Pooling

```python
import aiohttp

# Use session for connection pooling
async with aiohttp.ClientSession() as session:
    factory = ClientFactory("http://localhost:8080", session=session)
    clients = factory.create_all_clients()
    
    # Multiple requests will reuse connections
    for i in range(100):
        node = await clients["core"].get_node(f"node-{i}")
```

### Batch Operations

```python
# Batch node creation
import asyncio

async def create_multiple_nodes():
    core_client = clients["core"]
    
    tasks = []
    for i in range(10):
        task = core_client.create_node("-root-", {
            "name": f"Node {i}",
            "nodeType": "cm:content"
        })
        tasks.append(task)
    
    # Execute in parallel
    results = await asyncio.gather(*tasks)
    return results
```

## LLM Integration

Perfect for AI and LLM tool integration:

```python
from typing import List
from python_alfresco_api.models import NodeEntry

def search_documents(query: str) -> List[NodeEntry]:
    """Search for documents - perfect as LLM tool"""
    search_client = AlfrescoSearchClient("http://localhost:8080")
    
    results = search_client.search_sync({
        "query": {"query": query}
    })
    
    return [entry.entry for entry in results.entries]

# Use with LangChain, CrewAI, etc.
from langchain.tools import Tool

alfresco_search_tool = Tool(
    name="alfresco_search",
    description="Search Alfresco repository for documents",
    func=search_documents
)
```

## MCP Server Example

```python
from mcp.server import Server
from python_alfresco_api import ClientFactory

app = Server("alfresco-mcp")
factory = ClientFactory("http://localhost:8080")
clients = factory.create_all_clients()

@app.tool("search_documents")
async def search_documents(query: str) -> str:
    """Search for documents in Alfresco"""
    results = await clients["search"].search({
        "query": {"query": query}
    })
    
    return f"Found {len(results.entries)} documents"

@app.tool("get_node_info")
async def get_node_info(node_id: str) -> dict:
    """Get detailed information about a node"""
    node = await clients["core"].get_node(node_id)
    
    return {
        "name": node.name,
        "type": node.nodeType,
        "created": node.createdAt.isoformat(),
        "modified": node.modifiedAt.isoformat()
    }
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Run the test suite: `python run_tests.py`
5. Submit a pull request

## License

Apache 2.0 - See [LICENSE](../LICENSE) for details.

## Support

- **Documentation**: [Full API Reference](API_REFERENCE.md)
- **Installation Guide**: [Installation Instructions](INSTALLATION.md)
- **GitHub Issues**: Report bugs and request features
- **Community**: Join discussions on GitHub

---

**Built for the modern Python ecosystem with async-first design and complete type safety.** 