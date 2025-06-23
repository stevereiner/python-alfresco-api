#!/usr/bin/env python3
"""
Basic Alfresco API Testing Script

Tests the python-alfresco-api clients against a local Alfresco instance.
Perfect for validating functionality with Docker Compose Alfresco setup.
"""

import asyncio
import sys
import requests
import pytest
from pathlib import Path

# Add python_alfresco_api to path
sys.path.insert(0, str(Path(__file__).parent / "python_alfresco_api"))

@pytest.mark.asyncio
async def test_alfresco_connection():
    """Test basic connection to Alfresco instance"""
    
    # Configuration for local Docker Compose Alfresco
    ALFRESCO_URL = "http://localhost:8080"
    USERNAME = "admin"
    PASSWORD = "admin"  # Default admin password
    
    print("🚀 Testing Alfresco API Connection")
    print("=" * 50)
    
    # 1. Test basic connectivity
    print("\n1. Testing basic connectivity...")
    try:
        response = requests.get(f"{ALFRESCO_URL}/alfresco/api/-default-/public/alfresco/versions/1/probes/-ready-", timeout=10)
        if response.status_code == 200:
            print("✅ Alfresco is running and ready")
        else:
            print(f"⚠️  Alfresco responded with status: {response.status_code}")
    except Exception as e:
        print(f"❌ Cannot connect to Alfresco: {e}")
        print("Make sure your Docker Compose Alfresco is running!")
        return False
    
    # 2. Test Discovery API (no auth required)
    print("\n2. Testing Discovery API...")
    try:
        response = requests.get(f"{ALFRESCO_URL}/alfresco/api/discovery", timeout=10)
        if response.status_code == 200:
            discovery_info = response.json()
            print("✅ Discovery API working")
            print(f"   Repository: {discovery_info.get('entry', {}).get('repository', {}).get('name', 'Unknown')}")
            print(f"   Version: {discovery_info.get('entry', {}).get('repository', {}).get('version', {}).get('display', 'Unknown')}")
        else:
            print(f"⚠️  Discovery API responded with status: {response.status_code}")
    except Exception as e:
        print(f"❌ Discovery API error: {e}")
    
    # 3. Test Authentication API
    print("\n3. Testing Authentication API...")
    try:
        auth_data = {
            "userId": USERNAME,
            "password": PASSWORD
        }
        response = requests.post(
            f"{ALFRESCO_URL}/alfresco/api/-default-/public/authentication/versions/1/tickets",
            json=auth_data,
            timeout=10
        )
        
        if response.status_code == 201:
            ticket_info = response.json()
            ticket_id = ticket_info.get('entry', {}).get('id', '')
            print("✅ Authentication successful")
            print(f"   Ticket ID: {ticket_id[:20]}...")
            
            # Test ticket validation
            headers = {"X-Alfresco-Ticket": ticket_id}
            validate_response = requests.get(
                f"{ALFRESCO_URL}/alfresco/api/-default-/public/authentication/versions/1/tickets/-me-",
                headers=headers,
                timeout=10
            )
            
            if validate_response.status_code == 200:
                print("✅ Ticket validation successful")
                return ticket_id
            else:
                print(f"⚠️  Ticket validation failed: {validate_response.status_code}")
                
        else:
            print(f"❌ Authentication failed: {response.status_code}")
            if response.status_code == 403:
                print("   Check your username/password")
            print(f"   Response: {response.text}")
            
    except Exception as e:
        print(f"❌ Authentication error: {e}")
    
    return None

@pytest.mark.asyncio
async def test_python_clients():
    """Test our python-alfresco-api clients"""
    
    print("\n" + "=" * 50)
    print("🐍 Testing Python Alfresco API Clients")
    print("=" * 50)
    
    try:
        # Import our clients
        from python_alfresco_api import (
            ClientFactory, 
            AuthUtil,
            AlfrescoAuthClient,
            AlfrescoDiscoveryClient,
            AlfrescoCoreClient
        )
        print("✅ Successfully imported python-alfresco-api clients")
    except ImportError as e:
        print(f"❌ Failed to import clients: {e}")
        return
    
    # Configuration
    ALFRESCO_URL = "http://localhost:8080"
    USERNAME = "admin"
    PASSWORD = "admin"
    
    # 1. Test ClientFactory
    print("\n1. Testing ClientFactory...")
    try:
        factory = ClientFactory(
            base_url=ALFRESCO_URL,
            username=USERNAME,
            password=PASSWORD
        )
        print("✅ ClientFactory created successfully")
        
        # Get all clients
        clients = factory.create_all_clients()
        print(f"   Available clients: {list(clients.keys())}")
        
    except Exception as e:
        print(f"❌ ClientFactory error: {e}")
    
    # 2. Test AuthUtil
    print("\n2. Testing AuthUtil...")
    try:
        auth_util = AuthUtil(
            base_url=ALFRESCO_URL,
            username=USERNAME,
            password=PASSWORD
        )
        
        # Try authentication
        auth_success = await auth_util.authenticate()
        if auth_success:
            print("✅ AuthUtil authentication successful")
            print(f"   Ticket: {auth_util.ticket[:20] if auth_util.ticket else 'None'}...")
        else:
            print("❌ AuthUtil authentication failed")
            
    except Exception as e:
        print(f"❌ AuthUtil error: {e}")
    
    # 3. Test Individual Clients
    print("\n3. Testing Individual Clients...")
    
    # Test Discovery Client (no auth needed)
    try:
        discovery_client = AlfrescoDiscoveryClient(ALFRESCO_URL)
        client_info = discovery_client.get_client_info()
        print(f"✅ Discovery Client: {client_info}")
    except Exception as e:
        print(f"❌ Discovery Client error: {e}")
    
    # Test Auth Client
    try:
        auth_client = AlfrescoAuthClient(ALFRESCO_URL)
        client_info = auth_client.get_client_info()
        print(f"✅ Auth Client: {client_info}")
    except Exception as e:
        print(f"❌ Auth Client error: {e}")
    
    # Test Core Client
    try:
        core_client = AlfrescoCoreClient(ALFRESCO_URL)
        client_info = core_client.get_client_info()
        print(f"✅ Core Client: {client_info}")
    except Exception as e:
        print(f"❌ Core Client error: {e}")

@pytest.mark.asyncio
async def test_raw_client_availability():
    """Test if the raw generated clients are available"""
    
    print("\n" + "=" * 50)
    print("🔧 Testing Raw Generated Clients")
    print("=" * 50)
    
    raw_clients_dir = Path("python_alfresco_api/raw_clients")
    
    if not raw_clients_dir.exists():
        print("❌ Raw clients directory not found")
        return
    
    print("✅ Raw clients directory found")
    
    # Check each client directory
    for client_dir in raw_clients_dir.iterdir():
        if client_dir.is_dir():
            print(f"\n📁 Checking {client_dir.name}...")
            
            # Look for generated package
            package_dirs = [d for d in client_dir.iterdir() if d.is_dir() and not d.name.startswith('.')]
            if package_dirs:
                print(f"   ✅ Generated package found: {package_dirs[0].name}")
                
                # Check for key files
                package_dir = package_dirs[0]
                key_files = ['client.py', '__init__.py']
                for key_file in key_files:
                    if (package_dir / key_file).exists():
                        print(f"   ✅ {key_file} exists")
                    else:
                        print(f"   ⚠️  {key_file} missing")
                        
                # Check API endpoints
                api_dir = package_dir / "api"
                if api_dir.exists():
                    api_files = list(api_dir.glob("*.py"))
                    print(f"   ✅ API endpoints: {len(api_files)} files")
                else:
                    print(f"   ⚠️  API directory missing")
                    
                # Check models
                models_dir = package_dir / "models"
                if models_dir.exists():
                    model_files = list(models_dir.glob("*.py"))
                    print(f"   ✅ Models: {len(model_files)} files")
                else:
                    print(f"   ⚠️  Models directory missing")
                    
            else:
                print(f"   ❌ No generated package found")

async def main():
    """Main test function"""
    
    print("🧪 Alfresco API Testing Suite")
    print("Testing python-alfresco-api against local Docker Compose Alfresco")
    print("=" * 70)
    
    # Test basic Alfresco connection
    ticket = await test_alfresco_connection()
    
    # Test raw client availability
    await test_raw_client_availability()
    
    # Test our Python clients
    await test_python_clients()
    
    print("\n" + "=" * 70)
    print("🏁 Testing Complete!")
    
    if ticket:
        print("✅ Basic Alfresco connectivity: WORKING")
        print("✅ Authentication: WORKING")
        print("Now you can develop with confidence against this Alfresco instance!")
    else:
        print("⚠️  Some connectivity issues detected")
        print("Check your Docker Compose setup and try again")

if __name__ == "__main__":
    asyncio.run(main()) 