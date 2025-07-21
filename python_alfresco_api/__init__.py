"""
Python Alfresco API - Hybrid Architecture

The perfect combination of:
- Pydantic v2 models for LLM integration & MCP servers
- Professional HTTP clients with async support
- Individual clients for enterprise modularity
- Factory pattern for easy configuration

Generated using the proven hybrid approach:
datamodel-code-generator + openapi-python-client
"""

from .client_factory import ClientFactory
from .auth_util import AuthUtil, OAuth2AuthUtil

# Individual clients - V1.1 hierarchical structure
from .clients.auth import AlfrescoAuthClient
from .clients.core import AlfrescoCoreClient  
from .clients.discovery import AlfrescoDiscoveryClient
from .clients.search import AlfrescoSearchClient
from .clients.workflow import AlfrescoWorkflowClient
from .clients.model import AlfrescoModelClient
from .clients.search_sql import AlfrescoSearchSqlClient

# Pydantic models for LLM integration
from .models import *

# Conversion utilities for Pydantic ↔ attrs model transformation  
from .clients.conversion_utils import (
    pydantic_to_attrs_dict,
    attrs_to_pydantic,
    create_converter_pair
)

# Import raw_clients to ensure they get packaged
from . import raw_clients

__version__ = "1.0.0"
__all__ = [
    # Factory & utilities
    "ClientFactory",
    "AuthUtil",
    "OAuth2AuthUtil",
    
    # Individual clients
    "AlfrescoAuthClient",
    "AlfrescoCoreClient", 
    "AlfrescoDiscoveryClient",
    "AlfrescoSearchClient",
    "AlfrescoWorkflowClient", 
    "AlfrescoModelClient",
    "AlfrescoSearchSqlClient",
    
    # Conversion utilities
    "pydantic_to_attrs_dict",
    "attrs_to_pydantic", 
    "create_converter_pair",
    
    # Raw clients
    "raw_clients"
]
