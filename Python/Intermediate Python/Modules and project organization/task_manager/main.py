from tasks import add_task,view_tasks,delete_task

def show_menu():
    print("\n =================TASK MANAGER=================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

while True:
    show_menu()

    choice=input("Choose an option: ")
    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")