"""
Alfresco Model API Client - V1.1 Three-Tier Architecture

Provides access to Model API operations with lazy loading and hierarchical organization.
"""

# Import from Level 2 models
from .models import ModelResponse, ModelRequest

# Import the main client class
from .model_client import AlfrescoModelClient

# Export the client class
__all__ = ['AlfrescoModelClient', 'ModelResponse', 'ModelRequest']