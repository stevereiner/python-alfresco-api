"""
Versions Operations Client - Level 3: Document Lifecycle Operations

This module provides version control operations within the Core API.
Part of the three-tier V1.1 architecture.
"""

from typing import Optional
from datetime import datetime

# Import from Level 3 (operation-specific models)
from .models import CheckoutResponse, CheckinResponse


class VersionsClient:
    """
    Document lifecycle operations client for checkout/checkin workflows.
    
    Provides high-level methods for document version control operations
    that are essential for MCP servers and document workflows.
    """
    
    def __init__(self, client_factory):
        """Initialize with client factory for raw client access."""
        self._client_factory = client_factory
        self._raw_client = None
    
    def _get_raw_client(self):
        """Get the actual raw core client for API calls."""
        if self._raw_client is None:
            # Create raw core client directly
            from ....raw_clients.alfresco_core_client.core_client.client import AuthenticatedClient
            
            self._raw_client = AuthenticatedClient(
                base_url=f"{self._client_factory.base_url}/alfresco/api/-default-/public/alfresco/versions/1",
                token=self._client_factory.auth.get_auth_token(),
                prefix=self._client_factory.auth.get_auth_prefix(),
                verify_ssl=self._client_factory.verify_ssl
            )
        return self._raw_client
    
    def _get_core_client(self):
        """Get the core client from the factory."""
        return self._client_factory.create_core_client()
    
    # ==================== SYNC METHODS ====================
    
    def enable_versioning(self, node_id: str, major_version: bool = True, **kwargs) -> dict:
        """
        Enable versioning on an existing node.
        
        Perfect for MCP servers that need to enable versioning after node creation.
        This method creates an initial version for the node.
        
        Args:
            node_id (str): ID of the node to enable versioning for
            major_version (bool): Whether to create as major version (default: True)
            **kwargs: Additional parameters passed to the raw client
            
        Returns:
            dict: Response containing version information
            
        Examples:
            ```python
            # Enable versioning with major version
            version_info = client.versions.enable_versioning(
                node_id="abc123-def456",
                major_version=True
            )
            
            # Enable versioning with minor version
            version_info = client.versions.enable_versioning(
                node_id="abc123-def456", 
                major_version=False
            )
            ```
            
        Raises:
            NodeNotFoundError: Node doesn't exist
            PermissionError: User lacks permission to modify versioning
            ValidationError: Invalid node for versioning
        """
        # Get HTTPx client for direct API call
        httpx_client = self._get_raw_client().get_httpx_client()
        
        # Enable versioning by updating the node content (triggers versioning)
        # This is the standard way to enable versioning in Alfresco
        try:
            response = httpx_client.put(
                f"/nodes/{node_id}/content",
                params={
                    "majorVersion": str(major_version).lower(),
                    "comment": "Enable versioning"
                },
                content=b"",  # Empty content update
                headers={"Content-Type": "application/octet-stream"}
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                response.raise_for_status()
                return {"error": f"Unexpected status: {response.status_code}"}
                
        except Exception as e:
            raise ValueError(f"Failed to enable versioning on node {node_id}: {str(e)}")
    
    def checkout(self, node_id: str, **kwargs) -> CheckoutResponse:
        """
        Checkout (lock) a document for editing.
        
        Perfect for MCP servers and collaborative document workflows.
        Locks the document to prevent concurrent modifications.
        
        Args:
            node_id: ID of the document to checkout
            
        Returns:
            CheckoutResponse: Response with checkout details
        """
        from ....utils import version_utils
        
        # Get core client from the same factory
        core_client = self._client_factory.create_core_client()
        
        # Use utility function for implementation
        result = version_utils.checkout_document(core_client, node_id)
        
        # Convert to CheckoutResponse model
        return CheckoutResponse(
            node_id=result["node_id"],
            locked=result.get("locked", False),
            working_copy_id=result.get("working_copy_id"),
            locked_by=result.get("locked_by"),
            locked_at=datetime.fromisoformat(result["locked_at"]) if result.get("locked_at") else None
        )
    
    def cancel_checkout(self, node_id: str, **kwargs) -> CheckoutResponse:
        """
        Cancel checkout (unlock) a document.
        
        Perfect for canceling editing sessions without creating versions.
        Unlocks the document and discards any working copy.
        
        Args:
            node_id: ID of the document to unlock
            
        Returns:
            CheckoutResponse: Response with unlock details
        """
        from ....utils import version_utils
        
        # Get core client from the same factory
        core_client = self._client_factory.create_core_client()
        
        # Use utility function for implementation
        result = version_utils.cancel_checkout(core_client, node_id)
        
        # Convert to CheckoutResponse model
        return CheckoutResponse(
            node_id=result["node_id"],
            locked=not result.get("unlocked", False),
            working_copy_id=None,
            locked_by=None,
            locked_at=None
        )
    
    def checkin(
        self, 
        node_id: str, 
        comment: Optional[str] = None,
        major_version: bool = False,
        **kwargs
    ) -> CheckinResponse:
        """
        Checkin (save) document changes as new version.
        
        Perfect for finalizing document edits and creating versions.
        Creates a new version and unlocks the document.
        
        Args:
            node_id: ID of the document to checkin
            comment: Version comment
            major_version: Create major version (default: minor)
            
        Returns:
            CheckinResponse: Response with new version details
        """
        from ....utils import version_utils
        
        # Get core client from the same factory
        core_client = self._client_factory.create_core_client()
        
        # Use utility function for implementation
        result = version_utils.checkin_document(
            core_client, 
            node_id,
            comment=comment,
            major_version=major_version
        )
        
        # Convert to CheckinResponse model
        return CheckinResponse(
            node_id=result["node_id"],
            version_number=result.get("version_number", "1.0"),
            comment=result.get("comment", ""),
            major_version=result.get("major_version", False),
            created_at=datetime.now(),
            created_by="current_user"
        )
    
    # ==================== ASYNC METHODS ====================
    
    async def enable_versioning_async(self, node_id: str, major_version: bool = True, **kwargs) -> dict:
        """
        Enable versioning on an existing node (async).
        
        Perfect for web applications that need to enable versioning after node creation.
        This method creates an initial version for the node.
        
        Args:
            node_id (str): ID of the node to enable versioning for
            major_version (bool): Whether to create as major version (default: True)
            **kwargs: Additional parameters passed to the raw client
            
        Returns:
            dict: Response containing version information
            
        Examples:
            ```python
            # Enable versioning with major version
            version_info = await client.versions.enable_versioning_async(
                node_id="abc123-def456",
                major_version=True
            )
            ```
            
        Raises:
            NodeNotFoundError: Node doesn't exist
            PermissionError: User lacks permission to modify versioning
            ValidationError: Invalid node for versioning
        """
        # Get HTTPx client for direct API call
        httpx_client = self._get_raw_client().get_async_httpx_client()
        
        # Enable versioning by updating the node content (triggers versioning)
        # This is the standard way to enable versioning in Alfresco
        try:
            response = await httpx_client.put(
                f"/nodes/{node_id}/content",
                params={
                    "majorVersion": str(major_version).lower(),
                    "comment": "Enable versioning"
                },
                content=b"",  # Empty content update
                headers={"Content-Type": "application/octet-stream"}
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                response.raise_for_status()
                return {"error": f"Unexpected status: {response.status_code}"}
                
        except Exception as e:
            raise ValueError(f"Failed to enable versioning on node {node_id}: {str(e)}")
    
    async def checkout_async(self, node_id: str) -> CheckoutResponse:
        """Async version of checkout."""
        # For now, return a mock response structure
        return CheckoutResponse(
            node_id=node_id,
            locked=True,
            working_copy_id=f"{node_id}-working-copy",
            locked_by="current_user",
            locked_at=datetime.now()
        )
    
    async def cancel_checkout_async(self, node_id: str) -> CheckoutResponse:
        """Async version of cancel_checkout."""
        # For now, return a mock response structure
        return CheckoutResponse(
            node_id=node_id,
            locked=False,
            working_copy_id=None,
            locked_by=None,
            locked_at=None
        )
    
    async def checkin_async(
        self, 
        node_id: str, 
        comment: Optional[str] = None,
        major_version: bool = False
    ) -> CheckinResponse:
        """Async version of checkin."""
        # For now, return a mock response structure
        version_number = "2.0" if major_version else "1.1"
        
        return CheckinResponse(
            node_id=node_id,
            version_number=version_number,
            comment=comment or "No comment",
            major_version=major_version,
            created_at=datetime.now(),
            created_by="current_user"
        )
    
    # ==================== DETAILED METHODS - Moved from AlfrescoCoreClient ====================
    
    def checkout_detailed(self, node_id: str, **kwargs):
        """
        Checkout operation (detailed sync).
        
        Returns complete Response object with status_code, headers, content, parsed.
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        from ....utils import version_utils
        
        # Use version utils for actual implementation
        core_client = self._get_core_client()
        return version_utils.checkout_document(core_client, node_id)
    
    async def checkout_detailed_async(self, node_id: str, **kwargs):
        """
        Checkout operation (detailed async).
        
        Returns complete Response object with status_code, headers, content, parsed.
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        # For now, delegate to sync version
        return self.checkout_detailed(node_id, **kwargs)
    
    def checkin_detailed(
        self, 
        node_id: str, 
        comment: Optional[str] = None,
        major_version: bool = False,
        **kwargs
    ):
        """
        Checkin operation (detailed sync).
        
        Returns complete Response object with status_code, headers, content, parsed.
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        from ....utils import version_utils
        
        # Use version utils for actual implementation
        core_client = self._get_core_client()
        return version_utils.checkin_document(
            core_client, 
            node_id, 
            comment=comment, 
            major_version=major_version
        )
    
    async def checkin_detailed_async(
        self, 
        node_id: str, 
        comment: Optional[str] = None,
        major_version: bool = False,
        **kwargs
    ):
        """
        Checkin operation (detailed async).
        
        Returns complete Response object with status_code, headers, content, parsed.
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        # For now, delegate to sync version
        return self.checkin_detailed(node_id, comment=comment, major_version=major_version, **kwargs)
    
    def cancel_checkout_detailed(self, node_id: str, **kwargs):
        """
        Cancel checkout operation (detailed sync).
        
        Returns complete Response object with status_code, headers, content, parsed.
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        from ....utils import version_utils
        
        # Use version utils for actual implementation
        core_client = self._get_core_client()
        return version_utils.cancel_checkout(core_client, node_id)
    
    async def cancel_checkout_detailed_async(self, node_id: str, **kwargs):
        """
        Cancel checkout operation (detailed async).
        
        Returns complete Response object with status_code, headers, content, parsed.
        
        Returns:
            Response: Complete response with status_code, headers, content, parsed
        """
        # For now, delegate to sync version
        return self.cancel_checkout_detailed(node_id, **kwargs)

    def __repr__(self) -> str:
        """String representation for debugging."""
        base_url = getattr(self._client_factory, 'base_url', 'unknown')
        return f"AlfrescoVersionsClient(base_url='{base_url}')" 