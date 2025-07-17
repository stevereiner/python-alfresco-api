"""
Pydantic Field Annotations - Auto-Generated Documentation Example

Shows how Field annotations automatically generate beautiful documentation,
validation, and type safety for data models.
"""

from datetime import datetime
from enum import Enum
from typing import Annotated, Optional, List
from pydantic import BaseModel, Field, EmailStr, validator


class Priority(Enum):
    """Task priority levels."""
    LOW = "low"
    MEDIUM = "medium" 
    HIGH = "high"
    URGENT = "urgent"


class TaskStatus(Enum):
    """Task completion status."""
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    REVIEW = "review"
    COMPLETED = "completed"


class DocumentMetadata(BaseModel):
    """
    Document metadata with auto-generated documentation.
    
    Each Field annotation automatically generates:
    - HTML documentation
    - IDE tooltips  
    - JSON Schema
    - Runtime validation
    - Type safety
    """
    
    # Basic field with description
    title: Annotated[
        str, 
        Field(
            description="Document title - will appear in search results and listings",
            min_length=1,
            max_length=255
        )
    ]
    
    # Optional field with rich description
    description: Annotated[
        Optional[str],
        Field(
            description="Detailed document description supporting markdown formatting. "
                       "This appears in document previews and helps with content discovery.",
            max_length=2000
        )
    ] = None
    
    # Enum field with validation
    priority: Annotated[
        Priority,
        Field(
            description="Document priority level affecting processing order and notifications. "
                       "URGENT documents trigger immediate alerts to assigned users.",
        )
    ] = Priority.MEDIUM
    
    # List field with constraints
    tags: Annotated[
        List[str],
        Field(
            description="Searchable tags for content organization and discovery. "
                       "Tags should be lowercase, alphanumeric, and separated by commas.",
            min_length=0,
            max_length=20
        )
    ] = []
    
    # Email field with built-in validation
    author_email: Annotated[
        EmailStr,
        Field(
            description="Author's email address for notifications and ownership tracking. "
                       "Must be a valid email format (user@domain.com)."
        )
    ]
    
    # Datetime field with description
    created_at: Annotated[
        datetime,
        Field(
            description="Document creation timestamp in ISO format. "
                       "Automatically set when document is first created."
        )
    ] = Field(default_factory=datetime.now)
    
    # Constrained string with pattern
    document_id: Annotated[
        str,
        Field(
            description="Unique document identifier following Alfresco node ID format. "
                       "Must be alphanumeric with hyphens, used for API operations.",
            pattern=r'^[a-zA-Z0-9\-]+$',
            min_length=10,
            max_length=50
        )
    ]
    
    # Numeric field with bounds
    file_size_bytes: Annotated[
        int,
        Field(
            description="Document file size in bytes. Used for storage quota calculations "
                       "and upload progress tracking. Maximum size is 100MB.",
            ge=0,  # greater than or equal to 0
            le=100 * 1024 * 1024  # less than or equal to 100MB
        )
    ] = 0


class TaskModel(BaseModel):
    """
    Task management model with comprehensive Field annotations.
    
    Demonstrates advanced validation patterns and documentation generation.
    """
    
    # Required field with detailed description
    name: Annotated[
        str,
        Field(
            description="Task name displayed in task lists and notifications. "
                       "Should be descriptive and actionable (e.g., 'Review Q4 budget proposal').",
            min_length=3,
            max_length=100
        )
    ]
    
    # Status enum with documentation
    status: Annotated[
        TaskStatus,
        Field(
            description="Current task status affecting workflow and notifications:\n"
                       "- TODO: Not started, appears in pending lists\n"
                       "- IN_PROGRESS: Actively being worked on\n"
                       "- REVIEW: Awaiting review/approval\n"
                       "- COMPLETED: Finished, archived in completed lists"
        )
    ] = TaskStatus.TODO
    
    # Optional deadline with validation
    due_date: Annotated[
        Optional[datetime],
        Field(
            description="Task deadline for priority sorting and overdue alerts. "
                       "Leave empty for tasks without specific deadlines."
        )
    ] = None
    
    # List of assignees with constraints
    assignees: Annotated[
        List[str],
        Field(
            description="List of user IDs assigned to this task. Users receive notifications "
                       "for status changes and approaching deadlines. Maximum 10 assignees.",
            max_length=10
        )
    ] = []
    
    # Progress percentage with bounds
    progress_percent: Annotated[
        int,
        Field(
            description="Task completion percentage (0-100). Used for progress tracking "
                       "and project dashboards. Updates automatically in some workflows.",
            ge=0,
            le=100
        )
    ] = 0
    
    # Rich text field
    notes: Annotated[
        str,
        Field(
            description="Task notes and comments supporting markdown formatting. "
                       "Use for progress updates, blockers, and collaboration.",
            max_length=5000
        )
    ] = ""
    
    @validator('due_date')
    def validate_due_date(cls, v):
        """Ensure due date is not in the past."""
        if v and v < datetime.now():
            raise ValueError('Due date cannot be in the past')
        return v


# Example usage and documentation generation
if __name__ == "__main__":
    # Create a documented model instance
    doc = DocumentMetadata(
        title="Python Alfresco API Guide",
        description="Comprehensive guide for integrating Python applications with Alfresco",
        priority=Priority.HIGH,
        tags=["python", "alfresco", "api", "integration"],
        author_email="developer@example.com",
        document_id="doc-python-alfresco-guide-2025",
        file_size_bytes=1024000
    )
    
    # Create a task model
    task = TaskModel(
        name="Review documentation updates",
        status=TaskStatus.IN_PROGRESS,
        assignees=["user123", "user456"],
        progress_percent=75,
        notes="## Progress\n- [x] Content review\n- [ ] Technical validation"
    )
    
    print("=== Document Model ===")
    print(doc.model_dump_json(indent=2))
    
    print("\n=== Task Model ===")
    print(task.model_dump_json(indent=2))
    
    print("\n=== Generated JSON Schema (with descriptions!) ===")
    schema = DocumentMetadata.model_json_schema()
    for field_name, field_info in schema.get('properties', {}).items():
        if 'description' in field_info:
            print(f"{field_name}: {field_info['description']}") 