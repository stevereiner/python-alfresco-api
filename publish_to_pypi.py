#!/usr/bin/env python3
"""
PyPI Publishing Script for python-alfresco-api v1.1
Automates the PyPI publishing process with safety checks.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path


def run_command(cmd, check=True):
    """Run a command and return the result."""
    print(f"🔧 Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if result.stdout:
        print(result.stdout)
    if result.stderr and check:
        print(f"❌ Error: {result.stderr}")
        
    if check and result.returncode != 0:
        sys.exit(1)
        
    return result


def main():
    """Main publishing workflow."""
    print("🚀 PYTHON-ALFRESCO-API v1.1 PyPI PUBLISHING")
    print("=" * 50)
    
    # 1. Verify we're in the right directory
    if not Path("pyproject.toml").exists():
        print("❌ Error: pyproject.toml not found. Run from project root.")
        sys.exit(1)
    
    print("✅ Project directory verified")
    
    # 2. Clean previous builds
    print("\n🧹 Cleaning previous builds...")
    dirs_to_clean = ["build", "dist", "python_alfresco_api.egg-info"]
    for dir_name in dirs_to_clean:
        if Path(dir_name).exists():
            shutil.rmtree(dir_name)
            print(f"   Removed {dir_name}/")
    
    # 3. Build the package
    print("\n📦 Building package...")
    run_command("python -m build")
    
    # 4. Verify dist contents
    print("\n📋 Verifying build output...")
    dist_files = list(Path("dist").glob("*"))
    if len(dist_files) != 2:
        print(f"❌ Expected 2 files in dist/, found {len(dist_files)}")
        sys.exit(1)
    
    for file in dist_files:
        size_mb = file.stat().st_size / (1024 * 1024)
        print(f"   ✅ {file.name} ({size_mb:.1f}MB)")
    
    # 5. Check package with twine
    print("\n🔍 Checking package integrity...")
    run_command("python -m twine check dist/*")
    
    # 6. Prompt for PyPI credentials confirmation
    print("\n🔐 PyPI PUBLISHING READY")
    print("=" * 30)
    print("Before proceeding, ensure you have:")
    print("   ✅ PyPI account created")
    print("   ✅ twine installed (pip install twine)")
    print("   ✅ PyPI API token ready")
    print("   ✅ Project name 'python-alfresco-api' available on PyPI")
    
    response = input("\n📤 Ready to upload to PyPI? (yes/no): ").lower().strip()
    if response != "yes":
        print("⏸️  Upload cancelled. Build files ready in dist/")
        return
    
    # 7. Upload to PyPI
    print("\n📤 Uploading to PyPI...")
    print("You will be prompted for your PyPI credentials...")
    
    # Test PyPI first (optional)
    test_response = input("🧪 Upload to Test PyPI first? (yes/no): ").lower().strip()
    if test_response == "yes":
        print("📤 Uploading to Test PyPI...")
        run_command("python -m twine upload --repository testpypi dist/*")
        print("✅ Test PyPI upload complete!")
        print("🔗 Check: https://test.pypi.org/project/python-alfresco-api/")
        
        confirm = input("\n📤 Proceed to production PyPI? (yes/no): ").lower().strip()
        if confirm != "yes":
            print("⏸️  Production upload cancelled.")
            return
    
    # Production PyPI
    print("📤 Uploading to production PyPI...")
    run_command("python -m twine upload dist/*")
    
    print("\n🎉 PYPI PUBLISHING COMPLETE!")
    print("=" * 30)
    print("✅ python-alfresco-api v1.1.0 published to PyPI")
    print("🔗 Package URL: https://pypi.org/project/python-alfresco-api/")
    print("🛠️  Install with: pip install python-alfresco-api")
    
    # 8. Cleanup option
    cleanup = input("\n🧹 Clean build files? (yes/no): ").lower().strip()
    if cleanup == "yes":
        for dir_name in ["build", "dist", "python_alfresco_api.egg-info"]:
            if Path(dir_name).exists():
                shutil.rmtree(dir_name)
        print("✅ Build files cleaned")


if __name__ == "__main__":
    main() 