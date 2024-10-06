import random, os, time

# Generates a dice
def rollDice(side):
  result = random.randint(1,side)
  return result

# Generates health stat
def char_health():
  healthDice = ((rollDice(6) * rollDice(12) / 2)) + 10
  return healthDice

# Generates strength stat
def char_strength():
  strengthDice = ((rollDice(6) * rollDice(12) / 2)) + 12
  return strengthDice

while True:
  print("⚔️ Battle Game ⚔️ ")
  print()
  time.sleep(1)

  # Player 1
  player1 = input("Name your Legend:\n")
  race1 = input("Character Type (Human, Elf, Wizard, Orc):\n")
  print()

  # Player 1 stats
  print(player1 + " the " + race1)
  player1health = char_health()
  print("HEALTH:", player1health)
  player1strength = char_strength()
  print("STRENGTH:", player1strength)
  print()
  time.sleep(1)

  print("Who are they battling?")
  print()

  #Player 2
  player2 = input("Name your Legend:\n")
  race2 = input("Character Type (Human, Elf, Wizard, Orc):\n")
  print()

  #Player 2 stats
  print(player2 + " the " + race2)
  player2health = char_health()
  print("HEALTH:", player2health)
  player2strength = char_strength()
  print("STRENGTH:", player2strength)
  print()
  time.sleep(1)
  os.system("clear")
  
  print("⚔️ Battle Time ⚔️")
  print()

  print("The battle begins!")
  print()

  damage = abs(player1strength - player2strength) + 1
  round = 0 # Rounds starts in 0
  
  while True:
    player1_dice = rollDice(6)
    player2_dice = rollDice(6)

    round += 1

    # Checks dices for players' damage
    if player1_dice > player2_dice:
      print(player1 + " wins this round")
      print(player2 + " takes a hit, with", damage, "damage")
      player2health -= damage
      print()
      time.sleep(1)
    elif player2_dice > player1_dice:
      print(player2 + " wins this round")
      print(player1 + " takes a hit, with", damage, "damage")
      player1health -= damage
      print()
      time.sleep(1)
    else:
      print("It's a draw")
      print("Both players are still standing")
      print()
      time.sleep(1)
    
    print(player1)
    print("HEALTH:", player1health)
    print()
    print(player2)
    print("HEALTH:", player2health)
    print()
    time.sleep(1)

    # Checks stats for whether finish the game
    if player1health <= 0:
      print("Oh no", player1, "has died!")
      print()
      print(player2, "destroyed", player1, "in", round, "rounds!")
      break
    elif player2health <= 0:
      print("Oh no", player2, "has died!")
      print()
      print(player1, "destroyed", player2, "in", round, "rounds!")
      break
    else:
      print("And they're both standing for the next round!")
      time.sleep(2)
      os.system("clear")
      print("⚔️ BATTLE TIME ⚔️")
      print()
      print("The battle continues!")
      print()
      continue
  print()

  # Lets the game restart
  playAgain = input("Would you like to play again? ")
  if playAgain == "yes" or playAgain == "Yes":
    continue
  else:
    break
