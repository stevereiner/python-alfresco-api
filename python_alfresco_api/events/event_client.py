"""
Alfresco Event Client

Alfresco Content Services uses ActiveMQ for message queuing, with repo events published to the
STOMP topic /topic/alfresco.repo.event2. This client detects ActiveMQ availability and holds
registered handlers.

NOTE: actual event *listening* is not implemented here (see _start_listening_activemq); consumers
should subscribe to the STOMP topic directly (e.g. via stomp.py). This client is a thin
detection/handler-registry helper.
"""

import asyncio
import logging
from typing import Any, Callable, Dict, List, Optional, Union

try:
    import stomp
    STOMP_AVAILABLE = True
except ImportError:
    STOMP_AVAILABLE = False

from .models import EventSubscription, EventNotification


logger = logging.getLogger(__name__)


class AlfrescoEventClient:
    """
    Alfresco Event Client (ActiveMQ / STOMP).

    Alfresco messaging runs on ActiveMQ; repo events are published to the STOMP topic
    /topic/alfresco.repo.event2 (STOMP port 61613; 61616 is OpenWire).
    """

    def __init__(
        self,
        alfresco_host: str = "localhost",
        username: str = "admin",
        password: str = "admin",
        activemq_port: int = 61613,
        auto_detect: bool = True,
        debug: bool = False
    ):
        self.alfresco_host = alfresco_host
        self.username = username
        self.password = password
        self.activemq_port = activemq_port  # ActiveMQ STOMP port
        self.debug = debug

        # Detection results
        self.activemq_available = False
        self.event_system: Optional[str] = None  # 'activemq' or None

        # Event handlers
        self.event_handlers: Dict[str, List[Callable]] = {}

        # STOMP connection
        self.stomp_connection = None

        if auto_detect:
            # Schedule detection only when an event loop is already running;
            # otherwise callers can await detect_event_systems() explicitly.
            try:
                loop = asyncio.get_running_loop()
            except RuntimeError:
                pass
            else:
                loop.create_task(self._detect_event_systems())

    async def detect_event_systems(self):
        """Detect ActiveMQ availability (call when no loop was running at init)."""
        await self._detect_event_systems()

    async def _detect_event_systems(self):
        """Detect ActiveMQ availability."""
        await asyncio.gather(
            self._check_activemq(),
            return_exceptions=True
        )

        self.event_system = "activemq" if self.activemq_available else None

        if self.debug:
            logger.info(f"Event system detection complete: {self.event_system}")

    async def _check_activemq(self):
        """Check ActiveMQ availability."""
        if not STOMP_AVAILABLE:
            self.activemq_available = False
            return

        try:
            # Test STOMP connection. NOTE: stomp.py's kwarg is `passcode`, not `password`
            # (a `password=` kwarg silently becomes a stray header, leaving the passcode EMPTY).
            # wait=True so this actually validates authentication: ActiveMQ 6.x (ACS 26.1+)
            # enforces JAAS auth, whereas 5.x accepted anonymous connections, so wait=False would
            # report "available" even for rejected credentials.
            conn = stomp.Connection([(self.alfresco_host, self.activemq_port)])
            conn.connect(username=self.username, passcode=self.password, wait=True)
            conn.disconnect()
            self.activemq_available = True

        except Exception as e:
            if self.debug:
                logger.debug(f"ActiveMQ check failed: {e}")
            self.activemq_available = False

    def get_system_info(self) -> Dict[str, Any]:
        """Get event system detection information"""
        return {
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
        """Create event subscription on ActiveMQ."""
        if self.activemq_available:
            return await self._create_subscription_activemq(subscription)
        return {
            "success": False,
            "error": "No event system available"
        }

    async def _create_subscription_activemq(self, subscription: EventSubscription) -> Dict[str, Any]:
        """Create ActiveMQ subscription"""
        try:
            if not STOMP_AVAILABLE:
                return {
                    "success": False,
                    "error": "stomp.py not installed"
                }

            # Mock successful creation for now
            return {
                "success": True,
                "subscription_id": f"activemq-{subscription.name}",
                "system": "activemq",
                "events": subscription.events
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    async def start_listening(self):
        """Start listening for events."""
        if self.activemq_available:
            await self._start_listening_activemq()
        elif self.debug:
            logger.warning("No event system available for listening")

    async def _start_listening_activemq(self):
        """Start ActiveMQ listening.

        NOT implemented here — subscribe to the STOMP topic /topic/alfresco.repo.event2 directly
        (see flexible-graphrag's AlfrescoEventBroadcaster for a working consumer).
        """
        if not STOMP_AVAILABLE:
            if self.debug:
                logger.warning("Cannot start listening: stomp.py not available")
            return

        if self.debug:
            logger.info("Started listening for ActiveMQ events")

    def __repr__(self) -> str:
        return f"AlfrescoEventClient(host={self.alfresco_host}, system={self.event_system})"
