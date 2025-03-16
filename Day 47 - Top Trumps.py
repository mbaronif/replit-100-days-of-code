import random

topTrumps = {
    "Pikachu": {
        "CP": 797,
        "HP": 90,
        "Weight": 4.53,
        "Height": 0.31
    },
    "Charmander": {
        "CP": 632,
        "HP": 85,
        "Weight": 9.23,
        "Height": 0.6
    },
    "Bulbasaur": {
        "CP": 772,
        "HP": 93,
        "Weight": 7.18,
        "Height": 0.75
    },
    "Squirtle": {
        "CP": 536,
        "HP": 84,
        "Weight": 11.12,
        "Height": 0.55
    },
    "Eevee": {
        "CP": 884,
        "HP": 119,
        "Weight": 2.24,
        "Height": 0.19
    },
}

def characters():
    for name in topTrumps:
        print(name)
    print()

def printTopTrumps():
    print()
    print("TOP TRUMPS\n----------")
    print()
    characters()
    print()

while True:
    printTopTrumps()
    userCharacter = input("Pick a character:\n")
    print()
    computerCharacter = random.choice(list(topTrumps.keys()))
    print(f"Computer picked: {computerCharacter}")
    print()
    userStat = input("Choose a stat (CP, HP, Weight, Height):\n")
    print()
    computerStat = random.choice(["CP", "HP", "Weight", "Height"])
    print(f"{userCharacter} : {topTrumps[userCharacter][userStat]}")
    print(f"{computerCharacter} : {topTrumps[computerCharacter][userStat]}")
    print()

    # Transform the stats values into flots, so they can be compared in the if statement.
    userStatValue = float(topTrumps[userCharacter][userStat])
    computerStatValue = float(topTrumps[computerCharacter][computerStat])

    # Compare the stats values and print the result.
    if userStatValue > computerStatValue:
        print(f"{userCharacter} wins!")
    elif userStatValue < computerStatValue:
        print(f"{computerCharacter} wins!")
    else:
        print("It's a draw!")
    print()






"""    name = input("Enter the name of the player: ")
    if name == "":
        break
    topTrumps[name] = {}
    topTrumps[name]["Speed"] = int(input("Enter the speed of the player: "))
    topTrumps[name]["Strength"] = int(input("Enter the strength of the player: "))
    topTrumps[name]["Skill"] = int(input("Enter the skill of the player: "))"""