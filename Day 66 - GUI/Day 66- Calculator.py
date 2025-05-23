import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("250x200")

label = 0


# Command functions
def add():
    pass
def subtract():
    pass
def multiply():
    pass
def divide():
    pass
def clear():
    pass
def calculate():
    pass

# Number keys
def number1():
    global label
    number = text.get("1.0", "end")
    number = int(number)

def number2():
    global label
    number = text.get("1.0", "end")
    number = int(number)

def number3():
    global label
    number = text.get("1.0", "end")
    number = int(number)

def number4():
    global label
    number = text.get("1.0", "end")
    number = int(number)

def number5():
    global label
    number = text.get("1.0", "end")
    number = int(number)

def number6():
    global label
    number = text.get("1.0", "end")
    number = int(number)

def number7():
    global label
    number = text.get("1.0", "end")
    number = int(number)

def number8():
    global label
    number = text.get("1.0", "end")
    number = int(number)

def number9():
    global label
    number = text.get("1.0", "end")
    number = int(number)

def number0():
    global label
    number = text.get("1.0", "end")
    number = int(number)

# Display
text = tk.Text(window, height = 1, width = 30)
text.grid(row= 0, column=1, columnspan=4)

# Buttons
button = tk.Button(text="1", command = number1)
button.grid(row=1, column=1)
button = tk.Button(text="2", command = number2)
button.grid(row=1, column=2)
button = tk.Button(text="3", command = number3)
button.grid(row=1, column=3)

button = tk.Button(text="4", command = number4)
button.grid(row=2, column=1)
button = tk.Button(text="5", command = number5)
button.grid(row=2, column=2)
button = tk.Button(text="6", command = number6)
button.grid(row=2, column=3)

button = tk.Button(text="7", command = number7)
button.grid(row=3, column=1)
button = tk.Button(text="8", command = number8)
button.grid(row=3, column=2)
button = tk.Button(text="9", command = number9)
button.grid(row=3, column=3)

button = tk.Button(text="0", command = number0)
button.grid(row=4, column=1)
button = tk.Button(text="=", command = calculate)
button.grid(row=4, column=2)
button = tk.Button(text="AC", command = clear)
button.grid(row=4, column=3)

button = tk.Button(text="+", command = add)
button.grid(row=1, column=4)
button = tk.Button(text="-", command = subtract)
button.grid(row=2, column=4)
button = tk.Button(text="*", command = multiply)
button.grid(row=3, column=4)
button = tk.Button(text="/", command = divide)
button.grid(row=4, column=4)


# Starts the GUI
tk.mainloop()