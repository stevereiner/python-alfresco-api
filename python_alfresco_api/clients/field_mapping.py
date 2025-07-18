"""
Field Mapping Utilities for Automated attrs ↔ Pydantic Conversion

This module provides systematic utilities to handle the field mapping between:
- Raw attrs models (openapi-python-client generated) using snake_case
- Pydantic models (datamodel-code-generator style) using snake_case  
- JSON API responses using camelCase

Key Benefits for Automation:
1. Consistent field alias generation
2. Automatic camelCase ↔ snake_case conversion
3. Reusable patterns for all model generation
4. Type-safe field mapping helpers
"""

from typing import Dict, Any, Union, Optional, get_type_hints
from pydantic import BaseModel, Field
import re


def snake_to_camel(snake_str: str) -> str:
    """
    Convert snake_case to camelCase.
    
    Args:
        snake_str: String in snake_case format
        
    Returns:
        String in camelCase format
        
    Examples:
        >>> snake_to_camel("created_at")
        'createdAt'
        >>> snake_to_camel("is_file")
        'isFile'
        >>> snake_to_camel("allowable_operations")
        'allowableOperations'
    """
    components = snake_str.split('_')
    return components[0] + ''.join(word.capitalize() for word in components[1:])


def camel_to_snake(camel_str: str) -> str:
    """
    Convert camelCase to snake_case.
    
    Args:
        camel_str: String in camelCase format
        
    Returns:
        String in snake_case format
        
    Examples:
        >>> camel_to_snake("createdAt")
        'created_at'
        >>> camel_to_snake("isFile")
        'is_file'
        >>> camel_to_snake("allowableOperations")
        'allowable_operations'
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def create_field_with_alias(
    description: str,
    alias: Optional[str] = None,
    **field_kwargs
) -> Any:
    """
    Create a Pydantic Field with automatic camelCase alias.
    
    This function automatically generates camelCase aliases for field names,
    making it perfect for automated model generation.
    
    Args:
        description: Field description
        alias: Custom alias (if None, auto-generated from field name)
        **field_kwargs: Additional Field arguments
        
    Returns:
        Pydantic Field with alias
        
    Examples:
        >>> # In a model definition
        >>> created_at: datetime = create_field_with_alias(
        ...     "Creation timestamp",
        ...     examples=["2024-01-15T10:30:00.000Z"]
        ... )
        >>> # Automatically creates alias="createdAt"
    """
    return Field(description=description, alias=alias, **field_kwargs)


def auto_alias_field(field_name: str, description: str, **field_kwargs) -> Any:
    """
    Automatically create field with camelCase alias.
    
    Args:
        field_name: Snake case field name
        description: Field description
        **field_kwargs: Additional Field arguments
        
    Returns:
        Pydantic Field with auto-generated alias
        
    Examples:
        >>> created_at = auto_alias_field("created_at", "Creation timestamp")
        >>> # Creates Field with alias="createdAt"
    """
    alias = snake_to_camel(field_name)
    return Field(description=description, alias=alias, **field_kwargs)


class FieldMappingMixin(BaseModel):
    """
    Mixin to add field mapping capabilities to Pydantic models.
    
    Provides utilities for converting between different field naming conventions
    and handling attrs model integration.
    """
    
    @classmethod
    def from_attrs_dict(cls, attrs_dict: Dict[str, Any]) -> 'FieldMappingMixin':
        """
        Create instance from attrs model dictionary.
        
        Automatically converts camelCase keys to snake_case for Pydantic.
        
        Args:
            attrs_dict: Dictionary from attrs model.to_dict()
            
        Returns:
            Model instance with converted fields
        """
        # Convert camelCase keys to snake_case
        converted_dict = {}
        for key, value in attrs_dict.items():
            snake_key = camel_to_snake(key)
            converted_dict[snake_key] = value
        
        return cls(**converted_dict)
    
    def to_attrs_dict(self) -> Dict[str, Any]:
        """
        Convert to dictionary compatible with attrs models.
        
        Automatically converts snake_case keys to camelCase.
        
        Returns:
            Dictionary with camelCase keys for attrs compatibility
        """
        model_dict = self.model_dump()
        
        # Convert snake_case keys to camelCase
        converted_dict = {}
        for key, value in model_dict.items():
            camel_key = snake_to_camel(key)
            converted_dict[camel_key] = value
        
        return converted_dict
    
    def to_api_dict(self) -> Dict[str, Any]:
        """
        Convert to dictionary for API requests using field aliases.
        
        Uses the actual field aliases defined in the model for API compatibility.
        
        Returns:
            Dictionary with aliased keys for API requests
        """
        return self.model_dump(by_alias=True)


# Common field patterns for automated generation
COMMON_FIELD_PATTERNS = {
    # Timestamp fields
    "created_at": {
        "type": "datetime",
        "alias": "createdAt",
        "description": "Creation timestamp"
    },
    "modified_at": {
        "type": "datetime", 
        "alias": "modifiedAt",
        "description": "Last modification timestamp"
    },
    "updated_at": {
        "type": "datetime",
        "alias": "updatedAt", 
        "description": "Last update timestamp"
    },
    
    # Boolean fields
    "is_file": {
        "type": "bool",
        "alias": "isFile",
        "description": "True if this is a file"
    },
    "is_folder": {
        "type": "bool",
        "alias": "isFolder",
        "description": "True if this is a folder"
    },
    "is_favorite": {
        "type": "bool",
        "alias": "isFavorite",
        "description": "True if marked as favorite"
    },
    "is_locked": {
        "type": "bool",
        "alias": "isLocked",
        "description": "True if node is locked"
    },
    
    # ID fields
    "parent_id": {
        "type": "str",
        "alias": "parentId",
        "description": "Parent node identifier"
    },
    "node_id": {
        "type": "str",
        "alias": "nodeId", 
        "description": "Node identifier"
    },
    
    # Type fields
    "node_type": {
        "type": "str",
        "alias": "nodeType",
        "description": "Alfresco content model type"
    },
    "content_type": {
        "type": "str",
        "alias": "contentType",
        "description": "MIME content type"
    },
    
    # User fields
    "created_by_user": {
        "type": "UserInfo",
        "alias": "createdByUser",
        "description": "User who created this item"
    },
    "modified_by_user": {
        "type": "UserInfo", 
        "alias": "modifiedByUser",
        "description": "User who last modified this item"
    },
    
    # List/Array fields
    "allowable_operations": {
        "type": "List[str]",
        "alias": "allowableOperations",
        "description": "Operations allowed on this item"
    },
    "aspect_names": {
        "type": "List[str]",
        "alias": "aspectNames",
        "description": "Aspect names applied to this item"
    }
}


def generate_field_definition(field_name: str, field_info: Dict[str, Any]) -> str:
    """
    Generate Pydantic field definition code for automated model generation.
    
    Args:
        field_name: Snake case field name
        field_info: Field information from COMMON_FIELD_PATTERNS or custom
        
    Returns:
        Python code string for field definition
        
    Examples:
        >>> generate_field_definition("created_at", COMMON_FIELD_PATTERNS["created_at"])
        'created_at: Annotated[datetime, Field(alias="createdAt", description="Creation timestamp")]'
    """
    field_type = field_info.get("type", "Any")
    alias = field_info.get("alias", snake_to_camel(field_name))
    description = field_info.get("description", f"{field_name.replace('_', ' ').title()}")
    
    return f'{field_name}: Annotated[{field_type}, Field(alias="{alias}", description="{description}")]'


# Export utilities for automated model generation
__all__ = [
    "snake_to_camel",
    "camel_to_snake", 
    "create_field_with_alias",
    "auto_alias_field",
    "FieldMappingMixin",
    "COMMON_FIELD_PATTERNS",
    "generate_field_definition"
] 