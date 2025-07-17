# Pydantic ↔ Attrs Conversion Utilities Design

**Solving the V1.1 Architectural Gap: Seamless Model Conversion**

## 🎯 **Problem Statement**

Currently, python-alfresco-api V1.1 has:
- **Pydantic models** in hierarchical clients (CreateNodeRequest, UpdateNodeRequest) 
- **Attrs models** in raw clients (NodeBodyCreate, SearchRequest)
- **Manual conversion** with inconsistent patterns
- **Unused FieldMappingMixin** with sophisticated conversion capabilities
- **Search API gap** - users forced to use raw client attrs models

## 🏗️ **Proposed Solution: Three-Layer Approach**

### **Layer 1: Enhanced FieldMappingMixin (Foundation)**

Expand the existing `FieldMappingMixin` to handle all conversion patterns:

```python
from python_alfresco_api.clients.field_mapping import FieldMappingMixin

class CreateNodeRequest(BaseModel, FieldMappingMixin):
    name: str
    node_type: NodeType
    properties: Optional[Dict[str, Any]] = None
    
    def to_raw_client_body(self) -> NodeBodyCreate:
        """Convert to raw client attrs model."""
        return self.convert_to_attrs_model(NodeBodyCreate)
    
    @classmethod
    def from_raw_client_result(cls, attrs_result):
        """Create from raw client attrs result."""
        return cls.from_attrs_dict(attrs_result.to_dict())
```

### **Layer 2: Conversion Utilities (Convenience)**

Create helper functions for common patterns:

```python
# python_alfresco_api/clients/conversion_utils.py

from typing import TypeVar, Type, Any
from .field_mapping import FieldMappingMixin

T = TypeVar('T')
R = TypeVar('R')

def pydantic_to_attrs(pydantic_model: FieldMappingMixin, attrs_class: Type[R]) -> R:
    """Convert any Pydantic model to attrs model."""
    attrs_dict = pydantic_model.to_attrs_dict()
    return attrs_class.from_dict(attrs_dict)

def attrs_to_pydantic(attrs_model: Any, pydantic_class: Type[T]) -> T:
    """Convert any attrs model to Pydantic model."""
    return pydantic_class.from_attrs_dict(attrs_model.to_dict())

def create_converter_pair(pydantic_class: Type[T], attrs_class: Type[R]):
    """Create bidirectional converter functions."""
    def to_attrs(pydantic_instance: T) -> R:
        return pydantic_to_attrs(pydantic_instance, attrs_class)
    
    def from_attrs(attrs_instance: R) -> T:
        return attrs_to_pydantic(attrs_instance, pydantic_class)
    
    return to_attrs, from_attrs
```

### **Layer 3: High-Level Pydantic Wrappers (Developer Experience)**

Create Pydantic wrappers for complex operations like Search:

```python
# python_alfresco_api/clients/search/models.py

class AlfrescoSearchRequest(BaseModel, FieldMappingMixin):
    """High-level Pydantic wrapper for SearchRequest."""
    
    # Simple, intuitive fields
    query: str = Field(description="Search query string")
    language: Literal["afts", "cmis", "lucene"] = Field(default="afts")
    max_items: int = Field(default=100, ge=1, le=1000)
    skip_count: int = Field(default=0, ge=0)
    
    # Advanced options made optional and intuitive
    content_types: Optional[List[str]] = Field(
        default=None,
        description="Filter by content types",
        examples=[["cm:content", "cm:folder"]]
    )
    file_extensions: Optional[List[str]] = Field(
        default=None, 
        description="Filter by file extensions",
        examples=[["pdf", "docx", "xlsx"]]
    )
    date_range: Optional[Dict[str, datetime]] = Field(
        default=None,
        description="Date range filter",
        examples=[{"from": "2024-01-01", "to": "2024-12-31"}]
    )
    facets: Optional[List[str]] = Field(
        default=None,
        description="Enable faceting on fields", 
        examples=[["creator", "cm:modified"]]
    )
    highlight: bool = Field(default=False, description="Enable result highlighting")
    
    def to_raw_search_request(self) -> SearchRequest:
        """Convert to raw client SearchRequest (attrs model)."""
        # Build RequestQuery
        query_obj = RequestQuery(
            query=self._build_query_string(),
            language=RequestQueryLanguage(self.language),
            user_query=self.query
        )
        
        # Build SearchRequest with all advanced options
        search_request = SearchRequest(
            query=query_obj,
            paging=RequestPagination(
                max_items=self.max_items,
                skip_count=self.skip_count
            )
        )
        
        # Add advanced options if specified
        if self.facets:
            search_request.facet_fields = self._build_facet_fields()
        if self.highlight:
            search_request.highlight = self._build_highlight_config()
        if self.date_range:
            search_request.filter_queries = self._build_date_filters()
            
        return search_request
    
    def _build_query_string(self) -> str:
        """Build optimized query string based on filters."""
        query_parts = [self.query]
        
        if self.content_types:
            type_filter = " OR ".join(f"TYPE:{ct}" for ct in self.content_types)
            query_parts.append(f"({type_filter})")
            
        if self.file_extensions:
            ext_filter = " OR ".join(f"cm:name:*.{ext}" for ext in self.file_extensions)
            query_parts.append(f"({ext_filter})")
            
        return " AND ".join(query_parts)
```

## 🚀 **Implementation Plan**

### **Phase 1: Foundation Enhancement**
1. Expand `FieldMappingMixin` with automatic model conversion
2. Add type mapping registry for common Pydantic ↔ attrs pairs
3. Implement bidirectional conversion with field validation

### **Phase 2: Conversion Utilities**
1. Create `conversion_utils.py` with helper functions
2. Add converter decorators for automatic method wrapping
3. Implement conversion caching for performance

### **Phase 3: High-Level Wrappers**
1. Create `AlfrescoSearchRequest` as Pydantic wrapper
2. Add similar wrappers for other complex operations
3. Implement automatic fallback to raw clients when needed

### **Phase 4: Integration**
1. Update existing operations to use new conversion patterns
2. Add conversion examples to documentation
3. Provide migration guide for users

## 📚 **Usage Examples**

### **Simple Conversion (Layer 2)**
```python
# Convert CreateNodeRequest (Pydantic) → NodeBodyCreate (attrs)
from python_alfresco_api.clients.conversion_utils import pydantic_to_attrs

request = CreateNodeRequest(name="test.pdf", node_type=NodeType.CONTENT)
body = pydantic_to_attrs(request, NodeBodyCreate)
result = create_node.sync(client=raw_client, node_id="-my-", body=body)
```

### **High-Level Search (Layer 3)**
```python
# High-level Pydantic search → automatic conversion to raw SearchRequest
search = AlfrescoSearchRequest(
    query="annual report",
    content_types=["cm:content"],
    file_extensions=["pdf", "docx"],
    facets=["creator", "cm:modified"],
    highlight=True
)

# Automatic conversion to raw client model
raw_request = search.to_raw_search_request()
result = client.search.search(body=raw_request)
```

### **Bidirectional Conversion**
```python
# Create converter pair for reuse
to_attrs, from_attrs = create_converter_pair(CreateNodeRequest, NodeBodyCreate)

# Pydantic → attrs
request = CreateNodeRequest(name="test.pdf")
body = to_attrs(request)

# attrs → Pydantic (for results)
result_pydantic = from_attrs(attrs_result)
```

## ✅ **Benefits**

### **For Developers:**
- **Consistent patterns** - no more manual conversion guesswork
- **Type safety** - Pydantic validation throughout
- **Better DX** - intuitive high-level models for complex operations
- **Gradual adoption** - can use any layer as needed

### **For Architecture:**
- **Clean separation** - Pydantic for business logic, attrs for raw client
- **Performance** - conversion caching and lazy evaluation
- **Maintainability** - centralized conversion logic
- **Backwards compatibility** - existing code continues to work

### **For Search API:**
- **Eliminates the gap** - no more raw client attrs models required
- **Intuitive API** - simple fields for common operations
- **Full power** - access to all raw client features when needed
- **Type safety** - Pydantic validation for search parameters

## 🎯 **Success Criteria**

1. **Zero manual conversion** in new operations
2. **High-level Pydantic models** for all complex operations
3. **Seamless fallback** to raw clients when needed
4. **100% backwards compatibility** with existing code
5. **Comprehensive examples** and documentation

This design solves the architectural gap while providing multiple levels of abstraction for different use cases. 