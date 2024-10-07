def printRoutine(color, word):
  if (color=="red"):
    print("\033[31m", word, sep="", end="")
  elif (color=="green"):
    print("\033[32m", word, sep="", end="")
  elif (color=="blue"):
    print("\033[34m", word, sep="", end="")
  else:
    print("\033[0m", word, sep="", end="")

print("Super Subroutine\n\nWith my ", end="")
printRoutine("green", "new program ")
printRoutine("reset ", "I can just\n")
print("call red ('and') ", end="")
printRoutine("red", "and ")
printRoutine("reset ", "that word will\nappear in the color I set it to.\n\n")
print("With no ", end="")
printRoutine("blue", "weird gaps.\n\n")
printRoutine("reset", "Epic.")
