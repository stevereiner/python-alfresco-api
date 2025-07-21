"""
Audit Operations Client - Level 3: Audit-Specific Operations

This module provides audit-specific operations within the Core API.
Part of the three-tier V1.1 architecture with complete 4-pattern detailed functions.
"""

from .audit_client import AuditClient
from . import models

__all__ = ['AuditClient', 'models']