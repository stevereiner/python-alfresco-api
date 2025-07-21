"""
SQL Operations Client - Level 3: SQL-Specific Operations

This module provides sql-specific operations within the Search SQL API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.
"""

from .sql_client import SqlClient
from . import models

__all__ = ['SqlClient', 'models']