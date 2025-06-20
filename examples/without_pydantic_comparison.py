#!/usr/bin/env python3
"""
Alfresco API: With vs Without Pydantic Models Comparison

This example demonstrates the dramatic difference between using Pydantic models
vs basic Python types when working with Alfresco APIs.
"""

import sys
import os
from datetime import datetime
from typing import Dict, Any, List, Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'enhanced_generated'))

# Raw JSON/dict responses vs Pydantic models
import json


def main():
    """Compare Alfresco API usage with and without Pydantic models."""
    print("🔍 Alfresco API: With vs Without Pydantic Models")
    print("=" * 80)
    
    # =============================================================================
    # WITHOUT Pydantic Models - Raw Dictionaries and Basic Types
    # =============================================================================
    print("\n❌ WITHOUT Pydantic Models - Raw Python Dictionaries")
    print("=" * 70)
    
    print("📄 1. Raw API Response (what you'd get from requests.get().json()):")
    
    # This is what you get from raw API calls - just dictionaries
    raw_node_response = {
        "list": {
            "pagination": {
                "count": 3,
                "hasMoreItems": False,
                "totalItems": 3,
                "skipCount": 0,
                "maxItems": 100
            },
            "entries": [
                {
                    "entry": {
                        "id": "workspace://SpacesStore/12345",
                        "name": "Important Document.pdf",
                        "nodeType": "cm:content",
                        "isFile": True,
                        "isFolder": False,
                        "createdAt": "2024-01-15T10:30:45.123Z",
                        "modifiedAt": "2024-01-16T14:22:10.456Z",
                        "properties": {
                            "cm:title": "Important Document",
                            "cm:author": "John Smith",
                            "cm:description": "Critical business document"
                        },
                        "aspectNames": ["cm:titled", "cm:author"]
                    }
                },
                {
                    "entry": {
                        "id": "workspace://SpacesStore/67890", 
                        "name": "Project Folder",
                        "nodeType": "cm:folder",
                        "isFile": False,
                        "isFolder": True,
                        "createdAt": "2024-01-10T09:15:30.789Z",
                        "modifiedAt": "2024-01-16T16:45:22.123Z",
                        "properties": {
                            "cm:description": "Contains project files"
                        }
                    }
                }
            ]
        }
    }
    
    print("✅ Raw response structure:")
    print(f"   📊 Type: {type(raw_node_response)} (just a dictionary)")
    print(f"   🔍 Keys: {list(raw_node_response.keys())}")
    print(f"   📝 JSON size: {len(json.dumps(raw_node_response))} characters")
    
    # =============================================================================
    # Problems with Raw Dictionaries
    # =============================================================================
    print("\n⚠️ Problems with Raw Dictionary Approach:")
    print("-" * 50)
    
    print("🚫 1. NO Type Safety:")
    try:
        # These errors won't be caught until runtime!
        entries = raw_node_response["list"]["entries"]  # Could be None
        first_node = entries[0]["entry"]  # Could fail if empty
        
        # Typos in field names - no IDE help, silent failures
        wrong_field = first_node.get("titel")  # Typo: should be "title" 
        print(f"   ❌ Typo returns None: {wrong_field}")
        
        # Wrong nested access - runtime errors
        bad_access = first_node["properties"]["cm:titel"]  # Another typo
        print(f"   ❌ This would crash: {bad_access}")
        
    except KeyError as e:
        print(f"   💥 Runtime error: {e}")
    
    print("\n🚫 2. NO Validation:")
    # You can put anything in dictionaries - no validation!
    bad_node = {
        "name": "file|with:bad*chars.txt",  # Invalid filename - not caught!
        "isFile": "not_a_boolean",  # Wrong type - not caught!
        "createdAt": "not_a_date",  # Invalid date - not caught!
        "properties": "should_be_dict"  # Wrong type - not caught!
    }
    print(f"   ❌ Invalid data accepted: {bad_node['name']}")
    print(f"   ❌ Wrong types accepted: isFile = {bad_node['isFile']}")
    
    print("\n🚫 3. NO IDE Support:")
    print("   ❌ No autocomplete for field names")
    print("   ❌ No type hints or IntelliSense") 
    print("   ❌ No documentation in IDE")
    print("   ❌ Manual string-based field access prone to typos")
    
    print("\n🚫 4. Manual Data Processing:")
    # Processing children manually with dictionaries
    print("   📂 Processing folder children manually:")
    entries = raw_node_response["list"]["entries"]
    for i, entry_dict in enumerate(entries):
        node_dict = entry_dict["entry"]
        file_type = "📄" if node_dict.get("isFile") else "📁"
        print(f"      {i+1}. {file_type} {node_dict.get('name', 'Unknown')}")
        
        # Have to manually check for properties existence
        properties = node_dict.get("properties")
        if properties and isinstance(properties, dict):
            title = properties.get("cm:title")
            if title:
                print(f"         Title: {title}")
    
    print("\n🚫 5. Date Handling Nightmare:")
    # Dates come as strings - manual parsing required
    created_str = raw_node_response["list"]["entries"][0]["entry"]["createdAt"]
    print(f"   📅 Date as string: {created_str}")
    print("   ⚠️  Must manually parse: datetime.strptime() or dateutil.parser")
    print("   💥 Easy to get timezone/format errors")
    
    # =============================================================================
    # WITH Pydantic Models - Type-Safe, Validated, IDE-Friendly
    # =============================================================================
    print("\n" + "=" * 70)
    print("✅ WITH Pydantic Models - Type-Safe and Validated")
    print("=" * 70)
    
    # Import our Pydantic models
    from pydantic import BaseModel, Field, ValidationError
    
    # Define the same models as in our main example
    class Node(BaseModel):
        id: str
        name: str = Field(..., description="Node name with validation")
        nodeType: str
        isFile: bool
        isFolder: bool
        createdAt: datetime
        modifiedAt: datetime
        properties: Optional[Dict[str, Any]] = None
        aspectNames: Optional[List[str]] = None
    
    class NodeEntry(BaseModel):
        entry: Node
    
    class NodePaging(BaseModel):
        entries: Optional[List[NodeEntry]] = None
        pagination: Optional[Dict[str, Any]] = None
    
    class NodeListResponse(BaseModel):
        list: NodePaging
    
    print("📄 1. Same Data with Pydantic Models:")
    
    # Convert raw response to Pydantic models
    try:
        # This automatically validates and converts the data!
        pydantic_response = NodeListResponse(**raw_node_response)
        
        print("✅ Pydantic response structure:")
        print(f"   📊 Type: {type(pydantic_response)} (Pydantic model)")
        print(f"   🔍 Fields: {list(pydantic_response.model_fields.keys())}")
        print(f"   ✅ All data validated and type-converted automatically!")
        
    except ValidationError as e:
        print(f"❌ Validation failed: {e}")
    
    # =============================================================================
    # Benefits of Pydantic Models
    # =============================================================================
    print("\n🎉 Benefits of Pydantic Models:")
    print("-" * 50)
    
    print("✅ 1. Type Safety & IDE Support:")
    print("   🔍 Full autocomplete for all fields")
    print("   📖 Built-in documentation") 
    print("   🚨 IDE warns about typos BEFORE runtime")
    print("   💡 IntelliSense shows field types and descriptions")
    
    # Demonstrate IDE-friendly access
    if 'pydantic_response' in locals():
        print("\n   💻 IDE-friendly access:")
        print("   # response.list.entries[0].entry.name  ← Full autocomplete!")
        print("   # response.list.entries[0].entry.isFile  ← Type hints!")
        print("   # response.list.entries[0].entry.createdAt  ← datetime object!")
    
    print("\n✅ 2. Automatic Validation:")
    print("   🛡️  Invalid data rejected at creation time")
    print("   🔒 Type conversion (strings to dates, etc.)")
    print("   📏 Field validation (required fields, formats, etc.)")
    
    # Demonstrate validation
    print("\n   🧪 Validation examples:")
    try:
        # This will fail validation
        invalid_node = Node(
            id="valid-id",
            name="valid-name.txt",
            nodeType="cm:content",
            isFile="not_a_boolean",  # Wrong type
            isFolder=True,
            createdAt="not_a_date",  # Invalid date
            modifiedAt=datetime.now()
        )
    except ValidationError as e:
        print(f"   ✅ Caught validation error: Type conversion failed")
    
    print("\n✅ 3. Automatic Date Handling:")
    if 'pydantic_response' in locals():
        first_node = pydantic_response.list.entries[0].entry
        print(f"   📅 Automatic date parsing: {first_node.createdAt}")
        print(f"   🕐 Python datetime object: {type(first_node.createdAt)}")
        print(f"   📊 Can do date math: {first_node.createdAt.strftime('%Y-%m-%d')}")
    
    print("\n✅ 4. Clean Data Processing:")
    if 'pydantic_response' in locals():
        print("   📂 Processing with type safety:")
        for i, child_entry in enumerate(pydantic_response.list.entries or []):
            node = child_entry.entry  # Fully typed Node object
            icon = "📄" if node.isFile else "📁"
            print(f"      {i+1}. {icon} {node.name}")
            
            # Safe property access with type hints
            if node.properties and "cm:title" in node.properties:
                print(f"         Title: {node.properties['cm:title']}")
    
    print("\n✅ 5. Serialization Benefits:")
    if 'pydantic_response' in locals():
        # Easy conversion back to dict/JSON
        as_dict = pydantic_response.model_dump()
        as_json = pydantic_response.model_dump_json()
        print(f"   📤 Convert to dict: {len(str(as_dict))} chars")
        print(f"   📤 Convert to JSON: {len(as_json)} chars")
        print("   ✅ Perfect for API calls and data exchange")
    
    # =============================================================================
    # Real-World Code Comparison
    # =============================================================================
    print("\n" + "=" * 70)
    print("🔍 Real-World Code Comparison")
    print("=" * 70)
    
    print("📝 WITHOUT Pydantic (Raw Dictionaries):")
    print("```python")
    print("# Manual dictionary navigation - error prone")
    print("def process_folder_contents(api_response):")
    print("    try:")
    print("        entries = api_response['list']['entries']  # Could fail")
    print("        for entry in entries:")
    print("            node = entry['entry']  # More failure points")
    print("            name = node.get('name', 'Unknown')  # Manual defaults")
    print("            ")
    print("            # Manual type checking")
    print("            if node.get('isFile') == True:  # Fragile comparison")
    print("                print(f'File: {name}')")
    print("            ")
    print("            # Manual date parsing")
    print("            created_str = node.get('createdAt')")
    print("            if created_str:")
    print("                # Complex date parsing logic...")
    print("                pass")
    print("                ")
    print("            # Manual property access")
    print("            props = node.get('properties', {})")
    print("            title = props.get('cm:title')  # More string literals")
    print("            ")
    print("    except (KeyError, TypeError) as e:")
    print("        print(f'Data structure error: {e}')")
    print("```")
    
    print("\n📝 WITH Pydantic Models:")
    print("```python")
    print("# Type-safe, validated, IDE-friendly")
    print("def process_folder_contents(api_response: NodeListResponse):")
    print("    # No try/catch needed - structure guaranteed")
    print("    for child_entry in api_response.list.entries:")
    print("        node = child_entry.entry  # Fully typed Node")
    print("        ")
    print("        # Type-safe property access with autocomplete")
    print("        if node.isFile:  # Boolean, not string comparison")
    print("            print(f'File: {node.name}')  # IDE autocomplete")
    print("        ")
    print("        # Automatic date handling")
    print("        age_days = (datetime.now() - node.createdAt).days")
    print("        ")
    print("        # Safe property access")
    print("        if node.properties and 'cm:title' in node.properties:")
    print("            title = node.properties['cm:title']")
    print("```")
    
    # =============================================================================
    # Performance and Memory Comparison
    # =============================================================================
    print("\n" + "=" * 70)
    print("⚡ Performance & Memory Impact")
    print("=" * 70)
    
    print("📊 Raw Dictionaries:")
    print("   ✅ Faster initial parsing (no validation)")
    print("   ✅ Lower memory usage")
    print("   ❌ Runtime errors cost more than validation")
    print("   ❌ More code = more bugs = more debugging time")
    
    print("\n📊 Pydantic Models:")
    print("   ⚡ Small validation overhead (usually <1ms)")
    print("   📈 Slightly higher memory usage")
    print("   ✅ Catches errors early = saves debugging time")
    print("   ✅ Cleaner code = faster development")
    print("   ✅ IDE support = fewer bugs")
    
    # =============================================================================
    # Summary
    # =============================================================================
    print("\n" + "=" * 70)
    print("📋 Summary: The Dramatic Difference")
    print("=" * 70)
    
    print("❌ WITHOUT Pydantic Models:")
    print("   🚫 Raw dictionaries with manual string-based access")
    print("   🚫 No type safety - errors at runtime")
    print("   🚫 No validation - bad data accepted silently")
    print("   🚫 No IDE support - prone to typos")
    print("   🚫 Manual date parsing and type conversion")
    print("   🚫 Verbose error-prone code")
    
    print("\n✅ WITH Pydantic Models:")
    print("   🎯 Strongly typed objects with autocomplete")
    print("   🛡️  Automatic validation and type conversion")
    print("   💻 Full IDE support with IntelliSense")
    print("   📅 Automatic date/time handling")
    print("   🧹 Clean, maintainable code")
    print("   🚀 Catch errors at development time, not production")
    
    print("\n🎉 Result: Pydantic transforms Alfresco API from error-prone")
    print("   dictionary manipulation into type-safe, IDE-friendly,")
    print("   self-documenting code that catches bugs early!")
    
    print(f"\n✨ Comparison completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    main() 