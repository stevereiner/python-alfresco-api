"""
People Operations Client - Level 3: People-Specific Operations

This module provides people-specific operations within the Core API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.
"""

from .people_client import PeopleClient
from . import models

__all__ = ['PeopleClient', 'models']