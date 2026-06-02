from datetime import datetime

def validate_task_title(title):
    if not title or not isinstance(title, str):
        raise ValueError("Task title must be a non-empty string. ")
    return title
    
def validate_task_description(description):
    if not description or not isinstance(description, str):
        raise ValueError("Task description must be a non-empty string.")
    return description     
    
def validate_due_date(due_date):
    if not due_date or not isinstance (due_date, str):
        raise ValueError("Due date must be a valid string in YYYY-MM-DD format.")