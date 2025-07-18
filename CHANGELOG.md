# Changelog

All notable changes to python-alfresco-api will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2025-07-18

### Added
  - Implemented hierarchical client architecture with three-tier organization  and lazy loading (3 tiers doesn't count optional master). This is generated from raw clients (previously had 7 files one per client). 
  - Pydantic models are in the hierarchy (more Pydantic models to come in 1.2) 
  - Added utility modules (content_utils_highlevel, version_utils_highlevel, node_utils_highlevel) that simplify operations (upload, download, checkin / checkout versioning, node operations, search).

### Added
  - Added examples/operations/ folder easy-to-use code demonstrating high-level utilities (upload, download, checkin / checkout versioning, node operations, searc

### Added
  - Reorganized scripts into logical 5-folder structure (code-gen, doc-gen, utility, testing, examples-and-docs). 
  - For v1.1, scripts added to generate hierarchical clients  from raw clients with some pydantic models. 
  - Added script(s) for doc gen

### Added
  - For v1.1 added testing for high level utilities
  - Added high level api testing of all operations needed forthe Python Alfresco MCP Server                                                    
  - Added tests of all sync and async node operations in nodes folder. 
  - Added tests that call gets throughout clients with sync, async, and detailed sync/async. Sone tests removed

### Documentation
  - v1.1 now has generated hierarchical linked md docs with for client APIs and models  
  - Arch, models, and client type diagrams added. 
  - Updated docs to cover v1.1.0 hierarchical client architecture. 
  - Documented high-level utilities allow less code needed for common operations.  
  - Documented Pydantic models and conversion utils

### Documentation
  - Readme extensively updated covering v1.1, with some details moved to docs. 
  - Readme: see link to Architecture Overview and Diagram! 
  - Akso a diagram in docs/pydantic_models_guide.md and in client_types_guide.md. 
  - Readme: link to Python Alfresco MCP Server. 
  - Readme has a gt clone command to get a Alfresco Community docker from github if you need it. 
  - Readme covers venv setup, pip install, env setup, factory pattern, authentication, syn/async usuage, operations using siimple util function, 
    model arch and conversion, event system, testing, project structure, requirements, ref to package developer guide, ref to related projects
  - Added sample-dot-env.txt example for.env file

#### Changed
  - In pyproject.toml minimum now Python 3.10, added Python 3.13. 
  - .gitignore ignores Cursor files
  - run_tests.py updated for tests available in v1.1 




### Added
- **OAuth2 Authentication Support**: Enterprise-ready OAuth2 authentication for cloud and SSO environments
  - `OAuth2AuthUtil` class supporting client credentials and authorization code flows
  - Automatic token refresh and expiration handling
  - Environment variable configuration for OAuth2 credentials
  - Support for custom token endpoints and scopes
  - Compatible with MCP (Model Context Protocol) OAuth2 requirements
  - Smart endpoint detection for common Alfresco OAuth2 patterns
  - Seamless integration with existing ClientFactory and auth architecture
- **Environment Configuration Support**: Automatic loading from .env files and environment variables
- `sample-dot-env.txt`: Sample environment configuration file for easy setup
- `ClientFactory` now supports priority-based configuration: explicit parameters > environment variables > defaults
- Support for multiple environment variable names (ALFRESCO_URL/ALFRESCO_BASE_URL, ALFRESCO_VERIFY_SSL/ALFRESCO_SSL_VERIFY)
- `get_config_info()` method for configuration debugging
- `from_env()` class method for explicit environment-based initialization
- Comprehensive environment configuration documentation in `docs/ENVIRONMENT_CONFIGURATION.md`

### Changed
- **Enhanced SSL Handling**: Now matches raw client capabilities for SSL certificate verification
  - `verify_ssl=True` - Enable SSL verification (default)
  - `verify_ssl=False` - Disable SSL verification (not recommended for production)
  - `verify_ssl="/path/to/cert.pem"` - Custom certificate bundle path support (new)
  - Environment variable support for all modes: `ALFRESCO_VERIFY_SSL=/etc/ssl/certs/custom-ca.pem`
  - Full compatibility with underlying `AuthenticatedClient` SSL options
  - **Shared AuthUtil**: Single authentication session across all API clients for better performance and consistency
  - **Centralized Environment Loading**: Only in ClientFactory, eliminating scattered .env handling
- **Simplified Client Authentication**: Clients now accept username/password directly, eliminating need for auth_util parameters
  - ClientFactory constructor parameters are now optional with automatic environment loading
  - Updated README with environment configuration examples

## [1.0.0] - 2025-06-25

### Added
- Initial stable release of python-alfresco-api
- Complete Alfresco REST API client library with comprehensive coverage
- **Event Gateway and Event Support**: Full integration with Alfresco Event Gateway for real-time event processing
- Modern Pydantic v2 models for all API endpoints with full type safety
- Configuration system with development-friendly defaults (localhost:8080, admin/admin)
- Standardized URL architecture eliminating confusion between server URLs and API endpoints
- Async support across all API clients with proper error handling
- Comprehensive examples and documentation for all major use cases
- Support for both Community Edition (ActiveMQ) and Enterprise Edition (Event Gateway) events
- LLM integration patterns and Model Context Protocol (MCP) server examples

### Changed
- **Switched to openapi-python-client for better Python code generation**: Improved from previous generators for more reliable, maintainable client code
- Adopted hybrid approach combining datamodel-code-generator (Pydantic models) + openapi-python-client (HTTP clients)
- Implemented enterprise-grade architecture with individual API clients and factory patterns

### Technical Features
- 328 Pydantic v2 models across 7 Alfresco APIs
- 343 HTTP client files with full async support
- ClientFactory pattern for easy client instantiation
- AuthUtil for streamlined authentication workflows
- Automatic URL normalization and validation
- Multiple configuration sources: direct parameters > environment variables > config files > defaults
- Comprehensive test framework with 25+ test scenarios

### Documentation
- Complete API documentation index
- Authentication and authorization guides
- Event Gateway integration guide
- Pydantic models usage examples
- Master client usage patterns
- URL architecture examples

