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
    typeColor = "\033[0;32m" #White
elif mokeBeast["Type"] == "Air":
    typeColor = "\033[1;37m" #Green
elif mokeBeast["Type"] == "Spirit":
    typeColor ="\033[0;35m" #Purple

#Prints all entries in the Type respective color
for name, value in mokeBeast.items():
    print(f"{typeColor}{name}: {value}")
