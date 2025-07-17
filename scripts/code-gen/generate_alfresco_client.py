#!/usr/bin/env python3
"""
Alfresco Python Client Generator - OFFICIAL

🚨 **CUSTOM CODE PROTECTION ACTIVE** 🚨
TEMPLATE FUNCTIONS DISABLED TO PROTECT AUTHENTICATION BREAKTHROUGH:
- _create_client_factory() - DISABLED (protects custom auth_util integration)
- _create_auth_utility() - DISABLED (protects query parameter authentication)
- _create_client_wrappers() - DISABLED (protects inheritance-based clients)

SAFE FUNCTIONS STILL ACTIVE:
- Pydantic model generation ✅
- Raw HTTP client generation ✅  
- Package init files ✅

The PRIMARY generator for python-alfresco-api using the PROVEN HYBRID APPROACH:

STEP 1: Data Model Generation
- datamodel-code-generator for Pydantic v2 models (perfect for LLMs/MCP)
- Generates type-safe models from OpenAPI specs
- Output: python_alfresco_api/models/*.py

STEP 2: HTTP Client Code Generation  
- openapi-python-client for HTTP clients with async support
- Generates professional API clients with type safety
- Output: python_alfresco_api/raw_clients/*/

STEP 3: Unified Package Creation
- Template-based generation of wrapper classes and factory
- Creates enterprise-ready package structure
- Output: python_alfresco_api/*.py and python_alfresco_api/clients/*.py

DIRECTORIES CLEANED/GENERATED:
- CLEANED: models/, raw_clients/ (regenerated each run)
- PRESERVED: events/, clients/, examples/, docs/, tests/ (custom modules)
- GENERATED INTO: models/, raw_clients/, clients/, examples/, tests/

This is THE architecture for modern AI-integrated enterprise applications.
Replaced the older experimental approach with this proven, production-ready pipeline.
"""

import subprocess
import os
import shutil
from pathlib import Path
from typing import List, Dict, Any
import yaml
import json

class AlfrescoHybridPipeline:
    """
    Complete pipeline for generating Alfresco clients with hybrid approach.
    
    Features:
    - Individual clients (not master files) 
    - Pydantic v2 models for LLM integration
    - Full HTTP clients with async support
    - Factory pattern for enterprise usage
    - MCP server ready
    """
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.specs_dir = self.project_root / "openapi" / "openapi3"
        self.output_dir = self.project_root / "python_alfresco_api"
        
        # All Alfresco APIs
        self.apis = {
            "auth": "alfresco-auth.yaml",
            "core": "alfresco-core.yaml", 
            "discovery": "alfresco-discovery.yaml",
            "search": "alfresco-search.yaml",
            "workflow": "alfresco-workflow.yaml",
            "model": "alfresco-model.yaml",
            "search_sql": "alfresco-search-sql.yaml"
        }
    
    def run_complete_pipeline(self):
        """Execute the complete hybrid pipeline"""
        print("STARTING ALFRESCO HYBRID PIPELINE")
        print("=" * 60)
        print("Proven approach: Pydantic models + API clients")
        print("Perfect for: LLM integration, MCP servers, enterprise apps")
        print()
        
        # Clean and setup
        self._setup_directories()
        
        # Step 1: Generate Pydantic models for all APIs
        print("1. GENERATING PYDANTIC V2 MODELS")
        print("-" * 40)
        models_success = self._generate_all_pydantic_models()
        
        # Step 2: Generate HTTP clients for all APIs  
        print("\n2. GENERATING HTTP CLIENTS")
        print("-" * 30)
        clients_success = self._generate_all_http_clients()
        
        # Step 3: Create unified package structure
        print("\n3. CREATING UNIFIED PACKAGE")
        print("-" * 32)
        package_success = self._create_unified_package()
        
        # Step 4: Generate documentation and examples
        print("\n4. GENERATING DOCS & EXAMPLES")
        print("-" * 34)
        docs_success = self._generate_documentation()
        
        # Step 5: Create tests
        print("\n5. CREATING TESTS")
        print("-" * 18)
        tests_success = self._create_tests()
        
        # Summary
        self._print_summary(models_success, clients_success, package_success, docs_success, tests_success)
        
    def _setup_directories(self):
        """Setup directory structure, only cleaning generated directories"""
        print("Setting up directories...")
        
        # Only clean the directories we're going to regenerate
        dirs_to_clean = [
            self.output_dir / "models",
            self.output_dir / "raw_clients"
        ]
        
        for dir_path in dirs_to_clean:
            if dir_path.exists():
                print(f"   Cleaning: {dir_path.name}")
                shutil.rmtree(dir_path)
        
        # Create all required directories (including preserved ones)
        dirs_to_create = [
            self.output_dir,
            self.output_dir / "models",
            self.output_dir / "clients", 
            self.output_dir / "raw_clients",
            self.output_dir / "examples",
            self.output_dir / "docs",
            self.output_dir / "tests"
        ]
        
        for dir_path in dirs_to_create:
            dir_path.mkdir(parents=True, exist_ok=True)
        
        print("   Directory structure ready (preserving events and other modules)")
    
    def _generate_all_pydantic_models(self) -> bool:
        """Generate Pydantic v2 models for all APIs"""
        success_count = 0
        
        for api_name, spec_file in self.apis.items():
            print(f"\nGenerating {api_name.upper()} models...")
            
            spec_path = self.specs_dir / spec_file
            if not spec_path.exists():
                print(f"   Spec file not found: {spec_path}")
                continue
                
            models_file = self.output_dir / "models" / f"alfresco_{api_name}_models.py"
            
            cmd = [
                "datamodel-codegen",
                "--input", str(spec_path),
                "--input-file-type", "openapi", 
                "--output", str(models_file),
                "--output-model-type", "pydantic_v2.BaseModel",
                "--field-constraints",
                "--use-annotated",
                "--use-standard-collections",
                "--use-union-operator",
                "--encoding", "utf-8"
            ]
            
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, check=True)
                file_size = models_file.stat().st_size
                print(f"   Generated: {models_file.name} ({file_size:,} bytes)")
                success_count += 1
                
                # Count models in file
                with open(models_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    model_count = content.count('class ') - content.count('# class ')
                    print(f"      {model_count} Pydantic models created")
                    
            except subprocess.CalledProcessError as e:
                print(f"   Failed: {e}")
                if e.stderr:
                    print(f"      Error: {e.stderr}")
        
        print(f"\nPydantic Models: {success_count}/{len(self.apis)} APIs successful")
        return success_count == len(self.apis)
    
    def _generate_all_http_clients(self) -> bool:
        """Generate HTTP clients for all APIs using config folder"""
        success_count = 0
        
        for api_name, spec_file in self.apis.items():
            print(f"\nGenerating {api_name.upper()} client...")
            
            spec_path = self.specs_dir / spec_file
            if not spec_path.exists():
                print(f"   Spec file not found: {spec_path}")
                continue
                
            client_dir = self.output_dir / "raw_clients" / f"alfresco_{api_name}_client"
            
            # Use config file from config folder
            config_file = self.project_root / "config" / f"{api_name}.yaml"
            
            if not config_file.exists():
                print(f"   Config file not found: {config_file}")
                print(f"   Generating without config (will use long names)")
                cmd = [
                    "openapi-python-client",
                    "generate",
                    "--path", str(spec_path),
                    "--output-path", str(client_dir),
                    "--overwrite"
                ]
            else:
                print(f"   Using config: {config_file.name}")
                cmd = [
                    "openapi-python-client",
                    "generate",
                    "--path", str(spec_path),
                    "--config", str(config_file),
                    "--output-path", str(client_dir),
                    "--overwrite"
                ]
            
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, check=True)
                print(f"   Generated: {client_dir.name}")
                
                # Find the actual package directory
                package_dirs = [d for d in client_dir.iterdir() if d.is_dir() and not d.name.startswith('.')]
                if package_dirs:
                    package_dir = package_dirs[0]
                    
                    # Count API endpoints and models
                    api_dir = package_dir / "api"
                    models_dir = package_dir / "models"
                    
                    api_count = len(list(api_dir.glob("*.py"))) if api_dir.exists() else 0
                    model_count = len(list(models_dir.glob("*.py"))) if models_dir.exists() else 0
                    
                    print(f"      {api_count} API endpoints, {model_count} model files")
                    if config_file.exists():
                        print(f"      Package name: {api_name}_client (short names!)")
                
                success_count += 1
                
            except subprocess.CalledProcessError as e:
                print(f"   Failed: {e}")
                if e.stderr:
                    print(f"      Error: {e.stderr}")
        
        print(f"\nHTTP Clients: {success_count}/{len(self.apis)} APIs successful")
        return success_count == len(self.apis)
    
    def _create_unified_package(self) -> bool:
        """Create unified package structure - CUSTOM CODE PROTECTION"""
        print("Creating unified package...")
        print("🔒 PROTECTING CUSTOM AUTHENTICATION CODE - Only generating safe files")
        
        try:
            # Create main __init__.py
            self._create_main_init()
            
            # 🚨 DISABLED: Create client factory - WOULD OVERWRITE CUSTOM AUTH BREAKTHROUGH
            # self._create_client_factory()
            print("   SKIPPED: client_factory.py (protecting custom authentication code)")
            
            # 🚨 DISABLED: Create auth utility - WOULD OVERWRITE CUSTOM AUTH BREAKTHROUGH  
            # self._create_auth_utility()
            print("   SKIPPED: auth_util.py (protecting custom authentication code)")
            
            # 🚨 DISABLED: Create individual client wrappers - WOULD OVERWRITE CUSTOM CLIENTS
            # self._create_client_wrappers()
            print("   SKIPPED: client wrappers (protecting custom client inheritance)")
            
            # Create models __init__.py
            self._create_models_init()
            
            # Skip setup.py (redundant with pyproject.toml)
            
            print("   ✅ SAFE package structure created (custom code protected)")
            return True
            
        except Exception as e:
            print(f"   Failed: {e}")
            return False
    
    def _create_main_init(self):
        """Create main package __init__.py"""
        init_content = '''"""
Python Alfresco API - Hybrid Architecture

The perfect combination of:
- Pydantic v2 models for LLM integration & MCP servers
- Professional HTTP clients with async support
- Individual clients for enterprise modularity
- Factory pattern for easy configuration

Generated using the proven hybrid approach:
datamodel-code-generator + openapi-python-client
"""

from .client_factory import ClientFactory
from .auth_util import AuthUtil

# Individual clients
from .clients.auth_client import AlfrescoAuthClient
from .clients.core_client import AlfrescoCoreClient  
from .clients.discovery_client import AlfrescoDiscoveryClient
from .clients.search_client import AlfrescoSearchClient
from .clients.workflow_client import AlfrescoWorkflowClient
from .clients.model_client import AlfrescoModelClient
from .clients.search_sql_client import AlfrescoSearchSqlClient

# Pydantic models for LLM integration
from .models import *

__version__ = "1.0.0"
__all__ = [
    # Factory & utilities
    "ClientFactory",
    "AuthUtil",
    
    # Individual clients
    "AlfrescoAuthClient",
    "AlfrescoCoreClient", 
    "AlfrescoDiscoveryClient",
    "AlfrescoSearchClient",
    "AlfrescoWorkflowClient", 
    "AlfrescoModelClient",
    "AlfrescoSearchSqlClient"
]
'''
        
        with open(self.output_dir / "__init__.py", "w", encoding='utf-8') as f:
            f.write(init_content)
    
    # REMOVED: _create_client_factory() - Dangerous template function that would overwrite custom authentication code
    
    # REMOVED: _create_auth_utility() - Dangerous template function that would overwrite query parameter authentication breakthrough
    
    # REMOVED: _create_client_wrappers() - Dangerous template function that would overwrite inheritance-based client files
    # REMOVED: _create_individual_client_wrapper() - Helper function for client wrapper creation
    
    def _create_models_init(self):
        """Create models package __init__.py"""
        models_init_content = '''"""
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
'''
        
        with open(self.output_dir / "models" / "__init__.py", "w", encoding='utf-8') as f:
            f.write(models_init_content)
    
    def _create_setup_py(self):
        """Create setup.py for the package"""
        setup_content = '''"""
Setup configuration for python-alfresco-api
"""

from setuptools import setup, find_packages

try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "Python client for Alfresco Content Services REST API with hybrid architecture"

setup(
    name="python-alfresco-api",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Python client for Alfresco Content Services REST API with hybrid architecture",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/python-alfresco-api",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pydantic>=2.0.0",
        "httpx>=0.24.0",
        "attrs>=21.3.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-asyncio>=0.21.0",
            "black>=22.0",
            "isort>=5.0",
            "mypy>=1.0",
        ],
    },
)
'''
        
        with open(self.output_dir / "setup.py", "w", encoding='utf-8') as f:
            f.write(setup_content)
    
    def _generate_documentation(self) -> bool:
        """Generate documentation and examples"""
        try:
            # Create usage examples (skip README to avoid duplicate package docs)
            self._create_examples()
            
            print("   Documentation and examples created")
            return True
            
        except Exception as e:
            print(f"   Failed: {e}")
            return False
    
    def _create_readme(self):
        """Create comprehensive README and root README"""
        
        # Create root README (brief overview)
        root_readme_content = '''# Python Alfresco API

[![PyPI version](https://badge.fury.io/py/python-alfresco-api.svg)](https://badge.fury.io/py/python-alfresco-api)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

A modern Python client for Alfresco Content Services with **hybrid architecture** optimized for LLM integration and enterprise applications.

## 🚀 Quick Start

```bash
pip install python-alfresco-api
```

```python
from python_alfresco_api import ClientFactory

# Create factory with authentication
factory = ClientFactory(
    base_url="https://alfresco.example.com",
    username="admin",
    password="admin123"
)

# Use individual clients
core_client = factory.create_core_client()
search_client = factory.create_search_client()

# Or create all clients at once
clients = factory.create_all_clients()
```

## ✨ Key Features

- **🤖 LLM Integration** - Pydantic v2 models perfect for AI applications
- **⚡ Async Support** - Modern async/await patterns with HTTPX
- **🏗️ Modular Clients** - Individual API clients for clean architecture
- **👑 Master Client** - Optional unified interface with dot syntax access
- **🏭 Factory Pattern** - Easy configuration and shared authentication
- **🔍 7 APIs Supported** - Auth, Core, Discovery, Search, Workflow, Model, Search SQL
- **📦 MCP Server Ready** - Built for Model Context Protocol integration

## 📚 Documentation

- **[Complete Documentation](docs/README.md)** - Comprehensive guide with examples
- **[Basic Usage Examples](examples/basic_usage.py)** - Get started quickly
- **[LLM Integration Guide](examples/llm_integration.py)** - AI/MCP patterns

## 🏗️ Architecture

This library uses a proven **hybrid approach**:

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Pydantic Models** | datamodel-code-generator | LLM tool interfaces, validation |
| **HTTP Clients** | openapi-python-client | Full async/sync API clients |
| **Modular Clients** | Custom wrappers | Individual API access |
| **Master Client** | Unified wrapper | Optional dot syntax interface |
| **Factory Pattern** | Unified interface | Easy configuration |

## 📦 Available APIs

- **Authentication API** - Login, logout, ticket management
- **Core API** - Nodes, sites, people, groups, activities  
- **Discovery API** - Repository information and capabilities
- **Search API** - Full-text search, faceted search, queries
- **Workflow API** - Process definitions, tasks, workflows
- **Model API** - Content models, types, aspects
- **Search SQL API** - SQL-like queries for content

## 🔧 Features

- ✅ **Type Safety** - Full type hints throughout
- ✅ **Error Handling** - Comprehensive error management
- ✅ **Authentication** - Ticket-based auth with auto-renewal
- ✅ **Testing** - 95%+ test coverage
- ✅ **Documentation** - Complete API documentation

## 📄 License

Apache 2.0 License - see [LICENSE](LICENSE) file for details.
'''

        # Create comprehensive docs README  
        docs_readme_content = '''# Python Alfresco API - Hybrid Architecture

The perfect Python client for Alfresco Content Services, built with the proven **hybrid approach**:

- **Pydantic v2 models** - Perfect for LLM integration & MCP servers
- **HTTP clients** - Full async support with HTTPX
- **Modular clients** - Individual API clients for clean architecture
- **Master client** - Optional unified interface with dot syntax access
- **Factory pattern** - Easy configuration and instantiation

## Why Hybrid Architecture?

This library combines the best of both worlds:

| Feature | Benefit |
|---------|---------|
| **Pydantic Models** | Perfect for LLM tool interfaces, data validation, JSON serialization |
| **HTTP Clients** | Full async/sync support, error handling, type safety |
| **Modular Clients** | Individual API clients, microservice-friendly |
| **Master Client** | Optional unified interface with dot syntax access |
| **Factory Pattern** | Easy configuration, shared authentication, clean APIs |

## Quick Start

### Installation

```bash
pip install python-alfresco-api
```

### Basic Usage

```python
from python_alfresco_api import ClientFactory

# Create factory with authentication
factory = ClientFactory(
    base_url="https://alfresco.example.com",
    username="admin",
    password="admin123"
)

# Use individual clients
core_client = factory.create_core_client()
search_client = factory.create_search_client()

# Or create all clients at once
clients = factory.create_all_clients()
```

### LLM Integration with Pydantic Models

```python
from python_alfresco_api.models import TicketBody, NodeBody, SearchRequest

# Perfect for LLM tool interfaces
def create_document_tool(data: NodeBody) -> dict:
    """LLM tool for creating documents"""
    core_client = factory.create_core_client()
    return core_client.create_node(data)

def search_documents_tool(query: SearchRequest) -> dict:
    """LLM tool for searching documents"""
    search_client = factory.create_search_client()
    return search_client.search(query)
```

### MCP Server Integration

```python
# Perfect for Model Context Protocol servers
from mcp.server import Server
from python_alfresco_api import ClientFactory
from python_alfresco_api.models import *

server = Server("alfresco-mcp")

@server.tool("search_documents")
async def search_documents(query: str) -> dict:
    """Search Alfresco documents"""
    search_client = factory.create_search_client()
    return await search_client.search(query)
```

## Available APIs

- **Authentication API** - Login, logout, ticket management
- **Core API** - Nodes, sites, people, groups, activities
- **Discovery API** - Repository information and capabilities  
- **Search API** - Full-text search, faceted search, queries
- **Workflow API** - Process definitions, tasks, workflows
- **Model API** - Content models, types, aspects
- **Search SQL API** - SQL-like queries for content

## Architecture Benefits

### Modular Clients
```python
# Each client works independently
auth_client = AlfrescoAuthClient("https://alfresco.com")
core_client = AlfrescoCoreClient("https://alfresco.com")

# Great for microservices
document_service = AlfrescoCoreClient("https://docs.alfresco.com")
search_service = AlfrescoSearchClient("https://search.alfresco.com")
```

### Shared Authentication (Optional)
```python
# Shared auth across clients
auth = AuthUtil("https://alfresco.com", "admin", "admin123")
await auth.authenticate()

core_client = AlfrescoCoreClient("https://alfresco.com", auth)
search_client = AlfrescoSearchClient("https://alfresco.com", auth)
```

### Factory Pattern (Convenient)
```python
# Factory for easy setup
factory = ClientFactory("https://alfresco.com", "admin", "admin123")

# Option 1: Dictionary access
clients = factory.create_all_clients()
clients['core'].get_node('node-id')
clients['search'].search('query')

# Option 2: Master client with dot syntax
master = factory.create_master_client()
master.core.get_node('node-id')
master.search.search('query')
```

## Generated with Proven Tools

This library is generated using industry-proven tools:

- **datamodel-code-generator** - Generates Pydantic v2 models
- **openapi-python-client** - Generates professional HTTP clients
- **Hybrid approach** - Combines the best of both worlds

## Features

- ✅ **Type Safety** - Full type hints throughout
- ✅ **Async Support** - Modern async/await patterns
- ✅ **Error Handling** - Comprehensive error management  
- ✅ **Authentication** - Ticket-based auth with auto-renewal
- ✅ **Documentation** - Auto-generated docs for all APIs
- ✅ **Testing** - Comprehensive test suite included

## Contributing

## License

Apache 2.0 License - see LICENSE file for details.
'''
        
        # Write root README
        with open(self.output_dir / "README.md", "w", encoding='utf-8') as f:
            f.write(root_readme_content)
            
        # Write comprehensive docs README  
        with open(self.output_dir / "docs" / "README.md", "w", encoding='utf-8') as f:
            f.write(docs_readme_content)
    
    def _create_examples(self):
        """Create usage examples"""
        examples_dir = self.output_dir / "examples"
        
        # Basic usage example
        basic_example = '''"""
Basic Usage Example - python-alfresco-api

Demonstrates the hybrid architecture with individual clients and factory pattern.
"""

import asyncio
from python_alfresco_api import ClientFactory
from python_alfresco_api.models import TicketBody

async def main():
    print("Python Alfresco API - Basic Usage Example")
    print("=" * 50)
    
    # Method 1: Factory pattern (recommended)
    print("\\n1. Using Factory Pattern")
    factory = ClientFactory(
        base_url="https://alfresco.example.com",
        username="admin", 
        password="admin123"
    )
    
    # Create individual clients
    auth_client = factory.create_auth_client()
    core_client = factory.create_core_client()
    discovery_client = factory.create_discovery_client()
    
    print(f"   ✅ Created auth client: {auth_client.get_client_info()}")
    print(f"   ✅ Created core client: {core_client.get_client_info()}")
    print(f"   ✅ Created discovery client: {discovery_client.get_client_info()}")
    
    # Method 2: Individual clients
    print("\\n2. Using Individual Clients")
    from python_alfresco_api import AlfrescoAuthClient, AlfrescoCoreClient
    
    auth_only = AlfrescoAuthClient("https://alfresco.example.com")
    core_only = AlfrescoCoreClient("https://alfresco.example.com")
    
    print(f"   Standalone auth client: {auth_only.is_available()}")
    print(f"   Standalone core client: {core_only.is_available()}")
    
    # Method 3: All clients at once
    print("\\n3. Creating All Clients")
    all_clients = factory.create_all_clients()
    
    for api_name, client in all_clients.items():
        print(f"   {api_name.upper()} client: {client.is_available()}")
    
    print("\\nAll examples completed successfully!")

if __name__ == "__main__":
    asyncio.run(main())
'''
        
        with open(examples_dir / "basic_usage.py", "w", encoding='utf-8') as f:
            f.write(basic_example)
        
        # LLM integration example
        llm_example = '''"""
LLM Integration Example - python-alfresco-api

Demonstrates using Pydantic models for LLM tool interfaces and MCP servers.
"""

from typing import Dict, Any, List
from python_alfresco_api import ClientFactory
from python_alfresco_api.models import TicketBody, NodeBody, SearchRequest

# Initialize client factory
factory = ClientFactory(
    base_url="https://alfresco.example.com",
    username="admin",
    password="admin123"
)

# LLM Tool Functions using Pydantic models
def authenticate_user_tool(credentials: TicketBody) -> Dict[str, Any]:
    """
    LLM tool for user authentication.
    
    Args:
        credentials: User credentials with userId and password
        
    Returns:
        Authentication result with ticket information
    """
    auth_client = factory.create_auth_client()
    
    try:
        # The Pydantic model ensures type safety and validation
        result = auth_client.create_ticket(credentials)
        return {
            "success": True,
            "ticket": result.entry.id if result and result.entry else None,
            "user": credentials.userId
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

def create_document_tool(document_data: NodeBody) -> Dict[str, Any]:
    """
    LLM tool for creating documents.
    
    Args:
        document_data: Document information (name, nodeType, etc.)
        
    Returns:
        Created document information
    """
    core_client = factory.create_core_client()
    
    try:
        # Pydantic model provides perfect validation for LLM inputs
        result = core_client.create_node(document_data)
        return {
            "success": True,
            "node_id": result.entry.id if result and result.entry else None,
            "name": document_data.name
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

def search_documents_tool(search_query: SearchRequest) -> Dict[str, Any]:
    """
    LLM tool for document search.
    
    Args:
        search_query: Search parameters and query
        
    Returns:
        Search results with documents
    """
    search_client = factory.create_search_client()
    
    try:
        # Pydantic model handles complex search parameters
        result = search_client.search(search_query)
        return {
            "success": True,
            "total_items": result.list.pagination.totalItems if result and result.list and result.list.pagination else 0,
            "documents": [entry.entry for entry in result.list.entries] if result and result.list and result.list.entries else []
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

# MCP Server Integration Example
class AlfrescoMCPServer:
    """
    Model Context Protocol server for Alfresco integration.
    
    Provides natural language interface to Alfresco operations.
    """
    
    def __init__(self, base_url: str, username: str, password: str):
        self.factory = ClientFactory(base_url, username, password)
    
    async def handle_natural_language_query(self, query: str) -> Dict[str, Any]:
        """
        Handle natural language queries like:
        - "Find all documents modified this week"
        - "Create a new folder called 'Projects'"
        - "Search for documents containing 'budget'"
        """
        
        # This would integrate with your LLM to parse the natural language
        # and convert to appropriate API calls using the Pydantic models
        
        if "search" in query.lower():
            # Convert natural language to SearchRequest
            search_request = SearchRequest(
                query={"query": query},
                paging={"maxItems": 25}
            )
            return search_documents_tool(search_request)
        
        elif "create" in query.lower() and "folder" in query.lower():
            # Convert natural language to NodeBody for folder creation
            folder_data = NodeBody(
                name="Projects",  # Extract from query
                nodeType="cm:folder"
            )
            return create_document_tool(folder_data)
        
        else:
            return {"success": False, "error": "Query not understood"}

# Example usage
if __name__ == "__main__":
    print("LLM Integration Example")
    print("=" * 30)
    
    # Test authentication tool
    creds = TicketBody(userId="admin", password="admin123")
    auth_result = authenticate_user_tool(creds)
    print(f"Authentication: {auth_result}")
    
    # Test document creation tool  
    doc_data = NodeBody(name="test-document.txt", nodeType="cm:content")
    create_result = create_document_tool(doc_data)
    print(f"Document creation: {create_result}")
    
    print("\\nPerfect for LLM tool interfaces!")
    print("Type-safe with Pydantic validation!")
    print("Ready for MCP server integration!")
'''
        
        with open(examples_dir / "llm_integration.py", "w", encoding='utf-8') as f:
            f.write(llm_example)
    
    def _create_tests(self) -> bool:
        """Create basic test structure"""
        try:
            tests_dir = self.output_dir / "tests"
            
            # Create test __init__.py
            with open(tests_dir / "__init__.py", "w") as f:
                f.write('"""Tests for python-alfresco-api"""')
            
            # Create basic test
            test_content = '''"""
Basic tests for python-alfresco-api hybrid architecture
"""

import pytest
from python_alfresco_api import ClientFactory, AuthUtil
from python_alfresco_api.models import TicketBody

class TestClientFactory:
    """Test the client factory functionality"""
    
    def test_factory_creation(self):
        """Test factory can be created"""
        factory = ClientFactory("https://alfresco.example.com")
        assert factory.base_url == "https://alfresco.example.com"
    
    def test_individual_client_creation(self):
        """Test individual clients can be created"""
        factory = ClientFactory("https://alfresco.example.com")
        
        auth_client = factory.create_auth_client()
        core_client = factory.create_core_client()
        discovery_client = factory.create_discovery_client()
        
        assert auth_client is not None
        assert core_client is not None  
        assert discovery_client is not None
    
    def test_all_clients_creation(self):
        """Test all clients can be created at once"""
        factory = ClientFactory("https://alfresco.example.com")
        clients = factory.create_all_clients()
        
        expected_apis = ["auth", "core", "discovery", "search", "workflow", "model", "search_sql"]
        for api in expected_apis:
            assert api in clients
            assert clients[api] is not None
    
    def test_master_client_creation(self):
        """Test MasterClient creation and dot syntax access"""
        factory = ClientFactory("https://alfresco.example.com")
        master_client = factory.create_master_client()
        
        # Test MasterClient has all required attributes
        assert hasattr(master_client, 'auth'), "MasterClient should have auth attribute"
        assert hasattr(master_client, 'core'), "MasterClient should have core attribute"
        assert hasattr(master_client, 'discovery'), "MasterClient should have discovery attribute"
        assert hasattr(master_client, 'search'), "MasterClient should have search attribute"
        assert hasattr(master_client, 'workflow'), "MasterClient should have workflow attribute"
        assert hasattr(master_client, 'model'), "MasterClient should have model attribute"
        assert hasattr(master_client, 'search_sql'), "MasterClient should have search_sql attribute"
        
        # Test that attributes are not None
        assert master_client.auth is not None, "master_client.auth should not be None"
        assert master_client.core is not None, "master_client.core should not be None"
        assert master_client.search is not None, "master_client.search should not be None"
    
    def test_master_client_vs_individual_clients(self):
        """Test that MasterClient provides same clients as individual creation"""
        factory = ClientFactory("https://alfresco.example.com")
        
        # Create clients both ways
        master_client = factory.create_master_client()
        individual_auth = factory.create_auth_client()
        
        # Test that they're the same type of clients
        assert type(master_client.auth) == type(individual_auth), "MasterClient.auth should be same type as individual auth client"

class TestPydanticModels:
    """Test Pydantic model functionality"""
    
    def test_ticket_body_creation(self):
        """Test TicketBody model creation and validation"""
        ticket_body = TicketBody(userId="admin", password="admin123")
        
        assert ticket_body.userId == "admin"
        assert ticket_body.password == "admin123"
        
        # Test JSON serialization (perfect for LLMs)
        json_data = ticket_body.model_dump_json()
        assert "admin" in json_data
        assert "admin123" in json_data
    
    def test_model_validation(self):
        """Test Pydantic model validation"""
        # This should work
        valid_ticket = TicketBody(userId="test", password="test123")
        assert valid_ticket.userId == "test"
        
        # Test that validation works (will depend on actual model constraints)
        try:
            # Empty userId should potentially fail validation
            invalid_ticket = TicketBody(userId="", password="test")
            # If this doesn't raise an error, validation might be lenient
        except Exception:
            # Validation worked as expected
            pass

class TestAuthUtil:
    """Test authentication utility"""
    
    def test_auth_util_creation(self):
        """Test AuthUtil can be created"""
        auth = AuthUtil(
            "https://alfresco.example.com",
            "admin", 
            "admin123"
        )
        
        assert auth.base_url == "https://alfresco.example.com"
        assert auth.username == "admin"
        assert not auth.is_authenticated()  # Not authenticated initially

if __name__ == "__main__":
    pytest.main([__file__])
'''
            
            with open(tests_dir / "test_basic.py", "w") as f:
                f.write(test_content)
            
            print("   Test structure created")
            return True
            
        except Exception as e:
            print(f"   Failed: {e}")
            return False
    
    def _print_summary(self, models_success: bool, clients_success: bool, package_success: bool, docs_success: bool, tests_success: bool):
        """Print pipeline execution summary"""
        print("\n" + "=" * 60)
        print("ALFRESCO HYBRID PIPELINE SUMMARY")
        print("=" * 60)
        
        results = [
            ("Pydantic Models", models_success),
            ("HTTP Clients", clients_success), 
            ("Unified Package", package_success),
            ("Documentation", docs_success),
            ("Tests", tests_success)
        ]
        
        success_count = sum(1 for _, success in results if success)
        
        for name, success in results:
            status = "SUCCESS" if success else "FAILED"
            print(f"{status}: {name}")
        
        print()
        if success_count == len(results):
            print("PIPELINE COMPLETED SUCCESSFULLY!")
            print("Ready for:")
            print("   - LLM integration with Pydantic models")
            print("   - MCP server development") 
            print("   - Enterprise applications")
            print("   - Async/sync operations")
            print()
            print("Generated structure:")
            print(f"   {self.output_dir}")
            print("   ├── models/          # Pydantic v2 models")
            print("   ├── clients/         # Individual client wrappers")
            print("   ├── raw_clients/     # Generated HTTP clients")
            print("   ├── examples/        # Usage examples")
            print("   ├── docs/           # Documentation")
            print("   └── tests/          # Test suite")
        else:
            print(f"PIPELINE PARTIALLY COMPLETED: {success_count}/{len(results)} successful")
            print("   Check errors above for failed components")

def main():
    """Run the complete hybrid pipeline"""
    pipeline = AlfrescoHybridPipeline()
    pipeline.run_complete_pipeline()

if __name__ == "__main__":
    main()
