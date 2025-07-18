"""
Alfresco Discovery API Client - V1.1 Three-Tier Architecture

Provides access to Discovery API operations with lazy loading and hierarchical organization.
"""

# Import from Level 2 models
from .models import DiscoveryResponse, DiscoveryRequest

# Import the main client class
from .discovery_client import AlfrescoDiscoveryClient

# Export the client class
__all__ = ['AlfrescoDiscoveryClient', 'DiscoveryResponse', 'DiscoveryRequest']