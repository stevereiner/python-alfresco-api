"""
Alfresco Workflow API Client - V1.1 Three-Tier Architecture

Provides access to Workflow API operations with lazy loading and hierarchical organization.
"""

# Import from Level 2 models
from .models import WorkflowResponse, WorkflowRequest

# Import the main client class
from .workflow_client import AlfrescoWorkflowClient

# Import all submodules to ensure they get packaged
from . import deployments, process_definitions, processes, tasks, models

# Export the client class and submodules
__all__ = [
    'AlfrescoWorkflowClient', 'WorkflowResponse', 'WorkflowRequest',
    # Lazy-loaded submodules and models
    'deployments', 'process_definitions', 'processes', 'tasks', 'models'
]