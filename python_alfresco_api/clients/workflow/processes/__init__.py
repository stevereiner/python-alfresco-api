"""
Processes Operations - Level 3: Processes-Specific Operations

This module provides processes-specific operations within the Workflow API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.

Clean imports only - implementation moved to processes_client.py
"""

# Import the main client class
from .processes_client import ProcessesClient

# Export clean public API
__all__ = [
    'ProcessesClient'
]