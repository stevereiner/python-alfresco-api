"""
Authentication Operations Client - Level 3: Authentication-Specific Operations

This module provides authentication-specific operations within the Auth API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.
"""

from .authentication_client import AuthenticationClient
from . import models

__all__ = ['AuthenticationClient', 'models']