#!/usr/bin/env python3
"""
Alfresco Model API Examples

This file demonstrates how to use the Model API with the master client.
The Model API provides access to content model definitions, types, and aspects.
"""

import sys
import os

from python_alfresco_api import ClientFactory

def main():
    """Model API examples."""
    print("🏗️ Model API Examples")
    
    # Initialize client
    factory = ClientFactory(base_url="http://localhost:8080", username="admin", password="admin")
    client = factory.create_master_client()
    
    if not client.model:
        print("❌ Model API not available")
        return
    
    # Check Model API structure
    if isinstance(client.model, dict):
        print(f"Available Model APIs: {list(client.model.keys())}")
        
        # Example 1: List Custom Models
        if 'custom_models' in client.model:
            print("\n1. Getting custom models...")
            try:
                models = client.model['custom_models'].get_custom_models()
                if models and hasattr(models, 'list'):
                    print(f"✅ Found {len(models.list.entries)} custom models")
                    for i, model in enumerate(models.list.entries[:3]):
                        if hasattr(model, 'entry'):
                            print(f"  {i+1}. {model.entry.name}: {getattr(model.entry, 'description', 'No description')}")
                else:
                    print("✅ Custom Models API responded")
            except Exception as e:
                print(f"❌ Custom Models API failed: {e}")
        
        # Example 2: List Aspects
        if 'aspects' in client.model:
            print("\n2. Getting aspects...")
            try:
                aspects = client.model['aspects'].get_aspects()
                if aspects and hasattr(aspects, 'list'):
                    print(f"✅ Found {len(aspects.list.entries)} aspects")
                    for i, aspect in enumerate(aspects.list.entries[:3]):
                        if hasattr(aspect, 'entry'):
                            print(f"  {i+1}. {aspect.entry.name}: {getattr(aspect.entry, 'title', 'No title')}")
                else:
                    print("✅ Aspects API responded")
            except Exception as e:
                print(f"❌ Aspects API failed: {e}")
        
        # Example 3: List Types
        if 'types' in client.model:
            print("\n3. Getting types...")
            try:
                types = client.model['types'].get_types()
                if types and hasattr(types, 'list'):
                    print(f"✅ Found {len(types.list.entries)} types")
                    for i, type_def in enumerate(types.list.entries[:3]):
                        if hasattr(type_def, 'entry'):
                            print(f"  {i+1}. {type_def.entry.name}: {getattr(type_def.entry, 'title', 'No title')}")
                else:
                    print("✅ Types API responded")
            except Exception as e:
                print(f"❌ Types API failed: {e}")
        
        # Example 4: Get specific aspect (using aspects API)
        if 'aspects' in client.model:
            print("\n4. Getting specific aspect details...")
            try:
                # Note: This requires the actual aspect ID, not name
                print("   Note: Requires valid aspect ID - using placeholder")
                aspect_detail = client.model['aspects'].get_aspect(aspect_id="placeholder")
                if aspect_detail:
                    print("✅ Aspect details retrieved")
                    if hasattr(aspect_detail, 'entry'):
                        print(f"   Name: {aspect_detail.entry.name}")
                        print(f"   Title: {getattr(aspect_detail.entry, 'title', 'No title')}")
                else:
                    print("✅ Get aspect API responded")
            except Exception as e:
                print(f"❌ Get aspect failed (expected with placeholder ID): {e}")
        
        # Example 5: Get specific type (using types API)
        if 'types' in client.model:
            print("\n5. Getting specific type details...")
            try:
                # Note: This requires the actual type ID, not name
                print("   Note: Requires valid type ID - using placeholder")
                type_detail = client.model['types'].get_type(type_id="placeholder")
                if type_detail:
                    print("✅ Type details retrieved")
                    if hasattr(type_detail, 'entry'):
                        print(f"   Name: {type_detail.entry.name}")
                        print(f"   Title: {getattr(type_detail.entry, 'title', 'No title')}")
                else:
                    print("✅ Get type API responded")
            except Exception as e:
                print(f"❌ Get type failed (expected with placeholder ID): {e}")
    
    else:
        print("Model API available in single object format")
        # Example for single object format
        if hasattr(client.model, 'list_custom_models'):
            print("\n1. Testing model functionality...")
            try:
                models = client.model.list_custom_models()
                print("✅ Model functionality available")
            except Exception as e:
                print(f"❌ Model failed: {e}")

if __name__ == "__main__":
    main() 