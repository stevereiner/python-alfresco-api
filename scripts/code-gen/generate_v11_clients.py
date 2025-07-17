#!/usr/bin/env python3
"""
Generate V1.1 Style Clients from Raw Clients

Automatically creates clean, composition-based wrapper clients with:
- Composition instead of inheritance (self._raw_client)
- Pydantic models instead of attrs models
- Clean method naming (no sync/asyncio confusion)
- Pre-imported raw functions (hidden complexity)
- MCP-optimized interfaces
"""

import os
from pathlib import Path
from typing import Dict, List, Set
import ast
import inspect
import importlib.util


class V11ClientGenerator:
    """Generate v1.1 style clients from raw client analysis."""
    
    def __init__(self, raw_clients_path: str, output_path: str):
        self.raw_clients_path = Path(raw_clients_path)
        self.output_path = Path(output_path)
        self.client_configs = {}
    
    def analyze_raw_client(self, client_name: str) -> Dict:
        """Analyze a raw client to extract API operations."""
        client_path = self.raw_clients_path / f"alfresco_{client_name}_client"
        api_path = client_path / f"{client_name}_client" / "api"
        
        if not api_path.exists():
            return {}
        
        operations = {}
        
        # Scan API directories for operations
        for api_dir in api_path.iterdir():
            if api_dir.is_dir() and api_dir.name != "__pycache__":
                category = api_dir.name
                operations[category] = []
                
                # Scan for operation files
                for op_file in api_dir.glob("*.py"):
                    if op_file.name != "__init__.py":
                        op_name = op_file.stem
                        operations[category].append(op_name)
        
        return {
            "name": client_name,
            "path": client_path,
            "operations": operations,
            "models_available": self._check_models(client_path)
        }
    
    def _extract_function_signature(self, client_name: str, category: str, operation: str) -> Dict:
        """Extract function signature from raw client operation."""
        try:
            # Path to the operation file
            op_path = self.raw_clients_path / f"alfresco_{client_name}_client" / f"{client_name}_client" / "api" / category / f"{operation}.py"
            
            if not op_path.exists():
                return {"params": [], "has_body": False}
            
            # Parse the file to extract sync_detailed function signature
            with open(op_path, 'r') as f:
                content = f.read()
            
            # Extract parameters from sync_detailed function
            params = []
            has_body = False
            
            # Simple regex to find sync_detailed function signature
            import re
            match = re.search(r'def sync_detailed\(\s*([^)]+)\s*\)', content, re.DOTALL)
            if match:
                params_str = match.group(1)
                # Parse parameters (simplified - could be more robust)
                for param in params_str.split(','):
                    param = param.strip()
                    if param and not param.startswith('*') and 'client' not in param:
                        if ':' in param:
                            param_name = param.split(':')[0].strip()
                            if param_name not in ['client']:
                                params.append(param)
                                if 'body' in param_name.lower():
                                    has_body = True
            
            return {"params": params, "has_body": has_body}
            
        except Exception as e:
            print(f"Warning: Could not extract signature for {operation}: {e}")
            return {"params": [], "has_body": False}
    
    def _check_models(self, client_path: Path) -> List[str]:
        """Check what models are available for this client."""
        models_path = client_path / f"{client_path.name.replace('alfresco_', '').replace('_client', '_client')}" / "models"
        
        if not models_path.exists():
            return []
        
        models = []
        for model_file in models_path.glob("*.py"):
            if model_file.name != "__init__.py":
                models.append(model_file.stem)
        
        return models
    
    def generate_client_config(self, client_name: str) -> Dict:
        """Generate configuration for a v1.1 client."""
        
        # MCP-focused operation mappings
        mcp_operations = {
            "core": {
                "essential": [
                    "get_node", "create_node", "update_node", "delete_node",
                    "list_node_children", "update_node_content", "get_node_content",
                    "lock_node", "unlock_node", "find_nodes", "copy_node",
                    "move_node", "create_association", "delete_association",
                    "get_node_associations", "create_comment", "delete_comment",
                    "list_comments", "create_favorite", "delete_favorite",
                    "get_favorite", "create_rating", "delete_rating",
                    "get_rating", "create_tag_for_node", "delete_tag_from_node",
                    "list_tags_for_node", "create_rendition", "get_rendition",
                    "list_renditions", "create_shared_link", "delete_shared_link",
                    "get_shared_link", "create_site", "delete_site",
                    "get_site", "list_sites", "create_site_membership",
                    "delete_site_membership", "get_site_membership"
                ],
                "categories": {
                    "nodes": ["get_node", "create_node", "update_node", "delete_node"],
                    "content": ["update_node_content", "get_node_content"],
                    "navigation": ["list_node_children", "find_nodes"],
                    "locking": ["lock_node", "unlock_node"]
                }
            },
            "search": {
                "essential": ["search"],
                "categories": {
                    "search": ["search"]
                }
            },
            "discovery": {
                "essential": ["get_repository_information"],
                "categories": {
                    "discovery": ["get_repository_information"]
                }
            },
            "auth": {
                "essential": ["create_ticket", "validate_ticket", "delete_ticket"],
                "categories": {
                    "auth": ["create_ticket", "validate_ticket", "delete_ticket"]
                }
            },
            "workflow": {
                "essential": ["get_processes", "create_process", "get_tasks"],
                "categories": {
                    "workflow": ["get_processes", "create_process", "get_tasks"]
                }
            },
            "model": {
                "essential": ["get_types", "get_aspects", "get_constraints"],
                "categories": {
                    "model": ["get_types", "get_aspects", "get_constraints"]
                }
            },
            "search_sql": {
                "essential": ["search_sql"],
                "categories": {
                    "search_sql": ["search_sql"]
                }
            }
        }
        
        return mcp_operations.get(client_name, {})
    
    def generate_v11_client(self, client_name: str) -> str:
        """Generate a complete v1.1 client."""
        config = self.generate_client_config(client_name)
        analysis = self.analyze_raw_client(client_name)
        
        # Template for v1.1 client
        template = f'''#!/usr/bin/env python3
"""
Alfresco{client_name.title()}Client v1.1 - Clean, MCP-Optimized Design

Generated automatically from raw client analysis.

BREAKING CHANGES from v1.0:
- Clean method naming: get_node(), get_node_async(), get_node_detailed()
- Pre-imported raw functions (hidden complexity)
- Composition instead of inheritance (self._raw_client)
- Pydantic models instead of attrs models
- Focus on MCP + common operations only
"""

from typing import Optional, Any, Dict, Union
import httpx
from attrs import NOTHING as UNSET

try:
    MODELS_AVAILABLE = True
    from python_alfresco_api.models.alfresco_{client_name}_models import *
except ImportError:
    MODELS_AVAILABLE = False

# Module-level variable for raw client availability
_raw_client_available = False


class Alfresco{client_name.title()}Client:
    """
    Clean, MCP-optimized Alfresco {client_name.title()} API client.
    
    Features:
    - Clean method naming (no sync/asyncio confusion)
    - Pre-imported raw functions (hidden complexity)
    - Composition over inheritance (self._raw_client)
    - Pydantic models for rich validation/serialization
    - Perfect for MCP integration
    """
    
    # Class-level variable to track raw client availability
    RAW_CLIENT_AVAILABLE = False
    
    # ================================================================
    # PRE-IMPORT RAW FUNCTIONS (HIDDEN FROM USERS)
    # ================================================================
    
    try:
{self._generate_imports(client_name, analysis)}
        
        _raw_client_available = True
        
    except ImportError as e:
        _raw_client_available = False
        import warnings
        warnings.warn(f"Raw client not available: {{e}}")
    
    # ================================================================
    # INITIALIZATION - COMPOSITION NOT INHERITANCE
    # ================================================================
    
    def __init__(self, client_factory):
        """Initialize clean {client_name} client using composition."""
        self.api_name = "{client_name}"
        self._client_factory = client_factory
        self._base_url = client_factory.base_url
        self.auth_util = client_factory.auth
        self._verify_ssl = client_factory.verify_ssl
        self._timeout = client_factory.timeout
        
        # Create authenticated client for raw operations
        self._raw_client = self._create_raw_client()
    
    def _create_raw_client(self):
        """Create the underlying raw client."""
        if not self.RAW_CLIENT_AVAILABLE:
            raise ImportError("Raw client not available")
            
        from python_alfresco_api.raw_clients.alfresco_{client_name}_client.{client_name}_client.client import AuthenticatedClient
        
        # Build correct API base URL for {client_name} client
        api_base_url = f"{{self._base_url}}{self._get_api_path(client_name)}"
        
        return AuthenticatedClient(
            base_url=api_base_url,
            token=self.auth_util.get_auth_token(),
            prefix=self.auth_util.get_auth_prefix(),
            verify_ssl=self._verify_ssl,
            timeout=self._timeout
        )
    
    @property
    def base_url(self) -> str:
        """Get the server base URL."""
        return self._base_url
    
    @property
    def client_factory(self):
        """Get the client factory."""
        return self._client_factory
    
    @property
    def raw_client(self):
        """Get the raw authenticated client."""
        return self._raw_client
    
    @property
    def httpx_client(self) -> httpx.Client:
        """Get the httpx client for direct HTTP operations."""
        return self._raw_client.get_httpx_client()
    
    @property
    def api(self) -> str:
        """Get the API name."""
        return self.api_name
    
    @property
    def auth_type(self) -> str:
        """Get the authentication type."""
        return type(self.auth_util).__name__
    
    @property
    def verify_ssl(self) -> bool:
        """Get SSL verification setting."""
        return self._verify_ssl
    
    @property
    def timeout(self) -> int:
        """Get request timeout."""
        return self._timeout
    
    @property
    def available(self) -> bool:
        """Check if the client is available and functional."""
        return self.RAW_CLIENT_AVAILABLE and self._raw_client is not None
    
    def ensure_httpx_client(self) -> httpx.Client:
        """
        Ensure httpx client is initialized and return it.
        
        Perfect for MCP servers that need raw HTTP access.
        This method both initializes (if needed) and returns the client.
        """
        return self._raw_client.get_httpx_client()
    
    # Backward compatibility - can be removed later
    def get_httpx_client(self) -> httpx.Client:
        """Deprecated: Use httpx_client property or ensure_httpx_client() method."""
        return self.ensure_httpx_client()
    
    # ================================================================
    # CLEAN {client_name.upper()} OPERATIONS (MCP CORE)
    # ================================================================
    
{self._generate_methods(client_name, analysis)}
    
    # ================================================================
    # CLIENT UTILITIES
    # ================================================================
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"Alfresco{client_name.title()}Client(base_url='{{self._base_url}}')"

# Set the class attribute after class definition
Alfresco{client_name.title()}Client.RAW_CLIENT_AVAILABLE = _raw_client_available
'''
        
        return template
    
    def _generate_imports(self, client_name: str, analysis: Dict) -> str:
        """Generate import statements for raw functions."""
        imports = []
        
        for category, operations in analysis.get('operations', {}).items():
            # Generate ALL operations, not just a limited set
            ops = [f"{op} as _{op}" for op in operations]
            if ops:
                imports.append(f'''        # {category.title()} operations
        from python_alfresco_api.raw_clients.alfresco_{client_name}_client.{client_name}_client.api.{category} import (
            {', '.join(ops)}
        )''')
        
        return '\n'.join(imports)
    
    def _generate_methods(self, client_name: str, analysis: Dict) -> str:
        """Generate clean method implementations with sync/async detailed variants."""
        methods = []
        
        # Generate ALL operations from analysis, not just a limited set
        all_operations = []
        for category, operations in analysis.get('operations', {}).items():
            for operation in operations:
                all_operations.append((category, operation))
        
        # Generate methods for ALL operations (first 10 for now to test)
        for category, operation in all_operations[:10]:  # Limit to 10 for testing
            signature = self._extract_function_signature(client_name, category, operation)
            
            method = f'''    def {operation}(self, **kwargs):
        """
        {operation.replace('_', ' ').title()} operation (simple).
        
        Returns:
            Simplified response for common use cases
        """
        if not self.RAW_CLIENT_AVAILABLE:
            raise ImportError("Raw client not available")
        result = self._{operation}.sync(client=self._raw_client, **kwargs)
        
        # TODO: Convert attrs result to Pydantic model
        return result
    
    async def {operation}_async(self, **kwargs):
        """
        {operation.replace('_', ' ').title()} operation (simple, async).
        
        Returns:
            Simplified response for common use cases
        """
        if not self.RAW_CLIENT_AVAILABLE:
            raise ImportError("Raw client not available")
        return await self._{operation}.asyncio(client=self._raw_client, **kwargs)
    
    def {operation}_detailed(self, **kwargs):
        """
        {operation.replace('_', ' ').title()} operation (detailed).
        
        Returns:
            Full Response object with status_code, headers, content, parsed
        """
        if not self.RAW_CLIENT_AVAILABLE:
            raise ImportError("Raw client not available")
        return self._{operation}.sync_detailed(client=self._raw_client, **kwargs)
    
    async def {operation}_detailed_async(self, **kwargs):
        """
        {operation.replace('_', ' ').title()} operation (detailed, async).
        
        Returns:
            Full Response object with status_code, headers, content, parsed
        """
        if not self.RAW_CLIENT_AVAILABLE:
            raise ImportError("Raw client not available")
        return await self._{operation}.asyncio_detailed(client=self._raw_client, **kwargs)'''
            
            methods.append(method)
        
        return '\n\n'.join(methods)
    
    def _get_api_path(self, client_name: str) -> str:
        """Get the API path for each client type."""
        paths = {
            "core": "/alfresco/api/-default-/public/alfresco/versions/1",
            "search": "/alfresco/api/-default-/public/search/versions/1",
            "auth": "/alfresco/api/-default-/public/authentication/versions/1",
            "discovery": "/alfresco/api",
            "workflow": "/alfresco/api/-default-/public/workflow/versions/1",
            "model": "/alfresco/api/-default-/public/alfresco/versions/1",
            "search_sql": "/alfresco/api/-default-/public/search/versions/1"
        }
        return paths.get(client_name, "/alfresco/api/-default-/public")
    
    def generate_all_v11_clients(self):
        """Generate all v1.1 style clients."""
        clients = ["core", "search", "discovery", "auth", "workflow", "model", "search_sql"]
        
        for client_name in clients:
            print(f"Generating {client_name} client v1.1...")
            
            client_code = self.generate_v11_client(client_name)
            output_file = self.output_path / f"{client_name}_client_v11.py"
            
            with open(output_file, 'w') as f:
                f.write(client_code)
            
            print(f"✅ Generated: {output_file}")


if __name__ == "__main__":
    generator = V11ClientGenerator(
        raw_clients_path="python_alfresco_api/raw_clients",
        output_path="python_alfresco_api/clients"
    )
    
    # Analyze existing raw clients
    for client in ["core", "search", "discovery"]:
        analysis = generator.analyze_raw_client(client)
        print(f"\n=== {client.upper()} CLIENT ANALYSIS ===")
        print(f"Operations: {analysis.get('operations', {})}")
        print(f"Models: {len(analysis.get('models_available', []))} available")
    
    # Generate v1.1 clients
    print("\n=== GENERATING V1.1 CLIENTS ===")
    generator.generate_all_v11_clients() 