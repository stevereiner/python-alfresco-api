"""
Favorites Operations Client - Level 3: Favorites-Specific Operations

This module provides favorites-specific operations within the Core API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.
"""

from .favorites_client import FavoritesClient
from . import models

__all__ = ['FavoritesClient', 'models']