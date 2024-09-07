print("Name the Lyrics Game")
print()
print("Fill in the blank lyrics!")
print("Find out the missing workd to complete the song. How many attempts will it take you?")
print()

counter = 1
while True:
  lyrics = input("I wanna rock'n'roll all night, and ______ every day! ")
  if lyrics == "party" or lyrics == "Party":
    print("You got it!")
    break
  else:
    print("Nope! Try again!")
    counter +=1
print("You got the correct lyrics in", counter, "attempt(s).")
