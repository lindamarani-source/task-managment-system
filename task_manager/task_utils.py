"""
Task Utilities Module
Functions for managing tasks including adding, completing, viewing, and progress tracking.
"""

from typing import List, Dict, Any
from .validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date,
    get_validated_string,
    get_validated_integer
)

# Global database to store tasks
tasks_db: List[Dict[str, Any]] = []


def add_task() -> None:
    """
    Creates a new task with validated input and adds it to the database.
    
    Prompts user for:
    - Title (validated via validate_task_title)
    - Description (validated via validate_task_description)
    - Due date (validated via validate_due_date)
    
    Each task is stored as a dictionary with:
    - id: Unique identifier (auto-incremented)
    - title: Task title
    - description: Task description
    - due_date: Due date in YYYY-MM-DD format
    - completed: Boolean completion status
    
    Returns:
        None
    """
    print("\n--- Add New Task ---")
    
    # Get and validate title
    title = get_validated_string(
        "Enter task title: ",
        validate_task_title
    )
    
    # Get and validate description
    description = get_validated_string(
        "Enter task description: ",
        validate_task_description
    )
    
    # Get and validate due date
    due_date = get_validated_string(
        "Enter due date (YYYY-MM-DD): ",
        validate_due_date
    )
    
    # Generate unique task ID
    task_id = len(tasks_db) + 1
    
    # Create task dictionary
    new_task = {
        "id": task_id,
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    
    tasks_db.append(new_task)
    print(f"✅ Success: Task '{title}' added successfully with ID #{task_id}.")


def mark_task_as_complete() -> None:
    """
    Marks an existing pending task as completed using its unique ID.
    
    Shows pending tasks first, then prompts user for task ID to complete.
    Validates that the task exists and is not already completed.
    
    Returns:
        None
    """
    print("\n--- Complete a Task ---")
    pending = [task for task in tasks_db if not task["completed"]]
    
    if not pending:
        print("❌ There are no pending tasks to complete.")
        return
    
    view_pending_tasks()
    task_id = get_validated_integer("Enter the ID of the task to complete: ")
    
    # Search for the task matching the provided ID
    for task in tasks_db:
        if task["id"] == task_id:
            if task["completed"]:
                print("ℹ️ That task is already marked as complete.")
                return
            task["completed"] = True
            print(f"✅ Success: Task #{task_id} ('{task['title']}') marked complete!")
            return
    
    print(f"❌ Error: Task with ID #{task_id} does not exist.")


def view_pending_tasks() -> None:
    """
    Filters and displays all tasks where 'completed' is False.
    
    Shows task information in a formatted list including:
    - Task ID
    - Title
    - Description
    - Due date
    
    Returns:
        None
    """
    print("\n--- Pending Tasks ---")
    pending = [task for task in tasks_db if not task["completed"]]
    
    if not pending:
        print("🎉 No pending tasks found! You are all caught up.")
        return
    
    for task in pending:
        print(f"[{task['id']}] {task['title']} (Due: {task['due_date']})")
        print(f"    Description: {task['description']}\n")


def calculate_progress() -> None:
    """
    Calculates and displays task completion metrics and progress tracking.
    
    Displays:
    - Total number of registered tasks
    - Number of completed tasks
    - Number of remaining tasks
    - Visual progress bar using block characters
    - Overall completion rate as a percentage
    
    Returns:
        None
    """
    print("\n--- Productivity Progress Metrics ---")
    total_tasks = len(tasks_db)
    
    if total_tasks == 0:
        print("📊 Metrics: No tasks logged yet. Current completion: 0.0%")
        return
    
    completed_tasks = sum(1 for task in tasks_db if task["completed"])
    completion_rate = (completed_tasks / total_tasks) * 100
    
    print(f"🔹 Total Registered Tasks: {total_tasks}")
    print(f"🔹 Completed Tasks: {completed_tasks}")
    print(f"🔹 Remaining Tasks: {total_tasks - completed_tasks}")
    print(f"📊 Progress Bar: [{chr(9632) * (completed_tasks)} {chr(9633) * (total_tasks - completed_tasks)}]")
    print(f"📈 Overall Completion Rate: {completion_rate:.1f}%")


def get_tasks_db() -> List[Dict[str, Any]]:
    """
    Returns the task database.
    
    Returns:
        List[Dict[str, Any]]: The current tasks database
    """
    return tasks_db
