#!/usr/bin/env python3
"""
Simple test for documentation generation
"""

import sys
from pathlib import Path

# Add project root to path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def main():
    print("=" * 50)
    print("🧪 Testing Documentation Generation")
    print("=" * 50)
    
    # Check if auth API exists
    auth_path = project_root / "python_alfresco_api/clients/auth"
    print(f"📁 Auth API path: {auth_path}")
    print(f"📁 Exists: {auth_path.exists()}")
    
    if auth_path.exists():
        # List contents
        print("📋 Contents:")
        for item in auth_path.iterdir():
            print(f"   {item.name}")
        
        # Check models.py
        models_path = auth_path / "models.py"
        print(f"📄 models.py exists: {models_path.exists()}")
        
        if models_path.exists():
            with open(models_path, 'r') as f:
                content = f.read()
            print(f"📊 models.py size: {len(content)} chars")
            print("📖 First few lines:")
            for line in content.split('\n')[:5]:
                print(f"   {line}")
        
        # Check authentication subsection
        auth_subsection = auth_path / "authentication"
        print(f"📁 authentication subsection exists: {auth_subsection.exists()}")
        
        if auth_subsection.exists():
            print("📋 Authentication contents:")
            for item in auth_subsection.iterdir():
                print(f"   {item.name}")
    
    print("✅ Test complete!")

if __name__ == "__main__":
    main() 