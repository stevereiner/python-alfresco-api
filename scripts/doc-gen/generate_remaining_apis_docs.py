#!/usr/bin/env python3
"""
Generate documentation for remaining APIs using hierarchical structure.
Creates docs for Auth, Discovery, Search, Workflow, Model, and Search SQL APIs.
"""

import os
import sys
import time
from pathlib import Path
from typing import Dict, List

# Define remaining APIs and their subsections
REMAINING_APIS = {
    'auth': {
        'name': 'Authentication API',
        'description': 'Handles user authentication, ticket creation, and session management',
        'subsections': ['authentication']
    },
    'discovery': {
        'name': 'Discovery API', 
        'description': 'Provides repository information and capability discovery',
        'subsections': ['discovery']
    },
    'search': {
        'name': 'Search API',
        'description': 'Enables content search and query capabilities',
        'subsections': ['search']
    },
    'workflow': {
        'name': 'Workflow API',
        'description': 'Manages business processes, tasks, and workflow automation',
        'subsections': ['tasks', 'process_definitions', 'processes', 'deployments']
    },
    'model': {
        'name': 'Model API',
        'description': 'Defines content types, aspects, and metadata schemas',
        'subsections': ['types', 'aspects']
    },
    'search_sql': {
        'name': 'Search SQL API',
        'description': 'Provides SQL-like query interface for content search',
        'subsections': ['sql']
    }
}

def generate_api_level_doc(api_name: str, api_info: Dict) -> str:
    """Generate API-level documentation."""
    subsections = api_info['subsections']
    
    # Create links to subsection docs
    subsection_links = []
    for subsection in subsections:
        subsection_links.append(f"- [{subsection.title()} Models]({subsection}/{subsection}-models.md)")
        subsection_links.append(f"- [{subsection.title()} API]({subsection}/{subsection}-api.md)")
    
    subsection_links_str = '\n'.join(subsection_links)
    
    content = f"""# {api_info['name']} Documentation

## Overview

{api_info['description']}

## Architecture

This API follows the three-tier V1.1 hierarchical architecture:

1. **Global Level**: Shared models like `BaseEntry`, `PagingInfo`, `ErrorResponse`
2. **API Level**: {api_info['name']}-specific models and responses
3. **Operation Level**: Specific operation models and implementations

## API-Level Models

### {api_info['name']} Models

Located in: `python_alfresco_api/clients/{api_name}/models.py`

**Core Models:**
- `{api_info['name'].replace(' ', '')}Response`: Standard response wrapper
- `{api_info['name'].replace(' ', '')}ListResponse`: List response wrapper  
- `Create{api_info['name'].replace(' ', '')}Request`: Creation request model

## Operation Groups

{subsection_links_str}

## Usage Examples

### Basic Usage

```python
from python_alfresco_api.clients.{api_name} import Alfresco{api_info['name'].replace(' ', '')}Client

# Initialize client
client = Alfresco{api_info['name'].replace(' ', '')}Client(client_factory)

# Access operation groups
{chr(10).join([f"result = client.{subsection}.operation_name()" for subsection in subsections])}
```

### Advanced Usage

```python
# Direct raw client access
raw_client = client._get_raw_client()
httpx_client = client.get_httpx_client()

# Async operations
async def async_example():
{chr(10).join([f"    result = await client.{subsection}.operation_name_async()" for subsection in subsections])}
```

## API Reference

See individual operation group documentation for detailed API references.
"""
    
    return content

def generate_subsection_models_doc(api_name: str, subsection: str) -> str:
    """Generate subsection models documentation."""
    content = f"""# {subsection.title()} Models

## Overview

Models specific to {subsection} operations within the {api_name.title()} API.

## Architecture

Part of the three-tier V1.1 hierarchical architecture:
- **Level 3**: Operation-specific models for {subsection} operations
- **Level 2**: {api_name.title()} API-level models  
- **Level 1**: Global shared models

## Location

```
python_alfresco_api/clients/{api_name}/{subsection}/models.py
```

## Models

### Response Models

#### {subsection.title()}Response
Standard response wrapper for {subsection} operations.

```python
class {subsection.title()}Response(BaseModel):
    entry: {subsection.title()}Entry
    # Additional response fields
```

#### {subsection.title()}ListResponse  
List response wrapper for {subsection} operations.

```python
class {subsection.title()}ListResponse(BaseModel):
    list: PagingInfo
    entries: List[{subsection.title()}Entry]
```

### Request Models

#### Create{subsection.title()}Request
Request model for creating {subsection} items.

```python
class Create{subsection.title()}Request(BaseModel):
    name: str
    # Additional creation fields
```

## Usage Examples

### Import Models

```python
from python_alfresco_api.clients.{api_name}.{subsection}.models import (
    {subsection.title()}Response,
    {subsection.title()}ListResponse,
    Create{subsection.title()}Request
)
```

### Type Hints

```python
from typing import List

def process_{subsection}(response: {subsection.title()}Response) -> List[str]:
    return [item.name for item in response.entries]
```

## Related Documentation

- [Back to {api_name.title()} API](../{api_name}-doc.md)
- [{subsection.title()} API Operations]({subsection}-api.md)
- [Global Models](../../clients_doc.md#global-models)
"""
    
    return content

def generate_subsection_api_doc(api_name: str, subsection: str) -> str:
    """Generate subsection API documentation."""
    content = f"""# {subsection.title()} API Operations

## Overview

{subsection.title()} operations within the {api_name.title()} API.

## Architecture

Part of the three-tier V1.1 hierarchical architecture:
- **Level 3**: Specific {subsection} operation implementations
- **Level 2**: {api_name.title()} API-level functionality
- **Level 1**: Global client infrastructure

## Location

```
python_alfresco_api/clients/{api_name}/{subsection}/__init__.py
```

## Client Class

### Alfresco{subsection.title()}Client

Main client class for {subsection} operations.

```python
class Alfresco{subsection.title()}Client:
    def __init__(self, client_factory):
        self._client_factory = client_factory
        self._raw_client = None
    
    def _get_client(self):
        \"\"\"Get or create the raw client.\"\"\"
        if self._raw_client is None:
            self._raw_client = self._client_factory.create_{api_name}_client()
        return self._raw_client
    
    def get_httpx_client(self):
        \"\"\"Get direct access to raw httpx client.\"\"\"
        return self._get_client().get_httpx_client()
```

## Operations

### Sync Operations

All sync operations call raw client methods directly (no async wrapper).

```python
def operation_name(self, **kwargs) -> ResponseType:
    \"\"\"Sync operation description.\"\"\"
    raw_client = self._get_client()
    return getattr(raw_client.{subsection}, 'operation_name')(**kwargs)
```

### Async Operations  

All async operations call raw client async methods directly.

```python
async def operation_name_async(self, **kwargs) -> ResponseType:
    \"\"\"Async operation description.\"\"\"
    raw_client = self._get_client()
    return await getattr(raw_client.{subsection}, 'operation_name_async')(**kwargs)
```

## Usage Examples

### Basic Usage

```python
from python_alfresco_api.clients.{api_name}.{subsection} import Alfresco{subsection.title()}Client

# Initialize
client = Alfresco{subsection.title()}Client(client_factory)

# Sync operation
result = client.operation_name(param1="value1")

# Async operation
result = await client.operation_name_async(param1="value1")
```

### Advanced Usage

```python
# Direct raw client access
raw_client = client._get_client()
httpx_client = client.get_httpx_client()

# Custom HTTP operations
response = httpx_client.get("/custom-endpoint")
```

## Error Handling

```python
try:
    result = client.operation_name()
except ClientError as e:
    print(f"Client error: {{e}}")
except ValidationError as e:
    print(f"Validation error: {{e}}")
```

## Related Documentation

- [Back to {api_name.title()} API](../{api_name}-doc.md)
- [{subsection.title()} Models]({subsection}-models.md)
- [Global API Reference](../../clients_doc.md)
"""
    
    return content

def create_docs_for_api(api_name: str, api_info: Dict) -> bool:
    """Create documentation for a specific API."""
    try:
        # Create API directory
        api_docs_dir = Path(f'docs/{api_name}')
        api_docs_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate API-level doc
        api_doc_content = generate_api_level_doc(api_name, api_info)
        api_doc_path = api_docs_dir / f'{api_name}-doc.md'
        
        with open(api_doc_path, 'w', encoding='utf-8') as f:
            f.write(api_doc_content)
        
        print(f"   📄 Created {api_doc_path}")
        
        # Generate subsection docs
        for subsection in api_info['subsections']:
            # Create subsection directory
            subsection_dir = api_docs_dir / subsection
            subsection_dir.mkdir(parents=True, exist_ok=True)
            
            # Generate models doc
            models_content = generate_subsection_models_doc(api_name, subsection)
            models_path = subsection_dir / f'{subsection}-models.md'
            
            with open(models_path, 'w', encoding='utf-8') as f:
                f.write(models_content)
            
            print(f"   📄 Created {models_path}")
            
            # Generate API doc
            api_content = generate_subsection_api_doc(api_name, subsection)
            api_path = subsection_dir / f'{subsection}-api.md'
            
            with open(api_path, 'w', encoding='utf-8') as f:
                f.write(api_content)
            
            print(f"   📄 Created {api_path}")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Error creating docs for {api_name}: {str(e)}")
        return False

def main():
    """Generate documentation for all remaining APIs."""
    print("📚 Generating documentation for remaining APIs...")
    print("=" * 60)
    
    success_count = 0
    total_count = len(REMAINING_APIS)
    
    for api_name, api_info in REMAINING_APIS.items():
        print(f"\n🌟 Creating {api_info['name']} documentation...")
        
        start_time = time.time()
        
        if create_docs_for_api(api_name, api_info):
            success_count += 1
            
        elapsed = time.time() - start_time
        print(f"   ⏱️  Completed in {elapsed:.2f}s")
    
    print("\n" + "=" * 60)
    print(f"🎉 Complete! Generated docs for {success_count}/{total_count} APIs")
    
    if success_count == total_count:
        print("✅ All remaining APIs now have complete documentation!")
        print("\n🏆 DOCUMENTATION SUMMARY:")
        
        total_files = 0
        for api_name, api_info in REMAINING_APIS.items():
            subsection_count = len(api_info['subsections'])
            files_count = 1 + (subsection_count * 2)  # 1 API doc + 2 docs per subsection
            total_files += files_count
            print(f"   • {api_info['name']}: {files_count} files")
        
        print(f"   • TOTAL: {total_files} documentation files")
    else:
        print(f"⚠️ {total_count - success_count} APIs need manual review")

if __name__ == '__main__':
    main() 