from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L E")
print("There are 3 possible moves: Rock, Paper, Scissors.")

while True:
  player1 = input("Select your move (R, P or S): ")
  player1 = player1.upper()
  if player1.upper() != "R" and player1.upper() != "P" and player1.upper() != "S":
    print("Invalid move, Player 1!" ☠️)
  else:
    break

while True:
  player2 = input("Select your move (R, P or S): ")
  player2 = player2.upper()
  if player2.upper() != "R" and player2.upper() != "P" and player2.upper() != "S":
    print("Invalid move, Player 2!" ☠️)
  else:
    break

#tie
if player1.upper() == "R" and player2.upper() == "R" or player1.upper() == "P" and player2.upper() == "P" or player1.upper() == "S" and player2.upper() == "S":
  print("It's a tie!" 🎲🎲)

#Player 1 wins
elif player1.upper() == "R" and player2.upper() == "S" or player1.upper() == "P" and player2.upper() == "R" or player1.upper() == "S" and player2.upper() == "P":
  print("Player 2 loses! Contrats Player 1!" 🏆)
  
#Player 2 wins
elif player1.upper() == "R" and player2.upper() == "P" or player1.upper() == "P" and player2.upper() == "S" or player1.upper() == "S" and player2.upper() == "R":
  print("Player 1 loses! Contrats Player 2!" 🏆)

else:
  print("Please, try again!")
