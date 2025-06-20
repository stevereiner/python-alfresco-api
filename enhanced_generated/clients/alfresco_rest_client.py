"""
High-Level Alfresco REST API Client

This client provides a stable, user-friendly interface to the Alfresco REST API
that doesn't depend on the specific structure of generated code from OpenAPI.
It uses direct HTTP requests following the OpenAPI specifications to ensure
compatibility even when the generated code changes.

Key Features:
- Stable API that won't break when YAML changes
- Support for both JSON and multipart/form-data uploads
- Proper error handling and response parsing
- Type hints for better IDE support
- Comprehensive logging

Author: AI Assistant
"""

import json
import requests
import logging
from typing import Dict, Any, Optional, Union, BinaryIO
from pathlib import Path


class AlfrescoRestClient:
    """
    High-level Alfresco REST API client that provides stable, easy-to-use methods
    for common Alfresco operations without depending on generated code structure.
    """
    
    def __init__(self, base_url: str, username: str, password: str, verify_ssl: bool = True):
        """
        Initialize the Alfresco REST client.
        
        Args:
            base_url: Base URL of Alfresco server (e.g., 'http://localhost:8080')
            username: Username for authentication
            password: Password for authentication
            verify_ssl: Whether to verify SSL certificates
        """
        self.base_url = base_url.rstrip('/')
        self.username = username
        self.password = password
        self.verify_ssl = verify_ssl
        self.api_base = f"{self.base_url}/alfresco/api/-default-/public/alfresco/versions/1"
        
        # Set up logging
        self.logger = logging.getLogger(__name__)
        
        # Test connection on initialization
        self._test_connection()
    
    def _test_connection(self) -> None:
        """Test connection to Alfresco server."""
        try:
            response = self.get_node('-root-')
            self.logger.info(f"Successfully connected to Alfresco: {response.get('name', 'Unknown')}")
        except Exception as e:
            raise ConnectionError(f"Failed to connect to Alfresco at {self.base_url}: {e}")
    
    def _make_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """
        Make HTTP request to Alfresco API.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint (relative to api_base)
            **kwargs: Additional arguments for requests
            
        Returns:
            requests.Response object
        """
        url = f"{self.api_base}/{endpoint.lstrip('/')}"
        
        # Set default auth if not provided
        if 'auth' not in kwargs:
            kwargs['auth'] = (self.username, self.password)
        
        # Set SSL verification
        kwargs['verify'] = self.verify_ssl
        
        # Make request
        response = requests.request(method, url, **kwargs)
        
        # Log request details
        self.logger.debug(f"{method} {url} -> {response.status_code}")
        
        return response
    
    def _handle_response(self, response: requests.Response) -> Dict[str, Any]:
        """
        Handle API response and extract data.
        
        Args:
            response: HTTP response object
            
        Returns:
            Parsed JSON response data
            
        Raises:
            Exception: If response indicates an error
        """
        if not response.ok:
            try:
                error_data = response.json()
                error_msg = error_data.get('error', {}).get('briefSummary', response.text)
            except:
                error_msg = response.text
            raise Exception(f"API Error {response.status_code}: {error_msg}")
        
        return response.json()
    
    # =====================================================================
    # NODE OPERATIONS
    # =====================================================================
    
    def get_node(self, node_id: str, include: Optional[str] = None) -> Dict[str, Any]:
        """
        Get information about a node.
        
        Args:
            node_id: Node ID or alias (e.g., '-root-', '-my-')
            include: Optional comma-separated list of fields to include
            
        Returns:
            Node information from the 'entry' field
        """
        params = {}
        if include:
            params['include'] = include
        
        response = self._make_request('GET', f'nodes/{node_id}', params=params)
        data = self._handle_response(response)
        return data['entry']
    
    def list_node_children(self, node_id: str, skip_count: int = 0, max_items: int = 100) -> Dict[str, Any]:
        """
        List children of a node.
        
        Args:
            node_id: Parent node ID
            skip_count: Number of items to skip
            max_items: Maximum number of items to return
            
        Returns:
            Children list with pagination info
        """
        params = {
            'skipCount': skip_count,
            'maxItems': max_items
        }
        
        response = self._make_request('GET', f'nodes/{node_id}/children', params=params)
        data = self._handle_response(response)
        return data['list']
    
    def create_folder(self, parent_node_id: str, name: str, title: Optional[str] = None, 
                     description: Optional[str] = None, properties: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Create a new folder using JSON API.
        
        Args:
            parent_node_id: ID of parent node
            name: Folder name
            title: Optional folder title (cm:title property)
            description: Optional folder description (cm:description property)
            properties: Optional additional properties
            
        Returns:
            Created folder information from 'entry' field
        """
        folder_data = {
            "name": name,
            "nodeType": "cm:folder"
        }
        
        # Add properties if provided
        if title or description or properties:
            folder_data["properties"] = {}
            if title:
                folder_data["properties"]["cm:title"] = title
            if description:
                folder_data["properties"]["cm:description"] = description
            if properties:
                folder_data["properties"].update(properties)
        
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        response = self._make_request('POST', f'nodes/{parent_node_id}/children', 
                                    json=folder_data, headers=headers)
        data = self._handle_response(response)
        return data['entry']
    
    def create_document(self, parent_node_id: str, name: str, title: Optional[str] = None,
                       description: Optional[str] = None, properties: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Create a new empty document using JSON API.
        
        Args:
            parent_node_id: ID of parent node
            name: Document name
            title: Optional document title (cm:title property)
            description: Optional document description (cm:description property)
            properties: Optional additional properties
            
        Returns:
            Created document information from 'entry' field
        """
        doc_data = {
            "name": name,
            "nodeType": "cm:content"
        }
        
        # Add properties if provided
        if title or description or properties:
            doc_data["properties"] = {}
            if title:
                doc_data["properties"]["cm:title"] = title
            if description:
                doc_data["properties"]["cm:description"] = description
            if properties:
                doc_data["properties"].update(properties)
        
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        response = self._make_request('POST', f'nodes/{parent_node_id}/children', 
                                    json=doc_data, headers=headers)
        data = self._handle_response(response)
        return data['entry']
    
    def upload_file(self, parent_node_id: str, file_path: Union[str, Path], 
                   name: Optional[str] = None, title: Optional[str] = None,
                   description: Optional[str] = None, overwrite: bool = False) -> Dict[str, Any]:
        """
        Upload a file with content using multipart/form-data API.
        
        Args:
            parent_node_id: ID of parent node
            file_path: Path to file to upload
            name: Optional custom name (defaults to filename)
            title: Optional file title (cm:title property)
            description: Optional file description (cm:description property)
            overwrite: Whether to overwrite existing file with same name
            
        Returns:
            Created file information from 'entry' field
        """
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Use custom name or filename
        file_name = name or file_path.name
        
        # Prepare multipart data
        with open(file_path, 'rb') as f:
            files = {
                'filedata': (file_name, f, 'application/octet-stream')
            }
            
            form_data = {
                'name': file_name,
            }
            
            if overwrite:
                form_data['overwrite'] = 'true'
            
            # Add properties if provided
            if title or description:
                properties = {}
                if title:
                    properties["cm:title"] = title
                if description:
                    properties["cm:description"] = description
                form_data['properties'] = json.dumps(properties)
            
            response = self._make_request('POST', f'nodes/{parent_node_id}/children', 
                                        files=files, data=form_data)
        
        data = self._handle_response(response)
        return data['entry']
    
    def upload_content_string(self, parent_node_id: str, content: str, filename: str,
                            title: Optional[str] = None, description: Optional[str] = None,
                            mime_type: str = 'text/plain') -> Dict[str, Any]:
        """
        Upload text content as a file using multipart/form-data API.
        
        Args:
            parent_node_id: ID of parent node
            content: Text content to upload
            filename: Name for the created file
            title: Optional file title (cm:title property)
            description: Optional file description (cm:description property)
            mime_type: MIME type for the content
            
        Returns:
            Created file information from 'entry' field
        """
        files = {
            'filedata': (filename, content.encode('utf-8'), mime_type)
        }
        
        form_data = {
            'name': filename,
        }
        
        # Add properties if provided
        if title or description:
            properties = {}
            if title:
                properties["cm:title"] = title
            if description:
                properties["cm:description"] = description
            form_data['properties'] = json.dumps(properties)
        
        response = self._make_request('POST', f'nodes/{parent_node_id}/children', 
                                    files=files, data=form_data)
        data = self._handle_response(response)
        return data['entry']
    
    def update_node_content(self, node_id: str, content: Union[str, bytes], 
                           content_type: str = 'text/plain') -> Dict[str, Any]:
        """
        Update the content of an existing document.
        
        Args:
            node_id: ID of the document node
            content: New content (string or bytes)
            content_type: MIME type of the content
            
        Returns:
            Updated node information from 'entry' field
        """
        if isinstance(content, str):
            content = content.encode('utf-8')
        
        headers = {
            'Content-Type': content_type,
            'Accept': 'application/json'
        }
        
        response = self._make_request('PUT', f'nodes/{node_id}/content', 
                                    data=content, headers=headers)
        data = self._handle_response(response)
        return data['entry']
    
    def get_node_content(self, node_id: str) -> bytes:
        """
        Download the content of a document.
        
        Args:
            node_id: ID of the document node
            
        Returns:
            Document content as bytes
        """
        response = self._make_request('GET', f'nodes/{node_id}/content')
        if not response.ok:
            raise Exception(f"Failed to download content: {response.status_code} {response.text}")
        return response.content
    
    def update_node_properties(self, node_id: str, properties: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update properties of a node.
        
        Args:
            node_id: ID of the node
            properties: Dictionary of properties to update
            
        Returns:
            Updated node information from 'entry' field
        """
        update_data = {
            "properties": properties
        }
        
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        response = self._make_request('PUT', f'nodes/{node_id}', 
                                    json=update_data, headers=headers)
        data = self._handle_response(response)
        return data['entry']
    
    def delete_node(self, node_id: str, permanent: bool = False) -> None:
        """
        Delete a node.
        
        Args:
            node_id: ID of the node to delete
            permanent: Whether to permanently delete (bypass trashcan)
        """
        params = {}
        if permanent:
            params['permanent'] = 'true'
        
        response = self._make_request('DELETE', f'nodes/{node_id}', params=params)
        if not response.ok:
            error_msg = f"Failed to delete node {node_id}: {response.status_code} {response.text}"
            raise Exception(error_msg)
    
    def copy_node(self, node_id: str, target_parent_id: str, name: Optional[str] = None) -> Dict[str, Any]:
        """
        Copy a node to another location.
        
        Args:
            node_id: ID of the node to copy
            target_parent_id: ID of the target parent node
            name: Optional new name for the copied node
            
        Returns:
            Copied node information from 'entry' field
        """
        copy_data = {
            "targetParentId": target_parent_id
        }
        
        if name:
            copy_data["name"] = name
        
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        response = self._make_request('POST', f'nodes/{node_id}/copy', 
                                    json=copy_data, headers=headers)
        data = self._handle_response(response)
        return data['entry']
    
    # =====================================================================
    # SEARCH OPERATIONS
    # =====================================================================
    
    def search_nodes(self, query: str, max_items: int = 25) -> Dict[str, Any]:
        """
        Search for nodes using Alfresco Full Text Search.
        
        Args:
            query: Search query string
            max_items: Maximum number of results to return
            
        Returns:
            Search results with pagination info
        """
        search_data = {
            "query": {
                "query": query
            },
            "paging": {
                "maxItems": max_items
            }
        }
        
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        response = self._make_request('POST', 'search/nodes', 
                                    json=search_data, headers=headers)
        data = self._handle_response(response)
        return data['list']
    
    # =====================================================================
    # UTILITY METHODS
    # =====================================================================
    
    def get_api_info(self) -> Dict[str, Any]:
        """
        Get information about the Alfresco API.
        
        Returns:
            API information
        """
        # This is a simple implementation - could be extended to get real discovery info
        return {
            'name': 'Alfresco Core API',
            'version': '1.0',
            'description': 'High-level Python client for Alfresco REST API',
            'base_url': self.base_url,
            'api_base': self.api_base
        }
    
    def __repr__(self) -> str:
        return f"AlfrescoRestClient(base_url='{self.base_url}', username='{self.username}')" 