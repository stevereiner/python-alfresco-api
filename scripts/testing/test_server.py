#!/usr/bin/env python3
import requests
import sys

try:
    response = requests.get('http://localhost:8080/alfresco/api/-default-/public/alfresco/versions/1/probes/-ready-', timeout=5)
    if response.status_code == 200:
        print("success")
    else:
        print(f"Server responded with status: {response.status_code}")
        sys.exit(1)
except Exception as e:
    print(f"Connection failed: {e}")
    sys.exit(1) 