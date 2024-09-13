import random

print("Infinity Dice 🎲")

diceSides = int(input("How many sides?: "))

def rollDice(diceSides):
  while True:
    print("You rolled", random.randint(1, diceSides))
    quitGame = input("Roll again? ")
    if quitGame == "yes" or quitGame == "Yes":
      continue
    else:
      print("OK, then. See you later. Bye!")
      break

rollDice(diceSides)
