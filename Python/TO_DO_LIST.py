print("----- TO-DO LIST -----")
print("1.Add Task")
print("2. Mark Task as Completed")
print("3. Delete Task")
print("4. View Tasks")
print("5. Exit")
print()

tasks = []

while True:
    choice = int(input("Enter choice: "))
    match choice:
        case 1:
            task_in = input("Enter task name: ")
            tasks.append({"title": task_in,"done": False})
            print()
            print("Task added.")
            print()
        case 2:
            mark_done = int(input("Enter task number to mark as done: "))
            tasks[mark_done-1]["done"] = True
            print()
            print("Task marked as completed.")
            print()
        case 3:
            dele = int(input("Enter task number to delete: "))
            tasks.pop(dele-1)
            print()
            print("Task deleted.")
            print()
        case 4:
            if not tasks:
                print("No Task")
                print()
            else:
                for t in tasks:
                    print(t["title"],"[DONE]" if t["done"] else "[NOT DONE]")
                print()
        case 5:
            print("Exiting... Bye!")
            break
        case _:
            print("Invalid Input")