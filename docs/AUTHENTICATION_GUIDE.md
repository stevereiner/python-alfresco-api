# Alfresco API Authentication Guide

## Understanding 401 Unauthorized Errors

If you're getting a 401 Unauthorized error when trying to interact with Alfresco APIs, this guide will help you understand and resolve the issue.

## Common Causes of 401 Errors

### 1. Authentication Methods
Alfresco REST API supports multiple authentication methods:

- **Basic Authentication**: Username and password encoded in Base64 in the Authorization header
- **Ticket Authentication**: After successful authentication, Alfresco returns a ticket for subsequent API calls
- **Invalid/Expired Tickets**: If the ticket is invalid or expired, you'll get a 401 error

### 2. Authentication Header Issues
Make sure you're properly including the Authorization header in your request with:
- Correct authentication method (Basic, Bearer, etc.)
- Valid credentials/token
- Proper Base64 encoding

## Step-by-Step Authentication Process

### Step 1: Test Server Connectivity
First, test if the server is accessible using the Discovery API (which typically doesn't require authentication):

```bash
curl -X GET "http://localhost:8080/alfresco/api/discovery"
```

Expected response: Repository information without authentication.

### Step 2: Authenticate and Get a Ticket
Use the Authentication API to get a ticket:

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"userId":"admin","password":"admin"}' \
  "http://localhost:8080/alfresco/api/-default-/public/authentication/versions/1/tickets"
```

Expected response:
```json
{
  "entry": {
    "id": "TICKET_xxxxxxxxxxxxxxx",
    "userId": "admin"
  }
}
```

### Step 3: Use the Ticket for Authenticated Requests
Base64 encode the ticket and use it in the Authorization header:

**Linux/Mac:**
```bash
echo -n 'TICKET_xxxxxxxxxxxxxxx' | base64
```

**Windows PowerShell:**
```powershell
[Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("TICKET_xxxxxxxxxxxxxxx"))
```

Then use the encoded ticket:
```bash
curl -X GET \
  -H "Accept: application/json" \
  -H "Authorization: Basic <base64-encoded-ticket>" \
  "http://localhost:8080/alfresco/api/-default-/public/alfresco/versions/1/sites"
```

## API Endpoint Authentication Requirements

| API Type | Endpoint | Authentication Required |
|----------|----------|------------------------|
| Discovery | `/alfresco/api/discovery` | ❌ No |
| Authentication | `/alfresco/api/-default-/public/authentication/versions/1/tickets` | ❌ No (for getting tickets) |
| Core APIs | `/alfresco/api/-default-/public/alfresco/versions/1/*` | ✅ Yes |
| Search API | `/alfresco/api/-default-/public/search/versions/1/*` | ✅ Yes |
| Sites API | `/alfresco/api/-default-/public/alfresco/versions/1/sites` | ✅ Yes |
| People API | `/alfresco/api/-default-/public/alfresco/versions/1/people` | ✅ Yes |

## Python Code Examples

### Basic Authentication Header
```python
import base64

def create_basic_auth_header(username, password):
    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()
    return f"Basic {encoded_credentials}"

# Usage
auth_header = create_basic_auth_header("admin", "admin")
headers = {"Authorization": auth_header}
```

### Ticket Authentication
```python
import requests
import base64

def get_alfresco_ticket(server_url, username, password):
    """Get an authentication ticket from Alfresco."""
    auth_url = f"{server_url}/alfresco/api/-default-/public/authentication/versions/1/tickets"
    auth_data = {
        "userId": username,
        "password": password
    }
    
    response = requests.post(auth_url, json=auth_data)
    if response.status_code == 201:
        return response.json()['entry']['id']
    else:
        raise Exception(f"Authentication failed: {response.status_code}")

def create_ticket_auth_header(ticket):
    """Create Authorization header using ticket."""
    encoded_ticket = base64.b64encode(ticket.encode()).decode()
    return f"Basic {encoded_ticket}"

# Usage
ticket = get_alfresco_ticket("http://localhost:8080", "admin", "admin")
auth_header = create_ticket_auth_header(ticket)
headers = {"Authorization": auth_header}
```

### Complete Example
```python
import requests
import base64

class AlfrescoAuthenticator:
    def __init__(self, server_url, username, password):
        self.server_url = server_url
        self.username = username
        self.password = password
        self.ticket = None
        
    def test_connectivity(self):
        """Test server connectivity using Discovery API."""
        try:
            response = requests.get(f"{self.server_url}/alfresco/api/discovery")
            return response.status_code == 200
        except requests.RequestException:
            return False
    
    def authenticate(self):
        """Authenticate and get a ticket."""
        auth_url = f"{self.server_url}/alfresco/api/-default-/public/authentication/versions/1/tickets"
        auth_data = {
            "userId": self.username,
            "password": self.password
        }
        
        response = requests.post(auth_url, json=auth_data)
        if response.status_code == 201:
            self.ticket = response.json()['entry']['id']
            return True
        return False
    
    def get_auth_headers(self):
        """Get headers with authentication."""
        if not self.ticket:
            if not self.authenticate():
                raise Exception("Authentication failed")
        
        encoded_ticket = base64.b64encode(self.ticket.encode()).decode()
        return {
            "Authorization": f"Basic {encoded_ticket}",
            "Accept": "application/json"
        }
    
    def make_authenticated_request(self, endpoint, method="GET", **kwargs):
        """Make an authenticated request to Alfresco API."""
        headers = self.get_auth_headers()
        if 'headers' in kwargs:
            headers.update(kwargs['headers'])
        kwargs['headers'] = headers
        
        url = f"{self.server_url}{endpoint}"
        response = requests.request(method, url, **kwargs)
        
        # If 401, try re-authenticating once
        if response.status_code == 401:
            self.ticket = None  # Clear expired ticket
            headers = self.get_auth_headers()
            kwargs['headers'] = headers
            response = requests.request(method, url, **kwargs)
        
        return response

# Usage
auth = AlfrescoAuthenticator("http://localhost:8080", "admin", "admin")

# Test connectivity
if auth.test_connectivity():
    print("✅ Server is accessible")
else:
    print("❌ Server is not accessible")

# Make authenticated request
response = auth.make_authenticated_request("/alfresco/api/-default-/public/alfresco/versions/1/sites")
if response.status_code == 200:
    print("✅ Authenticated request successful")
    sites = response.json()
else:
    print(f"❌ Request failed: {response.status_code}")
```

## Debugging 401 Errors

### Checklist for Troubleshooting

1. **✓ Verify server is running and accessible**
   - Test with Discovery API: `GET /alfresco/api/discovery`

2. **✓ Check username and password are correct**
   - Verify credentials work in Alfresco Share UI

3. **✓ Ensure proper Content-Type header for auth requests**
   - Use `Content-Type: application/json` for ticket requests

4. **✓ Verify Authorization header format**
   - Should be `Authorization: Basic <base64-encoded-credentials-or-ticket>`

5. **✓ Check if ticket has expired**
   - Tickets have a limited lifetime, re-authenticate if needed

6. **✓ Test with Discovery API first**
   - This endpoint typically doesn't require authentication

7. **✓ Check server logs for authentication errors**
   - Look at Alfresco server logs for detailed error messages

8. **✓ Verify Alfresco authentication subsystem configuration**
   - Ensure authentication is properly configured on the server

9. **✓ Test with curl command line tool first**
   - Isolate issues by testing with curl before using code

10. **✓ Check for any firewall or proxy issues**
    - Ensure network connectivity between client and server

### Common Error Scenarios

| Error | Cause | Solution |
|-------|--------|----------|
| 401 with "Invalid credentials" | Wrong username/password | Verify credentials are correct |
| 401 with valid credentials | Ticket expired | Re-authenticate to get new ticket |
| 401 on all requests | Missing Authorization header | Add proper Authorization header |
| 401 on specific endpoints | Wrong auth method | Use ticket auth for protected endpoints |
| 401 with network timeouts | Server/network issues | Check server status and network connectivity |

### Testing with curl

Test authentication with curl:

```bash
# Test Discovery API (should work without auth)
curl -v "http://localhost:8080/alfresco/api/discovery"

# Get authentication ticket
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"userId":"admin","password":"admin"}' \
  "http://localhost:8080/alfresco/api/-default-/public/authentication/versions/1/tickets"

# Use ticket for authenticated request (replace TICKET_xxx with actual ticket)
TICKET="TICKET_xxxxxxxxxxxxxxx"
ENCODED_TICKET=$(echo -n "$TICKET" | base64)
curl -X GET \
  -H "Authorization: Basic $ENCODED_TICKET" \
  "http://localhost:8080/alfresco/api/-default-/public/alfresco/versions/1/sites"
```

## Integration with Python Alfresco API Client

When using this Python Alfresco API client, authentication is handled automatically:

```python
from python_alfresco_api import ClientFactory

# Create client with credentials
client = AlfrescoClient(
    server_url="http://localhost:8080",
    username="admin",
    password="admin"
)

# The client handles authentication automatically
try:
    sites = client.core.get_sites()
    print("✅ Authentication successful")
except Exception as e:
    print(f"❌ Authentication failed: {e}")
```

The client will:
1. Test connectivity with Discovery API
2. Authenticate and get a ticket
3. Use the ticket for subsequent requests
4. Automatically re-authenticate if the ticket expires

## Additional Resources

- [Alfresco REST API Documentation](https://docs.alfresco.com/content-services/latest/develop/rest-api-guide/)
- [Alfresco Authentication Guide](https://docs.alfresco.com/content-services/latest/admin/security/)
- [Alfresco API Explorer](https://api-explorer.alfresco.com/api-explorer/)

## Support

If you continue to experience 401 authentication errors after following this guide:

1. Check the Alfresco server logs for detailed error messages
2. Verify your Alfresco server authentication configuration
3. Test with the Alfresco API Explorer first
4. Consider network connectivity and firewall issues
5. Consult the Alfresco community forums for server-specific issues 

# Authentication Guide - Python Alfresco API v1.0

This comprehensive guide covers all authentication methods and patterns for the Python Alfresco API v1.0.

## 📋 Table of Contents

- [Quick Start](#quick-start)
- [Authentication Methods](#authentication-methods)
- [ClientFactory Pattern](#clientfactory-pattern)
- [Manual Authentication](#manual-authentication)
- [Error Handling](#error-handling)
- [Best Practices](#best-practices)

## 🚀 Quick Start

### Modern ClientFactory Pattern (Recommended)

```python
from python_alfresco_api import ClientFactory

# Automatic authentication across all clients  
factory = ClientFactory(
    base_url="http://localhost:8080",
    username="admin",
    password="admin"
)

# All clients are pre-authenticated
clients = factory.create_all_clients()

# Test connection
try:
    repo_info = clients['discovery'].get_repository_info()
    print(f"✅ Connected to Alfresco {repo_info.entry.repository.version.major}.{repo_info.entry.repository.version.minor}")
except Exception as e:
    print(f"❌ Connection failed: {e}")
```

### Individual Client Authentication

```python
from python_alfresco_api.clients.auth_client import AlfrescoAuthClient
from python_alfresco_api.auth_util import AuthUtil

# Manual authentication control
auth = AuthUtil(
    base_url="http://localhost:8080", 
    username="admin",
    password="admin"
)

# Use with individual clients
auth_client = AlfrescoAuthClient(base_url="http://localhost:8080")
ticket = auth_client.create_ticket({"userId": "admin", "password": "admin"})
```

## 🔐 Authentication Methods

### 1. Basic Authentication
Simple username/password authentication for development and testing.

```python
from python_alfresco_api import ClientFactory

factory = ClientFactory(
    base_url="http://localhost:8080",
    username="admin",
    password="admin"
)

clients = factory.create_all_clients()
```

### 2. Ticket-Based Authentication
More secure session-based authentication for production applications.

```python
from python_alfresco_api.clients.auth_client import AlfrescoAuthClient
from python_alfresco_api.models.alfresco_auth_models import TicketBody

auth_client = AlfrescoAuthClient(base_url="http://localhost:8080")

# Create authentication ticket
ticket_request = TicketBody(
    userId="admin",
    password="admin"
)

ticket_response = auth_client.create_ticket(ticket_request)
ticket_id = ticket_response.entry.id

# Use ticket for subsequent requests
# (Implementation depends on specific client setup)
```

### 3. Environment-Based Authentication
Secure authentication using environment variables.

```python
import os
from python_alfresco_api import ClientFactory

factory = ClientFactory(
    base_url=os.getenv("ALFRESCO_BASE_URL", "http://localhost:8080"),
    username=os.getenv("ALFRESCO_USERNAME"),
    password=os.getenv("ALFRESCO_PASSWORD"),
    verify_ssl=os.getenv("ALFRESCO_VERIFY_SSL", "true").lower() == "true"
)

clients = factory.create_all_clients()
```

## 🏭 ClientFactory Pattern

### Complete Authentication Setup

```python
from python_alfresco_api import ClientFactory
from python_alfresco_api.exceptions import AlfrescoAPIException

def create_authenticated_clients():
    """Create fully authenticated client suite"""
    
    try:
        factory = ClientFactory(
            base_url="http://localhost:8080",
            username="admin", 
            password="admin",
            verify_ssl=False  # For development only
        )
        
        # Get all clients with shared authentication
        clients = factory.create_all_clients()
        
        # Verify authentication works
        repo_info = clients['discovery'].get_repository_info()
        print(f"✅ Authentication successful")
        print(f"   Server: {repo_info.entry.repository.name}")
        print(f"   Version: {repo_info.entry.repository.version.major}.{repo_info.entry.repository.version.minor}")
        
        return clients
        
    except AlfrescoAPIException as e:
        print(f"❌ Alfresco API Error: {e}")
        return None
    except Exception as e:
        print(f"❌ Connection Error: {e}")
        return None

# Usage
clients = create_authenticated_clients()
if clients:
    # All clients are ready to use
    nodes = clients['core'].get_nodes()
    search_results = clients['search'].search({"query": {"query": "*", "language": "afts"}})
```

### Per-Client Authentication

```python
from python_alfresco_api import ClientFactory

factory = ClientFactory(
    base_url="http://localhost:8080",
    username="admin",
    password="admin"
)

# Get individual clients as needed
auth_client = factory.create_auth_client()
core_client = factory.create_core_client()
search_client = factory.create_search_client()

# Each client is independently authenticated
```

## 🔧 Manual Authentication

### AuthUtil Pattern

```python
from python_alfresco_api.auth_util import AuthUtil
from python_alfresco_api.clients.core_client import AlfrescoCoreClient

# Create authentication utility
auth = AuthUtil(
    base_url="http://localhost:8080",
    username="admin",
    password="admin"
)

# Use with individual clients
core_client = AlfrescoCoreClient(
    base_url="http://localhost:8080",
    auth_util=auth
)

# Client is now authenticated
nodes = core_client.get_nodes()
```

### Custom Authentication Logic

```python
from python_alfresco_api.clients.auth_client import AlfrescoAuthClient
from python_alfresco_api.models.alfresco_auth_models import TicketBody

class CustomAuthManager:
    """Custom authentication management"""
    
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.auth_client = AlfrescoAuthClient(base_url=base_url)
        self.current_ticket = None
    
    def authenticate(self, username: str, password: str) -> bool:
        """Authenticate and store ticket"""
        try:
            ticket_request = TicketBody(userId=username, password=password)
            response = self.auth_client.create_ticket(ticket_request)
            self.current_ticket = response.entry.id
            return True
        except Exception as e:
            print(f"Authentication failed: {e}")
            return False
    
    def is_authenticated(self) -> bool:
        """Check if currently authenticated"""
        if not self.current_ticket:
            return False
        
        try:
            # Validate current ticket
            self.auth_client.validate_ticket(self.current_ticket)
            return True
        except:
            self.current_ticket = None
            return False
    
    def logout(self):
        """Logout and clear ticket"""
        if self.current_ticket:
            try:
                self.auth_client.delete_ticket(self.current_ticket)
            except:
                pass  # Ignore errors during logout
            finally:
                self.current_ticket = None

# Usage
auth_manager = CustomAuthManager("http://localhost:8080")
if auth_manager.authenticate("admin", "admin"):
    print("✅ Authentication successful")
else:
    print("❌ Authentication failed")
```

## 🚨 Error Handling

### Authentication Error Patterns

```python
from python_alfresco_api import ClientFactory
from python_alfresco_api.exceptions import AlfrescoAPIException

def safe_authentication(base_url: str, username: str, password: str):
    """Safely authenticate with comprehensive error handling"""
    
    try:
        factory = ClientFactory(
            base_url=base_url,
            username=username,
            password=password
        )
        
        clients = factory.create_all_clients()
        
        # Test authentication
        repo_info = clients['discovery'].get_repository_info()
        
        return {
            "success": True,
            "clients": clients,
            "server_info": {
                "name": repo_info.entry.repository.name,
                "version": f"{repo_info.entry.repository.version.major}.{repo_info.entry.repository.version.minor}"
            }
        }
        
    except AlfrescoAPIException as e:
        return {
            "success": False,
            "error_type": "alfresco_api",
            "error": str(e),
            "suggestion": "Check username/password and user permissions"
        }
    
    except ConnectionError as e:
        return {
            "success": False,
            "error_type": "connection",
            "error": str(e),
            "suggestion": "Check base_url and network connectivity"
        }
    
    except Exception as e:
        return {
            "success": False,
            "error_type": "unknown",
            "error": str(e),
            "suggestion": "Check logs for detailed error information"
        }

# Usage
result = safe_authentication(
    base_url="http://localhost:8080",
    username="admin",
    password="admin"
)

if result["success"]:
    print(f"✅ Connected to {result['server_info']['name']}")
    clients = result["clients"]
else:
    print(f"❌ {result['error_type'].title()} Error: {result['error']}")
    print(f"💡 Suggestion: {result['suggestion']}")
```

### Retry Logic

```python
import time
from python_alfresco_api import ClientFactory

def authenticate_with_retry(base_url: str, username: str, password: str, max_retries: int = 3):
    """Authenticate with retry logic"""
    
    for attempt in range(max_retries):
        try:
            factory = ClientFactory(
                base_url=base_url,
                username=username,
                password=password
            )
            
            clients = factory.create_all_clients()
            
            # Test connection
            clients['discovery'].get_repository_info()
            
            print(f"✅ Authentication successful on attempt {attempt + 1}")
            return clients
            
        except Exception as e:
            print(f"❌ Attempt {attempt + 1} failed: {e}")
            
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff
                print(f"⏳ Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print("❌ All authentication attempts failed")
                return None

# Usage
clients = authenticate_with_retry(
    base_url="http://localhost:8080",
    username="admin",
    password="admin"
)
```

## 📝 Best Practices

### 1. Use Environment Variables

```python
import os
from python_alfresco_api import ClientFactory

# Never hardcode credentials
factory = ClientFactory(
    base_url=os.getenv("ALFRESCO_BASE_URL"),
    username=os.getenv("ALFRESCO_USERNAME"),
    password=os.getenv("ALFRESCO_PASSWORD")
)
```

### 2. Validate Authentication Early

```python
def validate_authentication(clients):
    """Validate authentication before proceeding"""
    try:
        # Simple test to verify authentication
        repo_info = clients['discovery'].get_repository_info()
        return True
    except:
        return False

clients = factory.create_all_clients()
if not validate_authentication(clients):
    raise Exception("Authentication validation failed")
```

### 3. Handle SSL Appropriately

```python
# Development (disable SSL verification)
factory = ClientFactory(
    base_url="http://localhost:8080",
    username="admin",
    password="admin",
    verify_ssl=False
)

# Production (enable SSL verification)
factory = ClientFactory(
    base_url="https://alfresco.company.com/alfresco/api",
    username=os.getenv("ALFRESCO_USERNAME"),
    password=os.getenv("ALFRESCO_PASSWORD"),
    verify_ssl=True
)
```

### 4. Use Configuration Classes

```python
from dataclasses import dataclass
from typing import Optional
import os

@dataclass
class AlfrescoConfig:
    base_url: str
    username: str
    password: str
    verify_ssl: bool = True
    timeout: int = 30
    
    @classmethod
    def from_environment(cls) -> 'AlfrescoConfig':
        """Create config from environment variables"""
        return cls(
            base_url=os.getenv("ALFRESCO_BASE_URL", "http://localhost:8080"),
            username=os.getenv("ALFRESCO_USERNAME", "admin"),
            password=os.getenv("ALFRESCO_PASSWORD", "admin"),
            verify_ssl=os.getenv("ALFRESCO_VERIFY_SSL", "true").lower() == "true"
        )

def create_clients(config: AlfrescoConfig):
    """Create clients from configuration"""
    factory = ClientFactory(
        base_url=config.base_url,
        username=config.username,
        password=config.password,
        verify_ssl=config.verify_ssl
    )
    return factory.create_all_clients()

# Usage
config = AlfrescoConfig.from_environment()
clients = create_clients(config)
```

## 🔍 Troubleshooting

### Common Authentication Issues

#### 1. Connection Refused
```
Error: Connection refused
```
**Solution**: Check if Alfresco is running and accessible
- Verify base_url is correct
- Check network connectivity
- Confirm Alfresco service is started

#### 2. 401 Unauthorized
```
Error: 401 Client Error: Unauthorized
```
**Solution**: Check credentials and permissions
- Verify username/password are correct
- Confirm user account is active
- Check user has necessary permissions

#### 3. SSL Certificate Issues
```
Error: SSL verification failed
```
**Solution**: Handle SSL appropriately
- For development: Set `verify_ssl=False`
- For production: Ensure valid SSL certificates
- Consider custom certificate handling if needed

#### 4. Timeout Issues
```
Error: Request timeout
```
**Solution**: Adjust timeout settings
- Increase timeout values
- Check network latency
- Verify server performance

### Debug Authentication

```python
import logging
from python_alfresco_api import ClientFactory

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

try:
    factory = ClientFactory(
        base_url="http://localhost:8080",
        username="admin",
        password="admin"
    )
    
    clients = factory.create_all_clients()
    repo_info = clients['discovery'].get_repository_info()
    
    print("🎉 Authentication successful!")
    print(f"Server: {repo_info.entry.repository.name}")
    
except Exception as e:
    print(f"❌ Debug info:")
    print(f"   Error: {e}")
    print(f"   Type: {type(e).__name__}")
    import traceback
    traceback.print_exc()
```

## 🎯 Summary

The Python Alfresco API v2.0 provides flexible authentication options:

- ✅ **ClientFactory Pattern** - Recommended for most applications
- ✅ **Manual Authentication** - For custom authentication logic  
- ✅ **Environment Variables** - Secure credential management
- ✅ **Error Handling** - Comprehensive error management
- ✅ **SSL Support** - Production-ready security
- ✅ **Retry Logic** - Robust connection handling

Start with the ClientFactory pattern for the best developer experience, then customize as needed for your specific requirements.

For more information:
- **[API Documentation Index](API_DOCUMENTATION_INDEX.md)** - Complete API reference
- **[Authentication 401 Solution](AUTHENTICATION_401_SOLUTION.md)** - Troubleshooting guide
- **[examples/auth_examples.py](../examples/auth_examples.py)** - Working authentication examples 