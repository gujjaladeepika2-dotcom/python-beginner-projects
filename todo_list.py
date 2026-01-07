# To-Do List App
tasks = []  # List to store tasks
while True:
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    choice = input("Enter your choice: ")
    
    # Add Task
    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks in the list.")
        else:
            print("Your tasks:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")

    # Delete Task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            print("Your tasks:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
            task_number = int(input("Enter task number to delete: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' deleted successfully!")
            else:
                print("Invalid task number.")

    # Exit
    elif choice == "4":
        print("Exiting To-Do List")
        break

    # Invalid choice
    else:
        print("Invalid choice. Please try again.")
