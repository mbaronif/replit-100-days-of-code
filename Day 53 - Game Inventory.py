import os, time

gameInventory = []

try:
    f = open("Game_Inventory.txt", "r")
    gameInventory = eval(f.read())
    f.close()

except FileNotFoundError:
    print("\nFile not found. Creating a new file...\n")
    f = open("Game_Inventory.txt", "a+")
    f.close()

def gameMenu():
    print("INVENTORY\n\n==========\n\n")
    print("1: Add\n2: View\n3: Remove\n4: Exit\n\n")

def addItem():
    print("INVENTORY\n\n==========\n\n")
    itemName = input("Item to add > ").capitalize()
    gameInventory.append(itemName)
    print("Item added!\n")
    time.sleep(2)
    os.system("clear")   

def viewItem():
    print("INVENTORY\n\n==========\n\n")
    print("Items in Inventory\n")
    for item in gameInventory:
        #itemQty = gameInventory.count(item)
        print(item, gameInventory.count(item))
    print()
    time.sleep(2)
    os.system("clear")

def removeItem():
    print("INVENTORY\n\n==========\n\n")
    itemName = input("Item to remove > ").capitalize()
    if itemName in gameInventory:
        gameInventory.remove(itemName)
        print("Item removed!\n")
        time.sleep(2)
        os.system("clear")
    else:
        print("Item not found!\n")
        tryAgain = input("Do you want to try again? (Yes/No) > ")
        if tryAgain.strip().capitalize() == "yes":
            itemName = input("Item to remove > ").capitalize()
            if itemName in gameInventory:
                gameInventory.remove(itemName)
                print("Item removed!\n")
                time.sleep(2)
                os.system("clear")
            else:
                print("Item not found!\n")
                time.sleep(2)
        else:
            pass

while True:
    gameMenu()
    menuChoice = input("> ")
    time.sleep(1)
    os.system("clear")

    if menuChoice == "1":
        addItem()
    elif menuChoice == "2":
        viewItem()
    elif menuChoice == "3":
        removeItem()
    elif menuChoice == "4":
        print("Exiting...")
        break
    else:
        #If the user enters an invalid choice, the loop will restart, due to the while-True loop.
        print("Invalid choice. Please, try again.\n")
        time.sleep(2)
        os.system("clear")
    f = open("Game_Inventory.txt", "w")
    f.write(str(gameInventory))
    f.close()