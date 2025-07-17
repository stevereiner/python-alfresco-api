#!/usr/bin/env python3
"""
Generate Proper API Documentation

This script generates comprehensive API documentation by analyzing the actual 
high-level client files and extracting real method signatures, arguments, 
and docstrings.
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
        "returns": None  # Could extract return annotation if needed
    }


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


def generate_method_documentation(method: Dict[str, Any]) -> str:
    """Generate detailed documentation for a single method."""
    
    name = method["name"]
    args = method["args"]
    docstring = method["docstring"]
    is_async = method["is_async"]
    
    # Build method signature
    signature_parts = []
    for arg in args:
        arg_str = arg["name"]
        if arg["type"]:
            arg_str += f": {arg['type']}"
        if arg["default"]:
            arg_str += f" = {arg['default']}"
        signature_parts.append(arg_str)
    
    signature = f"{'async ' if is_async else ''}def {name}(self"
    if signature_parts:
        signature += f", {', '.join(signature_parts)}"
    signature += ")"
    
    # Extract description from docstring
    description = "Operation description."
    examples = ""
    
    if docstring:
        lines = docstring.split('\n')
        if lines:
            description = lines[0].strip()
        
        # Extract examples if they exist
        in_examples = False
        example_lines = []
        for line in lines:
            if "Examples:" in line or "```python" in line:
                in_examples = True
                continue
            elif "```" in line and in_examples:
                break
            elif in_examples:
                example_lines.append(line)
        
        if example_lines:
            examples = '\n'.join(example_lines).strip()
    
    doc = f"""#### {name}

{description}

**Signature:**
```python
{signature}
```

"""
    
    # Add parameter documentation
    if args:
        doc += "**Parameters:**\n"
        for arg in args:
            type_str = f" ({arg['type']})" if arg['type'] else ""
            default_str = f", default: {arg['default']}" if arg['default'] else ""
            doc += f"- `{arg['name']}`{type_str}: Parameter description{default_str}\n"
        doc += "\n"
    
    # Add examples if available
    if examples:
        doc += f"**Example:**\n```python\n{examples}\n```\n\n"
    
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

```python
class {class_name}:
    def __init__(self, client_factory):
        self._client_factory = client_factory
        self._raw_client = None
```

## Operations

"""
    
    # Document main sync operations
    if main_sync_methods:
        doc += "### Sync Operations\n\n"
        doc += "Perfect for scripts, MCP servers, and command-line tools.\n\n"
        
        for method in main_sync_methods:
            doc += generate_method_documentation(method)
    
    # Document main async operations
    if main_async_methods:
        doc += "### Async Operations\n\n"
        doc += "Perfect for web applications and concurrent operations.\n\n"
        
        for method in main_async_methods:
            doc += generate_method_documentation(method)
    
    # Document utility methods
    utility_sync = [m for m in sync_methods if m["name"] in utility_methods]
    if utility_sync:
        doc += "### Utility Methods\n\n"
        for method in utility_sync:
            doc += generate_method_documentation(method)
    
    # Add usage examples
    if main_sync_methods:
        first_method = main_sync_methods[0]
        doc += f"""## Usage Examples

### Basic Usage

```python
from python_alfresco_api.clients.{api_name}.{subsection_name} import {class_name}

# Initialize
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


def main():
    """Generate proper documentation for specific APIs."""
    
    print("=" * 80)
    print("📚 Generate Proper API Documentation")
    print("=" * 80)
    print()
    
    # Generate documentation for the two problematic APIs
    apis_to_fix = [
        ("discovery", "discovery"),
        ("core", "nodes")
    ]
    
    for api_name, subsection_name in apis_to_fix:
        print(f"📝 Generating proper documentation for {api_name}/{subsection_name}...")
        
        doc_content = generate_api_documentation(api_name, subsection_name)
        
        # Write to file
        output_file = project_root / f"docs/{api_name}/{subsection_name}/{subsection_name}-api-fixed.md"
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(doc_content)
        
        print(f"✅ Generated: {output_file}")
        print(f"📊 Size: {len(doc_content)} characters")
        
        # Show preview
        lines = doc_content.split('\n')
        print("📖 Preview:")
        print("-" * 40)
        for line in lines[:15]:
            print(line)
        if len(lines) > 15:
            print(f"... and {len(lines) - 15} more lines")
        print("-" * 40)
        print()
    
    print("🎉 Proper API documentation generation complete!")


if __name__ == "__main__":
    main() 