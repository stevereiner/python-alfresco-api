"""
Event System Models

Data models for Alfresco event subscriptions and notifications.
"""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, ConfigDict


class EventSubscription(BaseModel):
    """Event subscription configuration"""
    
    model_config = ConfigDict(extra="allow")

    name: str
    events: List[str]
    description: Optional[str] = None
    webhook_url: Optional[str] = None  # optional delivery webhook, if a consumer uses one
    filter_expression: Optional[str] = None


class EventNotification(BaseModel):
    """Standardized event notification format"""
    
    model_config = ConfigDict(extra="allow")

    event_type: str
    node_id: Optional[str] = None
    user_id: Optional[str] = None
    timestamp: Optional[str] = None
    data: Optional[Dict[str, Any]] = None
    source_system: Optional[str] = None  # e.g. 'activemq'