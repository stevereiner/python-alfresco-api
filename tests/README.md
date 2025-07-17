# Testing Guide - Python Alfresco API v1.1

This directory contains essential tests for the Python Alfresco API v1.1 hierarchical architecture, focusing on high-level APIs and MCP server integration.

## 🧪 Test Categories

### Core Foundation Tests (11 tests)
- **`test_basic.py`** - Basic client functionality and imports (6 tests)
- **`test_simple.py`** - Simple API operations validation (5 tests)

### High-Level API Coverage Tests (45 tests)
- **`test_all_gets_high_level.py`** - High-level sync GET operations across all 18 Core API subsections (19 tests)
- **`test_all_gets_high_level_async.py`** - High-level async GET operations across all 18 Core API subsections (19 tests)
- **`test_all_gets_high_level_detailed.py`** - Detailed sync GET operations with parameter variations (3 tests)
- **`test_all_gets_high_level_detailed_async.py`** - Detailed async GET operations with parameter variations (4 tests)

### Coverage Recovery Tests (6 tests)
- **`test_comprehensive_coverage_recovery.py`** - Factory patterns, model instantiation, and auth client coverage (6 tests)

### Integration Tests (Available but not in standard collection)
- **`test_mcp_v11_true_high_level_apis_fixed.py`** - Complete MCP server integration test with 15 operations
- **`test_highlevel_utils.py`** - High-level utility modules test (content_utils_highlevel, version_utils_highlevel, node_utils_highlevel)

### Specialized Testing
- **`nodes/`** - Directory for sync/async node operations testing (comprehensive 19-operation validation)

## 📊 Current Test Status

- **✅ Total Tests Available**: 67 tests collected by pytest
- **✅ Core Foundation**: 11 tests (basic functionality working)
- **✅ High-Level API Coverage**: 45 tests (comprehensive GET method validation)
- **✅ Coverage Recovery**: 6 tests (factory/model coverage)
- **✅ Current Coverage**: 44-46% (with comprehensive high-level API tests)
- **🎯 Target Coverage**: 80%+ (professional standard)
- **⚠️ Integration Tests**: Require live Alfresco server (not included in standard runs)

## 🚀 Running Tests

### Professional Test Runner (Recommended)
```bash
# Use the comprehensive test runner from project root
python run_tests.py

# Features:
# - Colored output and progress indicators
# - Automatic coverage reporting (HTML + terminal)
# - Performance metrics and timing
# - Environment validation
# - Live server detection
# - Auto directory detection (works from any directory)
```

### Quick Test Runs by Category
```bash
# Run core foundation tests (11 tests)
pytest tests/test_basic.py tests/test_simple.py -v

# Run high-level API coverage tests (45 tests) 
pytest tests/test_all_gets_high_level.py tests/test_all_gets_high_level_async.py tests/test_all_gets_high_level_detailed.py tests/test_all_gets_high_level_detailed_async.py -v

# Run coverage recovery tests (6 tests)
pytest tests/test_comprehensive_coverage_recovery.py -v

# Run all collected tests (67 tests)
pytest tests/ -v

# Run with coverage for specific categories
pytest tests/test_basic.py tests/test_simple.py --cov=python_alfresco_api --cov-report=term-missing
```

### Quick Test Run
```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest tests/ -v

# Run specific test files
pytest tests/test_basic.py
pytest tests/test_mcp_v11_true_high_level_apis_fixed.py
```

### MCP Integration Testing
```bash
# Run the comprehensive MCP test (requires live Alfresco server)
pytest tests/test_mcp_v11_true_high_level_apis_fixed.py -v
```

### Sync/Async Node Testing
```bash
# Run specialized node operation tests
pytest tests/nodes/ -v
```

### High-Level Utilities Testing
```bash
# Test the new high-level utility modules (requires live Alfresco server)
pytest tests/test_highlevel_utils.py -v

# Test individual utility modules standalone
python tests/test_highlevel_utils.py
```

## 📊 Code Coverage

### Automatic Coverage (via run_tests.py)
```bash
# Quick coverage with basic tests (recommended for development)
python run_tests.py

# Works from any directory - automatically detects project structure
# From project root: python run_tests.py  
# From tests/: python ../run_tests.py

# The script automatically:
# - Runs core tests with coverage (~28% baseline coverage)
# - Generates HTML report at htmlcov/index.html
# - Shows terminal coverage summary with color coding
# - Provides performance metrics and timing
# - Checks for live Alfresco server availability
# - Professional output with colored status indicators
```

### Comprehensive Coverage Testing
```bash
# For 44-46% coverage with high-level API tests (recommended baseline)
pytest tests/test_all_gets_high_level.py tests/test_all_gets_high_level_async.py --cov=python_alfresco_api --cov-report=html --cov-report=term-missing

# For ~30% coverage with foundation + recovery tests  
pytest tests/test_basic.py tests/test_simple.py tests/test_comprehensive_coverage_recovery.py --cov=python_alfresco_api --cov-report=html

# MCP integration test (adds significant coverage)
pytest tests/test_mcp_v11_true_high_level_apis_fixed.py --cov=python_alfresco_api --cov-report=html

# High-level API operations
pytest tests/test_all_gets_high_level.py --cov=python_alfresco_api --cov-report=html

# High-level utility modules
pytest tests/test_highlevel_utils.py --cov=python_alfresco_api --cov-report=html

# Node operations (sync/async)
pytest tests/nodes/ --cov=python_alfresco_api --cov-report=html

# Combined comprehensive test (requires live Alfresco server)
pytest tests/test_basic.py tests/test_simple.py tests/test_mcp_v11_true_high_level_apis_fixed.py tests/nodes/ --cov=python_alfresco_api --cov-report=html --cov-report=term-missing
```

### Manual Coverage Commands
```bash
# Run tests with coverage
pytest tests/ --cov=python_alfresco_api --cov-report=term-missing

# Generate HTML coverage report
pytest tests/ --cov=python_alfresco_api --cov-report=html

# Run specific tests with coverage
pytest tests/test_mcp_v11_true_high_level_apis_fixed.py --cov=python_alfresco_api --cov-report=term-missing

# View HTML coverage report
# Open: htmlcov/index.html in your browser
```

### Coverage Configuration
Coverage is configured in `pyproject.toml`:
```toml
[tool.coverage.run]
source = ["python_alfresco_api"]
omit = ["tests/*", "setup.py"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise AssertionError", 
    "raise NotImplementedError",
]
```

### Coverage Targets
- **Basic Tests Only**: ~28% baseline coverage (core functionality)
- **With High-Level API Tests**: ~44-46% coverage (comprehensive GET operations across all APIs)
- **With MCP Integration**: ~60%+ coverage (includes real API usage)
- **Comprehensive Tests**: ~80%+ coverage target (all test suites)
- **V1.1 Architecture**: Focus on hierarchical clients and core operations
- **MCP Integration**: Coverage of MCP-compatible utilities and formatters
- **Sync/Async Operations**: Both patterns covered

### Coverage Notes
- **Generated Code**: Raw clients (0% coverage) are auto-generated and tested via integration
- **Focus Areas**: V1.1 hierarchical architecture, MCP utilities, and client factories
- **Real Usage**: MCP integration test provides the most meaningful coverage

## 📝 Test Configuration

### Environment Setup
Tests use the following configuration:
- **Base URL**: `http://localhost:8080` (server URL - API endpoints constructed automatically)
- **Username**: `admin`
- **Password**: `admin`
- **SSL Verification**: Disabled for testing

> **Note:** We use the standardized URL architecture where `base_url` refers to the Alfresco **server URL**, not the API endpoint. The library automatically constructs API URLs as `base_url + "/alfresco/api/..."`

## 🔧 Test Architecture

### V1.1 Hierarchical Architecture
All tests use the modern V1.1 hierarchical architecture:

```python
from python_alfresco_api import ClientFactory

# V1.1 hierarchical pattern
factory = ClientFactory(
    base_url="http://localhost:8080",
    username="admin",
    password="admin"
)

# Get hierarchical clients
core_client = factory.create_core_client()
search_client = factory.create_search_client()

# Use hierarchical operations
folder = core_client.nodes.create_folder(name="Test Folder", parent_id="-my-")
results = search_client.search.search_content("test query")
```

### MCP Server Patterns
The comprehensive MCP test validates 15 operations:
- **Search operations** (4): content search, advanced search, metadata search, CMIS search
- **Discovery operations** (1): repository info
- **Content & Node operations** (6): browse, create folder, upload, get properties, update properties, delete
- **Versioning operations** (4): checkout, checkin, cancel checkout, download

## ⚠️ Important Notes

### Live Server Requirements
Most tests require a running Alfresco server:
- Start Alfresco with Docker Compose
- Ensure default admin credentials work
- Tests will skip or fail gracefully if server is unavailable

### V1.1 Architecture Focus
These tests focus on the V1.1 hierarchical architecture:
- ✅ Clean hierarchical client organization
- ✅ Perfect sync/async separation
- ✅ MCP server compatibility
- ✅ High-level utility functions

## 🎯 Test Development Guidelines

### Writing New Tests
1. Use V1.1 hierarchical client patterns
2. Follow sync/async separation principles
3. Include proper error handling
4. Test both sync and async variants
5. Validate MCP server compatibility

### Test Categories
- **Basic tests**: Core functionality and imports
- **High-level tests**: Complex workflows and utilities
- **MCP tests**: Full MCP server integration scenarios
- **Node tests**: Specialized sync/async node operations

## 🐛 Troubleshooting Tests

### Common Issues

#### 1. Authentication Failures
```bash
# Check Alfresco is running
curl http://localhost:8080/alfresco/api/-default-/public/alfresco/versions/1/discovery
```

#### 2. Sync/Async Issues
Ensure proper separation:
- Sync methods: `operation.sync()`
- Async methods: `await operation.asyncio()`
- No mixing of sync/async patterns

#### 3. MCP Integration Issues
Check the comprehensive test for working patterns:
```python
# Example working pattern
core_client = factory.create_core_client()
folder = core_client.nodes.create_folder(name="Test", parent_id="-my-")
```

## 📈 Test Results Summary

### V1.1 Architecture Validation
```
✅ All hierarchical clients working
✅ 15/15 MCP operations successful (100%)
✅ Sync/async patterns both working
✅ High-level utilities validated
✅ Production-ready for MCP servers
```

### Key Achievements
- **Perfect MCP integration**: 100% success rate for all 15 operations
- **Clean architecture**: V1.1 hierarchical organization working
- **Sync/async separation**: Both patterns working perfectly
- **Real-world validation**: Tested with live Alfresco servers

## 📚 Related Documentation

- **[API Documentation Index](../docs/API_DOCUMENTATION_INDEX.md)** - Complete API reference
- **[Authentication Guide](../docs/AUTHENTICATION_GUIDE.md)** - Authentication setup
- **[README.md](../README.md)** - Project overview and setup

Start testing with `python run_tests.py` (recommended) for comprehensive testing with coverage, or `pytest tests/test_mcp_v11_true_high_level_apis_fixed.py -v` for MCP integration validation! 