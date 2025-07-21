#!/usr/bin/env python3
"""
Performance testing for python-alfresco-api v1.1
Tests various performance aspects of the V1.1 hierarchical architecture.
"""
import sys
import time

def test_performance():
    """Run comprehensive performance tests."""
    try:
        from python_alfresco_api import ClientFactory
        
        print("Client creation performance:")
        
        # Test factory creation
        start = time.time()
        factory = ClientFactory('http://localhost:8080')
        factory_time = (time.time() - start) * 1000
        print(f"  Factory creation: {factory_time:.2f}ms")
        
        # Test all clients creation
        start = time.time()
        all_clients = factory.create_all_clients()
        all_clients_time = (time.time() - start) * 1000
        print(f"  All clients: {all_clients_time:.2f}ms")
        
        # Test core client creation
        start = time.time()
        core_client = factory.create_core_client()
        core_time = (time.time() - start) * 1000
        print(f"  Core client: {core_time:.2f}ms")
        
        print("\nImport performance:")
        
        # Test main package import
        start = time.time()
        import python_alfresco_api
        main_import_time = (time.time() - start) * 1000
        print(f"  Main package: {main_import_time:.2f}ms")
        
        # Test downloads module (previously problematic)
        start = time.time()
        from python_alfresco_api.clients.core.downloads import DownloadsClient
        downloads_import_time = (time.time() - start) * 1000
        print(f"  Downloads module: {downloads_import_time:.2f}ms")
        
        # Test auth client
        start = time.time()
        auth_client = factory.create_auth_client()
        auth_time = (time.time() - start) * 1000
        print(f"  Auth client: {auth_time:.2f}ms")
        
        # Summary for run_tests.py
        print(f"\nSummary: Client creation {all_clients_time:.2f}ms, Import {main_import_time:.2f}ms")
        
        return True
        
    except Exception as e:
        print(f"Performance test failed: {str(e)}")
        return False

def main():
    """Main performance test runner."""
    success = test_performance()
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main()) 