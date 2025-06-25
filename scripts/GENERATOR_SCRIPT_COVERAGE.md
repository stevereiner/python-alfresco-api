# Generator Script - Files Created from Template Text

This document lists all files that the `generate_alfresco_client.py` script creates from template text embedded in the script.

## 📊 **Quick Summary**

- **7 ACTIVE template functions** generating 11+ files
- **2 DISABLED functions** to avoid duplication 
- **Zero external dependencies** - all templates embedded in script
- **Safe directory management** - only cleans generated folders

## 🔄 Generator Pipeline Overview

### STEP 1: Data Model Generation  
- **Tool**: `datamodel-code-generator` 
- **Input**: OpenAPI specs from `openapi/openapi3/*.yaml`
- **Output**: `python_alfresco_api/models/alfresco_*_models.py`
- **Purpose**: Pydantic v2 models for LLM/MCP integration

### STEP 2: HTTP Client Code Generation
- **Tool**: `openapi-python-client`
- **Input**: OpenAPI specs + config files from `config/*.yaml`  
- **Output**: `python_alfresco_api/raw_clients/alfresco_*_client/`
- **Purpose**: Professional HTTP clients with async support

### STEP 3: Template-Based Package Creation
- **Tool**: Embedded templates in generator script
- **Input**: Template strings in Python functions
- **Output**: Wrapper classes, factory, utilities, examples, tests
- **Purpose**: Enterprise-ready unified package structure

## 📁 Directory Management

### Directories CLEANED (regenerated each run):
- ✅ `python_alfresco_api/models/` - Pydantic models  
- ✅ `python_alfresco_api/raw_clients/` - HTTP clients

### Directories PRESERVED (custom modules):
- 🔒 `python_alfresco_api/events/` - Event system (from GitHub)
- 🔒 `python_alfresco_api/clients/` - Wrapper clients (generated via templates)
- 🔒 `python_alfresco_api/examples/` - Usage examples (generated via templates)
- 🔒 `python_alfresco_api/docs/` - Package docs (if they exist)
- 🔒 `python_alfresco_api/tests/` - Test files (generated via templates)

## 🚀 Template Architecture Functions

These functions generate code from templates:

| Function | Purpose | Status |
|----------|---------|--------|
| `_create_main_init()` | Generate `__init__.py` | ✅ **ACTIVE** |
| `_create_client_factory()` | Generate `client_factory.py` | ✅ **ACTIVE** |
| `_create_auth_utility()` | Generate `auth_util.py` | ✅ **ACTIVE** |
| `_create_individual_client_wrapper()` | Generate client wrappers (7 files) | ✅ **ACTIVE** |
| `_create_models_init()` | Generate models `__init__.py` | ✅ **ACTIVE** |
| `_create_setup_py()` | Generate `setup.py` | ❌ **DISABLED** (redundant with pyproject.toml) |
| `_create_readme()` | Generate README | ❌ **DISABLED** (avoids duplicate docs) |
| `_create_examples()` | Generate example files (2 files) | ✅ **ACTIVE** |
| `_create_tests()` | Generate test files | ✅ **ACTIVE** |

**Template System**: All code is generated from embedded Python f-string templates within the script functions, making the generator completely self-contained.

## Files Created from Template Text in Script

### 1. **`python_alfresco_api/__init__.py`** (lines 259-307)
**Template**: `_create_main_init()`
- Main package entry point
- Imports all clients and models
- Defines `__version__` and `__all__`

### 2. **`python_alfresco_api/client_factory.py`** (lines 309-404) 
**Template**: `_create_client_factory()`
- Factory class for creating all clients
- Shared authentication management
- Methods like `create_auth_client()`, `create_all_clients()`

### 3. **`python_alfresco_api/auth_util.py`** (lines 406-514)
**Template**: `_create_auth_utility()`
- Shared authentication utility
- Ticket management with auto-renewal
- Authentication headers for API requests

### 4. **Individual Client Wrappers** (lines 528-621)
**Template**: `_create_individual_client_wrapper()`
**Creates 7 files**:
- `python_alfresco_api/clients/auth_client.py`
- `python_alfresco_api/clients/core_client.py`
- `python_alfresco_api/clients/discovery_client.py`
- `python_alfresco_api/clients/search_client.py`
- `python_alfresco_api/clients/workflow_client.py`
- `python_alfresco_api/clients/model_client.py`
- `python_alfresco_api/clients/search_sql_client.py`

Each wrapper:
- Imports the raw generated client
- Provides enhanced functionality
- Handles authentication automatically
- Offers both sync and async methods

### 5. **`python_alfresco_api/models/__init__.py`** (lines 623-673)
**Template**: `_create_models_init()`
- Imports all Pydantic models
- Makes models available for LLM/MCP integration

### 6. **`python_alfresco_api/setup.py`** (lines 675-731) ❌ **REMOVED**
**Template**: `_create_setup_py()`
- Package configuration (redundant with pyproject.toml)
- Dependencies and metadata
- Installation requirements
- **STATUS**: Removed to avoid duplication with pyproject.toml

### 7. **Package README** ❌ **DISABLED**  
**Template**: `_create_readme()` - DISABLED to avoid duplicate documentation
- Would create comprehensive package-level documentation
- **REASON**: Avoids confusion with root README.md
- **STATUS**: Function preserved but not called

### 8. **`python_alfresco_api/examples/basic_usage.py`** (lines 907-965)
**Template**: `_create_examples()` 
- Basic usage demonstrations
- Factory pattern examples
- Individual client examples

### 9. **`python_alfresco_api/examples/llm_integration.py`** (lines 967-1126)
**Template**: `_create_examples()`
- LLM tool function examples
- MCP server integration patterns
- Pydantic model usage for AI

### 10. **`python_alfresco_api/tests/test_basic.py`** (lines 1135-1233)
**Template**: `_create_tests()`
- Basic functionality tests
- Client factory tests
- Pydantic model validation tests

## Summary

**Total: 10+ files created from template text** (2 disabled to avoid duplication)
- ✅ 1 main package file (`__init__.py`)
- ✅ 1 factory file (`client_factory.py`)
- ✅ 1 auth utility file (`auth_util.py`)
- ✅ 7 individual client wrapper files
- ✅ 1 models package file (`models/__init__.py`)
- ❌ 1 setup file (`setup.py`) - **REMOVED** (redundant with pyproject.toml)
- ❌ 1 README file - **DISABLED** (avoids duplication with root README.md)
- ✅ 2 example files
- ✅ 1 test file

**Active Files Generated**: 11 files from embedded templates
**Disabled Functions**: 2 functions preserved but not called to avoid duplication

All template text is embedded in the script between the specified line ranges, making the generator completely self-contained while avoiding documentation conflicts. 