"""
Upload Document Example using High-Level Utilities

This example demonstrates how to upload documents to Alfresco using the high-level
content_utils_highlevel module, showing the dramatic simplification compared to
raw API calls (83% code reduction from original MCP implementation).
"""

from pathlib import Path
from python_alfresco_api.client_factory import ClientFactory
from python_alfresco_api.utils.content_utils_highlevel import create_and_upload_file_highlevel


def upload_document_example():
    """Example of uploading a document with automatic versioning."""
    
    # Initialize clients
    client_factory = ClientFactory()
    core_client = client_factory.create_core_client()
    
    # Example 1: Upload with minimal parameters
    print("Example 1: Basic upload")
    try:
        result = create_and_upload_file_highlevel(
            core_client=core_client,
            file_path="./test_document.txt",
            filename="My Document.txt",
            parent_id="-shared-"  # Upload to shared folder
        )
        print(f"[SUCCESS] Upload successful: {result}")
    except Exception as e:
        print(f"[ERROR] Upload failed: {e}")
    
    # Example 2: Upload with full metadata
    print("\nExample 2: Upload with metadata")
    try:
        result = create_and_upload_file_highlevel(
            core_client=core_client,
            file_path="./important_document.pdf",
            filename="Important Report.pdf",
            parent_id="-my-",  # Upload to user's folder
            description="Quarterly financial report",
            title="Q4 Financial Report"
        )
        print(f"[SUCCESS] Upload with metadata successful: {result}")
    except Exception as e:
        print(f"[ERROR] Upload failed: {e}")
    
    # Example 3: Upload to specific folder
    print("\nExample 3: Upload to specific folder")
    try:
        # First, you would get the folder ID from browsing or searching
        specific_folder_id = "your-folder-id-here"
        
        result = create_and_upload_file_highlevel(
            core_client=core_client,
            file_path="./project_file.docx",
            parent_id=specific_folder_id
        )
        print(f"[SUCCESS] Upload to specific folder successful: {result}")
    except Exception as e:
        print(f"[ERROR] Upload failed: {e}")


def batch_upload_example():
    """Example of uploading multiple documents."""
    
    client_factory = ClientFactory()
    core_client = client_factory.create_core_client()
    
    # Files to upload
    files_to_upload = [
        {"path": "./document1.txt", "name": "Document One.txt"},
        {"path": "./document2.pdf", "name": "Document Two.pdf"},
        {"path": "./document3.docx", "name": "Document Three.docx"}
    ]
    
    print("Batch upload example:")
    for file_info in files_to_upload:
        try:
            result = create_and_upload_file_highlevel(
                core_client=core_client,
                file_path=file_info["path"],
                filename=file_info["name"],
                parent_id="-shared-"
            )
            print(f"[SUCCESS] Uploaded {file_info['name']}: {result}")
        except Exception as e:
            print(f"[ERROR] Failed to upload {file_info['name']}: {e}")


if __name__ == "__main__":
    print(">>> High-Level Upload Document Examples")
    print("=" * 50)
    
    print("\n[FOLDER] Single Document Upload Examples:")
    upload_document_example()
    
    print("\n[BATCH] Batch Upload Example:")
    batch_upload_example()
    
    print("\n[BENEFITS] Key Benefits:")
    print("- Automatic versioning (starts at 1.0)")
    print("- Built-in error handling")
    print("- Type safety with Pydantic models")
    print("- One-line operations")
    print("- 83% code reduction vs raw API calls") 