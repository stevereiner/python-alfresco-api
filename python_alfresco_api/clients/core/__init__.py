"""
Alfresco Core API Client

Provides access to Core API operations including nodes, folders, content,
and other repository operations through a clean, lazy-loaded interface.
"""

# Import the client class from separate file
from .core_client import AlfrescoCoreClient

__all__ = ['AlfrescoCoreClient'] 