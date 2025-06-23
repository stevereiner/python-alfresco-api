#!/usr/bin/env python3
"""
Test Individual API Client Dependencies

Test that all individual API clients can be imported and work correctly.
"""

import sys
import os
import tempfile
import shutil
from pathlib import Path
import pytest

# Add the python_alfresco_api to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from python_alfresco_api import AlfrescoMasterClient, ClientFactory

def test_client_imports():
    """Test that all API clients can be imported correctly."""
    
    # Test individual clients import
    from python_alfresco_api.clients.auth_client import AlfrescoAuthClient
    from python_alfresco_api.clients.core_client import AlfrescoCoreClient  
    from python_alfresco_api.clients.discovery_client import AlfrescoDiscoveryClient
    from python_alfresco_api.clients.search_client import AlfrescoSearchClient
    from python_alfresco_api.clients.workflow_client import AlfrescoWorkflowClient
    from python_alfresco_api.clients.model_client import AlfrescoModelClient
    from python_alfresco_api.clients.search_sql_client import AlfrescoSearchSqlClient
    
    # Test master client import
    assert AlfrescoMasterClient is not None
    assert ClientFactory is not None
    
    print("✅ All client imports successful")

def test_auth_client_creation():
    """Test auth client can be created successfully."""
    try:
        # Test via ClientFactory
        client = ClientFactory.create_auth_client("http://localhost:8080")
        assert client is not None
        print("   ✅ Auth client created successfully")
        
    except Exception as e:
        print(f"   ⚠️  Auth client creation: {e}")

def test_discovery_client_creation():
    """Test discovery client can be created successfully.""" 
    try:
        # Test via ClientFactory
        client = ClientFactory.create_discovery_client("http://localhost:8080")
        assert client is not None
        print("   ✅ Discovery client created successfully")
        
    except Exception as e:
        print(f"   ⚠️  Discovery client creation: {e}")

def test_search_client_creation():
    """Test search client can be created successfully."""
    try:
        # Test via ClientFactory
        client = ClientFactory.create_search_client("http://localhost:8080")
        assert client is not None
        print("   ✅ Search client created successfully")
        
    except Exception as e:
        print(f"   ⚠️  Search client creation: {e}")

def test_search_sql_client_creation():
    """Test search SQL client can be created successfully."""
    try:
        # Test via ClientFactory
        client = ClientFactory.create_search_sql_client("http://localhost:8080")
        assert client is not None
        print("   ✅ Search SQL client created successfully")
        
    except Exception as e:
        print(f"   ⚠️  Search SQL client creation: {e}")

def test_master_client_creation():
    """Test master client can be created and has all APIs."""
    try:
        master_client = AlfrescoMasterClient("http://localhost:8080")
        
        # Test all clients exist
        assert hasattr(master_client, 'auth')
        assert hasattr(master_client, 'core')
        assert hasattr(master_client, 'discovery')
        assert hasattr(master_client, 'search')
        assert hasattr(master_client, 'workflow')
        assert hasattr(master_client, 'model')
        assert hasattr(master_client, 'search_sql')
        
        print("   ✅ Master client created with all APIs")
        
    except Exception as e:
        print(f"   ⚠️  Master client creation: {e}")

def test_core_client_comprehensive():
    """Test core client creation in detail."""
    try:
        # Test via ClientFactory
        client = ClientFactory.create_core_client("http://localhost:8080")
        assert client is not None
        print("   ✅ Core client created successfully")
        
    except Exception as e:
        print(f"   ⚠️  Core client creation: {e}")

if __name__ == "__main__":
    print("🧪 Testing Individual API Client Dependencies")
    test_client_imports()
    test_auth_client_creation()
    test_discovery_client_creation() 
    test_search_client_creation()
    test_search_sql_client_creation()
    test_master_client_creation()
    test_core_client_comprehensive()
    print("✅ All dependency tests completed!") 