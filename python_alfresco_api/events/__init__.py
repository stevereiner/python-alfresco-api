"""
Alfresco Event System

Unified event client supporting both Community Edition (ActiveMQ) and Enterprise Edition (Event Gateway).
Provides automatic detection and graceful fallback capabilities.
"""

from .event_client import AlfrescoEventClient
from .models import EventSubscription, EventNotification

__all__ = [
    "AlfrescoEventClient",
    "EventSubscription", 
    "EventNotification"
] 