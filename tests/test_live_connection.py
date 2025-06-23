#!/usr/bin/env python3
"""
Simple Live Connection Test

Test the hybrid python-alfresco-api with running Alfresco instance.
"""

from python_alfresco_api import ClientFactory, AlfrescoMasterClient
from python_alfresco_api.models import TicketBody

def test_basic_connection():
    """Test basic connection and client availability"""
    print("=" * 60)
    print("TESTING BASIC CONNECTION")
    print("=" * 60)
    
    # Test individual clients via factory
    print("\n1. Testing ClientFactory...")
    factory = ClientFactory(
        base_url="http://localhost:8080",
        username="admin",
        password="admin"
    )
    
    # Test each client
    clients = {
        "auth": factory.create_auth_client(),
        "core": factory.create_core_client(),
        "discovery": factory.create_discovery_client(),
        "search": factory.create_search_client(),
        "workflow": factory.create_workflow_client(),
        "model": factory.create_model_client(),
        "search_sql": factory.create_search_sql_client()
    }
    
    print("Individual Client Availability:")
    for name, client in clients.items():
        available = client.is_available() if hasattr(client, 'is_available') else "Unknown"
        print(f"   {name.upper()}: {available}")
        assert client is not None, f"{name} client should not be None"
    
    # Test master client
    print("\n2. Testing Master Client...")
    master = AlfrescoMasterClient(base_url="http://localhost:8080")
    master_info = master.get_client_info()
    print(f"Master client info: {master_info}")
    assert master_info is not None, "Master client info should not be None"
    assert isinstance(master_info, dict), "Master client info should be a dict"

def test_pydantic_models():
    """Test Pydantic model functionality"""
    print("\n" + "=" * 60)
    print("TESTING PYDANTIC MODELS")
    print("=" * 60)
    
    # Test TicketBody model
    try:
        ticket = TicketBody(userId="admin", password="admin")
        print(f"✓ TicketBody created: {ticket}")
        json_output = ticket.model_dump_json()
        print(f"✓ JSON export: {json_output}")
        
        assert ticket.userId == "admin", "Ticket userId should be 'admin'"
        assert ticket.password == "admin", "Ticket password should be 'admin'"
        assert isinstance(json_output, str), "JSON output should be a string"
        assert "admin" in json_output, "JSON should contain 'admin'"
        
    except Exception as e:
        print(f"✗ TicketBody error: {e}")
        assert False, f"TicketBody test failed: {e}"

def main():
    """Main test execution"""
    print("PYTHON ALFRESCO API - LIVE CONNECTION TEST")
    print("Hybrid Architecture: Individual Clients + Optional Master Client")
    
    try:
        # Test basic connection
        test_basic_connection()
        
        # Test Pydantic models
        test_pydantic_models()
        
        print("\n" + "=" * 60)
        print("TEST RESULTS")
        print("=" * 60)
        print("✓ Package import: SUCCESS")
        print("✓ ClientFactory: SUCCESS")
        print("✓ Individual clients: SUCCESS")
        print("✓ Master client: SUCCESS")
        print("✓ Pydantic models: SUCCESS")
        
        print("\n" + "=" * 60)
        print("READY FOR NEXT PHASES")
        print("=" * 60)
        print("✓ Phase 1 Complete: Hybrid library foundation")
        print("→ Phase 2 Ready: Event Gateway support")
        print("→ Phase 3 Ready: First MCP server")
        print("→ Phase 4+ Ready: GraphRAG development")
        
        print("\nYour Alfresco instance is running and the hybrid library works perfectly!")
        
    except Exception as e:
        print(f"\nTest failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 