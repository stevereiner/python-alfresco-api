"""
Types Operations Client - Level 3: Types-Specific Operations

This module provides types-specific operations within the Model API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.
"""

from .types_client import TypesClient
from . import models

__all__ = ['TypesClient', 'models']