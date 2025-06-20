# Alfresco Master Client Guide

A comprehensive guide to using the Alfresco Master Client and all 7 API sub-clients.

## Table of Contents

1. [Overview](#overview)
2. [Installation & Setup](#installation--setup)
3. [Master Client Usage](#master-client-usage)
4. [Authentication](#authentication)
5. [API Sub-Clients](#api-sub-clients)
6. [Advanced Usage](#advanced-usage)
7. [Error Handling](#error-handling)
8. [Best Practices](#best-practices)

## Overview

The Alfresco Master Client (`AlfrescoClient`) provides unified access to all 7 Alfresco REST APIs through a single, easy-to-use interface.

### Supported APIs

| API | Purpose | Client Property | Status |
|-----|---------|----------------|---------|
| **Authentication** | User authentication and ticket management | `client.auth` | ✅ Fully Working |
| **Core** | Nodes, sites, people, groups, comments, ratings | `client.core` | 🚧 Actions API Working |
| **Discovery** | Repository information and capabilities | `client.discovery` | ✅ Fully Working |
| **Search** | Content search with AFTS and CMIS queries | `client.search` | ✅ Fully Working |
| **Workflow** | Process definitions, tasks, workflows | `client.workflow` | 📦 Generated Client |
| **Model** | Content models, types, aspects | `client.model` | 📦 Generated Client |
| **Search SQL** | SQL-based content search | `client.search_sql` | 📦 Generated Client |

## Installation & Setup

### Basic Setup

```python
from enhanced_generated.AlfrescoClient import AlfrescoClient

client = AlfrescoClient(
    host="http://localhost:8080",
    username="admin",
    password="admin",
    verify_ssl=False  # Set to True in production
)
```

### Verify Connection

```python
# Test the connection and see which APIs are available
connection_info = client.test_connection()
print(f"Connected to: {connection_info['host']}")
print(f"Working APIs: {connection_info['working_apis']}/{connection_info['total_apis']}")
print(f"Success Rate: {connection_info['success_rate']}")

# Get list of working APIs
working_apis = client.get_working_apis()
print(f"Available APIs: {', '.join(working_apis)}")

# Get detailed API status
api_status = client.get_api_status()
for api_name, is_working in api_status.items():
    status = "✅ Working" if is_working else "❌ Failed"
    print(f"{api_name}: {status}")
```

## Master Client Usage

### Client Information

```python
# Get detailed client information
client_info = client.get_client_info()
print(f"Client Type: {client_info['client_type']}")
print(f"Host: {client_info['host']}")
print(f"Username: {client_info['username']}")

# Check API status
api_status = client.get_api_status()
for api_name, is_working in api_status.items():
    status = "✅ Working" if is_working else "❌ Failed"
    print(f"{api_name}: {status}")
```

### URL Management

```python
# Get API URLs for different services
auth_url = client.get_api_url('auth')
core_url = client.get_api_url('core')
search_url = client.get_api_url('search')

print(f"Auth URL: {auth_url}")
print(f"Core URL: {core_url}")
print(f"Search URL: {search_url}")
```

## Authentication

The master client handles authentication automatically, but you can also manage it manually.

### Automatic Authentication

```python
# Authentication is handled automatically when you create the client
client = AlfrescoClient(host="http://localhost:8080", username="admin", password="admin")

# All API calls will automatically include proper authentication
repo_info = client.discovery.get_repository_information()
```

### Manual Authentication Management

```python
# Create authentication ticket manually
try:
    ticket_response = client.auth.create_ticket(
        ticket_body={'userId': 'admin', 'password': 'admin'}
    )
    print("✅ Authentication successful")
    print(f"Ticket ID: {ticket_response.entry.id}")
except Exception as e:
    print(f"❌ Authentication failed: {e}")

# Validate ticket
try:
    validation = client.auth.validate_ticket()
    print("✅ Ticket is valid")
    print(f"User ID: {validation.entry.id}")
except Exception as e:
    print(f"❌ Ticket validation failed: {e}")

# Delete ticket (logout)
try:
    client.auth.delete_ticket()
    print("✅ Logged out successfully")
except Exception as e:
    print(f"❌ Logout failed: {e}")
```

## API Sub-Clients

### Authentication API ✅ **FULLY WORKING**

Manage user authentication and tickets.

```python
# Create authentication ticket
ticket = client.auth.create_ticket(
    ticket_body={'userId': 'testuser', 'password': 'password'}
)
print(f"Ticket: {ticket.entry.id}")

# Validate current ticket
validation = client.auth.validate_ticket()
print(f"Valid user: {validation.entry.id}")

# Delete ticket (logout)
client.auth.delete_ticket()
```

**Available Methods:**
- `create_ticket(ticket_body)` - Create authentication ticket
- `validate_ticket()` - Validate current ticket
- `delete_ticket()` - Delete/invalidate ticket

### Core API 🚧 **ACTIONS API WORKING**

Access core Alfresco functionality including nodes, sites, people, and groups.

```python
# Check what Core APIs are available
if isinstance(client.core, dict):
    print(f"Available Core APIs: {list(client.core.keys())}")
    
    # Actions API (currently working)
    if 'actions' in client.core:
        actions = client.core['actions'].list_actions()
        print(f"Found {len(actions.list.entries)} actions")
        
        # Show first few actions
        for i, action in enumerate(actions.list.entries[:3]):
            print(f"{i+1}. {action.entry.id}: {action.entry.title}")
            
        # Get specific action
        if actions.list.entries:
            first_action_id = actions.list.entries[0].entry.id
            specific_action = client.core['actions'].get_action(action_id=first_action_id)
            print(f"Retrieved action: {specific_action.entry.id}")

# Future APIs (planned)
planned_apis = ['nodes', 'sites', 'people', 'groups']
for api_name in planned_apis:
    if isinstance(client.core, dict) and api_name in client.core:
        print(f"✅ {api_name.title()} API available")
    else:
        print(f"🚧 {api_name.title()} API - Coming soon")
```

**Currently Available:**
- ✅ **Actions API** - Content actions and operations

**Planned APIs:**
- 🚧 **Nodes API** - File/folder operations
- 🚧 **Sites API** - Site management
- 🚧 **People API** - User management
- 🚧 **Groups API** - Group management

### Discovery API ✅ **FULLY WORKING**

Explore repository capabilities and information.

```python
# Get repository information
repo_info = client.discovery.get_repository_information()
repository = repo_info.entry.repository

print(f"Repository Name: {repository.name}")
print(f"Version: {repository.version.display}")
print(f"Edition: {getattr(repository, 'edition', 'Unknown')}")

# Additional information
status = getattr(repo_info.entry, 'status', None)
if status:
    print(f"Status: {status.isReadOnly}")
```

**Available Methods:**
- `get_repository_information()` - Get complete repository details

### Search API ✅ **FULLY WORKING**

Perform content searches using AFTS and CMIS queries.

```python
# Basic content search
search_request = {
    'query': {
        'query': 'cm:name:*',
        'language': 'afts'
    },
    'paging': {
        'maxItems': 10,
        'skipCount': 0
    }
}

results = client.search.search(search_request=search_request)
print(f"Found {len(results.list.entries)} results")

for result in results.list.entries:
    entry = result.entry
    print(f"- {entry.name} ({entry.nodeType})")

# Advanced search with filters
advanced_search = {
    'query': {
        'query': 'TYPE:cm:content',
        'language': 'afts'
    },
    'filterQueries': [
        {'query': 'cm:name:test*'}
    ],
    'sort': [
        {'type': 'FIELD', 'field': 'cm:name', 'ascending': True}
    ],
    'paging': {
        'maxItems': 5,
        'skipCount': 0
    }
}

advanced_results = client.search.search(search_request=advanced_search)
print(f"Advanced search found {len(advanced_results.list.entries)} results")
```

**Available Methods:**
- `search(search_request)` - Execute search with full query options

### Workflow API 📦 **GENERATED CLIENT**

Process and task management (generated client ready for testing).

```python
# Check if workflow API is available
if client.workflow:
    if isinstance(client.workflow, dict):
        print(f"Available Workflow APIs: {list(client.workflow.keys())}")
        
        # Example usage (when tested)
        # processes = client.workflow['processes'].list_processes()
        # tasks = client.workflow['tasks'].list_tasks()
    else:
        print("Workflow API available as single object")
else:
    print("Workflow API not available")
```

### Model API 📦 **GENERATED CLIENT**

Content models and types management (generated client ready for testing).

```python
# Check if model API is available
if client.model:
    print("Model API available")
    
    # Example usage (when tested)
    if hasattr(client.model, 'list_aspects'):
        # aspects = client.model.list_aspects()
        # types = client.model.list_types()
        pass
else:
    print("Model API not available")
```

### Search SQL API 📦 **GENERATED CLIENT**

SQL-based content search (requires Solr configuration).

```python
# Check if search SQL API is available
if client.search_sql:
    print("Search SQL API available")
    
    # Example SQL query (requires Solr setup)
    sql_query = {"stmt": "SELECT * FROM cmis:document LIMIT 5"}
    
    try:
        sql_results = client.search_sql.search(sql_query)
        print(f"SQL search found {len(sql_results.list.entries)} results")
    except Exception as e:
        print(f"SQL search failed (expected if Solr not configured): {e}")
else:
    print("Search SQL API not available")
```

## Advanced Usage

### API Availability Checking

```python
# Check which APIs are working before using them
def check_api_availability(client):
    """Check which APIs are available and working."""
    results = {}
    
    # Test each API
    apis_to_test = {
        'auth': lambda: client.auth.validate_ticket() if client.auth else None,
        'core': lambda: client.core['actions'].list_actions() if isinstance(client.core, dict) and 'actions' in client.core else None,
        'discovery': lambda: client.discovery.get_repository_information() if client.discovery else None,
        'search': lambda: client.search.search(search_request={'query': {'query': '*', 'language': 'afts'}, 'paging': {'maxItems': 1}}) if client.search else None,
    }
    
    for api_name, test_func in apis_to_test.items():
        try:
            result = test_func()
            results[api_name] = True if result else False
        except:
            results[api_name] = False
    
    return results

# Use the function
availability = check_api_availability(client)
for api_name, is_available in availability.items():
    status = "✅ Available" if is_available else "❌ Not available"
    print(f"{api_name}: {status}")
```

### Combining Multiple APIs

```python
# Example: Search and get repository info
def comprehensive_example(client):
    """Demonstrate using multiple APIs together."""
    
    # Step 1: Get repository information
    if client.discovery:
        try:
            repo_info = client.discovery.get_repository_information()
            print(f"Repository: {repo_info.entry.repository.name}")
        except Exception as e:
            print(f"Failed to get repository info: {e}")
    
    # Step 2: Authenticate (optional, as it's automatic)
    if client.auth:
        try:
            # Create a fresh ticket
            ticket = client.auth.create_ticket(
                ticket_body={'userId': 'admin', 'password': 'admin'}
            )
            print(f"Authenticated with ticket: {ticket.entry.id}")
        except Exception as e:
            print(f"Authentication failed: {e}")
    
    # Step 3: Search for content
    if client.search:
        try:
            search_results = client.search.search(search_request={
                'query': {'query': 'TYPE:cm:content', 'language': 'afts'},
                'paging': {'maxItems': 3}
            })
            print(f"Found {len(search_results.list.entries)} content items")
        except Exception as e:
            print(f"Search failed: {e}")
    
    # Step 4: Get available actions
    if isinstance(client.core, dict) and 'actions' in client.core:
        try:
            actions = client.core['actions'].list_actions()
            print(f"Available actions: {len(actions.list.entries)}")
        except Exception as e:
            print(f"Failed to get actions: {e}")

# Run the comprehensive example
comprehensive_example(client)
```

### Configuration Management

```python
# Environment-based configuration
import os

def create_client_from_environment():
    """Create client using environment variables."""
    
    host = os.getenv('ALFRESCO_HOST', 'http://localhost:8080')
    username = os.getenv('ALFRESCO_USERNAME', 'admin')
    password = os.getenv('ALFRESCO_PASSWORD', 'admin')
    verify_ssl = os.getenv('ALFRESCO_VERIFY_SSL', 'false').lower() == 'true'
    
    return AlfrescoClient(
        host=host,
        username=username,
        password=password,
        verify_ssl=verify_ssl
    )

# Use environment-based client
env_client = create_client_from_environment()
```

## Error Handling

### Robust Error Handling Patterns

```python
def safe_api_call(func, *args, **kwargs):
    """Safely execute an API call with comprehensive error handling."""
    try:
        result = func(*args, **kwargs)
        return {'success': True, 'data': result, 'error': None}
    except Exception as e:
        return {'success': False, 'data': None, 'error': str(e)}

# Example usage
def robust_repository_info(client):
    """Get repository information with error handling."""
    
    if not client.discovery:
        return {'success': False, 'error': 'Discovery API not available'}
    
    result = safe_api_call(client.discovery.get_repository_information)
    
    if result['success']:
        repo_data = result['data']
        return {
            'success': True,
            'repository_name': repo_data.entry.repository.name,
            'version': repo_data.entry.repository.version.display
        }
    else:
        return {
            'success': False,
            'error': f"Failed to get repository info: {result['error']}"
        }

# Use robust function
repo_result = robust_repository_info(client)
if repo_result['success']:
    print(f"Repository: {repo_result['repository_name']}")
else:
    print(f"Error: {repo_result['error']}")
```

### Connection Testing

```python
def test_all_apis(client):
    """Test all available APIs and report status."""
    
    test_results = {}
    
    # Test Authentication API
    if client.auth:
        auth_result = safe_api_call(client.auth.validate_ticket)
        test_results['Authentication'] = auth_result['success']
    
    # Test Discovery API
    if client.discovery:
        discovery_result = safe_api_call(client.discovery.get_repository_information)
        test_results['Discovery'] = discovery_result['success']
    
    # Test Search API
    if client.search:
        search_result = safe_api_call(
            client.search.search,
            search_request={'query': {'query': '*', 'language': 'afts'}, 'paging': {'maxItems': 1}}
        )
        test_results['Search'] = search_result['success']
    
    # Test Core API (Actions)
    if isinstance(client.core, dict) and 'actions' in client.core:
        core_result = safe_api_call(client.core['actions'].list_actions)
        test_results['Core (Actions)'] = core_result['success']
    
    return test_results

# Run comprehensive test
test_results = test_all_apis(client)
print("API Test Results:")
for api_name, success in test_results.items():
    status = "✅ Pass" if success else "❌ Fail"
    print(f"  {api_name}: {status}")
```

## Best Practices

### 1. Always Check API Availability

```python
# Good practice: Check before using
if client.auth:
    ticket = client.auth.create_ticket(ticket_body={'userId': 'admin', 'password': 'admin'})

# Even better: Use the built-in methods
working_apis = client.get_working_apis()
if 'auth' in working_apis:
    ticket = client.auth.create_ticket(ticket_body={'userId': 'admin', 'password': 'admin'})
```

### 2. Use Error Handling

```python
# Always wrap API calls in try-except blocks
try:
    repo_info = client.discovery.get_repository_information()
    print(f"Repository: {repo_info.entry.repository.name}")
except Exception as e:
    print(f"Failed to get repository info: {e}")
```

### 3. Validate Input Data

```python
def create_search_request(query, language='afts', max_items=10):
    """Create a properly formatted search request."""
    if not query:
        raise ValueError("Query cannot be empty")
    
    if language not in ['afts', 'cmis']:
        raise ValueError("Language must be 'afts' or 'cmis'")
    
    if max_items < 1 or max_items > 100:
        raise ValueError("max_items must be between 1 and 100")
    
    return {
        'query': {
            'query': query,
            'language': language
        },
        'paging': {
            'maxItems': max_items,
            'skipCount': 0
        }
    }

# Use validated input
search_request = create_search_request('cm:name:test*', 'afts', 5)
results = client.search.search(search_request=search_request)
```

### 4. Handle Different API Structures

```python
def get_core_api_info(client):
    """Get information about Core API structure."""
    if not client.core:
        return "Core API not available"
    
    if isinstance(client.core, dict):
        available_apis = list(client.core.keys())
        return f"Core API has {len(available_apis)} sub-APIs: {available_apis}"
    else:
        # Single object format
        methods = [method for method in dir(client.core) if not method.startswith('_')]
        return f"Core API has {len(methods)} methods available"

print(get_core_api_info(client))
```

### 5. Use Environment Variables for Configuration

```bash
# Set environment variables
export ALFRESCO_HOST=http://localhost:8080
export ALFRESCO_USERNAME=admin
export ALFRESCO_PASSWORD=admin
export ALFRESCO_VERIFY_SSL=false
```

```python
# Use in code
import os

client = AlfrescoClient(
    host=os.getenv('ALFRESCO_HOST', 'http://localhost:8080'),
    username=os.getenv('ALFRESCO_USERNAME', 'admin'),
    password=os.getenv('ALFRESCO_PASSWORD', 'admin'),
    verify_ssl=os.getenv('ALFRESCO_VERIFY_SSL', 'false').lower() == 'true'
)
```

### 6. Session Management

```python
class AlfrescoSession:
    """Manage Alfresco client session with proper cleanup."""
    
    def __init__(self, host, username, password):
        self.client = AlfrescoClient(host=host, username=username, password=password)
        self.authenticated = False
    
    def __enter__(self):
        # Authenticate when entering context
        if self.client.auth:
            try:
                self.client.auth.create_ticket(
                    ticket_body={'userId': self.client.username, 'password': self.client.password}
                )
                self.authenticated = True
            except Exception as e:
                print(f"Authentication failed: {e}")
        return self.client
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Clean up when exiting context
        if self.authenticated and self.client.auth:
            try:
                self.client.auth.delete_ticket()
            except Exception as e:
                print(f"Logout failed: {e}")

# Use session manager
with AlfrescoSession('http://localhost:8080', 'admin', 'admin') as client:
    # Use client here
    repo_info = client.discovery.get_repository_information()
    print(f"Repository: {repo_info.entry.repository.name}")
# Automatic cleanup when exiting
```
