#Color rules
def colorRule(color):
  if (color == "yellow"):
    return("\033[1;33m") #can be simplified to return("\033[1;33m")
  elif (color == "green"):
    return("\033[0;32m") #can be simplified to return("\033[0;32m")
  elif (color == "red"):
    return("\033[0;31m") #can be simplified to return("\033[0;31m")
  elif (color == "blue"):
    return("\033[0;34m") #can be simplified to return("\033[0;34m")
  elif (color == "light_purple"):
    return("\033[1;35m") #can be simplified to return("\033[1;35m")
  elif (color == "white"):
    return("\033[0m") #can be simplified to return("\033[1;35m")
  else:
    return("\033[0m")


#Interface 1 - variables
title = f"{colorRule('red')}={colorRule('white')}={colorRule('blue')}={colorRule('yellow')}Music App{colorRule('blue')}={colorRule('white')}={colorRule('red')}="
prev = "PREV"
next = "NEXT"
pause = "PAUSE"

#Interface 2 - variables
welcome = "Welcome to"
armbook = "--    ARMBOOK    --"
notaRip1 = "Definitelly not a rip off of"
notaRip2 = "a certain other social" 
notaRip3 = "networking site."
honest = "Honest."
username = "Username:"
password = "Password:"

#Interface 1 - print
print(f"            {title: ^50}")
print(f"🔥▶️\t{colorRule('white')}Radio Gaga")
print(f"\t{colorRule('yellow')}Queen")
print()
print()
print(f"{colorRule('white')}{prev: <20}")
print(f"{colorRule('green')}{next: ^20}")
print(f"{colorRule('light_purple')}{pause: >20}")
print()
print()

#Interface 2 - print
print(f"{colorRule('white')}{welcome: ^50}")
print(f"{colorRule('blue')}{armbook: ^50}")
print( )
print(f"{colorRule('yellow')}{notaRip1: >50}")
print(f"{colorRule('yellow')}{notaRip2: >50}")
print(f"{colorRule('yellow')}{notaRip3: >50}")
print()
print(f"{colorRule('red')}{honest: ^50}")
print()
print(f"{colorRule('white')}{username: ^50}")
print(f"{colorRule('white')}{password: ^50}")
