import requests
from typing import Optional, Dict, Any
import json

class AlfrescoBaseClient:
    def __init__(self, base_url: str, username: str, password: str, verify_ssl: bool = True):
        """
        Initialize the base Alfresco client.
        
        Args:
            base_url (str): The base URL of the Alfresco instance
            username (str): Alfresco username
            password (str): Alfresco password
            verify_ssl (bool): Whether to verify SSL certificates
        """
        self.base_url = base_url.rstrip('/')
        self.username = username
        self.password = password
        self.verify_ssl = verify_ssl
        self.session = requests.Session()
        self.session.verify = verify_ssl
        self.session.auth = (username, password)
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })

    def _make_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """
        Make an HTTP request to the Alfresco API.
        
        Args:
            method (str): HTTP method (GET, POST, PUT, DELETE, etc.)
            endpoint (str): API endpoint
            **kwargs: Additional arguments to pass to requests
            
        Returns:
            requests.Response: The response from the API
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, **kwargs)
        response.raise_for_status()
        return response

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> requests.Response:
        """Make a GET request"""
        return self._make_request('GET', endpoint, params=params)

    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> requests.Response:
        """Make a POST request"""
        return self._make_request('POST', endpoint, json=data)

    def put(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> requests.Response:
        """Make a PUT request"""
        return self._make_request('PUT', endpoint, json=data)

    def delete(self, endpoint: str) -> requests.Response:
        """Make a DELETE request"""
        return self._make_request('DELETE', endpoint) 