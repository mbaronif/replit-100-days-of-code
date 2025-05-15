import random

# Tested and working
def rollDice(sides):
    result = random.randint(1, sides)
    return result

def printRoutine(color):
    if (color=="red"):
        print("\033[31m", sep="", end="")
    elif (color=="green"):
        print("\033[32m", sep="", end="")
    elif (color=="blue"):
        print("\033[34m", sep="", end="")
    else:
        print("\033[0m", sep="", end="")

def randomNumberGenerator():
    number = random.randint(1,100)
    return number

def palindrome_checker(word):
    # Reads the word backwards and compare it to the original word
    if word == word[::-1]:
        return "TRUE"
    else:
        return "FALSE"

# Not tested yet, not working, or just a reference
def nameList(): # Prints the full list, with new additions.
    for item in list:
        print(item)
    print()
    

def checkOut():
    print(f"{'Name'.center(6)}{'Topping'.center(13)}{'Size'.center(6)}{'Qty'.center(7)}{'Total'.center(8)}")
    for order in pizzaOrders:
        print(f"""{order["Name"]:^6}|{order["Topping"]:^12}|{order["Size"]:^5}|{order["Quantity"]:^5}|{order["Total"]:^7}""")
    print()