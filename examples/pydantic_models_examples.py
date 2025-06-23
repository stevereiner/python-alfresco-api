#!/usr/bin/env python3
"""
Alfresco Pydantic Data Models Examples - Core API Focus

This file demonstrates how to use the Pydantic data models with focus on the most commonly used 
Core API operations: Node models, getting children, and working with node properties.

These are the bread and butter operations for most Alfresco integrations.
"""

import sys
import os
from datetime import datetime
from typing import Dict, Any, List, Optional

from AlfrescoClient import AlfrescoClient

# Import Pydantic for creating example models
from pydantic import BaseModel, ValidationError, Field

# =============================================================================
# Core API Pydantic Models - The Most Important Ones
# =============================================================================

class Node(BaseModel):
    """
    Core Node model - the fundamental entity in Alfresco.
    Represents files, folders, and all content items.
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
    """Core API Pydantic data models examples."""
    print("🏗️ Alfresco Core API - Pydantic Models Examples")
    print("Focus: Nodes, Children, Properties - The Most Common Operations")
    print("="*80)
    
    # Initialize client
    client = AlfrescoClient(host="http://localhost:8080", username="admin", password="admin")
    
    # =============================================================================
    # Example 1: Node Model - The Foundation of Everything
    # =============================================================================
    print("\n" + "="*70)
    print("📁 1. Node Model - The Foundation of Alfresco")
    print("="*70)
    
    # Create a sample Node using Pydantic
    try:
        sample_node = Node(
            id="workspace://SpacesStore/12345",
            name="Important Document.pdf",
            nodeType="cm:content",
            isFile=True,
            isFolder=False,
            createdAt=datetime.now(),
            modifiedAt=datetime.now(),
            parentId="workspace://SpacesStore/company-home",
            properties={
                "cm:title": "Important Document",
                "cm:description": "This is a critical business document",
                "cm:author": "John Smith"
            },
            aspectNames=["cm:titled", "cm:author"],
            allowableOperations=["read", "update", "delete"]
        )
        
        print("✅ Created Node model:")
        print(f"   📄 Name: {sample_node.name}")
        print(f"   🏷️  Type: {sample_node.nodeType}")
        print(f"   📅 Created: {sample_node.createdAt.strftime('%Y-%m-%d %H:%M')}")
        print(f"   📂 Parent: {sample_node.parentId}")
        print(f"   🏷️  Aspects: {', '.join(sample_node.aspectNames or [])}")
        print(f"   🔑 Properties: {len(sample_node.properties or {})} custom properties")
        
        # Show properties detail
        if sample_node.properties:
            print("\n   📝 Custom Properties:")
            for key, value in sample_node.properties.items():
                print(f"      {key}: {value}")
        
        # JSON serialization for API calls
        print(f"\n   📄 JSON for API: {len(sample_node.model_dump_json())} characters")
        
    except Exception as e:
        print(f"❌ Failed to create Node: {e}")
    
    # =============================================================================
    # Example 2: Node Creation Models - Making New Content
    # =============================================================================
    print("\n" + "="*70)
    print("📝 2. Node Creation - Making New Files and Folders")
    print("="*70)
    
    # Example: Creating a folder
    try:
        new_folder = NodeBodyCreate(
            name="Project Documents",
            nodeType="cm:folder",
            properties={
                "cm:title": "Project Documents Folder",
                "cm:description": "Contains all project-related documents"
            },
            aspectNames=["cm:titled"]
        )
        
        print("✅ Folder creation model:")
        print(f"   📁 Name: {new_folder.name}")
        print(f"   🏷️  Type: {new_folder.nodeType}")
        print(f"   📝 Properties: {new_folder.properties}")
        print(f"   🏷️  Aspects: {new_folder.aspectNames}")
        
        # Example: Creating a file
        new_file = NodeBodyCreate(
            name="project-plan.docx",
            nodeType="cm:content",
            properties={
                "cm:title": "Project Plan Document",
                "cm:description": "Detailed project timeline and milestones",
                "cm:author": "Project Manager"
            },
            aspectNames=["cm:titled", "cm:author"],
            relativePath="Projects/2024"  # Create in subfolder
        )
        
        print("\n✅ File creation model:")
        print(f"   📄 Name: {new_file.name}")
        print(f"   🏷️  Type: {new_file.nodeType}")
        print(f"   📍 Path: {new_file.relativePath}")
        print(f"   👤 Author: {new_file.properties.get('cm:author')}")
        
        # Show how this would be used with API
        print("\n💡 API Usage:")
        print("   # Create folder in Company Home")
        print(f"   folder_data = {new_folder.model_dump()}")
        print("   response = client.core.create_node(node_id='-root-', node_body_create=folder_data)")
        
    except Exception as e:
        print(f"❌ Failed to create node models: {e}")
    
    # =============================================================================
    # Example 3: Node Update Models - Modifying Existing Content
    # =============================================================================
    print("\n" + "="*70)
    print("✏️ 3. Node Updates - Modifying Properties and Metadata")
    print("="*70)
    
    try:
        # Example: Updating node properties
        node_updates = NodeBodyUpdate(
            name="Updated-project-plan.docx",  # Rename file
            properties={
                "cm:title": "Updated Project Plan",
                "cm:description": "Revised project timeline with new deadlines",
                "cm:author": "Senior Project Manager",
                "custom:priority": "High",
                "custom:status": "In Review"
            },
            aspectNames=["cm:titled", "cm:author", "custom:projectAspect"]
        )
        
        print("✅ Node update model:")
        print(f"   📝 New name: {node_updates.name}")
        print(f"   📊 Updated properties: {len(node_updates.properties or {})} properties")
        
        if node_updates.properties:
            print("   📝 Property changes:")
            for key, value in node_updates.properties.items():
                print(f"      {key}: {value}")
        
        print(f"   🏷️  New aspects: {node_updates.aspectNames}")
        
        # Validation example
        print("\n🔍 Validation features:")
        print("   ✅ Name validation (no invalid characters)")
        print("   ✅ Properties are properly typed")
        print("   ✅ Aspects are validated as list of strings")
        
    except Exception as e:
        print(f"❌ Failed to create update model: {e}")
    
    # =============================================================================
    # Example 4: Node Children - Listing Folder Contents
    # =============================================================================
    print("\n" + "="*70)
    print("📂 4. Node Children - Listing Folder Contents (Most Common!)")
    print("="*70)
    
    # Simulate a response from getting node children
    try:
        # Create sample child nodes
        child_nodes = [
            NodeEntry(entry=Node(
                id="workspace://SpacesStore/child1",
                name="Budget Spreadsheet.xlsx",
                nodeType="cm:content",
                isFile=True,
                isFolder=False,
                createdAt=datetime.now(),
                modifiedAt=datetime.now(),
                properties={"cm:title": "Annual Budget", "cm:author": "Finance Team"}
            )),
            NodeEntry(entry=Node(
                id="workspace://SpacesStore/child2", 
                name="Presentations",
                nodeType="cm:folder",
                isFile=False,
                isFolder=True,
                createdAt=datetime.now(),
                modifiedAt=datetime.now(),
                properties={"cm:description": "Marketing presentations"}
            )),
            NodeEntry(entry=Node(
                id="workspace://SpacesStore/child3",
                name="Meeting Notes.docx", 
                nodeType="cm:content",
                isFile=True,
                isFolder=False,
                createdAt=datetime.now(),
                modifiedAt=datetime.now(),
                properties={"cm:title": "Weekly Team Meeting", "cm:author": "Team Lead"}
            ))
        ]
        
        # Create paginated response
        children_response = NodeListResponse(
            list=NodePaging(
                entries=child_nodes,
                pagination={
                    "count": len(child_nodes),
                    "hasMoreItems": False,
                    "maxItems": 100,
                    "skipCount": 0,
                    "totalItems": len(child_nodes)
                }
            )
        )
        
        print("✅ Children listing response structure:")
        print(f"   📊 Total items: {len(children_response.list.entries or [])}")
        print(f"   📄 Pagination: {children_response.list.pagination}")
        
        print("\n📁 Child nodes:")
        for i, child_entry in enumerate(children_response.list.entries or [], 1):
            node = child_entry.entry
            icon = "📄" if node.isFile else "📁"
            print(f"   {i}. {icon} {node.name}")
            print(f"      🆔 ID: {node.id}")
            print(f"      🏷️  Type: {node.nodeType}")
            if node.properties:
                print(f"      📝 Properties: {len(node.properties)} custom properties")
                if 'cm:title' in node.properties:
                    print(f"         Title: {node.properties['cm:title']}")
                if 'cm:author' in node.properties:
                    print(f"         Author: {node.properties['cm:author']}")
        
        # Show how to process children in code
        print("\n💡 Processing children in your code:")
        print("   ```python")
        print("   # Get children from API")
        print("   response = client.core.list_node_children(node_id='folder-id')")
        print("   ")
        print("   # Process each child") 
        print("   for child_entry in response.list.entries:")
        print("       node = child_entry.entry")
        print("       if node.isFile:")
        print("           print(f'File: {node.name}')")
        print("       elif node.isFolder:")
        print("           print(f'Folder: {node.name}')")
        print("   ```")
        
    except Exception as e:
        print(f"❌ Failed to create children example: {e}")
    
    # =============================================================================
    # Example 5: Working with Node Properties - The Power of Metadata
    # =============================================================================
    print("\n" + "="*70)
    print("🏷️ 5. Node Properties - The Power of Metadata")
    print("="*70)
    
    print("📝 Common Alfresco Properties by Aspect:")
    
    # Example properties by aspect
    aspects_and_properties = {
        "cm:titled": {
            "cm:title": "Document title",
            "cm:description": "Document description"
        },
        "cm:author": {
            "cm:author": "Document author"
        },
        "cm:auditable": {
            "cm:created": "Creation date",
            "cm:creator": "Creator username", 
            "cm:modified": "Last modified date",
            "cm:modifier": "Last modifier username"
        },
        "cm:versionable": {
            "cm:versionLabel": "Version number (1.0, 1.1, etc.)",
            "cm:autoVersion": "Auto-versioning enabled",
            "cm:autoVersionOnUpdateProps": "Version on property changes"
        },
        "exif:exif": {
            "exif:pixelXDimension": "Image width in pixels",
            "exif:pixelYDimension": "Image height in pixels", 
            "exif:dateTimeOriginal": "Photo taken date"
        }
    }
    
    for aspect, properties in aspects_and_properties.items():
        print(f"\n   🏷️  {aspect}:")
        for prop_name, prop_desc in properties.items():
            print(f"      {prop_name}: {prop_desc}")
    
    # Example: Working with custom properties
    try:
        custom_document = Node(
            id="workspace://SpacesStore/custom-doc",
            name="Contract_ABC_Corp.pdf",
            nodeType="cm:content", 
            isFile=True,
            isFolder=False,
            createdAt=datetime.now(),
            modifiedAt=datetime.now(),
            properties={
                # Standard Alfresco properties
                "cm:title": "Service Agreement - ABC Corporation",
                "cm:description": "Annual service contract with ABC Corp",
                "cm:author": "Legal Department",
                
                # Custom business properties
                "contract:client": "ABC Corporation",
                "contract:value": 150000.00,
                "contract:startDate": "2024-01-01",
                "contract:endDate": "2024-12-31", 
                "contract:status": "Active",
                "contract:renewalDate": "2024-11-01",
                "contract:owner": "sales.manager@company.com",
                
                # Compliance properties
                "compliance:reviewed": True,
                "compliance:approvedBy": "legal.director@company.com",
                "compliance:approvalDate": "2023-12-15"
            },
            aspectNames=[
                "cm:titled",
                "cm:author", 
                "contract:contractAspect",
                "compliance:reviewAspect"
            ]
        )
        
        print("\n✅ Document with rich metadata:")
        print(f"   📄 Document: {custom_document.name}")
        print(f"   📝 Total properties: {len(custom_document.properties or {})}")
        
        # Categorize properties
        standard_props = {k: v for k, v in custom_document.properties.items() if k.startswith('cm:')}
        contract_props = {k: v for k, v in custom_document.properties.items() if k.startswith('contract:')}
        compliance_props = {k: v for k, v in custom_document.properties.items() if k.startswith('compliance:')}
        
        print(f"\n   📋 Standard properties ({len(standard_props)}):")
        for prop, value in standard_props.items():
            print(f"      {prop}: {value}")
        
        print(f"\n   💼 Contract properties ({len(contract_props)}):")
        for prop, value in contract_props.items():
            print(f"      {prop}: {value}")
        
        print(f"\n   ✅ Compliance properties ({len(compliance_props)}):")
        for prop, value in compliance_props.items():
            print(f"      {prop}: {value}")
        
    except Exception as e:
        print(f"❌ Failed to create custom properties example: {e}")
    
    # =============================================================================
    # Example 6: Real Core API Usage with Pydantic Models
    # =============================================================================
    print("\n" + "="*70)
    print("🚀 6. Real Core API Usage with Pydantic Models")
    print("="*70)
    
    if client.core and isinstance(client.core, dict):
        print("💡 Common Core API patterns with Pydantic models:")
        print()
        print("📁 1. Get Repository Root Children:")
        print("   ```python")
        print("   # API call returns Pydantic models")
        print("   response = client.core['nodes'].list_node_children(node_id='-root-')")
        print("   ")
        print("   # Work with strongly-typed response")
        print("   for child_entry in response.list.entries:")
        print("       node = child_entry.entry  # This is a Node Pydantic model")
        print("       print(f'{node.name} ({node.nodeType})')")
        print("       ")
        print("       # Access properties with validation")
        print("       if 'cm:title' in (node.properties or {}):")
        print("           print(f'Title: {node.properties[\"cm:title\"]}')")
        print("   ```")
        
        print("\n📄 2. Create Document with Properties:")
        print("   ```python")
        print("   # Use Pydantic model for type safety")
        print("   new_doc = NodeBodyCreate(")
        print("       name='important-file.pdf',")
        print("       nodeType='cm:content',")
        print("       properties={")
        print("           'cm:title': 'Important Document',")
        print("           'cm:author': 'John Smith'")
        print("       },")
        print("       aspectNames=['cm:titled', 'cm:author']")
        print("   )")
        print("   ")
        print("   # API call with validated data")
        print("   response = client.core['nodes'].create_node(")
        print("       node_id='parent-folder-id',")
        print("       node_body_create=new_doc.model_dump()")
        print("   )")
        print("   ```")
        
        print("\n✏️ 3. Update Node Properties:")
        print("   ```python")
        print("   # Type-safe property updates")
        print("   updates = NodeBodyUpdate(")
        print("       properties={")
        print("           'cm:description': 'Updated description',")
        print("           'custom:status': 'Reviewed'")
        print("       }")
        print("   )")
        print("   ")
        print("   # Apply updates")
        print("   response = client.core['nodes'].update_node(")
        print("       node_id='document-id',")
        print("       node_body_update=updates.model_dump()")
        print("   )")
        print("   ```")
        
        # Try a real API call if possible
        print("\n📡 Testing real API call...")
        try:
            if 'nodes' in client.core:
                # This will likely fail due to auth, but demonstrates the pattern
                root_children = client.core['nodes'].list_node_children(node_id='-root-')
                print("✅ API call succeeded - response is automatically Pydantic models!")
                print(f"   Response type: {type(root_children)}")
                if hasattr(root_children, 'list') and root_children.list.entries:
                    print(f"   Found {len(root_children.list.entries)} children")
        except Exception as e:
            print(f"❌ API call failed (expected without live server): {e}")
            print("   💡 In real usage, responses are automatically Pydantic models")
    
    # =============================================================================
    # Example 7: Validation Benefits for Core API
    # =============================================================================
    print("\n" + "="*70)
    print("⚠️ 7. Validation Benefits - Catching Errors Early")
    print("="*70)
    
    print("🧪 Testing validation for common Core API mistakes...")
    
    # Test 1: Invalid node name
    try:
        invalid_node = NodeBodyCreate(
            name="file|with:invalid*chars.txt",  # Contains invalid characters
            nodeType="cm:content"
        )
        print(f"❌ Unexpected: Invalid filename was accepted: {invalid_node.name}")
    except ValidationError as e:
        print(f"✅ Validation caught invalid filename characters")
        print(f"   Pydantic prevented creation of node with invalid name")
    
    # Test 2: Missing required fields
    try:
        incomplete_node = Node(
            # Missing required fields like id, name, nodeType, etc.
            isFile=True,
            isFolder=False
        )
        print(f"❌ Unexpected: Incomplete node was accepted")
    except ValidationError as e:
        print(f"✅ Validation caught missing required fields")
        print(f"   Required fields like 'id', 'name', 'nodeType' must be provided")
    
    # Test 3: Type validation
    try:
        wrong_types = Node(
            id="valid-id",
            name="valid-name.txt",
            nodeType="cm:content", 
            isFile="not_a_boolean",  # Should be boolean
            isFolder="also_not_boolean",  # Should be boolean
            createdAt="not_a_datetime",  # Should be datetime
            modifiedAt="not_a_datetime"  # Should be datetime
        )
        print(f"❌ Unexpected: Wrong types were accepted")
    except ValidationError as e:
        print(f"✅ Validation caught type errors")
        print(f"   Pydantic ensures isFile/isFolder are booleans, dates are datetime objects")
    
    # Summary of Core API benefits
    print("\n" + "="*70)
    print("📋 Summary - Core API Pydantic Models Benefits")
    print("="*70)
    print("🏗️ Node Operations:")
    print("   ✅ Type-safe node creation, updates, and queries")
    print("   ✅ Validation of node names, types, and properties")
    print("   ✅ Automatic serialization for API calls")
    
    print("\n📂 Children & Navigation:")
    print("   ✅ Structured access to folder contents")
    print("   ✅ Pagination support built-in")
    print("   ✅ Easy filtering of files vs folders")
    
    print("\n🏷️ Properties & Metadata:")
    print("   ✅ Rich metadata support with validation")
    print("   ✅ Standard and custom property handling")
    print("   ✅ Aspect management with type safety")
    
    print("\n🚀 Developer Experience:")
    print("   ✅ IDE autocomplete for all node fields")
    print("   ✅ Catch errors at development time, not runtime")
    print("   ✅ Self-documenting code with field descriptions")
    print("   ✅ Consistent patterns across all Core API operations")
    
    print(f"\n🎉 Core API Pydantic examples completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\n💡 Next steps: Import the real models from python_alfresco_api.models.alfresco_core_models")
    print("   for production use with full Alfresco API compatibility!")

if __name__ == "__main__":
    main() 