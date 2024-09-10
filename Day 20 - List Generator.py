print("List Generator")
print("-----")
print("You are going to give me a number you want to start with, an ending number, and by how many you want me to increment the list.")
print("Let's go!")
print()
start = int(input("Start number: "))
end = int(input("End number: "))
increment = int(input("Increment number: "))

for list in range (start, end, increment):
  print(list)
