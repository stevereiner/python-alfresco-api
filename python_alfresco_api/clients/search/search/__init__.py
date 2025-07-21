"""
Search Operations - Clean Import Structure

This module provides clean imports for search operations.
Implementation moved to search_operations.py for better organization.
"""

# Import the actual implementation class
from .search_operations import SearchClient
from . import models

# Export for external use
__all__ = ['SearchClient', 'models']