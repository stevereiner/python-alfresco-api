"""
AlfrescoSearchClient - Individual client for Alfresco SEARCH API

Wraps the generated HTTP client with enhanced functionality:
- Automatic authentication handling
- Pydantic model integration
- Async/sync support
- Error handling
"""

import sys
from pathlib import Path
from typing import Optional, Dict, Any

# Add raw client to path
raw_client_path = Path(__file__).parent.parent / "raw_clients" / "alfresco_search_client"
if raw_client_path.exists():
    # Find the actual package directory
    package_dirs = [d for d in raw_client_path.iterdir() if d.is_dir() and not d.name.startswith('.')]
    if package_dirs:
        sys.path.insert(0, str(package_dirs[0]))

class AlfrescoSearchClient:
    """
    Individual client for Alfresco SEARCH API.
    
    Features:
    - Uses generated HTTP client internally
    - Automatic authentication with AuthUtil
    - Pydantic model integration
    - Both sync and async methods
    """
    
    def __init__(
        self,
        base_url: str,
        auth_util: Optional[Any] = None,
        verify_ssl: bool = True,
        timeout: int = 30
    ):
        """
        Initialize search client.
        
        Args:
            base_url: Base URL of Alfresco instance
            auth_util: Optional AuthUtil instance for authentication
            verify_ssl: Whether to verify SSL certificates
            timeout: Request timeout in seconds
        """
        self.base_url = base_url.rstrip('/')
        self.auth_util = auth_util
        self.verify_ssl = verify_ssl
        self.timeout = timeout
        
        # Initialize the generated client
        self._init_generated_client()
    
    def _init_generated_client(self):
        """Initialize the generated HTTP client"""
        try:
            from client import Client
            self.client = Client(base_url=self.base_url)
            self._client_available = True
        except ImportError as e:
            print(f"⚠️  Generated client not available for search: {e}")
            self.client = None
            self._client_available = False
    
    def is_available(self) -> bool:
        """Check if the generated client is available"""
        return self._client_available
    
    async def _ensure_auth(self):
        """Ensure authentication before API calls"""
        if self.auth_util:
            await self.auth_util.ensure_authenticated()
    
    def get_client_info(self) -> Dict[str, Any]:
        """Get information about this client"""
        return {
            "api": "search",
            "base_url": self.base_url,
            "authenticated": self.auth_util.is_authenticated() if self.auth_util else False,
            "client_available": self._client_available
        }
