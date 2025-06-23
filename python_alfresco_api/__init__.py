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
from .auth_util import AuthUtil

# Individual clients
from .clients.auth_client import AlfrescoAuthClient
from .clients.core_client import AlfrescoCoreClient  
from .clients.discovery_client import AlfrescoDiscoveryClient
from .clients.search_client import AlfrescoSearchClient
from .clients.workflow_client import AlfrescoWorkflowClient
from .clients.model_client import AlfrescoModelClient
from .clients.search_sql_client import AlfrescoSearchSQLClient

# Pydantic models for LLM integration
from .models import *

__version__ = "2.0.0"
__all__ = [
    # Factory & utilities
    "ClientFactory",
    "AuthUtil",
    
    # Individual clients
    "AlfrescoAuthClient",
    "AlfrescoCoreClient", 
    "AlfrescoDiscoveryClient",
    "AlfrescoSearchClient",
    "AlfrescoWorkflowClient", 
    "AlfrescoModelClient",
    "AlfrescoSearchSQLClient"
]
