"""
Nodes operations - simplified function-based approach.
Clean, intuitive API without nested class access.
"""

# Import the client class from separate file
from .nodes_client import NodesClient

# Also export the models and functions for convenience
from .models import NodeResponse, NodeListResponse, CreateNodeRequest, UpdateNodeRequest, CopyNodeRequest, MoveNodeRequest, IncludeOption
from ..models import NodeType

# Export the individual functions too for direct access
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

__all__ = ['NodesClient']