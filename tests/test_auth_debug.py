#!/usr/bin/env python3
"""
Authentication Debug Test

Focuses on debugging the authentication ticket issue with Alfresco.
"""

import requests
import json

def debug_auth():
    """Debug authentication step by step"""
    
    BASE_URL = "http://localhost:8080"
    USERNAME = "admin"
    PASSWORD = "admin"
    
    print("🔍 Authentication Debug Test")
    print("=" * 40)
    
    # Step 1: Get ticket
    print("\n1. Getting authentication ticket...")
    auth_url = f"{BASE_URL}/alfresco/api/-default-/public/authentication/versions/1/tickets"
    auth_data = {"userId": USERNAME, "password": PASSWORD}
    
    try:
        print(f"POST {auth_url}")
        print(f"Body: {json.dumps(auth_data, indent=2)}")
        
        auth_response = requests.post(auth_url, json=auth_data, timeout=10)
        print(f"Status: {auth_response.status_code}")
        print(f"Headers: {dict(auth_response.headers)}")
        
        if auth_response.status_code == 201:
            response_data = auth_response.json()
            print(f"Response: {json.dumps(response_data, indent=2)}")
            
            ticket = response_data["entry"]["id"]
            print(f"\n✅ Ticket obtained: {ticket}")
            
            # Step 2: Try different authentication methods
            print(f"\n2. Testing authentication methods...")
            
            # Method 1: X-Alfresco-Ticket header
            print(f"\nMethod 1: X-Alfresco-Ticket header")
            headers1 = {"X-Alfresco-Ticket": ticket}
            test_url = f"{BASE_URL}/alfresco/api/-default-/public/alfresco/versions/1/people/-me-"
            
            print(f"GET {test_url}")
            print(f"Headers: {headers1}")
            
            response1 = requests.get(test_url, headers=headers1, timeout=10)
            print(f"Status: {response1.status_code}")
            if response1.status_code != 200:
                print(f"Error: {response1.text}")
            
            # Method 2: Basic Auth
            print(f"\nMethod 2: Basic Auth")
            from requests.auth import HTTPBasicAuth
            
            response2 = requests.get(test_url, auth=HTTPBasicAuth(USERNAME, PASSWORD), timeout=10)
            print(f"Status: {response2.status_code}")
            if response2.status_code == 200:
                print("✅ Basic Auth works!")
                user_data = response2.json()
                print(f"User: {user_data.get('entry', {}).get('displayName', 'Unknown')}")
            else:
                print(f"Error: {response2.text}")
            
            # Method 3: Ticket as query parameter
            print(f"\nMethod 3: Ticket as query parameter")
            test_url_with_ticket = f"{test_url}?alf_ticket={ticket}"
            
            response3 = requests.get(test_url_with_ticket, timeout=10)
            print(f"GET {test_url_with_ticket}")
            print(f"Status: {response3.status_code}")
            if response3.status_code == 200:
                print("✅ Query parameter ticket works!")
            else:
                print(f"Error: {response3.text}")
                
            # Method 4: Authorization header
            print(f"\nMethod 4: Authorization header")
            headers4 = {"Authorization": f"Basic {ticket}"}
            
            response4 = requests.get(test_url, headers=headers4, timeout=10)
            print(f"Status: {response4.status_code}")
            if response4.status_code == 200:
                print("✅ Authorization header works!")
            
        else:
            print(f"❌ Authentication failed: {auth_response.status_code}")
            print(f"Response: {auth_response.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print(f"\n" + "=" * 40)
    print("🏁 Debug Complete")

if __name__ == "__main__":
    debug_auth() 