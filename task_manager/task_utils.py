# from datetime import datetime

# # Import validation functions
# from task_manager.validation import (
#     validate_task_title,
#     validate_task_description,
#     validate_due_date
# )

# # Define tasks list
# tasks = []

# # Implement add_task function
# def add_task(title, description, due_date):
#     if not validate_task_title(title):
#         return

#     if not validate_task_description(description):
#         return

#     if not validate_due_date(due_date):
#         return

#     task = {
#         "title": title,
#         "description": description,
#         "due_date": due_date,
#         "completed": False
#     }

#     tasks.append(task)
#     print("Task added successfully!")

# # Implement mark_task_as_complete function
# def mark_task_as_complete(index, tasks=tasks):
#     if 0 <= index < len(tasks):
#         tasks[index]["completed"] = True
#         print("Task marked as complete")
#     else:
#         print("Invalid task index")

# # Implement view_pending_tasks function
# def view_pending_tasks(tasks=tasks):
#     pending_found = False

#     for index, task in enumerate(tasks):
#         if not task["completed"]:
#             pending_found = True
#             print(f"\nTask {index}")
#             print(f"Title: {task['title']}")
#             print(f"Description: {task['description']}")
#             print(f"Due Date: {task['due_date']}")

#     if not pending_found:
#         print("No pending tasks.")

# # Implement calculate_progress function
# def calculate_progress(tasks=tasks):
#     if len(tasks) == 0:
#         return 0

#     completed_tasks = 0

#     for task in tasks:
#         if task["completed"]:
#             completed_tasks += 1

#     progress = (completed_tasks / len(tasks)) * 100
#     return progress





tasks = []


def add_task(title, description, due_date):
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")


def mark_task_as_complete(task_index):
    if len(tasks) == 0:
        raise ValueError("No tasks available.")
    if task_index < 0 or task_index >= len(tasks):
        raise ValueError("Invalid task index")
    tasks[task_index]["completed"] = True
    print("Task marked as complete!")


def view_pending_tasks():
    pending = [task for task in tasks if not task["completed"]]
    if len(pending) == 0:
        print("No pending tasks.")
    else:
        for task in pending:
            print(f"{task['title']} - Due: {task['due_date']}")


def calculate_progress():
    if len(tasks) == 0:
        return 0.0
    completed = sum(1 for task in tasks if task["completed"])
    return (completed / len(tasks)) * 100