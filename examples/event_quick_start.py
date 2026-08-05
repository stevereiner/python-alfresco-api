#!/usr/bin/env python3
"""
Quick Start Example - Alfresco Events

Simple example showing how to use the unified event client.
"""

import asyncio
from python_alfresco_api.events import AlfrescoEventClient, EventNotification

async def main():
    print("🚀 Alfresco Event Client - Quick Start")
    print("=" * 50)
    
    # 1. Create client (auto-detects ActiveMQ)
    print("\n1. Creating event client...")
    event_client = AlfrescoEventClient(
        alfresco_host="localhost",    # No port - handled automatically
        username="admin",             # Default Alfresco credentials
        password="admin",
        auto_detect=True,            # Auto-detect available systems
        debug=True                   # Show debug info
    )
    
    # 2. Wait for detection
    print("2. Detecting event systems...")
    await asyncio.sleep(2)
    
    # 3. Show what was detected
    system_info = event_client.get_system_info()
    print("\n3. Detection Results:")
    print(f"   📨 ActiveMQ: {system_info['activemq_available']}")
    print(f"   📚 STOMP library: {system_info['stomp_installed']}")
    print(f"   ⚡ Active system: {system_info.get('active_system', 'none')}")
    
    # 4. Register custom event handler
    print("\n4. Setting up event handlers...")
    
    async def my_content_handler(notification: EventNotification):
        print(f"📄 Content Event: {notification.event_type}")
        if notification.node_id:
            print(f"   Node: {notification.node_id}")
        if notification.user_id:
            print(f"   User: {notification.user_id}")
    
    # Register for node events
    event_client.register_event_handler("node.created", my_content_handler)
    event_client.register_event_handler("node.updated", my_content_handler)
    event_client.register_event_handler("node.deleted", my_content_handler)
    
    # 5. Setup content monitoring
    print("5. Setting up content monitoring...")
    subscription_result = await event_client.setup_content_monitoring()
    print(f"   Result: {subscription_result}")
    
    if subscription_result.get("success", True):
        print("   ✅ Content monitoring active!")
        
        # 6. Start listening
        print("6. Starting event listener...")
        await event_client.start_listening()
        
        print("\n🎯 Event system ready!")
        print(f"   Client: {event_client}")
        
    else:
        print("   ⚠️  Content monitoring setup failed")
        print(f"   Error: {subscription_result.get('error', 'Unknown')}")
    
    # 7. Summary
    print("\n" + "=" * 50)
    print("📋 QUICK START SUMMARY")
    print("=" * 50)
    
    if system_info.get('active_system') == 'enterprise':
        print("🏢 ENTERPRISE EDITION Active")
        print("   → Event Gateway on port 7070")
        print("   → REST API subscriptions")
        
    elif system_info.get('active_system') == 'community':
        print("🏘️  COMMUNITY EDITION Active") 
        print("   → ActiveMQ on port 61616")
        print("   → STOMP subscriptions")
        
    else:
        print("❌ NO EVENT SYSTEM DETECTED")
        print("   💡 Tips:")
        print("   • Make sure Alfresco is running")
        print("   • For Community: Enable ActiveMQ")
        print("   • For Enterprise: Start Event Gateway")
        if not system_info['stomp_installed']:
            print("   • Install: pip install stomp.py")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Bye!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc() 