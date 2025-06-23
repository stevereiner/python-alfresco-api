# Original OpenAPI 2.0 Specifications

This directory contains the **original, unprocessed OpenAPI 2.0 (Swagger) specifications** downloaded directly from the Alfresco API Explorer.

## 📁 Contents

| File | Size | Description |
|------|------|-------------|
| `alfresco-auth.yaml` | 5.1 KB | Authentication API - Raw from Alfresco |
| `alfresco-core.yaml` | 307 KB | Core API - Raw from Alfresco |
| `alfresco-discovery.yaml` | 4.3 KB | Discovery API - Raw from Alfresco |
| `alfresco-search.yaml` | 40 KB | Search API - Raw from Alfresco |
| `alfresco-workflow.yaml` | 63 KB | Workflow API - Raw from Alfresco |
| `alfresco-model.yaml` | 17 KB | Model API - Raw from Alfresco |
| `alfresco-search-sql.yaml` | 7.7 KB | Search SQL API - Raw from Alfresco |

## 🔗 Source

These files are downloaded from:
- **Alfresco API Explorer**: [api-explorer.alfresco.com](https://api-explorer.alfresco.com/api-explorer/)
- **Version**: Alfresco Content Services 23.2+
- **Format**: OpenAPI 2.0 (Swagger)

## ⚠️ Usage Note

**These are baseline reference files.** For code generation, use the processed versions in `../openapi2-processed/` which have been cleaned and optimized for better compatibility.

## 🔄 Update Process

To update these files:

1. Visit [Alfresco API Explorer](https://api-explorer.alfresco.com/api-explorer/)
2. Navigate to each API section
3. Download the OpenAPI specification
4. Replace the corresponding file in this directory
5. Run the processing pipeline to update the processed versions

## 📋 File Status

- ✅ **Complete**: All 7 Alfresco REST APIs included
- ✅ **Current**: Based on latest Alfresco Content Services
- ⚠️ **Raw**: Unprocessed, may contain formatting inconsistencies
- ⚠️ **Direct Use**: Not recommended for code generation without processing 