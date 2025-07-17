# Generator Script - Files Created from Template Text

This document lists all files that the `generate_alfresco_client.py` script creates from template text embedded in the script.

## 📊 **🛡️ PROTECTION STATUS**

- **4 ACTIVE template functions** generating 5 safe files ✅
- **3 REMOVED functions** to protect authentication breakthrough 🚨
- **2 DISABLED functions** to avoid duplication ❌
- **Zero external dependencies** - all templates embedded in script
- **Safe directory management** - only cleans generated folders
- **🛡️ CUSTOM CODE PROTECTED** - Authentication breakthrough preserved

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
| `_create_client_factory()` | Generate `client_factory.py` | 🚨 **REMOVED** (would overwrite custom authentication) |
| `_create_auth_utility()` | Generate `auth_util.py` | 🚨 **REMOVED** (would overwrite query parameter auth breakthrough) |
| `_create_individual_client_wrapper()` | Generate client wrappers (7 files) | 🚨 **REMOVED** (would overwrite inheritance-based clients) |
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

### 2. **`python_alfresco_api/client_factory.py`** 🚨 **REMOVED**
**Template**: `_create_client_factory()` - **REMOVED TO PROTECT CUSTOM AUTHENTICATION**
- Would have created factory class for creating all clients
- Would have overwritten breakthrough query parameter authentication
- **SAFE**: Custom implementation with environment variables and OAuth2 support preserved

### 3. **`python_alfresco_api/auth_util.py`** 🚨 **REMOVED**
**Template**: `_create_auth_utility()` - **REMOVED TO PROTECT AUTHENTICATION BREAKTHROUGH**
- Would have created basic ticket authentication
- Would have overwritten working query parameter authentication (`alf_ticket`)
- **SAFE**: Custom implementation with direct HTTP auth and `add_auth_params()` method preserved

### 4. **Individual Client Wrappers** 🚨 **REMOVED**
**Template**: `_create_individual_client_wrapper()` - **REMOVED TO PROTECT INHERITANCE-BASED CLIENTS**
**Would have created 7 files**:
- `python_alfresco_api/clients/auth_client.py`
- `python_alfresco_api/clients/core_client.py`
- `python_alfresco_api/clients/discovery_client.py`
- `python_alfresco_api/clients/search_client.py`
- `python_alfresco_api/clients/workflow_client.py`
- `python_alfresco_api/clients/model_client.py`
- `python_alfresco_api/clients/search_sql_client.py`

**SAFE**: Custom inheritance-based clients with `AuthenticatedClient` pattern preserved

### 5. **`python_alfresco_api/models/__init__.py`**
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

**🛡️ AUTHENTICATION BREAKTHROUGH PROTECTED!**

**Total: 6 files created from template text** (5 removed/disabled for safety)
- ✅ 1 main package file (`__init__.py`)
- 🚨 1 factory file (`client_factory.py`) - **REMOVED** (protects custom authentication)
- 🚨 1 auth utility file (`auth_util.py`) - **REMOVED** (protects query parameter breakthrough)
- 🚨 7 individual client wrapper files - **REMOVED** (protects inheritance-based clients)
- ✅ 1 models package file (`models/__init__.py`)
- ❌ 1 setup file (`setup.py`) - **DISABLED** (redundant with pyproject.toml)
- ❌ 1 README file - **DISABLED** (avoids duplication with root README.md)
- ✅ 2 example files
- ✅ 1 test file

**Safe Files Generated**: 5 files from embedded templates
**Dangerous Functions**: 3 functions **COMPLETELY REMOVED** to protect custom authentication code
**Disabled Functions**: 2 functions preserved but not called to avoid duplication

**CRITICAL**: The three most dangerous template functions have been **permanently removed** from the script to prevent accidental overwriting of:
1. Custom query parameter authentication (`alf_ticket`) breakthrough
2. Enhanced ClientFactory with environment variable support and OAuth2
3. Inheritance-based clients using `AuthenticatedClient` pattern

All remaining template text is embedded in the script, making the generator self-contained while **protecting your authentication breakthrough work**. 