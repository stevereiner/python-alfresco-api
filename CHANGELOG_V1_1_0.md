# Changelog - v1.1.0

## [1.1.0] - 2025-01-16

### Architecture Changes
- Introduced V1.1 Hierarchical Architecture with three-tier organization (Global → API-Level → Operation-Specific)
- Added hierarchical client access pattern: `core_client.nodes.create()`, `core_client.versions.checkout()`
- Implemented lazy loading for improved client initialization performance
- Improved sync/async separation to eliminate event loop conflicts in MCP environments

### High-Level Utilities
- Added `content_utils_highlevel.py` for simplified content management operations
- Added `version_utils_highlevel.py` for document versioning workflows
- Added `node_utils_highlevel.py` for streamlined node operations
- Included auto-versioning, batch operations, and comprehensive error handling

### Documentation
- Added `docs/ESSENTIAL_OPERATIONS_GUIDE.md` with complete operation coverage
- Enhanced `docs/PACKAGE_DEVELOPERS_GUIDE.md` with 3-step generation process documentation
- Added `docs/CLIENT_TYPES_GUIDE.md` with decision matrix for client approaches
- Reorganized README.md to focus on user-facing features

### Examples
- Added `examples/operations/` folder with Windows-compatible code
- Included `upload_document.py`, `versioning_workflow.py`, `basic_operations.py`, `search_operations.py`
- Provided production-ready examples with comprehensive error handling
- Improved Windows compatibility with ASCII tags replacing Unicode emojis

### Testing
- Added `test_highlevel_utils.py` for high-level utilities testing
- Enhanced `test_mcp_v11_true_high_level_apis_fixed.py` with 15 MCP operations
- Improved integration testing patterns
- Achieved 46% test coverage with professional test runner

### Development Tools
- Reorganized scripts into logical 5-folder structure (code-gen, doc-gen, utility, testing, examples-and-docs)
- Automated V1.1 generation pipeline
- Improved documentation generation with real method signatures
- Generated 54+ API documentation files with complete parameter documentation

### MCP Integration
- Fixed all 15 MCP operations with 100% success rate
- Resolved multipart boundary errors, authentication issues, and parsing problems
- Optimized sync patterns for MCP server environments
- Added utility functions for MCP server integration

### Performance & Quality
- Improved client initialization performance through lazy loading
- Integrated Pydantic v2 models for type safety
- Added comprehensive exception management in utilities
- Simplified syntax with `client.api.operation()` pattern

### Integration & Compatibility
- Maintained full backward compatibility with v1.0.2 patterns
- Added conversion utilities for Pydantic ↔ attrs model transformation
- Included field mapping with automatic snake_case ↔ camelCase conversion
- Provided direct HTTPx client access for advanced use cases

### Summary
- High-level utilities allow less code needed for common operations
- Hierarchical client architecture generated from raw clients
- 54+ generated documentation files
- 4 production-ready examples with comprehensive test patterns
- 51+ scripts organized into logical categories

---

### Migration Notes
- V1.0.2 patterns continue to work unchanged
- V1.1 hierarchical access is additive (opt-in)
- High-level utilities are optional enhancements
- All examples demonstrate both V1.0.2 and V1.1 patterns

### Breaking Changes
- None - all changes are additive and backward compatible

### Deprecations
- None in this release 