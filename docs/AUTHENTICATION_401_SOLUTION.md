# Authentication 401 Solution Guide - Python Alfresco API v2.0

This guide provides comprehensive solutions for resolving HTTP 401 (Unauthorized) errors when using the Python Alfresco API v2.0.

## 🎯 Quick Fix

### Most Common Solution

```python
from python_alfresco_api import ClientFactory

# Use the modern ClientFactory pattern
factory = ClientFactory(
    base_url="http://localhost:8080",  # Note: /alfresco/api suffix
    username="admin",
    password="admin",
    verify_ssl=False  # For local development
)

clients = factory.create_all_clients()

# Test authentication
try:
    repo_info = clients['discovery'].get_repository_info()
    print(f"✅ Success! Connected to {repo_info.entry.repository.name}")
except Exception as e:
    print(f"❌ Still failing: {e}")
```

## 🔍 Diagnosis Steps

### Step 1: Verify Base URL Format

```python
# ✅ CORRECT formats
base_urls = [
    "http://localhost:8080",                       # Standard local (server URL)
    "https://your-domain.com/alfresco/api",         # HTTPS production
    "http://alfresco.company.com:8080/alfresco/api" # Custom domain
]

# ❌ INCORRECT formats (will cause 401)
bad_urls = [
    "http://localhost:8080",                    # Missing /alfresco/api
    "http://localhost:8080/alfresco",          # Missing /api
    "http://localhost:8080/alfresco/api/",     # Trailing slash
    "http://localhost:8080/api",               # Missing /alfresco
]
```

### Step 2: Test Authentication Systematically

```python
from python_alfresco_api import ClientFactory

def test_authentication(base_url, username, password):
    """Systematically test authentication"""
    
    print(f"🔍 Testing: {base_url}")
    print(f"   User: {username}")
    print(f"   Pass: {'*' * len(password)}")
    
    try:
        factory = ClientFactory(
            base_url=base_url,
            username=username,
            password=password,
            verify_ssl=False
        )
        
        clients = factory.create_all_clients()
        
        # Test with discovery API (lightest test)
        repo_info = clients['discovery'].get_repository_info()
        
        print(f"✅ SUCCESS!")
        print(f"   Server: {repo_info.entry.repository.name}")
        print(f"   Version: {repo_info.entry.repository.version.major}.{repo_info.entry.repository.version.minor}")
        return True
        
    except Exception as e:
        print(f"❌ FAILED: {e}")
        return False

# Test different configurations
test_configs = [
    ("http://localhost:8080", "admin", "admin"),
    ("http://127.0.0.1:8080/alfresco/api", "admin", "admin"),
    ("http://localhost:8080", "admin", "password"),
]

for base_url, username, password in test_configs:
    test_authentication(base_url, username, password)
    print("-" * 50)
```

## 🚨 Common 401 Causes & Solutions

### 1. Wrong Base URL

**Problem**: Using incorrect URL format
```python
# ❌ This will cause 401
factory = ClientFactory(
    base_url="http://localhost:8080",  # Missing /alfresco/api
    username="admin",
    password="admin"
)
```

**Solution**: Use correct URL format
```python
# ✅ Correct format
factory = ClientFactory(
    base_url="http://localhost:8080",  # Include /alfresco/api
    username="admin",
    password="admin"
)
```

### 2. Wrong Credentials

**Problem**: Incorrect username or password
```python
# ❌ Wrong credentials
factory = ClientFactory(
    base_url="http://localhost:8080",
    username="admin",
    password="wrong_password"  # Incorrect password
)
```

**Solution**: Verify credentials
```python
# ✅ Test credentials with curl first
# curl -u admin:admin http://localhost:8080/alfresco/api/-default-/public/alfresco/versions/1/discovery

# Then use correct credentials
factory = ClientFactory(
    base_url="http://localhost:8080",
    username="admin",
    password="admin"  # Correct password
)
```

### 3. Alfresco Not Running

**Problem**: Alfresco service is not started
```python
# This will fail if Alfresco is not running
factory = ClientFactory(
    base_url="http://localhost:8080",
    username="admin",
    password="admin"
)
```

**Solution**: Start Alfresco service
```bash
# Docker Compose
docker-compose up -d

# Or check if Alfresco is running
curl http://localhost:8080/alfresco/api/-default-/public/alfresco/versions/1/discovery
```

### 4. Network/Firewall Issues

**Problem**: Network connectivity or firewall blocking
```python
# May fail due to network issues
factory = ClientFactory(
    base_url="http://remote-alfresco:8080/alfresco/api",
    username="admin",
    password="admin"
)
```

**Solution**: Test network connectivity
```bash
# Test connectivity
ping remote-alfresco
telnet remote-alfresco 8080

# Test HTTP access
curl http://remote-alfresco:8080/alfresco/api/-default-/public/alfresco/versions/1/discovery
```

### 5. SSL Certificate Issues

**Problem**: SSL verification failing
```python
# May fail with SSL errors
factory = ClientFactory(
    base_url="https://alfresco.company.com/alfresco/api",
    username="admin",
    password="admin",
    verify_ssl=True  # Default, may cause issues with self-signed certs
)
```

**Solution**: Handle SSL appropriately
```python
# For development with self-signed certificates
factory = ClientFactory(
    base_url="https://alfresco.company.com/alfresco/api",
    username="admin",
    password="admin",
    verify_ssl=False  # Disable SSL verification
)

# For production with proper certificates
factory = ClientFactory(
    base_url="https://alfresco.company.com/alfresco/api",
    username="admin",
    password="admin",
    verify_ssl=True  # Keep SSL verification enabled
)
```

## 🔧 Advanced Troubleshooting

### Debug Authentication Flow

```python
import logging
from python_alfresco_api import ClientFactory

# Enable detailed logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def debug_authentication():
    """Debug authentication with detailed logging"""
    
    print("🔍 Starting authentication debug...")
    
    try:
        # Create factory with debug logging
        factory = ClientFactory(
            base_url="http://localhost:8080",
            username="admin",
            password="admin",
            verify_ssl=False
        )
        
        print("✅ Factory created successfully")
        
        # Get clients
        clients = factory.create_all_clients()
        print("✅ Clients created successfully")
        
        # Test each client
        print("\n🧪 Testing individual clients:")
        
        # Discovery (no auth required)
        try:
            repo_info = clients['discovery'].get_repository_info()
            print(f"✅ Discovery: {repo_info.entry.repository.name}")
        except Exception as e:
            print(f"❌ Discovery failed: {e}")
        
        # Auth (requires credentials)
        try:
            # This might not work depending on implementation
            current_user = clients['auth'].get_current_user()
            print(f"✅ Auth: {current_user.entry.id}")
        except Exception as e:
            print(f"❌ Auth failed: {e}")
        
        # Core (requires auth)
        try:
            nodes = clients['core'].get_nodes()
            print(f"✅ Core: Found {len(nodes.list.entries)} nodes")
        except Exception as e:
            print(f"❌ Core failed: {e}")
        
        print("\n🎉 Authentication debug complete!")
        
    except Exception as e:
        print(f"❌ Debug failed: {e}")
        import traceback
        traceback.print_exc()

# Run debug
debug_authentication()
```

### Test with Different Authentication Methods

```python
from python_alfresco_api.clients.auth_client import AlfrescoAuthClient
from python_alfresco_api.models.alfresco_auth_models import TicketBody

def test_ticket_authentication():
    """Test ticket-based authentication"""
    
    try:
        # Create auth client
        auth_client = AlfrescoAuthClient(
            base_url="http://localhost:8080"
        )
        
        # Create ticket
        ticket_request = TicketBody(
            userId="admin",
            password="admin"
        )
        
        ticket_response = auth_client.create_ticket(ticket_request)
        print(f"✅ Ticket created: {ticket_response.entry.id}")
        
        # Validate ticket
        validation = auth_client.validate_ticket(ticket_response.entry.id)
        print(f"✅ Ticket validated: {validation.entry.id}")
        
        return True
        
    except Exception as e:
        print(f"❌ Ticket authentication failed: {e}")
        return False

# Test ticket authentication
test_ticket_authentication()
```

### Comprehensive Connection Test

```python
def comprehensive_connection_test():
    """Comprehensive test of connection and authentication"""
    
    print("🔍 Comprehensive Connection Test")
    print("=" * 50)
    
    # Test configurations
    test_configs = [
        {
            "name": "Local HTTP",
            "base_url": "http://localhost:8080",
            "username": "admin",
            "password": "admin",
            "verify_ssl": False
        },
        {
            "name": "Local HTTP (127.0.0.1)",
            "base_url": "http://127.0.0.1:8080/alfresco/api",
            "username": "admin",
            "password": "admin",
            "verify_ssl": False
        }
    ]
    
    results = []
    
    for config in test_configs:
        print(f"\n🧪 Testing: {config['name']}")
        print(f"   URL: {config['base_url']}")
        
        try:
            factory = ClientFactory(
                base_url=config['base_url'],
                username=config['username'],
                password=config['password'],
                verify_ssl=config['verify_ssl']
            )
            
            clients = factory.create_all_clients()
            
            # Test discovery
            repo_info = clients['discovery'].get_repository_info()
            
            result = {
                "config": config['name'],
                "status": "SUCCESS",
                "server": repo_info.entry.repository.name,
                "version": f"{repo_info.entry.repository.version.major}.{repo_info.entry.repository.version.minor}"
            }
            
            print(f"✅ SUCCESS: {result['server']} v{result['version']}")
            
        except Exception as e:
            result = {
                "config": config['name'],
                "status": "FAILED",
                "error": str(e)
            }
            
            print(f"❌ FAILED: {result['error']}")
        
        results.append(result)
    
    # Summary
    print("\n📊 Test Summary:")
    print("=" * 50)
    
    for result in results:
        status_icon = "✅" if result['status'] == "SUCCESS" else "❌"
        print(f"{status_icon} {result['config']}: {result['status']}")
        
        if result['status'] == "SUCCESS":
            print(f"   Server: {result['server']} v{result['version']}")
        else:
            print(f"   Error: {result['error']}")
    
    return results

# Run comprehensive test
comprehensive_connection_test()
```

## 🛠️ Environment-Specific Solutions

### Docker Compose Environment

```python
# For Docker Compose setups
factory = ClientFactory(
    base_url="http://localhost:8080",  # Standard Docker port
    username="admin",
    password="admin",
    verify_ssl=False
)
```

### Docker with Custom Ports

```python
# If using custom ports in Docker
factory = ClientFactory(
    base_url="http://localhost:8081/alfresco/api",  # Custom port
    username="admin",
    password="admin",
    verify_ssl=False
)
```

### Remote Alfresco Server

```python
# For remote servers
factory = ClientFactory(
    base_url="https://alfresco.company.com/alfresco/api",
    username="your_username",
    password="your_password",
    verify_ssl=True  # Enable for production
)
```

### Development vs Production

```python
import os

# Environment-aware configuration
def create_alfresco_clients():
    """Create clients based on environment"""
    
    if os.getenv("ENVIRONMENT") == "production":
        # Production configuration
        factory = ClientFactory(
            base_url=os.getenv("ALFRESCO_BASE_URL"),
            username=os.getenv("ALFRESCO_USERNAME"),
            password=os.getenv("ALFRESCO_PASSWORD"),
            verify_ssl=True
        )
    else:
        # Development configuration
        factory = ClientFactory(
            base_url="http://localhost:8080",
            username="admin",
            password="admin",
            verify_ssl=False
        )
    
    return factory.create_all_clients()

# Usage
clients = create_alfresco_clients()
```

## 📋 Checklist for 401 Issues

### Before You Start
- [ ] Alfresco is running and accessible
- [ ] You have valid credentials
- [ ] Network connectivity is working
- [ ] Firewall allows connections

### URL Format Check
- [ ] Base URL includes `/alfresco/api`
- [ ] No trailing slash in URL
- [ ] Correct protocol (http/https)
- [ ] Correct port number

### Credentials Check
- [ ] Username is correct
- [ ] Password is correct
- [ ] User account is active
- [ ] User has necessary permissions

### SSL Check
- [ ] SSL verification disabled for development
- [ ] Valid certificates for production
- [ ] Proper SSL configuration

### Code Check
- [ ] Using `python_alfresco_api` imports
- [ ] Using `ClientFactory` pattern
- [ ] Proper exception handling
- [ ] Debug logging enabled

## 🎯 Final Verification

```python
def final_verification():
    """Final verification that everything works"""
    
    print("🎯 Final Verification")
    print("=" * 30)
    
    try:
        # Create clients
        factory = ClientFactory(
            base_url="http://localhost:8080",
            username="admin",
            password="admin",
            verify_ssl=False
        )
        
        clients = factory.create_all_clients()
        
        # Test key operations
        print("🔍 Testing key operations...")
        
        # 1. Discovery
        repo_info = clients['discovery'].get_repository_info()
        print(f"✅ Discovery: {repo_info.entry.repository.name}")
        
        # 2. Core
        nodes = clients['core'].get_nodes()
        print(f"✅ Core: {len(nodes.list.entries)} root nodes")
        
        # 3. Search
        search_results = clients['search'].search({
            "query": {"query": "*", "language": "afts"},
            "paging": {"maxItems": 1}
        })
        print(f"✅ Search: {search_results.list.pagination.totalItems} total items")
        
        print("\n🎉 ALL TESTS PASSED!")
        print("Your authentication is working correctly.")
        
        return True
        
    except Exception as e:
        print(f"❌ Verification failed: {e}")
        print("\nPlease review the solutions above and try again.")
        return False

# Run final verification
final_verification()
```

## 🆘 Still Having Issues?

If you're still experiencing 401 errors after following this guide:

1. **Check Alfresco logs** for detailed error messages
2. **Verify Alfresco configuration** (especially authentication settings)
3. **Test with curl** to isolate the issue:
   ```bash
   curl -u admin:admin http://localhost:8080/alfresco/api/-default-/public/alfresco/versions/1/discovery
   ```
4. **Review network configuration** (proxies, firewalls, etc.)
5. **Check Alfresco community forums** for server-specific issues

## 📚 Related Documentation

- **[Authentication Guide](AUTHENTICATION_GUIDE.md)** - Complete authentication documentation
- **[API Documentation Index](API_DOCUMENTATION_INDEX.md)** - Full API reference
- **[examples/auth_examples.py](../examples/auth_examples.py)** - Working authentication examples

Remember: The Python Alfresco API v2.0 with ClientFactory pattern resolves most authentication issues automatically. If you're still using old patterns, migrating to the new architecture will likely solve your problems! 