#!/usr/bin/env python3
"""
Test Runner for Alfresco API Tests

Runs unit tests with mocking and integration tests against live server.
"""

import sys
import os
import subprocess
import time
from pathlib import Path

def run_unit_tests():
    """Run unit tests with mocking."""
    print("🧪 Running Unit Tests (with mocking)...")
    print("=" * 50)
    
    try:
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            "tests/test_unit_master_client.py",
            "tests/test_individual_apis.py",
            "-v",
            "--tb=short"
        ], capture_output=True, text=True)
        
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Error running unit tests: {e}")
        return False

def run_integration_tests():
    """Run integration tests against live server."""
    print("\n🔗 Running Integration Tests (live server)...")
    print("=" * 50)
    
    try:
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            "tests/test_integration_live_server.py",
            "-v",
            "--tb=short"
        ], capture_output=True, text=True)
        
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Error running integration tests: {e}")
        return False

def run_all_tests():
    """Run all tests."""
    print("🚀 Running All Alfresco API Tests")
    print("=" * 60)
    
    start_time = time.time()
    
    # Run unit tests
    unit_success = run_unit_tests()
    
    # Run integration tests
    integration_success = run_integration_tests()
    
    end_time = time.time()
    total_time = end_time - start_time
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    print(f"⏱️  Total time: {total_time:.2f} seconds")
    print(f"🧪 Unit tests: {'✅ PASSED' if unit_success else '❌ FAILED'}")
    print(f"🔗 Integration tests: {'✅ PASSED' if integration_success else '❌ FAILED'}")
    
    if unit_success and integration_success:
        print("🎉 All tests passed!")
        return True
    else:
        print("⚠️  Some tests failed!")
        return False

def run_specific_test(test_file):
    """Run a specific test file."""
    print(f"🎯 Running specific test: {test_file}")
    print("=" * 50)
    
    try:
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            test_file,
            "-v",
            "--tb=short"
        ], capture_output=True, text=True)
        
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Error running test: {e}")
        return False

def main():
    """Main test runner."""
    if len(sys.argv) > 1:
        # Run specific test
        test_file = sys.argv[1]
        if not os.path.exists(test_file):
            print(f"❌ Test file not found: {test_file}")
            sys.exit(1)
        
        success = run_specific_test(test_file)
        sys.exit(0 if success else 1)
    else:
        # Run all tests
        success = run_all_tests()
        sys.exit(0 if success else 1)

if __name__ == "__main__":
    main() 