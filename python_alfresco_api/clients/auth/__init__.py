"""
Alfresco Auth API Client - V1.1 Three-Tier Architecture

Provides access to Auth API operations with lazy loading and hierarchical organization.
"""

# Import from Level 2 models
from .models import AuthResponse, AuthRequest

# Import the main client class
from .auth_client import AlfrescoAuthClient

# Import models module itself to ensure it gets packaged
from . import models

# Export the client class, models, and the models module itself
__all__ = ['AlfrescoAuthClient', 'AuthResponse', 'AuthRequest', 'models']