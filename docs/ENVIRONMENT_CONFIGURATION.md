# 🔧 Environment Configuration Guide

The Python Alfresco API now supports automatic configuration from environment variables and `.env` files, making deployment and development much easier.

## 📋 **Configuration Priority**

1. **Explicit parameters** (highest priority)
2. **Environment variables** 
3. **Default values** (lowest priority)

```python
# Explicit parameters override everything
factory = ClientFactory(
    base_url="http://prod.alfresco.com",  # This overrides ALFRESCO_URL
    username="admin"                      # This overrides ALFRESCO_USERNAME
)
```

## 🌍 **Environment Variables**

### **Supported Environment Variables**

| Variable | Alternative | Description | Default |
|----------|-------------|-------------|---------|
| `ALFRESCO_URL` | `ALFRESCO_BASE_URL` | Alfresco server URL | `http://localhost:8080` |
| `ALFRESCO_USERNAME` | - | Authentication username | `admin` |
| `ALFRESCO_PASSWORD` | - | Authentication password | `admin` |
| `ALFRESCO_VERIFY_SSL` | `ALFRESCO_SSL_VERIFY` | SSL verification | `true` |

### **Usage Examples**

```bash
# Linux/macOS
export ALFRESCO_URL="https://alfresco.company.com"
export ALFRESCO_USERNAME="your-username"
export ALFRESCO_PASSWORD="your-password"
export ALFRESCO_VERIFY_SSL="true"

# Windows
set ALFRESCO_URL=https://alfresco.company.com
set ALFRESCO_USERNAME=your-username
set ALFRESCO_PASSWORD=your-password
set ALFRESCO_VERIFY_SSL=true
```

## 📁 **.env File Support**

### **Installation**

For `.env` file support, install the optional dependency:
```bash
pip install python-dotenv
```

### **Create .env File**

Copy the sample file and customize for your environment:
```bash
# Copy the sample file
cp sample-dot-env.txt .env

# Edit the .env file with your settings
# The sample includes examples for development, Docker, and production
```

Sample `.env` file content (see `sample-dot-env.txt`):
```bash
# Python Alfresco API Configuration
ALFRESCO_URL=http://localhost:8080
ALFRESCO_USERNAME=admin
ALFRESCO_PASSWORD=admin
ALFRESCO_VERIFY_SSL=false
```

### **Usage Patterns**

#### **1. Automatic .env Loading (Recommended)**
```python
from python_alfresco_api import ClientFactory

# Automatically loads from .env file if present
factory = ClientFactory()
print(factory.get_config_info())  # Shows loaded configuration
```

#### **2. Explicit .env File**
```python
from python_alfresco_api import ClientFactory

# Load from specific .env file
factory = ClientFactory(env_file=".env.production")
```

#### **3. From Environment Only**
```python
from python_alfresco_api import ClientFactory

# Use class method for clarity
factory = ClientFactory.from_env()
```

#### **4. Disable Environment Loading**
```python
from python_alfresco_api import ClientFactory

# Explicit parameters only, ignore environment
factory = ClientFactory(
    base_url="http://localhost:8080",
    username="admin",
    password="admin",
    load_env=False  # Disable environment loading
)
```

## 🔒 **SSL Certificate Configuration**

The `ALFRESCO_VERIFY_SSL` setting supports three modes (matching raw client capabilities):

```bash
# 1. Enable SSL verification (default)
ALFRESCO_VERIFY_SSL=true

# 2. Disable SSL verification (NOT recommended for production)
ALFRESCO_VERIFY_SSL=false

# 3. Custom certificate bundle path (for internal certificates)
ALFRESCO_VERIFY_SSL=/etc/ssl/certs/custom-ca.pem
```

### **Usage Examples**

```python
from python_alfresco_api import ClientFactory

# Boolean values
factory1 = ClientFactory(verify_ssl=True)   # Standard SSL verification
factory2 = ClientFactory(verify_ssl=False)  # Disable SSL (testing only)

# Certificate path  
factory3 = ClientFactory(verify_ssl="/path/to/custom.pem")  # Custom certificate

# From environment variables
# ALFRESCO_VERIFY_SSL=/etc/ssl/certs/internal-ca.pem
factory4 = ClientFactory()  # Uses custom certificate from environment
```

This matches the raw client's SSL handling capabilities from the generated `AuthenticatedClient`.

## 🔍 **Configuration Debugging**

### **Check Current Configuration**
```python
factory = ClientFactory()
config = factory.get_config_info()
print(config)

# Output:
# {
#     'base_url': 'http://localhost:8080',
#     'username': 'admin', 
#     'password': '***',
#     'verify_ssl': False,
#     'timeout': 30,
#     'has_auth': True,
#     'dotenv_available': True
# }
```

## 🚀 **Real-World Examples**

### **Development Setup**
```python
# .env file for development
ALFRESCO_URL=http://localhost:8080
ALFRESCO_USERNAME=admin
ALFRESCO_PASSWORD=admin
ALFRESCO_VERIFY_SSL=false

# Python code
from python_alfresco_api import ClientFactory
factory = ClientFactory()  # Loads automatically
master_client = factory.create_master_client()
```

### **Production Deployment**
```python
# Environment variables in production (Docker, Kubernetes, etc.)
ALFRESCO_URL=https://alfresco.company.com
ALFRESCO_USERNAME=${VAULT_USERNAME}
ALFRESCO_PASSWORD=${VAULT_PASSWORD}
ALFRESCO_VERIFY_SSL=true

# Python code (same as development!)
from python_alfresco_api import ClientFactory
factory = ClientFactory()  # Loads from environment
master_client = factory.create_master_client()
```

### **Multi-Environment Config**
```python
import os
from python_alfresco_api import ClientFactory

# Load different .env files based on environment
env = os.getenv('APP_ENV', 'development')
env_file = f".env.{env}"

factory = ClientFactory(env_file=env_file)
print(f"Loaded config from {env_file}")
print(factory.get_config_info())
```

## 🔒 **Security Best Practices**

### **Don't Commit .env Files**
```bash
# .gitignore (already included)
.env
.env.local
.env.production
.env.staging
```

### **Use Environment Variables in Production**
```yaml
# Docker Compose example
version: '3.8'
services:
  app:
    environment:
      - ALFRESCO_URL=https://alfresco.company.com
      - ALFRESCO_USERNAME=${VAULT_USERNAME}
      - ALFRESCO_PASSWORD=${VAULT_PASSWORD}
      - ALFRESCO_VERIFY_SSL=true
```

### **Kubernetes ConfigMap/Secret**
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: alfresco-config
data:
  ALFRESCO_URL: "https://alfresco.company.com"
  ALFRESCO_VERIFY_SSL: "true"
---
apiVersion: v1
kind: Secret
metadata:
  name: alfresco-credentials
data:
  ALFRESCO_USERNAME: <base64-encoded-username>
  ALFRESCO_PASSWORD: <base64-encoded-password>
```

## 🆚 **Migration from Manual Configuration**

### **Before (Manual)**
```python
import os
from python_alfresco_api import ClientFactory

factory = ClientFactory(
    base_url=os.getenv('ALFRESCO_URL', 'http://localhost:8080'),
    username=os.getenv('ALFRESCO_USERNAME', 'admin'),
    password=os.getenv('ALFRESCO_PASSWORD', 'admin'),
    verify_ssl=os.getenv('ALFRESCO_VERIFY_SSL', 'true').lower() == 'true'
)
```

### **After (Automatic)**
```python
from python_alfresco_api import ClientFactory

# Same result, much simpler!
factory = ClientFactory()
```

The new automatic configuration makes the Python Alfresco API much more deployment-friendly while maintaining full backward compatibility! 🎉 