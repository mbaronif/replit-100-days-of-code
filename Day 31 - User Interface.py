#Color rules
def colorRule(color, word):
def colorRule(color, word):
  if (color == "yellow"):
    print("\033[1;33m", word, end="") #can be simplified to return("\033[1;33m")
  elif (color == "green"):
    print("\033[0;32m", word, end="") #can be simplified to return("\033[0;32m")
  elif (color == "red"):
    print("\033[0;31m", word, end="") #can be simplified to return("\033[0;31m")
  elif (color == "blue"):
    print("\033[0;34m", word, end="") #can be simplified to return("\033[0;34m")
  elif (color == "light_purple"):
    print("\033[1;35m", word, end="") #can be simplified to return("\033[1;35m")
  else:
    print("\033[0m", word, end="")


#Interface 1 - variables
equalSign = "="
title = "Music App"
song = "🔥▶️ Radio Gaga"
band = "Queen"
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
colorRule("red", f"{equalSign: >11}")
colorRule("reset", "=")
colorRule("blue", f"{equalSign}")
colorRule("reset", "")
colorRule("yellow", f"{title}")
colorRule("reset", "")
colorRule("blue", f"{equalSign}")
colorRule("reset", "=")
colorRule("red", f"{equalSign}")
colorRule("reset", "")
print()
print()
print(f"{song}")
colorRule("yellow", f"{band: ^11}")
colorRule("reset", "\n")
print()
print()
print(f"{prev}")
colorRule("green", f"{next: ^11}")
colorRule("reset", "\n")
colorRule("light_purple", f"{pause: ^21}")
colorRule("reset", "\n")
print()
print()

#Interface 2 - print
print(f"{welcome: ^50}")
colorRule("blue", f"{armbook: ^50}")
colorRule("reset", "\n")
print( )
colorRule("yellow", f"{notaRip1: >43}\n")
colorRule("yellow", f"{notaRip2: >43}\n")
colorRule("yellow", f"{notaRip3: >43}")
colorRule("reset", "\n")
print()
colorRule("red", f"{honest: ^50}")
colorRule("reset", "\n")
print()
print(f"{username: ^50}")
print(f"{username: ^50}")
