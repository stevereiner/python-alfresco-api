# Changelog

All notable changes to python-alfresco-api will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-25

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

## [Unreleased]

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
- **Clean Architecture Implementation**: Centralized authentication and configuration management
  - **Shared AuthUtil**: Single authentication session across all API clients for better performance and consistency
  - **Centralized Environment Loading**: Only in ClientFactory, eliminating scattered .env handling
  - **Factory Pattern Encouraged**: README simplified to promote factory usage over direct client instantiation
  - **Enterprise Benefits**: Improved authentication flow, ticket management, and separation of concerns
- **Simplified Client Authentication**: Clients now accept username/password directly, eliminating need for auth_util parameters
- ClientFactory constructor parameters are now optional with automatic environment loading
- Updated README with environment configuration examples

