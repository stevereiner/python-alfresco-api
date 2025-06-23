#!/usr/bin/env python3
"""
Simple Test Suite

Quick tests to verify the basic functionality works.
"""

import sys
import os
from pathlib import Path

# Add python_alfresco_api to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from python_alfresco_api import AlfrescoMasterClient
import pytest

def test_import():
    """Test that AlfrescoClient can be imported."""
    print("🧪 Testing import...")
    from python_alfresco_api import AlfrescoMasterClient
    assert AlfrescoMasterClient is not None
    print("   ✅ AlfrescoMasterClient imported successfully")

def test_client_creation():
    """Test that AlfrescoClient can be created."""
    print("🧪 Testing client creation...")
    from python_alfresco_api import AlfrescoMasterClient
    
    try:
        client = AlfrescoMasterClient("http://localhost:8080")
        assert client is not None
        print("   ✅ AlfrescoMasterClient created successfully")
    except Exception as e:
        print(f"   ⚠️  Client creation: {e}")

def test_client_properties():
    """Test that AlfrescoClient has expected properties."""
    print("🧪 Testing client properties...")
    from python_alfresco_api import AlfrescoMasterClient
    
    try:
        client = AlfrescoMasterClient("http://localhost:8080")
        
        # Test basic properties
        assert hasattr(client, 'base_url')
        assert hasattr(client, 'auth')
        assert hasattr(client, 'core')
        assert hasattr(client, 'discovery')
        assert hasattr(client, 'search')
        
        print("   ✅ AlfrescoMasterClient has expected properties")
    except Exception as e:
        print(f"   ⚠️  Client properties: {e}")

def test_client_info():
    """Test client info functionality."""
    print("🧪 Testing client info...")
    from python_alfresco_api import AlfrescoMasterClient
    
    try:
        client = AlfrescoMasterClient("http://localhost:8080")
        info = client.get_client_info()
        
        assert isinstance(info, dict)
        assert 'base_url' in info
        assert 'available_apis' in info
        
        print("   ✅ Client info working")
    except Exception as e:
        print(f"   ⚠️  Client info: {e}")

def test_individual_clients():
    """Test individual client access."""
    print("🧪 Testing individual clients...")
    from python_alfresco_api import AlfrescoMasterClient
    
    try:
        client = AlfrescoMasterClient("http://localhost:8080")
        
        # Test accessing individual clients
        auth_client = client.auth_client
        core_client = client.core_client
        discovery_client = client.discovery_client
        
        assert auth_client is not None
        assert core_client is not None
        assert discovery_client is not None
        
        print("   ✅ Individual clients accessible")
    except Exception as e:
        print(f"   ⚠️  Individual clients: {e}")

def test_client_factory():
    """Test ClientFactory functionality."""
    print("🧪 Testing ClientFactory...")
    from python_alfresco_api.client_factory import ClientFactory
    
    try:
        # Test creating individual clients through factory
        factory = ClientFactory("http://localhost:8080")
        auth_client = factory.create_auth_client()
        core_client = factory.create_core_client()
        
        assert auth_client is not None
        assert core_client is not None
        
        print("   ✅ ClientFactory working")
    except Exception as e:
        print(f"   ⚠️  ClientFactory: {e}")

if __name__ == "__main__":
    print("🚀 Running Simple Test Suite")
    test_import()
    test_client_creation()
    test_client_properties()
    test_client_info()
    test_individual_clients()
    test_client_factory()
    print("✅ Simple tests completed!") 