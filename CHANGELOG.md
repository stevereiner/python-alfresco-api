# Changelog

All notable changes to python-alfresco-api will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.4] - 2025-10-01

### Added
- Implemented the methods of 15 subclients that had placeholder sections
- `test_todays_15_subclients.py` test the timeout handling the 15 subclients with the implementation methods added today

### Changed
- Same timeout fix by using the parent raw client
- Removed some use of emojis in logging from some files to avoid errors in windows consoles
- `pyproject.toml` version change from 1.1.2 to 1.1.4 (1.1.3 not in pypi)
- `publish_to_pypi` removed specific version info, don't stop if test publish doesn't work since the website never works, gives 403

## [1.1.3] - 2025-09-30

### Fixed
- Fixed timeout handling in 7 top level clients yesterday, this fixed 16 subclient timeout handling
- To fix 16 subclients timeout handling and improve the code, the subclients use the raw client from the parent client instead recreating their own raw clients
- Fixed in `authentication_client.py` to import correct raw client model packages

### Changed
- Subclients now have `raw_client()` and `httpx_client()` properties that return parent client properties and replace any `_get_raw_client()` and `get_httpx_client()` methods
- Parent clients give subclient constructors themselves instead of client factory

### Added
- `test_client_factory_configuration.py` now also tests previous 16 subclients handling of timeout setup in addition to previous testing of the 7 parent clients


## [1.1.2] - 2025-09-29

### Enhanced
- **Timeout Configuration System**: Comprehensive overhaul of timeout handling throughout the client hierarchy
  - Removed hardcoded 30-second defaults from `AuthUtil` and `OAuth2AuthUtil` constructors
  - Implemented proper None timeout handling - when no timeout specified, system/ticket defaults apply
  - Enhanced parameter priority chain: `auth_util parameters > explicit parameters > environment variables > None`
  - Updated all 7 main clients to conditionally pass timeout to `AuthenticatedClient` only when specified
  - Modified httpx client creation in auth utilities to not get a timeout if None

### Added
- **Parameter Priority Logic**: Enhanced `ClientFactory` to respect auth_util parameters as highest priority
  - Auth_util parameters (timeout, base_url, verify_ssl, username, password) take precedence over factory parameters
  - Added username/password property access from any auth_util type
  - Comprehensive parameter propagation verification throughout client hierarchy
- **Environment Configuration**: Extended timeout support in environment variables
  - Added `ALFRESCO_TIMEOUT` environment variable support
  - Added `ALFRESCO_FILE_IO_TIMEOUT` configuration option (not used currently)
  - Updated priority documentation in `sample-dot-env.txt`
- **Comprehensive Testing**: New test suite `test_client_factory_configuration.py` with 15 test methods
  - Tests timeout priority chain across all scenarios
  - Verifies parameter propagation to raw and httpx clients
  - Validates MCP server pattern compatibility
  - Tests None timeout handling and system default behavior

### Changed
- **ClientFactory**: Enhanced constructor parameter handling
  - Changed `timeout: int = 30` to `timeout: Optional[int] = None`
  - Improved auth_util parameter extraction and priority logic
  - **Authentication Utilities**: Improved timeout parameter handling
  - `AuthUtil` and `OAuth2AuthUtil` now accept `timeout: Optional[int] = None`
  - httpx client creation doesn't use timeout if None
  - Updated docstrings to reflect "None = use system defaults" behavior

### Documentation
- **README.md**: Enhanced Factory Pattern and Authentication sections
  - Added parameter priority documentation
  - Clarified timeout behavior when not specified
  - Added platform-specific .env file setup instructions (copy for Windows, cp for Linux/Mac)
- **sample-dot-env.txt**: timeout configuration examples
  - Added timeout configuration section with examples
  - Documented parameter priority order
  - Added file I/O timeout option for large operations (not used currently)

### Technical
- **Content Utilities**: Enhanced `content_utils_highlevel.py`
  - Improved Share-style create/upload functionality
  - Better version handling (documents created with version 1.0)
- **Project Configuration**: Updated version and build configuration
  - Version bumped from 1.1.1 to 1.1.2 in `pyproject.toml`
  - Cleaned up manifest includes


## [1.1.1] - 2025-07-21

### Changes
  - Updated __init__.py files to have all things in __all_  so they get included in the package 
  - Now have basic requirements.txt, requirements-dev.txt for development.txt,  and new
    requirements-codegen.txt for advanced development where raw clients, 
    high level clients, or documentation  needs to be regenerated
  - Run_tests.py performance test is now the time of running the whole test suite, not a few client creates
  - Pyproject has added includes for package and sdist
  - Fix gitignore to not cause downloads/ ignored so core/downloads and raw core /downloads get checked in
  - version updated to v1.1.1
 
### Documentation
  - Readme: reworded build with source description
  - Readme: tests section at the end now develop and test
  - Removed docs for eliminated core.folders (use ops in nodes)

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

### Changed
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

