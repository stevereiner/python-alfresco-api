# Python-Alfresco-API v1.1

**A Complete Python client package for developing python code and apps for Alfresco. Great for doing AI development 
with Python based LangChain, LlamaIndex, neo4j-graphrag, etc. Also great for creating MCP servers (see [python-alfresco-mcp-server](https://github.com/stevereiner/python-alfresco-mcp-server)).**

Note this uses the remote Alfresco REST APIs. Not for in-process development in Alfresco.

A modern, type-safe Python client library for Alfresco Content Services REST APIs with dual model architecture (attrs + Pydantic) and async support.

[![PyPI version](https://img.shields.io/pypi/v/python-alfresco-api.svg)](https://pypi.org/project/python-alfresco-api/)
[![PyPI downloads](https://pepy.tech/badge/python-alfresco-api)](https://pepy.tech/project/python-alfresco-api)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Pydantic](https://img.shields.io/badge/pydantic-v2-green.svg)](https://pydantic.dev/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

## 🚀 Features

- **Complete API Coverage**: All 7 Alfresco REST APIs (Auth, Core, Discovery, Search, Workflow, Model, Search SQL)
- **328+ Complete Domain Models**: attrs-based raw client models with separate Pydantic models available for AI integration
- **Model Conversion Utilities**: Bridge utilities for attrs ↔ Pydantic transformation when needed
- **Async/Sync Support**: Both synchronous and asynchronous API calls
- **Modular Architecture**: Individual client design for scalability
- **AI/LLM Ready**: Pydantic models available for AI integration, MCP servers, and tool interfaces
- **Event System**: ActiveMQ and Event Gateway support for Python apps to handle change events 
- **Docker Compatible**: Works with Alfresco running in separate Docker Compose setups
- **Comprehensive Testing**: Extensive unit and live Alfresco integration tests

## 📚 Documentation & Examples

- **[🏗️ Architecture Overview and Diagram](docs/ARCH_DIAGRAM_AND_OVERVIEW.md)** - V1.1 hierarchical architecture with visual diagram
- **[📖 Complete Documentation](docs/)** - Comprehensive guides and API documentation
- **[🎯 Working Examples](examples/)** - Live code examples and usage patterns
- **[🧪 Test Suite](tests/)** - Complete test coverage and integration examples

## 🤖 MCP Server / LLM Integration 

### See [python-alfresco-mcp-server](https://github.com/stevereiner/python-alfresco-mcp-server)
This is a MCP Server that uses Python Alfresco API

## 📦 Installation

### Quick Install from PyPI

[![PyPI](https://img.shields.io/pypi/v/python-alfresco-api.svg)](https://pypi.org/project/python-alfresco-api/)

```bash
pip install python-alfresco-api
```
- **Requres**: Python: 3.10+
- **All features included** - No optional dependencies needed! Includes event system, async support, and all 7 Alfresco APIs.

### Virtual Environment Setup (Recommended)

**Best Practice**: Always use a virtual environment to avoid dependency conflicts

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

# Deactivate when done
deactivate
```


### Package Installation

Install the package form PyPI use:

```bash
pip install python-alfresco-api
```


### Development with source

For development of your project using python-alfresco-api to have debugging with source:

```bash
# After setting up virtual environment above
git clone https://github.com/your-org/python-alfresco-api.git
cd python-alfresco-api

# Activate your virtual environment first
# Windows: venv\Scripts\activate
# Linux/macOS: source venv/bin/activate

# Install in development mode
pip install -e .
```

## Alfresco Installation 

If you don't have an Alfresco server installed you can get a docker for the 
Community version from Github
   ```bash
   git clone https://github.com/Alfresco/acs-deployment.git
```
**Start Alfresco with Docker Compose**
   ```bash
   cd acs-deployment/docker-compose
```
   Note: you will likely need to comment out activemq ports other than 8161
   in community-compose.yaml
   ```bash   
      ports:
      - "8161:8161" # Web Console
      #- "5672:5672" # AMQP
      #- "61616:61616" # OpenWire
      #- "61613:61613" # STOMP

    docker-compose -f community-compose.yaml up
```

## 🎯 Environment Setup

### Environment Configuration (Recommended)

For easy configuration, copy the sample environment file:
```bash
cp sample-dot-env.txt .env
# Edit .env with your Alfresco settings
```

## Factory Pattern 

The factory pattern provides shared authentication and centralized configuration:

```python
from python_alfresco_api import ClientFactory

# Automatic configuration (loads from .env file or environment variables)
factory = ClientFactory()  # Uses ALFRESCO_URL, ALFRESCO_USERNAME, etc.

# Or explicit configuration
factory = ClientFactory(
    base_url="http://localhost:8080",
    username="admin",
    password="admin"
)

# Create individual clients (all share same authentication session)
auth_client = factory.create_auth_client()
core_client = factory.create_core_client()
search_client = factory.create_search_client()
workflow_client = factory.create_workflow_client()
discovery_client = factory.create_discovery_client()
model_client = factory.create_model_client()
search_sql_client = factory.create_search_sql_client()  # SOLR admin only

# Can also use a master client like setup with all clients initialized
master_client = factory.create_master_client()

```


### Authentication

For standard Alfresco authentication (recommended):

```python
from python_alfresco_api import AuthUtil, ClientFactory

# Primary authentication pattern - Basic Auth with Alfresco
auth_util = AuthUtil(
    base_url="http://localhost:8080",
    username="admin",
    password="admin"
)

# Use with factory for shared authentication
factory = ClientFactory(auth_util=auth_util)
clients = factory.create_all_clients()
```

**Alternative Authentication:**
- `OAuth2AuthUtil` is available for enterprise OAuth2-based authentication but has not been live tested

### Sync and Async Usage

```python
import asyncio
from python_alfresco_api import ClientFactory

async def main():
    factory = ClientFactory(
        base_url="http://localhost:8080",
        username="admin",
        password="admin"
    )
    
    # Create core client for node operations
    core_client = factory.create_core_client()
    
    # Sync node operation
    sync_node = core_client.get_node("-my-")
    print(f"Sync: User folder '{sync_node.entry.name}'")
    
    # Async node operation
    async_node = await core_client.get_node_async("-my-")
    print(f"Async: User folder '{async_node.entry.name}'")

# Run the async example
asyncio.run(main())
```

## 🎯 Key Operations & Examples

### Essential Operation Samples

Quick examples of the most common operations. **👉 For complete coverage, see [📖 Essential Operations Guide](docs/ESSENTIAL_OPERATIONS_GUIDE.md)**

#### Basic Setup
```python
from python_alfresco_api import ClientFactory
from python_alfresco_api.utils import content_utils_highlevel

factory = ClientFactory(base_url="http://localhost:8080", username="admin", password="admin")
core_client = factory.create_core_client()
```

#### Create Folder & Upload Document
```python
# Create folder (High-Level Utility)
folder_result = content_utils_highlevel.create_folder_highlevel(
    core_client=core_client,
    name="My Project Folder", 
    parent_id="-my-"
)

# Upload document with auto-versioning
document_result = content_utils_highlevel.create_and_upload_file_highlevel(
    core_client=core_client,
    file_path="/path/to/document.pdf",
    parent_id=folder_result['id']
)
```

#### Search Content
```python
from python_alfresco_api.utils import search_utils

search_client = factory.create_search_client()

# Simple text search (already optimized!)
results = search_utils.simple_search(
    search_client=search_client,
    query_str="finance AND reports",
    max_items=25
)
```

#### Download Document
```python
# Download document content
content_response = core_client.nodes.get_content(node_id=document_id)

# Save to file
with open("downloaded_document.pdf", "wb") as file:
    file.write(content_response.content)
```

#### Get & Set Properties
```python
from python_alfresco_api.utils import content_utils_highlevel

# Get node properties and details
node_info = content_utils_highlevel.get_node_info_highlevel(
    core_client=core_client,
    node_id=document_id
)
print(f"Title: {node_info.get('properties', {}).get('cm:title', 'No title')}")

# Update node properties
update_request = {
    "properties": {
        "cm:title": "Updated Document Title",
        "cm:description": "Updated via Python API"
    }
}
updated_node = core_client.nodes.update(node_id=document_id, request=update_request)
```

#### Document Versioning - Checkout & Checkin
```python
from python_alfresco_api.utils import version_utils_highlevel

# Checkout document (lock for editing)
checkout_result = version_utils_highlevel.checkout_document_highlevel(
    core_client=core_client,
    node_id=document_id
)

# Later: Checkin with updated content (create new version)
checkin_result = version_utils_highlevel.checkin_document_highlevel(
    core_client=core_client,
    node_id=document_id,
    content="Updated document content",
    comment="Fixed formatting and added new section"
)
```

### 📚 Complete Documentation & Examples

| Resource | Purpose | What You'll Find |
|----------|---------|------------------|
| **[📖 Essential Operations Guide](docs/ESSENTIAL_OPERATIONS_GUIDE.md)** | **Complete operation coverage** | All operations with both high-level utilities and V1.1 APIs |
| **[📁 examples/operations/](examples/operations/)** | **Copy-paste examples** | Windows-compatible, production-ready code |
| **[🧪 tests/test_mcp_v11_true_high_level_apis_fixed.py](tests/test_mcp_v11_true_high_level_apis_fixed.py)** | **MCP Server patterns** | 15 operations with sync/async patterns |
| **[🧪 tests/test_highlevel_utils.py](tests/test_highlevel_utils.py)** | **High-level utilities testing** | Real Alfresco integration examples |

#### 🎯 Production-Ready Examples (examples/operations/)

| Example File | Key Operations |
|--------------|----------------|
| **[upload_document.py](examples/operations/upload_document.py)** | Document upload, automatic versioning, batch uploads |
| **[versioning_workflow.py](examples/operations/versioning_workflow.py)** | Checkout → Edit → Checkin workflow, version history |
| **[basic_operations.py](examples/operations/basic_operations.py)** | Folder creation, CRUD operations, browsing, deletion |
| **[search_operations.py](examples/operations/search_operations.py)** | Content search, metadata queries, advanced search |



### 🔄 Model Architecture & Conversion (V1.1)

V1.1 implements a dual model system with conversion utilities:

| Component | Model Type | Purpose |
|-----------|------------|---------|
| **Raw Client Models** | `@_attrs_define` | Complete OpenAPI domain models (`RepositoryInfo`, `NodeEntry`, etc.) |
| **Pydantic Models** | `BaseModel` | AI/LLM integration, validation, type safety |
| **Conversion Utils** | Bridge utilities | Transformation between attrs ↔ Pydantic |

**For detailed guidance**, see **[📖 Pydantic Models Guide](docs/PYDANTIC_MODELS_GUIDE.md)** and **[🔄 Conversion Utilities Design](docs/CONVERSION_UTILITIES_DESIGN.md)**.

```python
# ✅ V1.1: Two model systems with conversion utilities
from python_alfresco_api.models.alfresco_core_models import NodeBodyCreate  # Pydantic
from python_alfresco_api.raw_clients.alfresco_core_client.models import NodeBodyCreate as AttrsNodeBodyCreate  # attrs
from python_alfresco_api.clients.conversion_utils import pydantic_to_attrs_dict

# 1. Use Pydantic for validation and AI integration
pydantic_model = NodeBodyCreate(name="document.pdf", nodeType="cm:content")

# 2. Convert for raw client usage  
factory = ClientFactory()
core_client = factory.create_core_client()

# Option A: Manual conversion via model_dump()
result = core_client.create_node(pydantic_model.model_dump())

# Option B: Conversion utilities (V1.1)
attrs_dict = pydantic_to_attrs_dict(pydantic_model, target_class_name="NodeBodyCreate") 
result = core_client.create_node(attrs_dict)

# 3. Raw clients return attrs-based domain models
repository_info = discovery_client.get_repository_information()  # Returns attrs RepositoryInfo
# Convert to dict for further processing
repo_dict = repository_info.to_dict()
```

### V1.2 Roadmap: Unified Pydantic Architecture

V1.2 will migrate raw client models from attrs to Pydantic v2:

```python
# 🎯 V1.2 Target: Single Pydantic model system
from python_alfresco_api.raw_clients.alfresco_core_client.models import NodeBodyCreate  # Will be Pydantic!

# No conversion needed - everything is Pydantic BaseModel
pydantic_model = NodeBodyCreate(name="document.pdf", nodeType="cm:content")
result = core_client.create_node(pydantic_model)  # Direct usage!
```

**Notes**
- V1.1: Dual system with conversion utilities
- Pydantic models: Available for AI/LLM integration and validation  
- Raw client models: attrs-based with 328+ complete domain models
- V1.2: Will unify to Pydantic v2 throughout


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


## 🔧 For Developing the Python Alfresco API Package

For complete development documentation including the **3-step generation process** (Pydantic models → HTTP clients → High-level APIs), see **[📖 Package Developers Guide](docs/PACKAGE_DEVELOPERS_GUIDE.md)**.


## 🧪 Development and Testing

### Development Setup

For development, testing, and contributing:

```bash
pip install -r requirements-dev.txt
```

For most development work on python-alfresco-api, you can develop directly without regenerating code:

```bash
git clone https://github.com/stevereiner/python-alfresco-api.git
cd python-alfresco-api

# Install in development mode
pip install -e .
```

> **Note**: For proper pytest execution, work from the source directory with `pip install -e .` rather than testing from separate directories. This avoids import path conflicts.

### Run Tests

```bash
cd python-alfresco-api

# Simple - just run all tests pytest
pytest

# Run all tests with coverage
pytest --cov=python_alfresco_api --cov-report=html

# Custom test runner with additional features
python run_tests.py
# Features:
# - Environment validation (venv, dependencies)
# - Colored output with progress tracking
# - Test selection for 44%+ coverage baseline
# - Performance metrics (client creation speed)
# - Live Alfresco server detection
# - HTML coverage reports (htmlcov/index.html)
# - Test summary with next steps
```

### Live Integration Tests

To run tests against a live Alfresco server 
(Note: This package was developed and tested with Community Edition)

   ```bash

   # Run one test (test live with Alfresco)
   pytest tests/test_mcp_v11_true_high_level_apis_fixed.py -v
 
   ```

## 🔄 Project Structure

```
python-alfresco-api/
├── python_alfresco_api/
│   ├── __init__.py                 # Main exports
│   ├── auth_util.py               # Authentication utility
│   ├── client_factory.py          # Client factory pattern
│   ├── clients/                   # Individual API clients + utilities
│   │   ├── auth_client.py
│   │   ├── core_client.py
│   │   ├── discovery_client.py
│   │   ├── search_client.py
│   │   ├── workflow_client.py
│   │   ├── model_client.py
│   │   ├── search_sql_client.py
│   │   └── conversion_utils.py    # Pydantic ↔ attrs conversion utilities
│   ├── models/                    # Pydantic v2 models (available for separate use)
│   │   ├── alfresco_auth_models.py
│   │   ├── alfresco_core_models.py
│   │   ├── alfresco_discovery_models.py
│   │   ├── alfresco_search_models.py
│   │   ├── alfresco_workflow_models.py
│   │   ├── alfresco_model_models.py
│   │   └── alfresco_search_sql_models.py
│   ├── raw_clients/               # Generated HTTP clients
│   ├── utils/                     # Utility functions
│   │   ├── content_utils.py
│   │   ├── node_utils.py
│   │   ├── search_utils.py
│   │   ├── version_utils.py
│   │   └── mcp_formatters.py
│   └── events/                    # Event system (Community + Enterprise)
│       ├── __init__.py            # Event exports
│       ├── event_client.py        # Unified event client (AlfrescoEventClient)
│       └── models.py              # Event models (EventSubscription, EventNotification)
├── config/                        # Code generation configurations
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
├── docs/                          # Comprehensive documentation
│   ├── PYDANTIC_MODELS_GUIDE.md  # Complete Pydantic models guide
│   ├── CLIENT_TYPES_GUIDE.md     # Client architecture guide  
│   ├── CONVERSION_UTILITIES_DESIGN.md # Model conversion utilities
│   ├── REQUEST_TYPES_GUIDE.md    # Node & Search request documentation
│   └── API_DOCUMENTATION_INDEX.md # Complete API reference
├── examples/                      # Working usage examples
├── requirements.txt               # Runtime dependencies
├── requirements-dev.txt           # Development dependencies
├── run_tests.py                   # Test runner with nice display
└── README.md                      # This file
```



## 📋 Requirements

### Runtime Requirements

- **Python**: 3.10+
- **pydantic**: >=2.0.0,<3.0.0
- **requests**: >=2.31.0
- **httpx**: >=0.24.0 (for async support)
- **aiohttp**: >=3.8.0 (for async HTTP)

### Optional Dependencies

- **stomp.py**: >=8.1.0 (for ActiveMQ events)
- **ujson**: >=5.7.0 (faster JSON parsing)
- **requests-oauthlib**: >=1.3.0 (OAuth support)

## 🛠️ Contributing

For development workflows, code generation, testing, and contribution guidelines, see **[📖 Package Developers Guide](docs/PACKAGE_DEVELOPERS_GUIDE.md)**.

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

- **Model Context Protocol (MCP)**: [MCP Documentation](https://modelcontextprotocol.io/docs) - Standard for AI-data source and function integration
- **Alfresco Community Edition**: [Community Documentation](https://support.hyland.com/r/Alfresco/Alfresco-Content-Services-Community-Edition/25.1/Alfresco-Content-Services-Community-Edition/Introduction)
- **Alfresco Enterprise Edition**: [Enterprise Documentation](https://support.hyland.com/r/Alfresco/Alfresco-Content-Services/25.1/Alfresco-Content-Services/Introduction)
- **Pydantic**: [Type validation library](https://pydantic.dev/)
- **Datamodel-code-generator**: [Pydantic model generator](https://github.com/koxudaxi/datamodel-code-generator)
- **Openapi-python-client**: [HTTP client generator](https://github.com/openapi-generators/openapi-python-client)
- **MCP Server based on Python Alfresco API**: [python-alfresco-mcp-server](https://github.com/stevereiner/python-alfresco-mcp-server)

## ⭐ Star History

If this project helps you, please consider giving it a star! ⭐

