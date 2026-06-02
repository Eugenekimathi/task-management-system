from datetime import datetime

# Import validation functions
from validation import validation

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    title = validation.validate_task_title(title)
    description = validation.validate_task_description(description)
    due_date = validation.validate_due_date(due_date)
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print(f"Task '{title}' added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    for task in tasks:
        if task["title"] == "title":
            task["completed"] = True
            print(f"Task '{'title'}' marked as complete.")
            return
    print(f"Task '{'title'}' not found.")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    print ("\nPending Tasks:")
    for task in tasks:
        if not task ["completed"]:
            print(f"-{task['title']}(Due: {task['due_date']})")

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if not tasks:
        return 0
    completed = sum (1 for task in tasks if task ["completed"])
    return progress