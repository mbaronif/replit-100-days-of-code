import random, time, os

def menuIntro():
    print("IDEAS")
    print()
    print("1: Add an idea\n2: Load up a random idea\n3: Exit\n")


while True:
    menuIntro()
    menuChoice = input("> ")
    time.sleep(1)
    os.system("clear")

    if menuChoice == "1":
        newIdea = input("IDEAS\n\nAdd an idea: ")
        with open("my.ideas", "a") as f:
            f.write(f"{newIdea}\n")
        print("\nIdea saved!") 
        time.sleep(1)
        os.system("clear")
        f.close()      
    elif menuChoice == "2":
        with open("my.ideas", "r") as f:
            ideas = f.readlines()
            randomIdea = random.choice(ideas).strip()
            print("IDEAS\n\nRandom idea: " + randomIdea)
            time.sleep(2)
            os.system("clear")
        f.close()
    elif menuChoice == "3":
        print("IDEAS\n\nSee you next time!")
        time.sleep(1)
        os.system("clear")
        break
    else:
        print("IDEAS\n\nInvalid choice.\n")
        time.sleep(1)
        os.system("clear")
        continue

        