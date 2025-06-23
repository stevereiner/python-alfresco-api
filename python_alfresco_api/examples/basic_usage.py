"""
Basic Usage Example - python-alfresco-api

Demonstrates the hybrid architecture with individual clients and factory pattern.
"""

import asyncio
from python_alfresco_api import ClientFactory
from python_alfresco_api.models import TicketBody

async def main():
    print("Python Alfresco API - Basic Usage Example")
    print("=" * 50)
    
    # Method 1: Factory pattern (recommended)
    print("\n1. Using Factory Pattern")
    factory = ClientFactory(
        base_url="https://alfresco.example.com",
        username="admin", 
        password="admin123"
    )
    
    # Create individual clients
    auth_client = factory.create_auth_client()
    core_client = factory.create_core_client()
    discovery_client = factory.create_discovery_client()
    
    print(f"   ✅ Created auth client: {auth_client.get_client_info()}")
    print(f"   ✅ Created core client: {core_client.get_client_info()}")
    print(f"   ✅ Created discovery client: {discovery_client.get_client_info()}")
    
    # Method 2: Individual clients
    print("\n2. Using Individual Clients")
    from python_alfresco_api import AlfrescoAuthClient, AlfrescoCoreClient
    
    auth_only = AlfrescoAuthClient("https://alfresco.example.com")
    core_only = AlfrescoCoreClient("https://alfresco.example.com")
    
    print(f"   Standalone auth client: {auth_only.is_available()}")
    print(f"   Standalone core client: {core_only.is_available()}")
    
    # Method 3: All clients at once
    print("\n3. Creating All Clients")
    all_clients = factory.create_all_clients()
    
    for api_name, client in all_clients.items():
        print(f"   {api_name.upper()} client: {client.is_available()}")
    
    print("\nAll examples completed successfully!")

if __name__ == "__main__":
    asyncio.run(main())
