import tkinter as tk

window = tk.Tk()
window.title("Hello world")
window.geometry("400x200")

label = 0

"""
# This function changes the label when the button is clicked.
def updateLabel():
    label "Bye world!"
    hello["text"] = label"""

# This function cincreases the number of the label when the button is clicked. It's a good way to create a counter.
def updateLabel():
    global label
    number = text.get("1.0", "end") 
    # The first argument in text.get() is the start of the text, and should be a decimal number. 
    # The second argument is the end of the text.
    number = int(number)
    label = number
    hello["text"] = label
    
hello = tk.Label(text=label)
hello.grid(row=0, column=1)
#hello.pack() 

text = tk.Text(window, height = 1, width = 25)
text.grid(row=2, column=1)
#text.pack(side=tk.TOP)

button = tk.Button(text="Button 1", command = updateLabel)
button.grid(row=3, column=0)
#button.pack()
button = tk.Button(text="Button 2", command = updateLabel)
button.grid(row=3, column=1)
#button.pack()
button = tk.Button(text="Button 3", command = updateLabel)
button.grid(row=3, column=2)
#button.pack()

tk.mainloop()