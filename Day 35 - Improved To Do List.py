toDoList = []

def printList():
    for item in toDoList:
        print(item)
    print()

while True:
    print("ToDo List Manager")
    print()
    # Added option "remove" and replaced "edit" with "change", which I think makes it clearer.
    menu = input("Do you want to view, add, remove, change, or clear your ToDo list?\n")
    print()
    if menu == "view":
        printList()
    elif menu == "add":
        item = input("What do you want to add?\n")
        if item in toDoList: # Checks if the item already exists in the list.
            print()
            print("Sorry, the item is already in the list.")
            retryOption = input("Do you want to add another item?\n") # In case the user still wants to add a new item to the list.
            if retryOption == "yes":
                item = input("What do you want to add?\n") # Prompts for the item to be added to the list.
                toDoList.append(item)
            else:
                continue # Restarts the program.
        else:
            toDoList.append(item)
        print()
    elif menu == "change":
        item = input("What do you want to change?\n")
        if item in toDoList:
            removed = toDoList.index(item) # Checks the position of the item to be removed.
            toDoList.remove(item) # Removes the item from the list.
            item = input("What will be the new item?\n")
            if item in toDoList: # Checks if the item already exists in the list.
                print()
                print("Sorry, the item is already in the list.")
                retryOption = input("Do you want to add another item?\n") # In case the user still wants to add a new item to the list.
                if retryOption == "yes":
                    item = input("What do you want to add?\n")
                    toDoList.insert(removed, item) # Adds the new item to the place of the removed item.
                else:
                    continue
            else:
                toDoList.insert(removed, item) # Adds the new item to the place of the removed item.
            print()
        else:
            print(f"Sorry, {item} is not in the list.")
            retryRemoveOption = input("Do you want to remove another item?\n")
            if retryRemoveOption == "yes":
                item = input("What do you want to remove?\n")
                removed = toDoList.index(item) # Checks the position of the item to be removed.
                toDoList.remove(item) # Removes the item from the list.
                item = input("What will be the new item?\n")
                if item in toDoList: # Checks if the item already exists in the list.
                    print()
                    print("Sorry, the item is already in the list.")
                    retryOption = input("Do you want to add another item?\n") # In case the user still wants to add a new item to the list.
                    if retryOption == "yes":
                        item = input("What do you want to add?\n")
                        toDoList.insert(removed, item) # Adds the new item to the place of the removed item.
                    else:
                        continue
            else:
                continue # Restarts the program.
    elif menu == "remove":
        item = input("What do you want to remove?\n")
        if item in toDoList: # Checks if the item exists in the list.
            doubleCheck = input(f"Are you sure you want to remove {item}?\n") # Confirmation of removal
            if doubleCheck == "yes":
                toDoList.remove(item)
                print()
            else:
                continue # Restarts the program.
        else:
            print(f"{item} is not in the ToDo menu:\n")
            print()
    elif menu == "clear": # Clears the items on the list.
        toDoList.clear()
        print()
    else:
        print("Thanks for using the Todo menu Manager")
        break
