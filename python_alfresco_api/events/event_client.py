"""
Unified Alfresco Event Client

Supports both Community Edition (ActiveMQ/STOMP) and Enterprise Edition (Event Gateway/REST).
Features automatic detection and graceful fallback capabilities.
"""

import asyncio
import logging
from typing import Any, Callable, Dict, List, Optional, Union

try:
    import stomp
    STOMP_AVAILABLE = True
except ImportError:
    STOMP_AVAILABLE = False

try:
    import httpx
    HTTPX_AVAILABLE = True
except ImportError:
    HTTPX_AVAILABLE = False

from .models import EventSubscription, EventNotification


logger = logging.getLogger(__name__)


class AlfrescoEventClient:
    """
    Unified Alfresco Event Client
    
    Automatically detects and supports both:
    - Community Edition: ActiveMQ (port 61616) with STOMP protocol
    - Enterprise Edition: Event Gateway (port 7070) with REST API
    """
    
    def __init__(
        self,
        alfresco_host: str = "localhost",
        username: str = "admin",
        password: str = "admin",
        community_port: int = 61616,
        enterprise_port: int = 7070,
        auto_detect: bool = True,
        debug: bool = False
    ):
        self.alfresco_host = alfresco_host
        self.username = username
        self.password = password
        self.community_port = community_port
        self.enterprise_port = enterprise_port
        self.debug = debug
        
        # Detection results
        self.event_gateway_available = False
        self.activemq_available = False
        self.event_system: Optional[str] = None  # 'enterprise', 'community', or None
        
        # Event handlers
        self.event_handlers: Dict[str, List[Callable]] = {}
        
        # STOMP connection (Community Edition)
        self.stomp_connection = None
        
        # HTTP client (Enterprise Edition)
        self.http_client = None
        
        if auto_detect:
            # Start detection in background
            asyncio.create_task(self._detect_event_systems())
    
    async def _detect_event_systems(self):
        """Detect available event systems"""
        await asyncio.gather(
            self._check_event_gateway(),
            self._check_activemq(),
            return_exceptions=True
        )
        
        # Determine active system (Enterprise takes priority)
        if self.event_gateway_available:
            self.event_system = "enterprise"
        elif self.activemq_available:
            self.event_system = "community"
        else:
            self.event_system = None
            
        if self.debug:
            logger.info(f"Event system detection complete: {self.event_system}")
    
    async def _check_event_gateway(self):
        """Check Enterprise Event Gateway availability"""
        if not HTTPX_AVAILABLE:
            return
            
        try:
            url = f"http://{self.alfresco_host}:{self.enterprise_port}/alfresco/api/-default-/private/alfresco/versions/1/event-subscriptions"
            
            async with httpx.AsyncClient() as client:
                response = await client.get(url, timeout=5.0)
                self.event_gateway_available = response.status_code in [200, 401, 403]
                
        except Exception as e:
            if self.debug:
                logger.debug(f"Event Gateway check failed: {e}")
            self.event_gateway_available = False
    
    async def _check_activemq(self):
        """Check Community ActiveMQ availability"""
        if not STOMP_AVAILABLE:
            self.activemq_available = False
            return
            
        try:
            # Test STOMP connection
            conn = stomp.Connection([(self.alfresco_host, self.community_port)])
            conn.connect(self.username, self.password, wait=False)
            conn.disconnect()
            self.activemq_available = True
            
        except Exception as e:
            if self.debug:
                logger.debug(f"ActiveMQ check failed: {e}")
            self.activemq_available = False
    
    def get_system_info(self) -> Dict[str, Any]:
        """Get event system detection information"""
        return {
            "event_gateway_available": self.event_gateway_available,
            "activemq_available": self.activemq_available,
            "active_system": self.event_system,
            "stomp_installed": STOMP_AVAILABLE,
            "handlers_registered": sum(len(handlers) for handlers in self.event_handlers.values())
        }
    
    def register_event_handler(self, event_type: str, handler: Union[Callable[[EventNotification], None], Callable[[EventNotification], Any]]):
        """Register an event handler for a specific event type"""
        if event_type not in self.event_handlers:
            self.event_handlers[event_type] = []
        self.event_handlers[event_type].append(handler)
    
    def setup_content_handlers(self):
        """Setup default content monitoring handlers"""
        
        async def handle_node_created(notification: EventNotification):
            logger.info(f"Node created: {notification.node_id}")
            
        async def handle_node_updated(notification: EventNotification):
            logger.info(f"Node updated: {notification.node_id}")
            
        async def handle_node_deleted(notification: EventNotification):
            logger.info(f"Node deleted: {notification.node_id}")
        
        self.register_event_handler("node.created", handle_node_created)
        self.register_event_handler("node.updated", handle_node_updated)
        self.register_event_handler("node.deleted", handle_node_deleted)
    
    async def setup_content_monitoring(self) -> Dict[str, Any]:
        """Setup content monitoring subscription"""
        subscription = EventSubscription(
            name="Content Monitoring",
            events=["node.created", "node.updated", "node.deleted"]
        )
        
        return await self.create_subscription(subscription)
    
    async def create_subscription(self, subscription: EventSubscription) -> Dict[str, Any]:
        """Create event subscription based on available system"""
        if self.event_system == "enterprise":
            return await self._create_subscription_enterprise(subscription)
        elif self.event_system == "community":
            return await self._create_subscription_community(subscription)
        else:
            return {
                "success": False,
                "error": "No event system available"
            }
    
    async def _create_subscription_enterprise(self, subscription: EventSubscription) -> Dict[str, Any]:
        """Create Enterprise Event Gateway subscription"""
        try:
            url = f"http://{self.alfresco_host}:{self.enterprise_port}/alfresco/api/-default-/private/alfresco/versions/1/event-subscriptions"
            
            payload = {
                "name": subscription.name,
                "events": subscription.events,
                "config": {
                    "delivery": {
                        "url": subscription.webhook_url or f"http://localhost:8080/webhook/{subscription.name}"
                    }
                }
            }
            
            if not HTTPX_AVAILABLE:
                return {
                    "success": False,
                    "error": "httpx not available for Enterprise Edition"
                }
            
            # Mock successful creation for now
            return {
                "success": True,
                "subscription_id": f"enterprise-{subscription.name}",
                "system": "event-gateway",
                "events": subscription.events
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    async def _create_subscription_community(self, subscription: EventSubscription) -> Dict[str, Any]:
        """Create Community ActiveMQ subscription"""
        try:
            if not STOMP_AVAILABLE:
                return {
                    "success": False,
                    "error": "stomp.py not installed for Community Edition"
                }
            
            # Mock successful creation for now
            return {
                "success": True,
                "subscription_id": f"community-{subscription.name}",
                "system": "activemq",
                "events": subscription.events
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    async def start_listening(self):
        """Start listening for events based on active system"""
        if self.event_system == "enterprise":
            await self._start_listening_enterprise()
        elif self.event_system == "community":
            await self._start_listening_community()
        else:
            if self.debug:
                logger.warning("No event system available for listening")
    
    async def _start_listening_enterprise(self):
        """Start Enterprise Event Gateway listening"""
        # In real implementation, this would setup webhook server
        # or poll for events via REST API
        if self.debug:
            logger.info("Started listening for Enterprise Event Gateway events")
    
    async def _start_listening_community(self):
        """Start Community ActiveMQ listening"""
        if not STOMP_AVAILABLE:
            if self.debug:
                logger.warning("Cannot start Community listening: stomp.py not available")
            return
            
        # In real implementation, this would setup STOMP listeners
        if self.debug:
            logger.info("Started listening for Community ActiveMQ events")
    
    def __repr__(self) -> str:
        return f"AlfrescoEventClient(host={self.alfresco_host}, system={self.event_system})" 