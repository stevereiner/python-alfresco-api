"""
Queries Operations Client - Level 3: Queries-Specific Operations

This module provides queries-specific operations within the Core API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.
"""

from .queries_client import QueriesClient
from . import models

__all__ = ['QueriesClient', 'models']