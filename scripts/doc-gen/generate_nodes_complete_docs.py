#!/usr/bin/env python3
"""
Generate Complete Nodes Documentation

This script generates comprehensive documentation for the nodes subsection
to demonstrate the rich field details and proper API documentation.
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


def extract_detailed_field_info(class_node: ast.ClassDef) -> Dict[str, Any]:
    """Extract detailed Pydantic field information from AST node."""
    
    fields = []
    
    for item in class_node.body:
        if isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name):
            field_name = item.target.id
            field_info = {
                "name": field_name,
                "type": "Any",
                "description": None,
                "examples": None,
                "default": None,
                "alias": None,
                "constraints": []
            }
            
            # Extract type annotation
            if item.annotation:
                if isinstance(item.annotation, ast.Subscript):
                    # Handle Annotated[Type, Field(...)]
                    if isinstance(item.annotation.value, ast.Name) and item.annotation.value.id == "Annotated":
                        # Get the base type
                        if isinstance(item.annotation.slice, ast.Tuple) and item.annotation.slice.elts:
                            first_elem = item.annotation.slice.elts[0]
                            field_info["type"] = ast.unparse(first_elem)
                            
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
                                                elif isinstance(ex, ast.List):
                                                    # Handle nested lists
                                                    nested_examples = []
                                                    for nested_ex in ex.elts:
                                                        if isinstance(nested_ex, ast.Constant):
                                                            nested_examples.append(nested_ex.value)
                                                    examples.append(nested_examples)
                                            field_info["examples"] = examples
                                        elif keyword.arg == "default":
                                            if isinstance(keyword.value, ast.Constant):
                                                field_info["default"] = keyword.value.value
                                            else:
                                                field_info["default"] = ast.unparse(keyword.value)
                                        elif keyword.arg in ["min_length", "max_length", "pattern"]:
                                            if isinstance(keyword.value, ast.Constant):
                                                field_info["constraints"].append(f"{keyword.arg}={keyword.value.value}")
                else:
                    # Simple type annotation
                    field_info["type"] = ast.unparse(item.annotation)
            
            fields.append(field_info)
    
    return {
        "name": class_node.name,
        "docstring": ast.get_docstring(class_node) or "",
        "fields": fields
    }


def generate_rich_models_documentation() -> str:
    """Generate detailed models documentation for nodes."""
    
    models_path = project_root / "python_alfresco_api/clients/core/nodes/models.py"
    
    if not models_path.exists():
        return "❌ Nodes models file not found"
    
    try:
        with open(models_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        
        models = []
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                model_info = extract_detailed_field_info(node)
                models.append(model_info)
    
    except Exception as e:
        return f"❌ Error analyzing models: {e}"
    
    doc = """# Nodes Models Documentation

## Overview

Level 3 models specific to nodes operations within the Core API - the most comprehensive model set in the entire python-alfresco-api package.

## Architecture

Part of the three-tier V1.1 hierarchical architecture:
- **Level 1**: Global models shared across ALL APIs
- **Level 2**: Core API models shared within Core API  
- **Level 3 (This file)**: Nodes operation-specific models

## Location

```
python_alfresco_api/clients/core/nodes/models.py
```

## Models

"""
    
    for model in models:
        doc += f"### {model['name']}\n\n"
        if model["docstring"]:
            doc += f"*{model['docstring']}*\n\n"
        
        if model["fields"]:
            doc += "**Fields:**\n\n"
            for field in model["fields"]:
                field_name = field["name"]
                field_type = field["type"]
                
                # Build field header
                field_header = f"**`{field_name}`** (`{field_type}`)"
                
                # Add alias if present
                if field["alias"]:
                    field_header += f" *(alias: `{field['alias']}`)*"
                
                # Add default if present
                if field["default"] is not None:
                    field_header += f" *(default: `{field['default']}`)*"
                
                doc += f"- {field_header}"
                
                # Add description
                if field["description"]:
                    doc += f": {field['description']}"
                
                doc += "\n"
                
                # Add examples if present
                if field["examples"]:
                    doc += f"  - **Examples**: {field['examples']}\n"
                
                # Add constraints if present
                if field["constraints"]:
                    doc += f"  - **Constraints**: {', '.join(field['constraints'])}\n"
            
            doc += "\n"
        
        doc += "---\n\n"
    
    doc += """## Usage Examples

### Import Models

```python
from python_alfresco_api.clients.core.nodes.models import (
    Node, NodeResponse, NodeListResponse,
    CreateNodeRequest, UpdateNodeRequest,
    CopyNodeRequest, MoveNodeRequest
)
```

### Basic Usage

```python
# Create a new node
create_request = CreateNodeRequest(
    name="My Document.pdf",
    node_type=NodeType.CONTENT,
    properties={
        "cm:title": "Important Document",
        "cm:description": "This is a critical business document"
    }
)

# Update node metadata
update_request = UpdateNodeRequest(
    name="Renamed Document.pdf",
    properties={
        "cm:title": "Updated Document Title"
    }
)

# Copy node to another location
copy_request = CopyNodeRequest(
    target_parent_id="target-folder-id",
    name="Copy of Document.pdf"
)
```

### Working with Rich Node Objects

```python
# Get a node (returns NodeResponse)
node_response = nodes_client.get("node-id")
node = node_response.entry

# Access rich metadata
print(f"Node name: {node.name}")
print(f"Created: {node.created_at}")
print(f"Modified: {node.modified_at}")
print(f"Size: {node.content.size_in_bytes if node.content else 'N/A'}")
print(f"MIME type: {node.content.mime_type if node.content else 'N/A'}")
print(f"Created by: {node.created_by_user.display_name if node.created_by_user else 'Unknown'}")

# Access custom properties
if node.properties:
    title = node.properties.get("cm:title")
    description = node.properties.get("cm:description")
    print(f"Title: {title}")
    print(f"Description: {description}")
```

## Related Documentation

- [Nodes API Operations](nodes-api.md)
- [Core API Overview](../core-doc.md)
- [Global Models](../../clients_doc.md)
"""
    
    return doc


def generate_rich_api_documentation() -> str:
    """Generate detailed API documentation for nodes."""
    
    nodes_path = project_root / "python_alfresco_api/clients/core/nodes/nodes.py"
    
    if not nodes_path.exists():
        return "❌ Nodes API file not found"
    
    try:
        with open(nodes_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        
        methods = []
        class_name = "NodesOperations"
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_name = node.name
                
                for item in node.body:
                    if isinstance(item, ast.FunctionDef) and not item.name.startswith('_'):
                        method_info = {
                            "name": item.name,
                            "docstring": ast.get_docstring(item) or "",
                            "args": [],
                            "is_async": False
                        }
                        
                        # Extract arguments
                        for arg in item.args.args:
                            if arg.arg != 'self':
                                arg_info = {"name": arg.arg, "type": None}
                                if arg.annotation:
                                    arg_info["type"] = ast.unparse(arg.annotation)
                                method_info["args"].append(arg_info)
                        
                        methods.append(method_info)
    
    except Exception as e:
        return f"❌ Error analyzing API: {e}"
    
    doc = """# Nodes API Operations

## Overview

Complete file and folder management with CRUD operations - the most comprehensive API in the python-alfresco-api package.

## Architecture

Part of the three-tier V1.1 hierarchical architecture:
- **Level 3**: Specific nodes operation implementations
- **Level 2**: Core API-level functionality
- **Level 1**: Global client infrastructure

## Location

```
python_alfresco_api/clients/core/nodes/nodes.py
```

## Client Class

### NodesOperations

Main client class for nodes operations with rich functionality.

## Operations

### Sync Operations

Perfect for scripts, MCP servers, and command-line tools.

"""
    
    # Filter and group methods
    main_methods = [m for m in methods if not m["name"].endswith("_async")]
    
    for method in main_methods:
        doc += f"#### {method['name']}\n\n"
        
        if method["docstring"]:
            doc += f"{method['docstring']}\n\n"
        
        # Build method signature
        signature_parts = []
        for arg in method["args"]:
            arg_str = arg["name"]
            if arg["type"]:
                arg_str += f": {arg['type']}"
            signature_parts.append(arg_str)
        
        signature = f"def {method['name']}(self"
        if signature_parts:
            signature += f", {', '.join(signature_parts)}"
        signature += ")"
        
        doc += f"```python\n{signature}\n```\n\n"
    
    doc += """## Usage Examples

### Basic File Operations

```python
from python_alfresco_api import ClientFactory
from python_alfresco_api.clients.core.nodes.models import CreateNodeRequest, NodeType

# Setup
factory = ClientFactory(base_url="http://localhost:8080")
core_client = factory.create_core_client()
nodes = core_client.nodes

# Create a folder
folder_request = CreateNodeRequest(
    name="My Project Folder",
    node_type=NodeType.FOLDER,
    properties={
        "cm:title": "Important Project Files",
        "cm:description": "Contains all project documentation"
    }
)
folder_response = nodes.create(parent_id="-my-", request=folder_request)
folder_id = folder_response.entry.id

# Create a file
file_request = CreateNodeRequest(
    name="project-plan.docx",
    node_type=NodeType.CONTENT,
    properties={
        "cm:title": "Project Plan",
        "cm:author": "Project Manager"
    }
)
file_response = nodes.create(parent_id=folder_id, request=file_request)
file_id = file_response.entry.id

# Get file details
file_details = nodes.get(file_id)
print(f"File: {file_details.entry.name}")
print(f"Size: {file_details.entry.content.size_in_bytes}")
print(f"MIME: {file_details.entry.content.mime_type}")
```

### Advanced Operations

```python
# List folder contents
children = nodes.get_children(folder_id)
for child in children.list.entries:
    print(f"- {child.entry.name} ({child.entry.node_type})")

# Copy file to another location
copy_request = CopyNodeRequest(
    target_parent_id="target-folder-id",
    name="Copy of project-plan.docx"
)
copied_file = nodes.copy(file_id, copy_request)

# Move file
move_request = MoveNodeRequest(
    target_parent_id="archive-folder-id",
    name="archived-project-plan.docx"
)
moved_file = nodes.move(file_id, move_request)
```

## Related Documentation

- [Nodes Models](nodes-models.md) - Rich model definitions
- [Core API Overview](../core-doc.md) - Level 2 Core API
- [Global Models](../../clients_doc.md) - Level 1 shared models
"""
    
    return doc


def main():
    """Generate complete documentation for nodes subsection."""
    
    print("=" * 80)
    print("📚 Generate Complete Nodes Documentation")
    print("=" * 80)
    print()
    
    # Generate models documentation
    print("📝 Generating detailed models documentation...")
    models_doc = generate_rich_models_documentation()
    models_file = project_root / "docs/core/nodes/nodes-models-rich.md"
    models_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(models_file, 'w', encoding='utf-8') as f:
        f.write(models_doc)
    
    print("✅ Generated nodes-models-rich.md")
    
    # Generate API documentation
    print("📝 Generating detailed API documentation...")
    api_doc = generate_rich_api_documentation()
    api_file = project_root / "docs/core/nodes/nodes-api-rich.md"
    
    with open(api_file, 'w', encoding='utf-8') as f:
        f.write(api_doc)
    
    print("✅ Generated nodes-api-rich.md")
    
    print("\n🎉 Generated complete nodes documentation!")
    print("   - Rich model documentation with all field details")
    print("   - Complete API documentation with method signatures")
    print("   - Detailed examples and usage patterns")


if __name__ == "__main__":
    main() 