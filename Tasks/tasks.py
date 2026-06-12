"""
Task Management System
A modular productivity application with full input validation and progress tracking.
"""

# Global data structure to hold our tasks
tasks_db = []


def validate_string(prompt: str) -> str:
    """Ensures user input is non-empty and stripped of extra spaces."""
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("❌ Error: Input cannot be blank. Please try again.")


def validate_integer(prompt: str, min_val: int = None, max_val: int = None) -> int:
    """Validates that user input is a valid integer within an optional range."""
    while True:
        try:
            val = int(input(prompt).strip())
            if min_val is not None and val < min_val:
                print(f"❌ Error: Value must be at least {min_val}.")
                continue
            if max_val is not None and val > max_val:
                print(f"❌ Error: Value cannot exceed {max_val}.")
                continue
            return val
        except ValueError:
            print("❌ Error: Please enter a valid whole number.")


def add_task() -> None:
    """Asks for task details, validates input, and appends it to the database."""
    print("\n--- Add New Task ---")
    title = validate_string("Enter task title: ")
    description = validate_string("Enter task description: ")
    
    # Generate unique ID based on length or sequential numbers
    task_id = len(tasks_db) + 1
    
    # Task stored strictly as a dictionary record
    new_task = {
        "id": task_id,
        "title": title,
        "description": description,
        "completed": False
    }
    
    tasks_db.append(new_task)
    print(f"✅ Success: Task '{title}' added successfully with ID #{task_id}.")


def view_pending_tasks() -> None:
    """Filters and displays only tasks where 'completed' is False."""
    print("\n--- Pending Tasks ---")
    pending = [task for task in tasks_db if not task["completed"]]
    
    if not pending:
        print("🎉 No pending tasks found! You are all caught up.")
        return
        
    for task in pending:
        print(f"[{task['id']}] {task['title']}")
        print(f"    Description: {task['description']}\n")


def mark_task_complete() -> None:
    """Marks an existing pending task as completed using its unique ID."""
    print("\n--- Complete a Task ---")
    pending = [task for task in tasks_db if not task["completed"]]
    
    if not pending:
        print("❌ There are no pending tasks to complete.")
        return
        
    view_pending_tasks()
    task_id = validate_integer("Enter the ID of the task to complete: ")
    
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


def track_progress() -> None:
    """Calculates and displays metrics regarding total productivity completion rates."""
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


def display_menu() -> None:
    """Renders the main system dashboard menu loops."""
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
        
        choice = validate_integer("Select an option (1-5): ", min_val=1, max_val=5)
        
        if choice == 1:
            add_task()
        elif choice == 2:
            view_pending_tasks()
        elif choice == 3:
            mark_task_complete()
        elif choice == 4:
            track_progress()
        elif choice == 5:
            print("\n👋 Exiting system. Keep up the productive momentum!")
            break


if __name__ == "__main__":
    display_menu()
