"""
Shared Authentication Utility

Provides authentication management that can be shared across multiple API clients.
Handles ticket-based authentication with automatic renewal.
"""

import asyncio
import base64
import os
from typing import Optional, Dict, Any, Union
from datetime import datetime, timedelta
import httpx

# Try to import python-dotenv for .env file support (optional)
try:
    from dotenv import load_dotenv
    DOTENV_AVAILABLE = True
except ImportError:
    DOTENV_AVAILABLE = False

def load_env_config(
    base_url: Optional[str] = None,
    username: Optional[str] = None,
    password: Optional[str] = None,
    verify_ssl: Optional[Union[bool, str]] = None,
    timeout: Optional[int] = None,
    load_env: bool = True,
    env_file: Optional[str] = None
) -> Dict[str, Any]:
    """
    Load configuration from environment variables and .env files.
    
    Priority: explicit parameters > environment variables > defaults
    
    Args:
        base_url: Explicit base URL (overrides env)
        username: Explicit username (overrides env) 
        password: Explicit password (overrides env)
        verify_ssl: SSL verification - True/False or path to certificate bundle (overrides env)
        timeout: Request timeout in seconds (overrides env)
        load_env: Whether to load from environment/.env file
        env_file: Specific .env file path
        
    Returns:
        Dict with resolved configuration values
    """
    # Load .env file if available and requested
    if load_env and DOTENV_AVAILABLE:
        if env_file:
            load_dotenv(env_file)
        else:
            load_dotenv()  # Loads .env from current directory
    
    # Priority: explicit parameters > environment variables > defaults
    resolved_base_url = base_url or os.getenv('ALFRESCO_URL') or os.getenv('ALFRESCO_BASE_URL') or 'http://localhost:8080'
    resolved_username = username or os.getenv('ALFRESCO_USERNAME') or 'admin'
    resolved_password = password or os.getenv('ALFRESCO_PASSWORD') or 'admin'
    
    # Handle timeout with environment variable support
    if timeout is not None:
        resolved_timeout = timeout
    else:
        timeout_env = os.getenv('ALFRESCO_TIMEOUT')
        if timeout_env:
            try:
                resolved_timeout = int(timeout_env)
            except ValueError:
                resolved_timeout = None  # Invalid value, don't set timeout
        else:
            resolved_timeout = None  # No timeout specified, let system/client defaults apply
    
    # Handle SSL verification (supports bool or certificate path like raw client)
    if verify_ssl is not None:
        resolved_verify_ssl = verify_ssl
    else:
        ssl_env = os.getenv('ALFRESCO_VERIFY_SSL') or os.getenv('ALFRESCO_SSL_VERIFY') or 'true'
        # Support raw client SSL modes: True, False, or certificate path
        if ssl_env.lower() in ('false', '0', 'no', 'off'):
            resolved_verify_ssl = False
        elif ssl_env.lower() in ('true', '1', 'yes', 'on'):
            resolved_verify_ssl = True
        else:
            # Assume it's a certificate path
            resolved_verify_ssl = ssl_env
    
    return {
        'base_url': resolved_base_url,
        'username': resolved_username,
        'password': resolved_password,
        'verify_ssl': resolved_verify_ssl,
        'timeout': resolved_timeout
    }

class SimpleAuthUtil:
    """
    Simple authentication utility using Basic authentication.
    
    This is the proven working implementation that the MCP server uses.
    Provides reliable Basic authentication for inheritance-based clients.
    """
    
    def __init__(self, username: str, password: str):
        """
        Initialize simple auth utility.
        
        Args:
            username: Alfresco username
            password: Alfresco password
        """
        self.username = username
        self.password = password
    
    def get_basic_auth_header(self):
        """Get basic auth header for HTTP requests."""
        auth_string = f"{self.username}:{self.password}"
        auth_b64 = base64.b64encode(auth_string.encode()).decode()
        return f'Basic {auth_b64}'
    
    def get_auth_token(self):
        """Get just the base64 auth token (without 'Basic ' prefix) for AuthenticatedClient."""
        auth_string = f"{self.username}:{self.password}"
        return base64.b64encode(auth_string.encode()).decode()
    
    def get_auth_prefix(self):
        """Get the authentication prefix for this auth type."""
        return "Basic"
    
    def is_authenticated(self):
        return True  # Simple auth is always "authenticated"
    
    async def ensure_authenticated(self):
        return True  # Simple auth is always ready

class AuthUtil:
    """
    Shared authentication utility for Alfresco APIs.
    
    Handles ticket-based authentication with automatic renewal.
    Can be shared across multiple API clients.
    """
    
    def __init__(
        self,
        base_url: str,
        username: str,
        password: str,
        verify_ssl: Union[bool, str] = True,
        timeout: Optional[int] = None
    ):
        """
        Initialize authentication utility.
        
        Args:
            base_url: Base URL of Alfresco instance
            username: Alfresco username
            password: Alfresco password
            verify_ssl: SSL verification - True, False, or path to certificate bundle
            timeout: Request timeout in seconds (None = use system defaults)
        """
        self.base_url = base_url.rstrip('/')
        self.username = username
        self.password = password
        self.verify_ssl = verify_ssl
        self.timeout = timeout
        
        self.ticket = None
        self.ticket_expires = None
        self._authenticated = False
    
    async def authenticate(self) -> bool:
        """
        Authenticate with Alfresco and get ticket using direct HTTP request.
        
        This uses the WORKING authentication method discovered in test_working_api.py.
        Uses direct HTTP requests instead of raw clients to avoid header auth issues.
        
        Returns:
            True if authentication successful, False otherwise
        """
        try:
            # Use direct HTTP approach like the working test code
            auth_url = f"{self.base_url}/alfresco/api/-default-/public/authentication/versions/1/tickets"
            auth_data = {"userId": self.username, "password": self.password}
            
            # Create httpx client with timeout only if specified
            client_kwargs = {"verify": self.verify_ssl}
            if self.timeout is not None:
                client_kwargs["timeout"] = self.timeout
            
            async with httpx.AsyncClient(**client_kwargs) as client:
                response = await client.post(auth_url, json=auth_data)
                
                if response.status_code == 201:
                    ticket_data = response.json()
                    self.ticket = ticket_data["entry"]["id"]
                    # Tickets typically expire after 1 hour
                    self.ticket_expires = datetime.now() + timedelta(hours=1)
                    self._authenticated = True
                    return True
                else:
                    print(f"Authentication failed with status {response.status_code}: {response.text}")
                    
        except Exception as e:
            print(f"Authentication failed: {e}")
            self._authenticated = False
        
        return False
    
    def is_authenticated(self) -> bool:
        """Check if currently authenticated with valid ticket"""
        if not self._authenticated or not self.ticket:
            return False
        
        if self.ticket_expires and datetime.now() >= self.ticket_expires:
            self._authenticated = False
            return False
        
        return True
    
    def get_auth_headers(self) -> Dict[str, str]:
        """Get authentication headers for API requests"""
        if not self.is_authenticated() or not self.ticket:
            return {}
        
        return {
            "X-Alfresco-Ticket": self.ticket
        }
    
    async def ensure_authenticated(self) -> bool:
        """Ensure we have valid authentication, refresh if needed"""
        if self.is_authenticated():
            return True
        
        return await self.authenticate()
    
    def get_basic_auth_header(self):
        """Get basic auth header for compatibility with SimpleAuthUtil interface"""
        auth_string = f"{self.username}:{self.password}"
        auth_b64 = base64.b64encode(auth_string.encode()).decode()
        return f'Basic {auth_b64}'
    
    def get_auth_token(self):
        """Get just the base64 auth token (without 'Basic ' prefix) for AuthenticatedClient."""
        auth_string = f"{self.username}:{self.password}"
        return base64.b64encode(auth_string.encode()).decode()
    
    def get_auth_prefix(self):
        """Get authentication prefix for headers. AuthUtil uses Basic auth."""
        return "Basic"
    
    def add_auth_params(self, url: str) -> str:
        """
        Add authentication parameters to URL (query parameter method).
        
        This is the WORKING authentication method for this Alfresco instance.
        Uses alf_ticket={ticket} as query parameter instead of headers.
        
        Args:
            url: Base URL to add authentication to
            
        Returns:
            URL with authentication parameters added
        """
        if not self.is_authenticated() or not self.ticket:
            # No authentication available, return original URL
            return url
        
        # Add ticket as query parameter
        separator = "&" if "?" in url else "?"
        return f"{url}{separator}alf_ticket={self.ticket}"

class TicketAuthUtil:
    """
    Enhanced authentication utility with direct ticket support.
    Handles both Basic auth and ticket-based authentication.
    """
    
    def __init__(self, username: str, password: str, base_url: str = ""):
        """
        Initialize ticket auth utility.
        
        Args:
            username: Alfresco username
            password: Alfresco password  
            base_url: Base URL for Alfresco (optional, for future ticket API calls)
        """
        self.username = username
        self.password = password
        self.base_url = base_url.rstrip('/')
        self.ticket = None
        self._authenticated = False
    
    def get_basic_auth_header(self):
        """Get basic auth header for initial authentication."""
        auth_string = f"{self.username}:{self.password}"
        auth_b64 = base64.b64encode(auth_string.encode()).decode()
        return f'Basic {auth_b64}'
    
    def get_auth_token(self):
        """Get just the base64 auth token (without 'Basic ' prefix) for AuthenticatedClient."""
        auth_string = f"{self.username}:{self.password}"
        return base64.b64encode(auth_string.encode()).decode()
    
    def get_ticket_header(self):
        """Get ticket auth header if we have a ticket."""
        if self.ticket:
            return f'Basic {base64.b64encode(self.ticket.encode()).decode()}'
        return self.get_basic_auth_header()
    
    def get_auth_header(self):
        """Get the appropriate auth header (ticket preferred, basic fallback)."""
        return self.get_ticket_header()
    
    def get_auth_prefix(self):
        """Get authentication prefix for headers. TicketAuthUtil uses Basic auth."""
        return "Basic"
    
    def store_ticket_from_response(self, response_data):
        """
        Store ticket from authentication response.
        
        Args:
            response_data: Response from create_ticket API call
        """
        if hasattr(response_data, 'entry') and hasattr(response_data.entry, 'id'):
            self.ticket = response_data.entry.id
            self._authenticated = True
        elif isinstance(response_data, dict) and 'entry' in response_data:
            if 'id' in response_data['entry']:
                self.ticket = response_data['entry']['id'] 
                self._authenticated = True
    
    def is_authenticated(self):
        """Check if we have a valid ticket."""
        return self._authenticated and self.ticket is not None

class OAuth2AuthUtil:
    """
    OAuth2 authentication utility for enterprise environments.
    
    Supports multiple OAuth2 flows while maintaining the same interface
    as other auth utilities for seamless integration.
    """
    
    def __init__(
        self,
        base_url: str,
        client_id: str,
        client_secret: Optional[str] = None,
        token_endpoint: Optional[str] = None,
        authorization_endpoint: Optional[str] = None,
        # OAuth2 flow configuration
        grant_type: str = "client_credentials",  # or "authorization_code"
        scope: Optional[str] = None,
        redirect_uri: Optional[str] = None,
        # Token management
        access_token: Optional[str] = None,
        refresh_token: Optional[str] = None,
        # Standard auth util parameters
        verify_ssl: Union[bool, str] = True,
        timeout: Optional[int] = None,
        # Environment loading
        load_env: bool = True,
        env_file: Optional[str] = None
    ):
        """
        Initialize OAuth2 authentication utility.
        
        Args:
            base_url: Alfresco server base URL
            client_id: OAuth2 client identifier
            client_secret: OAuth2 client secret (for confidential clients)
            token_endpoint: OAuth2 token endpoint URL
            authorization_endpoint: OAuth2 authorization endpoint URL (for auth code flow)
            grant_type: OAuth2 grant type ("client_credentials", "authorization_code", "refresh_token")
            scope: Requested OAuth2 scopes
            redirect_uri: Redirect URI for authorization code flow
            access_token: Existing access token (optional)
            refresh_token: Existing refresh token (optional)
            verify_ssl: SSL verification - True, False, or path to certificate bundle
            timeout: Request timeout in seconds (None = use system defaults)
            load_env: Whether to load configuration from environment
            env_file: Optional path to .env file
        """
        # Load configuration from environment if needed
        config = load_env_config(
            base_url=base_url,
            username=None,  # Not used for OAuth2
            password=None,  # Not used for OAuth2
            verify_ssl=verify_ssl,
            load_env=load_env,
            env_file=env_file
        )
        
        self.base_url = config['base_url'].rstrip('/')
        self.client_id = client_id
        self.client_secret = client_secret
        self.verify_ssl = config['verify_ssl']
        self.timeout = timeout
        
        # OAuth2 flow configuration
        self.grant_type = grant_type
        self.scope = scope
        self.redirect_uri = redirect_uri
        
        # Token endpoints - smart defaults for common providers
        self.token_endpoint = token_endpoint or self._detect_token_endpoint()
        self.authorization_endpoint = authorization_endpoint
        
        # Token state
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.token_expires = None
        self._authenticated = False
        
        # For environment variable loading
        self._load_oauth_env_config(load_env, env_file)
    
    def _load_oauth_env_config(self, load_env: bool, env_file: Optional[str]):
        """Load OAuth2-specific configuration from environment."""
        if not load_env:
            return
            
        if DOTENV_AVAILABLE:
            if env_file:
                from dotenv import load_dotenv
                load_dotenv(env_file)
            else:
                from dotenv import load_dotenv
                load_dotenv()
        
        # Load OAuth2 environment variables
        self.client_id = self.client_id or os.getenv('OAUTH2_CLIENT_ID') or os.getenv('ALFRESCO_OAUTH2_CLIENT_ID')
        self.client_secret = self.client_secret or os.getenv('OAUTH2_CLIENT_SECRET') or os.getenv('ALFRESCO_OAUTH2_CLIENT_SECRET')
        self.token_endpoint = self.token_endpoint or os.getenv('OAUTH2_TOKEN_ENDPOINT') or os.getenv('ALFRESCO_OAUTH2_TOKEN_ENDPOINT')
        self.scope = self.scope or os.getenv('OAUTH2_SCOPE') or os.getenv('ALFRESCO_OAUTH2_SCOPE')
        
        # Existing tokens from environment
        self.access_token = self.access_token or os.getenv('OAUTH2_ACCESS_TOKEN') or os.getenv('ALFRESCO_OAUTH2_ACCESS_TOKEN')
        self.refresh_token = self.refresh_token or os.getenv('OAUTH2_REFRESH_TOKEN') or os.getenv('ALFRESCO_OAUTH2_REFRESH_TOKEN')
    
    def _detect_token_endpoint(self) -> Optional[str]:
        """Smart detection of token endpoints for common providers."""
        if not self.base_url:
            return None
            
        # Common Alfresco OAuth2 patterns
        alfresco_patterns = [
            f"{self.base_url}/alfresco/service/oauth2/token",
            f"{self.base_url}/auth/oauth/token", 
            f"{self.base_url}/oauth2/token"
        ]
        
        # For cloud/enterprise environments, often separate auth servers
        if "cloud" in self.base_url.lower() or "enterprise" in self.base_url.lower():
            return None  # Require explicit configuration
            
        # Return most common pattern for on-premise
        return alfresco_patterns[0]
    
    async def authenticate(self) -> bool:
        """
        Authenticate using OAuth2 flow and obtain access token.
        
        Returns:
            True if authentication successful, False otherwise
        """
        try:
            if self.grant_type == "client_credentials":
                return await self._client_credentials_flow()
            elif self.grant_type == "refresh_token" and self.refresh_token:
                return await self._refresh_token_flow()
            elif self.grant_type == "authorization_code":
                # This typically requires user interaction, so we just validate existing token
                return self.is_authenticated()
            else:
                raise ValueError(f"Unsupported grant type: {self.grant_type}")
                
        except Exception as e:
            print(f"OAuth2 authentication failed: {e}")
            self._authenticated = False
            return False
    
    async def _client_credentials_flow(self) -> bool:
        """Execute OAuth2 client credentials flow."""
        if not self.client_id or not self.client_secret or not self.token_endpoint:
            raise ValueError(
                "Client credentials flow requires client_id, client_secret, and token_endpoint"
            )
        
        data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        
        if self.scope:
            data["scope"] = self.scope
        
        # Create httpx client with timeout only if specified
        client_kwargs = {"verify": self.verify_ssl}
        if self.timeout is not None:
            client_kwargs["timeout"] = self.timeout
        
        async with httpx.AsyncClient(**client_kwargs) as client:
            response = await client.post(
                self.token_endpoint,
                data=data,
                headers={"Content-Type": "application/x-www-form-urlencoded"}
            )
            
            if response.status_code == 200:
                token_data = response.json()
                self.access_token = token_data.get("access_token")
                
                # Handle token expiration
                expires_in = token_data.get("expires_in")
                if expires_in:
                    self.token_expires = datetime.now() + timedelta(seconds=expires_in)
                
                # Store refresh token if provided
                if "refresh_token" in token_data:
                    self.refresh_token = token_data["refresh_token"]
                
                self._authenticated = True
                return True
        
        return False
    
    async def _refresh_token_flow(self) -> bool:
        """Refresh access token using refresh token."""
        if not self.refresh_token or not self.token_endpoint:
            return False
        
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
            "client_id": self.client_id
        }
        
        if self.client_secret:
            data["client_secret"] = self.client_secret
        
        # Create httpx client with timeout only if specified
        client_kwargs = {"verify": self.verify_ssl}
        if self.timeout is not None:
            client_kwargs["timeout"] = self.timeout
        
        async with httpx.AsyncClient(**client_kwargs) as client:
            response = await client.post(
                self.token_endpoint,
                data=data,
                headers={"Content-Type": "application/x-www-form-urlencoded"}
            )
            
            if response.status_code == 200:
                token_data = response.json()
                self.access_token = token_data.get("access_token")
                
                # Update expiration
                expires_in = token_data.get("expires_in")
                if expires_in:
                    self.token_expires = datetime.now() + timedelta(seconds=expires_in)
                
                # Update refresh token if provided
                if "refresh_token" in token_data:
                    self.refresh_token = token_data["refresh_token"]
                
                self._authenticated = True
                return True
        
        return False
    
    def is_authenticated(self) -> bool:
        """Check if currently authenticated with valid access token."""
        if not self._authenticated or not self.access_token:
            return False
        
        # Check token expiration
        if self.token_expires and datetime.now() >= self.token_expires:
            self._authenticated = False
            return False
        
        return True
    
    def get_auth_headers(self) -> Dict[str, str]:
        """Get authentication headers for API requests."""
        if not self.is_authenticated():
            return {}
        
        return {
            "Authorization": f"Bearer {self.access_token}"
        }
    
    def get_basic_auth_header(self):
        """Compatibility method - returns Bearer token as auth header."""
        if self.is_authenticated():
            return f"Bearer {self.access_token}"
        return ""
    
    def get_auth_token(self):
        """Get just the access token (without 'Bearer ' prefix) for AuthenticatedClient."""
        if self.is_authenticated():
            return self.access_token
        return ""
    
    def get_auth_prefix(self):
        """Get authentication prefix for headers. OAuth2AuthUtil uses Bearer tokens."""
        return "Bearer"
    
    async def ensure_authenticated(self) -> bool:
        """Ensure we have valid authentication, refresh if needed."""
        if self.is_authenticated():
            return True
        
        # Try refresh token first if available
        if self.refresh_token:
            if await self._refresh_token_flow():
                return True
        
        # Fall back to main authentication flow
        return await self.authenticate()
    
    @classmethod
    def from_env(
        cls,
        base_url: Optional[str] = None,
        env_file: Optional[str] = None,
        grant_type: str = "client_credentials",
        **kwargs
    ):
        """
        Create OAuth2AuthUtil from environment variables.
        
        Expected environment variables:
        - OAUTH2_CLIENT_ID or ALFRESCO_OAUTH2_CLIENT_ID
        - OAUTH2_CLIENT_SECRET or ALFRESCO_OAUTH2_CLIENT_SECRET  
        - OAUTH2_TOKEN_ENDPOINT or ALFRESCO_OAUTH2_TOKEN_ENDPOINT
        - OAUTH2_SCOPE or ALFRESCO_OAUTH2_SCOPE (optional)
        """
        return cls(
            base_url=base_url or os.getenv('ALFRESCO_URL') or os.getenv('ALFRESCO_BASE_URL') or 'http://localhost:8080',
            client_id="",  # Will be loaded from env
            grant_type=grant_type,
            load_env=True,
            env_file=env_file,
            **kwargs
        )
    
    def get_config_info(self) -> Dict[str, Any]:
        """Get configuration information for debugging (without sensitive data)."""
        return {
            "base_url": self.base_url,
            "client_id": self.client_id[:8] + "..." if self.client_id else None,
            "client_secret": "***" if self.client_secret else None,
            "token_endpoint": self.token_endpoint,
            "grant_type": self.grant_type,
            "scope": self.scope,
            "has_access_token": bool(self.access_token),
            "has_refresh_token": bool(self.refresh_token),
            "token_expires": self.token_expires.isoformat() if self.token_expires else None,
            "is_authenticated": self.is_authenticated(),
            "verify_ssl": self.verify_ssl
        }
