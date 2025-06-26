#!/usr/bin/env python3
import sys
import time

try:
    from python_alfresco_api import ClientFactory
    start = time.time()
    factory = ClientFactory('http://localhost:8080')
    clients = factory.create_all_clients()
    duration = (time.time() - start) * 1000
    print(f'Client creation: {duration:.2f}ms')
    sys.exit(0)
except Exception as e:
    print(f'Performance test skipped: {str(e)}')
    sys.exit(1) 