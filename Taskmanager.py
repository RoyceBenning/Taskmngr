# task_manager.py

import os

# List to store tasks
tasks = []

def display_menu():
    """Displays the main menu to the user."""
    print("\nWelcome to Task Manager")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def view_tasks():
    """Displays all the tasks."""
    if tasks:
        print("\nCurrent Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("\nNo tasks available!")

def add_task():
    """Prompts user to add a new task."""
    task = input("\nEnter the task you want to add: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def remove_task():
    """Prompts user to remove an existing task."""
    view_tasks()
    if tasks:
        try:
            task_number = int(input("\nEnter the task number to remove: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' removed successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

def main():
    """Main function to run the task manager."""
    while True:
        display_menu()
        choice = input("\nSelect an option (1-4): ")
        
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("\nExiting Task Manager. Goodbye!")
            break
        else:
            print("\nInvalid option. Please try again.")

if __name__ == "__main__":
    main()
