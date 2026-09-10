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
    for index, task in enumerate(tasks, start=1): #enumerate() lets us get two things at the same time:
        print(f"{index}. {task.strip()}")

def delete_task():
    with open("tasks.txt","r") as file:
        tasks = file.readlines()

    print(tasks)
    
    try:
        task_number=int(input("Enter the task number to delete: "))

    #remove tasks
        tasks.pop(task_number-1)

    #write the updated list
        with open("tasks.txt","w") as file:
            file.writelines(tasks)
    
        print("Task deleted successfully")

    except ValueError:
        print("Please enter a valid number. ")

    except IndexError:
        print("Task number does not exist. ")
