print("Animal Sounds")
print()
print("Animals available: cow, dog, cat, duck, pig, and sheep")
print()
animal = input("What animal do you want? ")
while animal != " ":
  if animal == "cow":
    print("A cow goes moo. 🐮")
    exit = input("Do you want to exit? ")
    if exit == "yes":
      print("OK, that was fun! 😁")
      break
    else:
      animal = input("What animal do you want? ")
  elif animal == "dog":
    print("A dog goes woof. 🐶")
    exit = input("Do you want to exit? ")
    if exit == "yes":
      print("OK, that was fun! 😁")
      break
    else:
      animal = input("What animal do you want? ")
  elif animal == "cat":
    print("A cat goas meow. 🐱")
    exit = input("Do you want to exit? ")
    if exit == "yes":
      print("OK, that was fun! 😁")
      break
    else:
      animal = input("What animal do you want? ")
  elif animal == "duck":
    print("A duck goes quack. 🦆")
    exit = input("Do you want to exit? ")
    if exit == "yes":
      print("OK, that was fun! 😁")
      break
    else:
      animal = input("What animal do you want? ")
  elif animal == "pig":
    print("A pig goes oink. 🐷")
    exit = input("Do you want to exit? ")
    if exit == "yes":
      print("OK, that was fun! 😁")
      break
    else:
      animal = input("What animal do you want? ")
  elif animal == "sheep":
    print("A sheep goes baa. 🐑")
    exit = input("Do you want to exit? ")
    if exit == "yes":
      print("OK, that was fun! 😁")
      break
    else:
      animal = input("What animal do you want? ")
  else:
    print("OK, that was fun! 😁")
    break
