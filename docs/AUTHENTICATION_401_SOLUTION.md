# Solving 401 Unauthorized Errors with Alfresco APIs

## Overview

You mentioned seeing 401 Unauthorized errors when trying to interact with Alfresco APIs. This document provides solutions based on the research and testing we've completed.

## Key Authentication Methods in Alfresco

Based on the research, Alfresco REST API supports these authentication methods:

### 1. Basic Authentication
- **Username and password** encoded in Base64 in the Authorization header
- Often used during development and testing
- **Security Note**: Should only be used over HTTPS in production

### 2. Ticket-based Authentication
- After successful authentication, Alfresco returns a **ticket** for subsequent API calls
- Tickets have a limited lifetime and can expire
- More secure than repeatedly sending username/password

### 3. Authentication Header Requirements
- Must include proper **Authorization header** with correct format
- Different endpoints may have different authentication requirements

## Common Causes of 401 Errors

| Cause | Description | Solution |
|-------|-------------|----------|
| **Invalid Credentials** | Wrong username/password provided | Verify credentials work in Alfresco Share UI |
| **Expired Tickets** | Ticket has exceeded its lifetime | Re-authenticate to get a new ticket |
| **Missing Authorization Header** | No authentication header sent | Include proper `Authorization: Basic <encoded>` header |
| **Wrong Auth Method** | Using ticket auth on basic auth endpoint | Use appropriate method for specific endpoint |
| **Server Configuration** | Alfresco authentication subsystem issues | Check server logs and auth config |

## Step-by-Step Solution

### Step 1: Test Discovery API (No Auth Required)
This endpoint typically doesn't require authentication:
```bash
curl -X GET "http://localhost:8080/alfresco/api/discovery"
```
If this fails, you have connectivity issues, not authentication issues.

### Step 2: Get Authentication Ticket
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

### Step 3: Use Ticket for Authentication
Encode the ticket and use it in requests:

**Linux/Mac:**
```bash
echo -n 'TICKET_xxxxxxxxxxxxxxx' | base64
```

**Windows PowerShell:**
```powershell
[Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("TICKET_xxxxxxxxxxxxxxx"))
```

**Make authenticated request:**
```bash
curl -X GET \
  -H "Authorization: Basic <base64-encoded-ticket>" \
  -H "Accept: application/json" \
  "http://localhost:8080/alfresco/api/-default-/public/alfresco/versions/1/sites"
```

## Python Implementation

Here's a practical Python class that handles authentication automatically:

```python
import requests
import base64

class AlfrescoAuthenticator:
    def __init__(self, server_url, username, password):
        self.server_url = server_url
        self.username = username
        self.password = password
        self.ticket = None
    
    def authenticate(self):
        """Get authentication ticket from Alfresco."""
        auth_url = f"{self.server_url}/alfresco/api/-default-/public/authentication/versions/1/tickets"
        auth_data = {"userId": self.username, "password": self.password}
        
        response = requests.post(auth_url, json=auth_data)
        if response.status_code == 201:
            self.ticket = response.json()['entry']['id']
            return True
        else:
            print(f"Authentication failed: {response.status_code} - {response.text}")
            return False
    
    def get_auth_headers(self):
        """Get headers with authentication."""
        if not self.ticket and not self.authenticate():
            raise Exception("Authentication failed")
        
        encoded_ticket = base64.b64encode(self.ticket.encode()).decode()
        return {
            "Authorization": f"Basic {encoded_ticket}",
            "Accept": "application/json"
        }
    
    def make_request(self, endpoint, method="GET", **kwargs):
        """Make authenticated request with automatic retry on 401."""
        headers = self.get_auth_headers()
        if 'headers' in kwargs:
            headers.update(kwargs['headers'])
        kwargs['headers'] = headers
        
        url = f"{self.server_url}{endpoint}"
        response = requests.request(method, url, **kwargs)
        
        # If 401, try re-authenticating once
        if response.status_code == 401:
            print("Token expired, re-authenticating...")
            self.ticket = None
            headers = self.get_auth_headers()
            kwargs['headers'] = headers
            response = requests.request(method, url, **kwargs)
        
        return response

# Usage Example
auth = AlfrescoAuthenticator("http://localhost:8080", "admin", "admin")

# Test different endpoints
endpoints_to_test = [
    "/alfresco/api/discovery",  # Should work without auth
    "/alfresco/api/-default-/public/alfresco/versions/1/sites",
    "/alfresco/api/-default-/public/alfresco/versions/1/people", 
    "/alfresco/api/-default-/public/search/versions/1/search"
]

for endpoint in endpoints_to_test:
    try:
        if "discovery" in endpoint:
            # Discovery doesn't need auth
            response = requests.get(f"http://localhost:8080{endpoint}")
        else:
            # Other endpoints need auth
            response = auth.make_request(endpoint)
        
        print(f"✅ {endpoint}: {response.status_code}")
    except Exception as e:
        print(f"❌ {endpoint}: Error - {e}")
```

## API Endpoint Authentication Requirements

| Endpoint | Authentication Required | Notes |
|----------|------------------------|-------|
| `/alfresco/api/discovery` | ❌ No | Repository info |
| `/alfresco/api/-default-/public/authentication/versions/1/tickets` | ❌ No | For getting tickets |
| `/alfresco/api/-default-/public/alfresco/versions/1/*` | ✅ Yes | Core APIs |
| `/alfresco/api/-default-/public/search/versions/1/*` | ✅ Yes | Search APIs |

## Debugging Checklist

When you get 401 errors, check these in order:

1. **✓ Server Connectivity**
   ```bash
   curl "http://localhost:8080/alfresco/api/discovery"
   ```

2. **✓ Credentials Are Correct**
   - Test login in Alfresco Share web interface
   - Verify username/password combination

3. **✓ Authentication Request Format**
   ```bash
   curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"userId":"admin","password":"admin"}' \
     "http://localhost:8080/alfresco/api/-default-/public/authentication/versions/1/tickets"
   ```

4. **✓ Ticket Usage Format**
   ```bash
   # Get ticket first, then:
   curl -H "Authorization: Basic <base64-encoded-ticket>" \
        "http://localhost:8080/alfresco/api/-default-/public/alfresco/versions/1/sites"
   ```

5. **✓ Check Server Logs**
   - Look for authentication errors in Alfresco logs
   - Check for configuration issues

## Using This Python Alfresco API Client

When using this client library, authentication is handled automatically:

```python
from enhanced_generated.AlfrescoClient import AlfrescoClient

# Create client - handles authentication automatically
client = AlfrescoClient(
    server_url="http://localhost:8080",
    username="admin", 
    password="admin"
)

try:
    # Client handles authentication behind the scenes
    sites = client.core.get_sites()
    print("✅ Authentication successful")
    print(f"Found {len(sites)} sites")
except Exception as e:
    print(f"❌ Error: {e}")
```

## Different Authentication Scenarios

### Scenario 1: Development/Testing
```python
# Use basic auth for development
client = AlfrescoClient("http://localhost:8080", "admin", "admin")
```

### Scenario 2: Production with Tickets
```python
# Get ticket and reuse it
auth = AlfrescoAuthenticator("https://alfresco.company.com", "username", "password")
if auth.authenticate():
    # Use ticket for multiple requests
    response1 = auth.make_request("/alfresco/api/-default-/public/alfresco/versions/1/sites")
    response2 = auth.make_request("/alfresco/api/-default-/public/alfresco/versions/1/people")
```

### Scenario 3: Handle Authentication Errors
```python
def safe_api_call(auth, endpoint):
    try:
        response = auth.make_request(endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"API call failed: {response.status_code}")
            return None
    except Exception as e:
        print(f"Authentication error: {e}")
        return None
```

## Summary

The key to resolving 401 authentication errors is:

1. **Test connectivity first** with Discovery API
2. **Get a valid ticket** using the authentication endpoint  
3. **Use the ticket properly** in Base64 encoded Authorization header
4. **Handle ticket expiration** by re-authenticating when needed
5. **Check server configuration** if all else fails

The Python client library in this project handles most of this automatically, but understanding the underlying process helps debug issues when they occur.

## Need Help?

If you're still getting 401 errors after following this guide:

1. Check the authentication strategies test: `python -m pytest tests/test_authentication_strategies.py -v -s`
2. Review the server logs for specific error messages
3. Test with curl first to isolate the issue
4. Verify Alfresco server authentication configuration 