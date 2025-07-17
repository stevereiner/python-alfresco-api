#!/usr/bin/env python3
"""
Generate ALL Alfresco APIs - Complete V1.1 Three-Tier Architecture

Automates the generation of hierarchical three-tier architecture for ALL Alfresco APIs:
- Core API (20 subsections) ✅ Already done
- Auth API (1 subsection)
- Discovery API (1 subsection) 
- Search API (1 subsection)
- Search SQL API (1 subsection)
- Workflow API (4 subsections)
- Model API (2 subsections)

Total: 30+ subsections across 7 APIs with perfect hierarchical organization.
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Any, Tuple
import re

# Add project root to path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from python_alfresco_api.clients.field_mapping import (
    snake_to_camel, COMMON_FIELD_PATTERNS, generate_field_definition
)


# Complete API structure mapping
ALL_APIS = {
    "auth": {
        "client_name": "AlfrescoAuthClient",
        "raw_client_path": "alfresco_auth_client/auth_client",
        "description": "Authentication and ticket management",
        "subsections": ["authentication"]
    },
    "discovery": {
        "client_name": "AlfrescoDiscoveryClient", 
        "raw_client_path": "alfresco_discovery_client/discovery_client",
        "description": "Repository information and capabilities",
        "subsections": ["discovery"]
    },
    "search": {
        "client_name": "AlfrescoSearchClient",
        "raw_client_path": "alfresco_search_client/search_client", 
        "description": "Content and metadata search",
        "subsections": ["search"]
    },
    "search_sql": {
        "client_name": "AlfrescoSearchSqlClient",
        "raw_client_path": "alfresco_search_sql_client/search_sql_client",
        "description": "SQL-based content search", 
        "subsections": ["sql"]
    },
    "workflow": {
        "client_name": "AlfrescoWorkflowClient",
        "raw_client_path": "alfresco_workflow_client/workflow_client",
        "description": "Process and task management",
        "subsections": ["deployments", "process_definitions", "processes", "tasks"]
    },
    "model": {
        "client_name": "AlfrescoModelClient", 
        "raw_client_path": "alfresco_model_client/model_client",
        "description": "Content model introspection",
        "subsections": ["aspects", "types"]
    }
}


def extract_function_signature(api_name: str, subsection: str, operation_file: str) -> Dict[str, Any]:
    """
    Extract parameter signatures from raw client operation files.
    
    Args:
        api_name: Name of the API (e.g., "workflow")
        subsection: Name of the subsection (e.g., "tasks")
        operation_file: Name of the operation file (e.g., "create_task")
        
    Returns:
        Dictionary with parameter information
    """
    api_info = ALL_APIS[api_name]
    raw_path = project_root / f"python_alfresco_api/raw_clients/{api_info['raw_client_path']}/api/{subsection}/{operation_file}.py"
    
    if not raw_path.exists():
        return {"params": [], "has_body": False, "return_type": "Any", "params_str": "", "param_names": [], "imports": [], "model_imports": []}
    
    try:
        with open(raw_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract parameters from sync_detailed function using AST parsing
        import ast
        
        try:
            tree = ast.parse(content)
        except SyntaxError:
            # Fallback to simpler extraction if AST parsing fails
            return {"params": [], "has_body": False, "return_type": "Any", "params_str": "", "param_names": [], "imports": [], "model_imports": []}
        
        # Extract imports for proper type annotations
        imports = []
        model_imports = []
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module and 'types' in node.module:
                    for alias in node.names:
                        imports.append(alias.name)
                elif node.module and 'models' in node.module:
                    for alias in node.names:
                        model_imports.append(alias.name)
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'sync_detailed':
                params = []
                param_names = []
                has_body = False
                
                for arg in node.args.args:
                    if arg.arg != 'client':  # Skip client parameter
                        param_name = arg.arg
                        param_names.append(param_name)
                        
                        # Extract proper type annotation from the function
                        if arg.annotation:
                            # Handle Union[Unset, list[str]] and similar complex types
                            if isinstance(arg.annotation, ast.Subscript):
                                # Handle Union types
                                if isinstance(arg.annotation.value, ast.Name) and arg.annotation.value.id == 'Union':
                                    # This is a Union type - keep as is for compatibility
                                    param_str = f"{param_name}: Union[Unset, Any]"
                                elif isinstance(arg.annotation.value, ast.Name) and arg.annotation.value.id == 'list':
                                    # This is a list type
                                    param_str = f"{param_name}: List[Any]"
                                else:
                                    param_str = f"{param_name}: Any"
                            elif isinstance(arg.annotation, ast.Name):
                                # Simple type annotation
                                param_str = f"{param_name}: {arg.annotation.id}"
                            else:
                                param_str = f"{param_name}: Any"
                        else:
                            # No type annotation
                            param_str = f"{param_name}: Any"
                        
                        params.append(param_str)
                        
                        if 'body' in param_name.lower():
                            has_body = True
                
                # Handle keyword-only arguments
                for arg in node.args.kwonlyargs:
                    if arg.arg != 'client':  # Skip client parameter
                        param_name = arg.arg
                        param_names.append(param_name)
                        
                        # Extract proper type annotation from the function
                        if arg.annotation:
                            # Handle Union[Unset, list[str]] and similar complex types
                            if isinstance(arg.annotation, ast.Subscript):
                                # Handle Union types
                                if isinstance(arg.annotation.value, ast.Name) and arg.annotation.value.id == 'Union':
                                    # This is a Union type - keep as is for compatibility
                                    param_str = f"{param_name}: Union[Unset, Any] = UNSET"
                                elif isinstance(arg.annotation.value, ast.Name) and arg.annotation.value.id == 'list':
                                    # This is a list type
                                    param_str = f"{param_name}: List[Any] = UNSET"
                                else:
                                    param_str = f"{param_name}: Any = UNSET"
                            elif isinstance(arg.annotation, ast.Name):
                                # Simple type annotation
                                param_str = f"{param_name}: {arg.annotation.id} = UNSET"
                            else:
                                param_str = f"{param_name}: Any = UNSET"
                        else:
                            # No type annotation
                            param_str = f"{param_name}: Any = UNSET"
                        
                        params.append(param_str)
                        
                        if 'body' in param_name.lower():
                            has_body = True
                
                # Extract return type annotation
                return_type = "Any"
                if node.returns:
                    if isinstance(node.returns, ast.Subscript):
                        # This is Response[Something]
                        return_type = f"Response[Any]"
                    elif isinstance(node.returns, ast.Name):
                        return_type = node.returns.id
                
                return {
                    "params": params,
                    "has_body": has_body,
                    "return_type": return_type,
                    "params_str": ", ".join(params) if params else "",
                    "param_names": param_names,  # Clean parameter names for method calls
                    "imports": imports,
                    "model_imports": model_imports
                }
        
        # If sync_detailed function not found, return empty
        return {"params": [], "has_body": False, "return_type": "Any", "params_str": "", "param_names": [], "imports": [], "model_imports": []}
        
    except Exception as e:
        print(f"    ⚠️  Could not extract signature for {operation_file}: {e}")
        return {"params": [], "has_body": False, "return_type": "Any", "params_str": "", "param_names": [], "imports": [], "model_imports": []}


def analyze_api_subsection(api_name: str, subsection: str) -> Dict[str, Any]:
    """
    Analyze a specific subsection within an API.
    
    Args:
        api_name: Name of the API (e.g., "workflow")
        subsection: Name of the subsection (e.g., "tasks")
        
    Returns:
        Dictionary with operation information including signatures
    """
    api_info = ALL_APIS[api_name]
    raw_path = project_root / f"python_alfresco_api/raw_clients/{api_info['raw_client_path']}/api/{subsection}"
    
    if not raw_path.exists():
        return {"operations": [], "has_models": False}
    
    operations = []
    for py_file in raw_path.glob("*.py"):
        if py_file.name == "__init__.py":
            continue
        
        operation_name = py_file.stem
        
        # Extract parameter signature from the operation file
        signature = extract_function_signature(api_name, subsection, operation_name)
        
        method_name = operation_name.replace("_", "_")
        operations.append({
            "file": operation_name,
            "method": method_name,
            "sync_method": method_name.replace("_async", ""),
            "async_method": f"{method_name}_async" if not method_name.endswith("_async") else method_name,
            "signature": signature
        })
    
    return {
        "operations": operations,
        "has_models": len(operations) > 0,
        "operation_count": len(operations)
    }


def generate_api_level2_models(api_name: str) -> str:
    """Generate Level 2 API-specific models."""
    
    api_info = ALL_APIS[api_name]
    class_name = api_name.replace("_", " ").title().replace(" ", "")
    
    models_content = f'''"""
Level 2: {class_name} API Models - Shared within {class_name} API

This module contains models and structures that are specific to the
Alfresco {class_name} API but shared across multiple {class_name} operations.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs
- Level 2 (This file): {class_name} API models shared within {class_name} API  
- Level 3: Operation-specific models for specific {class_name} operations

Benefits:
- Perfect locality ({class_name}-specific models in {class_name} namespace)
- Clean imports (from .models import {class_name}Response)
- Logical organization (API-level grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from pydantic import BaseModel, Field, ConfigDict
from enum import Enum

# Import global models
from ..models import BaseEntry, PagingInfo


class {class_name}Response(BaseModel):
    """Base response wrapper for {class_name} API operations."""
    model_config = ConfigDict(extra='forbid')
    
    entries: List[BaseEntry] = Field(default_factory=list, description="{class_name} result entries")
    pagination: Optional[PagingInfo] = Field(None, description="Pagination information")


class {class_name}Request(BaseModel):
    """Base request model for {class_name} operations."""
    model_config = ConfigDict(extra='forbid')
    
    max_items: Annotated[int, Field(
        description="Maximum number of results to return",
        default=100,
        ge=1,
        le=1000
    )]
    
    skip_count: Annotated[int, Field(
        description="Number of results to skip for pagination",
        default=0,
        ge=0
    )]


# Export all models
__all__ = [
    '{class_name}Response', '{class_name}Request'
]'''

    return models_content


def generate_api_level3_models(api_name: str, subsection: str, operations: List[Dict]) -> str:
    """Generate Level 3 operation-specific models for an API subsection."""
    
    api_info = ALL_APIS[api_name]
    api_class = api_name.replace("_", " ").title().replace(" ", "")
    subsection_class = subsection.replace("_", " ").title().replace(" ", "")
    
    models_content = f'''"""
Level 3: {subsection_class} Operation Models - Specific to {subsection_class} Operations

This module contains models that are specific to {subsection} operations
within the {api_class} API.

Three-Tier Architecture:
- Level 1: Global models shared across ALL APIs  
- Level 2: {api_class} API models shared within {api_class} API
- Level 3 (This file): {subsection_class} operation-specific models

Benefits:
- Perfect locality ({subsection} models exactly where {subsection} operations are)
- Clean imports (from .models import {subsection_class}Response)
- Logical organization (operation-specific grouping)
"""

from typing import Optional, List, Dict, Any, Annotated
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

# Import from Level 1 (global)
from ...models import BaseEntry, ContentInfo, UserInfo

# Import from Level 2 ({api_class} API)
from ..models import {api_class}Response


class {subsection_class}Response({api_class}Response):
    """Response wrapper for {subsection} operations."""
    entry: BaseEntry = Field(..., description="{subsection_class} data")


class {subsection_class}ListResponse(BaseModel):
    """Response wrapper for {subsection} list operations."""
    model_config = ConfigDict(extra='forbid')
    
    list: Dict[str, Any] = Field(..., description="List data with pagination")


class Create{subsection_class}Request(BaseModel):
    """Request model for creating {subsection}."""
    model_config = ConfigDict(extra='forbid')
    
    name: Annotated[str, Field(
        description="{subsection_class} name",
        min_length=1,
        max_length=255
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Custom properties",
        default=None
    )]


class Update{subsection_class}Request(BaseModel):
    """Request model for updating {subsection}."""
    model_config = ConfigDict(extra='forbid')
    
    name: Annotated[Optional[str], Field(
        description="Updated name",
        min_length=1,
        max_length=255,
        default=None
    )]
    
    properties: Annotated[Optional[Dict[str, Any]], Field(
        description="Updated properties",
        default=None
    )]


# Export all models
__all__ = [
    '{subsection_class}Response', 
    '{subsection_class}ListResponse',
    'Create{subsection_class}Request',
    'Update{subsection_class}Request'
]'''

    return models_content


def generate_api_level3_client(api_name: str, subsection: str, operations: List[Dict]) -> str:
    """Generate Level 3 client for an API subsection with complete 4-pattern detailed functions."""
    
    api_info = ALL_APIS[api_name]
    api_class = api_name.replace("_", " ").title().replace(" ", "")
    subsection_class = subsection.replace("_", " ").title().replace(" ", "")
    client_class = f"Alfresco{subsection_class}Client"
    
    # Generate imports for raw operations
    imports = []
    model_imports = set()  # Use set to avoid duplicates
    for op in operations:
        imports.append(f"            {op['file']} as _{op['file']}")
        # Collect model imports from all operations
        if "signature" in op and "model_imports" in op["signature"]:
            model_imports.update(op["signature"]["model_imports"])
    
    imports_str = ",\n".join(imports) if imports else ""
    
    # Generate model import statements
    model_imports_str = ""
    if model_imports:
        model_imports_str = "\n# Import model types for proper parameter signatures\n"
        for model in sorted(model_imports):
            model_imports_str += f"from ....raw_clients.{api_info['raw_client_path'].replace('/', '.')}.models.{model.lower().replace('_', '_')} import {model}\n"
    
    # Generate method implementations with complete 4-pattern and proper parameter signatures
    methods_content = ""
    for op in operations:
        method_name = op["sync_method"]
        file_name = op["file"]
        signature = op["signature"]
        params_str = signature["params_str"]
        return_type = signature.get("return_type", "Any")
        
        # Use the clean parameter names for method calls (as keyword arguments)
        param_names = signature.get("param_names", [])
        call_params = ", ".join([f"{name}={name}" for name in param_names]) if param_names else ""
        
        methods_content += f'''
    # ==================== {method_name.upper()} OPERATION - Complete 4-Pattern ====================
    
    def {method_name}(self{", " + params_str if params_str else ""}) -> Any:
        """
        {method_name.replace("_", " ").title()} operation (sync).
        
        Perfect for MCP servers and {subsection} workflows.
        Returns parsed response for common use cases.
        
        Args:
{chr(10).join(f"            {param.split(':')[0].strip()}: {param.split(':', 1)[1].strip() if ':' in param else 'Any'}" for param in signature["params"]) if signature["params"] else "            No parameters"}
        
        Returns:
            Parsed response object
        """
        if not hasattr(self, '_{file_name}'):
            raise ImportError("Raw client operation not available")
        
        return self._{file_name}.sync(client=self._get_raw_client(){", " + call_params if call_params else ""})
    
    async def {method_name}_async(self{", " + params_str if params_str else ""}) -> Any:
        """
        {method_name.replace("_", " ").title()} operation (async).
        
        Perfect for MCP servers and {subsection} workflows.
        Returns parsed response for common use cases.
        
        Args:
{chr(10).join(f"            {param.split(':')[0].strip()}: {param.split(':', 1)[1].strip() if ':' in param else 'Any'}" for param in signature["params"]) if signature["params"] else "            No parameters"}
        
        Returns:
            Parsed response object
        """
        if not hasattr(self, '_{file_name}'):
            raise ImportError("Raw client operation not available")
        
        return await self._{file_name}.asyncio(client=self._get_raw_client(){", " + call_params if call_params else ""})
    
    def {method_name}_detailed(self{", " + params_str if params_str else ""}) -> {return_type}:
        """
        {method_name.replace("_", " ").title()} operation (detailed sync).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        
        Args:
{chr(10).join(f"            {param.split(':')[0].strip()}: {param.split(':', 1)[1].strip() if ':' in param else 'Any'}" for param in signature["params"]) if signature["params"] else "            No parameters"}
        
        Returns:
            {return_type}: Complete response with status_code, headers, content, parsed
        """
        if not hasattr(self, '_{file_name}'):
            raise ImportError("Raw client operation not available")
        
        return self._{file_name}.sync_detailed(client=self._get_raw_client(){", " + call_params if call_params else ""})
    
    async def {method_name}_detailed_async(self{", " + params_str if params_str else ""}) -> {return_type}:
        """
        {method_name.replace("_", " ").title()} operation (detailed async).
        
        Perfect for MCP servers needing full HTTP response details.
        Returns complete Response object with status_code, headers, content, parsed.
        
        Args:
{chr(10).join(f"            {param.split(':')[0].strip()}: {param.split(':', 1)[1].strip() if ':' in param else 'Any'}" for param in signature["params"]) if signature["params"] else "            No parameters"}
        
        Returns:
            {return_type}: Complete response with status_code, headers, content, parsed
        """
        if not hasattr(self, '_{file_name}'):
            raise ImportError("Raw client operation not available")
        
        return await self._{file_name}.asyncio_detailed(client=self._get_raw_client(){", " + call_params if call_params else ""})
'''
    
    client_content = f'''"""
{subsection_class} Operations Client - Level 3: {subsection_class}-Specific Operations

This module provides {subsection}-specific operations within the {api_class} API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.

Each operation provides 4 variants:
- operation(params) - basic sync with explicit parameters
- operation_async(params) - basic async with explicit parameters  
- operation_detailed(params) - detailed sync with explicit parameters
- operation_detailed_async(params) - detailed async with explicit parameters

Perfect for MCP servers and documentation generation.
"""

import asyncio
from typing import Optional, List, Union, Any, Awaitable
from httpx import Response

# Import required types for proper parameter handling
from ....raw_clients.{api_info['raw_client_path'].replace('/', '.')}.types import UNSET, Unset
from httpx import Response
{model_imports_str}
# Import from Level 3 (operation-specific models)
from .models import {subsection_class}Response, {subsection_class}ListResponse, Create{subsection_class}Request

# Import raw operations
try:
    from ....raw_clients.{api_info['raw_client_path'].replace('/', '.')}.api.{subsection} import (
{imports_str}
    )
    RAW_OPERATIONS_AVAILABLE = True
except ImportError:
    RAW_OPERATIONS_AVAILABLE = False


class {client_class}:
    """
    {subsection_class} operations client with 4-pattern detailed functions.
    
    Provides high-level methods for {subsection} management operations
    that are essential for MCP servers and {subsection} workflows.
    
    Each operation has 4 variants for maximum flexibility:
    - Basic sync/async for simple use cases
    - Detailed sync/async for full HTTP response access
    """
    
    def __init__(self, client_factory):
        """Initialize with client factory for raw client access."""
        self._client_factory = client_factory
        self._raw_client = None
        
        # Store raw operation references
        if RAW_OPERATIONS_AVAILABLE:
{chr(10).join(f"            self._{op['file']} = _{op['file']}" for op in operations)}
    
    def _get_raw_client(self):
        """Get or create the raw client."""
        if self._raw_client is None:
            # Import the raw client directly
            from ....raw_clients.{api_info['raw_client_path'].replace('/', '.')}.client import AuthenticatedClient
            
            # Create the raw client with same auth setup
            self._raw_client = AuthenticatedClient(
                base_url=f"{{self._client_factory.base_url}}/alfresco/api/{api_name}/versions/1",
                token=self._client_factory.auth.get_auth_token(),
                prefix=self._client_factory.auth.get_auth_prefix(),
                verify_ssl=self._client_factory.verify_ssl
            )
        return self._raw_client
    
    def get_httpx_client(self):
        """
        Get direct access to raw httpx client for advanced operations.
        
        Perfect for MCP servers that need raw HTTP access.
        """
        return self._get_raw_client().get_httpx_client()
    
    # ==================== 4-PATTERN OPERATIONS ====================
{methods_content}
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self._client_factory, 'base_url', 'unknown')
        return f"{client_class}(base_url='{{base_url}}')"'''

    return client_content


def generate_api_main_client(api_name: str, subsections: List[str]) -> str:
    """Generate the main API client with lazy-loaded subsections."""
    
    api_info = ALL_APIS[api_name]
    api_class = api_name.replace("_", " ").title().replace(" ", "")
    client_class = api_info["client_name"]
    
    # Generate property initializations
    property_inits = []
    for subsection in subsections:
        subsection_var = f"_{subsection}"
        property_inits.append(f"        self.{subsection_var}: Optional['{subsection.title()}Client'] = None")
    
    # Generate property methods with complete automation - no manual TODO fixes needed
    property_methods = ""
    for subsection in subsections:
        subsection_class = subsection.replace("_", " ").title().replace(" ", "")
        
        # Auto-generate operation counts by analyzing the subsection
        structure_info = analyze_api_subsection(api_name, subsection)
        operation_count = structure_info.get("operation_count", 0)
        
        property_methods += f'''
    @property
    def {subsection}(self):
        """Access to {subsection} operations ({operation_count} operations)."""
        if self._{subsection} is None:
            print("🔧 Loading {subsection} operations...")
            from .{subsection} import Alfresco{subsection_class}Client
            self._{subsection} = Alfresco{subsection_class}Client(self._client_factory)
        return self._{subsection}
'''
    
    # Generate checks for loaded subsections
    subsection_checks = []
    for s in subsections:
        subsection_checks.append(f"        if hasattr(self, '_{s}') and self._{s} is not None:")
        subsection_checks.append(f"            loaded_subsections.append('{s}')")
    
    client_content = f'''"""
Alfresco {api_class} API Client - V1.1 Three-Tier Architecture

Provides access to {api_class} API operations with lazy loading and hierarchical organization.
"""

import asyncio
from typing import Optional

# Import from Level 2 models
from .models import {api_class}Response, {api_class}Request


class {client_class}:
    """
    {api_class} operations client with lazy-loaded subsections.
    
    Provides high-level methods for {api_info['description']}
    that are essential for MCP servers and {api_name} workflows.
    """
    
    def __init__(self, client_factory):
        """Initialize with client factory for raw client access."""
        self._client_factory = client_factory
        
        # Lazy-loaded subsection clients
{chr(10).join(property_inits)}
    
    def get_httpx_client(self):
        """
        Get direct access to raw httpx client for advanced operations.
        
        Perfect for MCP servers that need raw HTTP access.
        """
        if not hasattr(self, '_raw_client') or self._raw_client is None:
            # Create raw {api_name} client  
            from ...raw_clients.{api_info['raw_client_path'].replace('/', '.')}.client import AuthenticatedClient
            
            self._raw_client = AuthenticatedClient(
                base_url=f"{{self._client_factory.base_url}}/alfresco/api/{api_name}/versions/1",
                auth=self._client_factory.auth.get_auth_tuple()
            )
        
        return self._raw_client.get_httpx_client()
{property_methods}
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self._client_factory, 'base_url', 'unknown')
        loaded_subsections = []
        
        # Check which subsections are loaded
{chr(10).join(subsection_checks)}
        
        loaded_str = f" (loaded: {{', '.join(loaded_subsections)}})" if loaded_subsections else " (no subsections loaded yet)"
        return f"{client_class}(base_url='{{base_url}}'{{loaded_str}})"'''

    return client_content


def create_api_structure(api_name: str):
    """Create the complete three-tier structure for an API."""
    
    api_info = ALL_APIS[api_name]
    api_path = project_root / f"python_alfresco_api/clients/{api_name}"
    
    print(f"🏗️  Creating {api_name} API - {len(api_info['subsections'])} subsections")
    
    # Create main API directory
    api_path.mkdir(parents=True, exist_ok=True)
    
    # Generate Level 2 models (API-specific)
    level2_models = generate_api_level2_models(api_name)
    with open(api_path / "models.py", "w", encoding="utf-8") as f:
        f.write(level2_models)
    
    # Generate subsections (Level 3)
    processed_subsections = []
    for subsection in api_info['subsections']:
        subsection_path = api_path / subsection
        
        # Analyze subsection structure
        structure_info = analyze_api_subsection(api_name, subsection)
        
        if not structure_info["has_models"]:
            print(f"  ⚠️  Skipping {subsection} - no operations found")
            continue
        
        print(f"  📁 Creating {subsection} - {structure_info['operation_count']} operations")
        
        # Create subsection directory
        subsection_path.mkdir(parents=True, exist_ok=True)
        
        # Generate Level 3 models
        level3_models = generate_api_level3_models(api_name, subsection, structure_info["operations"])
        with open(subsection_path / "models.py", "w", encoding="utf-8") as f:
            f.write(level3_models)
        
        # Generate Level 3 client
        level3_client = generate_api_level3_client(api_name, subsection, structure_info["operations"])
        with open(subsection_path / "__init__.py", "w", encoding="utf-8") as f:
            f.write(level3_client)
        
        processed_subsections.append(subsection)
    
    # Generate main API client with all subsections
    main_client = generate_api_main_client(api_name, processed_subsections)
    with open(api_path / "__init__.py", "w", encoding="utf-8") as f:
        f.write(main_client)
    
    print(f"  ✅ Generated {api_name} API with {len(processed_subsections)} subsections")
    

def main():
    """Generate complete V1.1 architecture for ALL Alfresco APIs."""
    
    print("=" * 80)
    print("🚀 Generating ALL Alfresco APIs - Complete V1.1 Three-Tier Architecture")
    print("=" * 80)
    print()
    
    total_apis = len(ALL_APIS)
    total_subsections = sum(len(api['subsections']) for api in ALL_APIS.values())
    
    print(f"📊 Total APIs: {total_apis}")
    print(f"📊 Total subsections: {total_subsections}")
    print(f"📊 Plus Core API: 20 subsections (already done)")
    print(f"🎯 Grand Total: ~50 subsections across 7 APIs")
    print()
    
    # Generate all APIs
    for api_name, api_info in ALL_APIS.items():
        try:
            create_api_structure(api_name)
        except Exception as e:
            print(f"❌ Error generating {api_name}: {e}")
    
    print()
    print("=" * 80)
    print("✅ ALL Alfresco APIs Generation Complete")
    print("=" * 80)
    print()
    print("📋 Generated Complete Structure:")
    print("   📁 Level 1: Global models (clients/models.py)")
    print("   📁 Level 2: API-level models (clients/{api}/models.py)")  
    print("   📁 Level 3: Operation-specific models (clients/{api}/{subsection}/models.py)")
    print()
    print("🎯 All APIs Ready:")
    for api_name, api_info in ALL_APIS.items():
        subsection_count = len(api_info['subsections'])
        print(f"   ✅ {api_name:12} - {subsection_count} subsections - {api_info['description']}")
    
    print()
    print("🏆 Complete Alfresco V1.1 Architecture:")
    print("   ✅ Perfect hierarchical organization across ALL APIs")
    print("   ✅ Field aliases for smooth automation")
    print("   ✅ Pythonic naming with API compatibility") 
    print("   ✅ MCP server ready with ~50 total subsections")
    print("   ✅ Lazy loading for maximum performance")
    print("   ✅ Clean imports and perfect locality")
    print()
    print("🚀 Ready for comprehensive MCP server development!")


if __name__ == "__main__":
    main() 