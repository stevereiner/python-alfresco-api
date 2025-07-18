"""
Utility functions for the Alfresco API.

This module provides convenient utility functions for common operations
that MCP servers and other applications need.
"""

from . import search_utils
from . import node_utils
from . import content_utils
from . import version_utils

# Example usage patterns for MCP servers:
# 
# # Search operations (4 MCP tools)
# from python_alfresco_api import ClientFactory
# from python_alfresco_api.utils import search_utils
# 
# factory = ClientFactory()
# search_client = factory.create_search_client()
# results = search_utils.simple_search(search_client, "document")
#
# # Node operations (10 MCP tools)
# from python_alfresco_api.utils import node_utils
# 
# core_client = factory.create_core_client()
# 
# # MCP browse_repository tool
# children = node_utils.browse_repository(core_client, parent_id="-my-")
# 
# # MCP get_node_properties tool  
# node_info = node_utils.get_node_properties(core_client, node_id)
# 
# # MCP create_folder tool
# folder = node_utils.create_folder(core_client, "My Folder", parent_id="-my-")
# 
# # MCP upload_document tool
# upload_result = node_utils.upload_document(core_client, "file.pdf", parent_id=folder_id)
# 
# # MCP download_document tool
# content = node_utils.download_document(core_client, node_id)
# 
# # MCP update_node_properties tool
# update_result = node_utils.update_node_properties(core_client, node_id, {"cm:title": "New Title"})
# 
# # MCP delete_node tool
# delete_result = node_utils.delete_node(core_client, node_id)
# 
# # MCP checkout_document tool (document lifecycle)
# checkout_result = node_utils.checkout_document(core_client, node_id)
# 
# # MCP checkin_document tool (document lifecycle)
# checkin_result = node_utils.checkin_document(core_client, node_id, content="Updated content", comment="Fixed issues")
# 
# # MCP cancel_checkout tool (document lifecycle)
# cancel_result = node_utils.cancel_checkout(core_client, node_id)
#
# # Alternative: High-level version utils for document versioning workflow
# from python_alfresco_api.utils import version_utils_highlevel
#
# # Checkout -> Edit -> Checkin workflow
# checkout_result = version_utils_highlevel.checkout_document_highlevel(core_client, node_id)
# checkin_result = version_utils_highlevel.checkin_document_highlevel(core_client, node_id, content="New content", comment="Updated")
# 
# # Or cancel if you want to discard changes
# cancel_result = version_utils_highlevel.cancel_checkout_highlevel(core_client, node_id)

__all__ = [
    "search_utils",
    "node_utils",
    "content_utils",
    "version_utils"
] 