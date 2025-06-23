"""
Event System Models

Data models for Alfresco event subscriptions and notifications.
"""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel


class EventSubscription(BaseModel):
    """Event subscription configuration"""
    
    name: str
    events: List[str]
    description: Optional[str] = None
    webhook_url: Optional[str] = None  # For Enterprise Edition
    filter_expression: Optional[str] = None
    
    class Config:
        extra = "allow"


class EventNotification(BaseModel):
    """Standardized event notification format"""
    
    event_type: str
    node_id: Optional[str] = None
    user_id: Optional[str] = None
    timestamp: Optional[str] = None
    data: Optional[Dict[str, Any]] = None
    source_system: Optional[str] = None  # 'community' or 'enterprise'
    
    class Config:
        extra = "allow" 