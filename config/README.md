# Configuration Files

This folder contains OpenAPI Python Client configuration files for all Alfresco APIs.

## Available Configurations

### Individual API Clients

| File | API | Package Name | Description |
|------|-----|--------------|-------------|
| auth.yaml | Authentication | auth_client | User authentication and tickets |
| core.yaml | Core Repository | core_client | Nodes, people, sites, content |
| discovery.yaml | Discovery | discovery_client | Server information |
| search.yaml | Search | search_client | Content search and queries |
| workflow.yaml | Workflow | workflow_client | Process definitions |
| model.yaml | Model | model_client | Content models and aspects |
| search_sql.yaml | Search SQL | search_sql_client | SQL-based search |

### Unified Configuration

| File | Use Case | Package Name | Description |
|------|----------|--------------|-------------|
| general.yaml | Unified Package | alfresco_client | Single package for all APIs |

## Usage

Generate specific API client:
openapi-python-client generate --path openapi/openapi3/alfresco-auth.yaml --config config/auth.yaml --output-path clients/auth_client

## Benefits

- Short Names: auth_client instead of alfresco_content_services_rest_api_client
- Organized: All configurations in one place
- Consistent: Same structure across all APIs
- Flexible: Choose individual or unified approach
