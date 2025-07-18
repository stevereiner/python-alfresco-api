"""
Version utility functions for the Alfresco API.

This module provides convenient utility functions for document versioning operations
that MCP servers and other applications need, using authenticated HTTP client
patterns that won't be overwritten by codegen.
"""

from typing import Optional, Dict, Any, Union
from pathlib import Path
import json

from python_alfresco_api.clients.core import AlfrescoCoreClient


def checkout_document(
    core_client: AlfrescoCoreClient,
    node_id: str
) -> Dict[str, Any]:
    """
    Checkout (lock) a document for editing.
    
    Args:
        core_client: The v1.1 hierarchical core client
        node_id: ID of the document to checkout
        
    Returns:
        Checkout response with lock details
        
    Examples:
        >>> # Lock document for editing
        >>> result = checkout_document(core_client, "doc-123")
        >>> print(f"Locked: {result['locked']}")
    """
    # Get authenticated HTTP client
    http_client = core_client._get_raw_client().get_httpx_client()
    
    # Build URL for lock operation
    base_url = core_client._client_factory.base_url
    url = f"{base_url}/alfresco/api/-default-/public/alfresco/versions/1/nodes/{node_id}/lock"
    
    # Prepare lock body
    lock_body = {
        "type": "ALLOW_OWNER_CHANGES"
    }
    
    # Lock the document
    response = http_client.post(url, json=lock_body)
    
    # Handle response
    if response.status_code == 200:
        # Successfully locked
        return {
            "node_id": node_id,
            "locked": True,
            "status": "locked"
        }
    elif response.status_code == 423:
        # Already locked
        return {
            "node_id": node_id,
            "locked": False,
            "status": "already_locked",
            "error": "Document is already locked by another user"
        }
    elif response.status_code == 405:
        # Lock not supported
        return {
            "node_id": node_id,
            "locked": False,
            "status": "no_lock_support",
            "error": "Server doesn't support document locking"
        }
    else:
        # Other error
        response.raise_for_status()
        return {
            "node_id": node_id,
            "locked": False,
            "status": "error"
        }


def cancel_checkout(
    core_client: AlfrescoCoreClient,
    node_id: str
) -> Dict[str, Any]:
    """
    Cancel checkout (unlock) a document without creating a version.
    
    Args:
        core_client: The v1.1 hierarchical core client
        node_id: ID of the document to unlock
        
    Returns:
        Cancel checkout response with unlock details
        
    Examples:
        >>> # Unlock document without saving changes
        >>> result = cancel_checkout(core_client, "doc-123")
        >>> print(f"Unlocked: {result['unlocked']}")
    """
    # Get authenticated HTTP client
    http_client = core_client._get_raw_client().get_httpx_client()
    
    # Build URL for unlock operation
    base_url = core_client._client_factory.base_url
    url = f"{base_url}/alfresco/api/-default-/public/alfresco/versions/1/nodes/{node_id}/unlock"
    
    # Unlock the document
    response = http_client.post(url)
    
    # Handle response
    if response.status_code == 200:
        # Successfully unlocked
        return {
            "node_id": node_id,
            "unlocked": True,
            "status": "unlocked"
        }
    elif response.status_code == 409:
        # Not locked or can't unlock
        return {
            "node_id": node_id,
            "unlocked": False,
            "status": "not_locked",
            "error": "Document is not locked or cannot be unlocked"
        }
    elif response.status_code == 422:
        # Document is already unlocked (unprocessable entity)
        return {
            "node_id": node_id,
            "unlocked": True,
            "status": "already_unlocked",
            "message": "Document is already unlocked"
        }
    elif response.status_code == 405:
        # Unlock not supported
        return {
            "node_id": node_id,
            "unlocked": False,
            "status": "no_unlock_support",
            "error": "Server doesn't support document unlocking"
        }
    else:
        # Other error
        response.raise_for_status()
        return {
            "node_id": node_id,
            "unlocked": False,
            "status": "error"
        }


def checkin_document(
    core_client: AlfrescoCoreClient,
    node_id: str,
    content_file: Optional[Union[str, Path]] = None,
    content_bytes: Optional[bytes] = None,
    comment: Optional[str] = None,
    major_version: bool = False
) -> Dict[str, Any]:
    """
    Checkin a document (create new version and unlock).
    
    Args:
        core_client: The v1.1 hierarchical core client
        node_id: ID of the document to checkin
        content_file: Optional path to new content file
        content_bytes: Optional new content as bytes
        comment: Optional version comment
        major_version: Whether to create major version
        
    Returns:
        Checkin response with version details
        
    Examples:
        >>> # Checkin with new content
        >>> result = checkin_document(
        ...     core_client, 
        ...     "doc-123", 
        ...     content_file="updated.pdf",
        ...     comment="Updated content"
        ... )
        >>> 
        >>> # Checkin current content as major version
        >>> result = checkin_document(
        ...     core_client,
        ...     "doc-123",
        ...     major_version=True,
        ...     comment="Major update"
        ... )
    """
    # If new content is provided, update it first
    if content_file or content_bytes:
        from . import content_utils
        
        if content_file:
            # Update from file
            content_utils.update_content(
                core_client=core_client,
                node_id=node_id,
                file_path=content_file,
                major_version=major_version,
                comment=comment
            )
        elif content_bytes is not None:
            # Update from bytes
            content_utils.update_content(
                core_client=core_client,
                node_id=node_id,
                file_path=content_bytes,
                major_version=major_version,
                comment=comment
            )
        
        # After content update, unlock if possible
        unlock_result = cancel_checkout(core_client, node_id)
        
        return {
            "node_id": node_id,
            "checked_in": True,
            "status": "content_updated",
            "major_version": major_version,
            "comment": comment or "No comment",
            "unlocked": unlock_result.get("unlocked", False)
        }
    else:
        # Just unlock without content changes (simple checkin)
        unlock_result = cancel_checkout(core_client, node_id)
        
        return {
            "node_id": node_id,
            "checked_in": True,
            "status": "unlocked_only",
            "major_version": False,
            "comment": comment or "No content changes",
            "unlocked": unlock_result.get("unlocked", False)
        }


def get_version_history(
    core_client: AlfrescoCoreClient,
    node_id: str,
    include_content: bool = False
) -> Dict[str, Any]:
    """
    Get version history for a document.
    
    Args:
        core_client: The v1.1 hierarchical core client
        node_id: ID of the document
        include_content: Whether to include content info for each version
        
    Returns:
        Version history information
    """
    # Get authenticated HTTP client
    http_client = core_client._get_raw_client().get_httpx_client()
    
    # Build URL for versions
    base_url = core_client._client_factory.base_url
    url = f"{base_url}/alfresco/api/-default-/public/alfresco/versions/1/nodes/{node_id}/versions"
    
    # Add include parameter if needed
    params = {}
    if include_content:
        params['include'] = 'content'
    
    # Get version history
    response = http_client.get(url, params=params)
    response.raise_for_status()
    
    return response.json()


def get_version_content(
    core_client: AlfrescoCoreClient,
    node_id: str,
    version_id: str,
    output_path: Optional[Union[str, Path]] = None
) -> Union[bytes, str]:
    """
    Download content of a specific version.
    
    Args:
        core_client: The v1.1 hierarchical core client
        node_id: ID of the document
        version_id: ID of the specific version
        output_path: Optional path to save file (if None, return content)
        
    Returns:
        File content as bytes if output_path is None, otherwise path where saved
    """
    # Get authenticated HTTP client
    http_client = core_client._get_raw_client().get_httpx_client()
    
    # Build URL for version content
    base_url = core_client._client_factory.base_url
    url = f"{base_url}/alfresco/api/-default-/public/alfresco/versions/1/nodes/{node_id}/versions/{version_id}/content"
    
    # Download version content
    response = http_client.get(url)
    response.raise_for_status()
    
    content = response.content
    
    if output_path:
        # Save to file
        output_path_obj = Path(output_path)
        output_path_obj.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path_obj, 'wb') as f:
            f.write(content)
        
        return str(output_path_obj)
    else:
        # Return content
        return content


def revert_to_version(
    core_client: AlfrescoCoreClient,
    node_id: str,
    version_id: str,
    comment: Optional[str] = None,
    major_version: bool = False
) -> Dict[str, Any]:
    """
    Revert document to a previous version.
    
    Args:
        core_client: The v1.1 hierarchical core client
        node_id: ID of the document
        version_id: ID of the version to revert to
        comment: Optional comment for the revert operation
        major_version: Whether to create major version for revert
        
    Returns:
        Revert operation result
    """
    # Get content of the target version
    old_content = get_version_content(core_client, node_id, version_id)
    
    # Update current document with old content
    from . import content_utils
    
    result = content_utils.update_content(
        core_client=core_client,
        node_id=node_id,
        file_path=old_content,
        major_version=major_version,
        comment=comment or f"Reverted to version {version_id}"
    )
    
    return {
        "node_id": node_id,
        "reverted_to": version_id,
        "status": "reverted",
        "major_version": major_version,
        "comment": comment or f"Reverted to version {version_id}"
    }


# Export all functions
__all__ = [
    'checkout_document',
    'cancel_checkout', 
    'checkin_document',
    'get_version_history',
    'get_version_content',
    'revert_to_version'
] 