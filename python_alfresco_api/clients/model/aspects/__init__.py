"""
Aspects Operations Client - Level 3: Aspects-Specific Operations

This module provides aspects-specific operations within the Model API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.
"""

from .aspects_client import AspectsClient
from . import models

__all__ = ['AspectsClient', 'models']