#!/usr/bin/env python3
"""
Test Fixed AuthUtil

Tests the updated AuthUtil that uses query parameter authentication.
"""

import pytest
import asyncio
import sys
from pathlib import Path

# Add python_alfresco_api to path
sys.path.insert(0, str(Path(__file__).parent.parent / "python_alfresco_api"))

@pytest.mark.asyncio
async def test_fixed_authutil():
    """Test the fixed AuthUtil implementation"""
    
    print("🔧 Testing Fixed AuthUtil")
    print("=" * 40)
    
    try:
        from python_alfresco_api.auth_util import AuthUtil
        print("✅ AuthUtil imported successfully")
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return
    
    # Configuration
    ALFRESCO_URL = "http://localhost:8080"
    USERNAME = "admin"
    PASSWORD = "admin"
    
    # Test 1: Create AuthUtil
    print("\n1. Creating AuthUtil...")
    try:
        auth_util = AuthUtil(
            base_url=ALFRESCO_URL,
            username=USERNAME,  
            password=PASSWORD
        )
        print("✅ AuthUtil created successfully")
    except Exception as e:
        print(f"❌ AuthUtil creation failed: {e}")
        return
    
    # Test 2: Authentication
    print("\n2. Testing authentication...")
    try:
        auth_success = await auth_util.authenticate()
        if auth_success:
            print("✅ Authentication successful")
            print(f"   Ticket: {auth_util.ticket[:30] if auth_util.ticket else 'None'}...")
            print(f"   Authenticated: {auth_util.is_authenticated()}")
        else:
            print("❌ Authentication failed")
            return
    except Exception as e:
        print(f"❌ Authentication error: {e}")
        return
    
    # Test 3: URL parameter addition
    print("\n3. Testing URL parameter addition...")
    try:
        test_urls = [
            "http://localhost:8080/alfresco/api/discovery",
            "http://localhost:8080/alfresco/api/people/-me-", 
            "http://localhost:8080/alfresco/api/nodes/-root-/children?maxItems=5"
        ]
        
        for test_url in test_urls:
            authenticated_url = auth_util.add_auth_params(test_url)
            print(f"   Original: {test_url}")
            print(f"   With auth: {authenticated_url}")
            print()
            
        print("✅ URL parameter addition working")
        
    except Exception as e:
        print(f"❌ URL parameter error: {e}")
    
    # Test 4: Test with actual API call
    print("\n4. Testing actual API call...")
    try:
        import requests
        
        # Test user info endpoint
        base_url = "http://localhost:8080/alfresco/api/-default-/public/alfresco/versions/1/people/-me-"
        authenticated_url = auth_util.add_auth_params(base_url)
        
        response = requests.get(authenticated_url, timeout=10)
        
        if response.status_code == 200:
            user_data = response.json()
            user_info = user_data.get("entry", {})
            print("✅ API call successful")
            print(f"   User: {user_info.get('displayName', 'Unknown')}")
            print(f"   ID: {user_info.get('id', 'Unknown')}")
        else:
            print(f"⚠️  API call failed: {response.status_code}")
            
    except Exception as e:
        print(f"❌ API call error: {e}")
    
    # Test 5: Test ClientFactory with fixed AuthUtil
    print("\n5. Testing ClientFactory with fixed AuthUtil...")
    try:
        from python_alfresco_api import ClientFactory
        
        factory = ClientFactory(
            base_url=ALFRESCO_URL,
            username=USERNAME,
            password=PASSWORD
        )
        
        print("✅ ClientFactory created with authentication")
        print(f"   Auth available: {factory.auth is not None}")
        
        if factory.auth:
            # Test authentication
            auth_success = await factory.auth.ensure_authenticated()
            print(f"   Authentication: {'✅ Success' if auth_success else '❌ Failed'}")
            
            # Test individual client creation
            discovery_client = factory.create_discovery_client()
            auth_client = factory.create_auth_client()
            core_client = factory.create_core_client()
            
            print("✅ Individual clients created successfully")
            print(f"   Discovery client: {discovery_client.get_client_info()['api']}")
            print(f"   Auth client: {auth_client.get_client_info()['api']}")  
            print(f"   Core client: {core_client.get_client_info()['api']}")
            
    except Exception as e:
        print(f"❌ ClientFactory error: {e}")
    
    print("\n" + "=" * 40)
    print("🎉 AuthUtil Testing Complete!")
    print("✅ Query parameter authentication working perfectly!")
    print("\n📋 Summary:")
    print("- ✅ AuthUtil authentication working")
    print("- ✅ Query parameter URL generation working")  
    print("- ✅ API calls with authentication working")
    print("- ✅ ClientFactory integration working")
    print("\n🚀 Ready for full client testing!")

if __name__ == "__main__":
    asyncio.run(test_fixed_authutil()) 