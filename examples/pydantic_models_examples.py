#!/usr/bin/env python3
"""
Standalone Pydantic Models Examples - For AI/LLM Integration

⚠️  IMPORTANT: These Pydantic models are STANDALONE and NOT integrated with HTTP clients.
    
    - Pydantic Models: For AI/LLM integration, validation, MCP servers
    - HTTP Clients: Accept dictionaries, return attrs objects
    
This example shows how to use Pydantic models for:
- Data validation
- AI/LLM tool interfaces  
- MCP server development
- Type-safe data structures

For HTTP client usage, see basic_usage.py or master_client_examples.py
"""

import sys
import os
from datetime import datetime
from typing import Dict, Any, List, Optional

# Import Pydantic for creating example models
from pydantic import BaseModel, ValidationError, Field

# Import actual API models (generated from OpenAPI specs)
from python_alfresco_api.models.alfresco_core_models import (
    NodeBodyCreate as ApiNodeBodyCreate,
    NodeBodyUpdate as ApiNodeBodyUpdate
)

# =============================================================================
# Example Custom Pydantic Models - For AI/LLM Integration
# =============================================================================

class Node(BaseModel):
    """
    Custom Node model for AI/LLM integration.
    Perfect for MCP servers and AI tool interfaces.
    """
    id: str
    name: str = Field(..., description="Node name with validation")
    nodeType: str
    isFile: bool
    isFolder: bool
    createdAt: datetime
    modifiedAt: datetime
    parentId: Optional[str] = None
    properties: Optional[Dict[str, Any]] = None
    aspectNames: Optional[List[str]] = None
    allowableOperations: Optional[List[str]] = None

class NodeEntry(BaseModel):
    """Wrapper for Node responses from API"""
    entry: Node

class NodePaging(BaseModel):
    """Paginated list of nodes (for children, search results, etc.)"""
    entries: Optional[List[NodeEntry]] = None
    pagination: Optional[Dict[str, Any]] = None

class NodeListResponse(BaseModel):
    """Complete response structure for node listings"""
    list: NodePaging

class NodeBodyCreate(BaseModel):
    """Model for creating new nodes (files/folders)"""
    name: str = Field(..., description="Name of the new node")
    nodeType: str = Field(default="cm:folder", description="Type of node to create")
    properties: Optional[Dict[str, Any]] = None
    aspectNames: Optional[List[str]] = None
    relativePath: Optional[str] = None

class NodeBodyUpdate(BaseModel):
    """Model for updating existing nodes"""
    name: Optional[str] = None
    nodeType: Optional[str] = None
    properties: Optional[Dict[str, str]] = None
    aspectNames: Optional[List[str]] = None

# Authentication models for Core API access
class TicketBody(BaseModel):
    userId: str
    password: str

def main():
    """Standalone Pydantic models examples for AI/LLM integration."""
    print("🤖 Standalone Pydantic Models - AI/LLM Integration Examples")
    print("⚠️  NOTE: These models are NOT integrated with HTTP clients")
    print("Use for: validation, AI tools, MCP servers, type-safe data structures")
    print("="*80)
    
    # =============================================================================
    # Example 1: Custom Pydantic Models for AI Tools
    # =============================================================================
    print("\n" + "="*70)
    print("🤖 1. Custom Pydantic Models - Perfect for AI/LLM Tools")
    print("="*70)
    
    # Create a sample Node using custom Pydantic model
    try:
        sample_node = Node(
            id="workspace://SpacesStore/12345",
            name="AI Generated Document.pdf",
            nodeType="cm:content",
            isFile=True,
            isFolder=False,
            createdAt=datetime.now(),
            modifiedAt=datetime.now(),
            parentId="workspace://SpacesStore/company-home",
            properties={
                "cm:title": "AI Generated Document",
                "cm:description": "Document created by AI assistant",
                "cm:author": "AI Assistant"
            },
            aspectNames=["cm:titled", "cm:author"],
            allowableOperations=["read", "update", "delete"]
        )
        
        print("✅ Created custom Node model for AI tools:")
        print(f"   📄 Name: {sample_node.name}")
        print(f"   🏷️  Type: {sample_node.nodeType}")
        print(f"   📅 Created: {sample_node.createdAt.strftime('%Y-%m-%d %H:%M')}")
        author = sample_node.properties.get('cm:author') if sample_node.properties else None
        print(f"   🤖 Author: {author}")
        
        # JSON serialization for AI tools
        json_data = sample_node.model_dump_json()
        print(f"\n   📄 JSON for AI tools: {len(json_data)} characters")
        print(f"   💾 Perfect for: MCP servers, LLM tool interfaces, validation")
        
    except Exception as e:
        print(f"❌ Failed to create Node: {e}")
    
    # =============================================================================
    # Example 2: Using Generated API Models (Standalone)
    # =============================================================================
    print("\n" + "="*70)
    print("🏗️ 2. Generated API Models - From OpenAPI Specs")
    print("="*70)
    
    try:
        # Use actual generated model from OpenAPI specs
        api_node_create = ApiNodeBodyCreate(
            name="api-generated-folder",
            nodeType="cm:folder",
            properties={
                "cm:title": "Generated from OpenAPI",
                "cm:description": "Created using official Alfresco API models"
            }
        )
        
        print("✅ Using generated API models:")
        print(f"   📁 Name: {api_node_create.name}")
        print(f"   🏷️  Type: {api_node_create.nodeType}")
        print(f"   📝 Properties: {api_node_create.properties}")
        
        # Convert to dictionary for client usage
        api_dict = api_node_create.model_dump()
        print(f"\n   🔄 Converting to dictionary for HTTP client:")
        print(f"   📦 Dictionary keys: {list(api_dict.keys())}")
        
        print(f"\n   💡 Usage with HTTP clients:")
        print("   # 1. Create Pydantic model for validation")
        print("   node_model = ApiNodeBodyCreate(...)")
        print("   # 2. Convert to dictionary")  
        print("   node_dict = node_model.model_dump()")
        print("   # 3. Pass dictionary to client")
        print("   client.core.create_node(node_dict)")
        
    except Exception as e:
        print(f"❌ Failed to create API model: {e}")
    
    # =============================================================================
    # Example 3: Data Validation for AI Systems
    # =============================================================================
    print("\n" + "="*70)
    print("🔍 3. Data Validation - Critical for AI/LLM Systems")
    print("="*70)
    
    # Example: Validating data from AI/LLM
    ai_generated_data = {
        "name": "AI Document.txt",
        "nodeType": "cm:content",
        "properties": {
            "cm:title": "Document from AI",
            "cm:author": "ChatGPT",
            "priority": "high"
        }
    }
    
    try:
        # Validate with Pydantic
        validated_node = NodeBodyCreate(**ai_generated_data)
        print("✅ AI data validation successful:")
        print(f"   📄 Validated name: {validated_node.name}")
        print(f"   🏷️  Validated type: {validated_node.nodeType}")
        print(f"   ✅ All fields valid for API submission")
        
        # Show validation benefits
        print(f"\n   🛡️ Validation benefits:")
        print("   • Type safety for AI-generated data")
        print("   • Field validation (names, types, etc.)")
        print("   • Automatic data cleaning")
        print("   • Error detection before API calls")
        
    except ValidationError as e:
        print(f"❌ Validation failed: {e}")
    
    # =============================================================================
    # Example 4: MCP Server Integration Pattern
    # =============================================================================
    print("\n" + "="*70)
    print("🔌 4. MCP Server Integration - Model Context Protocol")
    print("="*70)
    
    def simulate_mcp_tool(node_data: dict) -> dict:
        """Simulate an MCP tool that processes Alfresco nodes."""
        try:
            # Validate incoming data with Pydantic
            validated_node = Node(**node_data)
            
            # Process with type safety
            result = {
                "tool": "alfresco_node_processor",
                "status": "success",
                "processed_node": {
                    "id": validated_node.id,
                    "name": validated_node.name,
                    "type": validated_node.nodeType,
                    "properties_count": len(validated_node.properties or {}),
                    "is_content": validated_node.isFile
                }
            }
            
            return result
            
        except ValidationError as e:
            return {"tool": "alfresco_node_processor", "status": "error", "error": str(e)}
    
    # Test MCP tool simulation
    mcp_test_data = {
        "id": "workspace://SpacesStore/mcp-test",
        "name": "MCP Test Document.pdf",
        "nodeType": "cm:content", 
        "isFile": True,
        "isFolder": False,
        "createdAt": datetime.now().isoformat(),
        "modifiedAt": datetime.now().isoformat(),
        "properties": {"cm:title": "MCP Integration Test"}
    }
    
    mcp_result = simulate_mcp_tool(mcp_test_data)
    print("✅ MCP tool simulation:")
    print(f"   🔧 Tool: {mcp_result['tool']}")
    print(f"   📊 Status: {mcp_result['status']}")
    if mcp_result['status'] == 'success':
        processed = mcp_result['processed_node']
        print(f"   📄 Processed: {processed['name']}")
        print(f"   🏷️  Type: {processed['type']}")
        print(f"   📊 Properties: {processed['properties_count']}")
    
    # =============================================================================
    # Example 5: Type-Safe Data Structures for AI
    # =============================================================================
    print("\n" + "="*70)
    print("🎯 5. Type-Safe Data Structures - AI/LLM Integration")
    print("="*70)
    
    # Create hierarchical data structure
    try:
        # Parent folder
        parent_folder = NodeBodyCreate(
            name="AI Project Workspace",
            nodeType="cm:folder",
            properties={
                "cm:title": "AI Project Workspace",
                "cm:description": "Workspace for AI-generated content",
                "project:type": "ai_workspace"
            }
        )
        
        # Child documents
        child_docs = [
            NodeBodyCreate(
                name="analysis.md",
                nodeType="cm:content",
                properties={"cm:title": "Data Analysis", "ai:generated": "true"}
            ),
            NodeBodyCreate(
                name="report.pdf", 
                nodeType="cm:content",
                properties={"cm:title": "Final Report", "ai:reviewed": "true"}
            )
        ]
        
        print("✅ Type-safe hierarchical structure:")
        print(f"   📁 Parent: {parent_folder.name}")
        print(f"   📄 Children: {len(child_docs)} documents")
        
        # Serialize all for AI processing
        workspace_data = {
            "parent": parent_folder.model_dump(),
            "children": [doc.model_dump() for doc in child_docs]
        }
        
        print(f"   💾 Serialized: {len(str(workspace_data))} characters")
        print(f"   🤖 Ready for: AI processing, MCP tools, validation")
        
    except Exception as e:
        print(f"❌ Failed to create structure: {e}")
    
    # =============================================================================
    # Summary and Best Practices
    # =============================================================================
    print("\n" + "="*70)
    print("📋 SUMMARY - Standalone Pydantic Models")
    print("="*70)
    
    print("✅ PERFECT FOR:")
    print("   • 🤖 AI/LLM tool interfaces")
    print("   • 🔌 MCP server development") 
    print("   • 🛡️ Data validation")
    print("   • 📝 Type-safe data structures")
    print("   • 🔄 API data preparation")
    
    print("\n⚠️  NOT INTEGRATED WITH:")
    print("   • ❌ HTTP clients (use dictionaries instead)")
    print("   • ❌ Direct API calls")
    print("   • ❌ Client methods")
    
    print("\n💡 USAGE PATTERN:")
    print("   1. Create/validate with Pydantic models")
    print("   2. Convert to dictionaries: model.model_dump()")
    print("   3. Pass dictionaries to HTTP clients")
    print("   4. Clients return attrs objects")
    
    print("\n🎯 AI/LLM INTEGRATION VALUE:")
    print("   • Type-safe tool interfaces")
    print("   • Automatic validation")
    print("   • Perfect for MCP servers")
    print("   • Clean data structures")

if __name__ == "__main__":
    main() 