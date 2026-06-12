"""
Task Management System - Main Script
A menu-based interface for interacting with the modular task management system.

This script imports and uses functions from the task_manager package to provide
a user-friendly interface for managing tasks and tracking productivity.
"""

from task_manager import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress
)
from task_manager.validation import get_validated_integer


def display_menu() -> None:
    """
    Displays the main menu and handles user interactions.
    
    Presents a menu with 5 options:
    1. Add a Task
    2. View Pending Tasks
    3. Mark Task as Complete
    4. Track Productivity Progress
    5. Exit Application
    
    Loops continuously until user selects exit option.
    
    Returns:
        None
    """
    while True:
        print("\n==============================")
        print("    TASK MANAGEMENT SYSTEM    ")
        print("==============================")
        print("1. Add a Task")
        print("2. View Pending Tasks")
        print("3. Mark Task as Complete")
        print("4. Track Productivity Progress")
        print("5. Exit Application")
        print("==============================")
        
        choice = get_validated_integer("Select an option (1-5): ", min_val=1, max_val=5)
        
        if choice == 1:
            add_task()
        elif choice == 2:
            view_pending_tasks()
        elif choice == 3:
            mark_task_as_complete()
        elif choice == 4:
            calculate_progress()
        elif choice == 5:
            print("\n👋 Exiting system. Keep up the productive momentum!")
            break


if __name__ == "__main__":
    display_menu()
