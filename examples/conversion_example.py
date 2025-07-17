#!/usr/bin/env python3
"""
Conversion Utilities Example for Python-Alfresco-API V1.1

Demonstrates how to use Pydantic models with automatic conversion
to seamlessly integrate with Alfresco clients.

This bridges the gap between type-safe Pydantic models and 
the attrs-based raw clients for the best developer experience.
"""

from python_alfresco_api import (
    ClientFactory,
    pydantic_to_attrs_dict
)

# Import Pydantic models for type safety
from python_alfresco_api.models.alfresco_core_models import NodeBodyCreate

def demonstrate_node_creation():
    """Example: Creating nodes with Pydantic validation + client integration"""
    print("🎯 Node Creation with Pydantic Validation")
    print("=" * 50)
    
    # 1. Create type-safe Pydantic model
    node_request = NodeBodyCreate(
        name="my-document.pdf",
        nodeType="cm:content",
        properties={
            "cm:title": "Important Document",
            "cm:description": "This document contains important information",
            "cm:author": "API User"
        }
    )
    
    print(f"✅ Created Pydantic model: {node_request.name}")
    print(f"   Type: {node_request.nodeType}")
    print(f"   Properties: {len(node_request.properties or {})} custom properties")
    
    # 2. Convert to attrs format for client
    attrs_dict = pydantic_to_attrs_dict(node_request)
    print(f"✅ Converted to attrs format: {attrs_dict['name']}")
    
    # 3. Use with client (demo - would work with live Alfresco)
    factory = ClientFactory(
        base_url="http://localhost:8080",
        username="admin",
        password="admin"
    )
    core_client = factory.create_core_client()
    
    print(f"✅ Ready for client.create_node(attrs_dict)")
    print(f"   Client ready for: http://localhost:8080")
    
    return attrs_dict

def demonstrate_search_request():
    """Example: Simple search dictionary for client use"""
    print("\n🔍 Search Request with Dictionary Pattern")
    print("=" * 50)
    
    # 1. Create search dictionary (direct approach)
    search_dict = {
        "query": {
            "query": "TEXT:finance AND TYPE:cm:content",
            "language": "afts"
        },
        "paging": {
            "maxItems": 25,
            "skipCount": 0
        }
    }
    
    print(f"✅ Created search dictionary:")
    print(f"   Query: {search_dict['query']['query']}")
    print(f"   Language: {search_dict['query']['language']}")
    print(f"   Max Items: {search_dict['paging']['maxItems']}")
    
    # 2. Ready for search client
    factory = ClientFactory(
        base_url="http://localhost:8080",
        username="admin", 
        password="admin"
    )
    search_client = factory.create_search_client()
    
    print(f"✅ Ready for search_client.search(search_dict)")
    print(f"   Note: Complex SearchRequest Pydantic models coming in future updates")
    
    return search_dict

def demonstrate_basic_conversion():
    """Example: Basic conversion utilities demonstration"""
    print("\n🔄 Basic Conversion Utilities")
    print("=" * 50)
    
    # 1. Create a node model
    original_node = NodeBodyCreate(
        name="test-document.txt",
        nodeType="cm:content",
        properties={"cm:title": "Test Document"}
    )
    
    print(f"✅ Original Pydantic model: {original_node.name}")
    
    # 2. Convert to attrs format
    attrs_dict = pydantic_to_attrs_dict(original_node)
    print(f"✅ Converted to attrs dict: {attrs_dict['name']}")
    print(f"   Keys: {list(attrs_dict.keys())}")
    
    # 3. Show the conversion maintains data integrity
    print(f"✅ Data integrity maintained:")
    print(f"   Original name: {original_node.name}")
    print(f"   Converted name: {attrs_dict['name']}")
    print(f"   Properties preserved: {bool(attrs_dict.get('properties'))}")
    
    return attrs_dict

def demonstrate_full_workflow():
    """Example: Complete workflow with validation, conversion, and client usage"""
    print("\n🚀 Complete Workflow Example")
    print("=" * 50)
    
    # 1. Validate input data with Pydantic
    try:
        node_data = NodeBodyCreate(
            name="validated-document.pdf",
            nodeType="cm:content",
            properties={
                "cm:title": "Validated Document",
                "cm:description": "This document passed Pydantic validation"
            }
        )
        print("✅ Input validation passed")
    except Exception as e:
        print(f"❌ Validation failed: {e}")
        return
    
    # 2. Convert for client compatibility
    client_data = pydantic_to_attrs_dict(node_data)
    print("✅ Converted for client compatibility")
    
    # 3. Simulate client response (would come from actual API)
    simulated_response = {
        "id": "abc123-def456-ghi789",
        "name": client_data["name"],
        "nodeType": client_data["nodeType"],
        "createdAt": "2024-01-15T10:30:00.000Z",
        "modifiedAt": "2024-01-15T10:30:00.000Z"
    }
    print(f"✅ Simulated API response received for: {simulated_response['name']}")
    
    # 4. Future: Convert response back to Pydantic for type-safe handling
    print("✅ Response ready for Pydantic model conversion (future enhancement)")
    
    return {
        "request": node_data,
        "client_data": client_data,
        "response": simulated_response
    }

if __name__ == "__main__":
    print("🎯 Python-Alfresco-API V1.1 Conversion Utilities Demo")
    print("=" * 60)
    print("Demonstrating Request/Response mapping with Pydantic models")
    print()
    
    # Run all examples
    node_attrs = demonstrate_node_creation()
    search_dict = demonstrate_search_request()
    basic_conversion = demonstrate_basic_conversion()
    workflow_result = demonstrate_full_workflow()
    
    print("\n🎉 All Examples Completed Successfully!")
    print("=" * 60)
    print("Key Benefits Demonstrated:")
    print("✅ Type-safe Pydantic model validation") 
    print("✅ Automatic conversion to client-compatible formats")
    print("✅ Basic conversion utilities working")
    print("✅ Ready for V1.1 hierarchical client integration")
    print("✅ Perfect for MCP servers and AI/LLM applications")
    
    # Show import pattern for developers
    print("\n📦 Import Pattern for V1.1:")
    print("from python_alfresco_api import (")
    print("    ClientFactory,")
    print("    pydantic_to_attrs_dict")
    print(")")
    print("\n📋 Next Steps:")
    print("• Advanced converter pairs with attrs class integration")
    print("• High-level SearchRequest Pydantic models")  
    print("• Direct Pydantic model support in V1.1 clients")
    print("• Comprehensive Request/Response model coverage") 