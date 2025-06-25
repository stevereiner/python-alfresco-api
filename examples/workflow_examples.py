#!/usr/bin/env python3
"""
Alfresco Workflow API Examples

This file demonstrates how to use the Workflow API with the master client.
The Workflow API provides access to process definitions, process instances, and tasks.
"""

import sys
import os

from python_alfresco_api import ClientFactory

def main():
    """Workflow API examples."""
    print("⚙️ Workflow API Examples")
    
    # Initialize client
    factory = ClientFactory(base_url="http://localhost:8080", username="admin", password="admin")
    client = factory.create_master_client()
    
    if not client.workflow:
        print("❌ Workflow API not available")
        return
    
    # Check Workflow API structure
    if isinstance(client.workflow, dict):
        print(f"Available Workflow APIs: {list(client.workflow.keys())}")
        
        # Example 1: Process Definitions API
        if 'process-definitions' in client.workflow:
            print("\n1. Testing Process Definitions API...")
            try:
                process_defs = client.workflow['process-definitions'].list_process_definitions()
                if process_defs and hasattr(process_defs, 'list'):
                    print(f"✅ Found {len(process_defs.list.entries)} process definitions")
                    for i, proc_def in enumerate(process_defs.list.entries[:3]):
                        if hasattr(proc_def, 'entry'):
                            print(f"  {i+1}. {proc_def.entry.id}: {getattr(proc_def.entry, 'name', 'No name')}")
                else:
                    print("✅ Process Definitions API responded")
            except Exception as e:
                print(f"❌ Process Definitions API failed: {e}")
        
        # Example 2: Process Instances API
        if 'process-instances' in client.workflow:
            print("\n2. Testing Process Instances API...")
            try:
                process_instances = client.workflow['process-instances'].list_process_instances()
                if process_instances and hasattr(process_instances, 'list'):
                    print(f"✅ Found {len(process_instances.list.entries)} process instances")
                    for i, instance in enumerate(process_instances.list.entries[:3]):
                        if hasattr(instance, 'entry'):
                            print(f"  {i+1}. {instance.entry.id}: {getattr(instance.entry, 'processDefinitionId', 'No definition')}")
                else:
                    print("✅ Process Instances API responded")
            except Exception as e:
                print(f"❌ Process Instances API failed: {e}")
        
        # Example 3: Tasks API
        if 'tasks' in client.workflow:
            print("\n3. Testing Tasks API...")
            try:
                tasks = client.workflow['tasks'].list_tasks()
                if tasks and hasattr(tasks, 'list'):
                    print(f"✅ Found {len(tasks.list.entries)} tasks")
                    for i, task in enumerate(tasks.list.entries[:3]):
                        if hasattr(task, 'entry'):
                            print(f"  {i+1}. {task.entry.id}: {getattr(task.entry, 'name', 'No name')}")
                else:
                    print("✅ Tasks API responded")
            except Exception as e:
                print(f"❌ Tasks API failed: {e}")
        
        # Example 4: Deployments API
        if 'deployments' in client.workflow:
            print("\n4. Testing Deployments API...")
            try:
                deployments = client.workflow['deployments'].list_deployments()
                if deployments and hasattr(deployments, 'list'):
                    print(f"✅ Found {len(deployments.list.entries)} deployments")
                else:
                    print("✅ Deployments API responded")
            except Exception as e:
                print(f"❌ Deployments API failed: {e}")
        
        # Example 5: User Candidates API
        if 'user-candidates' in client.workflow:
            print("\n5. Testing User Candidates API...")
            try:
                candidates = client.workflow['user-candidates'].list_candidates()
                print("✅ User Candidates API available")
            except Exception as e:
                print(f"❌ User Candidates API failed: {e}")
    
    else:
        print("Workflow API available in single object format")
        # Example for single object format
        if hasattr(client.workflow, 'list_process_definitions'):
            print("\n1. Testing workflow functionality...")
            try:
                process_defs = client.workflow.list_process_definitions()
                print("✅ Workflow functionality available")
            except Exception as e:
                print(f"❌ Workflow failed: {e}")

if __name__ == "__main__":
    main() 