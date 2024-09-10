loan = 1000
for count in range (1, 11):
  loan = loan * 1.05
  print("Year", count, "is", round(loan,2))
print("You paid $" + str(round(loan - 1000,2)) + " in interest")
