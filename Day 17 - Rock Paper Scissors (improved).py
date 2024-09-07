from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L E")
print("There are 3 possible moves: Rock, Paper, Scissors.")

#The players' scores start in 0
player1_round = 0
player2_round = 0

while True:
  while True: #Player 1 plays
    player1 = input("Player 1, select your move (R, P or S): ")
    player1 = player1.upper()
    if player1.upper() != "R" and player1.upper() != "P" and player1.upper() != "S":
      print("Invalid move, Player 1! ☠️")
      continue
    else:
      break
  
  while True: #Player 2 Plays
    player2 = input("Player 2, select your move (R, P or S): ")
    player2 = player2.upper()
    if player2.upper() != "R" and player2.upper() != "P" and player2.upper() != "S":
      print("Invalid move, Player 2! ☠️")
      continue
    else:
      break  

  #tie
  if player1.upper() == "R" and player2.upper() == "R" or player1.upper() == "P" and player2.upper() == "P" or player1.upper() == "S" and player2.upper() == "S":
    print("It's a tie! 🎲🎲")
    print("Next round!")
  
  #Player 1 wins
  elif player1.upper() == "R" and player2.upper() == "S" or player1.upper() == "P" and player2.upper() == "R" or player1.upper() == "S" and player2.upper() == "P":
    print("Player 1 wins! 🏆")
    player1_round += 1
    print("Player 1 has ", player1_round, "wins.")
    print("Next round!")
  #Player 2 wins
  elif player1.upper() == "R" and player2.upper() == "P" or player1.upper() == "P" and player2.upper() == "S" or player1.upper() == "S" and player2.upper() == "R":
    print("Player 2 wins! 🏆")
    player2_round += 1
    print("Player 2 has ", player2_round, "wins.")
    print("Next round!")
  print()
  if player1_round == 3 or player2_round == 3:
    print("Game Over!")
    print("Player 1 has ", player1_round, "wins and Player 2 has ", player2_round, "wins.")
    print("Thanks for playing!")
    exit()
