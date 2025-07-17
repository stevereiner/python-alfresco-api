#!/usr/bin/env python3
"""
Generate Level 3 Documentation for Individual Subsections

Shows what the smallest/most focused documentation looks like at the
operation-specific level (Level 3) of the three-tier architecture.
"""

import sys
from pathlib import Path
import ast

# Add project root to path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


def safe_ast_parse(content: str, file_path: str):
    """Safely parse AST with error handling."""
    try:
        return ast.parse(content)
    except SyntaxError as e:
        print(f"⚠️  Syntax error in {file_path} (line {e.lineno}): {e.msg}")
        return None
    except Exception as e:
        print(f"⚠️  Error parsing {file_path}: {e}")
        return None


def analyze_subsection_models(models_path: Path):
    """Analyze Level 3 models file."""
    if not models_path.exists():
        return {"models": [], "exports": []}
    
    try:
        with open(models_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = safe_ast_parse(content, str(models_path))
        if tree is None:
            return {"models": [], "exports": []}
        
        models = []
        exports = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                docstring = ast.get_docstring(node) or "No description available"
                
                # Get base classes
                bases = []
                for base in node.bases:
                    if isinstance(base, ast.Name):
                        bases.append(base.id)
                    elif isinstance(base, ast.Attribute):
                        bases.append(f"{base.value.id}.{base.attr}")
                
                # Get fields
                fields = []
                for item in node.body:
                    if isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name):
                        fields.append(item.target.id)
                
                models.append({
                    "name": node.name,
                    "docstring": docstring,
                    "bases": bases,
                    "fields": fields
                })
            
            elif isinstance(node, ast.Assign):
                # Look for __all__ exports
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "__all__":
                        if isinstance(node.value, ast.List):
                            for elt in node.value.elts:
                                if hasattr(elt, 'value') and isinstance(elt.value, str):
                                    exports.append(elt.value)
        
        return {"models": models, "exports": exports}
        
    except Exception as e:
        print(f"⚠️  Error analyzing {models_path}: {e}")
        return {"models": [], "exports": []}


def analyze_subsection_client(client_path: Path):
    """Analyze Level 3 client file."""
    if not client_path.exists():
        return {"methods": [], "class_name": "Unknown", "client_type": "Unknown"}
    
    try:
        with open(client_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = safe_ast_parse(content, str(client_path))
        if tree is None:
            return {"methods": [], "class_name": "Unknown", "client_type": "Unknown"}
        
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
                        
                        methods.append({
                            "name": item.name,
                            "docstring": docstring,
                            "args": args,
                            "is_async": item.name.endswith("_async"),
                            "is_sync": not item.name.endswith("_async") and not item.name.startswith('_')
                        })
        
        # Determine client type
        client_type = "Operation Client"
        if "lazy" in content.lower():
            client_type = "Lazy Loading Client"
        elif "master" in content.lower():
            client_type = "Master Client"
        
        return {
            "methods": methods,
            "class_name": class_name,
            "client_type": client_type
        }
        
    except Exception as e:
        print(f"⚠️  Error analyzing {client_path}: {e}")
        return {"methods": [], "class_name": "Unknown", "client_type": "Unknown"}


def generate_level3_doc(api_name: str, subsection_name: str) -> str:
    """Generate focused Level 3 documentation for a specific subsection."""
    
    subsection_path = project_root / f"python_alfresco_api/clients/{api_name}/{subsection_name}"
    
    if not subsection_path.exists():
        return f"❌ Subsection not found: {subsection_path}"
    
    # Analyze models and client
    models_info = analyze_subsection_models(subsection_path / "models.py")
    client_info = analyze_subsection_client(subsection_path / "__init__.py")
    
    # Generate documentation
    api_title = api_name.replace("_", " ").title()
    subsection_title = subsection_name.replace("_", " ").title()
    
    doc_content = f"""# {subsection_title} Operations - Level 3 Documentation

## Overview

**API**: {api_title}  
**Subsection**: {subsection_title}  
**Level**: 3 (Operation-Specific)

This is the most focused level of the V1.1 Three-Tier Architecture, containing models and operations specific to **{subsection_title}** within the {api_title} API.

## Architecture Location

```
python_alfresco_api/clients/{api_name}/{subsection_name}/
├── models.py    # Level 3: {subsection_title}-specific models
└── __init__.py  # Level 3: {subsection_title} operations client
```

## Three-Tier Context

- **Level 1 (Global)**: `clients/models.py` - Models shared across ALL APIs
- **Level 2 (API)**: `clients/{api_name}/models.py` - Models shared within {api_title} API  
- **Level 3 (This file)**: `clients/{api_name}/{subsection_name}/` - **{subsection_title}-specific models and operations**

## Level 3 Models ({len(models_info['models'])} models)

**File**: `clients/{api_name}/{subsection_name}/models.py`

"""

    # Document each model
    for model in models_info['models']:
        doc_content += f"### {model['name']}\n\n"
        
        # Clean up docstring
        docstring_lines = model['docstring'].split('\n')
        clean_docstring = docstring_lines[0] if docstring_lines else "No description available"
        doc_content += f"{clean_docstring}\n\n"
        
        if model['bases']:
            doc_content += f"**Inherits from**: {', '.join(model['bases'])}\n\n"
        
        if model['fields']:
            doc_content += f"**Fields** ({len(model['fields'])}):\n"
            for field in model['fields'][:8]:  # Show up to 8 fields
                doc_content += f"- `{field}`\n"
            if len(model['fields']) > 8:
                doc_content += f"- ... and {len(model['fields']) - 8} more fields\n"
            doc_content += "\n"
        else:
            doc_content += "**Fields**: None defined\n\n"
    
    # Document the client
    doc_content += f"""## Level 3 Client

**Class**: `{client_info['class_name']}`  
**Type**: {client_info['client_type']}  
**File**: `clients/{api_name}/{subsection_name}/__init__.py`

This client provides **{subsection_title}-specific operations** within the {api_title} API.

"""

    # Document methods
    sync_methods = [m for m in client_info['methods'] if m['is_sync']]
    async_methods = [m for m in client_info['methods'] if m['is_async']]
    
    if sync_methods:
        doc_content += f"### Sync Methods ({len(sync_methods)})\n\n"
        doc_content += "Perfect for MCP servers, scripts, and synchronous workflows:\n\n"
        
        for method in sync_methods:
            args_str = f"({', '.join(method['args'])})" if method['args'] else "()"
            doc_content += f"#### `{method['name']}{args_str}`\n\n"
            
            # Clean docstring
            first_sentence = method['docstring'].split('.')[0] if method['docstring'] else "No description"
            doc_content += f"{first_sentence}.\n\n"
    
    if async_methods:
        doc_content += f"### Async Methods ({len(async_methods)})\n\n"
        doc_content += "Perfect for web applications and concurrent operations:\n\n"
        
        for method in async_methods:
            args_str = f"({', '.join(method['args'])})" if method['args'] else "()"
            doc_content += f"#### `{method['name']}{args_str}`\n\n"
            
            # Clean docstring
            first_sentence = method['docstring'].split('.')[0] if method['docstring'] else "No description"
            doc_content += f"{first_sentence}.\n\n"
    
    # Usage examples
    doc_content += f"""## Usage Examples

### Direct Client Usage

```python
from python_alfresco_api import ClientFactory
from python_alfresco_api.clients.{api_name}.{subsection_name} import {client_info['class_name']}

# Create factory and client
factory = ClientFactory()
{subsection_name}_client = {client_info['class_name']}(factory)

# Use {subsection_title} operations
"""
    
    if sync_methods:
        first_method = sync_methods[0]['name']
        doc_content += f"result = {subsection_name}_client.{first_method}()\n"
    else:
        doc_content += f"# result = {subsection_name}_client.example_operation()\n"
    
    doc_content += "```\n\n"
    
    # Via main API client
    doc_content += f"""### Via {api_title} Client

```python
from python_alfresco_api.clients.{api_name} import Alfresco{api_title.replace(' ', '')}Client

# Access through main API client
{api_name}_client = Alfresco{api_title.replace(' ', '')}Client(factory)
{subsection_name}_ops = {api_name}_client.{subsection_name}  # Lazy loading

# Use operations
"""
    
    if sync_methods:
        first_method = sync_methods[0]['name']
        doc_content += f"result = {subsection_name}_ops.{first_method}()\n"
    
    doc_content += "```\n\n"
    
    # Via master client
    doc_content += f"""### Via Master Client

```python
from python_alfresco_api import create_lazy_master_client

# Access through master client (all APIs)
master = create_lazy_master_client()

# Use {subsection_title} operations
"""
    
    if sync_methods:
        first_method = sync_methods[0]['name']
        doc_content += f"result = master.{api_name}.{subsection_name}.{first_method}()\n"
    
    doc_content += "```\n\n"
    
    # Model imports
    if models_info['exports']:
        doc_content += f"""### Model Imports

```python
# Import {subsection_title}-specific models
from python_alfresco_api.clients.{api_name}.{subsection_name}.models import (
"""
        for export in models_info['exports'][:5]:  # Show first 5
            doc_content += f"    {export},\n"
        if len(models_info['exports']) > 5:
            doc_content += f"    # ... and {len(models_info['exports']) - 5} more models\n"
        doc_content += ")\n```\n\n"
    
    # Level 3 benefits
    doc_content += f"""## Level 3 Benefits

✅ **Perfect Locality**: {subsection_title} models exactly where {subsection_title} operations are  
✅ **Focused Scope**: Only {subsection_title}-related functionality  
✅ **Clean Imports**: `from .models import {subsection_title}Response`  
✅ **Easy Testing**: Mock just the {subsection_title} subsection  
✅ **Maintainable**: Small focused files vs huge monoliths  
✅ **Type Safety**: Rich Pydantic models with validation  
✅ **MCP Ready**: Perfect for AI tool interfaces  
✅ **Discoverable**: IDE auto-completion guides usage  

## Summary

**Level 3 provides the most focused experience possible:**

- **{len(models_info['models'])} models** specific to {subsection_title} operations
- **{len(sync_methods)} sync + {len(async_methods)} async methods** for all use cases  
- **3 access patterns**: Direct client, API client, or master client
- **Perfect locality**: Everything {subsection_title}-related in one place
- **Rich types**: Full Pydantic v2 validation and IDE support

This is the **smallest possible scope** in the three-tier architecture - exactly what you need for {subsection_title} operations, nothing more, nothing less.
"""

    return doc_content


def main():
    """Generate Level 3 documentation examples."""
    
    print("=" * 70)
    print("📖 Level 3 Documentation Generator")
    print("=" * 70)
    print()
    
    # Find smallest subsections to demonstrate
    examples = [
        ("discovery", "discovery"),  # Should be very small
        ("auth", "authentication"),  # Also small  
        ("search_sql", "sql"),       # Simple SQL operations
    ]
    
    docs_dir = project_root / "docs" / "level3_examples"
    docs_dir.mkdir(parents=True, exist_ok=True)
    
    for api_name, subsection_name in examples:
        print(f"📝 Generating Level 3 doc: {api_name}/{subsection_name}")
        
        try:
            doc_content = generate_level3_doc(api_name, subsection_name)
            
            # Write documentation
            doc_filename = f"{api_name}_{subsection_name}_level3.md"
            doc_path = docs_dir / doc_filename
            
            with open(doc_path, 'w', encoding='utf-8') as f:
                f.write(doc_content)
            
            doc_size = len(doc_content)
            print(f"✅ Generated {doc_filename} - {doc_size:,} chars")
            
        except Exception as e:
            print(f"❌ Error generating {api_name}/{subsection_name}: {e}")
    
    print()
    print("📋 Level 3 Documentation Examples:")
    print(f"📁 Location: {docs_dir}")
    
    for file in docs_dir.glob("*.md"):
        size = file.stat().st_size
        print(f"   📄 {file.name} - {size:,} bytes")
    
    print()
    print("🎯 Level 3 = Most Focused Documentation")
    print("   → Smallest possible scope")
    print("   → Operation-specific models and methods")
    print("   → Perfect locality principle")
    print("   → Easy to understand and maintain")


if __name__ == "__main__":
    main() 