# Python Alfresco API v1.1 - Authentication Guide

This comprehensive guide covers all authentication methods and patterns for the Python Alfresco API v1.1, including the breakthrough query parameter authentication method and hierarchical client integration.

## 📋 Table of Contents

- [Quick Start](#-quick-start)
- [Authentication Methods](#-authentication-methods)
- [Authentication Breakthrough](#-authentication-breakthrough)
- [ClientFactory Pattern](#-clientfactory-pattern)
- [Environment Configuration](#-environment-configuration)
- [OAuth2 Authentication](#-oauth2-authentication)
- [Error Handling](#-error-handling)
- [Best Practices](#-best-practices)

## 🚀 Quick Start

### Simplest Authentication (Direct Clients)

```python
from python_alfresco_api import AlfrescoCoreClient, AlfrescoSearchClient

# Create clients with direct credentials
core_client = AlfrescoCoreClient(
    base_url="http://localhost:8080",
    username="admin",
    password="admin"
)

search_client = AlfrescoSearchClient(
    base_url="http://localhost:8080",
    username="admin", 
    password="admin"
)

# Use immediately - authentication is handled automatically
nodes = core_client.get_nodes()
print(f"✅ Found {len(nodes.list.entries)} nodes")
```

### Factory Pattern (Enterprise Applications)

```python
from python_alfresco_api import ClientFactory

# Centralized authentication management
factory = ClientFactory(
    base_url="http://localhost:8080",
    username="admin",
    password="admin"
)

# All clients share authentication session
clients = factory.create_all_clients()

# Test connection
try:
    repo_info = clients['discovery'].get_repository_info()
    print(f"✅ Connected to Alfresco {repo_info.entry.repository.version.major}.{repo_info.entry.repository.version.minor}")
except Exception as e:
    print(f"❌ Connection failed: {e}")
```

## 🔐 Authentication Methods

### 1. Query Parameter Authentication (Breakthrough Method)

Our research discovered that Alfresco works reliably with query parameter authentication using `alf_ticket`:

```python
# How it works internally (handled automatically by the client)
import requests

# Step 1: Get ticket
response = requests.post(
    "http://localhost:8080/alfresco/api/-default-/public/authentication/versions/1/tickets",
    json={"userId": "admin", "password": "admin"}
)
ticket = response.json()['entry']['id']

# Step 2: Use ticket as query parameter (not header)
api_response = requests.get(
    f"http://localhost:8080/alfresco/api/-default-/public/alfresco/versions/1/nodes/-root-/children?alf_ticket={ticket}"
)
```

**Benefits**:
- ✅ Most reliable authentication method for Alfresco
- ✅ Works consistently across all API endpoints  
- ✅ No header encoding issues
- ✅ Handled automatically by all our clients

### 2. Basic Authentication (Development)

Simple username/password for development and testing:

```python
from python_alfresco_api import ClientFactory

factory = ClientFactory(
    base_url="http://localhost:8080",
    username="admin",
    password="admin"
)

# The client automatically:
# 1. Tries basic auth first
# 2. Falls back to ticket auth if needed
# 3. Uses query parameter method for reliability
```

### 3. OAuth2 Authentication (Enterprise)

For enterprise applications requiring OAuth2:

```python
from python_alfresco_api import OAuth2AuthUtil, ClientFactory

# OAuth2 with client credentials
oauth_util = OAuth2AuthUtil(
    base_url="http://localhost:8080",
    client_id="your-client-id",
    client_secret="your-client-secret",
    grant_type="client_credentials"
)

# Use with factory
factory = ClientFactory(auth_util=oauth_util)
core_client = factory.create_core_client()
```

## 🔍 Authentication Breakthrough

### The Discovery

Through extensive testing, we discovered that while header-based authentication can be unreliable with Alfresco, **query parameter authentication using `alf_ticket` works consistently**:

```bash
# Traditional header method (can be problematic)
curl -H "Authorization: Basic TICKET_BASE64" \
  "http://localhost:8080/alfresco/api/-default-/public/alfresco/versions/1/sites"

# Query parameter method (reliable)  
curl "http://localhost:8080/alfresco/api/-default-/public/alfresco/versions/1/sites?alf_ticket=TICKET_abc123xyz"
```

### Implementation in Our Clients

All our clients automatically implement this breakthrough method:

1. **Get Ticket**: POST to `/tickets` endpoint with credentials
2. **Use Query Parameter**: Append `alf_ticket={ticket}` to all API URLs
3. **Auto-Renewal**: Automatically refresh expired tickets
4. **Fallback**: Graceful fallback to basic auth if ticket fails

This happens transparently - you just provide credentials and the client handles the rest.

## 🏭 ClientFactory Pattern

Best for enterprise applications with multiple API usage:

```python
from python_alfresco_api import ClientFactory

# Centralized configuration
factory = ClientFactory(
    base_url="http://localhost:8080",
    username="admin",
    password="admin",
    verify_ssl=False  # For development
)

# Create specific clients as needed
auth_client = factory.create_auth_client()
core_client = factory.create_core_client() 
search_client = factory.create_search_client()
workflow_client = factory.create_workflow_client()
model_client = factory.create_model_client()
discovery_client = factory.create_discovery_client()
search_sql_client = factory.create_search_sql_client()

# Or create all at once
all_clients = factory.create_all_clients()
```

**Benefits**:
- Shared authentication session across all clients
- Centralized configuration management
- Automatic token refresh
- Enterprise-grade error handling

> **⚠️ Important**: Always use the ClientFactory pattern. Direct client creation bypasses shared authentication and environment configuration. Alfresco requires ticket-based authentication after the first API call, which only works properly with the factory's shared authentication session.

## 🌍 Environment Configuration

### Using .env Files (Recommended)

Create a `.env` file in your project root:

```bash
# Copy the sample
cp sample-dot-env.txt .env
```

Edit `.env`:
```bash
# Alfresco Server Configuration
ALFRESCO_URL=http://localhost:8080
ALFRESCO_USERNAME=admin
ALFRESCO_PASSWORD=admin
ALFRESCO_VERIFY_SSL=false

# Alternative variable names also supported
ALFRESCO_BASE_URL=http://localhost:8080
ALFRESCO_USER=admin
ALFRESCO_PASS=admin
```

Use with automatic loading:
```python
from python_alfresco_api import ClientFactory

# Automatically loads from .env file
factory = ClientFactory()  # No parameters needed!

# Or override specific values
factory = ClientFactory(
    password="different-password"  # Override just password
)
```

### Environment Variables

Set environment variables directly:

**Windows:**
```powershell
$env:ALFRESCO_URL="http://localhost:8080"
$env:ALFRESCO_USERNAME="admin"
$env:ALFRESCO_PASSWORD="admin"
```

**Linux/Mac:**
```bash
export ALFRESCO_URL="http://localhost:8080"
export ALFRESCO_USERNAME="admin" 
export ALFRESCO_PASSWORD="admin"
```

**Python code:**
```python
import os
from python_alfresco_api import ClientFactory

# Set programmatically
os.environ['ALFRESCO_URL'] = 'http://localhost:8080'
os.environ['ALFRESCO_USERNAME'] = 'admin'
os.environ['ALFRESCO_PASSWORD'] = 'admin'

# Use with automatic detection
factory = ClientFactory()
```

### Configuration Priority

The configuration system uses this priority order:
1. **Direct parameters** (highest priority)
2. **Environment variables**
3. **Config files (.env)**
4. **Default values** (lowest priority)

```python
from python_alfresco_api import ClientFactory

# This username="admin" overrides environment variables and .env file
factory = ClientFactory(
    username="admin",  # Direct parameter - highest priority
    # base_url will come from environment or .env file
    # password will come from environment or .env file
)
```

## 🔒 OAuth2 Authentication

For enterprise applications requiring OAuth2:

### Client Credentials Flow

```python
from python_alfresco_api import OAuth2AuthUtil, ClientFactory

# OAuth2 configuration
oauth_util = OAuth2AuthUtil(
    base_url="http://localhost:8080",
    client_id="your-client-id",
    client_secret="your-client-secret",
    grant_type="client_credentials"
)

# Use with factory
factory = ClientFactory(auth_util=oauth_util)
clients = factory.create_all_clients()
```

### Authorization Code Flow

```python
from python_alfresco_api import OAuth2AuthUtil

# OAuth2 with authorization code
oauth_util = OAuth2AuthUtil(
    base_url="http://localhost:8080",
    client_id="your-client-id",
    client_secret="your-client-secret",
    grant_type="authorization_code",
    authorization_code="received-auth-code",
    redirect_uri="http://localhost:3000/callback"
)

# Use with clients
factory = ClientFactory(auth_util=oauth_util)
```

### Environment-based OAuth2

```bash
# .env file
ALFRESCO_OAUTH_CLIENT_ID=your-client-id
ALFRESCO_OAUTH_CLIENT_SECRET=your-client-secret
ALFRESCO_OAUTH_GRANT_TYPE=client_credentials
```

```python
# Python code
oauth_util = OAuth2AuthUtil()  # Loads from environment
factory = ClientFactory(auth_util=oauth_util)
```

## ⚠️ Error Handling

### Connection Testing

```python
from python_alfresco_api import ClientFactory

def test_alfresco_connection():
    """Test Alfresco server connectivity and authentication."""
    try:
        factory = ClientFactory(
            base_url="http://localhost:8080",
            username="admin", 
            password="admin"
        )
        
        # Test with Discovery API (no auth required)
        discovery_client = factory.create_discovery_client()
        repo_info = discovery_client.get_repository_info()
        print(f"✅ Server accessible: Alfresco {repo_info.entry.repository.version.display}")
        
        # Test authenticated endpoints
        core_client = factory.create_core_client()
        nodes = core_client.get_nodes()
        print(f"✅ Authentication successful: Found {len(nodes.list.entries)} root nodes")
        
        return True
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

# Run test
test_alfresco_connection()
```

### Common Error Scenarios

| Error | Cause | Solution |
|-------|--------|----------|
| `ConnectionError` | Server not accessible | Check server URL and status |
| `401 Unauthorized` | Invalid credentials | Verify username/password |
| `403 Forbidden` | User lacks permissions | Check user permissions in Alfresco |
| `404 Not Found` | Wrong API endpoint | Verify Alfresco version and API paths |
| `SSLError` | Certificate issues | Set `verify_ssl=False` for development |

### Debugging Authentication Issues

```python
from python_alfresco_api import ClientFactory
import logging

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

try:
    factory = ClientFactory(
        base_url="http://localhost:8080",
        username="admin",
        password="admin",
        verify_ssl=False
    )
    
    # Test each step
    print("1. Testing server connectivity...")
    discovery_client = factory.create_discovery_client() 
    repo_info = discovery_client.get_repository_info()
    print(f"✅ Server: {repo_info.entry.repository.version.display}")
    
    print("2. Testing authentication...")
    auth_client = factory.create_auth_client()
    ticket = auth_client.create_ticket({"userId": "admin", "password": "admin"})
    print(f"✅ Ticket: {ticket.entry.id[:20]}...")
    
    print("3. Testing authenticated API...")
    core_client = factory.create_core_client()
    nodes = core_client.get_nodes()
    print(f"✅ Nodes: {len(nodes.list.entries)} found")
    
except Exception as e:
    print(f"❌ Debug failed at: {e}")
    import traceback
    traceback.print_exc()
```

## 📋 Best Practices

### 1. Use Environment Configuration

```python
# ✅ Good: Environment-based configuration
factory = ClientFactory()  # Loads from .env

# ❌ Avoid: Hardcoded credentials
factory = ClientFactory(username="admin", password="admin")
```

### 2. Choose the Right Pattern

```python
# ✅ Factory pattern for enterprise apps
factory = ClientFactory()
clients = factory.create_all_clients()

# ✅ Direct clients for focused apps  
core_client = AlfrescoCoreClient(base_url="http://localhost:8080", username="admin", password="admin")
```

### 3. Handle SSL Properly

```python
# ✅ Development
factory = ClientFactory(verify_ssl=False)

# ✅ Production with custom cert
factory = ClientFactory(verify_ssl="/path/to/cert.pem")

# ✅ Production with trusted certs
factory = ClientFactory(verify_ssl=True)
```

### 4. Test Connections

```python
# ✅ Always test connectivity first
def verify_alfresco():
    try:
        factory = ClientFactory()
        discovery = factory.create_discovery_client()
        repo_info = discovery.get_repository_info()
        return True
    except:
        return False

if verify_alfresco():
    # Proceed with application
    pass
```

### 5. Use Proper Error Handling

```python
# ✅ Comprehensive error handling
try:
    factory = ClientFactory()
    core_client = factory.create_core_client()
    nodes = core_client.get_nodes()
except ConnectionError:
    print("Server not accessible")
except AuthenticationError:
    print("Invalid credentials")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## 🚀 Advanced Usage

### Async Authentication

```python
import asyncio
from python_alfresco_api import ClientFactory

async def async_alfresco_operations():
    factory = ClientFactory(
        base_url="http://localhost:8080",
        username="admin",
        password="admin"
    )
    
    core_client = factory.create_core_client()
    
    # Use async operations
    nodes = await core_client.get_nodes_asyncio()
    
    # Process results
    for node in nodes.list.entries:
        print(f"Node: {node.entry.name}")

# Run async operations
asyncio.run(async_alfresco_operations())
```

### Custom Authentication Utilities

```python
from python_alfresco_api import AuthUtil, ClientFactory

# Custom auth utility with additional configuration
auth_util = AuthUtil(
    base_url="http://localhost:8080",
    username="admin",
    password="admin",
    verify_ssl=False,
    timeout=30
)

# Use with factory
factory = ClientFactory(auth_util=auth_util)
```

## 📚 Additional Resources

- [Alfresco REST API Documentation](https://docs.alfresco.com/content-services/latest/develop/rest-api-guide/)
- [Alfresco Authentication Guide](https://docs.alfresco.com/content-services/latest/admin/security/)
- [Python Alfresco API Examples](../examples/)
- [Environment Configuration Guide](ENVIRONMENT_CONFIGURATION.md)

## 🆘 Support

If you experience authentication issues:

1. **Test with Discovery API first** - it doesn't require authentication
2. **Check server logs** - Alfresco logs contain detailed authentication errors
3. **Verify credentials in Alfresco Share** - ensure they work in the UI
4. **Use debug logging** - enable Python logging to see detailed requests
5. **Test with curl** - isolate issues by testing authentication manually

The authentication system in this library is designed to be robust and handle most edge cases automatically, including the breakthrough query parameter method that ensures reliable authentication across all Alfresco deployments. 