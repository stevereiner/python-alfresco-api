# Alfresco API Test Suite

Comprehensive testing for the enhanced generated Alfresco API client with unit tests (mocking) and integration tests (live server).

## 🏗️ Test Structure

```
tests/
├── __init__.py                          # Test package
├── conftest.py                          # Pytest configuration and fixtures  
├── requirements-test.txt                # Test dependencies
├── run_tests.py                        # Test runner script
├── README.md                           # Test documentation
├── test_unit_master_client.py          # Unit tests for master client (mocked)
├── test_integration_live_server.py     # Integration tests (live server) 
├── test_individual_apis.py             # Individual API tests
├── test_client_dependencies.py         # Client dependency tests
├── test_authentication_strategies.py   # Authentication strategy tests
├── test_simple.py                      # Simple/basic tests
└── test_summary.py                     # Test summary functionality
```

## 🧪 Test Types

### 1. Unit Tests (Mocked)
- **File**: `test_unit_master_client.py`
- **Purpose**: Test client functionality without requiring a live server
- **Coverage**: 
  - Client initialization
  - API status checking
  - Configuration management
  - URL generation
  - Error handling

### 2. Integration Tests (Live Server)
- **File**: `test_integration_live_server.py`
- **Purpose**: Test against real Alfresco server (localhost:8080)
- **Coverage**:
  - Server connection
  - All 7 APIs (auth, core, discovery, search, search-sql, workflow, model)
  - Performance testing
  - End-to-end functionality

### 3. Individual API Tests
- **File**: `test_individual_apis.py`
- **Purpose**: Test each API individually with mocking
- **Coverage**: All 7 Alfresco APIs with specific functionality tests

## 🚀 Running Tests

### Prerequisites

1. **Install test dependencies**:
   ```bash
   pip install -r tests/requirements-test.txt
   ```

2. **For integration tests**: Ensure Alfresco server is running on `localhost:8080` with admin/admin credentials

### Running All Tests (2-Section Approach)

```bash
# Using the test runner (RECOMMENDED - shows 2 sections)
python tests/run_tests.py

# Using pytest directly
pytest tests/ -v

# With coverage
pytest tests/ --cov=enhanced_generated --cov-report=html
```

### ⚠️ **IMPORTANT: Generated Tests Warning**

**🚫 DO NOT USE** the auto-generated test suites in `enhanced_generated/clients/*/test/`:
- ❌ These are **hundreds of generated test files** for standalone clients
- ❌ They use outdated import patterns (`from alfresco_auth import AuthClient`)
- ❌ They're designed for individual clients, not the master client architecture
- ❌ They will fail with `ModuleNotFoundError`

**✅ Use instead:** The curated test suite in `tests/` directory:
- ✅ **`python tests/run_tests.py`** - 2-section test runner (Unit + Integration)
- ✅ Designed for master client architecture  
- ✅ Uses proper imports and patterns
- ✅ Comprehensive coverage with organized sections

### Running Specific Tests

```bash
# Unit tests only
python tests/run_tests.py tests/test_unit_master_client.py

# Integration tests only
python tests/run_tests.py tests/test_integration_live_server.py

# Individual API tests
python tests/run_tests.py tests/test_individual_apis.py

# Using pytest
pytest tests/test_unit_master_client.py -v
pytest tests/test_integration_live_server.py -v
```

### Running with Different Options

```bash
# Verbose output
pytest tests/ -v

# Show print statements
pytest tests/ -s

# Stop on first failure
pytest tests/ -x

# Run in parallel
pytest tests/ -n auto

# Generate HTML report
pytest tests/ --html=test_report.html
```

## 🔧 Test Configuration

### Test Environment Variables

```bash
# Alfresco server configuration
export ALFRESCO_HOST=http://localhost:8080
export ALFRESCO_USERNAME=admin
export ALFRESCO_PASSWORD=admin
export ALFRESCO_VERIFY_SSL=true
```

### Pytest Configuration

The `conftest.py` file provides:
- **Fixtures**: Mock servers, test clients, configuration
- **Test data**: Sample responses, mock objects
- **Configuration**: Test settings and constants

## 📊 Test Coverage

### Unit Tests Coverage
- ✅ Client initialization and configuration
- ✅ API status checking
- ✅ URL generation for all APIs
- ✅ Error handling and edge cases
- ✅ Mock responses and data validation

### Integration Tests Coverage
- ✅ Live server connection
- ✅ Authentication (ticket creation/validation)
- ✅ Discovery API (repository information)
- ✅ Core API (nodes, sites, people)
- ✅ Search APIs (AFTS and SQL)
- ✅ Workflow API (processes, tasks)
- ✅ Model API (aspects, types)
- ✅ Performance testing

### Individual API Coverage
- ✅ Auth API: Ticket management
- ✅ Core API: Nodes, sites, people operations
- ✅ Discovery API: Repository information
- ✅ Search API: AFTS search queries
- ✅ Search SQL API: SQL queries
- ✅ Workflow API: Process and task management
- ✅ Model API: Aspect and type management

## 🎯 Test Scenarios

### Authentication Testing
```python
# Test ticket creation
auth_ticket = client.auth.create_ticket(username='admin', password='admin')
assert auth_ticket.entry.id is not None

# Test ticket validation
ticket_info = client.auth.get_ticket()
assert ticket_info is not None

# Test ticket cleanup
client.auth.delete_ticket()
```

### Core API Testing
```python
# Test node operations
root_nodes = client.core.list_nodes(node_id="-root-")
assert len(root_nodes.list.entries) > 0

# Test site operations
sites = client.core.list_sites()
assert sites is not None

# Test people operations
current_user = client.core.get_person(person_id="-me-")
assert current_user.entry.id == 'admin'
```

### Search Testing
```python
# Test AFTS search
search_query = {
    "query": {"query": "cm:name:*", "language": "afts"},
    "paging": {"maxItems": 10}
}
results = client.search.search(search_body=search_query)
assert results is not None

# Test SQL search
sql_results = client.search_sql.search("SELECT * FROM cmis:document")
assert sql_results is not None
```

## 🔍 Debugging Tests

### Common Issues

1. **Import Errors**: Ensure virtual environment is activated
2. **Connection Errors**: Check if Alfresco server is running
3. **Authentication Errors**: Verify admin/admin credentials
4. **Timeout Errors**: Increase timeout in test configuration

### Debug Mode

```bash
# Run with debug output
pytest tests/ -v -s --tb=long

# Run specific failing test
pytest tests/test_integration_live_server.py::TestLiveAlfrescoServer::test_server_connection -v -s
```

### Test Logs

```bash
# Generate detailed logs
pytest tests/ --log-cli-level=DEBUG

# Save logs to file
pytest tests/ --log-file=test.log --log-file-level=DEBUG
```

## 📈 Performance Testing

### Response Time Tests
- Connection speed: < 10 seconds
- API response times: < 5 seconds
- Search operations: < 5 seconds

### Load Testing
```bash
# Run performance tests
pytest tests/test_integration_live_server.py::TestLiveServerPerformance -v
```

## 🧹 Test Cleanup

### Automatic Cleanup
- Authentication tickets are automatically deleted
- Temporary test data is cleaned up
- Mock objects are properly disposed

### Manual Cleanup
```bash
# Clean up test artifacts
rm -rf .pytest_cache/
rm -rf htmlcov/
rm -f test_report.html
```

## 📝 Adding New Tests

### Unit Test Template
```python
def test_new_feature(self, enhanced_client):
    """Test new feature with mocking."""
    with patch.object(enhanced_client.api, 'method') as mock_method:
        mock_method.return_value = Mock(expected_response)
        
        result = enhanced_client.api.method()
        
        assert result is not None
        # Add more assertions
```

### Integration Test Template
```python
def test_new_feature_live(self, live_client):
    """Test new feature against live server."""
    if not live_client.api:
        pytest.skip("API not available")
    
    result = live_client.api.method()
    
    assert result is not None
    # Add more assertions
```

## 🎉 Success Criteria

Tests are considered successful when:
- ✅ All unit tests pass (mocked)
- ✅ All integration tests pass (live server)
- ✅ Code coverage > 80%
- ✅ Performance benchmarks met
- ✅ No critical security issues
- ✅ All 7 APIs functional

## 📞 Support

For test-related issues:
1. Check the test logs
2. Verify Alfresco server status
3. Review test configuration
4. Check virtual environment setup 