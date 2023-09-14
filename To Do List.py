tasks = {}
def add_task(task_name, task_description):
    tasks[task_name] = {"description": task_description, "done": False}
    print(f"Task '{task_name}' added!")

def list_tasks():
    if tasks:
        print("\nTo-Do List:")
        for task_name, task_info in tasks.items():
            status = "Done" if task_info["done"] else "Not Done"
            print(f"{task_name} - {task_info['description']} [{status}]")
    else:
        print("\nYour to-do list is empty.")

def update_task(task_name, new_description):
    if task_name in tasks:
        tasks[task_name]["description"] = new_description
        print(f"Task '{task_name}' updated!")
    else:
        print("Task not found.")

def mark_task_done(task_name):
    if task_name in tasks:
        tasks[task_name]["done"] = True
        print(f"Task '{task_name}' marked as done!")
    else:
        print("Task not found.")

def remove_task(task_name):
    if task_name in tasks:
        del tasks[task_name]
        print(f"Task '{task_name}' removed!")
    else:
        print("Task not found.")


while True:
    print("\n---------------|| To-do List Menu ||---------------")
    print("1. Add Task")
    print("2. View Task")
    print("3. Update Task Description")
    print("4. Mark Task as Done")
    print("5. Remove Task")
    print("6. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_name = input("Enter a task name: ")
        task_description = input("Enter a task description: ")
        add_task(task_name, task_description)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        task_name = input("Enter the task name to update: ")
        new_description = input("Enter the new task description: ")
        update_task(task_name, new_description)
    elif choice == "4":
        task_name = input("Enter the task name to mark as done: ")
        mark_task_done(task_name)
    elif choice == "5":
        task_name = input("Enter the task name to remove: ")
        remove_task(task_name)
    elif choice == "6":
        print("THANKS FOR YOUR COOPERATION.")
        break
    else:
        print("Invalid choice. Please try again.")
