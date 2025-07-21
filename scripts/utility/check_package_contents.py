#!/usr/bin/env python3
"""
Package Contents Verification Script
Checks that all expected modules are included in the wheel package.
"""

import zipfile
import os
from pathlib import Path

def check_package_contents(wheel_path="dist/python_alfresco_api-1.1.0-py3-none-any.whl"):
    """Check what's included in the wheel package"""
    
    if not os.path.exists(wheel_path):
        print(f"❌ Wheel not found: {wheel_path}")
        return False
    
    print(f"📦 Analyzing package: {wheel_path}")
    print("=" * 60)
    
    with zipfile.ZipFile(wheel_path, 'r') as z:
        all_files = z.namelist()
        
        # Check downloads module specifically
        downloads_files = [f for f in all_files if 'downloads' in f]
        print(f"\n🔍 Downloads module files ({len(downloads_files)}):")
        for f in downloads_files:
            print(f"  ✅ {f}")
        
        if not downloads_files:
            print("  ❌ No downloads files found!")
            return False
        
        # Check all core client directories
        core_files = [f for f in all_files if f.startswith('python_alfresco_api/clients/core/')]
        core_dirs = set()
        
        for f in core_files:
            parts = f.split('/')
            if len(parts) >= 4 and parts[3] != '__pycache__':
                core_dirs.add(parts[3])
        
        print(f"\n🏗️ Core client directories ({len(core_dirs)}):")
        expected_dirs = [
            'actions', 'activities', 'audit', 'comments', 'content', 'downloads',
            'favorites', 'groups', 'networks', 'nodes', 'people', 'preferences',
            'probes', 'queries', 'ratings', 'renditions', 'shared_links', 'sites',
            'tags', 'trashcan', 'versions'
        ]
        
        for expected in sorted(expected_dirs):
            if expected in core_dirs:
                print(f"  ✅ {expected}")
            else:
                print(f"  ❌ {expected} - MISSING!")
        
        # Check source directories vs package
        source_core_path = Path('python_alfresco_api/clients/core')
        if source_core_path.exists():
            source_dirs = set()
            for item in source_core_path.iterdir():
                if item.is_dir() and not item.name.startswith('__'):
                    source_dirs.add(item.name)
            
            missing_in_package = source_dirs - core_dirs
            extra_in_package = core_dirs - source_dirs
            
            print(f"\n📊 Comparison Summary:")
            print(f"  Source directories: {len(source_dirs)}")
            print(f"  Package directories: {len(core_dirs)}")
            
            if missing_in_package:
                print(f"  ❌ Missing from package: {missing_in_package}")
            if extra_in_package:
                print(f"  ⚠️ Extra in package: {extra_in_package}")
            
            if not missing_in_package and not extra_in_package:
                print(f"  ✅ Perfect match!")
        
        # Check key files
        print(f"\n📄 Key files verification:")
        key_files_patterns = [
            'python_alfresco_api/__init__.py',
            'python_alfresco_api/client_factory.py',
            'python_alfresco_api/auth_util.py',
            'python_alfresco_api/clients/core/downloads/__init__.py',
            'python_alfresco_api/clients/core/downloads/downloads_client.py',
            'python_alfresco_api/clients/core/downloads/models.py'
        ]
        
        for pattern in key_files_patterns:
            found = any(f == pattern for f in all_files)
            status = "✅" if found else "❌"
            print(f"  {status} {pattern}")
        
        print(f"\n📈 Package Statistics:")
        print(f"  Total files: {len(all_files)}")
        print(f"  Python files: {len([f for f in all_files if f.endswith('.py')])}")
        print(f"  Core client files: {len(core_files)}")
        
        return len(missing_in_package) == 0 if 'missing_in_package' in locals() else True

if __name__ == "__main__":
    success = check_package_contents()
    if success:
        print(f"\n🎉 Package verification PASSED!")
    else:
        print(f"\n❌ Package verification FAILED!")
    
    exit(0 if success else 1) 