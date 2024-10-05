import random, os, time

rollDiceSix = random.randint(1, 6)
rollDiceTwelve = random.randint(1, 12)
'''
Instead of those 2 variables, I could have simplified that with a subroutine for rolling dices:
def rollDice(side):
  result = random.randint(1,side)
  return result
'''

def char_name():
  firstName = input("Name your Legend:\n") #\n makes the answer goes to the next line
  return firstName
  
def char_race():
  charRace = input("Character Type (Human, Elf, Wizard, Orc):\n") #\n makes the answer goes to the next line
  return charRace

def char_health():
  healthDice = ((rollDiceSix * rollDiceTwelve / 2)) + 10
  return healthDice
'''
With the subroutine rollDice:
def char_health():
  healthDice = ((rollDice(6) * rollDice(12) / 2)) + 10
  return healthDice
'''
  
def char_strength():
  strengthDice = ((rollDiceSix * rollDiceTwelve / 2)) + 12
  return strengthDice
'''
With the subroutine rollDice:
def char_strength():
  strengthDice = ((rollDice(6) * rollDice(12) / 2)) + 12
  return strengthDice
'''

while True:
  print("⚔️ Character Builder 🛡️")
  print()
  time.sleep(1)
  name = char_name()
  print()
  race = char_race()
  os.system("clear")
  
  print(name + " the " + race)
  print("HEALTH:", char_health())
  print("STRENGTH:", char_strength())
  print()  # Implemented after delivery
  time.sleep(1)  # Implemented after delivery
  print("May your name go down in Legend...")  # Implemented after delivery
  print()  # Implemented after delivery

  playAgain = input("Would you like to play again? ")
  if playAgain == "yes":
    continue
  else:
    break
