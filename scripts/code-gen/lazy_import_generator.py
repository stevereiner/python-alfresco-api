#!/usr/bin/env python3
"""
Lazy Import Generator for V1.1 Clients

Generates wrapper clients with on-demand imports instead of central imports.
Each operation imports its dependencies only when called.
"""

def generate_lazy_import_client():
    """Generate a client with lazy imports instead of central imports."""
    
    client_code = '''#!/usr/bin/env python3
"""
AlfrescoCoreClient v1.1 - Lazy Import Architecture

🎯 LAZY IMPORTS STRATEGY:
- No upfront imports (faster startup)
- Import only when operation is called
- Graceful degradation (better error isolation)
- Memory efficient (load what you need)
- Perfect for MCP integration
"""

from typing import Optional, Any, Dict, Union
import httpx


class AlfrescoCoreClient:
    """
    Core client with lazy imports - perfect for MCP integration.
    
    🚀 INSTANT STARTUP: No upfront operation imports
    🛡️ GRACEFUL DEGRADATION: Operations fail individually 
    💾 MEMORY EFFICIENT: Only loads what you use
    🤖 MCP OPTIMIZED: Only import operations you expose as tools
    """
    
    def __init__(self, base_url: str, auth_util, **kwargs):
        """Initialize client - NO operation imports yet!"""
        self.api_name = "core"
        self._base_url = base_url
        self.auth_util = auth_util
        self._kwargs = kwargs
        
        # Create raw client (only this import needed)
        self._raw_client = self._create_raw_client()
        
        # Initialize operation groups (no imports!)
        self.nodes = NodeOperations(self)
        self.content = ContentOperations(self)
        self.search = SearchOperations(self)
    
    def _create_raw_client(self):
        """Create raw client - only import when needed."""
        try:
            # 🎯 Only import the base client
            from python_alfresco_api.raw_clients.alfresco_core_client.core_client import AuthenticatedClient
            
            api_base_url = f"{self._base_url}/alfresco/api/-default-/public/alfresco/versions/1"
            
            return AuthenticatedClient(
                base_url=api_base_url,
                token=self.auth_util.get_auth_header()["Authorization"],
                **self._kwargs
            )
        except ImportError:
            raise ImportError("Raw core client not available")


class NodeOperations:
    """Node operations with lazy imports."""
    
    def __init__(self, client):
        self._client = client
        self._raw_client = client._raw_client
        # No operation imports here!
    
    async def get(self, node_id: str, **kwargs):
        """Get node - lazy import get_node operation."""
        try:
            # 🎯 Import ONLY when this method is called
            from python_alfresco_api.raw_clients.alfresco_core_client.core_client.api.nodes import get_node
            
            result = await get_node.asyncio(client=self._raw_client, node_id=node_id, **kwargs)
            
            # TODO: Convert attrs to Pydantic model
            return result
            
        except ImportError as e:
            raise ImportError(f"get_node operation not available: {e}")
        except Exception as e:
            raise ValueError(f"get_node failed: {e}")
    
    def get_sync(self, node_id: str, **kwargs):
        """Sync version with same lazy import."""
        try:
            # 🎯 Same import pattern for sync version
            from python_alfresco_api.raw_clients.alfresco_core_client.core_client.api.nodes import get_node
            
            return get_node.sync(client=self._raw_client, node_id=node_id, **kwargs)
            
        except ImportError as e:
            raise ImportError(f"get_node operation not available: {e}")
    
    async def create(self, name: str, parent_id: str = "-my-", node_type: str = "cm:content", **kwargs):
        """Create node - lazy import create_node + models."""
        try:
            # 🎯 Import function AND models only when needed
            from python_alfresco_api.raw_clients.alfresco_core_client.core_client.api.nodes import create_node
            from python_alfresco_api.raw_clients.alfresco_core_client.core_client.models import NodeBodyCreate
            
            body = NodeBodyCreate(name=name, node_type=node_type, **kwargs)
            result = await create_node.asyncio(client=self._raw_client, node_id=parent_id, body=body)
            return result
            
        except ImportError as e:
            raise ImportError(f"create_node operation not available: {e}")
    
    async def update(self, node_id: str, properties: Dict[str, Any], **kwargs):
        """Update node - lazy import update operation."""
        try:
            # 🎯 Import only for update operations
            from python_alfresco_api.raw_clients.alfresco_core_client.core_client.api.nodes import update_node
            from python_alfresco_api.raw_clients.alfresco_core_client.core_client.models import NodeBodyUpdate
            
            # Create proper update body (simplified for demo)
            result = await update_node.asyncio(client=self._raw_client, node_id=node_id, **kwargs)
            return result
            
        except ImportError as e:
            raise ImportError(f"update_node operation not available: {e}")
    
    async def delete(self, node_id: str, permanent: bool = False, **kwargs):
        """Delete node - lazy import delete operation."""
        try:
            # 🎯 Import only for delete operations
            from python_alfresco_api.raw_clients.alfresco_core_client.core_client.api.nodes import delete_node
            
            return await delete_node.asyncio(client=self._raw_client, node_id=node_id, permanent=permanent, **kwargs)
            
        except ImportError as e:
            raise ImportError(f"delete_node operation not available: {e}")


class ContentOperations:
    """Content operations with lazy imports."""
    
    def __init__(self, client):
        self._client = client
        self._raw_client = client._raw_client
    
    async def download(self, node_id: str, **kwargs):
        """Download content - lazy import."""
        try:
            # 🎯 Import only when downloading
            from python_alfresco_api.raw_clients.alfresco_core_client.core_client.api.nodes import get_node_content
            
            return await get_node_content.asyncio(client=self._raw_client, node_id=node_id, **kwargs)
            
        except ImportError as e:
            raise ImportError(f"download operation not available: {e}")
    
    async def upload(self, node_id: str, content: bytes, **kwargs):
        """Upload content - lazy import."""
        try:
            # 🎯 Import only when uploading  
            from python_alfresco_api.raw_clients.alfresco_core_client.core_client.api.nodes import update_node_content
            
            return await update_node_content.asyncio(client=self._raw_client, node_id=node_id, body=content, **kwargs)
            
        except ImportError as e:
            raise ImportError(f"upload operation not available: {e}")


class SearchOperations:
    """Search operations with lazy imports."""
    
    def __init__(self, client):
        self._client = client
        self._raw_client = client._raw_client
    
    async def find_nodes(self, term: str, **kwargs):
        """Search nodes - lazy import."""
        try:
            # 🎯 Import only when searching
            from python_alfresco_api.raw_clients.alfresco_core_client.core_client.api.queries import find_nodes
            
            return await find_nodes.asyncio(client=self._raw_client, term=term, **kwargs)
            
        except ImportError as e:
            raise ImportError(f"search operation not available: {e}")


# ================================================================
# GENERATOR TEMPLATE
# ================================================================

def generate_operation_method(operation_name: str, api_category: str, client_name: str, is_async: bool = True) -> str:
    """Generate a single operation method with lazy imports."""
    
    async_prefix = "async " if is_async else ""
    await_prefix = "await " if is_async else ""
    method_suffix = ".asyncio" if is_async else ".sync"
    
    template = f'''    {async_prefix}def {operation_name}(self, **kwargs):
        """
        {operation_name.replace('_', ' ').title()} operation with lazy import.
        
        🎯 LAZY LOADING: Imports {operation_name} only when called
        🛡️ ERROR ISOLATION: Fails gracefully if operation not available
        💾 MEMORY EFFICIENT: No upfront import cost
        """
        try:
            # 🎯 Lazy import - only when this method is called
            from python_alfresco_api.raw_clients.alfresco_{client_name}_client.{client_name}_client.api.{api_category} import {operation_name}
            
            result = {await_prefix}{operation_name}{method_suffix}(client=self._raw_client, **kwargs)
            
            # TODO: Convert attrs to Pydantic model  
            return result
            
        except ImportError as e:
            raise ImportError(f"{operation_name} operation not available: {{e}}")
        except Exception as e:
            raise ValueError(f"{operation_name} operation failed: {{e}}")'''
    
    return template


def demonstrate_lazy_generation():
    """Demonstrate how to generate methods with lazy imports."""
    
    print("🏭 LAZY IMPORT GENERATOR DEMONSTRATION")
    print("=" * 50)
    
    # MCP operations that need generation
    mcp_operations = [
        ("get_node", "nodes", "core"),
        ("create_node", "nodes", "core"), 
        ("search", "search", "search"),
        ("find_nodes", "queries", "core")
    ]
    
    print("Generated methods with lazy imports:")
    print()
    
    for op_name, api_cat, client in mcp_operations[:2]:  # Show 2 examples
        print(f"🔧 {op_name} method:")
        method_code = generate_operation_method(op_name, api_cat, client)
        print(method_code)
        print()
    
    print("✅ BENEFITS OF GENERATED LAZY METHODS:")
    print("- Each method imports only its dependencies")
    print("- No upfront import cost at class level")
    print("- Perfect error isolation per operation")
    print("- Memory scales with actual usage")
    print("- Ideal for MCP tool interfaces")


if __name__ == "__main__":
    print("🎯 LAZY IMPORT GENERATOR FOR V1.1 CLIENTS")
    print()
    print("🚀 Generates wrapper clients with on-demand imports")
    print("🎯 Perfect for MCP integration")
    print("💾 Memory and performance optimized")
    print()
    
    demonstrate_lazy_generation()
    
    print("\n🎉 RESULT:")
    print("Generated clients with lazy imports are PERFECT for:")
    print("- 🤖 MCP servers (faster startup)")
    print("- 🎯 Focused APIs (only load what you use)")
    print("- 🛡️ Partial availability (graceful degradation)")
    print("- 💾 Memory efficiency (no upfront costs)") 