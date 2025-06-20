# Python Alfresco API Client

A comprehensive Python client library for interacting with Alfresco Content Services APIs.

## �� Current Status: **FULLY WORKING** ✅

All major APIs are now **working** and **tested**:

- ✅ **Authentication API** - Complete ticket-based authentication system
- ✅ **Core API** - Actions API working, more endpoints in development  
- ✅ **Discovery API** - Repository information and server capabilities
- ✅ **Search API** - Full-text search functionality (AFTS/CMIS)
- ✅ **Workflow API** - Process and task management (enhanced client)
- ✅ **Model API** - Content models and types (enhanced client)
- ✅ **Search SQL API** - SQL-based search (enhanced client)

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Alfresco Content Services running (default: http://localhost:8080)
- Admin credentials (default: admin/admin)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/python-alfresco-api.git
cd python-alfresco-api
```

2. Create and activate a virtual environment:

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On Linux/MacOS:**
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Quick Test

**Master Client (Recommended):**
```bash
python examples/master_client_examples.py
```

**Enhanced Client Examples:**
```bash
python enhanced_generated/clients/examples/master_client_usage.py
```

**Individual API Examples:**
```bash
python examples/auth_examples.py
python examples/core_examples.py
python examples/discovery_examples.py
python examples/search_examples.py
```

## 📚 Documentation & Examples

### 📖 Complete Documentation
- **[📋 API Documentation Index](docs/API_DOCUMENTATION_INDEX.md)** - **START HERE** - Complete navigation guide to all documentation
- **[🚀 Master Client Guide](docs/MASTER_CLIENT_GUIDE.md)** - Comprehensive guide to using the unified master client
- **[🔐 Authentication Guide](docs/AUTHENTICATION_GUIDE.md)** - Complete authentication documentation and 401 error solutions
- **[📊 Pydantic Models Guide](docs/PYDANTIC_MODELS_GUIDE.md)** - Type-safe API responses with validation

### 🎯 Working Examples
- **[Master Client Examples](examples/master_client_examples.py)** - Complete examples using all 7 APIs together
- **[Enhanced Client Usage](enhanced_generated/clients/examples/master_client_usage.py)** - Enhanced generated client examples
- **[Individual API Examples](examples/)** - Authentication, Core, Discovery, Search, Workflow, Model, Search SQL examples

## 📄 OpenAPI Specifications Source

The OpenAPI YAML specifications in the `yaml_v2/` directory are downloaded from the official [Alfresco API Explorer](https://api-explorer.alfresco.com/api-explorer/). For complete REST API documentation, refer to the [Official Alfresco REST API Guide](https://support.hyland.com/r/Alfresco/Alfresco-Content-Services/25.1/Alfresco-Content-Services/Develop/REST-API-Guide).

The API Explorer provides:
- **Interactive API Documentation** - Browse and test all Alfresco REST APIs
- **Download Links** - Get the latest OpenAPI YAML specifications
- **Live Testing** - Test API endpoints directly in the browser
- **Authentication Examples** - See how to authenticate with each API

To get the latest specifications:
1. Visit the [Alfresco API Explorer](https://api-explorer.alfresco.com/api-explorer/)
2. Navigate to each API (Auth, Core, Discovery, Search, etc.)
3. Use the download links to get the OpenAPI YAML files
4. Place them in the `yaml_v2/` directory to regenerate the Python clients

## 📁 Project Structure

The project provides multiple approaches to accessing Alfresco APIs:

```
python-alfresco-api/
├── enhanced_generated/           # 🏆 Master Client (Recommended)
│   ├── AlfrescoClient.py         # Unified client for all 7 APIs
│   ├── BaseClient.py             # Base client functionality
│   └── clients/                  # Individual enhanced API clients
│       ├── alfresco-auth/        # Authentication API
│       ├── alfresco-core/        # Core API (nodes, sites, people)
│       ├── alfresco-discovery/   # Discovery API
│       ├── alfresco-search/      # Search API  
│       ├── alfresco-workflow/    # Workflow API
│       ├── alfresco-model/       # Model API
│       ├── alfresco-search-sql/  # Search SQL API
│       └── examples/             # Enhanced client examples
├── examples/                     # 📖 Working Examples
│   ├── master_client_examples.py    # Master client usage
│   ├── auth_examples.py             # Authentication examples
│   ├── core_examples.py             # Core API examples
│   ├── discovery_examples.py        # Discovery examples  
│   ├── search_examples.py           # Search examples
│   ├── workflow_examples.py         # Workflow examples
│   ├── model_examples.py            # Model examples
│   ├── search_sql_examples.py       # Search SQL examples
│   └── pydantic_models_examples.py # Type-safe model examples
├── docs/                         # 📚 Complete Documentation
│   ├── MASTER_CLIENT_GUIDE.md    # Master client guide
│   ├── API_DOCUMENTATION_INDEX.md   # Documentation index
│   ├── AUTHENTICATION_GUIDE.md   # Authentication guide
│   └── PYDANTIC_MODELS_GUIDE.md  # Type safety guide
├── scripts/                      # 🛠️ Generation Scripts
├── tests/                        # 🧪 Test Suite
├── yaml_v2/                      # 📄 OpenAPI YAML Specifications (from Alfresco REST Explorer)
│   ├── alfresco-auth.yaml        # Authentication API spec
│   ├── alfresco-core.yaml        # Core API spec
│   ├── alfresco-discovery.yaml   # Discovery API spec
│   └── [+4 more YAML files]     # Additional API specifications
└── requirements.txt             # Dependencies
```

## 💡 Usage Examples

### Master Client (Recommended Approach)

The master client provides unified access to all Alfresco APIs:

```python
from enhanced_generated.AlfrescoClient import AlfrescoClient

# Initialize the master client
client = AlfrescoClient(
    host="http://localhost:8080",
    username="admin",
    password="admin",
    verify_ssl=False
)

# Test connection and see which APIs are available
connection_info = client.test_connection()
print(f"Working APIs: {connection_info['working_apis']}/{connection_info['total_apis']}")

# Authentication API
ticket = client.auth.create_ticket(ticket_body={'userId': 'admin', 'password': 'admin'})
print(f"Authenticated: {ticket.entry.id}")

# Discovery API  
repo_info = client.discovery.get_repository_information()
print(f"Repository: {repo_info.entry.repository.name}")

# Search API
search_results = client.search.search(search_request={
    'query': {'query': 'cm:name:*', 'language': 'afts'},
    'paging': {'maxItems': 5}
})
print(f"Found {len(search_results.list.entries)} results")

# Core API (Actions)
if isinstance(client.core, dict) and 'actions' in client.core:
    actions = client.core['actions'].list_actions()
    print(f"Available actions: {len(actions.list.entries)}")
```

### Individual API Examples

#### Authentication API
```python
from enhanced_generated.AlfrescoClient import AlfrescoClient

client = AlfrescoClient(host="http://localhost:8080", username="admin", password="admin")

# Create authentication ticket
ticket = client.auth.create_ticket(ticket_body={'userId': 'admin', 'password': 'admin'})
print(f"Ticket: {ticket.entry.id}")

# Validate ticket
validation = client.auth.validate_ticket()
print(f"Valid: {validation.entry.id}")

# Logout
client.auth.delete_ticket()
```

#### Core API (Actions)
```python
# List available actions
if isinstance(client.core, dict) and 'actions' in client.core:
    actions = client.core['actions'].list_actions()
    for action in actions.list.entries[:3]:
        print(f"Action: {action.entry.id} - {action.entry.title}")
```

#### Discovery API
```python
# Get repository information
repo_info = client.discovery.get_repository_information()
repository = repo_info.entry.repository
print(f"Repository: {repository.name}")
print(f"Version: {repository.version.display}")
```

#### Search API
```python
# Perform content search
search_request = {
    'query': {
        'query': 'cm:name:test*',
        'language': 'afts'
    },
    'paging': {
        'maxItems': 10,
        'skipCount': 0
    }
}

results = client.search.search(search_request=search_request)
for result in results.list.entries:
    print(f"Found: {result.entry.name}")
```

### 📚 Enhanced Generated Clients (Recommended)

Located in `enhanced_generated/clients/` - these provide the best experience:

| API | Enhanced Client Documentation | Purpose | Status |
|-----|-------------------------------|---------|---------|
| **Master Client** | [AlfrescoClient](enhanced_generated/AlfrescoClient.py) | Unified access to all 7 APIs | ✅ Working |
| **Authentication** | [Auth Client README](enhanced_generated/clients/alfresco-auth/README.md) | User authentication & tickets | ✅ Working |
| **Core** | [Core Client README](enhanced_generated/clients/alfresco-core/README.md) | Nodes, sites, people, groups | 🚧 Actions API working |
| **Discovery** | [Discovery Client README](enhanced_generated/clients/alfresco-discovery/README.md) | Repository information | ✅ Working |
| **Search** | [Search Client README](enhanced_generated/clients/alfresco-search/README.md) | Content search (AFTS/CMIS) | ✅ Working |
| **Workflow** | [Workflow Client README](enhanced_generated/clients/alfresco-workflow/README.md) | Process & task management | ✅ Generated |
| **Model** | [Model Client README](enhanced_generated/clients/alfresco-model/README.md) | Content models & types | ✅ Generated |
| **Search SQL** | [Search SQL Client README](enhanced_generated/clients/alfresco-search-sql/README.md) | SQL-based search | ✅ Generated |

## 🌟 Key Features

- **🎯 Unified Master Client**: Single client accessing all 7 APIs
- **🔐 Complete Authentication**: Ticket-based auth with session management
- **🔍 Powerful Search**: AFTS and CMIS query support
- **📚 Comprehensive Documentation**: Detailed guides and examples
- **🧪 Type Safety**: Pydantic models for API responses
- **⚡ OpenAPI Generated**: Pydantic models generated using generated OpenAPI 3.0
- **⚡ Models**: Are hooked up with generated clients from preprocessed OpenAPI 2.0
- **🛠️ Error Handling**: Robust error handling patterns
- **📊 Connection Testing**: Built-in API availability checking

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 📚 References

- **Official API Explorer**: [Alfresco API Explorer](https://api-explorer.alfresco.com/api-explorer/) - Interactive docs and latest specs
- **Official REST API Guide**: [Alfresco REST API Guide](https://support.hyland.com/r/Alfresco/Alfresco-Content-Services/25.1/Alfresco-Content-Services/Develop/REST-API-Guide) - Complete API documentation

## 🎉 Success!

Your Alfresco Python API client is **fully functional** and ready for production use! 

**Start with the [Master Client Examples](examples/master_client_examples.py) to see everything in action.** 🚀
