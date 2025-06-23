"""
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
    version="2.0.0",
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
        "License :: OSI Approved :: MIT License",
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
