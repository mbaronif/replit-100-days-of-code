mokeBeast = {"Name" : None, 
             "Type" : None,
             "Move" : None,
             "HP" : None,
             "MP" : None}

#Feeds the dictionary
for name, value in mokeBeast.items():
    mokeBeast[name] = input(f"{name}: ").strip().capitalize()

print()

#Defines the color of each Type
typeColor = "\033[0m" #Default - no color
if mokeBeast["Type"] == "Fire":
    typeColor = "\033[0;31m" #Red
elif mokeBeast["Type"] == "Water":
    typeColor = "\033[0;34m" #Blue
elif mokeBeast["Type"] == "Earth":
    typeColor = "\033[0;32m" #Green
elif mokeBeast["Type"] == "Air":
    typeColor = "\033[1;37m" #White
elif mokeBeast["Type"] == "Spirit":
    typeColor ="\033[0;35m" #Purple

#Prints all entries in the Type respective color
for name, value in mokeBeast.items():
    print(f"{typeColor}{name}: {value}")


"""
ALTERNATIVE
#No need for the typeColor variable with this solution.
if mokeBeast["Type"] == "Fire":
    print("\033[0;31m", end = "") #Red
elif mokeBeast["Type"] == "Water":
    print("\033[0;34m", end = "") #Blue
elif mokeBeast["Type"] == "Earth":
    print ("\033[0;32m", end = "") #Green
elif mokeBeast["Type"] == "Air":
    print ("\033[1;37m", end = "") #White
elif mokeBeast["Type"] == "Spirit":
    print = ("\033[0;35m", end = "") #Purple

for name, value in mokeBeast.items():
    print(f"{name: <15}: {value}") #space added to align the input
"""
