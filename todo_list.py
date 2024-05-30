class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = "Completed" if task['completed'] else "Not Completed"
                print(f"{idx}. {task['name']} - {status}")

    def add_task(self, task_name):
        self.tasks.append({"name": task_name, "completed": False})
        print(f"Task '{task_name}' has been added.")

    def mark_task_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]['completed'] = True
            print(f"Task '{self.tasks[task_number - 1]['name']}' has been marked as completed.")
        else:
            print("Invalid task number.")

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['name']}' has been removed.")
        else:
            print("Invalid task number.")

def main():
    to_do_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Display To-Do List")
        print("2. Add a Task")
        print("3. Mark a Task as Completed")
        print("4. Remove a Task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            to_do_list.display_tasks()
        elif choice == '2':
            task_name = input("Enter the task name: ")
            to_do_list.add_task(task_name)
        elif choice == '3':
            to_do_list.display_tasks()
            try:
                task_number = int(input("Enter the task number to mark as completed: "))
                to_do_list.mark_task_completed(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            to_do_list.display_tasks()
            try:
                task_number = int(input("Enter the task number to remove: "))
                to_do_list.remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
