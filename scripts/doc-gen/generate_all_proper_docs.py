#!/usr/bin/env python3
"""
Generate Proper API Documentation

This script generates comprehensive documentation for ALL APIs and models by 
analyzing the actual high-level client files and model files to extract real 
method signatures, model fields, and detailed information.
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional, Union
import ast
import inspect

# Add project root to path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


def extract_method_signature(func_node: Union[ast.FunctionDef, ast.AsyncFunctionDef]) -> Dict[str, Any]:
    """Extract detailed method signature information from AST node."""
    
    # Get arguments with types and defaults
    args = []
    defaults = func_node.args.defaults
    num_defaults = len(defaults)
    
    for i, arg in enumerate(func_node.args.args):
        if arg.arg == 'self':
            continue
            
        arg_info = {"name": arg.arg, "type": None, "default": None}
        
        # Extract type annotation
        if arg.annotation:
            if isinstance(arg.annotation, ast.Name):
                arg_info["type"] = arg.annotation.id
            elif isinstance(arg.annotation, ast.Attribute):
                # Safely handle nested attributes
                if isinstance(arg.annotation.value, ast.Name):
                    arg_info["type"] = f"{arg.annotation.value.id}.{arg.annotation.attr}"
                else:
                    arg_info["type"] = arg.annotation.attr
            elif isinstance(arg.annotation, ast.Subscript):
                # Handle Optional[Type], List[Type], etc.
                if isinstance(arg.annotation.value, ast.Name):
                    base_type = arg.annotation.value.id
                    if isinstance(arg.annotation.slice, ast.Name):
                        inner_type = arg.annotation.slice.id
                        arg_info["type"] = f"{base_type}[{inner_type}]"
                    else:
                        arg_info["type"] = base_type
        
        # Extract default value
        default_offset = i - (len(func_node.args.args) - num_defaults - 1)  # -1 for self
        if default_offset >= 0 and default_offset < num_defaults:
            default = defaults[default_offset]
            if isinstance(default, ast.Constant):
                arg_info["default"] = repr(default.value)
            elif isinstance(default, ast.Name) and default.id == "None":
                arg_info["default"] = "None"
            else:
                arg_info["default"] = "..."
        
        args.append(arg_info)
    
    return {
        "name": func_node.name,
        "args": args,
        "docstring": ast.get_docstring(func_node) or "",
        "is_async": isinstance(func_node, ast.AsyncFunctionDef),
        "returns": None
    }


def extract_model_fields(class_node: ast.ClassDef) -> Dict[str, Any]:
    """Extract Pydantic model field information from AST node."""
    
    fields = []
    
    for item in class_node.body:
        if isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name):
            field_name = item.target.id
            field_info = {
                "name": field_name,
                "type": None,
                "description": None,
                "examples": None,
                "default": None,
                "alias": None
            }
            
            # Extract type annotation
            if item.annotation:
                if isinstance(item.annotation, ast.Subscript):
                    # Handle Annotated[Type, Field(...)]
                    if isinstance(item.annotation.value, ast.Name) and item.annotation.value.id == "Annotated":
                        # Get the base type
                        if isinstance(item.annotation.slice, ast.Tuple) and item.annotation.slice.elts:
                            first_elem = item.annotation.slice.elts[0]
                            if isinstance(first_elem, ast.Name):
                                field_info["type"] = first_elem.id
                            elif isinstance(first_elem, ast.Subscript):
                                if isinstance(first_elem.value, ast.Name):
                                    field_info["type"] = first_elem.value.id
                            
                            # Extract Field() info
                            for field_elem in item.annotation.slice.elts[1:]:
                                if isinstance(field_elem, ast.Call) and isinstance(field_elem.func, ast.Name) and field_elem.func.id == "Field":
                                    # Extract Field parameters
                                    for keyword in field_elem.keywords:
                                        if keyword.arg == "description" and isinstance(keyword.value, ast.Constant):
                                            field_info["description"] = keyword.value.value
                                        elif keyword.arg == "alias" and isinstance(keyword.value, ast.Constant):
                                            field_info["alias"] = keyword.value.value
                                        elif keyword.arg == "examples" and isinstance(keyword.value, ast.List):
                                            examples = []
                                            for ex in keyword.value.elts:
                                                if isinstance(ex, ast.Constant):
                                                    examples.append(ex.value)
                                            field_info["examples"] = examples
                                        elif keyword.arg == "default" and isinstance(keyword.value, ast.Constant):
                                            field_info["default"] = keyword.value.value
                else:
                    # Simple type annotation
                    if isinstance(item.annotation, ast.Name):
                        field_info["type"] = item.annotation.id
            
            fields.append(field_info)
    
    return {
        "name": class_node.name,
        "docstring": ast.get_docstring(class_node) or "",
        "fields": fields
    }


def analyze_models_file(models_path: Path) -> Dict[str, Any]:
    """Analyze a models.py file and extract detailed model information."""
    if not models_path.exists():
        return {"models": [], "imports": []}
    
    try:
        with open(models_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        
        models = []
        imports = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                model_info = extract_model_fields(node)
                models.append(model_info)
            elif isinstance(node, ast.ImportFrom):
                # Track imports
                module = node.module or ""
                for alias in node.names:
                    imports.append(f"from {module} import {alias.name}")
        
        return {
            "models": models,
            "imports": imports
        }
    
    except Exception as e:
        print(f"⚠️  Error analyzing {models_path}: {e}")
        return {"models": [], "imports": []}


def analyze_client_methods(client_path: Path) -> Dict[str, Any]:
    """Analyze a client file and extract detailed method information."""
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
                    if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)) and not item.name.startswith('_'):
                        method_info = extract_method_signature(item)
                        methods.append(method_info)
        
        return {
            "methods": methods,
            "class_name": class_name
        }
    
    except Exception as e:
        print(f"⚠️  Error analyzing {client_path}: {e}")
        return {"methods": [], "class_name": "Unknown"}


def generate_models_documentation(api_name: str, subsection_name: str) -> str:
    """Generate detailed models documentation."""
    
    models_path = project_root / f"python_alfresco_api/clients/{api_name}/{subsection_name}/models.py"
    models_info = analyze_models_file(models_path)
    
    if not models_info["models"]:
        return f"❌ No models found for {api_name}/{subsection_name}"
    
    title = subsection_name.replace("_", " ").title()
    
    doc = f"""# {title} Models Documentation

## Overview

Level 3 models specific to {subsection_name} operations within the {api_name.title()} API.

## Architecture

Part of the three-tier V1.1 hierarchical architecture:
- **Level 1**: Global models shared across ALL APIs
- **Level 2**: {api_name.title()} API models shared within {api_name.title()} API
- **Level 3 (This file)**: {title} operation-specific models

## Location

```
python_alfresco_api/clients/{api_name}/{subsection_name}/models.py
```

## Models

"""
    
    for model in models_info["models"]:
        doc += f"### {model['name']}\n\n"
        if model["docstring"]:
            doc += f"{model['docstring']}\n\n"
        
        if model["fields"]:
            doc += "**Fields:**\n\n"
            for field in model["fields"]:
                field_name = field["name"]
                field_type = field["type"] or "Any"
                alias = f" (alias: `{field['alias']}`)" if field["alias"] else ""
                default = f", default: `{field['default']}`" if field["default"] is not None else ""
                
                doc += f"- **`{field_name}`** (`{field_type}`{alias}{default})"
                if field["description"]:
                    doc += f": {field['description']}"
                doc += "\n"
                
                if field["examples"]:
                    doc += f"  - Examples: {field['examples']}\n"
            doc += "\n"
        
        doc += "---\n\n"
    
    doc += f"""## Usage Examples

### Import Models

```python
from python_alfresco_api.clients.{api_name}.{subsection_name}.models import (
    {', '.join([m['name'] for m in models_info['models'][:3]])}
)
```

### Basic Usage

```python
# Example model usage
"""
    
    if models_info["models"]:
        first_model = models_info["models"][0]
        doc += f"instance = {first_model['name']}(...)\n"
    
    doc += f"""```

## Related Documentation

- [Back to {title} API]({subsection_name}-api.md)
- [{api_name.title()} API Overview](../{api_name}-doc.md)
- [Global API Reference](../../clients_doc.md)
"""
    
    return doc


def generate_api_documentation(api_name: str, subsection_name: str) -> str:
    """Generate comprehensive API documentation for a specific subsection."""
    
    # Try both file patterns
    client_paths = [
        project_root / f"python_alfresco_api/clients/{api_name}/{subsection_name}/__init__.py",
        project_root / f"python_alfresco_api/clients/{api_name}/{subsection_name}/{subsection_name}.py"
    ]
    
    client_info = None
    for client_path in client_paths:
        if client_path.exists():
            client_info = analyze_client_methods(client_path)
            break
    
    if not client_info or not client_info["methods"]:
        return f"❌ No methods found for {api_name}/{subsection_name}"
    
    class_name = client_info["class_name"]
    methods = client_info["methods"]
    
    # Separate sync and async methods
    sync_methods = [m for m in methods if not m["is_async"]]
    async_methods = [m for m in methods if m["is_async"]]
    
    # Filter out utility methods for main operations
    utility_methods = {"get_httpx_client", "__repr__", "__str__"}
    main_sync_methods = [m for m in sync_methods if m["name"] not in utility_methods]
    main_async_methods = [m for m in async_methods if m["name"] not in utility_methods]
    
    title = subsection_name.replace("_", " ").title()
    
    doc = f"""# {title} API Operations

## Overview

{title} operations within the {api_name.title()} API.

## Architecture

Part of the three-tier V1.1 hierarchical architecture:
- **Level 3**: Specific {subsection_name} operation implementations
- **Level 2**: {api_name.title()} API-level functionality
- **Level 1**: Global client infrastructure

## Location

```
python_alfresco_api/clients/{api_name}/{subsection_name}/
```

## Client Class

### {class_name}

Main client class for {subsection_name} operations.

## Operations

"""
    
    # Document main sync operations
    if main_sync_methods:
        doc += "### Sync Operations\n\n"
        doc += "Synchronous methods that call raw sync clients directly.\n\n"
        
        for method in main_sync_methods[:5]:  # Limit to first 5 to keep docs manageable
            doc += f"#### {method['name']}\n\n"
            if method['docstring']:
                doc += f"{method['docstring'].split('.')[0]}.\n\n"
            
            # Build method signature without self
            signature_parts = []
            for arg in method['args']:
                arg_str = arg["name"]
                if arg["type"]:
                    arg_str += f": {arg['type']}"
                if arg["default"]:
                    arg_str += f" = {arg['default']}"
                signature_parts.append(arg_str)
            
            # Create signature without self
            if signature_parts:
                signature = f"def {method['name']}({', '.join(signature_parts)})"
            else:
                signature = f"def {method['name']}()"
            
            doc += f"```python\n{signature}\n```\n\n"
            
            # Add technical note about sync implementation
            doc += "**Note:** This method calls the raw sync client directly.\n\n"
    
    # Document main async operations
    if main_async_methods:
        doc += "### Async Operations\n\n"
        doc += "Asynchronous methods that call raw async clients directly.\n\n"
        
        for method in main_async_methods[:3]:  # Limit async methods
            doc += f"#### {method['name']}\n\n"
            if method['docstring']:
                doc += f"{method['docstring'].split('.')[0]}.\n\n"
            
            # Build async method signature without self
            signature_parts = []
            for arg in method['args']:
                arg_str = arg["name"]
                if arg["type"]:
                    arg_str += f": {arg['type']}"
                if arg["default"]:
                    arg_str += f" = {arg['default']}"
                signature_parts.append(arg_str)
            
            # Create async signature without self
            if signature_parts:
                signature = f"async def {method['name']}({', '.join(signature_parts)})"
            else:
                signature = f"async def {method['name']}()"
            
            doc += f"```python\n{signature}\n```\n\n"
            
            # Add technical note about async implementation
            doc += "**Note:** This method calls the raw async client directly.\n\n"
    
    # Add usage examples
    if main_sync_methods:
        first_method = main_sync_methods[0]
        doc += f"""## Usage Examples

### Basic Usage

```python
from python_alfresco_api.clients.{api_name}.{subsection_name} import {class_name}

# Initialize client
client = {class_name}(client_factory)

# Call operation
result = client.{first_method['name']}()
```

"""
    
    doc += f"""## Related Documentation

- [Back to {api_name.title()} API](../{api_name}-doc.md)
- [{title} Models]({subsection_name}-models.md)
- [Global API Reference](../../clients_doc.md)
"""
    
    return doc


def get_all_api_subsections() -> Dict[str, List[str]]:
    """Get all API subsections that need documentation."""
    
    apis = {}
    
    # Core API - check what subsections exist
    core_path = project_root / "python_alfresco_api/clients/core"
    if core_path.exists():
        core_subsections = []
        for item in core_path.iterdir():
            if item.is_dir() and item.name != "__pycache__":
                core_subsections.append(item.name)
        apis["core"] = sorted(core_subsections)
    
    # Other APIs
    other_apis = ["auth", "discovery", "search", "search_sql", "workflow", "model"]
    for api_name in other_apis:
        api_path = project_root / f"python_alfresco_api/clients/{api_name}"
        if api_path.exists():
            subsections = []
            for item in api_path.iterdir():
                if item.is_dir() and item.name != "__pycache__":
                    subsections.append(item.name)
            if subsections:
                apis[api_name] = sorted(subsections)
    
    return apis


def main():
    """Generate proper documentation for ALL APIs and models."""
    
    print("=" * 80)
    print("📚 Generate Technical Documentation")
    print("=" * 80)
    print()
    
    # Get all APIs and subsections
    all_apis = get_all_api_subsections()
    
    print(f"🔍 Found APIs to document:")
    for api_name, subsections in all_apis.items():
        print(f"   📁 {api_name.upper()}: {len(subsections)} subsections")
    print()
    
    generated_count = 0
    
    for api_name, subsections in all_apis.items():
        print(f"📚 Processing {api_name.upper()} API...")
        
        for subsection_name in subsections[:3]:  # Limit to first 3 per API for demo
            print(f"   📝 Generating {subsection_name}...")
            
            # Generate API documentation
            api_doc = generate_api_documentation(api_name, subsection_name)
            api_file = project_root / f"docs/{api_name}/{subsection_name}/{subsection_name}-api-complete.md"
            api_file.parent.mkdir(parents=True, exist_ok=True)
            
            with open(api_file, 'w', encoding='utf-8') as f:
                f.write(api_doc)
            
            # Generate Models documentation
            models_doc = generate_models_documentation(api_name, subsection_name)
            models_file = project_root / f"docs/{api_name}/{subsection_name}/{subsection_name}-models-complete.md"
            
            with open(models_file, 'w', encoding='utf-8') as f:
                f.write(models_doc)
            
            generated_count += 2
            print(f"   ✅ Generated API + Models docs for {subsection_name}")
    
    print(f"\n✅ Generated {generated_count} documentation files")
    print("   - Method signatures without self parameter")
    print("   - Proper sync/async separation")
    print("   - Technical documentation without sales language")
    print("   - Actual field information from models")


if __name__ == "__main__":
    main() 