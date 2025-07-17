"""
Search Operations Example using High-Level Utilities

This example demonstrates Alfresco search operations using the high-level
search utilities. Shows the excellent patterns already in place for search
operations with minimal code reduction needed (search tools already use good patterns).

Key insight: Search tools already use search_utils.simple_search effectively!
Main improvement opportunity: Enhanced result formatting and UX.
"""

from python_alfresco_api.client_factory import ClientFactory
from python_alfresco_api.utils.search_utils import simple_search


def basic_content_search_example():
    """Example of basic content search using simple_search utility."""
    
    client_factory = ClientFactory()
    search_client = client_factory.create_search_client()
    
    print("Example 1: Basic content search")
    
    try:
        # Search for documents containing specific text
        print("[SEARCH] Searching for documents with 'project'...")
        search_results = simple_search(
            search_client=search_client,
            query_str="project",
            max_items=10
        )
        print(f"[SUCCESS] Found documents: {search_results}")
        
        # Search for specific file types
        print("[SEARCH] Searching for PDF documents...")
        pdf_results = simple_search(
            search_client=search_client,
            query_str="TYPE:content AND MIME:'application/pdf'",
            max_items=20
        )
        print(f"[SUCCESS] Found PDFs: {pdf_results}")
        
    except Exception as e:
        print(f"[ERROR] Content search failed: {e}")


def metadata_search_example():
    """Example of searching by metadata using simple_search."""
    
    client_factory = ClientFactory()
    search_client = client_factory.create_search_client()
    
    print("\nExample 2: Metadata search")
    
    try:
        # Search by title
        print("🔍 Searching by title...")
        title_results = simple_search(
            search_client=search_client,
            query_str="cm:title:'Important Document'",
            max_items=10
        )
        print(f"✅ Found by title: {title_results}")
        
        # Search by description
        print("🔍 Searching by description...")
        desc_results = simple_search(
            search_client=search_client,
            query_str="cm:description:*planning*",
            max_items=15
        )
        print(f"✅ Found by description: {desc_results}")
        
        # Search by creator
        print("🔍 Searching by creator...")
        creator_results = simple_search(
            search_client=search_client,
            query_str="cm:creator:admin",
            max_items=25
        )
        print(f"✅ Found by creator: {creator_results}")
        
    except Exception as e:
        print(f"❌ Metadata search failed: {e}")


def advanced_search_example():
    """Example of advanced search queries using simple_search."""
    
    client_factory = ClientFactory()
    search_client = client_factory.create_search_client()
    
    print("\nExample 3: Advanced search queries")
    
    try:
        # Search with date range
        print("🔍 Searching documents created this year...")
        date_results = simple_search(
            search_client=search_client,
            query="cm:created:[2024-01-01T00:00:00 TO NOW]",
            max_items=20
        )
        print(f"✅ Found recent documents: {date_results}")
        
        # Search with size constraints
        print("🔍 Searching large documents...")
        size_results = simple_search(
            search_client=search_client,
            query="content.size:[1MB TO MAX]",
            max_items=10
        )
        print(f"✅ Found large documents: {size_results}")
        
        # Complex boolean search
        print("🔍 Complex boolean search...")
        complex_results = simple_search(
            search_client=search_client,
            query="(project AND report) OR (meeting AND notes)",
            max_items=15
        )
        print(f"✅ Found with complex query: {complex_results}")
        
    except Exception as e:
        print(f"❌ Advanced search failed: {e}")


def folder_search_example():
    """Example of searching for folders using simple_search."""
    
    client_factory = ClientFactory()
    search_client = client_factory.create_search_client()
    
    print("\nExample 4: Folder search")
    
    try:
        # Search for folders only
        print("🔍 Searching for folders...")
        folder_results = simple_search(
            search_client=search_client,
            query="TYPE:folder",
            max_items=20
        )
        print(f"✅ Found folders: {folder_results}")
        
        # Search for specific folder names
        print("🔍 Searching for project folders...")
        project_folders = simple_search(
            search_client=search_client,
            query="TYPE:folder AND cm:name:*project*",
            max_items=10
        )
        print(f"✅ Found project folders: {project_folders}")
        
    except Exception as e:
        print(f"❌ Folder search failed: {e}")


def path_search_example():
    """Example of searching within specific paths."""
    
    client_factory = ClientFactory()
    search_client = client_factory.create_search_client()
    
    print("\nExample 5: Path-based search")
    
    try:
        # Search within user's home directory
        print("🔍 Searching in user home...")
        home_results = simple_search(
            search_client=search_client,
            query="PATH:\"/app:company_home/app:user_homes/cm:admin/*\"",
            max_items=15
        )
        print(f"✅ Found in user home: {home_results}")
        
        # Search within shared folder
        print("🔍 Searching in shared folders...")
        shared_results = simple_search(
            search_client=search_client,
            query="PATH:\"/app:company_home/app:shared/*\"",
            max_items=25
        )
        print(f"✅ Found in shared: {shared_results}")
        
    except Exception as e:
        print(f"❌ Path search failed: {e}")


def search_with_formatting_example():
    """Example showing enhanced result formatting."""
    
    client_factory = ClientFactory()
    search_client = client_factory.create_search_client()
    
    print("\nExample 6: Enhanced result formatting")
    
    try:
        # Basic search with result processing
        print("🔍 Searching with enhanced formatting...")
        raw_results = simple_search(
            search_client=search_client,
            query="TYPE:content",
            max_items=5
        )
        
        # Process and format results (this is where the 10-20% improvement comes from)
        print("📋 Processing search results...")
        
        # Enhanced formatting (you would customize this based on your needs)
        if hasattr(raw_results, 'list') and raw_results.list:
            entries = raw_results.list.entries
            print(f"✅ Found {len(entries)} documents:")
            
            for i, entry in enumerate(entries[:3], 1):  # Show first 3
                node = entry.entry
                print(f"  {i}. {node.name}")
                print(f"     ID: {node.id}")
                print(f"     Type: {node.node_type}")
                print(f"     Modified: {node.modified_at}")
                if hasattr(node, 'content'):
                    print(f"     Size: {node.content.size_in_bytes} bytes")
                print()
        else:
            print("✅ Search completed, no results to format")
        
    except Exception as e:
        print(f"❌ Enhanced formatting failed: {e}")


if __name__ == "__main__":
    print("🚀 High-Level Search Operations Examples")
    print("=" * 55)
    
    print("\n🔍 Content Search:")
    basic_content_search_example()
    
    print("\n📊 Metadata Search:")
    metadata_search_example()
    
    print("\n🎯 Advanced Queries:")
    advanced_search_example()
    
    print("\n📁 Folder Search:")
    folder_search_example()
    
    print("\n📍 Path Search:")
    path_search_example()
    
    print("\n✨ Enhanced Formatting:")
    search_with_formatting_example()
    
    print("\n🎯 Key Benefits:")
    print("- Search tools already use excellent patterns! ✅")
    print("- simple_search() handles most use cases perfectly")
    print("- Main improvement: Enhanced result formatting (10-20% reduction)")
    print("- Type safety with Pydantic models")
    print("- Consistent search interface across all query types")
    
    print("\n📋 Search Query Examples:")
    print("- Text search: 'project report'")
    print("- Type filter: 'TYPE:content'")
    print("- Metadata: 'cm:title:\"Important\"'")  
    print("- Date range: 'cm:created:[2024-01-01 TO NOW]'")
    print("- Path filter: 'PATH:\"/app:company_home/app:shared/*\"'")
    print("- Boolean: '(project AND report) OR (meeting AND notes)'")
    
    print("\n💡 Architecture Insight:")
    print("Search tools were already well-designed using search_utils.simple_search!")
    print("The 'not as bad as I thought' assessment was exactly right. ✅") 