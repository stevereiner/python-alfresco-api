# Pydantic Models Support Guide

The Alfresco Python API client provides comprehensive **Pydantic model support** for all API responses and requests, transforming raw JSON dictionaries into type-safe, validated, IDE-friendly Python objects.

## 🎯 What are Pydantic Models?

Pydantic models are Python classes that provide:
- **Type safety** with automatic validation
- **IDE autocomplete** and IntelliSense support
- **Automatic data conversion** (strings to dates, etc.)
- **Self-documenting code** with field descriptions
- **Early error detection** during development

## 🚀 Key Benefits

### ✅ Type Safety & IDE Support
- Full autocomplete for all API response fields
- Type hints show you what each field contains
- IDE warnings for typos and invalid field access
- IntelliSense documentation for every field

### ✅ Automatic Validation
- Invalid data rejected at creation time
- Automatic type conversion (strings to datetime objects)
- Field validation (required fields, formats, constraints)
- Catches errors in development, not production

### ✅ Clean, Maintainable Code
- No more manual dictionary navigation
- Strongly typed objects instead of raw dictionaries
- Self-documenting API interactions
- Reduced boilerplate and error-handling code

## 📚 Available Models

The client provides Pydantic models for all 7 Alfresco APIs:

| API | Model Location | Key Models |
|-----|---------------|------------|
| **Core API** | `enhanced_generated/models/alfresco_core_models.py` | `Node`, `NodeEntry`, `NodePaging`, `NodeBodyCreate` |
| **Search API** | `enhanced_generated/models/alfresco_search_models.py` | `SearchRequest`, `ResultSetPaging`, `ResultNode` |
| **Auth API** | `enhanced_generated/models/alfresco_auth_models.py` | `TicketBody`, `TicketEntry`, `ValidTicket` |
| **Discovery API** | `enhanced_generated/models/alfresco_discovery_models.py` | `DiscoveryEntry`, `RepositoryInfo` |
| **Workflow API** | `enhanced_generated/models/alfresco_workflow_models.py` | `ProcessDefinition`, `Task`, `Variable` |
| **Model API** | `enhanced_generated/models/alfresco_model_models.py` | `CustomModel`, `CustomType`, `CustomAspect` |
| **Search SQL API** | `enhanced_generated/models/alfresco_search_sql_models.py` | `SqlQuery`, `SqlResultSet` |

## 🏗️ Core API Models - Most Important

The **Core API models** are the most commonly used, as they handle nodes (files/folders), properties, and folder navigation:

```python
from enhanced_generated.models.alfresco_core_models import (
    Node,           # Files and folders
    NodeEntry,      # API response wrapper
    NodePaging,     # Paginated lists
    NodeBodyCreate, # Creating new nodes
    NodeBodyUpdate  # Updating existing nodes
)
```

### Essential Node Model
```python
class Node(BaseModel):
    id: str                                    # Node ID
    name: str                                  # File/folder name
    nodeType: str                             # cm:content, cm:folder, etc.
    isFile: bool                              # True if file
    isFolder: bool                            # True if folder
    createdAt: datetime                       # Creation date (auto-parsed!)
    modifiedAt: datetime                      # Last modified (auto-parsed!)
    properties: Optional[Dict[str, Any]]      # Custom properties
    aspectNames: Optional[List[str]]          # Applied aspects
    allowableOperations: Optional[List[str]]  # Permitted actions
```

## 💻 Usage Examples

### Basic Node Operations
```python
from enhanced_generated.AlfrescoClient import AlfrescoClient

client = AlfrescoClient(host="http://localhost:8080", username="admin", password="admin")

# Get folder children - returns Pydantic models automatically
response = client.core['nodes'].list_node_children(node_id='-root-')

# Type-safe access with IDE autocomplete
for child_entry in response.list.entries:
    node = child_entry.entry  # This is a Node Pydantic model
    
    if node.isFile:
        print(f"📄 File: {node.name}")
        print(f"   Size: {node.content.sizeInBytes if node.content else 'Unknown'}")
        print(f"   Modified: {node.modifiedAt.strftime('%Y-%m-%d')}")
    
    elif node.isFolder:
        print(f"📁 Folder: {node.name}")
    
    # Access custom properties safely
    if node.properties and 'cm:title' in node.properties:
        print(f"   Title: {node.properties['cm:title']}")
```

### Creating Nodes with Validation
```python
from enhanced_generated.models.alfresco_core_models import NodeBodyCreate

# Create with Pydantic validation
new_folder = NodeBodyCreate(
    name="Project Documents",
    nodeType="cm:folder",
    properties={
        "cm:title": "Project Documents Folder",
        "cm:description": "Contains all project files"
    },
    aspectNames=["cm:titled"]
)

# API call with validated data
response = client.core['nodes'].create_node(
    node_id='-root-',
    node_body_create=new_folder.model_dump()
)

# Response is also a Pydantic model
created_node = response.entry
print(f"Created: {created_node.name} with ID: {created_node.id}")
```

## 🔍 Detailed Examples

### 📚 Core API Examples
See **[examples/pydantic_models_examples.py](../examples/pydantic_models_examples.py)** for comprehensive examples covering:

- **Node Models** - Files, folders, and properties
- **Node Children** - Listing folder contents (most common operation)
- **Node Creation** - Making new files and folders with validation
- **Node Updates** - Modifying properties and metadata
- **Custom Properties** - Working with business metadata
- **Real API Usage** - Practical patterns for Core API operations

**🏃 Run the example:**
```bash
python examples/pydantic_models_examples.py
```

### 📊 Comparison: With vs Without Pydantic
See **[examples/without_pydantic_comparison.py](../examples/without_pydantic_comparison.py)** for a detailed comparison showing:

- **Raw dictionaries** vs **Pydantic models**
- **Manual type checking** vs **automatic validation**
- **Error-prone string access** vs **type-safe properties**
- **Complex date parsing** vs **automatic datetime conversion**
- **Verbose defensive code** vs **clean maintainable code**

**🏃 Run the comparison:**
```bash
python examples/without_pydantic_comparison.py
```

## 🔄 Without Pydantic Models

If you didn't have Pydantic models, you'd be working with raw dictionaries:

```python
# Raw API response - just dictionaries
response = {
    "list": {
        "entries": [
            {
                "entry": {
                    "id": "workspace://SpacesStore/12345",
                    "name": "document.pdf",
                    "isFile": True,
                    "createdAt": "2024-01-15T10:30:45.123Z",  # String, not datetime!
                    "properties": {"cm:title": "Some Document"}
                }
            }
        ]
    }
}

# Manual, error-prone access
node_name = response["list"]["entries"][0]["entry"]["name"]  # Typo-prone
is_file = response["list"]["entries"][0]["entry"].get("isFile")  # Defensive
created_str = response["list"]["entries"][0]["entry"]["createdAt"]  # Manual parsing needed!

# Manual date conversion required
from datetime import datetime
created_date = datetime.fromisoformat(created_str.replace('Z', '+00:00'))
```

### Problems Without Pydantic:
- ❌ **No type safety** - runtime errors only
- ❌ **No IDE autocomplete** - manual field names
- ❌ **No validation** - bad data accepted silently
- ❌ **Manual date parsing** - complex and error-prone
- ❌ **Verbose code** - lots of defensive programming

## 🛠️ Advanced Usage

### Custom Model Extensions
You can extend the generated Pydantic models for your specific needs:

```python
from enhanced_generated.models.alfresco_core_models import Node
from pydantic import computed_field

class EnhancedNode(Node):
    @computed_field
    @property
    def file_extension(self) -> str:
        """Get file extension from name."""
        if self.isFile and '.' in self.name:
            return self.name.split('.')[-1].lower()
        return ""
    
    @computed_field
    @property
    def is_document(self) -> bool:
        """Check if this is a document type."""
        doc_extensions = {'pdf', 'doc', 'docx', 'txt', 'rtf'}
        return self.file_extension in doc_extensions

# Usage
node_data = {...}  # From API response
enhanced = EnhancedNode(**node_data)
print(f"Is document: {enhanced.is_document}")
```

### Validation Customization
```python
from enhanced_generated.models.alfresco_core_models import NodeBodyCreate
from pydantic import field_validator

class StrictNodeCreate(NodeBodyCreate):
    @field_validator('name')
    @classmethod
    def validate_name(cls, v: str) -> str:
        if len(v) > 255:
            raise ValueError('Name too long')
        if any(char in v for char in ['<', '>', ':', '"', '|', '?', '*']):
            raise ValueError('Invalid characters in name')
        return v

# This will validate the name strictly
strict_node = StrictNodeCreate(
    name="Valid Name.txt",
    nodeType="cm:content"
)
```

## 🔗 Model Relationships

Pydantic models in the Alfresco client follow these patterns:

### Response Wrappers
- `NodeEntry` wraps `Node`
- `NodePaging` contains list of `NodeEntry`
- `NodeListResponse` contains `NodePaging`

### Request/Response Pairs
- `NodeBodyCreate` → creates → `NodeEntry` 
- `NodeBodyUpdate` → updates → `NodeEntry`
- `SearchRequest` → searches → `ResultSetPaging`

### Inheritance Hierarchies
```python
Node                    # Base node
├── NodeAssociation     # Node with association info
├── NodeChildAssociation # Node with child association info
└── DeletedNode         # Node in trash can
```

## 📖 Best Practices

### 1. Use Type Hints
```python
from enhanced_generated.models.alfresco_core_models import NodeListResponse

def process_folder(response: NodeListResponse) -> None:
    """Type hints provide IDE support and documentation."""
    for entry in response.list.entries:
        # IDE knows 'entry.entry' is a Node
        print(entry.entry.name)
```

### 2. Validate Early
```python
# Validate data as soon as you receive it
try:
    validated_response = NodeListResponse(**raw_api_data)
except ValidationError as e:
    logger.error(f"Invalid API response: {e}")
    return
```

### 3. Use Model Serialization
```python
# Convert back to dict/JSON for API calls
node_data = my_node.model_dump()
json_data = my_node.model_dump_json()

# Only include changed fields
updates = my_node.model_dump(exclude_unset=True)
```

### 4. Handle Optional Fields
```python
# Safe property access
if node.properties and 'cm:title' in node.properties:
    title = node.properties['cm:title']

# Or use get() for optional fields
title = (node.properties or {}).get('cm:title', 'No title')
```

## 🎯 Performance Considerations

### Validation Overhead
- **Minimal**: Usually <1ms per model creation
- **Benefits outweigh costs**: Catches errors early vs debugging production issues
- **Memory**: ~10-20% increase for type safety and validation

### When to Use Raw Dictionaries
Consider raw dictionaries only for:
- **High-frequency operations** where every microsecond matters
- **Simple data passing** without processing
- **Temporary prototyping** (but migrate to Pydantic for production)

### Optimization Tips
```python
# Disable validation for trusted data sources
trusted_node = Node.model_construct(**trusted_data)

# Partial loading for large responses
node_minimal = Node.model_validate(data, strict=False)
```

## 🆘 Troubleshooting

### Common Issues

#### Validation Errors
```python
# Problem: Field type mismatch
try:
    node = Node(**api_data)
except ValidationError as e:
    print(f"Validation failed: {e}")
    # Check the specific field causing issues
    for error in e.errors():
        print(f"Field: {error['loc']}, Error: {error['msg']}")
```

#### Missing Fields
```python
# Problem: Required field missing
# Solution: Check API response structure
print(f"Available fields: {list(api_data.keys())}")
```

#### Date Parsing Issues
```python
# Problem: Invalid date format
# Solution: Check timezone and format
from datetime import datetime
try:
    parsed_date = datetime.fromisoformat(date_string.replace('Z', '+00:00'))
except ValueError:
    # Handle invalid date format
    pass
```

## 🔮 Future Enhancements

The Pydantic model support could be enhanced:

- **Enhanced validation rules** based on Alfresco constraints
- **Custom field types** for Alfresco-specific data
- **Model inheritance** for specialized node types
- **Async model support** for high-performance operations
- **GraphQL-style field selection** for optimal data loading

## 📞 Support

For Pydantic model issues:

1. **Check the examples**: [pydantic_models_examples.py](../examples/pydantic_models_examples.py)
2. **Run the comparison**: [without_pydantic_comparison.py](../examples/without_pydantic_comparison.py)
3. **Review model definitions**: `enhanced_generated/models/`
4. **Check Pydantic docs**: https://docs.pydantic.dev/

---

**🎉 Pydantic models transform the Alfresco API experience from error-prone dictionary manipulation into type-safe, IDE-friendly, self-documenting code!** 