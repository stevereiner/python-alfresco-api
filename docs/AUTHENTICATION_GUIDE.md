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
from enhanced_generated.AlfrescoClient import AlfrescoClient

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