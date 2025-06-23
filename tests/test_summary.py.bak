#!/usr/bin/env python3
"""
Test Summary for Alfresco API

Shows the current status of all tests and provides a quick overview.
"""

import sys
import subprocess
from pathlib import Path

def run_test_summary():
    """Run a comprehensive test summary."""
    print("🧪 Alfresco API Test Suite Summary")
    print("=" * 50)
    
    # Test the enhanced client
    try:
        # Add the project root to the path
        sys.path.insert(0, str(Path(__file__).parent.parent))
        from enhanced_generated import AlfrescoClient
        
        print("\n🔧 Testing Enhanced Client...")
        client = AlfrescoClient(
            host="http://localhost:8080",
            username="admin",
            password="admin"
        )
        
        # Get client info
        info = client.get_client_info()
        print(f"✅ Client Type: {info['client_type']}")
        print(f"🌐 Host: {info['host']}")
        print(f"👤 Username: {info['username']}")
        
        # Get API status
        status = client.get_api_status()
        working_count = sum(1 for working in status.values() if working)
        total_apis = len(status)
        
        print(f"\n📊 API Status: {working_count}/{total_apis} APIs Working")
        print("Available APIs:")
        for api_name, is_working in status.items():
            status_icon = "✅" if is_working else "❌"
            print(f"   {status_icon} {api_name}")
        
        # Test connection
        print(f"\n🔗 Testing Connection...")
        results = client.test_connection()
        print(f"📈 Success Rate: {results['success_rate']}")
        print(f"🔍 Discovery Test: {results['discovery_test']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Enhanced client test failed: {e}")
        return False

def run_simple_tests():
    """Run simple tests."""
    print("\n🧪 Running Simple Tests...")
    try:
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            "tests/test_simple.py",
            "-v",
            "--tb=no"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Simple tests passed")
            return True
        else:
            print("❌ Simple tests failed")
            print(result.stdout)
            return False
            
    except Exception as e:
        print(f"❌ Error running simple tests: {e}")
        return False

def run_integration_tests():
    """Run integration tests."""
    print("\n🔗 Running Integration Tests...")
    try:
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            "tests/test_integration_live_server.py::TestLiveAlfrescoServer::test_full_client_functionality",
            "-v",
            "--tb=no"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Integration tests passed")
            return True
        else:
            print("❌ Integration tests failed")
            print(result.stdout)
            return False
            
    except Exception as e:
        print(f"❌ Error running integration tests: {e}")
        return False

def show_test_structure():
    """Show the test structure."""
    print("\n📁 Test Structure:")
    print("tests/")
    print("├── __init__.py                 # Test package")
    print("├── conftest.py                 # Pytest configuration and fixtures")
    print("├── test_simple.py              # Basic functionality tests")
    print("├── test_unit_master_client.py  # Unit tests for master client (mocked)")
    print("├── test_integration_live_server.py  # Integration tests (live server)")
    print("├── test_individual_apis.py     # Individual API tests")
    print("├── run_tests.py               # Test runner script")
    print("├── requirements-test.txt      # Test dependencies")
    print("├── README.md                  # Test documentation")
    print("└── test_summary.py            # This file")

def show_usage_instructions():
    """Show usage instructions."""
    print("\n🚀 Usage Instructions:")
    print("1. Install test dependencies:")
    print("   pip install -r tests/requirements-test.txt")
    print()
    print("2. Run all tests:")
    print("   python tests/run_tests.py")
    print()
    print("3. Run specific test types:")
    print("   python -m pytest tests/test_simple.py -v")
    print("   python -m pytest tests/test_integration_live_server.py -v")
    print()
    print("4. Run with coverage:")
    print("   python -m pytest tests/ --cov=enhanced_generated --cov-report=html")
    print()
    print("5. For integration tests, ensure Alfresco server is running on localhost:8080")

def main():
    """Main test summary function."""
    print("🧪 Alfresco API Test Suite")
    print("=" * 60)
    
    # Show test structure
    show_test_structure()
    
    # Run tests
    enhanced_success = run_test_summary()
    simple_success = run_simple_tests()
    integration_success = run_integration_tests()
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    print(f"🔧 Enhanced Client: {'✅ PASSED' if enhanced_success else '❌ FAILED'}")
    print(f"🧪 Simple Tests: {'✅ PASSED' if simple_success else '❌ FAILED'}")
    print(f"🔗 Integration Tests: {'✅ PASSED' if integration_success else '❌ FAILED'}")
    
    if enhanced_success and simple_success and integration_success:
        print("\n🎉 All tests passed! The Alfresco API client is working correctly.")
    else:
        print("\n⚠️  Some tests failed. Check the output above for details.")
    
    # Show usage instructions
    show_usage_instructions()
    
    return enhanced_success and simple_success and integration_success

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 