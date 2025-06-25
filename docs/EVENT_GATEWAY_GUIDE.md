# Alfresco Event Gateway Integration Guide

## Overview

The python-alfresco-api now includes **unified event system support** for both Community Edition (ActiveMQ) and Enterprise Edition (Event Gateway). This implements [the memory about unified event client][[memory:7162100363690079610]] with automatic detection and graceful fallback capabilities.

## Features

- ✅ **Auto-detection** of Community vs Enterprise event systems
- ✅ **Unified API** - same code works with both editions
- ✅ **Community Edition**: ActiveMQ STOMP integration (port 61616)
- ✅ **Enterprise Edition**: Event Gateway REST API (port 7070)
- ✅ **Graceful fallback** when systems aren't available
- ✅ **Standardized event format** for both editions
- ✅ **Ready for 30-day Enterprise trial testing**

## Quick Start

### Basic Usage

```python
import asyncio
from python_alfresco_api.event_client import AlfrescoEventClient

async def main():
    # Initialize unified event client (auto-detects Community vs Enterprise)
    event_client = AlfrescoEventClient(
        alfresco_host="localhost",
        username="admin",
        password="admin",
        auto_detect=True
    )
    
    # Wait for detection to complete
    await asyncio.sleep(2)
    
    # Show system info
    system_info = event_client.get_system_info()
    print(f"Active system: {system_info['active_system']}")
    
    # Setup content monitoring (works with both editions)
    subscription_result = await event_client.setup_content_monitoring()
    
    if subscription_result.get("success", True):
        # Setup event handlers
        event_client.setup_content_handlers()
        
        # Start listening
        await event_client.start_listening()

if __name__ == "__main__":
    asyncio.run(main())
```

### Custom Event Handlers

```python
from python_alfresco_api.event_client import EventNotification

async def custom_handler(notification: EventNotification):
    print(f"Event: {notification.event_type}")
    print(f"Node: {notification.node_id}")
    print(f"User: {notification.user_id}")
    print(f"Data: {notification.data}")

# Register custom handler
event_client.register_event_handler("node.created", custom_handler)
```

## System Detection

The event client automatically detects which system is available:

```python
system_info = event_client.get_system_info()
print(system_info)
# Output:
# {
#     "event_gateway_available": True,    # Enterprise Edition
#     "activemq_available": False,        # Community Edition  
#     "active_system": "enterprise",      # Which system is being used
#     "stomp_installed": True,            # Whether stomp.py is available
#     "handlers_registered": 3            # Number of registered handlers
# }
```

## Community Edition (ActiveMQ)

For Community Edition, you need the `stomp.py` library:

```bash
pip install stomp.py
```

### ActiveMQ Configuration

- **Port**: 61613 (STOMP protocol)
- **Topics**: `/topic/alfresco.node.created`, `/topic/alfresco.node.updated`, etc.
- **Protocol**: STOMP over TCP

### Example Community Setup

```python
# Community Edition automatically detected
event_client = AlfrescoEventClient(
    alfresco_host="localhost",
    username="admin", 
    password="admin"
)

# Topics are automatically configured:
# - /topic/alfresco.node.created
# - /topic/alfresco.node.updated  
# - /topic/alfresco.node.deleted
```

## Enterprise Edition (Event Gateway)

Enterprise Edition uses the Event Gateway REST API:

- **Port**: 7070
- **Protocol**: HTTP/REST
- **Authentication**: Basic Auth or OAuth
- **Delivery**: Webhook-based

### Example Enterprise Setup

```python
# Enterprise Edition automatically detected
event_client = AlfrescoEventClient(
    alfresco_host="localhost",
    username="admin",
    password="admin"
)

# Subscription via REST API
subscription = EventSubscription(
    name="Content Monitoring",
    events=["node.created", "node.updated", "node.deleted"],
    webhook_url="http://your-app.com/webhook",
    filter={"nodeType": "cm:content"}
)

result = await event_client.create_subscription(subscription)
```

## Event Types

Standard Alfresco events supported:

- `node.created` - Content created
- `node.updated` - Content modified
- `node.deleted` - Content deleted
- `node.moved` - Content moved
- `user.created` - User created
- `permission.changed` - Permissions modified

## Event Notification Format

All events use the standardized `EventNotification` format:

```python
from python_alfresco_api.event_client import EventNotification

notification = EventNotification(
    event_type="node.created",
    node_id="workspace://SpacesStore/abc123",
    node_type="cm:content",
    user_id="admin",
    timestamp=datetime.now(),
    data={
        "name": "document.pdf",
        "path": "/Company Home/Documents",
        "size": 1024
    }
)
```

## Error Handling

The event client provides graceful error handling:

```python
try:
    subscription_result = await event_client.setup_content_monitoring()
    
    if not subscription_result.get("success", True):
        print(f"Failed: {subscription_result.get('error')}")
        
except Exception as e:
    print(f"Error: {e}")
```

## Testing

Run the event detection test:

```bash
python -m pytest tests/test_event_detection.py -v
```

Or run the example directly:

```bash
python python_alfresco_api/event_client.py
```

## Configuration

### Environment Variables

```bash
export ALFRESCO_HOST=localhost
export ALFRESCO_USERNAME=admin
export ALFRESCO_PASSWORD=admin
export EVENT_GATEWAY_PORT=7070
export ACTIVEMQ_PORT=61613
```

### Using Configuration Files

```python
from python_alfresco_api.event_client import AlfrescoEventClient

# Load from config
event_client = AlfrescoEventClient.from_config("config/events.yaml")
```

## Integration Architecture

This event system provides real-time monitoring capabilities for Alfresco content changes, enabling responsive AI workflows and automated content processing.

## Custom MCP Server Integration

The event system can be integrated into custom MCP servers that handle events internally. Since MCP servers cannot relay events externally, the event handling must be managed within the server itself:

```python
from fastmcp import FastMCP
from python_alfresco_api.event_client import AlfrescoEventClient
import asyncio
import threading

# Custom MCP server with internal event handling
mcp = FastMCP("Alfresco Content Monitor")

class ContentMonitor:
    def __init__(self):
        self.event_client = None
        self.is_monitoring = False
        self.recent_events = []
        self.max_events = 100
    
    async def start_monitoring(self):
        """Start internal event monitoring"""
        if self.is_monitoring:
            return "Already monitoring"
        
        self.event_client = AlfrescoEventClient(auto_detect=True)
        await asyncio.sleep(2)  # Wait for detection
        
        # Setup internal event handlers
        def internal_handler(notification):
            # Store events internally for MCP tools to access
            self.recent_events.append({
                'timestamp': notification.timestamp.isoformat(),
                'event_type': notification.event_type,
                'node_id': notification.node_id,
                'node_type': notification.node_type,
                'user_id': notification.user_id
            })
            
            # Keep only recent events
            if len(self.recent_events) > self.max_events:
                self.recent_events.pop(0)
        
        # Register handlers for key events
        self.event_client.register_event_handler("node.created", internal_handler)
        self.event_client.register_event_handler("node.updated", internal_handler)
        self.event_client.register_event_handler("node.deleted", internal_handler)
        
        # Start monitoring in background
        self.is_monitoring = True
        await self.event_client.start_listening()
        return "Content monitoring started"

# Global monitor instance
monitor = ContentMonitor()

@mcp.tool()
def start_content_monitoring() -> str:
    """Start monitoring Alfresco content changes internally"""
    # Run async monitoring in background thread
    def run_monitor():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(monitor.start_monitoring())
    
    if not monitor.is_monitoring:
        thread = threading.Thread(target=run_monitor, daemon=True)
        thread.start()
        return "Content monitoring started (background thread)"
    
    return "Already monitoring content changes"

@mcp.tool()
def get_recent_events(limit: int = 10) -> str:
    """Get recent content events (stored internally)"""
    if not monitor.is_monitoring:
        return "Monitoring not active. Start monitoring first."
    
    recent = monitor.recent_events[-limit:]
    if not recent:
        return "No recent events captured"
    
    result = f"Recent {len(recent)} events:\n"
    for event in recent:
        result += f"- {event['timestamp']}: {event['event_type']} on {event['node_id']}\n"
    
    return result

@mcp.tool()
def get_monitoring_status() -> str:
    """Get current monitoring status"""
    if not monitor.is_monitoring:
        return "Not monitoring"
    
    event_count = len(monitor.recent_events)
    return f"Monitoring active, {event_count} events captured"

if __name__ == "__main__":
    mcp.run()
```

## Troubleshooting

### Common Issues

1. **No event system detected**
   - Check if Alfresco is running
   - Verify ports are accessible (7070 for Enterprise, 61613 for Community)
   - Check authentication credentials

2. **ActiveMQ not available**
   - Install: `pip install stomp.py`
   - Verify ActiveMQ is enabled in Alfresco
   - Check port 61613 is accessible

3. **Event Gateway not available**
   - Verify Enterprise Edition is running
   - Check Event Gateway service status
   - Verify port 7070 is accessible

### Debug Mode

```python
import logging
logging.basicConfig(level=logging.DEBUG)

event_client = AlfrescoEventClient(debug=True)
```

## Next Steps

The event system enables building custom MCP servers with internal event handling capabilities. This provides the foundation for:

- Real-time content change monitoring within MCP servers
- AI-powered content analysis triggered by events
- Automated workflow responses to content changes
- Custom notification and alerting systems

For a complete MCP server implementation that could be extended with event handling, see the [python-alfresco-mcp-server](https://github.com/stevereiner/python-alfresco-mcp-server) project. This provides a comprehensive MCP server with FastMCP 2.0 integration and complete Alfresco functionality - its code can serve as the foundation for adding custom event handling capabilities.

---

*The event system provides a foundation for building intelligent, event-driven content management applications.* 