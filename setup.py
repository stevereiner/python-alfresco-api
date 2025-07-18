#!/usr/bin/env python3
"""
Setup script for python-alfresco-api v1.1

Python Client for all Alfresco Content Services REST APIs, with Pydantic v2 Models, and Event Support
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

# Read requirements
def read_requirements(filename):
    """Read requirements from file, excluding comments and empty lines."""
    requirements = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and not line.startswith('-r'):
                requirements.append(line)
    return requirements

# Core runtime requirements
install_requires = read_requirements('requirements.txt')

# Optional dependencies
extras_require = {
    'events': [
        'stomp.py>=8.1.0',
    ],
    'performance': [
        'ujson>=5.7.0',
        'orjson>=3.8.0',
    ],
    'oauth': [
        'requests-oauthlib>=1.3.0',
    ],
    'dev': read_requirements('requirements-dev.txt'),
    'test': [
        'pytest>=7.4.0',
        'pytest-asyncio>=0.21.0',
        'pytest-cov>=4.1.0',
        'pytest-mock>=3.11.0',
        'requests-mock>=1.11.0',
    ],
}

# Convenience extras
extras_require['all'] = (
    extras_require['events'] + 
    extras_require['performance'] + 
    extras_require['oauth']
)

setup(
    name="python-alfresco-api",
    version="1.1.0",
    author="Steve Reiner",
    author_email="stevereiner@integratedsemantics.com",
    description="Python Client for all Alfresco Content Services REST APIs, with Pydantic v2 Models, and Event Support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stevereiner/python-alfresco-api",
    project_urls={
        "Bug Reports": "https://github.com/stevereiner/python-alfresco-api/issues",
        "Source": "https://github.com/stevereiner/python-alfresco-api",
        "Documentation": "https://github.com/stevereiner/python-alfresco-api/docs",
        "Examples": "https://github.com/stevereiner/python-alfresco-api/examples",
    },
    packages=find_packages(include=["python_alfresco_api", "python_alfresco_api.*"]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Content Management System",
        "Topic :: Office/Business :: Office Suites",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Framework :: Pydantic",
        "Typing :: Typed",
    ],
    python_requires=">=3.8",
    install_requires=install_requires,
    extras_require=extras_require,
    include_package_data=True,
    package_data={
        "python_alfresco_api": [
            "py.typed",  # Mark package as typed
        ],
    },
    keywords=[
        "alfresco",
        "content-management",
        "rest-api",
        "pydantic",
        "ecm",
        "enterprise",
        "document-management",
        "mcp",
        "model-context-protocol",
        "ai-integration"
    ],
    entry_points={
        "console_scripts": [
            # Add any command-line tools here if needed
        ],
    },
    zip_safe=False,  # Required for typed packages
) 