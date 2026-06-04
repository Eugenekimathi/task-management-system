# # Import functions from task_manager.task_utils package

# from task_utils import (
#     add_task,
#     mark_task_as_complete,
#     view_pending_tasks,
#     calculate_progress,
#     tasks
# )

# # Define the main function
# def main():
#     while True:
#         print("\nTask Management System")
#         print("1. Add Task")
#         print("2. Mark Task as Complete")
#         print("3. View Pending Tasks")
#         print("4. View Progress")
#         print("5. Exit")

#         choice = input("Enter your choice (1-5): ")

#         if choice == "1":
#             title = input("Enter task title: ")
#             description = input("Enter task description: ")
#             due_date = input("Enter due date (YYYY-MM-DD): ")

#             add_task(title, description, due_date)

#         elif choice == "2":
#             if len(tasks) == 0:
#                 print("No tasks available.")
#             else:
#                 print("\nTasks:")

#                 for index, task in enumerate(tasks):
#                     status = "Completed" if task["completed"] else "Pending"
#                     print(f"{index}. {task['title']} - {status}")

#                 try:
#                     task_index = int(
#                         input("Enter task index to mark as complete: ")
#                     )
#                     mark_task_as_complete(task_index)

#                 except ValueError:
#                     print("Please enter a valid number.")

#         elif choice == "3":
#             view_pending_tasks()

#         elif choice == "4":
#             progress = calculate_progress()
#             print(f"Progress: {progress:.2f}%")

#         elif choice == "5":
#             print("Exiting the program...")
#             break

#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()





from task_utils import (
    add_task,
    mark_task_complete,
    view_tasks,
    view_pending_tasks,
    calculate_progress
)

tasks = []


def display_menu():
    print("\n===== TASK MANAGER =====")
    print("1. Add Task")
    print("2. Mark Task Complete")
    print("3. View All Tasks")
    print("4. View Pending Tasks")
    print("5. Track Progress")
    print("6. Exit")


while True:
    display_menu()

    try:
        choice = input("Enter your choice: ")
    except EOFError:
        break

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        mark_task_complete(tasks)

    elif choice == "3":
        view_tasks(tasks)

    elif choice == "4":
        view_pending_tasks(tasks)

    elif choice == "5":
        print(calculate_progress(tasks))

    elif choice == "6":
        print("Exiting Task Manager...")
        break

    else:
        print("Invalid choice. Please try again.")