"""
Basic MCP client example for Alfresco MCP Server.

This example demonstrates how to connect to and use the Alfresco MCP server.
"""

import asyncio
import logging
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    """Main example function."""
    
    # Server parameters for stdio connection
    server_params = StdioServerParameters(
        command="python",
        args=["-m", "alfresco_mcp_server.main", "--transport", "stdio"],
        env=None,
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()
            logger.info("Connected to Alfresco MCP Server")
            
            # List available tools
            tools = await session.list_tools()
            logger.info(f"Available tools: {[tool.name for tool in tools.tools]}")
            
            # List available resources
            resources = await session.list_resources()
            logger.info(f"Available resources: {[resource.uri for resource in resources.resources]}")
            
            # List available prompts
            prompts = await session.list_prompts()
            logger.info(f"Available prompts: {[prompt.name for prompt in prompts.prompts]}")
            
            # Example: Search for content
            try:
                search_result = await session.call_tool(
                    "search_content", 
                    arguments={"query": "test", "max_results": 5}
                )
                logger.info(f"Search result: {search_result}")
            except Exception as e:
                logger.error(f"Search failed: {e}")
            
            # Example: Get repository info
            try:
                repo_content, mime_type = await session.read_resource("alfresco://repository")
                logger.info(f"Repository info: {repo_content}")
            except Exception as e:
                logger.error(f"Resource read failed: {e}")


if __name__ == "__main__":
    asyncio.run(main()) 