# Alfresco OpenAPI Specifications

This directory contains the **complete collection of Alfresco Content Services OpenAPI specifications** in multiple formats and processing stages. These are the canonical source files for the python-alfresco-api v2.0 library.

## 📁 Directory Structure

```
openapi/
├── openapi2/                    # Original OpenAPI 2.0 (Swagger) specifications
├── openapi2-processed/          # Cleaned and preprocessed OpenAPI 2.0 files
├── openapi3/                    # Converted OpenAPI 3.0 specifications
└── README.md                    # This documentation
```

## 🔄 Processing Pipeline

### 1. **openapi2/** - Original Sources
- **Source**: Downloaded from [Alfresco API Explorer](https://api-explorer.alfresco.com/api-explorer/)
- **Format**: OpenAPI 2.0 (Swagger)
- **Status**: Raw, unprocessed specifications
- **Purpose**: Baseline reference and backup

### 2. **openapi2-processed/** - Cleaned OpenAPI 2.0
- **Source**: Processed from `openapi2/` directory
- **Format**: OpenAPI 2.0 (Swagger) - cleaned and optimized
- **Status**: Production-ready for code generation
- **Purpose**: **PRIMARY SOURCE** for python-alfresco-api generation

### 3. **openapi3/** - Modern OpenAPI 3.0
- **Source**: Converted from `openapi2-processed/`
- **Format**: OpenAPI 3.0
- **Status**: Future-ready specifications
- **Purpose**: Next-generation tooling and broader ecosystem compatibility

## 📊 Available APIs

| API | Description | Auth | Core | Discovery | Search | Workflow | Model | Search SQL |
|-----|-------------|------|------|-----------|--------|----------|-------|------------|
| **Size (KB)** | File sizes | 5.1 | 307 | 4.3 | 40 | 63 | 17 | 7.7 |
| **Endpoints** | API count | 3 | 180+ | 4 | 12 | 45+ | 15+ | 8 |
| **Models** | Data types | 6 | 200+ | 10 | 35+ | 80+ | 25+ | 12 |

### API Details

#### 🔐 **Authentication API** (`alfresco-auth.yaml`)
- **Purpose**: User authentication and session management
- **Key Features**: Ticket creation, validation, logout
- **Models**: Ticket, TicketBody, ValidTicket, Error

#### 🏢 **Core API** (`alfresco-core.yaml`)
- **Purpose**: Primary content management operations
- **Key Features**: Nodes, sites, people, groups, permissions, actions
- **Models**: 200+ including Node, Site, Person, Group, Permission

#### 🔍 **Discovery API** (`alfresco-discovery.yaml`)
- **Purpose**: Repository information and capabilities
- **Key Features**: Version info, modules, license details
- **Models**: RepositoryInfo, VersionInfo, ModuleInfo

#### 🔎 **Search API** (`alfresco-search.yaml`)
- **Purpose**: Full-text search and query operations
- **Key Features**: AFTS queries, CMIS queries, faceted search
- **Models**: SearchRequest, SearchResponse, ResultSet, Facet

#### ⚙️ **Workflow API** (`alfresco-workflow.yaml`)
- **Purpose**: Process and task management
- **Key Features**: Process definitions, instances, tasks, variables
- **Models**: Process, Task, Variable, FormModel

#### 📋 **Model API** (`alfresco-model.yaml`)
- **Purpose**: Content model and type definitions
- **Key Features**: Custom types, aspects, properties, constraints
- **Models**: Model, Type, Aspect, Property, Constraint

#### 📊 **Search SQL API** (`alfresco-search-sql.yaml`)
- **Purpose**: SQL-based search for Insight Engine
- **Key Features**: SQL queries, result sets, metadata
- **Models**: SQLQuery, SQLResult, ResultSet

## 🚀 Code Generation Usage

### Primary Generation (Recommended)
Use the **processed OpenAPI 2.0** files for optimal results:

```bash
# Pydantic Models
datamodel-codegen \
  --input openapi/openapi2-processed/alfresco-core.yaml \
  --output python_alfresco_api/models/alfresco_core_models.py \
  --target-python-version 3.8

# HTTP Clients
openapi-python-client generate \
  --path openapi/openapi2-processed/alfresco-core.yaml \
  --config client_config.yaml
```

### Automated Pipeline
```bash
# Full hybrid generation
python scripts/generate_hybrid_pipeline.py
```

### Alternative Generators
```bash
# OpenAPI 3.0 with Java tools
openapi-generator generate \
  -i openapi/openapi3/alfresco-core.yaml \
  -g python-pydantic-v1 \
  -o generated/

# Original Swagger 2.0
swagger-codegen generate \
  -i openapi/openapi2/alfresco-core.yaml \
  -l python \
  -o generated/
```

## 🔧 Processing Quality

### openapi2-processed/ Enhancements
- ✅ **YAML Formatting**: Consistent indentation and structure
- ✅ **Schema Validation**: All OpenAPI 2.0 compliance issues resolved
- ✅ **Type Definitions**: Optimized schema references and data types
- ✅ **Unicode Support**: Full international character compatibility
- ✅ **Error Handling**: Comprehensive error response definitions
- ✅ **Documentation**: Enhanced descriptions and examples
- ✅ **Regex Fixes**: Corrected pattern validation syntax

### openapi3/ Conversion Benefits
- ✅ **Modern Standard**: OpenAPI 3.0 ecosystem compatibility
- ✅ **Enhanced Features**: Better parameter handling and responses
- ✅ **Tool Support**: Wider generator and tooling support
- ✅ **Future-Proof**: Ready for next-generation API tools

## 📋 Source Information

### Original Sources
- **Alfresco API Explorer**: [api-explorer.alfresco.com](https://api-explorer.alfresco.com/api-explorer/)
- **Official Documentation**: [Alfresco REST API Guide](https://support.hyland.com/r/Alfresco/Alfresco-Content-Services/25.1/Alfresco-Content-Services/Develop/REST-API-Guide)
- **Version**: Alfresco Content Services 23.2+

### Processing Tools
- **Preprocessing**: Custom YAML processing and validation
- **Conversion**: [swagger2openapi](https://github.com/Mermade/oas-kit) for OpenAPI 3.0
- **Validation**: [openapi-spec-validator](https://github.com/p1c2u/openapi-spec-validator)

## 🔄 Update Workflow

### 1. Download Latest Specifications
```bash
# Visit https://api-explorer.alfresco.com/api-explorer/
# Download each API specification to openapi/openapi2/
```

### 2. Process and Clean
```bash
# Run preprocessing pipeline
python scripts/preprocess_openapi.py
```

### 3. Convert to OpenAPI 3.0
```bash
# Convert processed files
python scripts/convert_to_openapi3.py
```

### 4. Regenerate Library
```bash
# Full regeneration
python scripts/generate_hybrid_pipeline.py
```

## 🎯 Integration Examples

### Direct YAML Loading
```python
import yaml

# Load any specification
with open('openapi/openapi2-processed/alfresco-core.yaml') as f:
    spec = yaml.safe_load(f)
    
print(f"API: {spec['info']['title']}")
print(f"Endpoints: {len(spec['paths'])}")
```

### Specification Analysis
```python
# Compare versions
import yaml

def analyze_spec(filepath):
    with open(filepath) as f:
        spec = yaml.safe_load(f)
    return {
        'version': spec.get('swagger') or spec.get('openapi'),
        'title': spec['info']['title'],
        'endpoints': len(spec['paths']),
        'models': len(spec.get('definitions', spec.get('components', {}).get('schemas', {})))
    }

# Compare all versions
for version in ['openapi2', 'openapi2-processed', 'openapi3']:
    result = analyze_spec(f'openapi/{version}/alfresco-core.yaml')
    print(f"{version}: {result}")
```

### Multi-Language Generation
```bash
# Generate for multiple languages using OpenAPI 3.0
languages=("python" "javascript" "java" "csharp" "go")
for lang in "${languages[@]}"; do
    openapi-generator generate \
        -i openapi/openapi3/alfresco-core.yaml \
        -g $lang \
        -o generated/$lang/
done
```

## 📚 Related Documentation

- **[Main README](../README.md)** - Complete library documentation
- **[Generation Scripts](../scripts/)** - Automated processing tools
- **[Python Package](../python_alfresco_api/)** - Generated library code
- **[Examples](../examples/)** - Usage examples and patterns
- **[Tests](../tests/)** - Comprehensive test suite

## 🔗 External Resources

- **[OpenAPI Specification](https://spec.openapis.org/)** - Official OpenAPI documentation
- **[Swagger Tools](https://swagger.io/tools/)** - Swagger ecosystem tools
- **[OpenAPI Generator](https://openapi-generator.tech/)** - Multi-language code generation
- **[Postman Integration](https://learning.postman.com/docs/integrations/available-integrations/working-with-openAPI/)** - API testing and documentation

---

**This directory contains the definitive OpenAPI specifications for Alfresco Content Services, organized for optimal code generation and ecosystem integration.** 