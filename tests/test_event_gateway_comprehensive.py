#!/usr/bin/env python3
"""
Comprehensive Event System Tests

Tests for both Community Edition (ActiveMQ) and Enterprise Edition (Event Gateway) event systems.

Configuration:
- Set EVENT_MODE environment variable to test specific mode:
  * 'community' (default) - Test ActiveMQ/STOMP (port 61616)
  * 'enterprise' - Test Event Gateway/REST (port 7070) 
  * 'both' - Test both with mocking
- Set ALFRESCO_HOST to change host (default: localhost)

Examples:
  pytest tests/test_event_gateway_comprehensive.py  # Default: community mode
  EVENT_MODE=enterprise pytest tests/test_event_gateway_comprehensive.py
  EVENT_MODE=both pytest tests/test_event_gateway_comprehensive.py
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

class TestEventSystemComprehensive:
    
    @pytest.mark.asyncio
    async def test_event_client_initialization(self):
        """Test event client initialization with different configurations"""
        
        # Basic initialization with correct parameters
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
        
    @pytest.mark.asyncio
    async def test_enterprise_detection_success(self):
        """Test successful Enterprise Event Gateway detection"""
        
        with patch('httpx.AsyncClient') as mock_client:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_client.return_value.__aenter__.return_value.get = AsyncMock(return_value=mock_response)
            
            client = AlfrescoEventClient(auto_detect=False)
            await client._check_event_gateway()
            
            assert client.event_gateway_available is True
    
    @pytest.mark.asyncio
    async def test_enterprise_detection_failure(self):
        """Test failed Enterprise Event Gateway detection"""
        
        with patch('httpx.AsyncClient') as mock_client:
            mock_client.return_value.__aenter__.return_value.get = AsyncMock(
                side_effect=httpx.RequestError("Connection failed")
            )
            
            client = AlfrescoEventClient(auto_detect=False)
            await client._check_event_gateway()
            
            assert client.event_gateway_available is False
    
    @pytest.mark.asyncio
    async def test_community_detection_success(self):
        """Test successful Community ActiveMQ detection"""
        
        with patch('python_alfresco_api.events.event_client.STOMP_AVAILABLE', True):
            with patch('stomp.Connection') as mock_connection:
                mock_conn = Mock()
                mock_conn.connect = Mock()
                mock_conn.disconnect = Mock()
                mock_connection.return_value = mock_conn
                
                client = AlfrescoEventClient(auto_detect=False)
                await client._check_activemq()
                
                assert client.activemq_available is True
    
    @pytest.mark.asyncio
    async def test_community_detection_no_stomp(self):
        """Test Community detection when stomp.py not available"""
        
        with patch('python_alfresco_api.events.event_client.STOMP_AVAILABLE', False):
            client = AlfrescoEventClient(auto_detect=False)
            await client._check_activemq()
            
            assert client.activemq_available is False
    
    @pytest.mark.asyncio
    async def test_community_detection_connection_failure(self):
        """Test Community detection when ActiveMQ connection fails"""
        
        with patch('python_alfresco_api.events.event_client.STOMP_AVAILABLE', True):
            with patch('stomp.Connection') as mock_connection:
                mock_connection.side_effect = Exception("Connection failed")
                
                client = AlfrescoEventClient(auto_detect=False)
                await client._check_activemq()
                
                assert client.activemq_available is False
    
    @pytest.mark.asyncio
    async def test_system_detection_priority(self):
        """Test system detection priority (Enterprise over Community)"""
        
        client = AlfrescoEventClient(auto_detect=False)
        client.event_gateway_available = True
        client.activemq_available = True
        
        await client._detect_event_systems()
        
        assert client.event_system == "enterprise"
    
    @pytest.mark.asyncio
    async def test_system_detection_community_fallback(self):
        """Test fallback to Community when Enterprise not available"""
        
        client = AlfrescoEventClient(auto_detect=False)
        client.event_gateway_available = False
        client.activemq_available = True
        
        await client._detect_event_systems()
        
        assert client.event_system == "community"
    
    @pytest.mark.asyncio
    async def test_system_detection_none_available(self):
        """Test when no event system is available"""
        
        client = AlfrescoEventClient(auto_detect=False)
        client.event_gateway_available = False
        client.activemq_available = False
        
        await client._detect_event_systems()
        
        assert client.event_system is None
    
    @pytest.mark.asyncio
    async def test_enterprise_subscription_success(self):
        """Test successful Enterprise subscription creation"""
        
        subscription = EventSubscription(
            name="Test Subscription",
            events=["node.created", "node.updated"],
            filter_expression="nodeType:cm:content"  # Use string format filter
        )
        
        with patch('httpx.AsyncClient') as mock_client:
            mock_response = Mock()
            mock_response.raise_for_status = Mock()
            mock_response.json.return_value = {"id": "sub123", "status": "active"}
            mock_client.return_value.__aenter__.return_value.post = AsyncMock(return_value=mock_response)
            
            client = AlfrescoEventClient(auto_detect=False)
            client.event_system = "enterprise"
            
            result = await client._create_subscription_enterprise(subscription)
            
            assert result["id"] == "sub123"
            assert result["status"] == "active"
    
    @pytest.mark.asyncio
    async def test_enterprise_subscription_failure(self):
        """Test failed Enterprise subscription creation"""
        
        subscription = EventSubscription(
            name="Test Subscription",
            events=["node.created"]
        )
        
        with patch('httpx.AsyncClient') as mock_client:
            mock_client.return_value.__aenter__.return_value.post = AsyncMock(
                side_effect=httpx.RequestError("Server error")
            )
            
            client = AlfrescoEventClient(auto_detect=False)
            client.event_system = "enterprise"
            
            result = await client._create_subscription_enterprise(subscription)
            
            assert result["success"] is False
            assert "error" in result
    
    @pytest.mark.asyncio
    async def test_community_subscription_success(self):
        """Test successful Community subscription creation"""
        
        subscription = EventSubscription(
            name="Test Subscription",
            events=["node.created", "node.updated"]
        )
        
        with patch('python_alfresco_api.events.event_client.STOMP_AVAILABLE', True):
            client = AlfrescoEventClient(auto_detect=False)
            client.event_system = "community"
            
            result = await client._create_subscription_community(subscription)
            
            assert result["success"] is True
            assert result["system"] == "activemq"
            assert result["events"] == ["node.created", "node.updated"]
    
    @pytest.mark.asyncio
    async def test_community_subscription_no_stomp(self):
        """Test Community subscription when stomp.py not available"""
        
        subscription = EventSubscription(
            name="Test Subscription",
            events=["node.created"]
        )
        
        with patch('python_alfresco_api.events.event_client.STOMP_AVAILABLE', False):
            client = AlfrescoEventClient(auto_detect=False)
            client.event_system = "community"
            
            result = await client._create_subscription_community(subscription)
            
            assert result["success"] is False
            assert "stomp.py not installed" in result["error"]
    
    @pytest.mark.asyncio
    async def test_unified_subscription_api(self):
        """Test unified subscription API routing"""
        
        subscription = EventSubscription(
            name="Test Subscription",
            events=["node.created"]
        )
        
        # Test Enterprise routing
        client = AlfrescoEventClient(auto_detect=False)
        client.event_system = "enterprise"
        
        with patch.object(client, '_create_subscription_enterprise') as mock_enterprise:
            mock_enterprise.return_value = {"success": True}
            
            result = await client.create_subscription(subscription)
            mock_enterprise.assert_called_once_with(subscription)
        
        # Test Community routing
        client.event_system = "community"
        
        with patch.object(client, '_create_subscription_community') as mock_community:
            mock_community.return_value = {"success": True}
            
            result = await client.create_subscription(subscription)
            mock_community.assert_called_once_with(subscription)
        
        # Test no system available
        client.event_system = None
        
        result = await client.create_subscription(subscription)
        
        assert result["success"] is False
        assert "No event system available" in result["error"]
    
    def test_event_handler_registration(self):
        """Test event handler registration"""
        
        client = AlfrescoEventClient(auto_detect=False)
        
        def sync_handler(notification):
            pass
        
        async def async_handler(notification):
            pass
        
        # Register handlers
        client.register_event_handler("node.created", sync_handler)
        client.register_event_handler("node.updated", async_handler)
        client.register_event_handler("node.created", async_handler)  # Multiple handlers for same event
        
        assert len(client.event_handlers["node.created"]) == 2
        assert len(client.event_handlers["node.updated"]) == 1
        assert sync_handler in client.event_handlers["node.created"]
        assert async_handler in client.event_handlers["node.created"]
        assert async_handler in client.event_handlers["node.updated"]
    
    @pytest.mark.asyncio
    async def test_content_monitoring_setup(self):
        """Test content monitoring setup"""
        
        client = AlfrescoEventClient(auto_detect=False)
        client.event_system = "enterprise"
        
        with patch.object(client, 'create_subscription') as mock_create:
            mock_create.return_value = {"success": True, "id": "sub123"}
            
            result = await client.setup_content_monitoring()
            
            assert result["success"] is True
            mock_create.assert_called_once()
            
            # Check subscription details
            call_args = mock_create.call_args[0][0]
            assert call_args.name == "Content Monitoring"
            assert "node.created" in call_args.events
            assert "node.updated" in call_args.events
            assert "node.deleted" in call_args.events
            assert call_args.filter["nodeType"] == "cm:content"
    
    def test_content_handlers_setup(self):
        """Test default content handlers setup"""
        
        client = AlfrescoEventClient(auto_detect=False)
        client.setup_content_handlers()
        
        assert "node.created" in client.event_handlers
        assert "node.updated" in client.event_handlers
        assert "node.deleted" in client.event_handlers
        
        assert len(client.event_handlers["node.created"]) == 1
        assert len(client.event_handlers["node.updated"]) == 1
        assert len(client.event_handlers["node.deleted"]) == 1
    
    @pytest.mark.asyncio
    async def test_start_listening_enterprise(self):
        """Test start listening for Enterprise system"""
        
        client = AlfrescoEventClient(auto_detect=False)
        client.event_system = "enterprise"
        
        # Should not raise an exception
        await client.start_listening()
    
    @pytest.mark.asyncio
    async def test_start_listening_community(self):
        """Test start listening for Community system"""
        
        with patch('python_alfresco_api.events.event_client.STOMP_AVAILABLE', True):
            client = AlfrescoEventClient(auto_detect=False)
            client.event_system = "community"
            
            # Should not raise an exception
            await client.start_listening()
    
    @pytest.mark.asyncio
    async def test_start_listening_community_no_stomp(self):
        """Test start listening for Community system without stomp.py"""
        
        with patch('python_alfresco_api.events.event_client.STOMP_AVAILABLE', False):
            client = AlfrescoEventClient(auto_detect=False)
            client.event_system = "community"
            
            # Should not raise an exception
            await client.start_listening()
    
    @pytest.mark.asyncio
    async def test_start_listening_no_system(self):
        """Test start listening when no system available"""
        
        client = AlfrescoEventClient(auto_detect=False)
        client.event_system = None
        
        # Should not raise an exception
        await client.start_listening()
    
    def test_system_info(self):
        """Test system info retrieval"""
        
        client = AlfrescoEventClient(auto_detect=False)
        client.event_gateway_available = True
        client.activemq_available = False
        client.event_system = "enterprise"
        client.register_event_handler("node.created", lambda x: None)
        client.register_event_handler("node.updated", lambda x: None)
        
        info = client.get_system_info()
        
        assert info["event_gateway_available"] is True
        assert info["activemq_available"] is False
        assert info["active_system"] == "enterprise"
        assert info["handlers_registered"] == 2
        assert "stomp_installed" in info
    
    def test_client_representation(self):
        """Test client string representation"""
        
        client = AlfrescoEventClient(
            alfresco_host="test-host",
            auto_detect=False
        )
        client.event_system = "enterprise"
        
        repr_str = repr(client)
        
        assert "AlfrescoEventClient" in repr_str
        assert "enterprise" in repr_str
        assert "test-host" in repr_str
    
    def test_event_subscription_model(self):
        """Test EventSubscription model"""
        
        subscription = EventSubscription(
            name="Test Sub",
            description="Test Description",
            events=["node.created", "node.updated"],
            filter={"nodeType": "cm:content"},
            webhook_url="http://example.com/webhook",
            active=True
        )
        
        assert subscription.name == "Test Sub"
        assert subscription.description == "Test Description"
        assert len(subscription.events) == 2
        assert subscription.filter["nodeType"] == "cm:content"
        assert subscription.webhook_url == "http://example.com/webhook"
        assert subscription.active is True
        
        # Test model dump
        data = subscription.model_dump(exclude_none=True)
        assert "name" in data
        assert "events" in data
        assert "id" not in data  # Should be excluded because it's None
    
    def test_event_notification_model(self):
        """Test EventNotification model"""
        
        timestamp = datetime.now()
        notification = EventNotification(
            event_type="node.created",
            node_id="workspace://SpacesStore/abc123",
            node_type="cm:content",
            user_id="admin",
            timestamp=timestamp,
            data={"name": "test.pdf", "size": 1024}
        )
        
        assert notification.event_type == "node.created"
        assert notification.node_id == "workspace://SpacesStore/abc123"
        assert notification.node_type == "cm:content"
        assert notification.user_id == "admin"
        assert notification.timestamp == timestamp
        assert notification.data["name"] == "test.pdf"
        assert notification.data["size"] == 1024

@pytest.mark.asyncio
async def test_example_usage():
    """Test the example usage pattern"""
    
    # Mock the detection methods
    with patch('python_alfresco_api.events.event_client.AlfrescoEventClient._detect_event_systems'):
        client = AlfrescoEventClient(
            alfresco_host="localhost",
            username="admin",
            password="admin",
            auto_detect=True
        )
        
        # Mock system as Enterprise
        client.event_gateway_available = True
        client.activemq_available = False
        client.event_system = "enterprise"
        
        # Test system info
        info = client.get_system_info()
        assert info["active_system"] == "enterprise"
        
        # Test setup with mocked subscription
        with patch.object(client, 'create_subscription') as mock_create:
            mock_create.return_value = {"success": True}
            
            result = await client.setup_content_monitoring()
            assert result["success"] is True
            
            # Setup handlers
            client.setup_content_handlers()
            assert len(client.event_handlers) == 3
            
            # Test start listening
            await client.start_listening()

if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 