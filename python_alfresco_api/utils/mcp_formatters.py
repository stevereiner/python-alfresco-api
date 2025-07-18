"""
MCP Formatters for Alfresco API responses.

This module provides formatters that convert raw API responses into MCP-compatible
formatted strings that match the expected output schema for MCP tools.

These formatters are designed to work with the utility functions and provide
human-readable output for AI models and MCP servers.
"""

from typing import Any, List, Dict, Optional
from datetime import datetime


def format_search_results(
    search_result: Any,
    query: str,
    max_results: int = 25
) -> str:
    """
    Format search results for MCP compatibility.
    
    Returns structured output matching MCP schema:
    {
        "result": "Found X item(s) matching 'query':\n\n..."
    }
    """
    try:
        # Extract entries from search result
        entries = []
        if search_result and hasattr(search_result, 'list'):
            list_data = search_result.list
            if isinstance(list_data, dict) and 'entries' in list_data:
                entries = list_data['entries']
            elif hasattr(list_data, 'entries'):
                entries = getattr(list_data, 'entries', [])
        
        if entries:
            result_text = f"Found {len(entries)} item(s) matching '{query}':\n\n"
            
            for i, entry in enumerate(entries, 1):
                if isinstance(entry, dict) and 'entry' in entry:
                    node = entry['entry']
                elif hasattr(entry, 'entry'):
                    node_obj = entry.entry
                    # Convert to dict for consistent access
                    node = {
                        'name': getattr(node_obj, 'name', 'Unknown'),
                        'id': getattr(node_obj, 'id', 'Unknown'),
                        'nodeType': getattr(node_obj, 'node_type', getattr(node_obj, 'nodeType', 'Unknown')),
                        'createdAt': getattr(node_obj, 'created_at', getattr(node_obj, 'createdAt', 'Unknown'))
                    }
                else:
                    node = entry
                
                name = str(node.get('name', 'Unknown'))
                node_id = str(node.get('id', 'Unknown'))
                node_type = str(node.get('nodeType', 'Unknown'))
                created_at = str(node.get('createdAt', 'Unknown'))
                
                result_text += f"{i}. **{name}**\n"
                result_text += f"   - ID: `{node_id}`\n"
                result_text += f"   - Type: {node_type}\n"
                result_text += f"   - Created: {created_at}\n\n"
            
            return result_text
        else:
            # No results found - provide helpful feedback
            feedback_msg = f"📭 No items found matching '{query}'\n\n"
            feedback_msg += "INFO: **Most likely reason: Search indexing delay**\n"
            feedback_msg += "• Alfresco search indexing can take time to update\n"
            feedback_msg += "• New documents may not appear in search immediately\n"
            feedback_msg += "• This is normal for Alfresco Community Edition\n\n"
            feedback_msg += ">> **Try these alternatives:**\n"
            feedback_msg += "1. **Browse repository structure** using browse_repository\n"
            feedback_msg += "2. **Upload a test document** and wait a few minutes for indexing\n"
            feedback_msg += "3. **Use direct node access** if you have the node ID\n"
            feedback_msg += "4. **Check Alfresco Share UI** at http://localhost:8080/share\n\n"
            feedback_msg += ">> **Search tips:**\n"
            feedback_msg += "• Use wildcards: `test*` finds files starting with 'test'\n"
            feedback_msg += "• Search by type: `TYPE:\"cm:content\"` finds all documents\n"
            feedback_msg += "• Path search: `PATH:\"/app:company_home/app:shared//*\"`\n"
            feedback_msg += "• **Note**: Search results depend on Alfresco's search indexing status"
            
            return feedback_msg
            
    except Exception as e:
        return f"❌ Search formatting failed: {str(e)}"


def format_browse_results(
    browse_result: Any,
    node_id: str = "-my-"
) -> str:
    """
    Format browse/repository listing results for MCP compatibility.
    """
    try:
        # Extract entries from browse result
        entries = []
        if browse_result and hasattr(browse_result, 'list'):
            list_data = browse_result.list
            if hasattr(list_data, 'entries'):
                entries = getattr(list_data, 'entries', [])
        
        response_text = f"📂 **Contents of '{node_id}'**\n\n"
        
        if entries:
            response_text += f">> Found {len(entries)} item(s):\n\n"
            
            for i, entry in enumerate(entries, 1):
                if hasattr(entry, 'entry'):
                    node = entry.entry
                    name = str(getattr(node, 'name', 'Unknown'))
                    node_id_val = str(getattr(node, 'id', 'Unknown'))
                    node_type = str(getattr(node, 'node_type', getattr(node, 'nodeType', 'Unknown')))
                    is_folder = getattr(node, 'is_folder', getattr(node, 'isFolder', False))
                    created_at = str(getattr(node, 'created_at', getattr(node, 'createdAt', 'Unknown')))
                    
                    icon = "[FOLDER]" if is_folder else "[FILE]"
                    response_text += f"{i}. {icon} **{name}**\n"
                    response_text += f"   - ID: `{node_id_val}`\n"
                    response_text += f"   - Type: {node_type}\n"
                    response_text += f"   - Created: {created_at}\n\n"
        else:
            response_text += "📭 **This folder is empty**\n\n"
            response_text += "INFO: **What you can do:**\n"
            response_text += "• Upload documents using upload_document\n"
            response_text += "• Create subfolders using create_folder\n"
            response_text += "• Browse other locations like `-shared-`, `-root-`, or `-sites-`\n"
        
        return response_text
        
    except Exception as e:
        return f"❌ Browse formatting failed: {str(e)}"


def format_upload_result(
    upload_result: Any,
    filename: str
) -> str:
    """
    Format document upload results for MCP compatibility.
    """
    try:
        if upload_result and isinstance(upload_result, dict) and 'entry' in upload_result:
            document = upload_result['entry']
            node_id = document.get('id', 'Unknown')
            node_name = document.get('name', filename)
            created_at = document.get('createdAt', 'Unknown')
            node_type = document.get('nodeType', 'cm:content')
            
            response_text = f"✅ **Document Uploaded Successfully!**\n\n"
            response_text += f"📄 **File**: {filename}\n"
            response_text += f"🆔 **Document ID**: `{node_id}`\n"
            response_text += f"📅 **Created**: {created_at}\n"
            response_text += f"🏷️ **Type**: {node_type}\n\n"
            response_text += f">> **Next steps:**\n"
            response_text += f"• **Download**: Use download_document with ID `{node_id}`\n"
            response_text += f"• **Update**: Use update_node_properties to modify metadata\n"
            response_text += f"• **Search**: File will appear in search once indexed\n"
            
            return response_text
        else:
            return f"❌ Upload failed: Invalid response from Alfresco"
            
    except Exception as e:
        return f"❌ Upload formatting failed: {str(e)}"


def format_folder_creation_result(
    creation_result: Any,
    folder_name: str
) -> str:
    """
    Format folder creation results for MCP compatibility.
    """
    try:
        if creation_result and hasattr(creation_result, 'entry'):
            folder_entry = creation_result.entry
            folder_id = getattr(folder_entry, 'id', 'Unknown')
            created_name = getattr(folder_entry, 'name', folder_name)
            created_at = getattr(folder_entry, 'created_at', getattr(folder_entry, 'createdAt', 'Unknown'))
            
            response_text = f"✅ **Folder Created Successfully!**\n\n"
            response_text += f"📁 **Folder**: {created_name}\n"
            response_text += f"🆔 **Folder ID**: `{folder_id}`\n"
            response_text += f"📅 **Created**: {created_at}\n\n"
            response_text += f">> **Next steps:**\n"
            response_text += f"• **Browse**: Use browse_repository with ID `{folder_id}`\n"
            response_text += f"• **Upload**: Use upload_document with parent_id `{folder_id}`\n"
            response_text += f"• **Create subfolders**: Use create_folder with parent_id `{folder_id}`\n"
            
            return response_text
        else:
            return f"❌ Folder creation failed: Invalid response from Alfresco"
            
    except Exception as e:
        return f"❌ Folder creation formatting failed: {str(e)}"


def format_node_properties_result(
    properties_result: Any,
    node_id: str
) -> str:
    """
    Format node properties retrieval results for MCP compatibility.
    """
    try:
        if properties_result and hasattr(properties_result, 'entry'):
            entry = properties_result.entry
            name = getattr(entry, 'name', 'Unknown')
            node_type = getattr(entry, 'node_type', getattr(entry, 'nodeType', 'Unknown'))
            created_at = getattr(entry, 'created_at', getattr(entry, 'createdAt', 'Unknown'))
            modified_at = getattr(entry, 'modified_at', getattr(entry, 'modifiedAt', 'Unknown'))
            is_folder = getattr(entry, 'is_folder', getattr(entry, 'isFolder', False))
            
            # Get properties if available
            properties = getattr(entry, 'properties', {})
            
            response_text = f"🏷️ **Node Properties for '{name}'**\n\n"
            response_text += f"📄 **Basic Information:**\n"
            response_text += f"   - **Name**: {name}\n"
            response_text += f"   - **ID**: `{node_id}`\n"
            response_text += f"   - **Type**: {node_type}\n"
            response_text += f"   - **Is Folder**: {'Yes' if is_folder else 'No'}\n"
            response_text += f"   - **Created**: {created_at}\n"
            response_text += f"   - **Modified**: {modified_at}\n\n"
            
            if properties:
                response_text += f"📋 **Custom Properties:**\n"
                for key, value in properties.items():
                    response_text += f"   - **{key}**: {value}\n"
                response_text += f"\n"
            
            response_text += f">> **Available Actions:**\n"
            response_text += f"• **Update**: Use update_node_properties to modify metadata\n"
            response_text += f"• **Download**: Use download_document (if file)\n"
            response_text += f"• **Browse**: Use browse_repository (if folder)\n"
            response_text += f"• **Delete**: Use delete_node to remove\n"
            
            return response_text
        else:
            return f"❌ Failed to retrieve properties for node `{node_id}`"
            
    except Exception as e:
        return f"❌ Properties formatting failed: {str(e)}"


def format_version_operation_result(
    operation_result: Dict[str, Any],
    operation_name: str
) -> str:
    """
    Format version operations (checkout/checkin/cancel) for MCP compatibility.
    """
    try:
        node_id = operation_result.get('node_id', 'Unknown')
        status = operation_result.get('status', 'Unknown')
        
        if operation_name == "checkout":
            if operation_result.get('locked', False):
                response_text = f"🔒 **Document Checked Out Successfully!**\n\n"
                response_text += f"📄 **Document ID**: `{node_id}`\n"
                response_text += f"🔐 **Status**: Locked for editing\n\n"
                response_text += f">> **Next steps:**\n"
                response_text += f"• **Edit**: Document is now locked for your changes\n"
                response_text += f"• **Checkin**: Use checkin_document to save changes\n"
                response_text += f"• **Cancel**: Use cancel_checkout to discard changes\n"
            else:
                response_text = f"⚠️ **Checkout Status**: {status}\n\n"
                response_text += f"📄 **Document ID**: `{node_id}`\n"
                if 'error' in operation_result:
                    response_text += f"❌ **Issue**: {operation_result['error']}\n"
        
        elif operation_name == "checkin":
            response_text = f"💾 **Document Checked In Successfully!**\n\n"
            response_text += f"📄 **Document ID**: `{node_id}`\n"
            response_text += f"📋 **Status**: {status}\n"
            if operation_result.get('major_version'):
                response_text += f"🔢 **Version**: Major version created\n"
            if operation_result.get('comment'):
                response_text += f"💬 **Comment**: {operation_result['comment']}\n"
            response_text += f"\n>> **Document is now available for others to edit**\n"
        
        elif operation_name == "cancel_checkout":
            if operation_result.get('unlocked', False):
                response_text = f"🚫 **Checkout Cancelled Successfully!**\n\n"
                response_text += f"📄 **Document ID**: `{node_id}`\n"
                response_text += f"🔓 **Status**: Document unlocked\n\n"
                response_text += f">> **Changes discarded - document is available for others**\n"
            else:
                response_text = f"⚠️ **Cancel Checkout Status**: {status}\n\n"
                response_text += f"📄 **Document ID**: `{node_id}`\n"
                if 'error' in operation_result:
                    response_text += f"❌ **Issue**: {operation_result['error']}\n"
                elif 'message' in operation_result:
                    response_text += f"ℹ️ **Info**: {operation_result['message']}\n"
        
        return response_text
        
    except Exception as e:
        return f"❌ Version operation formatting failed: {str(e)}"


def format_discovery_result(
    discovery_result: Any
) -> str:
    """
    Format repository discovery/info results for MCP compatibility.
    """
    try:
        if discovery_result and hasattr(discovery_result, 'entry'):
            repo_info = discovery_result.entry
            version = getattr(repo_info, 'version', {})
            
            if hasattr(version, 'display'):
                display_name = version.display
            else:
                display_name = getattr(version, 'display', 'Unknown')
            
            response_text = f"🏛️ **Alfresco Repository Information**\n\n"
            response_text += f"📋 **Version**: {display_name}\n"
            response_text += f"🌐 **Status**: Connected and accessible\n"
            response_text += f"🔧 **API**: REST API operational\n\n"
            response_text += f">> **Available Operations:**\n"
            response_text += f"• **Browse**: Use browse_repository to explore content\n"
            response_text += f"• **Search**: Use search_content to find documents\n"
            response_text += f"• **Upload**: Use upload_document to add files\n"
            response_text += f"• **Manage**: Full content management operations available\n"
            
            return response_text
        else:
            return f"❌ Unable to retrieve repository information"
            
    except Exception as e:
        return f"❌ Discovery formatting failed: {str(e)}"


def format_delete_result(
    delete_result: Any,
    node_id: str
) -> str:
    """
    Format node deletion results for MCP compatibility.
    """
    try:
        if delete_result:
            if isinstance(delete_result, dict):
                deleted = delete_result.get('deleted', True)
                permanent = delete_result.get('permanent', False)
            else:
                deleted = True
                permanent = False
            
            if deleted:
                if permanent:
                    response_text = f"🗑️ **Document Permanently Deleted!**\n\n"
                    response_text += f"📄 **Document ID**: `{node_id}`\n"
                    response_text += f"⚠️ **Warning**: This action cannot be undone\n"
                else:
                    response_text = f"🗂️ **Document Moved to Trash**\n\n"
                    response_text += f"📄 **Document ID**: `{node_id}`\n"
                    response_text += f"♻️ **Status**: Can be restored from trash\n\n"
                    response_text += f">> **Recovery:**\n"
                    response_text += f"• Documents in trash can be restored via Alfresco Share UI\n"
                    response_text += f"• Access trash at: http://localhost:8080/share (if available)\n"
                
                return response_text
            else:
                return f"❌ Failed to delete document `{node_id}`"
        else:
            return f"❌ Delete operation failed for `{node_id}`"
            
    except Exception as e:
        return f"❌ Delete formatting failed: {str(e)}"


def format_download_result(
    download_content: Any,
    node_id: str
) -> str:
    """
    Format download results for MCP compatibility.
    """
    try:
        if download_content and isinstance(download_content, bytes):
            content_size = len(download_content)
            
            # Format file size
            if content_size < 1024:
                size_str = f"{content_size} bytes"
            elif content_size < 1024 * 1024:
                size_str = f"{content_size / 1024:.1f} KB"
            else:
                size_str = f"{content_size / (1024 * 1024):.1f} MB"
            
            response_text = f"📥 **Document Downloaded Successfully!**\n\n"
            response_text += f"📄 **Document ID**: `{node_id}`\n"
            response_text += f"📏 **Size**: {size_str}\n"
            response_text += f"💾 **Content**: Retrieved to memory\n\n"
            response_text += f">> **Content Ready:**\n"
            response_text += f"• File content has been downloaded and is available\n"
            response_text += f"• Use appropriate tools to process the content\n"
            response_text += f"• Content is in binary format ({content_size:,} bytes)\n"
            
            return response_text
        else:
            return f"❌ Failed to download document `{node_id}`"
            
    except Exception as e:
        return f"❌ Download formatting failed: {str(e)}"


# Export all formatters
__all__ = [
    'format_search_results',
    'format_browse_results', 
    'format_upload_result',
    'format_folder_creation_result',
    'format_node_properties_result',
    'format_version_operation_result',
    'format_discovery_result',
    'format_delete_result',
    'format_download_result'
] 