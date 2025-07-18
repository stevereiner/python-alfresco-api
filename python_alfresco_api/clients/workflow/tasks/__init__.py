"""
Tasks Operations - Level 3: Tasks-Specific Operations

This module provides tasks-specific operations within the Workflow API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.

Clean imports only - implementation moved to tasks_client.py
"""

# Import the main client class
from .tasks_client import TasksClient

# Export clean public API
__all__ = [
    'TasksClient'
]