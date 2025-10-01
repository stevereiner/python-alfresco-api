"""
Alfresco API Clients

Three-tier architecture API clients with lazy loading and structured models.

This module provides a three-tier architecture:
- Level 1: Global models shared across ALL APIs
- Level 2: API-level models shared within ONE API  
- Level 3: Operation-specific models for ONE operation

Key Benefits:
- [PERFORMANCE] Better performance with lazy loading
- [ORGANIZATION] Organized locality (models exactly where used)
- [STRUCTURE] Structured imports and clear organization
- [MODELS] Pydantic v2 models for better type checking in general and for AI/LLM integration
- [ASYNC] Dual sync/async APIs (sync for simpler use, async for web apps)
"""

# Modern clients with three-tier architecture and lazy loading
from .core import AlfrescoCoreClient
from .master_client import AlfrescoMasterClient

# Global models shared across ALL APIs (Level 1)
from .models import (
    BaseEntry,
    PagingInfo, 
    ErrorResponse,
    ErrorDetail,
    RequestStatus,
    ContentInfo,
    UserInfo
)


# Export clean public API
__all__ = [
    # Modern Clients
    'AlfrescoCoreClient',
    'AlfrescoMasterClient',
    
    # Global Models (Level 1) 
    'BaseEntry',
    'PagingInfo',
    'ErrorResponse', 
    'ErrorDetail',
    'RequestStatus',
    'ContentInfo',
    'UserInfo'
    
    # Note: API-level models (Level 2) are exported from their specific clients
    # e.g., from python_alfresco_api.clients.core.models import CoreResponse
    
    # Note: Operation-specific models (Level 3) are exported from their operations
    # e.g., from python_alfresco_api.clients.core.nodes.models import Node, CreateNodeRequest
]

# Module metadata for discovery
__version__ = "1.1.1"
__description__ = "Alfresco API Clients with three-tier architecture and lazy loading"
__author__ = "Python Alfresco API Project"