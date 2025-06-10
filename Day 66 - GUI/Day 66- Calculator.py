import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("250x200")

answer = 0
operator = None

# Number keys
def typeKey(value):
    global answer
    answer = f"{answer}{value}"
    answer = int(answer)  # Convert the answer to an integer
    text["text"] = answer  # Update the display with the new answer
"""I can create a single function that takes the number as an argument. It'll, then, update the display with the number pressed.
This way, I can avoid repeating code for each number.
"""

# Command functions
def calcAnswer(thisOperator):
    global answer, lastNumber, operator
    # Store the current answer and reset it for the next input
    lastNumber = answer
    answer = 0
    # Set the operator based on the button pressed
    if thisOperator == "+":
        operator = "+"
    elif thisOperator == "-":
        operator = "-"
    elif thisOperator == "*":
        operator = "*"
    elif thisOperator == "/":
        operator = "/"
    text["text"] = answer  # Update the display with the new answer

def calculate():
    """
    Perform the calculation based on the selected operator.
    The function checks which operator was selected (+, -, *, /) and performs the corresponding operation
    using the last number entered and the current answer. If the operator is division and the current answer
    is zero, it displays an error message to prevent division by zero.
    """
    global answer, lastNumber, operator
    # Create if-else statement to handle operations when the operator is pressed.
    if operator == "+":
        total = lastNumber + answer
    elif operator == "-":
        total = lastNumber - answer
    elif operator == "*":
        total = lastNumber * answer
    elif operator == "/":
        if answer == 0:
            text["text"] = "Error"  # Display error for division by zero
            return
        total = lastNumber / answer
    answer = total  # Update the answer with the total
    text["text"] = total  # Update the display with the total

# Clear function to reset the calculator
def clear():
    global answer, operator
    text.config(text="0")  # Reset the display to 0
    answer = 0  # Reset the answer

# Display
text = tk.Label(text=str(answer), fg="black", bg="white", font=("Arial", 24))
text.grid(row=0, column=1, columnspan=4)  # Use columnspan to center the display across multiple columns

# Number keys
key1 = tk.Button(text="1", command = lambda:typeKey(1))
key1.grid(row=1, column=1)
key2 = tk.Button(text="2", command = lambda:typeKey(2))
key2.grid(row=1, column=2)
key3 = tk.Button(text="3", command = lambda:typeKey(3))
key3.grid(row=1, column=3)

key4 = tk.Button(text="4", command = lambda:typeKey(4))
key4.grid(row=2, column=1)
key5 = tk.Button(text="5", command = lambda:typeKey(5))
key5.grid(row=2, column=2)
key6 = tk.Button(text="6", command = lambda:typeKey(6))
key6.grid(row=2, column=3)

key7 = tk.Button(text="7", command = lambda:typeKey(7))
key7.grid(row=3, column=1)
key8 = tk.Button(text="8", command = lambda:typeKey(8))
key8.grid(row=3, column=2)
key9 = tk.Button(text="9", command= lambda:typeKey(9))
key9.grid(row=3, column=3)

key0 = tk.Button(text="0", command = lambda:typeKey(0))
key0.grid(row=4, column=1)

# Command keys
equal = tk.Button(text="=", command = lambda:calculate)
equal.grid(row=4, column=2)
clearButton = tk.Button(text="AC", command = clear)
clearButton.grid(row=4, column=3)

plus = tk.Button(text="+", command = lambda:calcAnswer("+"))
plus.grid(row=1, column=4)
minus = tk.Button(text="-", command = lambda:calcAnswer("-"))
minus.grid(row=2, column=4)
multiply = tk.Button(text="*", command = lambda:calcAnswer("*"))
multiply.grid(row=3, column=4)
divide = tk.Button(text="/", command = lambda:calcAnswer("/"))
divide.grid(row=4, column=4)


# Starts the GUI
tk.mainloop()