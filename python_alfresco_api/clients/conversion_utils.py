"""
Conversion Utilities - Proof of Concept

Seamless conversion between Pydantic models (V1.1 hierarchical) and attrs models (raw clients).
Solves the architectural gap without breaking existing code.
"""

from typing import TypeVar, Type, Any, Dict, Optional, get_type_hints
from pydantic import BaseModel
import inspect

T = TypeVar('T', bound=BaseModel)
R = TypeVar('R') 

def pydantic_to_attrs_dict(pydantic_model: BaseModel) -> Dict[str, Any]:
    """
    Convert Pydantic model to attrs-compatible dictionary.
    
    Handles field aliases and type conversions automatically.
    
    Args:
        pydantic_model: Any Pydantic model instance
        
    Returns:
        Dictionary compatible with attrs model.from_dict()
    """
    # Use model_dump with by_alias=True to get proper field names
    data = pydantic_model.model_dump(by_alias=True, exclude_none=True)
    
    # Handle special conversions
    converted_data = {}
    for key, value in data.items():
        # Convert enum values to strings
        if hasattr(value, 'value'):
            converted_data[key] = value.value
        else:
            converted_data[key] = value
            
    return converted_data


def attrs_to_pydantic(attrs_model: Any, pydantic_class: Type[T]) -> T:
    """
    Convert attrs model to Pydantic model.
    
    Args:
        attrs_model: Attrs model instance with .to_dict() method
        pydantic_class: Target Pydantic model class
        
    Returns:
        Pydantic model instance
    """
    if hasattr(attrs_model, 'to_dict'):
        attrs_dict = attrs_model.to_dict()
    else:
        # Fallback for objects that don't have to_dict
        attrs_dict = {k: v for k, v in attrs_model.__dict__.items() 
                     if not k.startswith('_')}
    
    return pydantic_class.model_validate(attrs_dict)


def create_converter_pair(pydantic_class: Type[T], attrs_class: Type[R]):
    """
    Create bidirectional converter functions for a Pydantic ↔ attrs model pair.
    
    Args:
        pydantic_class: Pydantic model class
        attrs_class: Attrs model class
        
    Returns:
        Tuple of (pydantic_to_attrs_fn, attrs_to_pydantic_fn)
    """
    def to_attrs(pydantic_instance: T) -> R:
        """Convert Pydantic instance to attrs instance."""
        attrs_dict = pydantic_to_attrs_dict(pydantic_instance)
        # Use getattr to safely access from_dict method
        if hasattr(attrs_class, 'from_dict'):
            return attrs_class.from_dict(attrs_dict)  # type: ignore
        else:
            raise AttributeError(f"Class {attrs_class} does not have from_dict method")
    
    def from_attrs(attrs_instance: R) -> T:
        """Convert attrs instance to Pydantic instance."""
        return attrs_to_pydantic(attrs_instance, pydantic_class)
    
    return to_attrs, from_attrs


# Registry for common conversion pairs (simplified for proof-of-concept)
CONVERSION_REGISTRY: Dict[str, Dict[str, str]] = {
    "nodes": {
        "create_pydantic": "python_alfresco_api.clients.core.nodes.models.CreateNodeRequest",
        "create_attrs": "python_alfresco_api.raw_clients.alfresco_core_client.core_client.models.NodeBodyCreate",
        "update_pydantic": "python_alfresco_api.clients.core.nodes.models.UpdateNodeRequest",
        "update_attrs": "python_alfresco_api.raw_clients.alfresco_core_client.core_client.models.NodeBodyUpdate",
    }
}


def get_converter_for_operation(operation_name: str):
    """
    Get pre-configured converter for common operations.
    
    Args:
        operation_name: Name of operation (e.g., "create_node", "update_node")
        
    Returns:
        Converter function or None if not found
    """
    # This could be expanded to include many common conversions
    converters = {
        "create_node": lambda req: pydantic_to_attrs_dict(req),
        "update_node": lambda req: pydantic_to_attrs_dict(req),
    }
    
    return converters.get(operation_name)


# Example usage and proof-of-concept integration
def enhanced_create_node_example():
    """
    Example of how conversion utilities could simplify existing operations.
    
    This shows how to eliminate manual conversion in create_node operations.
    """
    try:
        from python_alfresco_api.clients.core.nodes.models import CreateNodeRequest, NodeType
        
        # Instead of current manual conversion:
        # body = NodeBodyCreate(
        #     name=request.name,
        #     node_type=getattr(request.node_type, 'value', str(request.node_type)),
        #     aspect_names=aspects,
        #     properties=properties
        # )
        
        # Use automatic conversion:
        request = CreateNodeRequest(
            name="test.pdf",
            node_type=NodeType.CONTENT,
            properties={"cm:title": "Test Document"},
            auto_rename=True,
            aspects=None,
            versioning_enabled=None,
            major_version=None
        )
        
        # One-line conversion
        attrs_dict = pydantic_to_attrs_dict(request)
        
        # Could be used with any attrs model that accepts from_dict()
        print("Converted attrs dict:", attrs_dict)
        return attrs_dict
    except ImportError:
        # Handle case where modules aren't available during testing
        print("CreateNodeRequest not available (normal during testing)")
        return {"name": "test.pdf", "nodeType": "cm:content"}


def enhanced_search_example():
    """
    Example of how high-level Pydantic models could wrap complex raw client models.
    
    This demonstrates the potential for AlfrescoSearchRequest.
    """
    # Instead of users having to do:
    # from python_alfresco_api.raw_clients.alfresco_search_client.search_client.models import SearchRequest, RequestQuery
    # search_request = SearchRequest(query=RequestQuery(query="annual report"))
    
    # They could do:
    search_params = {
        "query": "annual report",
        "content_types": ["cm:content"],
        "file_extensions": ["pdf"],
        "max_items": 50
    }
    
    # This would automatically build the complex SearchRequest
    # (Implementation would be in AlfrescoSearchRequest.to_raw_search_request())
    print("High-level search params:", search_params)
    return search_params


if __name__ == "__main__":
    """Test the conversion utilities."""
    print("[TESTING] Testing Conversion Utilities")
    
    # Test 1: Enhanced create node
    print("\n1. Enhanced create node conversion:")
    enhanced_create_node_example()
    
    # Test 2: Search example
    print("\n2. Enhanced search example:")
    enhanced_search_example()
    
    print("\n[SUCCESS] Conversion utilities proof-of-concept complete!") 