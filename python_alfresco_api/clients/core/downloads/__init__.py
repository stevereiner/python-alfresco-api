"""
Downloads Operations Client - Level 3: Downloads-Specific Operations

This module provides downloads-specific operations within the Core API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.
"""

from .downloads_client import DownloadsClient
from . import models

__all__ = ['DownloadsClient', 'models']