"""
Shared Authentication Utility

Provides authentication management that can be shared across multiple API clients.
Handles ticket-based authentication with automatic renewal.
"""

from datetime import datetime, timedelta
from typing import Dict

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
        verify_ssl: bool = True,
        timeout: int = 30
    ):
        """
        Initialize authentication utility.

        Args:
            base_url: Base URL of Alfresco instance
            username: Alfresco username
            password: Alfresco password
            verify_ssl: Whether to verify SSL certificates
            timeout: Request timeout in seconds
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
        Authenticate with Alfresco and get ticket.

        Returns:
            True if authentication successful, False otherwise
        """
        try:
            # Import here to avoid circular imports
            from .clients.auth_client import AlfrescoAuthClient
            from .models.alfresco_auth_models import TicketBody

            auth_client = AlfrescoAuthClient(self.base_url, None, self.verify_ssl, self.timeout)

            ticket_body = TicketBody(userId=self.username, password=self.password)
            ticket_response = await auth_client.create_ticket(ticket_body)

            if ticket_response and hasattr(ticket_response, 'entry'):
                self.ticket = ticket_response.entry.id
                # Tickets typically expire after 1 hour
                self.ticket_expires = datetime.now() + timedelta(hours=1)
                self._authenticated = True
                return True

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
        if not self.is_authenticated():
            return {}

        return {
            "X-Alfresco-Ticket": self.ticket
        }

    async def ensure_authenticated(self) -> bool:
        """Ensure we have valid authentication, refresh if needed"""
        if self.is_authenticated():
            return True

        return await self.authenticate()
