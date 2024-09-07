faveShow = input("What's your favorite show? ")
if faveShow == "The IT Crowd":
  faveCharacter = input("Oh, really?! Name me one of the characters. ")
  if faveCharacter == "Moss":
    prize = input("You got that by pure chance. OK, then, what award does he win in the show? ")
    if prize == "spelling contest":
      print("You're a true fan!")
    else:
      print("Ha! I knew it! You're a fake fan!")
  elif faveCharacter == "Jen":
    colorShoes = input("You got that by pure chance. OK, then, what color are her desired shoes? ")
    if colorShoes == "red":
      print("You're a true fan!")
    else:
      print("Ha! I knew it! You're a fake fan!")
  else:
    print("Lame. That's not the better character.")
else:
  print("That's a good one too.")
