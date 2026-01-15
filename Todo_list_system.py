tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully")

def view_tasks():
    if not tasks:
        print("No tasks available")
    else:
        for index, task in enumerate(tasks, start=1):
            print(index, ".", task)

def main():
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
