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

### Planned
- Additional MCP server implementations
- GraphRAG integration patterns
- Performance optimizations
- Extended event handling capabilities 