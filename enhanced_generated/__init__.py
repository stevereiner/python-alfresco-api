"""
Enhanced Generated Alfresco API Package

Modern Python client for Alfresco APIs using OpenAPI Generator and Pydantic v2.

This package provides:
- AlfrescoClient: Master client for all 7 Alfresco APIs
- AlfrescoBaseClient: Base functionality
- Individual API clients in the clients/ directory
- Enhanced wrappers in the enhanced/ directory
- Pydantic models in the models/ directory

Usage:
    from enhanced_generated import AlfrescoClient
    
    client = AlfrescoClient(
        host="http://localhost:8080",
        username="admin", 
        password="admin"
    )
    
    # Access APIs
    nodes = client.core['nodes'].list_node_children('-root-')
    info = client.discovery.get_repository_information()
"""

from .AlfrescoClient import AlfrescoClient
from .BaseClient import AlfrescoBaseClient

__version__ = "1.0.0"
__author__ = "Python Alfresco API Team"

# Main exports
__all__ = [
    'AlfrescoClient',
    'AlfrescoBaseClient'
]

# Package metadata
AVAILABLE_APIS = [
    'auth',          # Authentication API
    'core',          # Core API (nodes, sites, people, etc.)
    'discovery',     # Discovery API  
    'search',        # Search API
    'workflow',      # Workflow API
    'model',         # Model API
    'search-sql'     # Search SQL API
]

def get_version():
    """Get package version."""
    return __version__

def get_available_apis():
    """Get list of available API names.""" 
    return AVAILABLE_APIS.copy()

def create_client(**kwargs):
    """
    Convenience factory function for creating an AlfrescoClient.
    
    Args:
        **kwargs: Arguments passed to AlfrescoClient constructor
        
    Returns:
        AlfrescoClient: Configured Alfresco client
    """
    return AlfrescoClient(**kwargs) 
