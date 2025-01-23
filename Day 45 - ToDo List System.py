import time, os

toDoList = {"Task" : None, "Deadline" : None, "Priority" : None}
to_do_list = []

def mainMenu():
    print("ToDo List Management System")
    print()
    print("1: Add\n2: View\n3: Edit\n4: Remove\n5: End")
    print()

def addAction():
    print("Add")
    print()
    task_name = input("What do you want to add?\n").strip().capitalize()
    
def viewAction():
    print("View")
    print()
    print(f"{'Task':<20}{'Deadline':<15}{'Priority':<10}") #Header for the elements of the dictionary
    print("-" * 45)
    for task in to_do_list: #Runs each line of the list
    #Prints the elements of the dictionary in a human-readable way.
        print(f"{task['Task']:<20}{task['Deadline']:<15}{task['Priority']:<10}")
    print()

def addDeadlinePriority():
    deadline = input("When do you need it done?\n").strip()
    priority = input("From 1-3, which is the priority of this task?\n").strip() # Prompts for the task to be added to the list.
            
    to_do_list.append({"Task":task_name, "Deadline":deadline, "Priority":priority})

def retryOption():
    print()
    print("Sorry, the task is already in the list.")
    retryOption = input("Do you want to add another task? (yes/no)\n").strip().lower() # If the user still wants to add a new task to the list           

while True:
    mainMenu()
    userAction = input("> ")

    if userAction == "1": #Add a new task
        print("Add")
        print()
        task_name = input("What do you want to add?\n").strip().capitalize()
        
        if any(existing_task["Task"] == task_name for existing_task in to_do_list): # Check if the task already exists in the list
            retryOption() # If the user still wants to add a new task to the list
            
            if retryOption == "yes":
                addAction() #Returns to the Add menu.
            else:
                continue # Restarts the program.

        else:
            deadline = input("When do you need it done?\n").strip()
            priority = input("From 1-3, which is the priority of this task?\n").strip() # Prompts for the task to be added to the list.
            
            to_do_list.append({"Task":task_name, "Deadline":deadline, "Priority":priority})
        print()
        
    elif userAction == "2": #View the list of tasks
        viewAction()
        #time.sleep(2)
    
    elif userAction == "3":
        print("Edit")
        print()
        old_task = input("What do you want to edit?\n").strip().capitalize()
        removed = next((listIndex for listIndex, task in enumerate(to_do_list) if task["Task"] == old_task), None) # Checks the position of the task to be removed. None is returned if the task is not in the list.

#Rerwite the View feature from here:
        if any(existing_task["Task"] == old_task for existing_task in to_do_list):
             # Checks the position of the task to be removed.
            to_do_list.pop(removed) # Removes the task from the list.
            new_task = input("What will be the new task?\n")
            if new_task in to_do_list: # Checks if the task already exists in the list.
                retryOption()
                if retryOption == "yes":
                    new_task = input("What do you want to add?\n")
                    addDeadlinePriority() # Adds the new task to the place of the removed task.
                else:
                    continue
            else:
                addDeadlinePriority() # Adds the new task to the place of the removed task.
            print()
        else:
            print(f"Sorry, {old_task} is not in the list.")
            retryRemoveOption = input("Do you want to edit another task? yes/no\n").strip().lower()
            if retryRemoveOption == "yes":
                old_task = input("What do you want to edit?\n")
                removed = to_do_list.index(old_task) # Checks the position of the task to be removed.
                to_do_list.pop(removed) # Removes the task from the list.
                new_task = input("What will be the new task?\n")
                if new_task in to_do_list: # Checks if the task already exists in the list.
                    retryOption()
                    if retryOption == "yes":
                        new_task = input("What do you want to add?\n")
                        addDeadlinePriority() # Adds the new task to the place of the removed task. # Adds the new task to the place of the removed task.
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
                toDoList.pop(task) #Removes the key-value inputed. Prompted by the key's name. Not what I want.
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
    
    toDoList["Task"] = task_name
    toDoList["Deadline"] = deadline
    toDoList["Priority"] = priority
    
    time.sleep(0.5)
    os.system("clear")
