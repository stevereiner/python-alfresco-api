# Package Developers Guide - Python-Alfresco-API

This comprehensive guide covers everything needed for developing, contributing to, and maintaining the python-alfresco-api package, including the complete **3-step generation process**, development workflows, and contribution guidelines.

## 🔄 **Complete 3-Step Generation Process**

The python-alfresco-api uses a sophisticated 3-step generation pipeline that transforms OpenAPI specifications into a production-ready Python package:

### **STEP 1: Pydantic Model Generation**
- **Tool**: `datamodel-code-generator` 
- **Input**: OpenAPI 3.0 specs from `openapi/openapi3/*.yaml`
- **Output**: `python_alfresco_api/models/alfresco_*_models.py`
- **Purpose**: Standalone Pydantic v2 models perfect for LLM/MCP integration and type safety

### **STEP 2: HTTP Client Generation**
- **Tool**: `openapi-python-client`
- **Input**: OpenAPI 3.0 specs + configuration files from `config/*.yaml`  
- **Output**: `python_alfresco_api/raw_clients/alfresco_*_client/`
- **Purpose**: Professional HTTP clients with attrs models, async support, and complete API coverage

### **STEP 3: High-Level API Generation**
- **Tool**: Custom generation scripts (`generate_all_apis_v11.py`)
- **Input**: Raw client code from Step 2
- **Output**: `python_alfresco_api/clients/` hierarchical architecture
- **Purpose**: Developer-friendly V1.1 hierarchical APIs with lazy loading, 4-pattern operations, and MCP compatibility

## 🛠️ **Prerequisites**

### **Development Requirements**

For development, testing, and contributing:

```bash
pip install -r requirements-dev.txt
```

### **Code Generation Requirements**

**Required tools**:
- **datamodel-code-generator**: >=0.21.0 (Pydantic model generation)
- **openapi-python-client**: >=0.15.0 (HTTP client generation)
- **swagger2openapi**: For OpenAPI 2.0 → 3.0 conversion
- **pytest**: >=7.4.0 (Testing framework)
- **black**: >=23.0.0 (Code formatting)
- **mypy**: >=1.5.0 (Type checking)

## 📋 **Complete Regeneration Process**

### **Full Pipeline (All 3 Steps)**

```bash
# Complete regeneration from OpenAPI specs
python scripts/code-gen/generate_alfresco_client.py

# Generate V1.1 hierarchical APIs (Step 3)
python scripts/code-gen/generate_all_apis_v11.py

# Generate documentation
python scripts/doc-gen/generate_all_docs_v11.py
```

### **Individual Steps**

#### **Step 1: Update OpenAPI Specifications**

**All OpenAPI specifications are checked in** - you can develop immediately:
- `openapi/openapi2/` - Original specifications  
- `openapi/openapi2-processed/` - Processed specifications
- `openapi/openapi3/` - OpenAPI 3.0 specifications

To update specifications, download the latest from [Alfresco API Explorer](https://api-explorer.alfresco.com/api-explorer/) and place them in:

```
openapi/openapi2/alfresco-auth.yaml
openapi/openapi2/alfresco-core.yaml
openapi/openapi2/alfresco-discovery.yaml
openapi/openapi2/alfresco-search.yaml
openapi/openapi2/alfresco-workflow.yaml
openapi/openapi2/alfresco-model.yaml
openapi/openapi2/alfresco-search-sql.yaml
```

#### **Step 2: Run Individual Generation Steps**

**Generate Pydantic Models (Step 1)**:
```bash
# Generate standalone Pydantic v2 models (NOT integrated with clients)
datamodel-codegen \
  --input openapi/openapi3/alfresco-core.yaml \
  --output python_alfresco_api/models/alfresco_core_models.py \
  --target-python-version 3.10
```

**Generate HTTP Clients (Step 2)**:
```bash
# Generate HTTP client with attrs models (separate from Pydantic models)
openapi-python-client generate \
  --path openapi/openapi3/alfresco-core.yaml \
  --config config/core.yaml \
  --output-path python_alfresco_api/raw_clients/alfresco_core_client
```

**Generate High-Level APIs (Step 3)**:
```bash
# Generate V1.1 hierarchical APIs from raw clients
python scripts/code-gen/generate_all_apis_v11.py
```

#### **Step 3: Package Integration**

The pipeline automatically:
- Creates individual client wrappers (using attrs models from openapi-python-client)
- Generates V1.1 hierarchical architecture from raw client source code
- Sets up the ClientFactory and AuthUtil integration  
- Establishes the unified package structure with lazy loading
- Places standalone Pydantic models in separate modules (for independent use)
- Creates conversion utilities for Pydantic ↔ attrs model transformation

## ⚙️ **Generation Configuration**

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

### **Example Configuration** 

**`config/auth.yaml`**:
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

### **Configuration Benefits**

All generated package names use **short, practical names** instead of the default 42-character names:

- ✅ `auth_client` (10 chars) vs ❌ `alfresco_content_services_rest_api_client` (42 chars)
- ✅ `core_client` (11 chars) vs ❌ Default long name
- ✅ **64-81% shorter names** for better developer experience

### **Using Configuration**

```bash
# Generate specific API client with configuration
openapi-python-client generate \
  --path openapi/openapi3/alfresco-auth.yaml \
  --config config/auth.yaml \
  --output-path python_alfresco_api/raw_clients/alfresco_auth_client
```

## 🏗️ **Architecture Overview**

### **Generated Structure**

```
python_alfresco_api/
├── models/                           # STEP 1: Pydantic v2 models
│   ├── alfresco_auth_models.py       # Standalone, LLM-ready
│   ├── alfresco_core_models.py       # Type-safe validation
│   └── ...
├── raw_clients/                      # STEP 2: HTTP clients  
│   ├── alfresco_auth_client/         # Professional attrs-based clients
│   ├── alfresco_core_client/         # Async support, type safety
│   └── ...
└── clients/                          # STEP 3: High-level APIs
    ├── auth/                         # V1.1 hierarchical structure
    ├── core/                         # Lazy loading, 4-pattern operations
    ├── search/                       # MCP-compatible interfaces
    └── ...
```

### **V1.1 Hierarchical Architecture** 

**Step 3** generates the sophisticated V1.1 architecture:

```python
# Three-tier hierarchical access
client = master_client.core.nodes.get("node-id")
results = master_client.search.search.search(body=request)

# 4-pattern operations for every endpoint
node = client.core.nodes.get(node_id)                    # Basic sync
node = await client.core.nodes.get_async(node_id)        # Basic async  
response = client.core.nodes.get_detailed(node_id)       # Full HTTP response sync
response = await client.core.nodes.get_detailed_async(node_id)  # Full HTTP response async
```

### **Benefits of 3-Step Process**

1. **Pydantic Models (Step 1)**: Perfect for LLM integration, MCP servers, type validation
2. **HTTP Clients (Step 2)**: Production-ready networking, async support, comprehensive API coverage  
3. **High-Level APIs (Step 3)**: Developer experience, hierarchical organization, MCP compatibility

## 🔧 **Development Workflows**

### **Standard Development** (No Regeneration Needed)

For most development work on python-alfresco-api, you can develop directly without regenerating code:

```bash
git clone https://github.com/your-org/python-alfresco-api.git
cd python-alfresco-api

# Install in development mode
pip install -e .
```

### **Development Tasks**

```bash
# Run tests
pytest

# Run tests with nice display
python run_tests.py

# Format code
black python_alfresco_api/
isort python_alfresco_api/

# Type checking
mypy python_alfresco_api/
```

### **Making Changes**

1. **Modify existing code** - No regeneration needed
2. **Add new features** - Work with existing generated clients
3. **Update documentation** - Edit docs/ and examples/
4. **Add tests** - Extend the test suite

### **Code Generation Workflows**

#### **Full Regeneration** (after OpenAPI changes)
```bash
python scripts/code-gen/generate_alfresco_client.py
python scripts/code-gen/generate_all_apis_v11.py  
python scripts/doc-gen/generate_all_docs_v11.py
```

#### **Quick Regeneration** (current OpenAPI specs)
```bash
# Only regenerate when updating OpenAPI specifications
python scripts/code-gen/generate_alfresco_client.py
```

#### **Update High-Level APIs Only** (Step 3)
```bash
# Regenerate V1.1 hierarchical APIs from existing raw clients
python scripts/code-gen/generate_all_apis_v11.py
```

#### **Documentation Only**
```bash
python scripts/doc-gen/generate_v11_docs_from_code.py
python scripts/doc-gen/generate_complete_docs.py
```

## 🛡️ **Safety & Protection**

### **Protected Directories**
- 🔒 `python_alfresco_api/events/` - Event system (custom code)
- 🔒 `python_alfresco_api/utils/` - Utility functions (custom implementations)
- 🔒 Custom authentication code - Protected from template overwrites

### **Regenerated Directories**
- ✅ `python_alfresco_api/models/` - Pydantic models (Step 1)
- ✅ `python_alfresco_api/raw_clients/` - HTTP clients (Step 2)
- ✅ `python_alfresco_api/clients/` - High-level APIs (Step 3, template-based)

### **Backup Recommendations**
- Always backup before running generation scripts
- Test generation on a branch before merging
- Review generated code for custom modifications

## 📊 **Generation Script Coverage**

For detailed information about the generation pipeline, template architecture, and protection mechanisms, see:
- **`scripts/README.md`** - Complete script organization
- **`scripts/examples-and-docs/GENERATOR_SCRIPT_COVERAGE.md`** - Detailed template coverage
- **`config/README.md`** - Configuration documentation

## 🏷️ **Version Notes**

- **V1.0**: Basic generated clients with manual integration
- **V1.1**: Complete 3-step process with hierarchical architecture, lazy loading, and MCP compatibility
- **Future**: Enhanced conversion utilities and direct Pydantic integration

This 3-step process ensures that python-alfresco-api provides both low-level control (raw clients) and high-level productivity (hierarchical APIs) while maintaining type safety and LLM integration capabilities throughout. 