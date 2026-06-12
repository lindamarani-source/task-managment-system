"""
Task Manager Package
A modular task management system with validation and utilities.
"""

from .task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress
from .validation import validate_task_title, validate_task_description, validate_due_date

__all__ = [
    'add_task',
    'mark_task_as_complete',
    'view_pending_tasks',
    'calculate_progress',
    'validate_task_title',
    'validate_task_description',
    'validate_due_date'
]
