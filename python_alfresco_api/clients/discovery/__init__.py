"""
Alfresco Discovery API Client - V1.1 Three-Tier Architecture

Provides access to Discovery API operations with lazy loading and hierarchical organization.
"""

# Import from Level 2 models
from .models import DiscoveryResponse, DiscoveryRequest

# Import the main client class
from .discovery_client import AlfrescoDiscoveryClient

# Import models module itself to ensure it gets packaged
from . import models

# Export the client class, models, and the models module itself
__all__ = ['AlfrescoDiscoveryClient', 'DiscoveryResponse', 'DiscoveryRequest', 'models']