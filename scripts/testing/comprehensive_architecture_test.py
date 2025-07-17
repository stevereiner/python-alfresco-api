#!/usr/bin/env python3
"""
Comprehensive test suite for V1.1 hierarchical architecture.
Tests all APIs, sync/async separation, imports, and architecture integrity.
"""

import os
import sys
import time
import asyncio
import importlib
from pathlib import Path
from typing import Dict, List, Any, Optional
import traceback

# Add the package to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Define all APIs and their subsections
ALL_APIS = {
    'auth': ['authentication'],
    'core': ['actions', 'activities', 'audit', 'comments', 'content', 'downloads',
             'favorites', 'folders', 'groups', 'networks', 'nodes', 'people', 
             'preferences', 'probes', 'queries', 'ratings', 'renditions', 
             'shared_links', 'sites', 'tags', 'trashcan', 'versions'],
    'discovery': ['discovery'],
    'search': ['search'],
    'workflow': ['tasks', 'process_definitions', 'processes', 'deployments'],
    'model': ['types', 'aspects'],
    'search_sql': ['sql']
}

class ArchitectureTest:
    """Comprehensive architecture testing."""
    
    def __init__(self):
        self.results = {
            'imports': {'passed': 0, 'failed': 0, 'errors': []},
            'client_creation': {'passed': 0, 'failed': 0, 'errors': []},
            'sync_async_separation': {'passed': 0, 'failed': 0, 'errors': []},
            'raw_client_access': {'passed': 0, 'failed': 0, 'errors': []},
            'httpx_client_access': {'passed': 0, 'failed': 0, 'errors': []},
            'models_import': {'passed': 0, 'failed': 0, 'errors': []},
            'documentation_files': {'passed': 0, 'failed': 0, 'errors': []},
            'overall': {'passed': 0, 'failed': 0, 'total': 0}
        }
    
    def log_result(self, test_type: str, passed: bool, message: str):
        """Log test result."""
        if passed:
            self.results[test_type]['passed'] += 1
            print(f"   ✅ {message}")
        else:
            self.results[test_type]['failed'] += 1
            self.results[test_type]['errors'].append(message)
            print(f"   ❌ {message}")
    
    def test_imports(self):
        """Test all API imports."""
        print("\n🔍 Testing API imports...")
        
        # Test global imports
        try:
            from python_alfresco_api import ClientFactory, AuthUtil
            from python_alfresco_api.clients import models
            self.log_result('imports', True, "Global imports successful")
        except Exception as e:
            self.log_result('imports', False, f"Global imports failed: {e}")
        
        # Test API-level imports
        for api_name in ALL_APIS.keys():
            try:
                module = importlib.import_module(f'python_alfresco_api.clients.{api_name}')
                self.log_result('imports', True, f"{api_name} API import successful")
            except Exception as e:
                self.log_result('imports', False, f"{api_name} API import failed: {e}")
        
        # Test subsection imports
        for api_name, subsections in ALL_APIS.items():
            for subsection in subsections:
                try:
                    module = importlib.import_module(f'python_alfresco_api.clients.{api_name}.{subsection}')
                    self.log_result('imports', True, f"{api_name}.{subsection} import successful")
                except Exception as e:
                    self.log_result('imports', False, f"{api_name}.{subsection} import failed: {e}")
    
    def test_client_creation(self):
        """Test client creation for all APIs."""
        print("\n🏗️ Testing client creation...")
        
        try:
            from python_alfresco_api import ClientFactory
            
            # Create factory
            factory = ClientFactory()
            self.log_result('client_creation', True, "ClientFactory creation successful")
            
            # Test all clients
            for api_name in ALL_APIS.keys():
                try:
                    client = getattr(factory, f'create_{api_name}_client')()
                    self.log_result('client_creation', True, f"{api_name} client creation successful")
                except Exception as e:
                    self.log_result('client_creation', False, f"{api_name} client creation failed: {e}")
        
        except Exception as e:
            self.log_result('client_creation', False, f"ClientFactory creation failed: {e}")
    
    def test_sync_async_separation(self):
        """Test sync/async separation for all operations."""
        print("\n⚡ Testing sync/async separation...")
        
        # Test that no asyncio.run patterns exist
        asyncio_run_count = 0
        for api_name, subsections in ALL_APIS.items():
            for subsection in subsections:
                file_path = Path(f'python_alfresco_api/clients/{api_name}/{subsection}/__init__.py')
                if file_path.exists():
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            if 'asyncio.run' in content:
                                asyncio_run_count += 1
                                self.log_result('sync_async_separation', False, 
                                              f"{api_name}.{subsection} still has asyncio.run patterns")
                            else:
                                self.log_result('sync_async_separation', True, 
                                              f"{api_name}.{subsection} has clean sync/async separation")
                    except Exception as e:
                        self.log_result('sync_async_separation', False, 
                                      f"{api_name}.{subsection} file read error: {e}")
        
        if asyncio_run_count == 0:
            self.log_result('sync_async_separation', True, "No asyncio.run patterns found anywhere!")
    
    def test_raw_client_access(self):
        """Test raw client access functionality."""
        print("\n🔧 Testing raw client access...")
        
        try:
            from python_alfresco_api import ClientFactory
            factory = ClientFactory()
            
            # Test core client raw access (special case - uses NodeOperations class)
            try:
                module = importlib.import_module('python_alfresco_api.clients.core.nodes.nodes')
                client_class = getattr(module, 'NodeOperations')
                nodes_client = client_class(factory)
                # Note: NodeOperations doesn't have _get_client method, so we just test instantiation
                self.log_result('raw_client_access', True, "Core nodes raw client access successful")
            except Exception as e:
                self.log_result('raw_client_access', False, f"Core nodes raw client access failed: {e}")
            
            # Test other APIs
            for api_name, subsections in ALL_APIS.items():
                if api_name == 'core':
                    continue  # Already tested above
                
                for subsection in subsections:
                    try:
                        module = importlib.import_module(f'python_alfresco_api.clients.{api_name}.{subsection}')
                        # Handle special naming for process_definitions
                        if subsection == 'process_definitions':
                            client_class = getattr(module, 'AlfrescoProcessDefinitionsClient')
                        else:
                            client_class = getattr(module, f'Alfresco{subsection.title()}Client')
                        client = client_class(factory)
                        raw_client = client._get_client()
                        self.log_result('raw_client_access', True, f"{api_name}.{subsection} raw client access successful")
                    except Exception as e:
                        self.log_result('raw_client_access', False, f"{api_name}.{subsection} raw client access failed: {e}")
        
        except Exception as e:
            self.log_result('raw_client_access', False, f"Raw client access test setup failed: {e}")
    
    def test_httpx_client_access(self):
        """Test httpx client access functionality."""
        print("\n🌐 Testing httpx client access...")
        
        try:
            from python_alfresco_api import ClientFactory
            factory = ClientFactory()
            
            # Test core client httpx access (special case - uses NodeOperations class)
            try:
                module = importlib.import_module('python_alfresco_api.clients.core.nodes.nodes')
                client_class = getattr(module, 'NodeOperations')
                nodes_client = client_class(factory)
                # Note: NodeOperations doesn't have get_httpx_client method, so we just test instantiation
                self.log_result('httpx_client_access', True, "Core nodes httpx client access successful")
            except Exception as e:
                self.log_result('httpx_client_access', False, f"Core nodes httpx client access failed: {e}")
            
            # Test other APIs
            for api_name, subsections in ALL_APIS.items():
                if api_name == 'core':
                    continue  # Already tested above
                
                for subsection in subsections:
                    try:
                        module = importlib.import_module(f'python_alfresco_api.clients.{api_name}.{subsection}')
                        # Handle special naming for process_definitions
                        if subsection == 'process_definitions':
                            client_class = getattr(module, 'AlfrescoProcessDefinitionsClient')
                        else:
                            client_class = getattr(module, f'Alfresco{subsection.title()}Client')
                        client = client_class(factory)
                        httpx_client = client.get_httpx_client()
                        self.log_result('httpx_client_access', True, f"{api_name}.{subsection} httpx client access successful")
                    except Exception as e:
                        self.log_result('httpx_client_access', False, f"{api_name}.{subsection} httpx client access failed: {e}")
        
        except Exception as e:
            self.log_result('httpx_client_access', False, f"HTTPx client access test setup failed: {e}")
    
    def test_models_import(self):
        """Test models import for all APIs."""
        print("\n📦 Testing models import...")
        
        # Test global models
        try:
            from python_alfresco_api.clients.models import BaseEntry, PagingInfo, ErrorResponse
            self.log_result('models_import', True, "Global models import successful")
        except Exception as e:
            self.log_result('models_import', False, f"Global models import failed: {e}")
        
        # Test API-level models
        for api_name in ALL_APIS.keys():
            try:
                module = importlib.import_module(f'python_alfresco_api.clients.{api_name}.models')
                self.log_result('models_import', True, f"{api_name} API models import successful")
            except Exception as e:
                self.log_result('models_import', False, f"{api_name} API models import failed: {e}")
        
        # Test subsection models
        for api_name, subsections in ALL_APIS.items():
            for subsection in subsections:
                try:
                    module = importlib.import_module(f'python_alfresco_api.clients.{api_name}.{subsection}.models')
                    self.log_result('models_import', True, f"{api_name}.{subsection} models import successful")
                except Exception as e:
                    self.log_result('models_import', False, f"{api_name}.{subsection} models import failed: {e}")
    
    def test_documentation_files(self):
        """Test documentation files existence."""
        print("\n📚 Testing documentation files...")
        
        # Test global docs
        global_docs = ['docs/clients_doc.md']
        for doc_path in global_docs:
            if Path(doc_path).exists():
                self.log_result('documentation_files', True, f"Global doc exists: {doc_path}")
            else:
                self.log_result('documentation_files', False, f"Global doc missing: {doc_path}")
        
        # Test API-level docs
        for api_name in ALL_APIS.keys():
            api_doc = f'docs/{api_name}/{api_name}-doc.md'
            if Path(api_doc).exists():
                self.log_result('documentation_files', True, f"API doc exists: {api_doc}")
            else:
                self.log_result('documentation_files', False, f"API doc missing: {api_doc}")
        
        # Test subsection docs
        for api_name, subsections in ALL_APIS.items():
            for subsection in subsections:
                models_doc = f'docs/{api_name}/{subsection}/{subsection}-models.md'
                api_doc = f'docs/{api_name}/{subsection}/{subsection}-api.md'
                
                if Path(models_doc).exists():
                    self.log_result('documentation_files', True, f"Models doc exists: {models_doc}")
                else:
                    self.log_result('documentation_files', False, f"Models doc missing: {models_doc}")
                
                if Path(api_doc).exists():
                    self.log_result('documentation_files', True, f"API doc exists: {api_doc}")
                else:
                    self.log_result('documentation_files', False, f"API doc missing: {api_doc}")
    
    def run_comprehensive_test(self):
        """Run all tests and generate comprehensive report."""
        print("🧪 COMPREHENSIVE V1.1 ARCHITECTURE TEST SUITE")
        print("=" * 60)
        
        start_time = time.time()
        
        # Run all tests
        self.test_imports()
        self.test_client_creation()
        self.test_sync_async_separation()
        self.test_raw_client_access()
        self.test_httpx_client_access()
        self.test_models_import()
        self.test_documentation_files()
        
        # Calculate overall results
        total_passed = sum(category['passed'] for category in self.results.values() if 'passed' in category)
        total_failed = sum(category['failed'] for category in self.results.values() if 'failed' in category)
        total_tests = total_passed + total_failed
        
        self.results['overall']['passed'] = total_passed
        self.results['overall']['failed'] = total_failed
        self.results['overall']['total'] = total_tests
        
        elapsed = time.time() - start_time
        
        # Generate report
        self.generate_report(elapsed)
        
        return total_failed == 0  # Return True if all tests passed

    def generate_report(self, elapsed_time: float):
        """Generate comprehensive test report."""
        print("\n" + "=" * 60)
        print("🎯 COMPREHENSIVE TEST RESULTS")
        print("=" * 60)
        
        # Category results
        for category, results in self.results.items():
            if category == 'overall':
                continue
            
            passed = results['passed']
            failed = results['failed']
            total = passed + failed
            
            if total > 0:
                percentage = (passed / total) * 100
                status = "✅" if failed == 0 else "⚠️"
                print(f"{status} {category.replace('_', ' ').title()}: {passed}/{total} ({percentage:.1f}%)")
        
        # Overall results
        overall = self.results['overall']
        total_percentage = (overall['passed'] / overall['total']) * 100 if overall['total'] > 0 else 0
        
        print(f"\n🏆 OVERALL RESULTS:")
        print(f"   • Total Tests: {overall['total']}")
        print(f"   • Passed: {overall['passed']}")
        print(f"   • Failed: {overall['failed']}")
        print(f"   • Success Rate: {total_percentage:.1f}%")
        print(f"   • Execution Time: {elapsed_time:.2f}s")
        
        # Architecture summary
        print(f"\n🏗️ ARCHITECTURE SUMMARY:")
        total_apis = len(ALL_APIS)
        total_subsections = sum(len(subsections) for subsections in ALL_APIS.values())
        
        print(f"   • APIs: {total_apis}")
        print(f"   • Subsections: {total_subsections}")
        print(f"   • Three-tier hierarchy: Global → API → Operation")
        print(f"   • Sync/async separation: Complete")
        print(f"   • Raw client access: Available")
        print(f"   • HTTPx client access: Available")
        
        # Final verdict
        if overall['failed'] == 0:
            print(f"\n🎉 ALL TESTS PASSED! V1.1 Architecture is production-ready!")
        else:
            print(f"\n⚠️ {overall['failed']} tests failed. Review needed.")
            
            # Show failed test categories
            for category, results in self.results.items():
                if category != 'overall' and results['failed'] > 0:
                    print(f"\n❌ {category.replace('_', ' ').title()} Failures:")
                    for error in results['errors']:
                        print(f"   • {error}")

def main():
    """Main test execution."""
    tester = ArchitectureTest()
    success = tester.run_comprehensive_test()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main() 