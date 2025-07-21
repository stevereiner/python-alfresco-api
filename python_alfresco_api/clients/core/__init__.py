"""
Alfresco Core API Client

Provides access to Core API operations including nodes, folders, content,
and other repository operations through a clean, lazy-loaded interface.
"""

# Import the client class from separate file
from .core_client import AlfrescoCoreClient

# Import all submodules to ensure they get packaged
from . import actions, activities, audit, comments, content, downloads
from . import favorites, groups, networks, nodes, people, preferences
from . import probes, queries, ratings, renditions, shared_links, sites
from . import tags, trashcan, versions, models

__all__ = [
    'AlfrescoCoreClient',
    # All lazy-loaded submodules and models
    'actions', 'activities', 'audit', 'comments', 'content', 'downloads',
    'favorites', 'groups', 'networks', 'nodes', 'people', 'preferences', 
    'probes', 'queries', 'ratings', 'renditions', 'shared_links', 'sites',
    'tags', 'trashcan', 'versions', 'models'
] 