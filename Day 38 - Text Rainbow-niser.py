#Brute force solution

"""
# ANSI colors:
red = "\033[0;31m"
green = "\033[0;32m"
blue = "\033[0;34m"
yellow = "\033[1;33m"
purple = "\033[0;35m"
cyan = "\033[0;36m"
defautl = "\033[0m" #end
"""

print("Sentence Rainbowniser")
sentence = input("What sentence do you want to rainbow-ising?\n")

for color in sentence:
    if color.lower() == "a":
        print("\033[0;31m", end="") #red
    elif color.lower() == "a":
        print("\033[0;32m", end="") #green
    elif color.lower() == "e":
        print("\033[0;34m", end="") #blue
    elif color.lower() == "i":
        print("\033[1;33m", end="") #yellow
    elif color.lower() == "m":
        print("\033[0;35m", end="") #purple
    elif color.lower() == "r":
        print("\033[0;36m", end="") #cyan
    elif color.lower() == " ":
        print("\033[0m", end = "") #default
    print(color, end="")

"""
#Alternative solution:
def colorChange(color):
    if color.lower() == "a":
        print("\033[0;31m", end="") #red
    elif color.lower() == "a":
        print("\033[0;32m", end="") #green
    elif color.lower() == "e":
        print("\033[0;34m", end="") #blue
    elif color.lower() == "i":
        print("\033[1;33m", end="") #yellow
    elif color.lower() == "m":
        print("\033[0;35m", end="") #purple
    elif color.lower() == "r":
        print("\033[0;36m", end="") #cyan
    elif color.lower() == " ":
        print("\033[0m", end = "") #default

sentence = input("What sentence do you want to rainbow-ising?\n")

for letter in sentence:
    colorChange(letter.lower())
    print(letter, end="")
print()
"""
