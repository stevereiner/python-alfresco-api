# python-alfresco-api v1.0

**A Complete Python client package for developing python code and apps for Alfresco. Great for doing AI development 
with Python based LangChain, LlamaIndex, neo4j-graphrag, etc. Also great for creating MCP servers (see python-alfreso-mcp-server in this repository).**

Note this uses the remote Alfresco REST APIs. Not for in-process development in Alfresco.

A modern, type-safe Python client library for Alfresco Content Services REST APIs with comprehensive Pydantic v2 model integration and async support.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Pydantic](https://img.shields.io/badge/pydantic-v2-green.svg)](https://pydantic.dev/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Test Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](#testing)

## 🚀 Features

- **Complete API Coverage**: All 7 Alfresco REST APIs (Auth, Core, Discovery, Search, Workflow, Model, Search SQL)
- **1,400+ Pydantic v2 Models**: Type-safe data validation and serialization
- **Async/Sync Support**: Both synchronous and asynchronous API calls
- **Modular Architecture**: Individual client design for scalability
- **LLM/AI Ready**: Type-safe Pydantic v2 models perfect for AI integration and tool interfaces
- **Event System**: ActiveMQ and Event Gateway support for Python apps to handle change events 
- **Docker Compatible**: Works with Alfresco running in separate Docker Compose setups
- **Comprehensive Testing**: 100% unit and live Alfresco integration tests

## 📚 Documentation & Examples

- **[📖 Complete Documentation](docs/)** - Comprehensive guides and API documentation
- **[🎯 Working Examples](examples/)** - Live code examples and usage patterns
- **[🧪 Test Suite](tests/)** - Complete test coverage and integration examples

## 📦 Installation

### Virtual Environment Setup

**Recommended**: Always use a virtual environment to avoid dependency conflicts and leave base clean

#### Windows

```powershell
# Clone the repository
git clone https://github.com/stevereiner/python-alfresco-api.git
cd python-alfresco-api

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Verify activation (should show venv path)
where python

# Install dependencies
pip install -r requirements.txt

# For development (RECOMMENDED - includes mypy, black, pytest, etc.)
pip install -e .[dev]

# Deactivate when done
deactivate
```

#### Linux / MacOS

```bash
# Clone the repository
git clone https://github.com/stevereiner/python-alfresco-api.git
cd python-alfresco-api

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Verify activation (should show venv path)
which python

# Install dependencies
pip install -r requirements.txt

# For development (RECOMMENDED - includes mypy, black, pytest, etc.)
pip install -e .[dev]

# Deactivate when done
deactivate
```

#### Alternative: Using conda

```bash
# Create conda environment
conda create -n alfresco-api python=3.11
conda activate alfresco-api

# Install dependencies
pip install -r requirements.txt

# Deactivate when done
conda deactivate
```

### Runtime Installation

Install the package for production use:

```bash
pip install python-alfresco-api
```

This installs all features including event system support.

### Development Installation

For development, testing, or package regeneration:

```bash
# After setting up virtual environment above
git clone https://github.com/your-org/python-alfresco-api.git
cd python-alfresco-api

# Activate your virtual environment first
# Windows: venv\Scripts\activate
# Linux/macOS: source venv/bin/activate

# Install development dependencies (RECOMMENDED)
pip install -e .[dev]

# Or install in development mode
pip install -e .
```

## 🎯 Quick Start

### Basic Usage

```python
from python_alfresco_api import ClientFactory

# Create client factory
factory = ClientFactory(
    base_url="http://localhost:8080",
    username="admin",
    password="admin"
)

# Get all clients
clients = factory.create_all_clients()

# Use individual clients
auth_client = factory.create_auth_client()
core_client = factory.create_core_client()
search_client = factory.create_search_client()
```

### Async Usage

```python
import asyncio
from python_alfresco_api import ClientFactory

async def main():
    factory = ClientFactory(
        base_url="http://localhost:8080",
        username="admin",
        password="admin"
    )
    
    # Authenticate
    await factory.auth.authenticate()
    
    # Use authenticated API calls
    # Your async API operations here

asyncio.run(main())
```

### Architecture Options

#### Option 1: Individual Clients + Factory Pattern (Recommended)

```python
from python_alfresco_api import ClientFactory

# Factory pattern for easy configuration
factory = ClientFactory(
    base_url="http://localhost:8080",
    username="admin",
    password="admin"
)

# Individual clients for modular architecture
auth_client = factory.create_auth_client()
core_client = factory.create_core_client()
search_client = factory.create_search_client()
workflow_client = factory.create_workflow_client()
```

#### Option 2: Master Client Pattern (Unified Interface)

```python
from python_alfresco_api import ClientFactory

# Create factory
factory = ClientFactory(
    base_url="http://localhost:8080",
    username="admin",
    password="admin"
)

# Master client with dot syntax access
master_client = factory.create_master_client()

# Use dot syntax for API access
nodes = master_client.core.get_node("some-node-id")
results = master_client.search.search("my query")
ticket = master_client.auth.create_ticket()
processes = master_client.workflow.list_processes()
```

#### Option 3: Direct Individual Clients (No Factory)

```python
# Direct client creation without factory
from python_alfresco_api.clients import (
    AlfrescoAuthClient,
    AlfrescoCoreClient,
    AlfrescoSearchClient,
    AlfrescoWorkflowClient
)
from python_alfresco_api import AuthUtil

# Create auth utility
auth_util = AuthUtil(
    base_url="http://localhost:8080",
    username="admin",
    password="admin"
)

# Create individual clients directly
auth_client = AlfrescoAuthClient("http://localhost:8080")
core_client = AlfrescoCoreClient("http://localhost:8080", auth_util)
search_client = AlfrescoSearchClient("http://localhost:8080", auth_util)
```

All approaches provide:
- **Type Safety**: Full Pydantic v2 model integration
- **Async Support**: Modern async/await patterns
- **Authentication**: Automatic ticket-based auth with renewal
- **Error Handling**: Comprehensive error management

### Pydantic Models

```python
from python_alfresco_api.models.alfresco_core_models import NodeBodyCreate
from python_alfresco_api.models.alfresco_auth_models import TicketBody

# Type-safe model creation
node_data = NodeBodyCreate(
    name="my-document.txt",
    nodeType="cm:content",
    properties={"cm:title": "My Document"}
)

# Serialize to dict/JSON
node_dict = node_data.model_dump()
node_json = node_data.model_dump_json()

# Validation
ticket = TicketBody(userId="admin", password="admin")
```



## 🔧 Code Regeneration

The library uses OpenAPI 3.0 specifications for generating both Pydantic models and HTTP clients.
These were derived from alfresco swagger / openapi 2.0 yaml files, processed to clean (still openapi 2.0) and then
given to swagger2openapi to convert to openapi 3.0 .

### Prerequisites

Install development dependencies:

```bash
# RECOMMENDED - includes mypy, black, pytest, etc.
pip install -e .[dev]

# Alternative (may have missing dependencies)
pip install -r requirements-dev.txt
```

### Regeneration Steps

1. **Update OpenAPI Specifications**

   Download the latest specifications from [Alfresco API Explorer](https://api-explorer.alfresco.com/api-explorer/) and place them in:
   ```
   openapi/openapi2/alfresco-auth.yaml
   openapi/openapi2/alfresco-core.yaml
   openapi/openapi2/alfresco-discovery.yaml
   openapi/openapi2/alfresco-search.yaml
   openapi/openapi2/alfresco-workflow.yaml
   openapi/openapi2/alfresco-model.yaml
   openapi/openapi2/alfresco-search-sql.yaml
   ```

2. **Run the Generation Pipeline**

   ```bash
   python scripts/generate_hybrid_pipeline.py
   ```

   This script:
   - Processes and cleans the OpenAPI 2.0 specifications
   - Converts them to OpenAPI 3.0 format
   - Generates Pydantic v2 models from OpenAPI 3.0
   - Generates HTTP clients from OpenAPI 3.0
   - Creates the unified package structure

3. **Manual Steps (if needed)**

   Generate individual components:

   ```bash
   # Generate Pydantic models from OpenAPI 3.0
   datamodel-codegen \
     --input openapi/openapi3/alfresco-core.yaml \
     --output python_alfresco_api/models/alfresco_core_models.py \
     --target-python-version 3.8

   # Generate HTTP client from OpenAPI 3.0
   openapi-python-client generate \
     --path openapi/openapi3/alfresco-core.yaml \
     --config client_config.yaml
   ```

4. **Package Integration**

   The pipeline automatically:
   - Creates individual client wrappers
   - Sets up the ClientFactory
   - Configures AuthUtil integration
   - Establishes the unified package structure

### Generation Configuration

Configuration files for all Alfresco API clients are organized in the `config/` folder:

```
config/
├── auth.yaml          # Authentication API → auth_client
├── core.yaml          # Core Repository API → core_client  
├── discovery.yaml     # Discovery API → discovery_client
├── search.yaml        # Search API → search_client
├── workflow.yaml      # Workflow API → workflow_client
├── model.yaml         # Model API → model_client
├── search_sql.yaml    # Search SQL API → search_sql_client
├── general.yaml       # Unified package → alfresco_client
└── README.md          # Configuration documentation
```

**Example configuration** (`config/auth.yaml`):

```yaml
# Alfresco Auth API Client Configuration
class_overrides:
  "Error": "AuthError"
  "HTTPValidationError": "AuthValidationError"

project_name_override: "auth_client"
package_name_override: "auth_client"

field_constraints: true
use_annotated: true
```

**Usage**:

```bash
# Generate specific API client
openapi-python-client generate \
  --path openapi/openapi3/alfresco-auth.yaml \
  --config config/auth.yaml \
  --output-path clients/auth_client
```

**Note**: All generated package names use short, practical names instead of the default long names. See `config/README.md` for complete documentation and customization options.

## 🧪 Testing

### Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=python_alfresco_api --cov-report=html

# Run specific test suites
pytest tests/test_current_architecture.py
pytest tests/test_enhanced_coverage.py
```

### Live Integration Tests

To run tests against a live Alfresco server (tested with Community Edition 23.2.0 and Community Edition 25.1):

1. **Start Alfresco with Docker Compose**

   ```yaml
   # docker-compose.yml - Community Edition (tested with 23.2.0 and 25.1)
   version: '3.8'
   services:
     alfresco:
       image: alfresco/alfresco-content-repository-community:23.2.0
       # or: alfresco/alfresco-content-repository-community:25.1.0
       ports:
         - "8080:8080"
       environment:
         JAVA_OPTS: "-Xms1500m -Xmx1500m"
   ```

   ```bash
   docker-compose up -d
   ```

2. **Run Integration Tests**

   ```bash
   pytest tests/ -m integration
   ```

### Test Coverage

Current test coverage: **80%** of code lines tested with **106/106 tests passing** (100% success rate)

- **Core Components**: 80%+ test coverage
- **Pydantic Models**: 100% test coverage (1,400+ classes)  
- **Live Integration**: 100% functional validation (tested with Community Edition 23.2.0 and 25.1)
- **Individual Clients**: 81% test coverage each
- **Authentication**: 81% test coverage
- **Client Factory**: 94% test coverage
- **Master Client**: 70% test coverage

### Test Runner Script

Use the convenient test runner for professional output:

```bash
# From project root
python run_tests.py

# From tests directory  
cd tests && python ../run_tests.py
```

The test runner automatically detects your location and provides:
- Colored output and progress indicators
- Coverage reporting with visual display
- Live integration test status
- Performance metrics and timing
- Auto-adjusts working directory as needed

## 🔌 Event System

### ActiveMQ Integration (Community Edition)

```python
from python_alfresco_api.activemq_events import AlfrescoActiveMQEventClient

# Create event client
event_client = AlfrescoActiveMQEventClient(
    activemq_host="localhost",
    activemq_port=61616,
    username="admin",
    password="admin"
)

# Register event handler
async def node_created_handler(notification):
    print(f"Node created: {notification.nodeId}")

event_client.register_event_handler("alfresco.node.created", node_created_handler)

# Start listening
await event_client.connect()
await event_client.start_listening()
```

### Event Gateway (Enterprise Edition)

```python
from python_alfresco_api.event_client import AlfrescoEventClient

# Unified event client (auto-detects available systems)
event_client = AlfrescoEventClient()

# Works with both Community (ActiveMQ) and Enterprise (Event Gateway)
await event_client.create_subscription("node-events")
await event_client.start_listening()
```

## 🤖 MCP Server / LLM Integration ([see python-alfresco-mcp-server](https://github.com/stevereiner/python-alfresco-mcp-server))

Perfect for Model Context Protocol (MCP) servers with FastMCP 2.0 and type-safe Pydantic v2 models:

### FastMCP 2.0 Server Example

```python
from fastmcp import FastMCP
from python_alfresco_api import ClientFactory

# Create MCP server with FastMCP 2.0
mcp = FastMCP("Alfresco Content Management")

# Initialize Alfresco client
factory = ClientFactory(
    base_url="http://localhost:8080",
    username="admin", 
    password="admin"
)

@mcp.tool()
def search_documents(query: str) -> str:
    """Search for documents in Alfresco"""
    search_client = factory.create_search_client()
    results = search_client.search({
        "query": {"query": query, "language": "afts"},
        "paging": {"maxItems": 10}
    })
    return f"Found {results.list.pagination.totalItems} documents"

@mcp.tool()
def get_repository_info() -> str:
    """Get Alfresco repository information"""
    discovery_client = factory.create_discovery_client()
    info = discovery_client.get_repository_info()
    return f"Connected to {info.entry.repository.name} v{info.entry.repository.version.major}.{info.entry.repository.version.minor}"

if __name__ == "__main__":
    mcp.run()
```

### Master Client with FastMCP 2.0

```python
from fastmcp import FastMCP
from python_alfresco_api import ClientFactory

mcp = FastMCP("Alfresco Master Client")

# Use master client for dot syntax access
master = ClientFactory(
    base_url="http://localhost:8080",
    username="admin",
    password="admin"
).create_master_client()

@mcp.tool()
def list_root_nodes() -> str:
    """List root nodes in Alfresco"""
    nodes = master.core.get_nodes()
    return f"Found {len(nodes.list.entries)} root nodes"

@mcp.tool()  
def search_content(query: str) -> str:
    """Search content with master client"""
    results = master.search.search({
        "query": {"query": query, "language": "afts"}
    })
    return f"Search returned {results.list.pagination.totalItems} results"
```

## 📁 Project Structure

```
python-alfresco-api/
├── python_alfresco_api/
│   ├── __init__.py                 # Main exports
│   ├── auth_util.py               # Authentication utility
│   ├── client_factory.py          # Client factory pattern
│   ├── master_client.py           # Unified master client
│   ├── clients/                   # Individual API clients
│   │   ├── auth_client.py
│   │   ├── core_client.py
│   │   ├── discovery_client.py
│   │   ├── search_client.py
│   │   ├── workflow_client.py
│   │   ├── model_client.py
│   │   └── search_sql_client.py
│   ├── models/                    # Pydantic v2 models
│   │   ├── alfresco_auth_models.py
│   │   ├── alfresco_core_models.py
│   │   ├── alfresco_discovery_models.py
│   │   ├── alfresco_search_models.py
│   │   ├── alfresco_workflow_models.py
│   │   ├── alfresco_model_models.py
│   │   └── alfresco_search_sql_models.py
│   ├── raw_clients/               # Generated HTTP clients
│   └── events/                    # Event system (Community + Enterprise)
│       ├── __init__.py            # Event exports
│       ├── event_client.py        # Unified event client (AlfrescoEventClient)
│       └── models.py              # Event models (EventSubscription, EventNotification)
├── config/                        # OpenAPI client configurations
│   ├── auth.yaml                  # Auth API config → auth_client
│   ├── core.yaml                  # Core API config → core_client
│   ├── discovery.yaml             # Discovery API config → discovery_client
│   ├── search.yaml                # Search API config → search_client
│   ├── workflow.yaml              # Workflow API config → workflow_client
│   ├── model.yaml                 # Model API config → model_client
│   ├── search_sql.yaml            # Search SQL API config → search_sql_client
│   ├── general.yaml               # Unified config → alfresco_client
│   └── README.md                  # Configuration documentation
├── openapi/                       # OpenAPI specifications (checked in)
│   ├── openapi2/                  # Original OpenAPI 2.0 specs
│   ├── openapi2-processed/        # Cleaned OpenAPI 2.0 specs
│   └── openapi3/                  # Converted OpenAPI 3.0 specs
├── tests/                         # Comprehensive test suite
├── scripts/                       # Generation scripts
├── docs/                          # Documentation
├── examples/                      # Usage examples
├── requirements.txt               # Runtime dependencies
├── requirements-dev.txt           # Development dependencies
├── run_tests.py                   # Test runner with nice display
└── README.md                      # This file
```

## 🔄 Development Workflow

### Standard Development (No Regeneration Needed)

For most development work, you can develop directly without regenerating code:

```bash
git clone https://github.com/your-org/python-alfresco-api.git
cd python-alfresco-api

# Install with all development dependencies (RECOMMENDED)
pip install -e .[dev]
```

**All OpenAPI specifications are checked in** - you can develop immediately:
- `openapi/openapi2/` - Original specifications  
- `openapi/openapi2-processed/` - Processed specifications
- `openapi/openapi3/` - OpenAPI 3.0 specifications

### Development Tasks

```bash
# Run tests with nice display
python run_tests.py

# Run specific test suites
pytest tests/test_current_architecture.py
pytest tests/test_enhanced_coverage.py

# Format code
black python_alfresco_api/
isort python_alfresco_api/

# Type checking
mypy python_alfresco_api/
```

### Making Changes

1. **Modify existing code** - No regeneration needed
2. **Add new features** - Work with existing generated clients
3. **Update documentation** - Edit docs/ and examples/
4. **Add tests** - Extend the test suite

### Code Regeneration (Only When Needed)

**Only regenerate when updating OpenAPI specifications:**

```bash
# Update OpenAPI specs in openapi/openapi2/
# Then regenerate
python scripts/generate_hybrid_pipeline.py
```

## 📋 Requirements

### Runtime Requirements

- **Python**: 3.8+
- **pydantic**: >=2.0.0,<3.0.0
- **requests**: >=2.31.0
- **httpx**: >=0.24.0 (for async support)
- **aiohttp**: >=3.8.0 (for async HTTP)

### Optional Dependencies

- **stomp.py**: >=8.1.0 (for ActiveMQ events)
- **ujson**: >=5.7.0 (faster JSON parsing)
- **requests-oauthlib**: >=1.3.0 (OAuth support)

### Development Requirements

### Code Rebuild/Regeneration Requirements

- **datamodel-code-generator**: >=0.21.0
- **openapi-python-client**: >=0.15.0
- **pytest**: >=7.4.0
- **black**: >=23.0.0
- **mypy**: >=1.5.0

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests: `pytest`
5. Submit a pull request

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Issues**: [GitHub Issues](https://github.com/stevereiner/python-alfresco-api/issues)
- **Documentation**: [Project Documentation](docs/)
- **Examples**: [Usage Examples](examples/)

## 🔗 Related Projects

- **Model Context Protocol (MCP)**: [MCP Documentation](https://modelcontextprotocol.io/docs) - Standard for AI-data source integration
- **Alfresco Community Edition**: [Community Documentation](https://support.hyland.com/r/Alfresco/Alfresco-Content-Services-Community-Edition/25.1/Alfresco-Content-Services-Community-Edition/Introduction)
- **Alfresco Enterprise Edition**: [Enterprise Documentation](https://support.hyland.com/r/Alfresco/Alfresco-Content-Services/25.1/Alfresco-Content-Services/Introduction)
- **Pydantic**: [Type validation library](https://pydantic.dev/)
- **datamodel-code-generator**: [Pydantic model generator](https://github.com/koxudaxi/datamodel-code-generator)
- **openapi-python-client**: [HTTP client generator](https://github.com/openapi-generators/openapi-python-client)

## ⭐ Star History

If this project helps you, please consider giving it a star! ⭐

