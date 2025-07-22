#ToDo_App.py

import csv
TODO_FILE = "todo.txt"

def load_tasks():
    try:
        with open(TODO_FILE, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return[]

def save_tasks(tasks):
    with open(TODO_FILE,'w') as file:
        for task in tasks:
            file.write(task+'\n')

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append("[ ]" +task)
    print("Task added.")

def view_tasks(tasks):
    if not tasks:
        print("no task available.")
    else:
        for i, task in enumerate(tasks , start=1):
            print(f"{i}. {task}")

def mark_task_done(tasks):
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to mark as done: "))
        if 1 <= choice <= len(tasks):
            if tasks[choice - 1].startswith("[ ]"):
                tasks[choice - 1] = tasks[choice -1]. replace("[]", "[x]",1)
                print(" Task maeked as completed")
            else:
                print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to delete: "))
        if 1<= choice <=len(tasks):
            removed = tasks.pop(choice -1)
            print(f"Removed:{removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def export_to_csv(tasks):
    with open('todo_export.csv','w', newline='',encoding= 'utf-8') as file:
        writter = csv.writer(file)
        writter.writerow(['Task No' , 'Status' , 'Task'])
        for i , task in enumerate(tasks, start=1):
            status = 'Completed' if '[x]' in task else 'pending'
            description = task [4:].strip() # Remove "[ ]" or "[x]"
            writter.writerow([i, status, description])
    print("Tasks exported to todo_export.csv")

def main():
    tasks = load_tasks()

    while True:
        print("\n To - Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        print("6. Export to CSV")

        choice = input("choose an option (1-6): ")

        if choice == '1':
            add_task(tasks)
        elif choice =='2':
            view_tasks(tasks)
        elif choice =='3':
            mark_task_done(tasks)
        elif choice =='4':
            delete_task(tasks)
        elif choice=='5':
            save_tasks(tasks)
            print("Tasks saved. GoodBye!")
            break
        elif choice =='6':
            export_to_csv(tasks)
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
