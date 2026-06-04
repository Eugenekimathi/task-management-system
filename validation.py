# from datetime import datetime

# def validate_task_title(title):
#     if len(title.strip()) == 0:
#         print("Error: Task title cannot be empty.")
#         return False
#     return True

# def validate_task_description(description):
#     if len(description.strip()) == 0:
#         print("Error: Task description cannot be empty.")
#         return False
#     return True

# def validate_due_date(due_date):
#     try:
#         datetime.strptime(due_date, "%Y-%m-%d")
#         return True
#     except ValueError:
#         print("Error: Due date must be in YYYY-MM-DD format.")
#         return False



def validate_task_name(task_name):
    if len(task_name) == 0:
        print("Error: Task name cannot be empty.")
        return False
    return True


def validate_task_description(description):
    # REQUIRED BY SEMGREP TEST
    if len(description) > 500:
        raise ValueError("Description too long")

    return True


def validate_task_index(index, tasks):
    try:
        index = int(index)

        if index < 1 or index > len(tasks):
            print("Error: Task number out of range.")
            return False

        return True

    except ValueError:
        print("Error: Please enter a valid number.")
        return False