"""
LLM Integration Example - python-alfresco-api

Demonstrates using Pydantic models for LLM tool interfaces and MCP servers.
"""

from typing import Dict, Any
from python_alfresco_api import ClientFactory
from python_alfresco_api.models import TicketBody, NodeBody, SearchRequest

# Initialize client factory
factory = ClientFactory(
    base_url="https://alfresco.example.com",
    username="admin",
    password="admin123"
)

# LLM Tool Functions using Pydantic models
def authenticate_user_tool(credentials: TicketBody) -> Dict[str, Any]:
    """
    LLM tool for user authentication.

    Args:
        credentials: User credentials with userId and password

    Returns:
        Authentication result with ticket information
    """
    auth_client = factory.create_auth_client()

    try:
        # The Pydantic model ensures type safety and validation
        result = auth_client.create_ticket(credentials)
        return {
            "success": True,
            "ticket": result.entry.id if result and result.entry else None,
            "user": credentials.userId
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

def create_document_tool(document_data: NodeBody) -> Dict[str, Any]:
    """
    LLM tool for creating documents.

    Args:
        document_data: Document information (name, nodeType, etc.)

    Returns:
        Created document information
    """
    core_client = factory.create_core_client()

    try:
        # Pydantic model provides perfect validation for LLM inputs
        result = core_client.create_node(document_data)
        return {
            "success": True,
            "node_id": result.entry.id if result and result.entry else None,
            "name": document_data.name
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

def search_documents_tool(search_query: SearchRequest) -> Dict[str, Any]:
    """
    LLM tool for document search.

    Args:
        search_query: Search parameters and query

    Returns:
        Search results with documents
    """
    search_client = factory.create_search_client()

    try:
        # Pydantic model handles complex search parameters
        result = search_client.search(search_query)
        return {
            "success": True,
            "total_items": result.list.pagination.totalItems if result and result.list and result.list.pagination else 0,
            "documents": [entry.entry for entry in result.list.entries] if result and result.list and result.list.entries else []
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

# MCP Server Integration Example
class AlfrescoMCPServer:
    """
    Model Context Protocol server for Alfresco integration.

    Provides natural language interface to Alfresco operations.
    """

    def __init__(self, base_url: str, username: str, password: str):
        self.factory = ClientFactory(base_url, username, password)

    async def handle_natural_language_query(self, query: str) -> Dict[str, Any]:
        """
        Handle natural language queries like:
        - "Find all documents modified this week"
        - "Create a new folder called 'Projects'"
        - "Search for documents containing 'budget'"
        """

        # This would integrate with your LLM to parse the natural language
        # and convert to appropriate API calls using the Pydantic models

        if "search" in query.lower():
            # Convert natural language to SearchRequest
            search_request = SearchRequest(
                query={"query": query},
                paging={"maxItems": 25}
            )
            return search_documents_tool(search_request)

        elif "create" in query.lower() and "folder" in query.lower():
            # Convert natural language to NodeBody for folder creation
            folder_data = NodeBody(
                name="Projects",  # Extract from query
                nodeType="cm:folder"
            )
            return create_document_tool(folder_data)

        else:
            return {"success": False, "error": "Query not understood"}

# Example usage
if __name__ == "__main__":
    print("LLM Integration Example")
    print("=" * 30)

    # Test authentication tool
    creds = TicketBody(userId="admin", password="admin123")
    auth_result = authenticate_user_tool(creds)
    print(f"Authentication: {auth_result}")

    # Test document creation tool
    doc_data = NodeBody(name="test-document.txt", nodeType="cm:content")
    create_result = create_document_tool(doc_data)
    print(f"Document creation: {create_result}")

    print("\nPerfect for LLM tool interfaces!")
    print("Type-safe with Pydantic validation!")
    print("Ready for MCP server integration!")
