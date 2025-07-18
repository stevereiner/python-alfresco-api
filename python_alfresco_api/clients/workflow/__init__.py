"""
Alfresco Workflow API Client - V1.1 Three-Tier Architecture

Provides access to Workflow API operations with lazy loading and hierarchical organization.
"""

# Import from Level 2 models
from .models import WorkflowResponse, WorkflowRequest

# Import the main client class
from .workflow_client import AlfrescoWorkflowClient

# Export the client class
__all__ = ['AlfrescoWorkflowClient', 'WorkflowResponse', 'WorkflowRequest']