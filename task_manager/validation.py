"""
Validation Module
Input validation functions for task details including title, description, and due date.
"""

from datetime import datetime


def validate_task_title(title: str) -> bool:
    """
    Validates task title.
    
    Requirements:
    - Must be non-empty after stripping whitespace
    - Must be between 3 and 100 characters
    - Cannot be only special characters
    
    Args:
        title (str): The task title to validate
        
    Returns:
        bool: True if valid, raises ValueError with descriptive message otherwise
        
    Raises:
        ValueError: If title does not meet validation criteria
    """
    if not title or not title.strip():
        raise ValueError("❌ Error: Task title cannot be blank.")
    
    title = title.strip()
    
    if len(title) < 3:
        raise ValueError("❌ Error: Task title must be at least 3 characters long.")
    
    if len(title) > 100:
        raise ValueError("❌ Error: Task title cannot exceed 100 characters.")
    
    if not any(char.isalnum() for char in title):
        raise ValueError("❌ Error: Task title must contain at least one alphanumeric character.")
    
    return True


def validate_task_description(description: str) -> bool:
    """
    Validates task description.
    
    Requirements:
    - Must be non-empty after stripping whitespace
    - Must be between 5 and 500 characters
    - Cannot be only special characters
    
    Args:
        description (str): The task description to validate
        
    Returns:
        bool: True if valid, raises ValueError with descriptive message otherwise
        
    Raises:
        ValueError: If description does not meet validation criteria
    """
    if not description or not description.strip():
        raise ValueError("❌ Error: Task description cannot be blank.")
    
    description = description.strip()
    
    if len(description) < 5:
        raise ValueError("❌ Error: Task description must be at least 5 characters long.")
    
    if len(description) > 500:
        raise ValueError("❌ Error: Task description cannot exceed 500 characters.")
    
    if not any(char.isalnum() for char in description):
        raise ValueError("❌ Error: Task description must contain at least one alphanumeric character.")
    
    return True


def validate_due_date(due_date: str) -> bool:
    """
    Validates task due date.
    
    Requirements:
    - Must be in YYYY-MM-DD format
    - Must be a valid calendar date
    
    Args:
        due_date (str): The due date to validate in YYYY-MM-DD format
        
    Returns:
        bool: True if valid, raises ValueError with descriptive message otherwise
        
    Raises:
        ValueError: If due date does not meet validation criteria
    """
    if not due_date or not due_date.strip():
        raise ValueError("❌ Error: Due date cannot be blank.")
    
    due_date = due_date.strip()
    
    try:
        due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("❌ Error: Invalid date format. Please use YYYY-MM-DD (e.g., 2024-06-26).")
    
    return True


def get_validated_string(prompt: str, validator_func, min_length: int = 0) -> str:
    """
    Gets and validates string input from user with retry loop.
    
    Args:
        prompt (str): The input prompt to display
        validator_func: The validation function to apply
        min_length (int): Minimum string length (legacy parameter, validator handles it)
        
    Returns:
        str: Validated user input
        
    Raises:
        ValueError: If validation fails and input is exhausted
    """
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        try:
            user_input = input(prompt).strip()
            validator_func(user_input)
            return user_input
        except ValueError as e:
            print(str(e))
            attempts += 1
        except EOFError:
            raise ValueError("Input stream exhausted. Unable to get valid input.")
    
    raise ValueError(f"Failed to get valid input after {max_attempts} attempts")


def get_validated_integer(prompt: str, min_val: int = None, max_val: int = None) -> int:
    """
    Gets and validates integer input from user with retry loop.
    
    Args:
        prompt (str): The input prompt to display
        min_val (int): Minimum allowed value (optional)
        max_val (int): Maximum allowed value (optional)
        
    Returns:
        int: Validated integer input
    """
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        try:
            val = int(input(prompt).strip())
            if min_val is not None and val < min_val:
                print(f"❌ Error: Value must be at least {min_val}.")
                attempts += 1
                continue
            if max_val is not None and val > max_val:
                print(f"❌ Error: Value cannot exceed {max_val}.")
                attempts += 1
                continue
            return val
        except ValueError:
            print("❌ Error: Please enter a valid whole number.")
            attempts += 1
        except EOFError:
            raise ValueError("Input stream exhausted. Unable to get valid input.")
    
    raise ValueError(f"Failed to get valid integer after {max_attempts} attempts")
