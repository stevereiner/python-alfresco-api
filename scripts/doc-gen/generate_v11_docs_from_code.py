#!/usr/bin/env python3
"""
Generate V1.1 Documentation from Actual Code with Real Method Signatures

This script analyzes the V1.1 hierarchical architecture code and generates
comprehensive documentation with actual method names and signatures extracted
from the code, not placeholders.

Usage:
    python scripts/generate_v11_docs_from_code.py
"""

import os
import ast
import inspect
import importlib
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime

# Add project root to path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


class V11DocumentationGenerator:
    """Generate comprehensive documentation from V1.1 hierarchical code with real method signatures."""
    
    def __init__(self):
        self.docs_dir = project_root / "docs"
        self.clients_dir = project_root / "python_alfresco_api" / "clients"
        self.utils_dir = project_root / "python_alfresco_api" / "utils"
        
        # API mapping to documentation folders
        self.api_folders = {
            'auth': 'auth',
            'core': 'core', 
            'search': 'search',
            'discovery': 'discovery',
            'workflow': 'workflow',
            'model': 'model',
            'search_sql': 'search_sql'
        }
        
    def generate_all_docs(self):
        """Generate documentation for all V1.1 APIs."""
        print("🚀 V1.1 Documentation Generation - Real Method Signatures")
        print("=" * 70)
        print(f"📁 Source: {self.clients_dir}")
        print(f"📚 Target: {self.docs_dir}")
        print()
        
        total_apis = len(self.api_folders)
        success_count = 0
        
        for api_name, docs_folder in self.api_folders.items():
            print(f"📖 Generating {api_name.upper()} API documentation...")
            
            try:
                # Check if API client exists
                api_client_path = self.clients_dir / api_name
                if not api_client_path.exists():
                    print(f"   ⚠️ API client not found: {api_client_path}")
                    continue
                
                # Generate API documentation with real method extraction
                api_doc = self.generate_api_documentation(api_name)
                
                # Write API overview document
                api_doc_file = self.docs_dir / docs_folder / f"{api_name}_api.md"
                api_doc_file.parent.mkdir(parents=True, exist_ok=True)
                api_doc_file.write_text(api_doc)
                
                print(f"   ✅ Generated: {api_doc_file.relative_to(project_root)}")
                
                # Generate model documentation for this API
                models_doc = self.generate_models_documentation(api_name)
                models_doc_file = self.docs_dir / docs_folder / f"{api_name}_models.md"
                models_doc_file.write_text(models_doc)
                
                print(f"   ✅ Generated: {models_doc_file.relative_to(project_root)}")
                
                # Generate subsection docs with real method signatures
                subsection_count = self.generate_subsection_docs(api_name, docs_folder)
                if subsection_count > 0:
                    print(f"   📄 Generated {subsection_count} subsection docs with real methods")
                
                success_count += 1
                
            except Exception as e:
                print(f"   ❌ Error generating {api_name} docs: {e}")
                continue
        
        # Generate utility documentation with real method signatures
        print(f"\n🔧 Generating utility documentation...")
        try:
            utils_doc = self.generate_utils_documentation()
            utils_doc_file = self.docs_dir / "utils_api.md"
            utils_doc_file.write_text(utils_doc)
            print(f"   ✅ Generated: {utils_doc_file.relative_to(project_root)}")
        except Exception as e:
            print(f"   ❌ Error generating utils docs: {e}")
        
        # Update root clients_doc.md with current status and correct links
        print(f"\n📋 Updating root documentation...")
        try:
            self.update_root_documentation()
            print(f"   ✅ Updated: docs/clients_doc.md")
        except Exception as e:
            print(f"   ❌ Error updating root docs: {e}")
        
        print(f"\n🎉 Documentation generation complete!")
        print(f"📊 Success: {success_count}/{total_apis} APIs documented")
        print(f"📊 Generated: API docs + Model docs + Subsection docs")
        print(f"📚 Root: docs/clients_doc.md")
        
    def generate_api_documentation(self, api_name: str) -> str:
        """Generate comprehensive documentation for an API."""
        try:
            # Import the API client
            client_module = importlib.import_module(f"python_alfresco_api.clients.{api_name}")
            
            # Get the main client class
            client_class = self.find_main_client_class(client_module, api_name)
            
            if not client_class:
                return self.generate_basic_api_doc(api_name)
            
            # Analyze the client class with real method extraction
            client_info = self.analyze_client_class(client_class)
            subsections = self.discover_subsections(api_name)
            
            # Generate documentation with real method examples
            doc = self.build_api_documentation(api_name, client_class, client_info, subsections)
            
            return doc
            
        except Exception as e:
            print(f"   ⚠️ Could not analyze {api_name} client: {e}")
            return self.generate_basic_api_doc(api_name)
    
    def find_main_client_class(self, module, api_name: str):
        """Find the main client class in a module."""
        # Try common patterns
        class_names = [
            f"Alfresco{api_name.title()}Client",
            f"{api_name.title()}Client", 
            f"Alfresco{api_name.upper()}Client"
        ]
        
        for class_name in class_names:
            if hasattr(module, class_name):
                return getattr(module, class_name)
        
        # Fallback: find any class with "Client" in the name
        for name in dir(module):
            obj = getattr(module, name)
            if inspect.isclass(obj) and "Client" in name:
                return obj
        
        return None
    
    def analyze_client_class(self, client_class) -> Dict[str, Any]:
        """Analyze a client class to extract real method signatures."""
        info = {
            'name': client_class.__name__,
            'docstring': inspect.getdoc(client_class) or "No description available.",
            'methods': [],
            'properties': [],
            'subsections': []
        }
        
        # Analyze methods and properties
        for name, method in inspect.getmembers(client_class):
            if name.startswith('_'):
                continue
                
            if inspect.ismethod(method) or inspect.isfunction(method):
                method_info = {
                    'name': name,
                    'signature': self.get_method_signature(method),
                    'docstring': inspect.getdoc(method) or "No description available.",
                    'parameters': self.extract_parameters(method)
                }
                info['methods'].append(method_info)
            elif isinstance(method, property):
                prop_info = {
                    'name': name,
                    'docstring': inspect.getdoc(method) or "No description available."
                }
                info['properties'].append(prop_info)
        
        return info
    
    def get_method_signature(self, method) -> str:
        """Get a clean method signature."""
        try:
            sig = inspect.signature(method)
            return str(sig)
        except (ValueError, TypeError):
            return "()"
    
    def extract_parameters(self, method) -> List[Dict[str, Any]]:
        """Extract parameter information from a method."""
        try:
            sig = inspect.signature(method)
            params = []
            
            for param_name, param in sig.parameters.items():
                if param_name == 'self':
                    continue
                    
                param_info = {
                    'name': param_name,
                    'type': str(param.annotation) if param.annotation != inspect.Parameter.empty else 'Any',
                    'default': str(param.default) if param.default != inspect.Parameter.empty else None,
                    'required': param.default == inspect.Parameter.empty
                }
                params.append(param_info)
            
            return params
        except (ValueError, TypeError):
            return []
    
    def discover_subsections(self, api_name: str) -> List[Dict[str, Any]]:
        """Discover subsections within an API and extract their methods."""
        subsections = []
        api_path = self.clients_dir / api_name
        
        if not api_path.exists():
            return subsections
        
        # Look for subdirectories that contain client code
        for item in api_path.iterdir():
            if item.is_dir() and item.name != "__pycache__":
                # Check if it has client files
                if (item / "__init__.py").exists() or any(f.suffix == ".py" for f in item.iterdir()):
                    # Try to load the subsection client to get real methods
                    subsection_methods = self.extract_subsection_methods(api_name, item.name)
                    
                    subsections.append({
                        'name': item.name,
                        'title': item.name.replace('_', ' ').title(),
                        'path': str(item.relative_to(self.clients_dir)),
                        'methods': subsection_methods
                    })
        
        return subsections
    
    def extract_subsection_methods(self, api_name: str, subsection_name: str) -> List[Dict[str, Any]]:
        """Extract real method signatures from a subsection client."""
        methods = []
        
        try:
            # Try to import the subsection client
            subsection_module = importlib.import_module(f"python_alfresco_api.clients.{api_name}.{subsection_name}")
            
            # Find the client class in the subsection - try new naming convention first
            client_class = None
            
            # Try different class name patterns for subclients
            class_patterns = [
                f"{subsection_name.title()}Client",  # New pattern: ActionsClient, ActivitiesClient, etc.
                f"Alfresco{subsection_name.title()}Client",  # Old pattern: AlfrescoActionsClient (fallback)
                f"{subsection_name.upper()}Client",  # Uppercase pattern
                f"Alfresco{subsection_name.upper()}Client"  # Old uppercase pattern
            ]
            
            for pattern in class_patterns:
                if hasattr(subsection_module, pattern):
                    client_class = getattr(subsection_module, pattern)
                    break
            
            # If no specific pattern found, try to find any class with "Client" in name
            if not client_class:
                for name in dir(subsection_module):
                    obj = getattr(subsection_module, name)
                    if inspect.isclass(obj) and "Client" in name and not name.startswith('_'):
                        client_class = obj
                        break
            
            if client_class:
                # Extract methods from the client class
                for name, method in inspect.getmembers(client_class):
                    if name.startswith('_'):
                        continue
                        
                    if inspect.ismethod(method) or inspect.isfunction(method):
                        method_info = {
                            'name': name,
                            'signature': self.get_method_signature(method),
                            'docstring': inspect.getdoc(method) or "No description available.",
                            'parameters': self.extract_parameters(method)
                        }
                        methods.append(method_info)
            
        except Exception as e:
            print(f"   ⚠️ Could not extract methods from {api_name}.{subsection_name}: {e}")
        
        return methods
    
    def build_api_documentation(self, api_name: str, client_class, client_info: Dict, subsections: List) -> str:
        """Build comprehensive API documentation with real method examples."""
        api_title = api_name.replace('_', ' ').title()
        
        # Find a good example method from subsections for the quick start
        example_method = self.find_example_method(subsections)
        
        doc = f"""# {api_title} API - V1.1 Hierarchical Architecture

Auto-generated from actual V1.1 code on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Overview

{client_info['docstring']}

**Client Class**: `{client_info['name']}`

## Quick Start

```python
from python_alfresco_api import ClientFactory

# Create factory
factory = ClientFactory(base_url="http://localhost:8080")

# Get {api_name} client
{api_name}_client = factory.create_{api_name}_client()

# Real method examples:
{example_method['sync_example']}
{example_method['async_example']}
```

## Architecture

This API follows the V1.1 three-tier hierarchical architecture:

- **Level 1**: Global models shared across all APIs
- **Level 2**: API-level models and client (`{client_info['name']}`) 
- **Level 3**: Operation-specific subsections with focused functionality

"""

        # Add subsections with real method examples
        if subsections:
            doc += "## Subsections\n\n"
            doc += "This API is organized into the following operation groups:\n\n"
            
            for subsection in subsections:
                doc += f"### [{subsection['title']}]({subsection['name']}/{subsection['name']}_api.md)\n"
                doc += f"Operations for {subsection['title'].lower()} management.\n"
                
                # Show real method examples if available
                if subsection['methods']:
                    sample_methods = subsection['methods'][:3]  # Show first 3 methods
                    doc += "\n**Available Methods:**\n"
                    for method in sample_methods:
                        doc += f"- `{method['name']}{method['signature']}` - {method['docstring'].split('.')[0]}\n"
                    
                    if len(subsection['methods']) > 3:
                        doc += f"- *...and {len(subsection['methods']) - 3} more methods*\n"
                
                doc += "\n"
        
        # Add client properties (lazy-loaded subsections)
        if client_info['properties']:
            doc += "## Client Properties\n\n"
            doc += "Lazy-loaded subsection clients:\n\n"
            
            for prop in client_info['properties']:
                if not prop['name'].startswith('_'):
                    doc += f"### `{prop['name']}`\n"
                    doc += f"{prop['docstring']}\n\n"
        
        # Add direct methods if any
        if client_info['methods']:
            doc += "## Direct Methods\n\n"
            
            for method in client_info['methods']:
                if not method['name'].startswith('_'):
                    doc += f"### `{method['name']}{method['signature']}`\n"
                    doc += f"{method['docstring']}\n\n"
                    
                    # Show parameter details
                    if method['parameters']:
                        doc += "**Parameters:**\n"
                        for param in method['parameters']:
                            required = " (required)" if param['required'] else f" (default: {param['default']})"
                            doc += f"- `{param['name']}`: {param['type']}{required}\n"
                        doc += "\n"
        
        # Add sync/async patterns with real examples
        sync_example, async_example = self.get_real_method_examples(subsections)
        
        doc += f"""## Sync/Async Patterns

All operations support both synchronous and asynchronous execution:

```python
# Synchronous (perfect for scripts, MCP servers)
{sync_example}

# Asynchronous (perfect for web apps)
{async_example}
```

## 4-Pattern Method Examples

Each operation provides 4 execution patterns:

```python
# 1. Basic sync
{sync_example}

# 2. Basic async  
{async_example}

# 3. Detailed sync (with full HTTP response)
{sync_example.replace('(', '_detailed(')}

# 4. Detailed async (with full HTTP response)
{async_example.replace('await ', 'await ').replace('(', '_detailed_async(')}
```

## Raw Client Access

For advanced operations, access the underlying HTTP client:

```python
# Get raw client
raw_client = {api_name}_client._get_raw_client()

# Get HTTPx client for custom requests
httpx_client = raw_client.get_httpx_client()
response = httpx_client.get("/custom-endpoint")
```

## Related Documentation

- [V1.1 Architecture Overview](../clients_doc.md)
- [Authentication Guide](../AUTHENTICATION_GUIDE.md)
- [MCP Integration Guide](../V11_MCP_SYNC_MIGRATION_GUIDE.md)
"""

        return doc
    
    def find_example_method(self, subsections: List) -> Dict[str, str]:
        """Find a good example method from subsections for documentation."""
        default_example = {
            'sync_example': "# Example method calls",
            'async_example': "# Example async method calls"
        }
        
        if not subsections:
            return default_example
        
        # Look for common methods like 'get', 'list', 'create'
        for subsection in subsections:
            for method in subsection['methods']:
                method_name = method['name']
                if method_name in ['get', 'list', 'create', 'search']:
                    # Create realistic examples based on method signature
                    subsection_name = subsection['name']
                    
                    if method_name == 'get' and method['parameters']:
                        param_example = '"node-id-123"' if 'id' in method['parameters'][0]['name'] else '"example-param"'
                        return {
                            'sync_example': f"result = {subsection_name}_client.{subsection_name}.{method_name}({param_example})",
                            'async_example': f"result = await {subsection_name}_client.{subsection_name}.{method_name}_async({param_example})"
                        }
                    elif method_name == 'list':
                        return {
                            'sync_example': f"items = {subsection_name}_client.{subsection_name}.{method_name}()",
                            'async_example': f"items = await {subsection_name}_client.{subsection_name}.{method_name}_async()"
                        }
                    elif method_name == 'create' and method['parameters']:
                        return {
                            'sync_example': f"new_item = {subsection_name}_client.{subsection_name}.{method_name}(request_data)",
                            'async_example': f"new_item = await {subsection_name}_client.{subsection_name}.{method_name}_async(request_data)"
                        }
        
        # Fallback to first available method
        if subsections and subsections[0]['methods']:
            first_method = subsections[0]['methods'][0]
            subsection_name = subsections[0]['name']
            method_name = first_method['name']
            
            return {
                'sync_example': f"result = {subsection_name}_client.{subsection_name}.{method_name}()",
                'async_example': f"result = await {subsection_name}_client.{subsection_name}.{method_name}_async()"
            }
        
        return default_example
    
    def get_real_method_examples(self, subsections: List) -> Tuple[str, str]:
        """Get real method examples for sync/async patterns."""
        if not subsections or not subsections[0]['methods']:
            return ("result = client.operation.method()", "result = await client.operation.method_async()")
        
        # Use the first available method as example
        first_subsection = subsections[0]
        first_method = first_subsection['methods'][0]
        
        subsection_name = first_subsection['name']
        method_name = first_method['name']
        
        sync_example = f"result = {subsection_name}_client.{subsection_name}.{method_name}()"
        async_example = f"result = await {subsection_name}_client.{subsection_name}.{method_name}_async()"
        
        return sync_example, async_example
    
    def generate_basic_api_doc(self, api_name: str) -> str:
        """Generate basic documentation when code analysis fails."""
        api_title = api_name.replace('_', ' ').title()
        
        return f"""# {api_title} API - V1.1 Hierarchical Architecture

Auto-generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Overview

{api_title} API operations for Alfresco Content Services.

## Quick Start

```python
from python_alfresco_api import ClientFactory

# Create factory
factory = ClientFactory(base_url="http://localhost:8080")

# Get {api_name} client
{api_name}_client = factory.create_{api_name}_client()
```

## Architecture

This API follows the V1.1 three-tier hierarchical architecture with lazy-loaded operation subsections.

## Related Documentation

- [V1.1 Architecture Overview](../clients_doc.md)
- [Authentication Guide](../AUTHENTICATION_GUIDE.md)
"""
    
    def generate_models_documentation(self, api_name: str) -> str:
        """Generate comprehensive model documentation for an API."""
        api_title = api_name.replace('_', ' ').title()
        
        doc = f"""# {api_title} API Models - V1.1 Hierarchical Architecture

Auto-generated from actual V1.1 models on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Overview

Pydantic v2 models for the {api_title} API following the V1.1 three-tier architecture:

- **Level 2**: API-level shared models (`python_alfresco_api.clients.{api_name}.models`)
- **Level 3**: Operation-specific models (e.g., `python_alfresco_api.clients.{api_name}.nodes.models`)

## Level 2: API-Level Models

**Module**: `python_alfresco_api.clients.{api_name}.models`

```python
from python_alfresco_api.clients.{api_name}.models import *
```

"""
        
        # Try to extract API-level models
        try:
            api_models_module = importlib.import_module(f"python_alfresco_api.clients.{api_name}.models")
            models = self.extract_models_from_module(api_models_module)
            
            if models:
                doc += "### Available Models\n\n"
                for model in models:
                    doc += f"#### `{model['name']}`\n"
                    doc += f"{model['docstring']}\n\n"
                    
                    if model['fields']:
                        doc += "**Fields:**\n"
                        for field in model['fields']:
                            doc += f"- `{field['name']}`: {field['type']} - {field['description']}\n"
                        doc += "\n"
            else:
                doc += "### No API-level models found\n\n"
                
        except Exception as e:
            doc += f"### Could not load API-level models: {e}\n\n"
        
        # Add subsection models
        doc += "## Level 3: Operation-Specific Models\n\n"
        
        subsections = self.discover_subsections(api_name)
        if subsections:
            for subsection in subsections:
                subsection_name = subsection['name']
                doc += f"### {subsection['title']} Models\n\n"
                doc += f"**Module**: `python_alfresco_api.clients.{api_name}.{subsection_name}.models`\n\n"
                
                try:
                    subsection_models_module = importlib.import_module(f"python_alfresco_api.clients.{api_name}.{subsection_name}.models")
                    models = self.extract_models_from_module(subsection_models_module)
                    
                    if models:
                        doc += "```python\n"
                        doc += f"from python_alfresco_api.clients.{api_name}.{subsection_name}.models import (\n"
                        for i, model in enumerate(models):
                            comma = "," if i < len(models) - 1 else ""
                            doc += f"    {model['name']}{comma}\n"
                        doc += ")\n```\n\n"
                        
                        doc += "**Available Models:**\n"
                        for model in models:
                            doc += f"- **`{model['name']}`** - {model['docstring']}\n"
                        doc += "\n"
                    else:
                        doc += "No models found in this subsection.\n\n"
                        
                except Exception as e:
                    doc += f"Could not load models: {e}\n\n"
        else:
            doc += "No subsections found for this API.\n\n"
        
        # Add usage patterns
        doc += f"""## Usage Patterns

### Basic Model Usage

```python
from python_alfresco_api.clients.{api_name}.models import *

# API-level models (shared across operations)
response = SomeResponse(...)
entry = SomeEntry(...)
```

### Operation-Specific Models

```python
from python_alfresco_api.clients.{api_name}.nodes.models import (
    Node,
    NodeResponse,
    CreateNodeRequest
)

# Create request models
request = CreateNodeRequest(name="My File", node_type="cm:content")

# Work with response models  
response: NodeResponse = api_result
node: Node = response.entry
```

### Model Validation

All models use Pydantic v2 for validation:

```python
# Automatic validation
try:
    model = SomeModel(field1="value", field2=123)
except ValidationError as e:
    print(f"Validation failed: {{e}}")

# Manual validation
data = {{"field1": "value", "field2": "invalid"}}
try:
    model = SomeModel.model_validate(data)
except ValidationError as e:
    print(f"Validation failed: {{e}}")
```

## Related Documentation

- [{api_title} API Overview]({api_name}_api.md)
- [V1.1 Architecture](../clients_doc.md)
"""
        
        return doc
    
    def extract_models_from_module(self, module) -> List[Dict[str, Any]]:
        """Extract Pydantic models from a module."""
        models = []
        
        for name in dir(module):
            obj = getattr(module, name)
            
            # Check if it's a Pydantic model class
            if (inspect.isclass(obj) and 
                hasattr(obj, '__annotations__') and 
                hasattr(obj, '__fields__') and
                not name.startswith('_')):
                
                model_info = {
                    'name': name,
                    'docstring': inspect.getdoc(obj) or "No description available.",
                    'fields': []
                }
                
                # Extract field information
                try:
                    if hasattr(obj, '__fields__'):
                        for field_name, field_info in obj.__fields__.items():
                            field_data = {
                                'name': field_name,
                                'type': str(field_info.annotation) if hasattr(field_info, 'annotation') else 'Any',
                                'description': field_info.description if hasattr(field_info, 'description') and field_info.description else "No description"
                            }
                            model_info['fields'].append(field_data)
                except Exception:
                    # If field extraction fails, still include the model
                    pass
                
                models.append(model_info)
        
        return models
    
    def generate_subsection_docs(self, api_name: str, docs_folder: str) -> int:
        """Generate documentation for API subsections with real method signatures."""
        subsections = self.discover_subsections(api_name)
        count = 0
        
        for subsection in subsections:
            try:
                # Generate subsection documentation with real methods
                subsection_doc = self.generate_subsection_documentation(api_name, subsection)
                
                # Write subsection document
                subsection_dir = self.docs_dir / docs_folder / subsection['name']
                subsection_dir.mkdir(parents=True, exist_ok=True)
                
                subsection_file = subsection_dir / f"{subsection['name']}_api.md"
                subsection_file.write_text(subsection_doc)
                
                count += 1
                
            except Exception as e:
                print(f"   ⚠️ Could not generate {subsection['name']} docs: {e}")
                continue
        
        return count
    
    def generate_subsection_documentation(self, api_name: str, subsection: Dict) -> str:
        """Generate documentation for a specific subsection with real method signatures."""
        subsection_title = subsection['title']
        subsection_name = subsection['name']
        methods = subsection['methods']
        
        # Get real method examples
        method_examples = self.get_subsection_method_examples(methods, subsection_name)
        
        doc = f"""# {subsection_title} Operations - {api_name.title()} API

Auto-generated from V1.1 hierarchical code on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Overview

{subsection_title} operations for the {api_name.title()} API.

## Usage

```python
from python_alfresco_api import ClientFactory

# Create factory and client
factory = ClientFactory(base_url="http://localhost:8080")
{api_name}_client = factory.create_{api_name}_client()

# Access {subsection_name} operations
{subsection_name}_ops = {api_name}_client.{subsection_name}

# Real method examples (sync):
{method_examples['sync_examples']}

# Real method examples (async):
{method_examples['async_examples']}
```

## Available Methods

This subsection provides {len(methods)} operations:

"""
        
        # Document each method with real signatures
        for method in methods:
            doc += f"### `{method['name']}{method['signature']}`\n\n"
            doc += f"{method['docstring']}\n\n"
            
            # Show parameter details
            if method['parameters']:
                doc += "**Parameters:**\n"
                for param in method['parameters']:
                    required = " (required)" if param['required'] else f" (default: {param['default']})"
                    doc += f"- `{param['name']}`: {param['type']}{required}\n"
                doc += "\n"
            
            # Show 4-pattern examples for this method
            doc += "**Usage Patterns:**\n"
            doc += f"```python\n"
            doc += f"# 1. Basic sync\n"
            doc += f"result = {subsection_name}_ops.{method['name']}({self.get_method_param_example(method)})\n\n"
            doc += f"# 2. Basic async\n"
            doc += f"result = await {subsection_name}_ops.{method['name']}_async({self.get_method_param_example(method)})\n\n"
            doc += f"# 3. Detailed sync (with full HTTP response)\n"
            doc += f"result = {subsection_name}_ops.{method['name']}_detailed({self.get_method_param_example(method)})\n\n"
            doc += f"# 4. Detailed async (with full HTTP response)\n"
            doc += f"result = await {subsection_name}_ops.{method['name']}_detailed_async({self.get_method_param_example(method)})\n"
            doc += f"```\n\n"
        
        doc += f"""## Models

Operation-specific Pydantic models are available in:
```python
from python_alfresco_api.clients.{api_name}.{subsection_name}.models import *
```

## Related Documentation

- [{api_name.title()} API Overview](../{api_name}_api.md)
- [V1.1 Architecture](../../clients_doc.md)
"""
        
        return doc
    
    def get_subsection_method_examples(self, methods: List, subsection_name: str) -> Dict[str, str]:
        """Get real method examples for a subsection."""
        if not methods:
            return {
                'sync_examples': f"# No methods available",
                'async_examples': f"# No methods available"
            }
        
        # Get first few methods as examples
        example_methods = methods[:3]
        
        sync_examples = []
        async_examples = []
        
        for method in example_methods:
            param_example = self.get_method_param_example(method)
            sync_examples.append(f"result = {subsection_name}_ops.{method['name']}({param_example})")
            async_examples.append(f"result = await {subsection_name}_ops.{method['name']}_async({param_example})")
        
        return {
            'sync_examples': '\n'.join(sync_examples),
            'async_examples': '\n'.join(async_examples)
        }
    
    def get_method_param_example(self, method: Dict) -> str:
        """Generate example parameters for a method."""
        if not method['parameters']:
            return ""
        
        examples = []
        for param in method['parameters']:
            param_name = param['name']
            param_type = param['type']
            
            # Generate realistic examples based on parameter name and type
            if 'id' in param_name.lower():
                examples.append(f'{param_name}="abc123-def456"')
            elif 'name' in param_name.lower():
                examples.append(f'{param_name}="My Document"')
            elif 'path' in param_name.lower():
                examples.append(f'{param_name}="/path/to/file"')
            elif 'body' in param_name.lower() or 'request' in param_name.lower():
                examples.append(f'{param_name}=request_data')
            elif 'str' in param_type.lower():
                examples.append(f'{param_name}="example"')
            elif 'int' in param_type.lower():
                examples.append(f'{param_name}=100')
            elif 'bool' in param_type.lower():
                examples.append(f'{param_name}=True')
            elif param['required']:
                examples.append(f'{param_name}=...')
        
        return ', '.join(examples)
    
    def generate_utils_documentation(self) -> str:
        """Generate documentation for utility functions with real method signatures."""
        doc = f"""# Utility Functions - V1.1 Compatible

Auto-generated from actual utility code on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Overview

High-level utility functions optimized for V1.1 hierarchical clients and MCP server integration.

## Available Utilities

"""
        
        # Discover utility modules
        for util_file in self.utils_dir.glob("*.py"):
            if util_file.name == "__init__.py":
                continue
                
            module_name = util_file.stem
            try:
                # Import and analyze utility module
                util_module = importlib.import_module(f"python_alfresco_api.utils.{module_name}")
                
                doc += f"### {module_name.replace('_', ' ').title()}\n"
                doc += f"**Module**: `python_alfresco_api.utils.{module_name}`\n\n"
                
                # Get module docstring
                module_doc = inspect.getdoc(util_module)
                if module_doc:
                    doc += f"{module_doc}\n\n"
                
                # List functions with real signatures
                functions = []
                for name, obj in inspect.getmembers(util_module):
                    if inspect.isfunction(obj) and not name.startswith('_'):
                        sig = self.get_method_signature(obj)
                        func_doc = inspect.getdoc(obj) or "No description available."
                        functions.append(f"- **`{name}{sig}`** - {func_doc.split('.')[0]}.")
                
                if functions:
                    doc += "**Functions:**\n"
                    doc += "\n".join(functions)
                    doc += "\n\n"
                
            except Exception as e:
                doc += f"Could not analyze {module_name}: {e}\n\n"
        
        doc += """## Usage Patterns

### With V1.1 Hierarchical Clients

```python
from python_alfresco_api import ClientFactory
from python_alfresco_api.utils import search_utils, node_utils

# Create client
factory = ClientFactory(base_url="http://localhost:8080")
core_client = factory.create_core_client()

# Use utilities with V1.1 client - real method examples:
results = search_utils.simple_search(core_client.search, "admin OR test", max_items=10)
folder = node_utils.create_folder(core_client, "My New Folder", parent_id="-my-")
document = node_utils.upload_document(core_client, "document.pdf", "/path/to/file.pdf")
```

### With MCP Servers

Utilities are optimized for MCP (Model Context Protocol) server patterns:

```python
# MCP-compatible search with real method signatures
async def search_content_impl(query: str, ctx: Context) -> str:
    client = await ensure_connection()
    results = search_utils.simple_search(client.search, query, max_items=20)
    return mcp_formatters.format_search_results(results, query)

# MCP-compatible node operations
async def create_folder_impl(name: str, parent_id: str, ctx: Context) -> str:
    client = await ensure_connection()
    result = node_utils.create_folder(client, name, parent_id)
    return mcp_formatters.format_folder_creation_result(result, name, parent_id)
```

## Related Documentation

- [V1.1 Architecture](clients_doc.md)
- [MCP Integration Guide](V11_MCP_SYNC_MIGRATION_GUIDE.md)
"""
        
        return doc
    
    def update_root_documentation(self):
        """Update the root clients_doc.md with current status and correct links."""
        root_doc_file = self.docs_dir / "clients_doc.md"
        
        if not root_doc_file.exists():
            print(f"   ⚠️ Root documentation not found: {root_doc_file}")
            return
        
        # Read current content
        try:
            current_content = root_doc_file.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            # Try with different encoding
            current_content = root_doc_file.read_text(encoding='latin-1')
        
        # Add generation timestamp comment
        timestamp_comment = f"<!-- Auto-generated docs updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} -->"
        
        # Fix the links to point to generated files
        # Update API documentation links
        link_fixes = {
            # Old links -> New generated links
            'core/core-doc.md': 'core/core_api.md',
            'search/search-doc.md': 'search/search_api.md', 
            'discovery/discovery-doc.md': 'discovery/discovery_api.md',
            'workflow/workflow-doc.md': 'workflow/workflow_api.md',
            'model/model-doc.md': 'model/model_api.md',
            'search_sql/search-sql-doc.md': 'search_sql/search_sql_api.md',
            'auth/auth-doc.md': 'auth/auth_api.md'
        }
        
        # Apply link fixes
        updated_content = current_content
        for old_link, new_link in link_fixes.items():
            updated_content = updated_content.replace(old_link, new_link)
        
        # Insert timestamp at the beginning (after the first line)  
        lines = updated_content.split('\n')
        if len(lines) > 1:
            # Remove any existing timestamp
            if len(lines) > 1 and lines[1].startswith('<!-- Auto-generated docs updated:'):
                lines.pop(1)
            lines.insert(1, timestamp_comment)
            updated_content = '\n'.join(lines)
        
        # Add model documentation links
        # Find the API Documentation section and add model links
        api_section_pattern = r'(### \[([^\]]+) API\]\(([^)]+)\))\n([^#]*?)\n\n'
        import re
        
        def add_model_link(match):
            api_title = match.group(2)
            api_link = match.group(3)
            description = match.group(4)
            
            # Extract API name from link (e.g., 'core' from 'core/core_api.md')
            api_name = api_link.split('/')[0]
            model_link = f"{api_name}/{api_name}_models.md"
            
            return f"{match.group(1)}\n{description}\n\n**Models**: [{api_title} Models]({model_link})\n\n"
        
        updated_content = re.sub(api_section_pattern, add_model_link, updated_content)
        
        root_doc_file.write_text(updated_content, encoding='utf-8')


def main():
    """Main entry point."""
    generator = V11DocumentationGenerator()
    generator.generate_all_docs()


if __name__ == "__main__":
    main() 