# Import functions from task_manager.task_utils package
from task_utils import task_utils

# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input ("Enter task title : ")
            description = input ("Enter task description: ")
            due_date = input ("Enter due date (YYYY-MM-DD): ")
            task_utils.add_task("tasks", title, description, due_date)
        elif choice == "2":
            title = input ("Enter task title to mark as complete: ")
            task_utils.mark_task_as_complete('tasks',title)
        elif choice == "3":
            task_utils.view_pending_tasks('tasks')
        elif choice =="4":
            progress = task_utils.calculate_progress('tasks')
            print(f"progress: {progress:.2f}% tasks completed.")
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
