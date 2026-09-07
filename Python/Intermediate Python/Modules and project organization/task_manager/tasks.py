def add_task():
    task=input("Enter task: ")

    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

    print("Task added successfully!") 

def view_tasks():
    with open("tasks.txt","r") as file:
        tasks=file.readlines()

    if not tasks:
        print("No tasks found.")
        return

    print("\n============YOUR TASKS===========")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task.strip()}")
