"""
Discovery Operations - Clean Import Structure

This module provides clean imports for discovery operations.
Implementation moved to discovery_operations.py for better organization.
"""

# Import the actual implementation class
from .discovery_operations import DiscoveryClient

# Export for external use
__all__ = ['DiscoveryClient']