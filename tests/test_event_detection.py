#!/usr/bin/env python3
"""
Event System Detection Test

Test the unified event client's ability to detect both Community (ActiveMQ) 
and Enterprise (Event Gateway) event systems.
"""

import asyncio
from python_alfresco_api.events import AlfrescoEventClient
import pytest
import sys
from pathlib import Path

# Add python_alfresco_api to path
sys.path.insert(0, str(Path(__file__).parent.parent / "python_alfresco_api"))

@pytest.mark.asyncio
async def test_event_detection():
    """Test event system detection"""
    print("=" * 60)
    print("ALFRESCO EVENT SYSTEM DETECTION TEST")
    print("=" * 60)
    
    # Create unified event client (auto-detects available systems)
    print("\n1. Initializing unified event client...")
    event_client = AlfrescoEventClient(
        alfresco_host="localhost",
        username="admin",
        password="admin",
        auto_detect=True
    )
    
    # Wait for detection to complete
    print("2. Running detection...")
    await asyncio.sleep(3)  # Give time for detection
    
    # Show detection results
    system_info = event_client.get_system_info()
    print("\n3. Detection Results:")
    print(f"   Event Gateway (Enterprise): {system_info['event_gateway_available']}")
    print(f"   ActiveMQ (Community): {system_info['activemq_available']}")
    print(f"   STOMP library installed: {system_info['stomp_installed']}")
    print(f"   Active system: {system_info['active_system']}")
    
    # Test subscription creation
    print("\n4. Testing subscription creation...")
    try:
        subscription_result = await event_client.setup_content_monitoring()
        print(f"   Subscription result: {subscription_result}")
        
        if subscription_result.get("success", True):
            print("   ✓ Subscription created successfully")
            
            # Setup event handlers
            print("\n5. Setting up event handlers...")
            event_client.setup_content_handlers()
            
            # Show handler count
            updated_info = event_client.get_system_info()
            print(f"   Handlers registered: {updated_info['handlers_registered']}")
            
            print("\n6. Testing event listening...")
            await event_client.start_listening()
            
        else:
            print(f"   ✗ Subscription failed: {subscription_result.get('error')}")
    
    except Exception as e:
        print(f"   ✗ Error during testing: {e}")
    
    # Summary
    print("\n" + "=" * 60)
    print("DETECTION SUMMARY")
    print("=" * 60)
    
    if system_info['active_system'] == 'enterprise':
        print("✓ ENTERPRISE EDITION detected")
        print("  → Event Gateway available on port 7070")
        print("  → Ready for REST API subscriptions")
        print("  → Webhook-based event delivery")
        
    elif system_info['active_system'] == 'community':
        print("✓ COMMUNITY EDITION detected")
        print("  → ActiveMQ available on port 61616")
        print("  → Ready for STOMP subscriptions")
        print("  → Topic-based event delivery")
        
    else:
        print("⚠ NO EVENT SYSTEM detected")
        print("  → Check if Alfresco is running")
        print("  → For Community: Ensure ActiveMQ is enabled")
        print("  → For Enterprise: Ensure Event Gateway is running")
        if not system_info['stomp_installed']:
            print("  → Install ActiveMQ support: pip install stomp.py")
    
    print(f"\nEvent client: {event_client}")
    print("Ready for Phase 2 event integration!")

async def main():
    """Main test execution"""
    try:
        await test_event_detection()
    except Exception as e:
        print(f"Test failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main()) 