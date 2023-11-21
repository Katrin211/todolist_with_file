# todolist_with_file.py

def show_menu():
    print("\n===== To-Do List Menu =====")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Save To-Do List to File")
    print("5. Load To-Do List from File")
    print("6. Quit")


def view_to_do_list():
    print("\n===== To-Do List =====")

    # Display incomplete tasks
    if not to_do_list:
        print("No tasks.")
    else:
        print("Incomplete tasks:")
        for index, task in enumerate(to_do_list, 1):
            print(f"{index}. {task}")

    # Display completed tasks
    if completed_tasks:
        print("\nCompleted tasks:")
        for index, task in enumerate(completed_tasks, 1):
            print(f"{index}. {task}")


def add_task():
    task = input("Enter the task: ")
    to_do_list.append(task)
    print("Task added!")


def mark_task_completed():
    if not to_do_list:
        print("No tasks to mark as completed.")
    else:
        view_to_do_list()
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_index < len(to_do_list):
            completed_task = to_do_list.pop(task_index)
            completed_tasks.append(completed_task)
            print(f"Task '{completed_task}' marked as completed!")

            # Save the updated to-do list to the file
            save_to_file()
        else:
            print("Invalid task number.")


# Function to save the To-Do List to a file
def save_to_file():
    with open("to_do_list.txt", "w") as file:
        for task in to_do_list:
            file.write(task + "\n")
    print("To-Do List saved to 'to_do_list.txt'.")


# Function to load the To-Do List from a file
def load_from_file():
    global to_do_list
    to_do_list = []  # Clear the current to-do list
    try:
        with open("to_do_list.txt", "r") as file:
            for line in file:
                to_do_list.append(line.strip())
        print("To-Do List loaded from 'to_do_list.txt'.")
        view_to_do_list()  # Print the loaded tasks
    except FileNotFoundError:
        print("No saved To-Do List found.")


# Initialize the To-Do List and completed tasks
to_do_list = []
completed_tasks = []

# Load tasks from the file at the beginning
load_from_file()

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    # Process user input
    if choice == "1":
        view_to_do_list()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_task_completed()
    elif choice == "4":
        save_to_file()
    elif choice == "5":
        load_from_file()
    elif choice == "6":
        print("Exiting the To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
