print("30 Days Down")
print()

for i in range(1, 31):
  dayThought = input(f"What do you think of Day {i}?\n")
  print()
  print(f"Day {i}")
  followUp = f"You thought Day {i} was \033[0;31m{dayThought}\033[0m."
  print(f"{followUp: ^50}")
  print()

print()
print("Well done! Let's keep going.")
