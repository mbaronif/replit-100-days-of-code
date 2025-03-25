import time, os

pizzaOrders = []
pizzaPrices = {"S": 10,
               "M": 15,
               "L": 20}

try:
    with open("Day 52 - Pizza Shop.txt", "r") as f:
        file_content = f.read()
        if file_content:
            pizzaOrders = eval(file_content)
except FileNotFoundError:
    with open("Day 52 - Pizza Shop.txt", "a+") as f:
        pass # Create the file if it doesn't exist

def menuIntro():
    print("Pizza Shop\n")
    print("1: Add a pizza order\n2: View all pizza orders\n3: Exit\n")

def pizzaCheckOut():
    print(f"{'Name'.center(6)}{'Topping'.center(13)}{'Size'.center(6)}{'Qty'.center(7)}{'Total'.center(8)}")
    for order in pizzaOrders:
        print(f"""{order["Name"]:^6}|{order["Topping"]:^12}|{order["Size"]:^5}|{order["Quantity"]:^5}|{order["Total"]:^7}""")
    print()

while True:
    menuIntro()
    menuChoice = input("> ")

    if menuChoice == "1":
        customerName = input("Name: ").title()
        pizzaTopping = input("Topping: ").capitalize()
        pizzaSize = input("Size (S/M/L): ").capitalize()
        pizzaQty = input("Quantity: ")
        try:
            pizzaQty = int(pizzaQty)  # Convert input to integer
            if isinstance(pizzaQty, int): # Check if the input is a whole number
                pass
            else:
                raise ValueError
        except ValueError:
            print("\nInvalid quantity. Please, enter a whole number.\n")
            pizzaQty = input("Quantity: ")
        pizzaTotal = pizzaPrices[pizzaSize] * pizzaQty
        pizzaOrders.append({"Name": customerName, "Topping": pizzaTopping, "Size": pizzaSize, "Quantity": pizzaQty, "Total": pizzaTotal})
        print("\nOrder saved!")
        time.sleep(1)
        os.system("clear")
    elif menuChoice == "2":
        print("\nAll pizza orders:")
        pizzaCheckOut()
        time.sleep(2)
        os.system("clear")
    elif menuChoice == "3":
        print("\nSee you next time!")
        time.sleep(1)
        os.system("clear")
        break
    else:
        print("\nInvalid choice.")
        time.sleep(1)
        os.system("clear")

with open("Day 52 - Pizza Shop.txt", "w") as f:
    f.write(str(pizzaOrders))
