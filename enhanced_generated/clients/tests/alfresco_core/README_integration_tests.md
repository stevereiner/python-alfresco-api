# Integration Tests for Alfresco Core API

## 🌐 Real API Integration Tests

The `test_coreclient_integration.py` file contains **real integration tests** that make actual HTTP calls to a running Alfresco instance, unlike the mocked unit tests in `test_coreclient.py`.

## ⚠️ Important Notes

- **These tests create, modify, and delete REAL data in Alfresco!**
- **Only run against test/development Alfresco instances**
- **Never run against production without understanding the impact**

## 🔧 Prerequisites

1. **Running Alfresco Instance**
   - Alfresco Community or Enterprise
   - Accessible via HTTP/HTTPS
   - Default: `http://localhost:8080`

2. **Valid Credentials**
   - Admin user credentials
   - Default: `admin/admin`

3. **Network Connectivity**
   - Tests must be able to reach Alfresco server
   - Firewall/proxy configuration if needed

## 🚀 How to Run

### Method 1: Default Configuration
```bash
# Uses default localhost:8080 with admin/admin
python -m unittest alfresco_client.tests.alfresco_core.test_coreclient_integration -v
```

### Method 2: Environment Variables
```bash
# Set your Alfresco configuration
export ALFRESCO_BASE_URL="http://your-alfresco.com:8080"
export ALFRESCO_USERNAME="your-username"
export ALFRESCO_PASSWORD="your-password"
export ALFRESCO_VERIFY_SSL="false"

# Run tests
python -m unittest alfresco_client.tests.alfresco_core.test_coreclient_integration -v
```

### Method 3: VS Code Debugging
Add this configuration to your `.vscode/launch.json`:
```json
{
    "name": "Debug Integration Tests",
    "type": "debugpy",
    "request": "launch",
    "module": "unittest",
    "args": [
        "alfresco_client.tests.alfresco_core.test_coreclient_integration",
        "-v"
    ],
    "console": "integratedTerminal",
    "cwd": "${workspaceFolder}",
    "python": "${config:python.defaultInterpreterPath}",
    "env": {
        "PYTHONPATH": "${workspaceFolder}",
        "ALFRESCO_BASE_URL": "http://localhost:8080",
        "ALFRESCO_USERNAME": "admin",
        "ALFRESCO_PASSWORD": "admin"
    }
}
```

## 🧪 What the Tests Do

The integration tests perform the following **real operations**:

### 📁 Node Operations
- ✅ Get root node (Company Home)
- ✅ List children of root node
- ✅ Create test folder with properties
- ✅ Update folder properties
- ✅ Create test file with content
- ✅ Download file content
- ✅ Copy nodes

### 💬 Content & Comments
- ✅ Create comments on nodes
- ✅ List comments
- ✅ Upload/download file content

### 🏷️ Tags & Metadata
- ✅ Create and list tags
- ✅ Update node properties
- ✅ Handle metadata

### 🔍 Other Operations
- ✅ Basic search functionality
- ✅ API information retrieval
- ✅ Connection verification

## 🧹 Automatic Cleanup

The tests **automatically clean up** all created data:
- Test folders and files are deleted
- Created in `tearDownClass()` method
- Runs even if tests fail (when possible)
- Uses permanent deletion to avoid trash

## 📊 Sample Output

```bash
✅ Connected to Alfresco: Company Home

🧪 Testing: Get root node
  ✅ Root node: Company Home (ID: 9b7b8e4a-...)

🧪 Testing: List root children  
  ✅ Found 4 children: ['Data Dictionary', 'Guest Home', 'Sites', 'Shared']

🧪 Testing: Create folder 'test-folder-1735744123'
  ✅ Created folder: test-folder-1735744123 (ID: 8a2f9c1d-...)

🧪 Testing: Create file 'test-file-1735744123.txt'
  ✅ Created file: test-file-1735744123.txt (ID: 4d6e8f2a-...)
  ✅ Uploaded content: 67 bytes

🧹 Cleaning up 3 test nodes...
  ✅ Deleted node: 4d6e8f2a-...
  ✅ Deleted node: 8a2f9c1d-...
```

## 🔐 Security Configuration

### SSL/TLS
```bash
# For production with valid certificates
export ALFRESCO_VERIFY_SSL="true"

# For development with self-signed certificates  
export ALFRESCO_VERIFY_SSL="false"
```

### Custom Authentication
To use different authentication methods, modify the `setUpClass()` method in the test file.

## 🐛 Troubleshooting

### Connection Issues
```bash
❌ Cannot connect to Alfresco at http://localhost:8080: HTTPConnectionPool(host='localhost', port=8080): Max retries exceeded
```
**Solution**: Ensure Alfresco is running and accessible

### Authentication Issues
```bash
❌ 401 Unauthorized
```
**Solution**: Check username/password or authentication method

### Permission Issues
```bash
❌ 403 Forbidden
```
**Solution**: Ensure user has sufficient permissions to create/delete content

### SSL Issues
```bash
❌ SSL: CERTIFICATE_VERIFY_FAILED
```
**Solution**: Set `ALFRESCO_VERIFY_SSL=false` for development

## 📋 Comparison: Integration vs Unit Tests

| Feature | Unit Tests (`test_coreclient.py`) | Integration Tests (`test_coreclient_integration.py`) |
|---------|-----------------------------------|---------------------------------------------------|
| **Speed** | ⚡ Very fast (milliseconds) | 🐌 Slower (seconds) |
| **Dependencies** | ✅ None (mocked) | ❗ Requires running Alfresco |
| **Data Safety** | ✅ No real data touched | ⚠️ Creates/deletes real data |
| **Network** | ✅ No network calls | 🌐 Real HTTP requests |
| **Purpose** | Test client code logic | Test actual API integration |
| **CI/CD** | ✅ Perfect for pipelines | ❗ Needs test environment |
| **Debugging** | 🐛 Debug client wrapper | 🔍 Debug API communication |

## 🎯 When to Use Each

### Use **Unit Tests** (`test_coreclient.py`) for:
- 🔧 Development and debugging
- 🏗️ CI/CD pipelines  
- ⚡ Fast feedback during coding
- 📦 Testing client wrapper logic

### Use **Integration Tests** (`test_coreclient_integration.py`) for:
- 🔗 End-to-end testing
- 🌐 API compatibility verification
- 🚀 Pre-deployment testing
- 🐛 Debugging real API issues 