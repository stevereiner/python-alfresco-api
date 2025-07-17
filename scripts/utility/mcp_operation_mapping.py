#!/usr/bin/env python3
"""
MCP-Focused Operation Filtering

This demonstrates how to filter the 133 Alfresco operations down to just the 14 
operations needed for your MCP server.
"""

# Your MCP Server needs 14 operations
MCP_TO_ALFRESCO_MAPPING = {
    # ================================================================
    # SEARCH OPERATIONS (4 MCP tools)
    # ================================================================
    "search_content": {
        "alfresco_operation": "search",
        "client": "search",
        "api_path": "search/search.py"
    },
    "advanced_search": {
        "alfresco_operation": "search", 
        "client": "search",
        "api_path": "search/search.py"
    },
    "search_by_metadata": {
        "alfresco_operation": "search",
        "client": "search", 
        "api_path": "search/search.py"
    },
    "cmis_search": {
        "alfresco_operation": "search",
        "client": "search_sql",
        "api_path": "sql/search.py"
    },
    
    # ================================================================
    # NODE/CONTENT OPERATIONS (7 MCP tools)
    # ================================================================
    "browse_repository": {
        "alfresco_operation": "list_node_children",
        "client": "core",
        "api_path": "nodes/list_node_children.py"
    },
    "get_node_properties": {
        "alfresco_operation": "get_node",
        "client": "core",
        "api_path": "nodes/get_node.py"
    },
    "update_node_properties": {
        "alfresco_operation": "update_node",
        "client": "core", 
        "api_path": "nodes/update_node.py"
    },
    "delete_node": {
        "alfresco_operation": "delete_node",
        "client": "core",
        "api_path": "nodes/delete_node.py"
    },
    "create_folder": {
        "alfresco_operation": "create_node",
        "client": "core",
        "api_path": "nodes/create_node.py"
    },
    "upload_document": {
        "alfresco_operation": "update_node_content",
        "client": "core",
        "api_path": "nodes/update_node_content.py"
    },
    "download_document": {
        "alfresco_operation": "get_node_content", 
        "client": "core",
        "api_path": "nodes/get_node_content.py"
    },
    
    # ================================================================
    # VERSIONING OPERATIONS (3 MCP tools)  
    # ================================================================
    "checkout_document": {
        "alfresco_operation": "checkout_version",  # Custom - needs implementation
        "client": "core",
        "api_path": "versions/checkout.py"  # May not exist yet
    },
    "checkin_document": {
        "alfresco_operation": "checkin_version",  # Custom - needs implementation
        "client": "core", 
        "api_path": "versions/checkin.py"  # May not exist yet
    },
    "cancel_checkout": {
        "alfresco_operation": "cancel_checkout",  # Custom - needs implementation
        "client": "core",
        "api_path": "versions/cancel_checkout.py"  # May not exist yet
    }
}

# ================================================================
# FILTERING RESULTS 
# ================================================================

def analyze_mcp_filtering():
    """Analyze what MCP filtering achieves."""
    
    # Total Alfresco operations discovered by generator
    total_alfresco_operations = 133
    
    # MCP operations needed
    mcp_operations = len(MCP_TO_ALFRESCO_MAPPING)
    
    # Unique Alfresco operations needed (some MCP ops share Alfresco ops)
    unique_alfresco_ops = set()
    for mcp_op, mapping in MCP_TO_ALFRESCO_MAPPING.items():
        unique_alfresco_ops.add(mapping["alfresco_operation"])
    
    unique_count = len(unique_alfresco_ops)
    
    print("🎯 MCP-FOCUSED OPERATION FILTERING ANALYSIS")
    print("=" * 50)
    print(f"📊 Total Alfresco operations available: {total_alfresco_operations}")
    print(f"🤖 MCP operations needed: {mcp_operations}")
    print(f"⚡ Unique Alfresco operations needed: {unique_count}")
    print(f"🔄 Reduction ratio: {unique_count}/{total_alfresco_operations} = {unique_count/total_alfresco_operations:.1%}")
    print(f"💾 Code reduction: {(total_alfresco_operations-unique_count)/total_alfresco_operations:.1%} smaller")
    
    print("\n🌳 OPERATION GROUPING:")
    clients = {}
    for mcp_op, mapping in MCP_TO_ALFRESCO_MAPPING.items():
        client = mapping["client"]
        if client not in clients:
            clients[client] = []
        clients[client].append(mcp_op)
    
    for client, ops in clients.items():
        print(f"  📦 {client}: {len(ops)} operations - {ops}")
    
    print("\n✅ BENEFITS OF MCP FILTERING:")
    print("  - 91% reduction in generated code size")
    print("  - Only generate what you actually use")
    print("  - Faster compilation and smaller packages")
    print("  - Cleaner, focused API surface")
    print("  - Better IDE autocomplete")
    
    return unique_alfresco_ops

def generate_filtered_imports(client_name: str) -> str:
    """Generate filtered imports for a specific client."""
    
    # Filter operations for this client
    client_ops = []
    for mcp_op, mapping in MCP_TO_ALFRESCO_MAPPING.items():
        if mapping["client"] == client_name:
            client_ops.append(mapping["alfresco_operation"])
    
    # Remove duplicates
    unique_ops = list(set(client_ops))
    
    if not unique_ops:
        return f"# No operations needed for {client_name} client"
    
    # Group by API category
    api_categories = {}
    for op in unique_ops:
        # Determine API category from operation name
        if op in ["get_node", "create_node", "update_node", "delete_node", "list_node_children", "get_node_content", "update_node_content"]:
            category = "nodes"
        elif op in ["find_nodes"]:
            category = "queries"
        elif op in ["search"]:
            category = "search"
        elif "version" in op or "checkout" in op or "checkin" in op:
            category = "versions"
        else:
            category = "other"
        
        if category not in api_categories:
            api_categories[category] = []
        api_categories[category].append(f"{op} as _{op}")
    
    # Generate import statements
    imports = []
    for category, ops in api_categories.items():
        imports.append(f"""    # {category.title()} operations (MCP-filtered)
    from python_alfresco_api.raw_clients.alfresco_{client_name}_client.{client_name}_client.api.{category} import (
        {', '.join(ops)}
    )""")
    
    return "\n".join(imports)

if __name__ == "__main__":
    print("🎯 MCP-FOCUSED OPERATION FILTERING DEMO")
    print()
    
    # Analyze the filtering
    unique_ops = analyze_mcp_filtering()
    
    print(f"\n📋 UNIQUE ALFRESCO OPERATIONS NEEDED:")
    for op in sorted(unique_ops):
        print(f"  - {op}")
    
    print(f"\n🔧 FILTERED IMPORTS FOR CORE CLIENT:")
    print(generate_filtered_imports("core"))
    
    print(f"\n🔧 FILTERED IMPORTS FOR SEARCH CLIENT:")
    print(generate_filtered_imports("search"))
    
    print(f"\n🔧 FILTERED IMPORTS FOR SEARCH_SQL CLIENT:")
    print(generate_filtered_imports("search_sql")) 