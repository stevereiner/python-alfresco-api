#!/usr/bin/env python3
"""
Event System Tests - Community & Enterprise Support

Tests for both Community Edition (ActiveMQ) and Enterprise Edition (Event Gateway) event systems.

Configuration:
- Set EVENT_MODE environment variable to test specific mode:
  * 'community' (default) - Test ActiveMQ/STOMP (port 61616)
  * 'enterprise' - Test Event Gateway/REST (port 7070) 
  * 'both' - Test both modes with mocking
- Set ALFRESCO_HOST to change host (default: localhost)

Examples:
  pytest tests/test_event_community_enterprise.py  # Default: community mode
  EVENT_MODE=enterprise pytest tests/test_event_community_enterprise.py
  EVENT_MODE=both pytest tests/test_event_community_enterprise.py
"""

import asyncio
import pytest
import os
from unittest.mock import Mock, patch, AsyncMock
from python_alfresco_api.events.event_client import AlfrescoEventClient
from python_alfresco_api.events.models import EventSubscription, EventNotification
import httpx
from datetime import datetime

# Test configuration - configurable via environment variables
EVENT_MODE = os.getenv('EVENT_MODE', 'community')  # 'community', 'enterprise', or 'both'
ALFRESCO_HOST = os.getenv('ALFRESCO_HOST', 'localhost')
ACTIVEMQ_PORT = int(os.getenv('ACTIVEMQ_PORT', '61616'))
EVENT_GATEWAY_PORT = int(os.getenv('EVENT_GATEWAY_PORT', '7070'))

# Test conditions based on mode
SKIP_COMMUNITY = EVENT_MODE == 'enterprise'
SKIP_ENTERPRISE = EVENT_MODE == 'community'

class TestEventSystemConfiguration:
    """Test event system configuration and initialization"""

    def test_environment_configuration(self):
        """Test that environment configuration works correctly"""
        print(f"\n🔧 Event System Configuration:")
        print(f"   - Mode: {EVENT_MODE}")
        print(f"   - Host: {ALFRESCO_HOST}")
        print(f"   - ActiveMQ Port: {ACTIVEMQ_PORT}")
        print(f"   - Event Gateway Port: {EVENT_GATEWAY_PORT}")
        
        assert EVENT_MODE in ['community', 'enterprise', 'both']
        assert ALFRESCO_HOST
        assert ACTIVEMQ_PORT > 0
        assert EVENT_GATEWAY_PORT > 0

    def test_client_initialization_basic(self):
        """Test basic client initialization with correct parameters"""
        
        client = AlfrescoEventClient(
            alfresco_host=ALFRESCO_HOST,
            username="admin",
            password="admin",
            community_port=ACTIVEMQ_PORT,
            enterprise_port=EVENT_GATEWAY_PORT,
            auto_detect=False,
            debug=True
        )
        
        assert client.alfresco_host == ALFRESCO_HOST
        assert client.username == "admin"
        assert client.password == "admin"
        assert client.community_port == ACTIVEMQ_PORT
        assert client.enterprise_port == EVENT_GATEWAY_PORT
        assert client.event_system is None
        assert len(client.event_handlers) == 0
        
        print(f"✅ Client initialized successfully for {EVENT_MODE} mode")

class TestCommunityEventSystem:
    """Test Community Edition (ActiveMQ) event system"""

    @pytest.mark.skipif(SKIP_COMMUNITY, reason=f"Community tests skipped in {EVENT_MODE} mode")
    def test_community_client_creation(self):
        """Test Community client creation and basic properties"""
        
        client = AlfrescoEventClient(
            alfresco_host=ALFRESCO_HOST,
            username="admin",
            password="admin",
            community_port=ACTIVEMQ_PORT,
            auto_detect=False,
            debug=True
        )
        
        # Test system info
        info = client.get_system_info()
        assert 'community' in info
        assert info['community']['port'] == ACTIVEMQ_PORT
        
        print(f"✅ Community client created for ActiveMQ on port {ACTIVEMQ_PORT}")

    @pytest.mark.skipif(SKIP_COMMUNITY, reason=f"Community tests skipped in {EVENT_MODE} mode")
    def test_community_subscription_model(self):
        """Test subscription model for community edition"""
        
        # Test with correct model attributes from the actual model
        subscription = EventSubscription(
            name="Community Test Subscription",
            events=["node.created", "node.updated"],
            filter_expression="cm:content",  # String filter expression
            callback_url="http://localhost:8081/webhooks"
        )
        
        assert subscription.name == "Community Test Subscription"
        assert "node.created" in subscription.events
        assert subscription.filter_expression == "cm:content"
        assert subscription.callback_url == "http://localhost:8081/webhooks"
        
        print("✅ Community subscription model created successfully")

    @pytest.mark.skipif(SKIP_COMMUNITY, reason=f"Community tests skipped in {EVENT_MODE} mode")
    @pytest.mark.asyncio
    async def test_community_subscription_creation_mock(self):
        """Test Community subscription creation with mocking"""
        
        subscription = EventSubscription(
            name="Test Community Subscription",
            events=["node.created"]
        )
        
        with patch('python_alfresco_api.events.event_client.STOMP_AVAILABLE', True):
            client = AlfrescoEventClient(
                alfresco_host=ALFRESCO_HOST,
                username="admin",
                password="admin",
                auto_detect=False
            )
            client.event_system = "community"
            
            # Mock the subscription creation
            result = await client._create_subscription_community(subscription)
            
            assert result["success"] is True
            assert result["system"] == "activemq"
            
        print("✅ Community subscription creation test passed")

class TestEnterpriseEventSystem:
    """Test Enterprise Edition (Event Gateway) event system"""

    @pytest.mark.skipif(SKIP_ENTERPRISE, reason=f"Enterprise tests skipped in {EVENT_MODE} mode")
    def test_enterprise_client_creation(self):
        """Test Enterprise client creation and basic properties"""
        
        client = AlfrescoEventClient(
            alfresco_host=ALFRESCO_HOST,
            username="admin",
            password="admin",
            enterprise_port=EVENT_GATEWAY_PORT,
            auto_detect=False,
            debug=True
        )
        
        # Test system info
        info = client.get_system_info()
        assert 'enterprise' in info
        assert info['enterprise']['port'] == EVENT_GATEWAY_PORT
        
        print(f"✅ Enterprise client created for Event Gateway on port {EVENT_GATEWAY_PORT}")

    @pytest.mark.skipif(SKIP_ENTERPRISE, reason=f"Enterprise tests skipped in {EVENT_MODE} mode")
    @pytest.mark.asyncio
    async def test_enterprise_subscription_creation_mock(self):
        """Test Enterprise subscription creation with mocking"""
        
        subscription = EventSubscription(
            name="Test Enterprise Subscription",
            events=["node.created", "node.updated"]
        )
        
        with patch('httpx.AsyncClient') as mock_client:
            mock_response = Mock()
            mock_response.raise_for_status = Mock()
            mock_response.json.return_value = {"id": "sub123", "status": "active"}
            mock_client.return_value.__aenter__.return_value.post = AsyncMock(return_value=mock_response)
            
            client = AlfrescoEventClient(
                alfresco_host=ALFRESCO_HOST,
                username="admin",
                password="admin",
                auto_detect=False
            )
            client.event_system = "enterprise"
            
            result = await client._create_subscription_enterprise(subscription)
            
            assert result["id"] == "sub123"
            assert result["status"] == "active"
        
        print("✅ Enterprise subscription creation test passed")

class TestUnifiedEventAPI:
    """Test unified event API that works with both systems"""

    def test_event_handler_registration(self):
        """Test event handler registration (works for both systems)"""
        
        client = AlfrescoEventClient(
            alfresco_host=ALFRESCO_HOST,
            username="admin",
            password="admin",
            auto_detect=False
        )
        
        def sync_handler(notification):
            pass
        
        async def async_handler(notification):
            pass
        
        # Register handlers
        client.register_event_handler("node.created", sync_handler)
        client.register_event_handler("node.updated", async_handler)
        client.register_event_handler("node.created", async_handler)  # Multiple handlers
        
        assert len(client.event_handlers["node.created"]) == 2
        assert len(client.event_handlers["node.updated"]) == 1
        assert sync_handler in client.event_handlers["node.created"]
        assert async_handler in client.event_handlers["node.created"]
        assert async_handler in client.event_handlers["node.updated"]
        
        print("✅ Event handler registration test passed")

    def test_event_notification_model(self):
        """Test event notification model"""
        
        # Test with correct model attributes
        notification = EventNotification(
            event_type="node.created",
            node_id="some-node-id",  # Use correct attribute name
            timestamp=datetime.now(),
            user="admin",
            data={"path": "/Company Home/test.txt"}
        )
        
        assert notification.event_type == "node.created"
        assert notification.node_id == "some-node-id"
        assert notification.user == "admin"
        assert notification.data["path"] == "/Company Home/test.txt"
        
        print("✅ Event notification model test passed")

    def test_system_info_unified(self):
        """Test system info for both configurations"""
        
        client = AlfrescoEventClient(
            alfresco_host=ALFRESCO_HOST,
            username="admin",
            password="admin",
            community_port=ACTIVEMQ_PORT,
            enterprise_port=EVENT_GATEWAY_PORT,
            auto_detect=False
        )
        
        info = client.get_system_info()
        
        # Should have info for both systems
        assert 'community' in info
        assert 'enterprise' in info
        assert info['community']['port'] == ACTIVEMQ_PORT
        assert info['enterprise']['port'] == EVENT_GATEWAY_PORT
        assert info['mode'] == EVENT_MODE
        
        print(f"✅ System info test passed for {EVENT_MODE} mode")

@pytest.mark.asyncio
async def test_example_usage():
    """Example usage that demonstrates the configurable approach"""
    
    print(f"\n🚀 Example Usage - {EVENT_MODE.title()} Mode")
    print("=" * 50)
    
    # Create client with current configuration
    client = AlfrescoEventClient(
        alfresco_host=ALFRESCO_HOST,
        username="admin",
        password="admin",
        community_port=ACTIVEMQ_PORT,
        enterprise_port=EVENT_GATEWAY_PORT,
        auto_detect=False,
        debug=True
    )
    
    # Register a simple event handler
    def handle_node_created(notification):
        print(f"📄 Node created: {notification.node_id}")
    
    client.register_event_handler("node.created", handle_node_created)
    
    # Create subscription based on mode
    subscription = EventSubscription(
        name=f"Example {EVENT_MODE.title()} Subscription",
        events=["node.created", "node.updated"],
        filter_expression="cm:content"
    )
    
    print(f"✅ Example configured for {EVENT_MODE} mode")
    print(f"   - ActiveMQ Port: {ACTIVEMQ_PORT}")
    print(f"   - Event Gateway Port: {EVENT_GATEWAY_PORT}")
    print(f"   - Event handlers registered: {len(client.event_handlers)}")

if __name__ == "__main__":
    print(f"🧪 Event System Tests")
    print(f"Mode: {EVENT_MODE}")
    print(f"Host: {ALFRESCO_HOST}")
    print("Run with: pytest tests/test_event_community_enterprise.py -v") 