import json
from datetime import date

# Task class to handle task properties
class Task:
    def _init_(self, title, priority, due_date):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.is_done = False

    def complete_task(self):
        self.is_done = True

# ToDoList class to manage a collection of tasks
class ToDoList:
    def _init_(self):
        self.task_list = []

    def add_new_task(self, title, priority, due_date):
        task = Task(title, priority, due_date)
        self.task_list.append(task)
        print(f"Task '{title}' added successfully!")

    def delete_task(self, title):
        self.task_list = [task for task in self.task_list if task.title != title]
        print(f"Task '{title}' removed successfully!")

    def complete_a_task(self, title):
        for task in self.task_list:
            if task.title == title:
                task.complete_task()
                print(f"Task '{title}' marked as complete!")

    def display_tasks(self):
        print("\nYour To-Do List:")
        for task in self.task_list:
            status = 'Done' if task.is_done else 'Not Done'
            print(f"- {task.title} (Priority: {task.priority}, Due: {task.due_date}) - {status}")

    def save_to_file(self):
        with open('my_tasks.json', 'w') as file:
            json.dump([vars(task) for task in self.task_list], file)
        print("Tasks saved to 'my_tasks.json'.")

    def load_from_file(self):
        try:
            with open('my_tasks.json', 'r') as file:
                tasks_data = json.load(file)
                for data in tasks_data:
                    self.task_list.append(Task(**data))
            print("Tasks loaded successfully!")
        except FileNotFoundError:
            print("No saved tasks found. Starting fresh!")

# Main function to run the to-do list app
def main():
    my_todo_list = ToDoList()
    my_todo_list.load_from_file()

    actions = {
        '1': my_todo_list.add_new_task,
        '2': my_todo_list.delete_task,
        '3': my_todo_list.complete_a_task,
        '4': my_todo_list.display_tasks
    }

    while True:
        print("\n-- My To-Do List App --")
        print("1: Add a Task")
        print("2: Remove a Task")
        print("3: Mark a Task as Done")
        print("4: Show all Tasks")
        print("5: Exit")
        user_choice = input("What would you like to do? ")

        if user_choice in actions:
            if user_choice == '4':
                actionsuser_choice
            else:
                task_title = input("Task Title: ")
                if user_choice == '1':
                    task_priority = input("Task Priority (high, medium, low): ")
                    task_due_date = input("Due Date (YYYY-MM-DD): ")
                    actionsuser_choice
                else:
                    actionsuser_choice
        elif user_choice == '5':
            my_todo_list.save_to_file()
            print("Goodbye!")
            break
        else:
            print("Oops! That's not a valid option. Try again.")

if _name_ == "_main_":
    main()