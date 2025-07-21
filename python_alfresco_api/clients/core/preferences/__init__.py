"""
Preferences Operations Client - Level 3: Preferences-Specific Operations

This module provides preferences-specific operations within the Core API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.
"""

from .preferences_client import PreferencesClient
from . import models

__all__ = ['PreferencesClient', 'models']