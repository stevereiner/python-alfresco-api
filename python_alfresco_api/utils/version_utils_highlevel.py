"""
High-Level Version Utilities for Alfresco API V1.1

This module provides convenient versioning operations using the V1.1 hierarchical
client architecture. Includes the core document versioning workflow:
- checkout_document_highlevel (lock for editing)
- checkin_document_highlevel (save new version and unlock)
- cancel_checkout_highlevel (discard changes and unlock)

Uses proven working methods from the V1.1 hierarchical architecture.
Perfect for MCP servers and applications that need document version control.
"""

import io
from typing import Optional, Dict, Any, List, Union
from datetime import datetime, timedelta
from pathlib import Path

from python_alfresco_api.clients.core import AlfrescoCoreClient


# =================================================================
# CORE DOCUMENT VERSIONING WORKFLOW
# =================================================================

def checkout_document_highlevel(
    core_client: AlfrescoCoreClient,
    node_id: str
) -> Any:
    """
    Checkout (lock) a document for editing using V1.1 hierarchical methods.
    
    This is the first step in the Alfresco document versioning workflow.
    Locks the document so only you can edit it.
    
    Args:
        core_client: The V1.1 hierarchical core client
        node_id: ID of the document to checkout
        
    Returns:
        Checkout response from V1.1 API
        
    Examples:
        >>> # Checkout document for editing
        >>> result = checkout_document_highlevel(core_client, "doc-123")
        >>> print(f"Document locked: {result}")
        
        >>> # Typical workflow
        >>> checkout_result = checkout_document_highlevel(core_client, "doc-123")
        >>> # ... make your changes ...
        >>> checkin_result = checkin_document_highlevel(core_client, "doc-123", comment="Updated content")
    """
    # Use the existing utility function that leverages V1.1 architecture
    from . import node_utils
    return node_utils.checkout_document(core_client, node_id)


def checkin_document_highlevel(
    core_client: AlfrescoCoreClient,
    node_id: str,
    content: Optional[Union[str, bytes, Path]] = None,
    comment: Optional[str] = None,
    major_version: bool = False
) -> Any:
    """
    Checkin (save) a document, creating a new version using V1.1 hierarchical methods.
    
    This is the final step in the Alfresco document versioning workflow.
    Creates a new version and unlocks the document for others to use.
    
    Args:
        core_client: The V1.1 hierarchical core client
        node_id: ID of the document to checkin
        content: Optional new content (file path, string, or bytes)
        comment: Optional version comment
        major_version: Create major version (True) or minor version (False)
        
    Returns:
        Checkin response from V1.1 API
        
    Examples:
        >>> # Simple checkin without content changes
        >>> result = checkin_document_highlevel(
        ...     core_client, 
        ...     "doc-123",
        ...     comment="Fixed typos"
        ... )
        
        >>> # Checkin with new content
        >>> result = checkin_document_highlevel(
        ...     core_client,
        ...     "doc-123", 
        ...     content="Updated document content",
        ...     comment="Major content update",
        ...     major_version=True
        ... )
        
        >>> # Checkin with file content
        >>> result = checkin_document_highlevel(
        ...     core_client,
        ...     "doc-123",
        ...     content=Path("updated_document.pdf"),
        ...     comment="Updated PDF with corrections"
        ... )
    """
    # Use the existing utility function that leverages V1.1 architecture
    from . import node_utils
    return node_utils.checkin_document(
        core_client=core_client,
        node_id=node_id,
        content=content,
        comment=comment,
        major_version=major_version
    )


def cancel_checkout_highlevel(
    core_client: AlfrescoCoreClient,
    node_id: str
) -> Any:
    """
    Cancel checkout (discard changes) using V1.1 hierarchical methods.
    
    This cancels the document checkout without creating a new version.
    Unlocks the document and discards any changes made during checkout.
    
    Args:
        core_client: The V1.1 hierarchical core client
        node_id: ID of the document to cancel checkout for
        
    Returns:
        Cancel checkout response from V1.1 API
        
    Examples:
        >>> # Cancel checkout and discard changes
        >>> result = cancel_checkout_highlevel(core_client, "doc-123")
        >>> print("Changes discarded, document unlocked")
        
        >>> # Error handling example
        >>> try:
        ...     result = cancel_checkout_highlevel(core_client, "doc-123")
        ... except Exception as e:
        ...     print(f"Failed to cancel checkout: {e}")
    """
    # Use the existing utility function that leverages V1.1 architecture
    from . import node_utils
    return node_utils.cancel_checkout(core_client, node_id)


# =================================================================
# DOCUMENT LOCKING OPERATIONS (for backward compatibility)
# =================================================================

def lock_document_highlevel(
    core_client: AlfrescoCoreClient,
    node_id: str,
    lock_type: str = "ALLOW_OWNER_CHANGES",
    time_to_expire: Optional[int] = 3600,
    include: Optional[List[str]] = None
) -> Any:
    """
    Lock a document using V1.1 hierarchical methods.
    
    Uses the proven working pattern: core_client.nodes.lock()
    
    Args:
        core_client: The V1.1 hierarchical core client
        node_id: ID of the document to lock
        lock_type: Type of lock ("ALLOW_OWNER_CHANGES", "FULL")
        time_to_expire: Lock expiration time in seconds (default: 1 hour)
        include: Optional include list for response
        
    Returns:
        Lock response from V1.1 API
        
    Examples:
        >>> # Lock document for editing
        >>> result = lock_document_highlevel(
        ...     core_client,
        ...     "doc-123",
        ...     lock_type="ALLOW_OWNER_CHANGES",
        ...     time_to_expire=7200  # 2 hours
        ... )
        >>> 
        >>> # Full lock (no one else can edit)
        >>> result = lock_document_highlevel(
        ...     core_client,
        ...     "doc-123", 
        ...     lock_type="FULL",
        ...     include=["isLocked"]
        ... )
    """
    # Build lock request using proven working pattern
    lock_request = {
        "type": lock_type
    }
    
    if time_to_expire is not None:
        lock_request["timeToExpire"] = str(time_to_expire)
    
    # Use the proven working V1.1 pattern
    return core_client.nodes.lock(
        node_id=node_id,
        request=lock_request,
        include=include
    )


def unlock_document_highlevel(
    core_client: AlfrescoCoreClient,
    node_id: str,
    include: Optional[List[str]] = None
) -> Any:
    """
    Unlock a document using V1.1 hierarchical methods.
    
    Uses the proven working pattern: core_client.nodes.unlock()
    
    Args:
        core_client: The V1.1 hierarchical core client
        node_id: ID of the document to unlock
        include: Optional include list for response
        
    Returns:
        Unlock response from V1.1 API
        
    Examples:
        >>> # Unlock document
        >>> result = unlock_document_highlevel(core_client, "doc-123")
        >>> 
        >>> # Unlock with additional info
        >>> result = unlock_document_highlevel(
        ...     core_client,
        ...     "doc-123",
        ...     include=["isLocked", "properties"]
        ... )
    """
    # Use the proven working V1.1 pattern
    return core_client.nodes.unlock(
        node_id=node_id,
        include=include
    )


# =================================================================
# VERSION INFORMATION AND STATUS
# =================================================================

def check_lock_status_highlevel(
    core_client: AlfrescoCoreClient,
    node_id: str
) -> Dict[str, Any]:
    """
    Check the lock status of a document using V1.1 hierarchical methods.
    
    Args:
        core_client: The V1.1 hierarchical core client
        node_id: ID of the document to check
        
    Returns:
        Dictionary with lock status information
        
    Examples:
        >>> # Check if document is locked
        >>> status = check_lock_status_highlevel(core_client, "doc-123")
        >>> if status["is_locked"]:
        ...     print(f"Locked by: {status['locked_by']}")
    """
    # Get node info with lock details
    node_info = core_client.nodes.get(
        node_id=node_id,
        include=["isLocked", "properties"]
    )
    
    entry = node_info.entry
    
    # Extract lock information
    lock_status = {
        'node_id': node_id,
        'name': entry.name,
        'is_locked': getattr(entry, 'isLocked', False),
        'locked_by': None,
        'lock_type': None,
        'lock_expiry': None,
        'can_unlock': False
    }
    
    # If locked, extract additional lock details from properties
    if hasattr(entry, 'properties') and entry.properties:
        props = entry.properties
        lock_status['locked_by'] = props.get('cm:lockOwner')
        lock_status['lock_type'] = props.get('cm:lockType')
        
        # Check if current user can unlock
        # This is a simplified check - in practice you'd compare with current user
        lock_status['can_unlock'] = True  # Assume user can unlock for now
    
    return lock_status


def get_version_history_highlevel(
    core_client: AlfrescoCoreClient,
    node_id: str,
    include: Optional[List[str]] = None,
    max_items: int = 100
) -> Any:
    """
    Get version history using V1.1 hierarchical methods.
    
    Args:
        core_client: The V1.1 hierarchical core client
        node_id: ID of the document
        include: Optional include list
        max_items: Maximum number of versions to retrieve
        
    Returns:
        Version history from Alfresco
        
    Examples:
        >>> # Get version history
        >>> history = get_version_history_highlevel(core_client, "doc-123")
        >>> for version in history.list.entries:
        ...     print(f"Version: {version.entry.id}")
    """
    # Use the existing utility function
    from . import version_utils
    return version_utils.get_version_history(
        core_client=core_client,
        node_id=node_id,
        include_content=bool(include and 'content' in include)
    )


# =================================================================
# ADVANCED VERSION OPERATIONS
# =================================================================

def create_version_with_content_highlevel(
    core_client: AlfrescoCoreClient,
    node_id: str,
    content: Union[str, bytes, io.BytesIO],
    version_comment: Optional[str] = None,
    major_version: bool = False,
    filename: Optional[str] = None,
    include: Optional[List[str]] = None
) -> Any:
    """
    Create a new version with content using V1.1 hierarchical methods.
    
    Combines lock + update_content + unlock for version control.
    
    Args:
        core_client: The V1.1 hierarchical core client
        node_id: ID of the document to version
        content: New content (string, bytes, or stream)
        version_comment: Comment for the new version
        major_version: Create as major version (True) or minor (False)
        filename: Optional new filename
        include: Optional include list for response
        
    Returns:
        Updated document with new version
        
    Examples:
        >>> # Create new version with text content
        >>> content = "Updated document content v2.0"
        >>> result = create_version_with_content_highlevel(
        ...     core_client,
        ...     "doc-123",
        ...     content,
        ...     version_comment="Added new features",
        ...     major_version=True
        ... )
        >>> 
        >>> # Create version from file bytes
        >>> with open("updated_doc.pdf", "rb") as f:
        ...     content = f.read()
        >>> result = create_version_with_content_highlevel(
        ...     core_client,
        ...     "doc-123",
        ...     content,
        ...     version_comment="Updated PDF with corrections"
        ... )
    """
    # Step 1: Checkout (lock) the document for editing
    checkout_result = checkout_document_highlevel(core_client, node_id)
    
    try:
        # Step 2: Update content using content utils
        from . import content_utils_highlevel
        
        # Convert content to appropriate format
        if isinstance(content, str):
            # Text content
            update_result = content_utils_highlevel.update_content_from_string_highlevel(
                core_client=core_client,
                node_id=node_id,
                content_text=content,
                filename=filename,
                include=include
            )
        elif isinstance(content, (bytes, io.BytesIO)):
            # Binary content or stream
            if isinstance(content, bytes):
                content_stream = io.BytesIO(content)
            else:
                content_stream = content
                
            update_result = content_utils_highlevel.update_content_from_stream_highlevel(
                core_client=core_client,
                node_id=node_id,
                content_stream=content_stream,
                filename=filename,
                include=include
            )
        else:
            raise ValueError(f"Unsupported content type: {type(content)}")
        
        # Step 3: Checkin (create version and unlock)
        checkin_result = checkin_document_highlevel(
            core_client=core_client,
            node_id=node_id,
            comment=version_comment,
            major_version=major_version
        )
        
        return checkin_result
        
    except Exception as e:
        # If anything fails, cancel checkout to unlock
        try:
            cancel_checkout_highlevel(core_client, node_id)
        except:
            pass  # Ignore cancel errors, focus on original error
        raise e


def revert_to_version_highlevel(
    core_client: AlfrescoCoreClient,
    node_id: str,
    version_id: str,
    version_comment: Optional[str] = None,
    major_version: bool = False
) -> Any:
    """
    Revert document to a previous version using V1.1 hierarchical methods.
    
    Downloads the old version content and creates a new version with that content.
    
    Args:
        core_client: The V1.1 hierarchical core client
        node_id: ID of the document
        version_id: ID of the version to revert to
        version_comment: Comment for the revert operation
        major_version: Create revert as major version
        
    Returns:
        Updated document with reverted content
        
    Examples:
        >>> # Revert to previous version
        >>> result = revert_to_version_highlevel(
        ...     core_client,
        ...     "doc-123",
        ...     "1.0",
        ...     version_comment="Reverted to stable version",
        ...     major_version=True
        ... )
    """
    # Use the existing utility function
    from . import version_utils
    return version_utils.revert_to_version(
        core_client=core_client,
        node_id=node_id,
        version_id=version_id,
        comment=version_comment,
        major_version=major_version
    )


def auto_version_document_highlevel(
    core_client: AlfrescoCoreClient,
    node_id: str,
    content: Union[str, bytes, io.BytesIO],
    auto_comment: bool = True,
    auto_major: bool = False,
    filename: Optional[str] = None
) -> Any:
    """
    Automatically version a document with smart defaults.
    
    Provides intelligent versioning with automatic comments and version numbering.
    
    Args:
        core_client: The V1.1 hierarchical core client
        node_id: ID of the document
        content: New content for the document
        auto_comment: Automatically generate version comment
        auto_major: Automatically determine if this should be a major version
        filename: Optional new filename
        
    Returns:
        Updated document with new version
        
    Examples:
        >>> # Auto-version with smart defaults
        >>> result = auto_version_document_highlevel(
        ...     core_client,
        ...     "doc-123",
        ...     "Updated content with new features"
        ... )
    """
    # Generate automatic comment if requested
    comment = None
    if auto_comment:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        comment = f"Auto-versioned on {timestamp}"
    
    # Auto-determine major version (simple heuristic)
    major_version = auto_major
    if auto_major and isinstance(content, str):
        # Simple heuristic: if content contains "major", "breaking", "v2", etc.
        major_keywords = ["major", "breaking", "v2.", "v3.", "release", "final"]
        content_lower = content.lower()
        major_version = any(keyword in content_lower for keyword in major_keywords)
    
    # Create version with content
    return create_version_with_content_highlevel(
        core_client=core_client,
        node_id=node_id,
        content=content,
        version_comment=comment,
        major_version=major_version,
        filename=filename
    )


# =================================================================
# OPERATION SUMMARY
# =================================================================

def list_version_operations_highlevel() -> List[str]:
    """
    List all available high-level version operations using V1.1 architecture.
    
    Returns:
        List of operation names including core versioning workflow
    """
    return [
        # Core document versioning workflow
        "checkout_document_highlevel",
        "checkin_document_highlevel", 
        "cancel_checkout_highlevel",
        
        # Document locking (backward compatibility)
        "lock_document_highlevel",
        "unlock_document_highlevel",
        "check_lock_status_highlevel",
        
        # Advanced version operations
        "get_version_history_highlevel",
        "create_version_with_content_highlevel",
        "revert_to_version_highlevel",
        "auto_version_document_highlevel"
    ] 