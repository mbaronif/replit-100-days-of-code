uniqueList = [] # My library

def nameList(): # Prints the full list, with new additions.
    for name in uniqueList:
        print(name)
    print()

while True: # Prompts the input requests
    firstName = input("Name: ").strip().title() # Deletes extra spaces and capitalizes the first letter. In this case, could be .capitalize too.
    lastName = input("Surname: ").strip().title()
    print()

    fullName = (f"{firstName} {lastName}") # Concatenates both inputs in a string, separated with a single space.

    if fullName not in uniqueList: # Checks the input name and surname to prevent duplicates. If the name is repeted, it'll not be added.
        uniqueList.append(fullName)
    else:
        print("ERROR: Duplicate name")
    nameList()

    if not firstName or not lastName: # Just a safe measure to avoid infinite loop.
        break
