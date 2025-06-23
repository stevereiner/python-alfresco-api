# Installation Guide

Complete installation and setup guide for Python Alfresco API.

## Requirements

### System Requirements
- **Python**: 3.8+ (3.9+ recommended)
- **Operating System**: Windows, macOS, Linux
- **Memory**: 512MB+ RAM available
- **Disk Space**: 50MB+ for installation

### Alfresco Requirements
- **Alfresco Community Edition**: 6.0+ or 7.0+
- **Alfresco Enterprise Edition**: 6.0+ or 7.0+
- **Network Access**: HTTP/HTTPS connectivity to Alfresco server

## Installation Methods

### Method 1: PyPI Installation (Recommended)

```bash
pip install python-alfresco-api
```

### Method 2: Development Installation

```bash
# Clone the repository
git clone https://github.com/your-org/python-alfresco-api.git
cd python-alfresco-api

# Install in development mode
pip install -e .

# Or install with development dependencies
pip install -e .[dev]
```

### Method 3: From Source

```bash
# Download and extract source
wget https://github.com/your-org/python-alfresco-api/archive/main.zip
unzip main.zip
cd python-alfresco-api-main

# Install
python setup.py install
```

## Virtual Environment Setup

### Using venv (Recommended)

```bash
# Create virtual environment
python -m venv alfresco-env

# Activate (Windows)
alfresco-env\Scripts\activate

# Activate (macOS/Linux)
source alfresco-env/bin/activate

# Install package
pip install python-alfresco-api
```

### Using conda

```bash
# Create conda environment
conda create -n alfresco-env python=3.9
conda activate alfresco-env

# Install package
pip install python-alfresco-api
```

### Using Poetry

```bash
# Initialize Poetry project
poetry init

# Add dependency
poetry add python-alfresco-api

# Install
poetry install
```

## Configuration

### Environment Variables

Create a `.env` file or set environment variables:

```bash
# Basic configuration
export ALFRESCO_BASE_URL="http://localhost:8080"
export ALFRESCO_USERNAME="admin"
export ALFRESCO_PASSWORD="admin"

# SSL configuration
export ALFRESCO_VERIFY_SSL=false

# Advanced configuration
export ALFRESCO_TIMEOUT=30
export ALFRESCO_MAX_RETRIES=3
```

### Configuration File

Create `alfresco_config.yaml`:

```yaml
# Alfresco server configuration
base_url: "http://localhost:8080"
username: "admin"
password: "admin"
verify_ssl: false

# Connection settings
timeout: 30
max_retries: 3
retry_delay: 1.0

# Logging
log_level: "INFO"
log_file: "alfresco_api.log"
```

### Programmatic Configuration

```python
from python_alfresco_api import ClientFactory

# Direct factory configuration
factory = ClientFactory(
    base_url="http://localhost:8080",
    username="admin",
    password="admin",
    verify_ssl=False
)
```

## Verification

### Quick Test

```python
# Test basic connectivity
from python_alfresco_api import ClientFactory

try:
    factory = ClientFactory("http://localhost:8080")
    clients = factory.create_all_clients()
    
    # Test auth client
    auth_client = clients["auth"]
    print(f"Auth client available: {auth_client.is_available()}")
    
    # Test discovery
    discovery_client = clients["discovery"]
    if discovery_client.is_available():
        repo_info = discovery_client.get_repository_info_sync()
        print(f"Connected to Alfresco {repo_info.version.display}")
    
    print("✅ Installation successful!")
    
except Exception as e:
    print(f"❌ Installation issue: {e}")
```

### Full Test Suite

```bash
# Clone repository for tests
git clone https://github.com/your-org/python-alfresco-api.git
cd python-alfresco-api

# Install with development dependencies (RECOMMENDED)
pip install -e .[dev]

# Run tests
python run_tests.py

# Run specific test
pytest tests/test_alfresco_basic.py -v
```

## Development Setup

### Prerequisites

```bash
# Install development tools
pip install build wheel twine
pip install pytest pytest-cov pytest-asyncio
pip install black isort mypy ruff
```

### Development Dependencies

**RECOMMENDED:** Use the modern pyproject.toml approach:

```bash
# Install with development dependencies (includes mypy, black, pytest, etc.)
pip install -e .[dev]

# Or install with both dev and test dependencies
pip install -e .[dev,test]
```

**ALTERNATIVE:** Use requirements files (may have missing dependencies):

```bash
# Install from requirements file
pip install -r requirements-dev.txt

# Note: Some tools like mypy may not be included in requirements-dev.txt
# Use the .[dev] method above for complete development setup
```

### Pre-commit Hooks

```bash
# Install pre-commit
pip install pre-commit

# Setup hooks
pre-commit install

# Run manually
pre-commit run --all-files
```

## Alfresco Server Setup

### Local Development (Docker)

```bash
# Quick Alfresco Community setup
docker run -d \
  --name alfresco \
  -p 8080:8080 \
  -e JAVA_OPTS="-Xms512m -Xmx1g" \
  alfresco/alfresco-community-repo:latest

# Wait for startup (2-3 minutes)
# Test: http://localhost:8080/alfresco
```

### Docker Compose

Create `docker-compose.yml`:

```yaml
version: '3.8'
services:
  alfresco:
    image: alfresco/alfresco-community-repo:7.4.0
    ports:
      - "8080:8080"
    environment:
      JAVA_OPTS: "-Xms512m -Xmx1g"
    volumes:
      - alfresco-data:/usr/local/tomcat/alf_data

  postgres:
    image: postgres:13
    environment:
      POSTGRES_DB: alfresco
      POSTGRES_USER: alfresco
      POSTGRES_PASSWORD: alfresco
    volumes:
      - postgres-data:/var/lib/postgresql/data

volumes:
  alfresco-data:
  postgres-data:
```

```bash
# Start services
docker-compose up -d

# Check logs
docker-compose logs -f alfresco
```

### Connection Testing

```bash
# Test Alfresco availability
curl http://localhost:8080/alfresco/api/-default-/public/alfresco/versions/1/probes/-ready-

# Test authentication
curl -X POST http://localhost:8080/alfresco/api/-default-/public/authentication/versions/1/tickets \
  -H "Content-Type: application/json" \
  -d '{"userId":"admin","password":"admin"}'
```

## IDE Setup

### Visual Studio Code

Install recommended extensions:

```json
{
  "recommendations": [
    "ms-python.python",
    "ms-python.mypy-type-checker",
    "charliermarsh.ruff",
    "ms-python.black-formatter",
    "ms-python.isort",
    "ms-vscode.vscode-json"
  ]
}
```

### PyCharm

1. **Project Setup**:
   - Open project folder
   - Configure Python interpreter (virtual environment)
   - Mark `python_alfresco_api` as sources root

2. **Code Style**:
   - Enable Black formatter
   - Configure import sorting (isort)
   - Enable type checking (mypy)

### Jupyter/Lab

```bash
# Install Jupyter
pip install jupyterlab

# Install in kernel
python -m ipykernel install --user --name alfresco-env

# Start Jupyter
jupyter lab

# Test in notebook
from python_alfresco_api import ClientFactory
factory = ClientFactory("http://localhost:8080")
```

## Dependencies

### Runtime Dependencies

```txt
pydantic>=2.0.0
httpx>=0.24.0
aiofiles>=23.0.0
python-dateutil>=2.8.0
typing-extensions>=4.0.0
```

### Development Dependencies

```txt
pytest>=7.0.0
pytest-asyncio>=0.21.0
pytest-cov>=4.0.0
black>=23.0.0
isort>=5.12.0
mypy>=1.0.0
ruff>=0.0.280
pre-commit>=3.0.0
```

### Complete Feature Set

The `python-alfresco-api` package includes all features by default:

```txt
# Core dependencies (included)
httpx>=0.24.0           # HTTP client
pydantic>=2.0.0         # Data validation
attrs>=23.1.0           # Generated client support
python-dateutil>=2.8.0  # Date handling
typing-extensions>=4.5.0 # Type hints
PyYAML>=6.0             # Configuration
stomp.py>=8.1.0         # Event system support
```

No optional dependencies needed - everything works out of the box!

## Troubleshooting

### Common Issues

#### Import Errors

```python
# Error: No module named 'python_alfresco_api'
# Solution: Check installation
pip list | grep alfresco
pip install python-alfresco-api

# Error: ModuleNotFoundError for dependencies
# Solution: Install dependencies
pip install -r requirements.txt
```

#### Connection Issues

```python
# Error: Connection refused
# Check: Alfresco server running
curl http://localhost:8080/alfresco/

# Error: SSL verification failed
# Solution: Disable SSL verification
factory = ClientFactory(verify_ssl=False)

# Error: Authentication failed
# Check: Username/password correct
# Test: Manual curl authentication
```

#### Performance Issues

```python
# Slow requests
# Solution: Use connection pooling
import aiohttp
async with aiohttp.ClientSession() as session:
    factory = ClientFactory("http://localhost:8080", session=session)
    
# High memory usage
# Solution: Use pagination
results = await search_client.search({
    "query": {"query": "TYPE:cm:content"},
    "paging": {"maxItems": 100}  # Limit results
})
```

### Logging Configuration

```python
import logging

# Enable debug logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Specific logger for Alfresco API
logger = logging.getLogger('python_alfresco_api')
logger.setLevel(logging.DEBUG)

# HTTP request logging
import httpx
httpx_logger = logging.getLogger("httpx")
httpx_logger.setLevel(logging.DEBUG)
```

### Diagnostic Information

```python
# System information
import sys
import platform
print(f"Python: {sys.version}")
print(f"Platform: {platform.platform()}")

# Package version
import python_alfresco_api
print(f"API Version: {python_alfresco_api.__version__}")

# Dependencies
import pydantic
import httpx
print(f"Pydantic: {pydantic.VERSION}")
print(f"HTTPX: {httpx.__version__}")

# Alfresco connectivity
from python_alfresco_api import ClientFactory
factory = ClientFactory("http://localhost:8080")
clients = factory.create_all_clients()

for name, client in clients.items():
    print(f"{name}: {client.is_available()}")
```

### Performance Optimization

#### Async Best Practices

```python
import asyncio
import aiohttp

async def optimized_usage():
    # Use session for connection pooling
    connector = aiohttp.TCPConnector(
        limit=100,          # Total connection pool size
        limit_per_host=30,  # Per-host connection limit
        ttl_dns_cache=300,  # DNS cache TTL
        use_dns_cache=True,
    )
    
    timeout = aiohttp.ClientTimeout(total=30)
    
    async with aiohttp.ClientSession(
        connector=connector,
        timeout=timeout
    ) as session:
        factory = ClientFactory(
            "http://localhost:8080",
            session=session
        )
        clients = factory.create_all_clients()
        
        # Batch operations
        tasks = []
        for i in range(10):
            task = clients["core"].get_node(f"node-{i}")
            tasks.append(task)
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results
```

#### Memory Optimization

```python
# Use generators for large datasets
async def iterate_nodes(core_client, folder_id):
    skip_count = 0
    max_items = 100
    
    while True:
        children = await core_client.get_node_children(
            folder_id,
            skipCount=skip_count,
            maxItems=max_items
        )
        
        if not children.entries:
            break
            
        for entry in children.entries:
            yield entry.entry
        
        skip_count += max_items
        
        # Prevent infinite loops
        if not children.pagination.hasMoreItems:
            break

# Usage
async for node in iterate_nodes(core_client, "-root-"):
    print(f"Processing: {node.name}")
```

## Production Deployment

### Configuration Management

```python
# Use environment-specific configs
import os
from python_alfresco_api import ClientFactory

def get_factory():
    env = os.getenv('ENVIRONMENT', 'development')
    
    if env == 'production':
        return ClientFactory(
            base_url=os.getenv('ALFRESCO_URL'),
            username=os.getenv('ALFRESCO_USER'),
            password=os.getenv('ALFRESCO_PASS'),
            verify_ssl=True,
            timeout=60
        )
    else:
        return ClientFactory()  # Uses dev defaults
```

### Security Considerations

```python
# Use secrets management
import keyring
from python_alfresco_api import ClientFactory

def get_secure_factory():
    return ClientFactory(
        base_url="https://alfresco.company.com",
        username=keyring.get_password("alfresco", "username"),
        password=keyring.get_password("alfresco", "password"),
        verify_ssl=True
    )

# Certificate handling
import ssl
import certifi

ssl_context = ssl.create_default_context(cafile=certifi.where())
# Add custom certificates if needed
```

### Monitoring

```python
# Prometheus metrics
from prometheus_client import Counter, Histogram, start_http_server

REQUEST_COUNT = Counter('alfresco_requests_total', 'Total requests', ['method', 'endpoint'])
REQUEST_DURATION = Histogram('alfresco_request_duration_seconds', 'Request duration')

# Usage in your application
with REQUEST_DURATION.time():
    result = await core_client.get_node(node_id)
    REQUEST_COUNT.labels(method='GET', endpoint='nodes').inc()

# Start metrics server
start_http_server(8000)
```

---

For additional help, see the [API Reference](API_REFERENCE.md) or open an issue on GitHub. 