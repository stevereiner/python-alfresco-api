"""
Update node content (file upload) operations for Alfresco nodes.
Clean function-based approach with 4 patterns: sync, async, detailed_sync, detailed_async.
"""

import io
from typing import Optional, List, Union, IO, BinaryIO
from .models import NodeResponse, NodeListResponse


def update_node_content(
    client,
    node_id: str, 
    content: Union[bytes, IO[bytes]], 
    filename: Optional[str] = None, 
    include: Optional[List[str]] = None
) -> NodeResponse:
    """
    Update node content (file upload) (synchronous).
    
    Perfect for scripts, MCP servers, and command-line tools.
    
    Args:
        client: NodesClient instance
        node_id (str): Node identifier to update content for
        content (Union[bytes, IO[bytes]]): File content as bytes or file-like object
        filename (Optional[str]): Name for the uploaded file
        include (Optional[List[str]]): Additional data to include in response
        
    Returns:
        NodeResponse: Updated node information
        
    Examples:
        ```python
        # Update file content with bytes
        with open("document.pdf", "rb") as f:
            content = f.read()
        
        updated = client.nodes.update_content(
            node_id="abc123-def456",
            content=content,
            filename="updated_document.pdf"
        )
        
        # Update with file-like object
        with open("document.pdf", "rb") as f:
            updated = client.nodes.update_content(
                node_id="abc123-def456",
                content=f,
                filename="updated_document.pdf",
                include=["properties"]
            )
        ```
        
    Raises:
        NodeNotFoundError: Node with given ID doesn't exist
        PermissionError: User lacks permission to update node content
        ValidationError: Invalid request parameters
        
    Note:
        This method calls the raw sync client directly for optimal performance.
        For async operations, use update_node_content_async().
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import update_node_content
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET, File
    
    # Get raw client
    raw_client = client.raw_client
    
    # Convert include options
    include_params = UNSET
    if include:
        include_params = include
    
    # Create File object for upload
    if isinstance(content, bytes):
        file_payload: BinaryIO = io.BytesIO(content)
    else:
        file_payload: BinaryIO = content  # type: ignore
    
    file_obj = File(
        payload=file_payload,
        file_name=filename or "content"
    )
    
    # Execute raw sync operation
    result = update_node_content.sync(
        client=raw_client,
        node_id=node_id,
        body=file_obj,
        include=include_params
    )
    
    # Validate and return rich model
    if result is None:
        raise ValueError(f"Failed to update content for node {node_id}")
    return NodeResponse.model_validate(result.to_dict())


async def update_node_content_async(
    client,
    node_id: str, 
    content: Union[bytes, IO[bytes]], 
    filename: Optional[str] = None, 
    include: Optional[List[str]] = None
) -> NodeResponse:
    """
    Update node content (file upload) (asynchronous).
    
    Args:
        client: NodesClient instance
        node_id: Node identifier to update content for
        content: File content as bytes or file-like object
        filename: Name for the uploaded file
        include: Additional data to include in response
        
    Returns:
        NodeResponse: Updated node information
        
    Examples:
        ```python
        # Update file content (async)
        with open("document.pdf", "rb") as f:
            updated = await client.nodes.update_content_async(
                node_id="abc123-def456",
                content=f,
                filename="updated_document.pdf"
            )
        ```
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import update_node_content
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET, File
    
    # Get raw client
    raw_client = client.raw_client
    
    # Convert include options
    include_params = UNSET
    if include:
        include_params = include
    
    # Create File object for upload
    if isinstance(content, bytes):
        file_payload: BinaryIO = io.BytesIO(content)
    else:
        file_payload: BinaryIO = content  # type: ignore
    
    file_obj = File(
        payload=file_payload,
        file_name=filename or "content"
    )
    
    # Execute raw async operation
    result = await update_node_content.asyncio(
        client=raw_client,
        node_id=node_id,
        body=file_obj,
        include=include_params
    )
    
    # Validate and return rich model
    if result is None:
        raise ValueError(f"Failed to update content for node {node_id}")
    return NodeResponse.model_validate(result.to_dict())


def update_node_content_detailed(
    client,
    node_id: str, 
    content: Union[bytes, IO[bytes]], 
    filename: Optional[str] = None, 
    include: Optional[List[str]] = None
):
    """
    Update node content (file upload) (detailed sync).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Args:
        client: NodesClient instance
        node_id: Node identifier to update content for
        content: File content as bytes or file-like object
        filename: Name for the uploaded file
        include: Additional data to include in response
        
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import update_node_content
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET, File
    
    # Get raw client
    raw_client = client.raw_client
    
    # Convert include options
    include_params = UNSET
    if include:
        include_params = include
    
    # Create File object for upload
    if isinstance(content, bytes):
        file_payload: BinaryIO = io.BytesIO(content)
    else:
        file_payload: BinaryIO = content  # type: ignore
    
    file_obj = File(
        payload=file_payload,
        file_name=filename or "content"
    )
    
    # Execute raw sync_detailed operation
    return update_node_content.sync_detailed(
        client=raw_client,
        node_id=node_id,
        body=file_obj,
        include=include_params
    )


async def update_node_content_detailed_async(
    client,
    node_id: str, 
    content: Union[bytes, IO[bytes]], 
    filename: Optional[str] = None, 
    include: Optional[List[str]] = None
):
    """
    Update node content (file upload) (detailed async).
    
    Perfect for MCP servers needing full HTTP response details.
    Returns complete Response object with status_code, headers, content, parsed.
    
    Args:
        client: NodesClient instance
        node_id: Node identifier to update content for
        content: File content as bytes or file-like object
        filename: Name for the uploaded file
        include: Additional data to include in response
        
    Returns:
        Response: Complete response with status_code, headers, content, parsed
    """
    # Lazy import of raw operation
    from ....raw_clients.alfresco_core_client.core_client.api.nodes import update_node_content
    from ....raw_clients.alfresco_core_client.core_client.types import UNSET, File
    
    # Get raw client
    raw_client = client.raw_client
    
    # Convert include options
    include_params = UNSET
    if include:
        include_params = include
    
    # Create File object for upload
    if isinstance(content, bytes):
        file_payload: BinaryIO = io.BytesIO(content)
    else:
        file_payload: BinaryIO = content  # type: ignore
    
    file_obj = File(
        payload=file_payload,
        file_name=filename or "content"
    )
    
    # Execute raw asyncio_detailed operation
    return await update_node_content.asyncio_detailed(
        client=raw_client,
        node_id=node_id,
        body=file_obj,
        include=include_params
    )
