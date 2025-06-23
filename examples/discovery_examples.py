#!/usr/bin/env python3
"""
Alfresco Discovery API Examples

This file demonstrates how to use the Discovery API with the master client.
The Discovery API provides repository information and system capabilities.
"""

import sys
import os
import json

from AlfrescoClient import AlfrescoClient

def main():
    """Discovery API examples."""
    print("🔍 Discovery API Examples")
    
    # Initialize client
    client = AlfrescoClient(host="http://localhost:8080", username="admin", password="admin")
    
    if not client.discovery:
        print("❌ Discovery API not available")
        return
    
    # Example 1: Get repository information
    print("\n1. Getting repository information...")
    try:
        repo_info = client.discovery.get_repository_information()
        
        if repo_info and hasattr(repo_info, 'entry') and hasattr(repo_info.entry, 'repository'):
            repo = repo_info.entry.repository
            print("✅ Repository Information Retrieved:")
            print(f"  Name: {getattr(repo, 'name', 'Unknown')}")
            print(f"  Version: {getattr(repo.version, 'display', 'Unknown') if hasattr(repo, 'version') else 'Unknown'}")
            print(f"  Edition: {getattr(repo, 'edition', 'Unknown')}")
            status = 'Read-only' if (hasattr(repo, 'status') and getattr(repo.status, 'isReadOnly', False)) else 'Read-write'
            print(f"  Status: {status}")
            
            # Show license info if available
            if hasattr(repo_info.entry, 'license'):
                license_info = repo_info.entry.license
                print(f"  License: {getattr(license_info, 'issued_at', 'Unknown')}")
                
            # Show version details if available
            if hasattr(repo, 'version'):
                version = repo.version
                print(f"  Major Version: {getattr(version, 'major', 'Unknown')}")
                print(f"  Minor Version: {getattr(version, 'minor', 'Unknown')}")
                print(f"  Patch Version: {getattr(version, 'patch', 'Unknown')}")
                
        else:
            print("⚠️ Repository info received but in unexpected format")
            
    except Exception as e:
        print(f"⚠️ Standard API call failed: {e}")
        
        # Example 2: Fallback to raw response
        print("\n2. Trying raw response fallback...")
        try:
            raw_response = client.discovery.get_repository_information_without_preload_content()
            if raw_response.status == 200:
                data = json.loads(raw_response.data.decode('utf-8'))
                repo = data['entry']['repository']
                print("✅ Repository Information (Raw Response):")
                print(f"  Name: {repo.get('name', 'Unknown')}")
                print(f"  Version: {repo.get('version', {}).get('display', 'Unknown')}")
                print(f"  Edition: {repo.get('edition', 'Unknown')}")
                
                # Show capabilities if available
                if 'modules' in data['entry']:
                    modules = data['entry']['modules']
                    print(f"  Modules: {len(modules)} available")
                    for module in modules[:3]:  # Show first 3 modules
                        print(f"    - {module.get('id', 'Unknown')}: {module.get('version', 'Unknown')}")
                        
            else:
                print(f"❌ Raw response failed with status: {raw_response.status}")
                
        except Exception as raw_error:
            print(f"❌ Raw response also failed: {raw_error}")
    
    # Example 3: Repository capabilities exploration
    print("\n3. Exploring repository capabilities...")
    try:
        # Try to get capabilities through different approaches
        repo_info = client.discovery.get_repository_information()
        
        if repo_info:
            print("Repository capabilities exploration:")
            
            # Check for specific features (if available in response)
            capabilities = []
            
            # Try to determine available features
            try:
                if hasattr(repo_info, 'entry'):
                    entry = repo_info.entry
                    if hasattr(entry, 'repository'):
                        print("  ✅ Core repository features available")
                        capabilities.append("Core Repository")
                    if hasattr(entry, 'license'):
                        print("  ✅ License information available")
                        capabilities.append("License Info")
                    if hasattr(entry, 'modules'):
                        print("  ✅ Module information available")
                        capabilities.append("Module Info")
                    if hasattr(entry, 'status'):
                        print("  ✅ Status information available")
                        capabilities.append("Status Info")
                        
            except Exception as cap_error:
                print(f"  ⚠️ Capability detection failed: {cap_error}")
            
            if capabilities:
                print(f"  Available capabilities: {', '.join(capabilities)}")
            else:
                print("  Basic repository information only")
                
    except Exception as e:
        print(f"❌ Capabilities exploration failed: {e}")
    
    # Example 4: Connection testing
    print("\n4. Testing Discovery API connectivity...")
    try:
        # Multiple attempts to test the API
        attempts = [
            ("Standard call", lambda: client.discovery.get_repository_information()),
            ("Raw response", lambda: client.discovery.get_repository_information_without_preload_content())
        ]
        
        for attempt_name, attempt_func in attempts:
            try:
                result = attempt_func()
                if result:
                    print(f"  ✅ {attempt_name}: Success")
                else:
                    print(f"  ⚠️ {attempt_name}: Returned None")
            except Exception as attempt_error:
                print(f"  ❌ {attempt_name}: {attempt_error}")
                
    except Exception as e:
        print(f"❌ Connectivity testing failed: {e}")

if __name__ == "__main__":
    main() 