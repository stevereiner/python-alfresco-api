"""
Fixes for Alfresco Search Client Generated Code Issues

This module provides fixes for regex and other syntax errors in the generated code.
"""

import re
import sys
from pathlib import Path

def fix_node_name_regex():
    """
    Fix the regex validation in the Node model that has syntax errors.
    
    The generated regex has improperly escaped backslashes that cause syntax errors.
    """
    # Correct regex pattern for node name validation
    # Original broken: r"^(?!(.*[\\"\*\\\\\>\<\?\/\:\|]+.*)|(.*[\.]?.*[\.]+$)|(.*[ ]+$))"
    # Fixed version:
    FIXED_NAME_REGEX = r'^(?!(.*[\\"\*<>?/:|]+.*)|(.*[\.]?.*[\.]+$)|(.*[ ]+$))'
    
    return FIXED_NAME_REGEX

def validate_node_name(value: str) -> str:
    """
    Enhanced node name validation with fixed regex.
    
    Args:
        value (str): The node name to validate
        
    Returns:
        str: The validated name
        
    Raises:
        ValueError: If the name contains invalid characters
    """
    # Use the fixed regex pattern
    pattern = fix_node_name_regex()
    
    if not re.match(pattern, value):
        raise ValueError(
            "Node name must not contain spaces or the following special characters: "
            "* \" < > \\ / ? : and |. The character . must not be used at the end of the name."
        )
    
    return value

def monkey_patch_search_client():
    """
    Apply monkey patches to fix issues in the generated search client.
    
    This function patches the problematic validation methods with working versions.
    """
    try:
        # Import the problematic module
        search_client_path = Path(__file__).parent.parent / "clients" / "alfresco-search"
        if str(search_client_path) not in sys.path:
            sys.path.insert(0, str(search_client_path))
        
        from alfresco_search_client.models.node import Node
        
        # Replace the broken validator with our fixed version
        def fixed_name_validate_regular_expression(cls, value):
            """Fixed version of the name validation"""
            return validate_node_name(value)
        
        # Monkey patch the validator
        Node.name_validate_regular_expression = classmethod(fixed_name_validate_regular_expression)
        
        print("✅ Applied search client regex fixes")
        return True
        
    except Exception as e:
        print(f"❌ Failed to apply search client fixes: {e}")
        return False

def apply_all_fixes():
    """Apply all available fixes for generated code issues."""
    fixes_applied = []
    
    # Apply search client fixes
    if monkey_patch_search_client():
        fixes_applied.append("search-regex")
    
    return fixes_applied 
