"""
Content Operations Client - Level 3: File Upload/Download Operations

This module provides content-specific operations within the Core API.
Part of the three-tier V1.1 architecture.
"""

# Import from Level 3 (operation-specific models)
from .models import UploadResponse, DownloadResponse
from . import models

# Import the main client class
from .content_client import ContentClient

# Export the client class and models
__all__ = ['ContentClient', 'UploadResponse', 'DownloadResponse', 'models'] 