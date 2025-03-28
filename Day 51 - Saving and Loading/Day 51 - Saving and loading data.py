import time, os

toDoList = []

f = open("ToDoList.txt", "r")
toDoList = eval(f.read())
f.close()

def printList():
    for item in toDoList:
        print(item)
    print()

while True:
    print("ToDo List Manager")
    print()
    # Added option "remove" and replaced "edit" with "change", which I think makes it clearer.
    menu = input("This is your To Do list. What do you want to do?\n1: view\n2: add\n3: change\n4: remove\n5: clear\n6: exit\n\n> ")
    print()
    if menu == "1":
        printList()
        time.sleep(2)
        os.system("clear")
    elif menu == "2":
        item = input("What do you want to add?\n> ")
        if item in toDoList: # Checks if the item already exists in the list.
            print()
            print("Sorry, the item is already in the list.")
            retryOption = input("Do you want to add another item?\n> ") # In case the user still wants to add a new item to the list.
            if retryOption == "yes":
                item = input("What do you want to add?\n> ") # Prompts for the item to be added to the list.
                toDoList.append(item)
            else:
                continue # Restarts the program.
        else:
            toDoList.append(item)
        time.sleep(1)
        os.system("clear")
        print()
    elif menu == "3":
        item = input("What do you want to change?\n> ")
        if item in toDoList:
            removed = toDoList.index(item) # Checks the position of the item to be removed.
            toDoList.remove(item) # Removes the item from the list.
            item = input("What will be the new item?\n> ")
            if item in toDoList: # Checks if the item already exists in the list.
                print()
                print("Sorry, the item is already in the list.")
                retryOption = input("Do you want to add another item?\n> ") # In case the user still wants to add a new item to the list.
                if retryOption == "yes":
                    item = input("What do you want to add?\n> ")
                    toDoList.insert(removed, item) # Adds the new item to the place of the removed item.
                else:
                    continue
            else:
                toDoList.insert(removed, item) # Adds the new item to the place of the removed item.
            print()           
        else:
            print(f"Sorry, {item} is not in the list.")
            retryRemoveOption = input("Do you want to change another item?\n> ")
            if retryRemoveOption == "yes":
                item = input("What do you want to change?\n> ")
                removed = toDoList.index(item) # Checks the position of the item to be removed.
                toDoList.remove(item) # Removes the item from the list.
                item = input("What will be the new item?\n> ")
                if item in toDoList: # Checks if the item already exists in the list.
                    print()
                    print("Sorry, the item is already in the list.")
                    retryOption = input("Do you want to add another item?\n> ") # In case the user still wants to add a new item to the list.
                    if retryOption == "yes":
                        item = input("What do you want to add?\n> ")
                        toDoList.insert(removed, item) # Adds the new item to the place of the removed item.
                    else:
                        continue
            else:
                continue # Restarts the program.
            time.sleep(1)
            os.system("clear") 
    elif menu == "4":
        item = input("What do you want to remove?\n> ")
        if item in toDoList: # Checks if the item exists in the list.
            doubleCheck = input(f"Are you sure you want to remove {item}?\n> ") # Confirmation of removal
            if doubleCheck == "yes":
                toDoList.remove(item)
                print(f"{item} has been removed from the list.")
                print()
            else:
                continue # Restarts the program.
        else:
            print(f"{item} is not in the ToDo menu:\n")
            print()
        time.sleep(1)
        os.system("clear") 
    elif menu == "5": # Clears the items on the list.
        toDoList.clear()
        print("The list has been cleared.")
        print()
        time.sleep(1)
        os.system("clear") 
    elif menu == "6":
        print("Thanks for using the Todo menu Manager")
        time.sleep(2)
        os.system("clear") 
        break
    else:
        print("Thanks for using the Todo menu Manager")
        time.sleep(2)
        os.system("clear")
        break

f = open("ToDoList.txt", "w")
f.write(str(toDoList))
f.close()
