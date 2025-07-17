# Scripts Directory - Developer Guide

This directory contains generation, testing, and utility scripts for the python-alfresco-api project, organized into logical categories.

## 📁 **ORGANIZED STRUCTURE**

```
scripts/
├── code-gen/              # Code generation scripts
├── doc-gen/               # Documentation generation scripts  
├── utility/               # Utility and helper scripts
├── testing/               # Testing and validation scripts
└── examples-and-docs/     # Examples and documentation
```

## 🚀 **CODE GENERATION** (`code-gen/`)

### **Main Generation Pipeline**
- **`generate_alfresco_client.py`** - **CRITICAL**: Main generation script that creates the entire package structure
  - Generates Pydantic models from OpenAPI specs
  - Creates HTTP clients using openapi-python-client
  - Builds unified package structure with templates
  - **Usage**: `python scripts/code-gen/generate_alfresco_client.py`

### **API Generation Scripts**
- **`generate_all_apis_v11.py`** - Generates all V1.1 hierarchical APIs
- **`generate_v11_clients.py`** - Generates V1.1 client architecture
- **`generate_v11_enhanced.py`** - Enhanced generation with additional features
- **`generate_v11_clients_enhanced.py`** - Enhanced client generation
- **`generate_v11_lazy_comprehensive.py`** - Lazy loading implementation generation

### **Architecture Utilities**
- **`generate_core_subsections.py`** - Generates core API subsections
- **`lazy_imports_with_docs.py`** - Lazy import generation with documentation
- **`lazy_import_generator.py`** - Lazy import utility functions

## 📖 **DOCUMENTATION GENERATION** (`doc-gen/`)

### **Primary Documentation Scripts**
- **`generate_v11_docs_from_code.py`** - Generates documentation directly from code
- **`generate_all_docs_v11.py`** - Complete V1.1 documentation generation
- **`generate_complete_docs.py`** - Complete documentation with examples

### **Specialized Documentation**
- **`generate_docs_v11.py`** - V1.1 specific documentation
- **`generate_nodes_complete_docs.py`** - Complete nodes API documentation
- **`generate_proper_api_docs.py`** - API reference documentation
- **`generate_level3_doc.py`** - Level 3 operation-specific documentation
- **`generate_all_proper_docs.py`** - All proper documentation generation
- **`generate_remaining_apis_docs.py`** - Remaining API documentation
- **`generate_complete_docs_with_progress.py`** - Complete docs with progress tracking

## 🔧 **UTILITIES** (`utility/`)

- **`mcp_operation_mapping.py`** - MCP server operation mapping utilities

## 🧪 **TESTING & VALIDATION** (`testing/`)

### **Architecture Testing**
- **`comprehensive_architecture_test.py`** - Complete architecture validation
  - Tests all client hierarchies
  - Validates sync/async patterns
  - Checks MCP integration
  - **Usage**: `python scripts/testing/comprehensive_architecture_test.py`

### **Performance & Specialized Testing**
- **`test_performance.py`** - Performance benchmarking
- **`test_server.py`** - Server testing utilities
- **`test_doc_gen.py`** - Documentation generation testing

## 📋 **EXAMPLES & DOCUMENTATION** (`examples-and-docs/`)

- **`simple_progress_example.py`** - Example of progress tracking implementation
- **`GENERATOR_SCRIPT_COVERAGE.md`** - Complete overview of the generation pipeline
  - Lists all template functions
  - Explains protection mechanisms
  - Documents safety measures for custom code

## 🛠️ **TYPICAL WORKFLOWS**

### **Regenerate Everything** (After OpenAPI changes):
```bash
python scripts/code-gen/generate_alfresco_client.py
python scripts/code-gen/generate_all_apis_v11.py
python scripts/doc-gen/generate_all_docs_v11.py
```

### **Update Documentation Only**:
```bash
python scripts/doc-gen/generate_v11_docs_from_code.py
python scripts/doc-gen/generate_complete_docs.py
```

### **Test Architecture**:
```bash
python scripts/testing/comprehensive_architecture_test.py
python scripts/testing/test_performance.py
```

### **Generate Specific API Subsections**:
```bash
python scripts/code-gen/generate_core_subsections.py
python scripts/doc-gen/generate_nodes_complete_docs.py
```

## ⚠️ **SAFETY NOTES**

- **Authentication Protection**: Main generation script has removed dangerous template functions to protect custom authentication code
- **Custom Code Safety**: Scripts avoid overwriting custom implementations in `/clients/` hierarchy
- **Backup Recommended**: Always backup before running generation scripts

## 🗂️ **ORGANIZATION BENEFITS**

### **Logical Separation**
- **`code-gen/`**: All scripts that generate actual Python code (9 scripts)
- **`doc-gen/`**: All scripts that generate documentation (10 scripts)
- **`utility/`**: Helper utilities and mappings (1 script)
- **`testing/`**: Validation and testing scripts (4 scripts)
- **`examples-and-docs/`**: Examples and documentation (2 files)

### **Improved Maintainability**
- Easy to find scripts by purpose
- Clear separation of concerns
- Reduced clutter in root directory
- Logical grouping for team development

### **Historical Cleanup**
- **✅ Kept**: 26 production utility scripts organized into folders
- **📦 Moved to Backup**: 23 historical fix/migration scripts no longer needed
- **🧹 Clean Structure**: Focus on ongoing development tools

For detailed information about the generation pipeline and template architecture, see `examples-and-docs/GENERATOR_SCRIPT_COVERAGE.md`. 