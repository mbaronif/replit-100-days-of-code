'''
import random
#This is my wrong interpretation of the exercise:

print("⚔️ CHARACTER STAT GENERATOR ⚔️")
print()

diceSides = int(input("How many sides?: "))

def rollDice(diceSides):
  firstDice = random.randint(1, diceSides)
  return firstDice
dice = rollDice(diceSides)

def roll2dices(dice):
  hpStats = random.randint(1, 6) * random.randint(1, 8)
  return hpStats

while True:
    character = input("Name your warrior: ")
    hp = roll2dices(dice)
    print("Their health is:", hp)
    print()
    again = input("Want to create another character? y/n: ")
    if again == "y":
        continue
    else:
        print("Thanks for playing!")
        break
'''

import random

#This function creates a random dice.
def rollDice(sides):
    result = random.randint(1, sides)
    return result

#This function creates 2 rolls of the previous dice and calculates
#the health points based on the value of those 2 dices.
def roll_6_and_8():
    roll_6_sided_dice = rollDice(6)
    roll_8_sided_dice = rollDice(8)
    hp = roll_6_sided_dice * roll_8_sided_dice
    return hp

#The game starts after the functions are created.
print("⚔️ Character stats generator ⚔️")

haveACharacter = "yes"

while haveACharacter == "yes":
  character = input("Name your warrior: ")
  health = str(roll_6_and_8())
  print("Their health is ", health,"hp" ) 
  haveACharacter = input("Want to create another character? ")
