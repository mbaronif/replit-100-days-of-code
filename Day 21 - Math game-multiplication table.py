print("Math game")
print("-----")
print("Let's brush up on your math skills!")
print("Can you answer all the questions correctly?")
print("Let's go!")
print()
# Ask the user to name their multiples
score = 0
multiple = int(input("Name your multiple: "))

for calc in range (1, 11, 1):
  print(calc, "x", multiple, "=")
  answer = int(input(""))

  if answer == (calc * multiple):
    score = score +1
    print("Great work!")
  else:
    print("Nope! The answer was", calc * multiple)

print("...")
if score == 10:
  print("You scored", score, "out of 10! 😎")
elif score >= 7 and score <= 9:
  print("You scored", score, "out of 10! 😊")
elif score >= 4 and score <= 6:
  print("You scored", score, "out of 10! 😕")
else:
  print("You scored", score, "out of 10! 😭")
