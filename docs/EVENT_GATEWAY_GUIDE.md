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

## Phase 2 Integration

This event system is **Phase 2** of the [8-phase Alfresco-AI roadmap][[memory:5182191768171681496]]:

- ✅ **Phase 1**: Core API clients (Complete)  
- ✅ **Phase 2**: Event Gateway integration (Complete)
- 🚧 **Phase 3**: MCP server implementation (Next)

## MCP Server Integration

The event system is designed for Model Context Protocol (MCP) integration:

```python
# Future MCP server usage
from python_alfresco_api.event_client import AlfrescoEventClient
from mcp import Server

@server.tool("monitor_content")
async def monitor_alfresco_content():
    """Monitor Alfresco content changes via events"""
    event_client = AlfrescoEventClient(auto_detect=True)
    await event_client.setup_content_monitoring()
    return "Content monitoring started"
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

With Phase 2 complete, the next phase is **MCP Server implementation** using the [official MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) to create:

- **python-alfresco-mcp-server** - A separate project
- Natural language interfaces for Alfresco operations
- AI-powered content management workflows
- GraphRAG capabilities for document understanding

---

*This completes Phase 2 of the Alfresco-AI integration roadmap. The event system provides the foundation for real-time AI-powered content management workflows.* 