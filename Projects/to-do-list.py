# 1. Set up an empty to-do list (use a list this time!)
tasks = []  # Step 1: Empty list for tasks

# 2. Define a function to add a task
def add_task(task):
    # Step 2: Append the task to the tasks list
    tasks.append(task)

# 3. Define a function to list all tasks
def list_tasks():
    # Step 3: Print each task, with a number beside it (start at 1)
    # Hint: Use enumerate
    for index, task in enumerate(tasks, 1):
        print(f"{index} {task}")

# 4. Define a function to remove a task by its number
def remove_task(number):
    # Step 4: Remove the task at the given index (number-1)
    # Make sure the number is valid!
    if number > len(tasks):
        print("Not in List")
    else:
        del tasks[number-1]
    

# 5. Main loop: Ask the user what they want to do
while True:

    print("\nTo-Do App - Choose an action:")
    print("1. Add task")
    print("2. List all tasks")
    print("3. Remove a task")
    print("4. Quit")
    choice = input("Enter choice (1-4): ")

    if choice == "1":
        task = input("Enter task description: ")
        # Call add_task here
        add_task(task)

    elif choice == "2":
        # Call list_tasks here
        list_tasks()

    elif choice == "3":
        # Call list_tasks first so they know what to delete
        # Then get the number and call remove_task
        print("=" * 30)
        list_tasks()
        delete_item = int(input("Which item do you want to delete? "))
        remove_task(delete_item)

    elif choice == "4":
        print("Bye, enjoy your productivity!")
        break

    else:
        print("Invalid choice, try again.")

# --- End of Mini-App ---
