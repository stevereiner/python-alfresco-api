# Testing Guide - Python Alfresco API v1.0

This directory contains comprehensive tests for the Python Alfresco API v1.0, covering unit tests, integration tests, and live server validation.

## 📊 Current Test Status

- **✅ 106/106 tests passing** (100% success rate)
- **✅ 80% code coverage** (excellent for v1.0 release)
- **✅ Live integration** validated with Alfresco Community 23.2.0 and 25.1
- **✅ All test categories** working perfectly

## 🧪 Test Categories

### Unit Tests
- **`test_current_architecture.py`** - Core architecture validation
- **`test_individual_apis.py`** - Individual API client testing
- **`test_client_dependencies.py`** - Client dependency validation

### Integration Tests  
- **`test_integration_live_server.py`** - Live Alfresco server integration
- **`test_enhanced_coverage.py`** - Enhanced functionality coverage
- **`test_complete_summary.py`** - Complete workflow testing

### Authentication Tests
- **`test_authutil_fixed.py`** - AuthUtil functionality
- **`test_auth_debug.py`** - Authentication debugging
- **`test_working_api.py`** - Working API validation

### Coverage Tests
- **`test_100_percent_coverage.py`** - Comprehensive coverage testing
- **`test_final_coverage_push.py`** - Final coverage validation

## 🚀 Running Tests

### Quick Test Run
```bash
# Professional test runner (recommended)
python run_tests.py                    # From project root
python ../run_tests.py                 # From tests/ directory

# Direct pytest commands
pytest tests/                          # Run all tests
pytest tests/ --cov=python_alfresco_api  # Run with coverage
```

### Specific Test Categories
```bash
# Unit tests only
pytest tests/test_current_architecture.py
pytest tests/test_individual_apis.py

# Integration tests
pytest tests/test_integration_live_server.py

# Authentication tests
pytest tests/test_authutil_fixed.py

# Coverage tests
pytest tests/test_enhanced_coverage.py
```

### Live Server Testing
```bash
# Test with live Alfresco server (requires running Alfresco)
pytest tests/test_integration_live_server.py -v
```

## 📝 Test Configuration

### Environment Setup
Tests use the following configuration:
- **Base URL**: `http://localhost:8080` (server URL - API endpoints constructed automatically)
- **Username**: `admin`
- **Password**: `admin`
- **SSL Verification**: Disabled for testing

> **Note:** We use the standardized URL architecture where `base_url` refers to the Alfresco **server URL**, not the API endpoint. The library automatically constructs API URLs as `base_url + "/alfresco/api/..."`

### Test Data
Tests create minimal test data and clean up automatically.

### Coverage Configuration
Coverage is configured in `pyproject.toml`:
```toml
[tool.coverage.run]
source = ["python_alfresco_api"]
omit = [
    "*/tests/*",
    "*/raw_clients/*",
    "setup.py"
]
```

## 🔧 Test Architecture

### Modern Testing Patterns
All tests use the modern `python_alfresco_api` architecture:

```python
from python_alfresco_api import ClientFactory
from python_alfresco_api.auth_util import AuthUtil
from python_alfresco_api.clients.core_client import AlfrescoCoreClient

# Modern test setup
factory = ClientFactory(
    base_url="http://localhost:8080",
    username="admin",
    password="admin"
)

clients = factory.create_all_clients()
```

### Test Utilities
Common test utilities in `conftest.py`:
- Client factory setup
- Authentication helpers
- Test data management
- Cleanup procedures

## 📊 Coverage Reports

### Generate Coverage Report
```bash
# HTML coverage report
pytest tests/ --cov=python_alfresco_api --cov-report=html

# Terminal coverage report
pytest tests/ --cov=python_alfresco_api --cov-report=term-missing
```

### Coverage Targets
- **Core Components**: 80%+ coverage
- **Individual Clients**: 80%+ coverage each
- **Authentication**: 80%+ coverage
- **Models**: 100% coverage (Pydantic models)

## ⚠️ Important Notes

### Live Server Requirements
Some tests require a running Alfresco server:
- Start Alfresco with Docker Compose
- Ensure default admin credentials work
- Tests will skip if server is unavailable

### Generated Client Tests
**🚫 DO NOT USE** the auto-generated test suites in `python_alfresco_api/raw_clients/*/test/`:
- These are auto-generated and may not work correctly
- Use the comprehensive tests in this directory instead
- Our tests cover the same functionality with better reliability

### Test Dependencies
Install test dependencies:
```bash
pip install -r tests/requirements-test.txt
```

## 🎯 Test Development Guidelines

### Writing New Tests
1. Use modern `python_alfresco_api` imports
2. Follow existing test patterns
3. Include proper error handling
4. Add cleanup procedures
5. Document test purpose clearly

### Test Naming
- `test_<component>_<functionality>.py` for unit tests
- `test_integration_<scenario>.py` for integration tests
- `test_<category>_<specific_case>.py` for specialized tests

### Mock vs Live Testing
- Use mocks for unit tests
- Use live server for integration tests
- Gracefully handle server unavailability

## 🐛 Troubleshooting Tests

### Common Issues

#### 1. Import Errors
```python
# ❌ Old import (will fail)

# ✅ New import (correct)
from python_alfresco_api import ClientFactory
```

#### 2. Authentication Failures
```python
# Check Alfresco is running
curl http://localhost:8080/alfresco/api/-default-/public/alfresco/versions/1/discovery
```

#### 3. Coverage Issues
```bash
# Clear coverage cache
rm -rf .coverage htmlcov/

# Reinstall in development mode
pip install -e .
```

#### 4. Test Isolation
Each test should be independent:
- Use fresh client instances
- Clean up test data
- Don't depend on test order

### Debug Mode
Run tests with debug output:
```bash
pytest tests/ -v -s --tb=long
```

## 📈 Test Results Summary

### Latest Test Run
```
✅ 106/106 tests passing (100% success rate)
✅ 80% code coverage achieved
✅ All API clients tested
✅ Live integration validated
✅ Authentication flows working
✅ Error handling comprehensive
```

### Performance
- **Test execution time**: ~30 seconds for full suite
- **Coverage generation**: ~10 seconds additional
- **Live server tests**: ~15 seconds (when server available)

## 🎉 Success Metrics

The Python Alfresco API v1.0 testing achieves:
- ✅ **100% test success rate** - All tests passing
- ✅ **80% code coverage** - Excellent coverage for v1.0
- ✅ **Live validation** - Tested with real Alfresco servers
- ✅ **Comprehensive coverage** - All components tested
- ✅ **Modern architecture** - Uses latest patterns
- ✅ **Production ready** - Robust error handling

## 📚 Related Documentation

- **[API Documentation Index](../docs/API_DOCUMENTATION_INDEX.md)** - Complete API reference
- **[Authentication Guide](../docs/AUTHENTICATION_GUIDE.md)** - Authentication setup
- **[README.md](../README.md)** - Project overview and setup

Start testing with `python run_tests.py` (from project root) or `python ../run_tests.py` (from tests/) for the best experience! 