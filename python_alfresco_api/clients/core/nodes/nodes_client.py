"""
Nodes Client - Simplified function-based API

Clean, intuitive node operations without nested class access.
"""

# Import the simplified functions
from .get_node import get_node, get_node_async, get_node_detailed, get_node_detailed_async
from .create_node import create_node, create_node_async, create_node_detailed, create_node_detailed_async
from .delete_node import delete_node, delete_node_async, delete_node_detailed, delete_node_detailed_async
from .list_node_children import list_node_children, list_node_children_async, list_node_children_detailed, list_node_children_detailed_async
from .update_node import update_node, update_node_async, update_node_detailed, update_node_detailed_async
from .copy_node import copy_node, copy_node_async, copy_node_detailed, copy_node_detailed_async
from .move_node import move_node, move_node_async, move_node_detailed, move_node_detailed_async
from .lock_node import lock_node, lock_node_async, lock_node_detailed, lock_node_detailed_async
from .unlock_node import unlock_node, unlock_node_async, unlock_node_detailed, unlock_node_detailed_async
from .update_node_content import update_node_content, update_node_content_async, update_node_content_detailed, update_node_content_detailed_async
from .list_target_associations import list_target_associations, list_target_associations_async, list_target_associations_detailed, list_target_associations_detailed_async
from .list_secondary_children import list_secondary_children, list_secondary_children_async, list_secondary_children_detailed, list_secondary_children_detailed_async
from .list_source_associations import list_source_associations, list_source_associations_async, list_source_associations_detailed, list_source_associations_detailed_async
from .list_parents import list_parents, list_parents_async, list_parents_detailed, list_parents_detailed_async
from .delete_secondary_child_association import delete_secondary_child_association, delete_secondary_child_association_async, delete_secondary_child_association_detailed, delete_secondary_child_association_detailed_async
from .delete_association import delete_association, delete_association_async, delete_association_detailed, delete_association_detailed_async
from .create_secondary_child_association import create_secondary_child_association, create_secondary_child_association_async, create_secondary_child_association_detailed, create_secondary_child_association_detailed_async
from .create_folder import create_folder, create_folder_async, create_folder_detailed, create_folder_detailed_async
from .create_association import create_association, create_association_async, create_association_detailed, create_association_detailed_async

# Import types for convenience
from typing import Optional, List, Union, IO, BinaryIO
from .models import NodeResponse, NodeListResponse, CreateNodeRequest, UpdateNodeRequest, CopyNodeRequest, MoveNodeRequest, IncludeOption
from ..models import NodeType


class NodesClient:
    """
    Simplified nodes client with clean function-based API.
    No more nested access like client.nodes.get.get() - just client.nodes.get().
    
    CLEAN API PATTERN:
    - client.nodes.get(node_id) - Simple and intuitive
    - client.nodes.create(parent_id, request) - Obvious what it does
    - client.nodes.delete(node_id) - Clear and direct
    - client.nodes.list_children(node_id) - Natural naming
    - client.nodes.update(node_id, request) - Clean updates
    - client.nodes.copy(node_id, request) - Copy operations
    - client.nodes.move(node_id, request) - Move operations
    - client.nodes.lock(node_id) - Lock operations
    - client.nodes.unlock(node_id) - Unlock operations
    - client.nodes.update_content(node_id, content) - File uploads
    - client.nodes.list_target_associations(node_id) - Target associations
    - client.nodes.list_secondary_children(node_id) - Secondary children
    - client.nodes.list_source_associations(node_id) - Source associations
    - client.nodes.list_parents(node_id) - List all parents
    - client.nodes.delete_secondary_child_association(node_id, child_id) - Delete secondary child association
    - client.nodes.delete_association(node_id, target_id) - Delete association
    - client.nodes.create_secondary_child_association(node_id, child_id, assoc_type) - Create secondary child association
    - client.nodes.create_folder_convenience(name, parent_id) - Create folder convenience method
    - client.nodes.create_association(node_id, target_id, assoc_type) - Create association
    
    ASYNC VERSIONS:
    - client.nodes.get_async(node_id)
    - client.nodes.create_async(parent_id, request)
    - client.nodes.delete_async(node_id)
    - client.nodes.list_children_async(node_id)
    - client.nodes.update_async(node_id, request)
    - client.nodes.copy_async(node_id, request)
    - client.nodes.move_async(node_id, request)
    - client.nodes.lock_async(node_id)
    - client.nodes.unlock_async(node_id)
    - client.nodes.update_content_async(node_id, content)
    - client.nodes.list_target_associations_async(node_id)
    - client.nodes.list_secondary_children_async(node_id)
    - client.nodes.list_source_associations_async(node_id)
    - client.nodes.list_parents_async(node_id)
    - client.nodes.delete_secondary_child_association_async(node_id, child_id)
    - client.nodes.delete_association_async(node_id, target_id)
    - client.nodes.create_secondary_child_association_async(node_id, child_id, assoc_type)
    - client.nodes.create_folder_convenience_async(name, parent_id)
    - client.nodes.create_association_async(node_id, target_id, assoc_type)
    """
    
    def __init__(self, parent_client):
        self.parent_client = parent_client
    
    @property
    def raw_client(self):
        """Delegate to parent client's raw client."""
        return self.parent_client.raw_client
    
    @property
    def httpx_client(self):
        """Delegate to parent client's httpx client."""
        return self.parent_client.httpx_client
    
    # ==========================================
    # SYNC VERSIONS
    # ==========================================
    
    def get(
        self, 
        node_id: str, 
        include: Optional[List[Union[str, IncludeOption]]] = None,
        relative_path: Optional[str] = None,
        fields: Optional[List[str]] = None,
        **kwargs
    ) -> NodeResponse:
        """Get node information - clean and simple."""
        return get_node(self, node_id, include, relative_path, fields, **kwargs)
    
    async def get_async(
        self, 
        node_id: str, 
        include: Optional[List[Union[str, IncludeOption]]] = None,
        relative_path: Optional[str] = None,
        fields: Optional[List[str]] = None,
        **kwargs
    ) -> NodeResponse:
        """Get node information (async) - clean and simple."""
        return await get_node_async(self, node_id, include, relative_path, fields, **kwargs)
    
    def create(self, parent_id: str, request: CreateNodeRequest) -> NodeResponse:
        """Create a new node - clean and simple."""
        return create_node(self, parent_id, request)
    
    async def create_async(self, parent_id: str, request: CreateNodeRequest) -> NodeResponse:
        """Create a new node (async) - clean and simple."""
        return await create_node_async(self, parent_id, request)
    
    def delete(self, node_id: str, permanent: bool = False) -> None:
        """Delete a node - clean and simple."""
        return delete_node(self, node_id, permanent)
    
    async def delete_async(self, node_id: str, permanent: bool = False) -> None:
        """Delete a node (async) - clean and simple."""
        return await delete_node_async(self, node_id, permanent)
    
    def list_children(self, node_id: str, skip_count: int = 0, max_items: int = 100) -> NodeListResponse:
        """List node children - clean and simple."""
        return list_node_children(self, node_id, skip_count, max_items)
    
    async def list_children_async(self, node_id: str, skip_count: int = 0, max_items: int = 100) -> NodeListResponse:
        """List node children (async) - clean and simple."""
        return await list_node_children_async(self, node_id, skip_count, max_items)
    
    def update(self, node_id: str, request: UpdateNodeRequest, include: Optional[List[Union[str, IncludeOption]]] = None) -> NodeResponse:
        """Update node properties - clean and simple."""
        return update_node(self, node_id, request, include)
    
    async def update_async(self, node_id: str, request: UpdateNodeRequest, include: Optional[List[Union[str, IncludeOption]]] = None) -> NodeResponse:
        """Update node properties (async) - clean and simple."""
        return await update_node_async(self, node_id, request, include)
    
    def copy(self, node_id: str, request: CopyNodeRequest, include: Optional[List[Union[str, IncludeOption]]] = None) -> NodeResponse:
        """Copy a node - clean and simple."""
        return copy_node(self, node_id, request, include)
    
    async def copy_async(self, node_id: str, request: CopyNodeRequest, include: Optional[List[Union[str, IncludeOption]]] = None) -> NodeResponse:
        """Copy a node (async) - clean and simple."""
        return await copy_node_async(self, node_id, request, include)
    
    def move(self, node_id: str, request: MoveNodeRequest, include: Optional[List[Union[str, IncludeOption]]] = None) -> NodeResponse:
        """Move a node - clean and simple."""
        return move_node(self, node_id, request, include)
    
    async def move_async(self, node_id: str, request: MoveNodeRequest, include: Optional[List[Union[str, IncludeOption]]] = None) -> NodeResponse:
        """Move a node (async) - clean and simple."""
        return await move_node_async(self, node_id, request, include)
    
    def lock(self, node_id: str, request: Optional[dict] = None, include: Optional[List[Union[str, str]]] = None) -> NodeResponse:
        """Lock a node - clean and simple."""
        return lock_node(self, node_id, request, include)
    
    async def lock_async(self, node_id: str, request: Optional[dict] = None, include: Optional[List[Union[str, str]]] = None) -> NodeResponse:
        """Lock a node (async) - clean and simple."""
        return await lock_node_async(self, node_id, request, include)
    
    def unlock(self, node_id: str, include: Optional[List[Union[str, str]]] = None) -> NodeResponse:
        """Unlock a node - clean and simple."""
        return unlock_node(self, node_id, include)
    
    async def unlock_async(self, node_id: str, include: Optional[List[Union[str, str]]] = None) -> NodeResponse:
        """Unlock a node (async) - clean and simple."""
        return await unlock_node_async(self, node_id, include)
    
    def update_content(self, node_id: str, content: Union[bytes, IO[bytes]], filename: Optional[str] = None, include: Optional[List[str]] = None) -> NodeResponse:
        """Update node content (file upload) - clean and simple."""
        return update_node_content(self, node_id, content, filename, include)
    
    async def update_content_async(self, node_id: str, content: Union[bytes, IO[bytes]], filename: Optional[str] = None, include: Optional[List[str]] = None) -> NodeResponse:
        """Update node content (file upload) (async) - clean and simple."""
        return await update_node_content_async(self, node_id, content, filename, include)
    
    def list_target_associations(self, node_id: str, where: Optional[str] = None, include: Optional[List[str]] = None, fields: Optional[List[str]] = None) -> NodeListResponse:
        """List target associations - clean and simple."""
        return list_target_associations(self, node_id, where, include, fields)
    
    async def list_target_associations_async(self, node_id: str, where: Optional[str] = None, include: Optional[List[str]] = None, fields: Optional[List[str]] = None) -> NodeListResponse:
        """List target associations (async) - clean and simple."""
        return await list_target_associations_async(self, node_id, where, include, fields)
    
    def list_secondary_children(self, node_id: str, where: Optional[str] = None, include: Optional[List[str]] = None, fields: Optional[List[str]] = None) -> NodeListResponse:
        """List secondary children - clean and simple."""
        return list_secondary_children(self, node_id, where, include, fields)
    
    async def list_secondary_children_async(self, node_id: str, where: Optional[str] = None, include: Optional[List[str]] = None, fields: Optional[List[str]] = None) -> NodeListResponse:
        """List secondary children (async) - clean and simple."""
        return await list_secondary_children_async(self, node_id, where, include, fields)
    
    def list_source_associations(self, node_id: str, where: Optional[str] = None, include: Optional[List[str]] = None, fields: Optional[List[str]] = None) -> NodeListResponse:
        """List source associations - clean and simple."""
        return list_source_associations(self, node_id, where, include, fields)
    
    async def list_source_associations_async(self, node_id: str, where: Optional[str] = None, include: Optional[List[str]] = None, fields: Optional[List[str]] = None) -> NodeListResponse:
        """List source associations (async) - clean and simple."""
        return await list_source_associations_async(self, node_id, where, include, fields)
    
    def list_parents(self, node_id: str, where: Optional[str] = None, include: Optional[List[str]] = None, fields: Optional[List[str]] = None):
        """List all parents of a node - clean and simple."""
        return list_parents(self, node_id, where, include, fields)
    
    async def list_parents_async(self, node_id: str, where: Optional[str] = None, include: Optional[List[str]] = None, fields: Optional[List[str]] = None):
        """List all parents of a node (async) - clean and simple."""
        return await list_parents_async(self, node_id, where, include, fields)
    
    def delete_secondary_child_association(self, node_id: str, child_id: str, assoc_type: Optional[str] = None) -> None:
        """Delete secondary child association - clean and simple."""
        return delete_secondary_child_association(self, node_id, child_id, assoc_type)
    
    async def delete_secondary_child_association_async(self, node_id: str, child_id: str, assoc_type: Optional[str] = None) -> None:
        """Delete secondary child association (async) - clean and simple."""
        return await delete_secondary_child_association_async(self, node_id, child_id, assoc_type)
    
    def delete_association(self, node_id: str, target_id: str, assoc_type: Optional[str] = None) -> None:
        """Delete association between nodes - clean and simple."""
        return delete_association(self, node_id, target_id, assoc_type)
    
    async def delete_association_async(self, node_id: str, target_id: str, assoc_type: Optional[str] = None) -> None:
        """Delete association between nodes (async) - clean and simple."""
        return await delete_association_async(self, node_id, target_id, assoc_type)
    
    def create_secondary_child_association(self, node_id: str, child_id: str, assoc_type: str, fields: Optional[List[str]] = None):
        """Create secondary child association - clean and simple."""
        return create_secondary_child_association(self, node_id, child_id, assoc_type, fields)
    
    async def create_secondary_child_association_async(self, node_id: str, child_id: str, assoc_type: str, fields: Optional[List[str]] = None):
        """Create secondary child association (async) - clean and simple."""
        return await create_secondary_child_association_async(self, node_id, child_id, assoc_type, fields)
    
    def create_folder_convenience(self, name: str, parent_id: str = "-my-", properties: Optional[dict] = None, auto_rename: bool = True, fields: Optional[List[str]] = None):
        """Create a folder (convenience method) - clean and simple."""
        return create_folder(self, name, parent_id, properties, auto_rename, fields)
    
    async def create_folder_convenience_async(self, name: str, parent_id: str = "-my-", properties: Optional[dict] = None, auto_rename: bool = True, fields: Optional[List[str]] = None):
        """Create a folder (convenience method) (async) - clean and simple."""
        return await create_folder_async(self, name, parent_id, properties, auto_rename, fields)
    
    def create_association(self, node_id: str, target_id: str, assoc_type: str, fields: Optional[List[str]] = None):
        """Create association between nodes - clean and simple."""
        return create_association(self, node_id, target_id, assoc_type, fields)
    
    async def create_association_async(self, node_id: str, target_id: str, assoc_type: str, fields: Optional[List[str]] = None):
        """Create association between nodes (async) - clean and simple."""
        return await create_association_async(self, node_id, target_id, assoc_type, fields)
    
    # ==========================================
    # DETAILED VERSIONS
    # ==========================================
    
    def get_detailed(
        self, 
        node_id: str, 
        include: Optional[List[Union[str, IncludeOption]]] = None,
        relative_path: Optional[str] = None,
        fields: Optional[List[str]] = None,
        **kwargs
    ):
        """Get node (detailed) - returns full HTTP response."""
        return get_node_detailed(self, node_id, include, relative_path, fields, **kwargs)
    
    async def get_detailed_async(
        self, 
        node_id: str, 
        include: Optional[List[Union[str, IncludeOption]]] = None,
        relative_path: Optional[str] = None,
        fields: Optional[List[str]] = None,
        **kwargs
    ):
        """Get node (detailed async) - returns full HTTP response."""
        return await get_node_detailed_async(self, node_id, include, relative_path, fields, **kwargs)
    
    def create_detailed(self, parent_id: str, request: CreateNodeRequest):
        """Create node (detailed) - returns full HTTP response."""
        return create_node_detailed(self, parent_id, request)
    
    async def create_detailed_async(self, parent_id: str, request: CreateNodeRequest):
        """Create node (detailed async) - returns full HTTP response."""
        return await create_node_detailed_async(self, parent_id, request)
    
    def delete_detailed(self, node_id: str, permanent: bool = False):
        """Delete node (detailed) - returns full HTTP response."""
        return delete_node_detailed(self, node_id, permanent)
    
    async def delete_detailed_async(self, node_id: str, permanent: bool = False):
        """Delete node (detailed async) - returns full HTTP response."""
        return await delete_node_detailed_async(self, node_id, permanent)
    
    def list_children_detailed(self, node_id: str, skip_count: int = 0, max_items: int = 100):
        """List children (detailed) - returns full HTTP response."""
        return list_node_children_detailed(self, node_id, skip_count, max_items)
    
    async def list_children_detailed_async(self, node_id: str, skip_count: int = 0, max_items: int = 100):
        """List children (detailed async) - returns full HTTP response."""
        return await list_node_children_detailed_async(self, node_id, skip_count, max_items)
    
    def update_detailed(self, node_id: str, request: UpdateNodeRequest, include: Optional[List[Union[str, IncludeOption]]] = None):
        """Update node (detailed) - returns full HTTP response."""
        return update_node_detailed(self, node_id, request, include)
    
    async def update_detailed_async(self, node_id: str, request: UpdateNodeRequest, include: Optional[List[Union[str, IncludeOption]]] = None):
        """Update node (detailed async) - returns full HTTP response."""
        return await update_node_detailed_async(self, node_id, request, include)
    
    def copy_detailed(self, node_id: str, request: CopyNodeRequest, include: Optional[List[Union[str, IncludeOption]]] = None):
        """Copy node (detailed) - returns full HTTP response."""
        return copy_node_detailed(self, node_id, request, include)
    
    async def copy_detailed_async(self, node_id: str, request: CopyNodeRequest, include: Optional[List[Union[str, IncludeOption]]] = None):
        """Copy node (detailed async) - returns full HTTP response."""
        return await copy_node_detailed_async(self, node_id, request, include)
    
    def move_detailed(self, node_id: str, request: MoveNodeRequest, include: Optional[List[Union[str, IncludeOption]]] = None):
        """Move node (detailed) - returns full HTTP response."""
        return move_node_detailed(self, node_id, request, include)
    
    async def move_detailed_async(self, node_id: str, request: MoveNodeRequest, include: Optional[List[Union[str, IncludeOption]]] = None):
        """Move node (detailed async) - returns full HTTP response."""
        return await move_node_detailed_async(self, node_id, request, include)
    
    def lock_detailed(self, node_id: str, request: Optional[dict] = None, include: Optional[List[Union[str, str]]] = None):
        """Lock node (detailed) - returns full HTTP response."""
        return lock_node_detailed(self, node_id, request, include)
    
    async def lock_detailed_async(self, node_id: str, request: Optional[dict] = None, include: Optional[List[Union[str, str]]] = None):
        """Lock node (detailed async) - returns full HTTP response."""
        return await lock_node_detailed_async(self, node_id, request, include)
    
    def unlock_detailed(self, node_id: str, include: Optional[List[Union[str, str]]] = None):
        """Unlock node (detailed) - returns full HTTP response."""
        return unlock_node_detailed(self, node_id, include)
    
    async def unlock_detailed_async(self, node_id: str, include: Optional[List[Union[str, str]]] = None):
        """Unlock node (detailed async) - returns full HTTP response."""
        return await unlock_node_detailed_async(self, node_id, include)
    
    def update_content_detailed(self, node_id: str, content: Union[bytes, IO[bytes]], filename: Optional[str] = None, include: Optional[List[str]] = None):
        """Update node content (detailed) - returns full HTTP response."""
        return update_node_content_detailed(self, node_id, content, filename, include)
    
    async def update_content_detailed_async(self, node_id: str, content: Union[bytes, IO[bytes]], filename: Optional[str] = None, include: Optional[List[str]] = None):
        """Update node content (detailed async) - returns full HTTP response."""
        return await update_node_content_detailed_async(self, node_id, content, filename, include)
    
    def list_target_associations_detailed(self, node_id: str, where: Optional[str] = None, include: Optional[List[str]] = None, fields: Optional[List[str]] = None):
        """List target associations (detailed) - returns full HTTP response."""
        return list_target_associations_detailed(self, node_id, where, include, fields)
    
    async def list_target_associations_detailed_async(self, node_id: str, where: Optional[str] = None, include: Optional[List[str]] = None, fields: Optional[List[str]] = None):
        """List target associations (detailed async) - returns full HTTP response."""
        return await list_target_associations_detailed_async(self, node_id, where, include, fields)
    
    def list_secondary_children_detailed(self, node_id: str, where: Optional[str] = None, include: Optional[List[str]] = None, fields: Optional[List[str]] = None):
        """List secondary children (detailed) - returns full HTTP response."""
        return list_secondary_children_detailed(self, node_id, where, include, fields)
    
    async def list_secondary_children_detailed_async(self, node_id: str, where: Optional[str] = None, include: Optional[List[str]] = None, fields: Optional[List[str]] = None):
        """List secondary children (detailed async) - returns full HTTP response."""
        return await list_secondary_children_detailed_async(self, node_id, where, include, fields)
    
    def list_source_associations_detailed(self, node_id: str, where: Optional[str] = None, include: Optional[List[str]] = None, fields: Optional[List[str]] = None):
        """List source associations (detailed) - returns full HTTP response."""
        return list_source_associations_detailed(self, node_id, where, include, fields)
    
    async def list_source_associations_detailed_async(self, node_id: str, where: Optional[str] = None, include: Optional[List[str]] = None, fields: Optional[List[str]] = None):
        """List source associations (detailed async) - returns full HTTP response."""
        return await list_source_associations_detailed_async(self, node_id, where, include, fields)
    
    def list_parents_detailed(self, node_id: str, where: Optional[str] = None, include: Optional[List[str]] = None, fields: Optional[List[str]] = None):
        """List all parents of a node (detailed) - returns full HTTP response."""
        return list_parents_detailed(self, node_id, where, include, fields)
    
    async def list_parents_detailed_async(self, node_id: str, where: Optional[str] = None, include: Optional[List[str]] = None, fields: Optional[List[str]] = None):
        """List all parents of a node (detailed async) - returns full HTTP response."""
        return await list_parents_detailed_async(self, node_id, where, include, fields)
    
    def delete_secondary_child_association_detailed(self, node_id: str, child_id: str, assoc_type: Optional[str] = None):
        """Delete secondary child association (detailed) - returns full HTTP response."""
        return delete_secondary_child_association_detailed(self, node_id, child_id, assoc_type)
    
    async def delete_secondary_child_association_detailed_async(self, node_id: str, child_id: str, assoc_type: Optional[str] = None):
        """Delete secondary child association (detailed async) - returns full HTTP response."""
        return await delete_secondary_child_association_detailed_async(self, node_id, child_id, assoc_type)
    
    def delete_association_detailed(self, node_id: str, target_id: str, assoc_type: Optional[str] = None):
        """Delete association between nodes (detailed) - returns full HTTP response."""
        return delete_association_detailed(self, node_id, target_id, assoc_type)
    
    async def delete_association_detailed_async(self, node_id: str, target_id: str, assoc_type: Optional[str] = None):
        """Delete association between nodes (detailed async) - returns full HTTP response."""
        return await delete_association_detailed_async(self, node_id, target_id, assoc_type)
    
    def create_secondary_child_association_detailed(self, node_id: str, child_id: str, assoc_type: str, fields: Optional[List[str]] = None):
        """Create secondary child association (detailed) - returns full HTTP response."""
        return create_secondary_child_association_detailed(self, node_id, child_id, assoc_type, fields)
    
    async def create_secondary_child_association_detailed_async(self, node_id: str, child_id: str, assoc_type: str, fields: Optional[List[str]] = None):
        """Create secondary child association (detailed async) - returns full HTTP response."""
        return await create_secondary_child_association_detailed_async(self, node_id, child_id, assoc_type, fields)
    
    def create_folder_convenience_detailed(self, name: str, parent_id: str = "-my-", properties: Optional[dict] = None, auto_rename: bool = True, fields: Optional[List[str]] = None):
        """Create a folder (convenience method) (detailed) - returns full HTTP response."""
        return create_folder_detailed(self, name, parent_id, properties, auto_rename, fields)
    
    async def create_folder_convenience_detailed_async(self, name: str, parent_id: str = "-my-", properties: Optional[dict] = None, auto_rename: bool = True, fields: Optional[List[str]] = None):
        """Create a folder (convenience method) (detailed async) - returns full HTTP response."""
        return await create_folder_detailed_async(self, name, parent_id, properties, auto_rename, fields)
    
    def create_association_detailed(self, node_id: str, target_id: str, assoc_type: str, fields: Optional[List[str]] = None):
        """Create association between nodes (detailed) - returns full HTTP response."""
        return create_association_detailed(self, node_id, target_id, assoc_type, fields)
    
    async def create_association_detailed_async(self, node_id: str, target_id: str, assoc_type: str, fields: Optional[List[str]] = None):
        """Create association between nodes (detailed async) - returns full HTTP response."""
        return await create_association_detailed_async(self, node_id, target_id, assoc_type, fields)
    
    # ==========================================
    # CONVENIENCE METHODS FOR COMMON TASKS
    # ==========================================
    
    def create_folder(self, name: str, parent_id: str = "-my-", properties: Optional[dict] = None) -> NodeResponse:
        """Convenience method: Create a folder."""
        request = CreateNodeRequest(
            name=name,
            node_type=NodeType.FOLDER,
            properties=properties,
            aspects=[],
            auto_rename=True,
            versioning_enabled=None,
            major_version=None
        )
        return self.create(parent_id, request)
    
    async def create_folder_async(self, name: str, parent_id: str = "-my-", properties: Optional[dict] = None) -> NodeResponse:
        """Convenience method: Create a folder (async)."""
        request = CreateNodeRequest(
            name=name,
            node_type=NodeType.FOLDER,
            properties=properties,
            aspects=[],
            auto_rename=True,
            versioning_enabled=None,
            major_version=None
        )
        return await self.create_async(parent_id, request)
    
    def browse(self, node_id: str = "-my-", max_items: int = 100) -> NodeListResponse:
        """Convenience method: Browse folder contents."""
        return self.list_children(node_id, max_items=max_items)
    
    async def browse_async(self, node_id: str = "-my-", max_items: int = 100) -> NodeListResponse:
        """Convenience method: Browse folder contents (async)."""
        return await self.list_children_async(node_id, max_items=max_items)
    
    def __repr__(self) -> str:
        return "NodesClient(simplified function-based API - clean and intuitive)" 