mokeBeast = {}

#Feeds the dictionary
def prettyPrint():
    print(f"Name\tType\tHP\tMP")
    for key, value in mokeBeast.items():
        print(f"""{key:^6}|{value["Type"]:^6}|{value["HP"]:^6}|{value["MP"]:^8}""")
    print()

while True:
    print("Enter the MokeBeast's information:")
    #Feeds the dictionary
    name = input("Name: ").title()
    type = input("Type: ").title()
    hp = int(input("HP: "))
    mp = int(input("MP: "))
    mokeBeast[name] = {"Type": type, "HP": hp, "MP": mp}
    print()
 
    prettyPrint()