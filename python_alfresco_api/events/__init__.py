"""
Alfresco Event System

Event client for Alfresco's ActiveMQ messaging (repo events on the STOMP topic
/topic/alfresco.repo.event2). Detects ActiveMQ availability and registers handlers; consumers
subscribe to the STOMP topic directly (see AlfrescoEventClient for details).
"""

from .event_client import AlfrescoEventClient
from .models import EventSubscription, EventNotification

__all__ = [
    "AlfrescoEventClient",
    "EventSubscription", 
    "EventNotification"
] 