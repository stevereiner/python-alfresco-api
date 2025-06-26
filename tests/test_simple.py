#!/usr/bin/env python3
"""
Simple tests for python-alfresco-api package.
"""

import pytest

def test_import():
    """Test basic import."""
    print("Testing basic import...")
    
    try:
        from python_alfresco_api import ClientFactory
        assert ClientFactory is not None
        print("   ✅ ClientFactory imported successfully")
    except ImportError as e:
        print(f"   ❌ Import failed: {e}")
        raise

def test_client_creation():
    """Test client creation.""" 
    print("Testing client creation...")
    
    try:
        from python_alfresco_api import ClientFactory
        
        factory = ClientFactory("http://localhost:8080", "admin", "admin")
        client = factory.create_master_client()
        assert client is not None
        print("   ✅ Master client created successfully")
    except Exception as e:
        print(f"   ❌ Client creation failed: {e}")
        raise

def test_client_attributes():
    """Test client has expected attributes."""
    print("Testing client attributes...")
    
    try:
        from python_alfresco_api import ClientFactory
        
        factory = ClientFactory("http://localhost:8080", "admin", "admin")
        client = factory.create_master_client()
        
        expected_apis = ['auth', 'core', 'discovery', 'search', 'workflow', 'model', 'search_sql']
        for api in expected_apis:
            assert hasattr(client, api), f"Client should have {api} API"
        
        print("   ✅ Master client has expected properties")
    except Exception as e:
        print(f"   ❌ Attribute test failed: {e}")
        raise

def test_factory_methods():
    """Test factory has all expected methods."""
    print("Testing factory methods...")
    
    try:
        from python_alfresco_api import ClientFactory
        
        factory = ClientFactory("http://localhost:8080", "admin", "admin")
        
        expected_methods = [
            'create_auth_client', 'create_core_client', 'create_discovery_client',
            'create_search_client', 'create_workflow_client', 'create_model_client',
            'create_search_sql_client', 'create_master_client', 'create_all_clients'
        ]
        
        for method in expected_methods:
            assert hasattr(factory, method), f"Factory should have {method} method"
        
        print("   ✅ Factory has all expected methods")
    except Exception as e:
        print(f"   ❌ Factory method test failed: {e}")
        raise

def test_individual_clients():
    """Test individual client creation."""
    print("Testing individual client creation...")
    
    try:
        from python_alfresco_api import ClientFactory
        
        factory = ClientFactory("http://localhost:8080", "admin", "admin")
        
        # Test creating individual clients
        auth_client = factory.create_auth_client()
        assert auth_client is not None
        
        discovery_client = factory.create_discovery_client()
        assert discovery_client is not None
        
        print("   ✅ Individual clients created successfully")
    except Exception as e:
        print(f"   ❌ Individual client test failed: {e}")
        raise

if __name__ == "__main__":
    test_import()
    test_client_creation()
    test_client_attributes()
    test_factory_methods()
    test_individual_clients()
    print("All tests passed!") 