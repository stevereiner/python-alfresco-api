#!/usr/bin/env python3
"""
Simple Progress Example - Clear, Obvious Progress Reporting

This shows how to make scripts that clearly show they're working
without looking like they're hanging.
"""

import time

def simple_task_with_clear_progress():
    """Example of clear progress reporting."""
    
    tasks = ["Setup", "Processing", "Validation", "Cleanup"]
    
    print("🚀 Starting tasks...")
    print()
    
    for i, task in enumerate(tasks, 1):
        print(f"⏳ Step {i}/{len(tasks)}: {task}...")
        
        # Simulate work with clear status updates
        for j in range(3):
            time.sleep(0.5)  # Simulate work
            print(f"   • Working... ({j+1}/3)")
        
        print(f"✅ Step {i} completed: {task}")
        print()
    
    print("🎉 All tasks completed successfully!")

if __name__ == "__main__":
    simple_task_with_clear_progress() 