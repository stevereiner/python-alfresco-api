#!/usr/bin/env python3
"""
Automated Documentation Generator for V1.1 Three-Tier Architecture

Generates comprehensive documentation for the hierarchical Alfresco APIs.
Fixed to use actual function names from high-level client files.
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional
import inspect
import ast

# Add project root to path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


def analyze_models_file(models_path: Path) -> Dict[str, Any]:
    """Analyze a models.py file and extract model information."""
    if not models_path.exists():
        return {"models": [], "imports": [], "exports": []}
    
    try:
        with open(models_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        
        models = []
        imports = []
        exports = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                # Extract class information
                docstring = ast.get_docstring(node) or "No description available"
                
                # Get base classes
                bases = []
                for base in node.bases:
                    if isinstance(base, ast.Name):
                        bases.append(base.id)
                    elif isinstance(base, ast.Attribute):
                        # Handle nested attributes like base.value.id
                        if isinstance(base.value, ast.Name):
                            bases.append(f"{base.value.id}.{base.attr}")
                        else:
                            bases.append(base.attr)
                
                # Get fields (simplified)
                fields = []
                for item in node.body:
                    if isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name):
                        field_name = item.target.id
                        fields.append(field_name)
                
                models.append({
                    "name": node.name,
                    "docstring": docstring,
                    "bases": bases,
                    "fields": fields
                })
            
            elif isinstance(node, ast.ImportFrom):
                # Track imports
                module = node.module or ""
                for alias in node.names:
                    imports.append(f"from {module} import {alias.name}")
            
            elif isinstance(node, ast.Assign):
                # Look for __all__ exports
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "__all__":
                        if isinstance(node.value, ast.List):
                            for elt in node.value.elts:
                                if isinstance(elt, ast.Str):
                                    exports.append(elt.s)
                                elif isinstance(elt, ast.Constant) and isinstance(elt.value, str):
                                    exports.append(elt.value)
        
        return {
            "models": models,
            "imports": imports,
            "exports": exports
        }
    
    except Exception as e:
        print(f"⚠️  Error analyzing {models_path}: {e}")
        return {"models": [], "imports": [], "exports": []}


def analyze_client_file(client_path: Path) -> Dict[str, Any]:
    """Analyze a client file and extract method information."""
    if not client_path.exists():
        return {"methods": [], "class_name": "Unknown"}
    
    try:
        with open(client_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        
        methods = []
        class_name = "Unknown"
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_name = node.name
                
                for item in node.body:
                    if isinstance(item, ast.FunctionDef) and not item.name.startswith('_'):
                        docstring = ast.get_docstring(item) or "No description available"
                        
                        # Get method arguments
                        args = []
                        for arg in item.args.args:
                            if arg.arg != 'self':
                                args.append(arg.arg)
                        
                        # Determine if async
                        is_async = isinstance(item, ast.AsyncFunctionDef) or item.name.endswith("_async")
                        
                        methods.append({
                            "name": item.name,
                            "docstring": docstring,
                            "args": args,
                            "is_async": is_async,
                            "is_sync": not is_async
                        })
        
        return {
            "methods": methods,
            "class_name": class_name
        }
    
    except Exception as e:
        print(f"⚠️  Error analyzing {client_path}: {e}")
        return {"methods": [], "class_name": "Unknown"}


def generate_operation_documentation(api_name: str, subsection_name: str, subsection_info: Dict[str, Any]) -> str:
    """Generate documentation for a specific operation subsection."""
    
    subsection_title = subsection_name.replace("_", " ").title()
    
    doc_content = f"""# {subsection_title} API Operations

## Overview

{subsection_title} operations within the {api_name.title()} API.

## Architecture

Part of the three-tier V1.1 hierarchical architecture:
- **Level 3**: Specific {subsection_name} operation implementations
- **Level 2**: {api_name.title()} API-level functionality
- **Level 1**: Global client infrastructure

## Location

```
python_alfresco_api/clients/{api_name}/{subsection_name}/__init__.py
```

## Client Class

### {subsection_info['client']['class_name']}

Main client class for {subsection_name} operations.

```python
class {subsection_info['client']['class_name']}:
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

"""
    
    # Separate sync and async methods
    sync_methods = [m for m in subsection_info['client']['methods'] if m['is_sync']]
    async_methods = [m for m in subsection_info['client']['methods'] if m['is_async']]
    
    # Document sync operations
    if sync_methods:
        doc_content += "### Sync Operations\n\n"
        doc_content += "All sync operations call raw client methods directly (no async wrapper).\n\n"
        
        for method in sync_methods:
            doc_content += f"#### {method['name']}\n\n"
            doc_content += f"{method['docstring'].split('.')[0]}.\n\n"
            
            # Generate method signature
            args_str = ", ".join(method['args']) if method['args'] else ""
            if args_str:
                args_str = f", {args_str}"
            
            doc_content += f"```python\n"
            doc_content += f"def {method['name']}(self{args_str}) -> ResponseType:\n"
            doc_content += f"    \"\"\"Sync {method['name']} operation.\"\"\"\n"
            doc_content += f"    raw_client = self._get_client()\n"
            doc_content += f"    return raw_client.{subsection_name}.{method['name']}.sync(client=raw_client{args_str})\n"
            doc_content += "```\n\n"
    
    # Document async operations
    if async_methods:
        doc_content += "### Async Operations\n\n"
        doc_content += "All async operations call raw client async methods directly.\n\n"
        
        for method in async_methods:
            doc_content += f"#### {method['name']}\n\n"
            doc_content += f"{method['docstring'].split('.')[0]}.\n\n"
            
            # Generate method signature (remove _async suffix for raw call)
            base_name = method['name'].replace('_async', '')
            args_str = ", ".join(method['args']) if method['args'] else ""
            if args_str:
                args_str = f", {args_str}"
            
            doc_content += f"```python\n"
            doc_content += f"async def {method['name']}(self{args_str}) -> ResponseType:\n"
            doc_content += f"    \"\"\"Async {method['name']} operation.\"\"\"\n"
            doc_content += f"    raw_client = self._get_client()\n"
            doc_content += f"    return await raw_client.{subsection_name}.{base_name}.asyncio(client=raw_client{args_str})\n"
            doc_content += "```\n\n"
    
    # Add usage examples with real method names
    doc_content += f"""## Usage Examples

### Basic Usage

```python
from python_alfresco_api.clients.{api_name}.{subsection_name} import {subsection_info['client']['class_name']}

# Initialize
client = {subsection_info['client']['class_name']}(client_factory)
"""
    
    # Add example with first real method
    if sync_methods:
        first_method = sync_methods[0]
        doc_content += f"""
# Sync operation
result = client.{first_method['name']}()
"""
    
    if async_methods:
        first_async = async_methods[0]
        doc_content += f"""
# Async operation
result = await client.{first_async['name']}()
"""
    
    doc_content += """```

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
    print(f"Client error: {e}")
except ValidationError as e:
    print(f"Validation error: {e}")
```

## Related Documentation

- [Back to """ + api_name.title() + f""" API](../{api_name}-doc.md)
- [Global API Reference](../../clients_doc.md)
"""
    
    return doc_content


def generate_api_documentation(api_name: str) -> str:
    """Generate comprehensive documentation for an API."""
    
    print(f"📝 Generating documentation for {api_name} API...")
    
    api_path = project_root / f"python_alfresco_api/clients/{api_name}"
    
    if not api_path.exists():
        return f"❌ API path not found: {api_path}"
    
    # Analyze Level 2 models
    level2_models_path = api_path / "models.py"
    level2_info = analyze_models_file(level2_models_path)
    
    # Analyze main client
    main_client_path = api_path / "__init__.py"
    main_client_info = analyze_client_file(main_client_path)
    
    # Analyze subsections
    subsections = []
    for item in api_path.iterdir():
        if item.is_dir() and item.name != "__pycache__":
            subsection_name = item.name
            
            # Analyze Level 3 models
            level3_models_path = item / "models.py"
            level3_models_info = analyze_models_file(level3_models_path)
            
            # Analyze subsection client (try both __init__.py and {subsection_name}.py)
            subsection_client_path = item / "__init__.py"
            if not subsection_client_path.exists():
                subsection_client_path = item / f"{subsection_name}.py"
            
            subsection_client_info = analyze_client_file(subsection_client_path)
            
            subsections.append({
                "name": subsection_name,
                "models": level3_models_info,
                "client": subsection_client_info
            })
    
    # Generate documentation
    api_title = api_name.replace("_", " ").title()
    
    doc_content = f"""# {api_title} API Documentation

## Overview

The {api_title} API provides {get_api_description(api_name)} capabilities within the Alfresco ecosystem.

This API follows the **V1.1 Three-Tier Architecture**:
- **Level 1**: Global models shared across ALL APIs
- **Level 2**: {api_title} API models shared within {api_title} API
- **Level 3**: Operation-specific models for specific {api_title} operations

## Architecture

```
python_alfresco_api/clients/{api_name}/
├── models.py                    # Level 2: {api_title} API models
├── __init__.py                  # Main {api_title} client
"""

    # Add subsection structure
    for subsection in subsections:
        doc_content += f"""└── {subsection['name']}/
    ├── models.py                # Level 3: {subsection['name'].title()} models
    └── __init__.py              # {subsection['name'].title()} client
"""
    
    doc_content += "```\n\n"
    
    # Main Client Documentation
    doc_content += f"## Main {api_title} Client\n\n"
    doc_content += f"**Class**: `{main_client_info['class_name']}`\n\n"
    doc_content += f"**File**: `clients/{api_name}/__init__.py`\n\n"
    
    # Subsections Documentation with real method names
    doc_content += f"## {api_title} Subsections\n\n"
    
    for subsection in subsections:
        subsection_title = subsection['name'].replace("_", " ").title()
        doc_content += f"### {subsection_title}\n\n"
        doc_content += f"**Client**: `{subsection['client']['class_name']}`\n\n"
        doc_content += f"**Files**:\n"
        doc_content += f"- Models: `clients/{api_name}/{subsection['name']}/models.py`\n"
        doc_content += f"- Client: `clients/{api_name}/{subsection['name']}/__init__.py`\n\n"
        
        # Show actual method names
        subsection_sync = [m for m in subsection['client']['methods'] if m['is_sync']]
        subsection_async = [m for m in subsection['client']['methods'] if m['is_async']]
        
        if subsection_sync or subsection_async:
            doc_content += f"**Operations** ({len(subsection_sync)} sync, {len(subsection_async)} async):\n"
            
            # Show sync methods
            for method in subsection_sync[:5]:  # Show first 5
                doc_content += f"- `{method['name']}()` (sync)\n"
            
            # Show async methods
            for method in subsection_async[:5]:  # Show first 5
                doc_content += f"- `{method['name']}()` (async)\n"
            
            if len(subsection_sync) + len(subsection_async) > 10:
                doc_content += f"- ... and {len(subsection_sync) + len(subsection_async) - 10} more methods\n"
            
            doc_content += "\n"
    
    # Usage Examples with real method names
    doc_content += f"""## Usage Examples

### Basic {api_title} Client

```python
from python_alfresco_api import ClientFactory
from python_alfresco_api.clients.{api_name} import {main_client_info['class_name']}

# Create client
factory = ClientFactory()
{api_name}_client = {main_client_info['class_name']}(factory)
"""
    
    # Add example with first real operation
    if subsections and subsections[0]['client']['methods']:
        first_subsection = subsections[0]
        first_method = first_subsection['client']['methods'][0]
        doc_content += f"""
# Access subsection and call real method
result = {api_name}_client.{first_subsection['name']}.{first_method['name']}()
"""
    
    doc_content += """```

### Subsection Clients

```python
"""
    
    for subsection in subsections[:2]:  # Show first 2 subsections
        subsection_title = subsection['name'].replace("_", " ").title()
        doc_content += f"""# {subsection_title} operations
from python_alfresco_api.clients.{api_name}.{subsection['name']} import {subsection['client']['class_name']}

{subsection['name']}_client = {subsection['client']['class_name']}(factory)
"""
        if subsection['client']['methods']:
            first_method = subsection['client']['methods'][0]
            doc_content += f"result = {subsection['name']}_client.{first_method['name']}()\n"
    
    doc_content += """```

### Master Client Access

```python
from python_alfresco_api import create_lazy_master_client

# Access through master client
master = create_lazy_master_client()
"""
    
    if subsections and subsections[0]['client']['methods']:
        first_subsection = subsections[0]
        first_method = first_subsection['client']['methods'][0]
        doc_content += f"result = master.{api_name}.{first_subsection['name']}.{first_method['name']}()\n"
    
    doc_content += "```\n\n"
    
    return doc_content


def get_api_description(api_name: str) -> str:
    """Get description for an API."""
    descriptions = {
        "auth": "authentication and ticket management",
        "core": "content repository operations",
        "discovery": "repository information and capabilities",
        "search": "content and metadata search",
        "search_sql": "SQL-based content search",
        "workflow": "process and task management",
        "model": "content model introspection"
    }
    return descriptions.get(api_name, "enterprise content management")


def main():
    """Generate documentation for specific API."""
    
    print("=" * 80)
    print("📚 V1.1 Three-Tier Architecture Documentation Generator")
    print("=" * 80)
    print()
    
    # Force output
    sys.stdout.flush()
    
    # Start with Discovery API (smallest)
    api_name = "discovery"
    print(f"🎯 Generating documentation for {api_name.upper()} API")
    print()
    
    try:
        doc_content = generate_api_documentation(api_name)
        
        # Create docs directory
        docs_dir = project_root / "docs"
        docs_dir.mkdir(parents=True, exist_ok=True)
        
        # Write documentation
        doc_path = docs_dir / f"{api_name}-doc-fixed.md"
        with open(doc_path, 'w', encoding='utf-8') as f:
            f.write(doc_content)
        
        print(f"✅ Generated {api_name} API documentation with real method names")
        print(f"📄 File: {doc_path}")
        print(f"📊 Size: {len(doc_content)} characters")
        print()
        
        # Show preview
        lines = doc_content.split('\n')
        print("📖 Documentation Preview:")
        print("-" * 50)
        for line in lines[:20]:  # Show first 20 lines
            print(line)
        if len(lines) > 20:
            print(f"... and {len(lines) - 20} more lines")
        print("-" * 50)
        print()
        
        print("✅ Documentation generation successful!")
        print()
        print("🔍 Real method names extracted from high-level client files")
        
    except Exception as e:
        print(f"❌ Error generating documentation: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main() 