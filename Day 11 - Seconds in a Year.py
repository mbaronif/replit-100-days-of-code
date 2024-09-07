print("How many seconds are in a year?")
print()
thisYear = int(input("What year is it? "))
leapYear = input("Is it a leap year? ")
if leapYear == "yes" or leapYear == "Yes":
  seconds = 60 * 60 * 24 * 366
  print("There are", seconds, "seconds in", thisYear)
else:
  seconds = 60 * 60 * 24 * 365
  print("There are", seconds, "seconds in", thisYear)
