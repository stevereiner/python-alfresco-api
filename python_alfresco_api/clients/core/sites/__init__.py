"""
Sites Operations Client - Level 3: Sites-Specific Operations

This module provides sites-specific operations within the Core API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.
"""

from .sites_client import SitesClient
from . import models

__all__ = ['SitesClient', 'models']