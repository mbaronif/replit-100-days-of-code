toDoList = []

def printList():
    for item in toDoList:
        print(item)
    print()

while True:
    print("ToDo List Manager")
    print()
    menu = input("Do you want to view, add, or edit your ToDo menu?\n")
    print()
    if menu == "view":
        printList()
    elif menu == "add":
        item = input("What do you want to add?\n")
        toDoList.append(item)
        print()
    elif menu == "edit":
        item = input("What do you want to remove?\n")
        if item in toDoList:
            toDoList.remove(item)
            print()
        else:
            print(f"{item} is not in the ToDo menu:\n")
            print()
    else:
        print("Thanks for using the Todo menu Manager")
        break
