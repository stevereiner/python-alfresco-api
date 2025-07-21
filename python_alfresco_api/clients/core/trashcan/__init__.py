"""
Trashcan Operations Client - Level 3: Trashcan-Specific Operations

This module provides trashcan-specific operations within the Core API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.
"""

from .trashcan_client import TrashcanClient
from . import models

__all__ = ['TrashcanClient', 'models']