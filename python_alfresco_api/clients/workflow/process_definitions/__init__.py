"""
ProcessDefinitions Operations - Level 3: ProcessDefinitions-Specific Operations

This module provides process_definitions-specific operations within the Workflow API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.

Clean imports only - implementation moved to process_definitions_client.py
"""

# Import the main client class
from .process_definitions_client import ProcessDefinitionsClient

# Export clean public API
__all__ = [
    'ProcessDefinitionsClient'
]