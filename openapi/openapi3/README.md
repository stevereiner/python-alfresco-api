# OpenAPI 3.0 Specifications

This directory contains the **converted OpenAPI 3.0 specifications** for next-generation tooling and broader ecosystem compatibility.

## 📁 Contents

| File | Size | Description |
|------|------|-------------|
| `alfresco-auth.yaml` | 5.4 KB | Authentication API - OpenAPI 3.0 format |
| `alfresco-core.yaml` | 322 KB | Core API - OpenAPI 3.0 format |
| `alfresco-discovery.yaml` | 4.7 KB | Discovery API - OpenAPI 3.0 format |
| `alfresco-search.yaml` | 41 KB | Search API - OpenAPI 3.0 format |
| `alfresco-workflow.yaml` | 67 KB | Workflow API - OpenAPI 3.0 format |
| `alfresco-model.yaml` | 18 KB | Model API - OpenAPI 3.0 format |
| `alfresco-search-sql.yaml` | 8.1 KB | Search SQL API - OpenAPI 3.0 format |

## 🔄 Conversion Process

These files are automatically converted from `../openapi2-processed/` using:
- **[swagger2openapi](https://github.com/Mermade/oas-kit)** - Professional conversion tool
- **Schema migration** - OpenAPI 2.0 → OpenAPI 3.0
- **Validation** - Full OpenAPI 3.0 compliance checking
- **Enhancement** - Modern OpenAPI 3.0 features

## ✨ OpenAPI 3.0 Benefits

### Enhanced Features
- **Better Parameter Handling** - More flexible parameter definitions
- **Improved Responses** - Richer response schema definitions
- **Modern Standards** - Latest OpenAPI specification compliance
- **Wider Tool Support** - Compatibility with newer generation tools

### Ecosystem Compatibility
- **Broader Generator Support** - More language generators available
- **Modern Tooling** - Latest API development tools
- **Future-Proof** - Ready for next-generation API tools
- **Industry Standard** - Current OpenAPI specification

## 🚀 Usage Examples

### Multi-Language Generation
```bash
# Python with modern generators
openapi-generator generate \
  -i openapi/openapi3/alfresco-core.yaml \
  -g python-pydantic-v1 \
  -o generated/python/

# JavaScript/TypeScript
openapi-generator generate \
  -i openapi/openapi3/alfresco-core.yaml \
  -g typescript-axios \
  -o generated/typescript/

# Java
openapi-generator generate \
  -i openapi/openapi3/alfresco-core.yaml \
  -g java \
  -o generated/java/

# C#
openapi-generator generate \
  -i openapi/openapi3/alfresco-core.yaml \
  -g csharp-netcore \
  -o generated/csharp/

# Go
openapi-generator generate \
  -i openapi/openapi3/alfresco-core.yaml \
  -g go \
  -o generated/go/
```

### Documentation Generation
```bash
# Swagger UI
swagger-ui-serve openapi/openapi3/alfresco-core.yaml

# Redoc
redoc-cli serve openapi/openapi3/alfresco-core.yaml

# Postman Collection
openapi2postmanv2 \
  -s openapi/openapi3/alfresco-core.yaml \
  -o alfresco-core.postman_collection.json
```

### API Testing
```bash
# Dredd API testing
dredd openapi/openapi3/alfresco-core.yaml http://localhost:8080

# Schemathesis property-based testing
schemathesis run openapi/openapi3/alfresco-core.yaml \
  --base-url http://localhost:8080
```

## 🎯 Use Cases

### Perfect For:
- ✅ **Multi-language SDKs** - Generate clients for JavaScript, Java, C#, Go, etc.
- ✅ **API Documentation** - Modern documentation tools and platforms
- ✅ **Testing Tools** - Property-based testing and validation
- ✅ **API Gateways** - Modern API management platforms
- ✅ **Contract Testing** - Consumer-driven contract testing
- ✅ **Mock Servers** - Advanced mocking and simulation

### Integration Examples
```python
# Direct usage in Python
import yaml
import requests

# Load OpenAPI 3.0 spec
with open('openapi/openapi3/alfresco-core.yaml') as f:
    spec = yaml.safe_load(f)

print(f"OpenAPI Version: {spec['openapi']}")
print(f"API Title: {spec['info']['title']}")
print(f"Servers: {spec['servers']}")
```

## 🔧 Quality Features

### OpenAPI 3.0 Enhancements
- **Server Objects** - Multiple server configurations
- **Component Schemas** - Reusable schema components
- **Request Bodies** - Explicit request body definitions
- **Callback Objects** - Webhook and callback support
- **Link Objects** - API operation relationships

### Validation & Compliance
- ✅ **OpenAPI 3.0 Compliant** - Full specification compliance
- ✅ **Schema Validated** - All schemas properly defined
- ✅ **Tool Compatible** - Works with all major OpenAPI 3.0 tools
- ✅ **Future Ready** - Prepared for OpenAPI 3.1+ migration

## 📋 File Status

- ✅ **Modern Format**: OpenAPI 3.0 specification
- ✅ **Converted**: Professional conversion from OpenAPI 2.0
- ✅ **Validated**: Full OpenAPI 3.0 compliance
- ✅ **Enhanced**: Modern OpenAPI 3.0 features
- ✅ **Tool Ready**: Compatible with latest generators and tools

## 🔄 Update Process

These files are automatically maintained:

1. **Source**: `../openapi2-processed/` (processed OpenAPI 2.0)
2. **Conversion**: swagger2openapi professional conversion
3. **Validation**: OpenAPI 3.0 compliance checking
4. **Output**: Modern OpenAPI 3.0 specifications

---

**Use these files for modern tooling, multi-language generation, and next-generation API development.** 