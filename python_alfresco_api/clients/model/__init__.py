"""
Alfresco Model API Client - V1.1 Three-Tier Architecture

Provides access to Model API operations with lazy loading and hierarchical organization.
"""

# Import from Level 2 models
from .models import ModelResponse, ModelRequest

# Import the main client class
from .model_client import AlfrescoModelClient

# Import all submodules to ensure they get packaged
from . import types, aspects, models

# Export the client class and submodules
__all__ = [
    'AlfrescoModelClient', 'ModelResponse', 'ModelRequest',
    # Lazy-loaded submodules and models
    'types', 'aspects', 'models'
]