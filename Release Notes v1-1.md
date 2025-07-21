## [1.1.0] - 2025-07-21

### Changes
  - Updated __init__.py files to have all things in __all_  so they get included in the package 
  - Now have basic requirements.txt, requirements-dev.txt for development.txt,  and new requirements-codegen.txt for advanced development where raw clients, 
    high level clients, or documentation  needs to be regenerated
  - Run_tests.py performance test is now the time of running the whole test suite, not a few client creates
  - Pyproject has added includes for package and sdist
  - Fix gitignore to not cause downloads/ dirignored so core/downloads and raw core /downloads get checked in
 
### Documentation
  - Readme: reworded build with source description
  - Readme: tests section at the end now develop and test
  - Removed docs for eliminated core.folders (use ops in nodes)

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
