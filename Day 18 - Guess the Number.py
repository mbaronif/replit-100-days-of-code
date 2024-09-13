print("Guess the Number!")
print("How many chances do you think you need to find out the number I'm thinking of?")
print("I'll give you a hint: the number is between 1 and 1000000!")
print("Let's go!")
print()

secretNumber = 560000
round = 1

while True:
  guess = int(input("What is your guess? "))
  if guess == secretNumber:
    print("That's correct! You nailed it!")
    break
  elif guess < secretNumber and guess > 0:
    round += 1
    print("Too low! Try again!")
  elif guess > secretNumber and guess <= 1000000:
    round += 1
    print("Too high! Try again!")
  else:
    print("You're not playing by the rules, are you?")
    exit()
print()
#edited to add the solution for plural vs. singular in the final message - credits to Brianda :)
if round == 1:
  print("You got it on the first try! You're a genius!")
else:
  print("It took you", round, "guesses to get it right!")
