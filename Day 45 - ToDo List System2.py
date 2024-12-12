import time, os

toDoList = {"Task" : None, "Deadline" : None, "Priority" : None}

def prettyPrint():
    print("ToDo List Management System")
    print()
    print("1: Add\n2: View\n3: Edit\n4: Remove\n5: End")
    print()

def printList():
    for task in toDoList:
        print(task)
    print()

def addTask():
    task = input("What do you want to add?\n")
    deadline = input("When do you need it done?\n")
    priority = input("From 1-3, which is the priority of this task?\n") # Prompts for the task to be added to the list.
    toDoList.update({"Task":task.capitalize(), "Deadline":deadline, "Priority":priority})

while True:
    prettyPrint()
    userAction = input("> ")

    

    if userAction == "1":
        print("Add")
        print()
        task = input("What do you want to add?\n")
        if task in toDoList: # Checks if the task already exists in the list.
            print()
            print("Sorry, the task is already in the list.")
            retryOption = input("Do you want to add another task?\n") # In case the user still wants to add a new task to the list.
            if retryOption.strip().lower() == "yes":
                task = input("What do you want to add?\n")
                deadline = input("When do you need it done?\n")
                priority = input("From 1-3, which is the priority of this task?\n") # Prompts for the task to be added to the list.
                toDoList.update({"Task":task.capitalize(), "Deadline":deadline, "Priority":priority})
            else:
                continue # Restarts the program.
        else:
            task = input("What do you want to add?\n")
            deadline = input("When do you need it done?\n")
            priority = input("From 1-3, which is the priority of this task?\n") # Prompts for the task to be added to the list.
            toDoList.update({"Task":task.capitalize(), "Deadline":deadline, "Priority":priority})
        print()
        
    elif userAction == "2":
        print("View")
        print()
        print(toDoList)
        #printList()
        #time.sleep(2)
    
    elif userAction == "3":
        print("Edit")
        print()
        task = input("What do you want to edit?\n")
        if task in toDoList:
            removed = toDoList.index(task) # Checks the position of the task to be removed.
            toDoList.remove(task) # Removes the task from the list.
            task = input("What will be the new task?\n")
            if task in toDoList: # Checks if the task already exists in the list.
                print()
                print("Sorry, the task is already in the list.")
                retryOption = input("Do you want to add another task?\n") # In case the user still wants to add a new task to the list.
                if retryOption.strip().lower() == "yes":
                    task = input("What do you want to add?\n")
                    toDoList.insert(removed, task.capitalize()) # Adds the new task to the place of the removed task.
                else:
                    continue
            else:
                toDoList.insert(removed, task.capitalize()) # Adds the new task to the place of the removed task.
            print()
        else:
            print(f"Sorry, {task} is not in the list.")
            retryRemoveOption = input("Do you want to edit another task?\n")
            if retryRemoveOption.strip().lower() == "yes":
                task = input("What do you want to edit?\n")
                removed = toDoList.index(task) # Checks the position of the task to be removed.
                toDoList.remove(task) # Removes the task from the list.
                task = input("What will be the new task?\n")
                if task in toDoList: # Checks if the task already exists in the list.
                    print()
                    print("Sorry, the task is already in the list.")
                    retryOption = input("Do you want to add another task?\n") # In case the user still wants to add a new task to the list.
                    if retryOption.strip().lower() == "yes":
                        task = input("What do you want to add?\n")
                        toDoList.insert(removed, task.capitalize()) # Adds the new task to the place of the removed task.
                    else:
                        continue
            else:
                continue # Restarts the program.
    elif userAction == "4":
        print("Remove")
        print()
        task = input("What do you want to remove?\n")
        if task in toDoList: # Checks if the task exists in the list.
            doubleCheck = input(f"Are you sure you want to remove {task}?\n") # Confirmation of removal
            if doubleCheck.strip().lower() == "yes":
                toDoList.remove(task)
                print()
                print(f"{task} was removed from the list.")
            else:
                continue # Restarts the program.
        else:
            print(f"{task} is not in the list.\n")
            print()
    else:
        print("Thanks for using the ToDo List Management System")
        break
    
    toDoList["Task"] = task
    toDoList["Deadline"] = deadline
    toDoList["Priority"] = priority
    
    time.sleep(0.5)
    #os.system("clear")
