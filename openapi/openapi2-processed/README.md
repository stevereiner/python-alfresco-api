# Processed OpenAPI 2.0 Specifications

This directory contains the **cleaned and optimized OpenAPI 2.0 specifications** that are the **primary source** for python-alfresco-api code generation.

## 📁 Contents

| File | Size | Description |
|------|------|-------------|
| `alfresco-auth.yaml` | 5.1 KB | Authentication API - Processed and optimized |
| `alfresco-core.yaml` | 307 KB | Core API - Processed and optimized |
| `alfresco-discovery.yaml` | 4.3 KB | Discovery API - Processed and optimized |
| `alfresco-search.yaml` | 40 KB | Search API - Processed and optimized |
| `alfresco-workflow.yaml` | 63 KB | Workflow API - Processed and optimized |
| `alfresco-model.yaml` | 17 KB | Model API - Processed and optimized |
| `alfresco-search-sql.yaml` | 7.7 KB | Search SQL API - Processed and optimized |

## ✅ Processing Enhancements

These files have been professionally processed with:

- **YAML Formatting**: Consistent indentation and structure
- **Schema Validation**: All OpenAPI 2.0 compliance issues resolved
- **Type Definitions**: Optimized schema references and data types
- **Unicode Support**: Full international character compatibility
- **Error Handling**: Comprehensive error response definitions
- **Documentation**: Enhanced descriptions and examples
- **Regex Fixes**: Corrected pattern validation syntax

## 🚀 **PRIMARY USE** - Code Generation

**These are the recommended files for all code generation:**

### Hybrid Pipeline (Recommended)
```bash
# Generate Pydantic models
datamodel-codegen \
  --input openapi/openapi2-processed/alfresco-core.yaml \
  --output python_alfresco_api/models/alfresco_core_models.py \
  --target-python-version 3.8

# Generate HTTP clients
openapi-python-client generate \
  --path openapi/openapi2-processed/alfresco-core.yaml \
  --config client_config.yaml
```

### Automated Generation
```bash
# Full library regeneration
python scripts/generate_hybrid_pipeline.py
```

### Alternative Tools
```bash
# OpenAPI Generator
openapi-generator generate \
  -i openapi/openapi2-processed/alfresco-core.yaml \
  -g python-pydantic-v1 \
  -o generated/

# Swagger Codegen
swagger-codegen generate \
  -i openapi/openapi2-processed/alfresco-core.yaml \
  -l python \
  -o generated/
```

## 🎯 Quality Assurance

All files in this directory:
- ✅ **Pass validation** with openapi-spec-validator
- ✅ **Generate clean code** with all major tools
- ✅ **Support type safety** for Pydantic v2 models
- ✅ **Enable async operations** with httpx/aiohttp
- ✅ **Work with LLM tools** for AI integration

## 🔄 Update Process

These files are automatically updated by the processing pipeline:

1. **Source**: Generated from `../openapi2/` (original files)
2. **Processing**: Custom YAML cleaning and validation
3. **Output**: Production-ready specifications
4. **Validation**: Comprehensive OpenAPI 2.0 compliance checking

## 📋 File Status

- ✅ **Production Ready**: Optimized for code generation
- ✅ **Validated**: All OpenAPI 2.0 compliance issues resolved
- ✅ **Type Safe**: Perfect for Pydantic model generation
- ✅ **LLM Compatible**: Ideal for AI integration and MCP servers
- ✅ **Future Proof**: Ready for conversion to OpenAPI 3.0

---

**Use these files as the primary source for all python-alfresco-api code generation.** 