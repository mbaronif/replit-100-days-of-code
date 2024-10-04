import random, os, time

rollDiceSix = random.randint(1, 6)
rollDiceTwelve = random.randint(1, 12)

def char_name():
  firstName = input("Name your Legend: ")
  return firstName
  
def char_race():
  charRace = input("Character Type (Human, Elf, Wizard, Orc): ")
  return charRace

def char_health():
  healthDice = ((rollDiceSix * rollDiceTwelve / 2)) + 10
  return healthDice
  
def char_strength():
  strengthDice = ((rollDiceSix * rollDiceTwelve / 2)) + 12
  return strengthDice

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

  playAgain = input("Would you like to play again? ")
  if playAgain == "yes":
    continue
  else:
    break
