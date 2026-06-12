"""
Task Utilities Module
Functions for managing tasks including adding, completing, viewing, and progress tracking.
"""

from typing import List, Dict, Any, Optional
from .validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date,
    get_validated_string,
    get_validated_integer
)

# Global database to store tasks
tasks_db: List[Dict[str, Any]] = []


def add_task(title: Optional[str] = None, description: Optional[str] = None, due_date: Optional[str] = None) -> Dict[str, Any]:
    """
    Creates a new task with validated input and adds it to the database.
    
    Can be called programmatically with parameters or interactively (prompts user).
    
    Args:
        title (str, optional): Task title. If None, prompts user for input.
        description (str, optional): Task description. If None, prompts user for input.
        due_date (str, optional): Task due date. If None, prompts user for input.
    
    Each task is stored as a dictionary with:
    - id: Unique identifier (auto-incremented)
    - title: Task title
    - description: Task description
    - due_date: Due date in YYYY-MM-DD format
    - completed: Boolean completion status
    
    Returns:
        Dict[str, Any]: The newly created task dictionary
        
    Raises:
        ValueError: If validation fails
    """
    print("\n--- Add New Task ---")
    
    # Get and validate title
    if title is None:
        title = get_validated_string(
            "Enter task title: ",
            validate_task_title
        )
    else:
        validate_task_title(title)
        title = title.strip()
    
    # Get and validate description
    if description is None:
        description = get_validated_string(
            "Enter task description: ",
            validate_task_description
        )
    else:
        validate_task_description(description)
        description = description.strip()
    
    # Get and validate due date
    if due_date is None:
        due_date = get_validated_string(
            "Enter due date (YYYY-MM-DD): ",
            validate_due_date
        )
    else:
        validate_due_date(due_date)
        due_date = due_date.strip()
    
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
    return new_task


def mark_task_as_complete(task_id: Optional[int] = None) -> Optional[Dict[str, Any]]:
    """
    Marks an existing pending task as completed using its unique ID.
    
    Can be called programmatically with task_id or interactively (prompts user).
    
    Args:
        task_id (int, optional): The ID of the task to complete. If None, prompts user.
    
    Returns:
        Dict[str, Any]: The completed task dictionary, or None if task not found/error
        
    Raises:
        ValueError: If task_id is invalid
    """
    print("\n--- Complete a Task ---")
    pending = [task for task in tasks_db if not task["completed"]]
    
    if not pending:
        print("❌ There are no pending tasks to complete.")
        return None
    
    view_pending_tasks()
    
    if task_id is None:
        task_id = get_validated_integer("Enter the ID of the task to complete: ")
    
    # Search for the task matching the provided ID
    for task in tasks_db:
        if task["id"] == task_id:
            if task["completed"]:
                print("ℹ️ That task is already marked as complete.")
                return None
            task["completed"] = True
            print(f"✅ Success: Task #{task_id} ('{task['title']}') marked complete!")
            return task
    
    print(f"❌ Error: Task with ID #{task_id} does not exist.")
    return None


def view_pending_tasks(display: bool = True) -> List[Dict[str, Any]]:
    """
    Filters and returns all tasks where 'completed' is False.
    Optionally displays the pending tasks.
    
    Args:
        display (bool): Whether to print the pending tasks. Default is True.
    
    Shows task information in a formatted list including:
    - Task ID
    - Title
    - Description
    - Due date
    
    Returns:
        List[Dict[str, Any]]: List of pending task dictionaries
    """
    if display:
        print("\n--- Pending Tasks ---")
    
    pending = [task for task in tasks_db if not task["completed"]]
    
    if not pending:
        if display:
            print("🎉 No pending tasks found! You are all caught up.")
        return pending
    
    if display:
        for task in pending:
            print(f"[{task['id']}] {task['title']} (Due: {task['due_date']})")
            print(f"    Description: {task['description']}\n")
    
    return pending


def calculate_progress(display: bool = True) -> Dict[str, Any]:
    """
    Calculates task completion metrics and progress tracking.
    Optionally displays the metrics.
    
    Args:
        display (bool): Whether to print the progress metrics. Default is True.
    
    Returns:
        Dict[str, Any]: Dictionary containing:
            - total_tasks: Total number of registered tasks
            - completed_tasks: Number of completed tasks
            - remaining_tasks: Number of remaining tasks
            - completion_rate: Overall completion rate as a percentage
    """
    if display:
        print("\n--- Productivity Progress Metrics ---")
    
    total_tasks = len(tasks_db)
    
    if total_tasks == 0:
        if display:
            print("📊 Metrics: No tasks logged yet. Current completion: 0.0%")
        return {
            "total_tasks": 0,
            "completed_tasks": 0,
            "remaining_tasks": 0,
            "completion_rate": 0.0
        }
    
    completed_tasks = sum(1 for task in tasks_db if task["completed"])
    remaining_tasks = total_tasks - completed_tasks
    completion_rate = (completed_tasks / total_tasks) * 100
    
    if display:
        print(f"🔹 Total Registered Tasks: {total_tasks}")
        print(f"🔹 Completed Tasks: {completed_tasks}")
        print(f"🔹 Remaining Tasks: {remaining_tasks}")
        print(f"📊 Progress Bar: [{chr(9632) * (completed_tasks)} {chr(9633) * (remaining_tasks)}]")
        print(f"📈 Overall Completion Rate: {completion_rate:.1f}%")
    
    return {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "remaining_tasks": remaining_tasks,
        "completion_rate": completion_rate
    }



def get_tasks_db() -> List[Dict[str, Any]]:
    """
    Returns the task database.
    
    Returns:
        List[Dict[str, Any]]: The current tasks database
    """
    return tasks_db
