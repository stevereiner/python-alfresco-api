"""
Pydantic v2 Models for Alfresco APIs

Auto-generated models perfect for:
- LLM tool interfaces
- MCP server implementations  
- Type-safe API interactions
- Data validation and serialization
"""

# Import all models from individual API model files
try:
    from .alfresco_auth_models import *
except ImportError:
    pass

try:
    from .alfresco_core_models import *
except ImportError:
    pass

try:
    from .alfresco_discovery_models import *
except ImportError:
    pass

try:
    from .alfresco_search_models import *
except ImportError:
    pass

try:
    from .alfresco_workflow_models import *
except ImportError:
    pass

try:
    from .alfresco_model_models import *
except ImportError:
    pass

try:
    from .alfresco_search_sql_models import *
except ImportError:
    pass
