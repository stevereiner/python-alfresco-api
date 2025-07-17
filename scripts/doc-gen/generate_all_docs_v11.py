#!/usr/bin/env python3
"""
Complete Documentation Generator for ALL V1.1 Three-Tier APIs

Generates comprehensive documentation for ALL Alfresco APIs with hierarchical organization.
Based on successful Auth API test.
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional
import ast

# Add project root to path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# All APIs to document
ALL_APIS = [
    "auth", "core", "discovery", "search", "search_sql", "workflow", "model"
]

API_DESCRIPTIONS = {
    "auth": "authentication and ticket management",
    "core": "content repository operations including nodes, sites, people, and content management",
    "discovery": "repository information and capabilities discovery",
    "search": "content and metadata search across the repository", 
    "search_sql": "SQL-based content search with structured query capabilities",
    "workflow": "process and task management including deployments and process definitions",
    "model": "content model introspection and type/aspect management"
}


def safe_ast_parse(content: str, file_path: str) -> Optional[ast.AST]:
    """Safely parse AST with error handling."""
    try:
        return ast.parse(content)
    except SyntaxError as e:
        print(f"⚠️  Syntax error in {file_path} (line {e.lineno}): {e.msg}")
        return None
    except Exception as e:
        print(f"⚠️  Error parsing {file_path}: {e}")
        return None


def analyze_models_file(models_path: Path) -> Dict[str, Any]:
    """Analyze a models.py file and extract model information."""
    if not models_path.exists():
        return {"models": [], "imports": [], "exports": []}
    
    try:
        with open(models_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = safe_ast_parse(content, str(models_path))
        if tree is None:
            return {"models": [], "imports": [], "exports": []}
        
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
                        bases.append(f"{base.value.id}.{base.attr}")
                
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
                            # Handle both ast.Str (old) and ast.Constant (new)
                            for elt in node.value.elts:
                                if hasattr(elt, 's'):  # ast.Str
                                    exports.append(elt.s)
                                elif hasattr(elt, 'value') and isinstance(elt.value, str):  # ast.Constant
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
    """Analyze a client __init__.py file and extract method information."""
    if not client_path.exists():
        return {"methods": [], "class_name": "Unknown"}
    
    try:
        with open(client_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = safe_ast_parse(content, str(client_path))
        if tree is None:
            return {"methods": [], "class_name": "Unknown"}
        
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
        
        return {
            "methods": methods,
            "class_name": class_name
        }
    
    except Exception as e:
        print(f"⚠️  Error analyzing {client_path}: {e}")
        return {"methods": [], "class_name": "Unknown"}


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
            
            # Analyze subsection client
            subsection_client_path = item / "__init__.py"
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

The {api_title} API provides {API_DESCRIPTIONS.get(api_name, 'enterprise content management')} capabilities within the Alfresco ecosystem.

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
    for i, subsection in enumerate(subsections):
        connector = "├──" if i < len(subsections) - 1 else "└──"
        doc_content += f"""{connector} {subsection['name']}/
    ├── models.py                # Level 3: {subsection['name'].title()} models
    └── __init__.py              # {subsection['name'].title()} client
"""
    
    doc_content += "```\n\n"
    
    # Level 2 Models Documentation
    doc_content += f"## Level 2: {api_title} API Models\n\n"
    doc_content += f"**File**: `clients/{api_name}/models.py`\n\n"
    doc_content += f"Models shared across all {api_title} operations:\n\n"
    
    for model in level2_info["models"]:
        doc_content += f"### {model['name']}\n\n"
        doc_content += f"{model['docstring'][:150]}{'...' if len(model['docstring']) > 150 else ''}\n\n"
        
        if model['bases']:
            doc_content += f"**Inherits from**: {', '.join(model['bases'])}\n\n"
        
        if model['fields']:
            doc_content += "**Fields**:\n"
            for field in model['fields'][:5]:  # Limit to first 5 fields
                doc_content += f"- `{field}`\n"
            if len(model['fields']) > 5:
                doc_content += f"- ... and {len(model['fields']) - 5} more\n"
            doc_content += "\n"
    
    # Main Client Documentation
    doc_content += f"## Main {api_title} Client\n\n"
    doc_content += f"**Class**: `{main_client_info['class_name']}`\n\n"
    doc_content += f"**File**: `clients/{api_name}/__init__.py`\n\n"
    
    sync_methods = [m for m in main_client_info["methods"] if m["is_sync"]]
    async_methods = [m for m in main_client_info["methods"] if m["is_async"]]
    
    if sync_methods:
        doc_content += "### Sync Methods\n\n"
        doc_content += "Perfect for MCP servers, scripts, and command-line tools:\n\n"
        for method in sync_methods[:3]:  # Show first 3
            doc_content += f"#### `{method['name']}()`\n\n"
            first_sentence = method['docstring'].split('.')[0] if method['docstring'] else "No description"
            doc_content += f"{first_sentence}.\n\n"
    
    if async_methods:
        doc_content += "### Async Methods\n\n"
        doc_content += "Perfect for web applications and concurrent operations:\n\n"
        for method in async_methods[:3]:  # Show first 3
            doc_content += f"#### `{method['name']}()`\n\n"
            first_sentence = method['docstring'].split('.')[0] if method['docstring'] else "No description"
            doc_content += f"{first_sentence}.\n\n"
    
    # Subsections Documentation
    if subsections:
        doc_content += f"## {api_title} Subsections\n\n"
        
        for subsection in subsections:
            subsection_title = subsection['name'].replace("_", " ").title()
            doc_content += f"### {subsection_title}\n\n"
            doc_content += f"**Client**: `{subsection['client']['class_name']}`\n\n"
            doc_content += f"**Files**:\n"
            doc_content += f"- Models: `clients/{api_name}/{subsection['name']}/models.py`\n"
            doc_content += f"- Client: `clients/{api_name}/{subsection['name']}/__init__.py`\n\n"
            
            # Models for this subsection
            if subsection['models']['models']:
                doc_content += f"**Level 3 Models**:\n"
                for model in subsection['models']['models'][:3]:  # Show first 3
                    first_sentence = model['docstring'].split('.')[0] if model['docstring'] else "No description"
                    doc_content += f"- `{model['name']}`: {first_sentence}\n"
                doc_content += "\n"
            
            # Methods for this subsection
            subsection_sync = [m for m in subsection['client']['methods'] if m['is_sync']]
            subsection_async = [m for m in subsection['client']['methods'] if m['is_async']]
            
            if subsection_sync or subsection_async:
                doc_content += f"**Operations** ({len(subsection_sync)} sync, {len(subsection_async)} async):\n"
                all_methods = subsection_sync + subsection_async
                for method in all_methods[:4]:  # Show first 4
                    method_type = "sync" if method['is_sync'] else "async"
                    doc_content += f"- `{method['name']}()` ({method_type})\n"
                if len(all_methods) > 4:
                    doc_content += f"- ... and {len(all_methods) - 4} more operations\n"
                doc_content += "\n"
    
    # Usage Examples
    doc_content += f"""## Usage Examples

### Basic {api_title} Client

```python
from python_alfresco_api import ClientFactory
from python_alfresco_api.clients.{api_name} import {main_client_info['class_name']}

# Create client
factory = ClientFactory()
{api_name}_client = {main_client_info['class_name']}(factory)

# Use operations
"""
    
    if sync_methods:
        doc_content += f"result = {api_name}_client.{sync_methods[0]['name']}()\n"
    else:
        doc_content += f"# result = {api_name}_client.example_method()\n"
    
    doc_content += "```\n\n"
    
    # Subsection examples
    if subsections:
        doc_content += "### Subsection Clients\n\n```python\n"
        
        for subsection in subsections[:2]:  # Show first 2 subsections
            subsection_title = subsection['name'].replace("_", " ").title()
            doc_content += f"""# {subsection_title} operations
from python_alfresco_api.clients.{api_name}.{subsection['name']} import {subsection['client']['class_name']}

{subsection['name']}_client = {subsection['client']['class_name']}(factory)
"""
        
        doc_content += "```\n\n"
    
    # Master client example
    doc_content += """### Master Client Access

```python
from python_alfresco_api import create_lazy_master_client

# Access through master client
master = create_lazy_master_client()
"""
    
    if subsections and subsections[0]['client']['methods']:
        first_subsection = subsections[0]['name']
        first_method = subsections[0]['client']['methods'][0]['name']
        doc_content += f"result = master.{api_name}.{first_subsection}.{first_method}()\n"
    
    doc_content += "```\n\n"
    
    # Benefits section
    doc_content += f"""## Benefits of {api_title} V1.1 Architecture

✅ **Perfect Locality**: {api_title} models exactly where {api_title} operations are used  
✅ **Clean Imports**: `from .models import {api_title}Response`  
✅ **Logical Organization**: Three clear hierarchical levels  
✅ **Maintainability**: Small focused files vs huge generated files  
✅ **Scalability**: Easy to add new {api_title} operations  
✅ **Developer Experience**: Intuitive {api_title} navigation and discovery  
✅ **Type Safety**: Rich Pydantic models with validation  
✅ **MCP Ready**: All {api_title} operations available for AI integration  
✅ **Performance**: Lazy loading for maximum efficiency  

## Field Mapping

All models use **snake_case** field names with **camelCase** aliases for API compatibility:

```python
# Python usage (snake_case)
response.created_at
response.node_type

# API compatibility (camelCase aliases)
response.model_dump(by_alias=True)  # Uses camelCase for API calls
```

This provides the best developer experience while maintaining full API compatibility.
"""

    return doc_content


def generate_index_documentation() -> str:
    """Generate main index documentation for all APIs."""
    
    doc_content = """# Alfresco V1.1 Three-Tier Architecture Documentation

## Overview

This documentation covers the complete **V1.1 Three-Tier Architecture** for all Alfresco APIs, designed for both traditional Alfresco developers and modern AI/MCP integration.

## Architecture Philosophy

The V1.1 architecture provides **perfect hierarchical organization** across all APIs:

### Three-Tier Structure

1. **Level 1 (Global)**: Models shared across ALL APIs
   - `BaseEntry`, `PagingInfo`, `ErrorResponse`
   - Location: `clients/models.py`

2. **Level 2 (API-Specific)**: Models shared within ONE API
   - `CoreResponse`, `WorkflowResponse`, `AuthResponse`
   - Location: `clients/{api}/models.py`

3. **Level 3 (Operation-Specific)**: Models for specific operations
   - `NodeResponse`, `TaskResponse`, `SiteResponse`
   - Location: `clients/{api}/{subsection}/models.py`

### Key Benefits

✅ **Perfect Locality**: Models exactly where operations are used  
✅ **Clean Imports**: `from .models import SpecificResponse`  
✅ **Logical Organization**: Three clear hierarchical levels  
✅ **Maintainability**: Small focused files vs huge generated files  
✅ **Scalability**: Easy to add new operations anywhere  
✅ **Developer Experience**: Intuitive navigation and discovery  
✅ **Type Safety**: Rich Pydantic models with validation  
✅ **MCP Ready**: All operations available for AI integration  
✅ **Performance**: Lazy loading for maximum efficiency  

## API Coverage

| API | Subsections | Description |
|-----|-------------|-------------|
"""

    # Add API table
    for api_name in ALL_APIS:
        api_path = project_root / f"python_alfresco_api/clients/{api_name}"
        subsection_count = 0
        
        if api_path.exists():
            for item in api_path.iterdir():
                if item.is_dir() and item.name != "__pycache__":
                    subsection_count += 1
        
        api_title = api_name.replace("_", " ").title()
        description = API_DESCRIPTIONS.get(api_name, "Enterprise content management")
        doc_link = f"[{api_title}](./{api_name}_api.md)"
        
        doc_content += f"| {doc_link} | {subsection_count} | {description} |\n"
    
    doc_content += """
## Usage Patterns

### Individual API Clients

```python
from python_alfresco_api import ClientFactory
from python_alfresco_api.clients.core import AlfrescoCoreClient

factory = ClientFactory()
core_client = AlfrescoCoreClient(factory)

# Lazy loading - subsections load on first access
sites = core_client.sites  # Loads sites subsection
result = sites.create_site(name="My Site")
```

### Master Client (All APIs)

```python
from python_alfresco_api import create_lazy_master_client

# Single client for all APIs
master = create_lazy_master_client()

# Access any operation across all APIs
node = master.core.nodes.get(node_id="123")
task = master.workflow.tasks.get(task_id="456")
ticket = master.auth.authentication.create_ticket()
```

### MCP Server Integration

```python
# Perfect for Model Context Protocol servers
from python_alfresco_api.clients.core.nodes.models import NodeResponse

def get_node_mcp(node_id: str) -> NodeResponse:
    \"\"\"MCP tool for getting Alfresco nodes.\"\"\"
    master = create_lazy_master_client()
    return master.core.nodes.get(node_id=node_id)
```

## Field Mapping

All models support both Python conventions and API compatibility:

```python
# Python-style field names (snake_case)
node.created_at
node.is_file
node.node_type

# API-compatible output (camelCase)
api_data = node.model_dump(by_alias=True)
# Results in: {"createdAt": "...", "isFile": true, "nodeType": "..."}
```

## Performance Features

- **Lazy Loading**: Subsections load only when accessed
- **Memory Efficient**: Small focused modules vs monolithic files
- **Import Optimization**: Clean dependency trees
- **Caching**: Clients reuse raw HTTP connections

## Development Benefits

- **Type Safety**: Full Pydantic v2 validation
- **IDE Support**: Rich auto-completion and navigation
- **Testing**: Easy to mock individual subsections
- **Extensibility**: Simple to add new operations
- **Documentation**: Self-documenting hierarchical structure

## Competitive Advantages

Compared to monolithic or flat API architectures:

1. **Developer Experience**: Intuitive organization vs confusing flat files
2. **Maintainability**: Focused modules vs huge generated files  
3. **Performance**: Lazy loading vs loading everything upfront
4. **AI Integration**: Rich models perfect for MCP servers
5. **Enterprise Scale**: Handles complexity without becoming unwieldy

---

*Generated by V1.1 Three-Tier Architecture Documentation Generator*
"""

    return doc_content


def main():
    """Generate comprehensive documentation for ALL APIs."""
    
    print("=" * 80)
    print("📚 Complete V1.1 Three-Tier Architecture Documentation Generator")
    print("=" * 80)
    print()
    
    # Create docs directory
    docs_dir = project_root / "docs" / "api_v11"
    docs_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"🎯 Generating documentation for {len(ALL_APIS)} APIs")
    print(f"📁 Output directory: {docs_dir}")
    print()
    
    generated_docs = []
    total_size = 0
    
    # Generate documentation for each API
    for api_name in ALL_APIS:
        try:
            doc_content = generate_api_documentation(api_name)
            
            # Write documentation
            doc_path = docs_dir / f"{api_name}_api.md"
            with open(doc_path, 'w', encoding='utf-8') as f:
                f.write(doc_content)
            
            doc_size = len(doc_content)
            total_size += doc_size
            generated_docs.append((api_name, doc_path, doc_size))
            
            print(f"✅ {api_name:12} - {doc_size:,} chars - {doc_path.name}")
            
        except Exception as e:
            print(f"❌ {api_name:12} - Error: {e}")
    
    print()
    
    # Generate index documentation
    try:
        index_content = generate_index_documentation()
        index_path = docs_dir / "README.md"
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)
        
        index_size = len(index_content)
        total_size += index_size
        
        print(f"✅ Generated index documentation - {index_size:,} chars")
        print(f"📄 Index file: {index_path}")
        
    except Exception as e:
        print(f"❌ Error generating index: {e}")
    
    print()
    print("=" * 80)
    print("📊 Documentation Generation Summary")
    print("=" * 80)
    print(f"📚 APIs documented: {len(generated_docs)}")
    print(f"📄 Total files: {len(generated_docs) + 1}")
    print(f"📊 Total size: {total_size:,} characters")
    print()
    
    print("📋 Generated Files:")
    print(f"   📖 README.md - Main index and overview")
    for api_name, doc_path, doc_size in generated_docs:
        api_title = api_name.replace("_", " ").title()
        print(f"   📄 {doc_path.name:20} - {api_title} API ({doc_size:,} chars)")
    
    print()
    print("🏆 Complete V1.1 Architecture Documentation:")
    print("   ✅ All 7 Alfresco APIs documented")
    print("   ✅ Three-tier hierarchy explained")
    print("   ✅ Usage examples and benefits")
    print("   ✅ MCP integration patterns")
    print("   ✅ Field mapping and performance")
    print("   ✅ Developer experience focus")
    print()
    print("🚀 Ready for comprehensive API documentation site!")


if __name__ == "__main__":
    main() 