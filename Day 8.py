print("Wholesome Positivity Machine")
print()

userName = input("Who are you? ")
print("Hello, " + userName + "!")
print()

userGoal = input("What do you want to achieve today? ")
print("That's great!")
print()

userFeel = input("On a scale of 1 - 10, how do you feel today? ")
if userFeel == "1" or userFeel == "2":
  print("I'm sorry to hear that. I hope you feel better soon!")
elif userFeel == "3" or userFeel == "4":
  print("I hope things get better soon!")
elif userFeel == "5" or userFeel == "6":
  print("Cheer up! It's just one day, not the whole life. You got this!")
elif userFeel == "7" or userFeel == "8":
  print("Great! I'm glad you're feeling good!")
elif userFeel == "9" or userFeel == "10":
  print("Awesome! It's a shiny day then!")
else:
  print("Please enter a number between 1 and 10.")
print()

weekDay = input("What day of the week is it today? ")
if weekDay == "Monday" or weekDay == "monday":
  print("Monday morning is a great time to start a new week! I'm sure you'll achieve your goal of " + userGoal + " today!")
elif weekDay == "Tuesday" or weekDay == "tuesday":
  print("Tuesday is just Monday's more sophisticated cousin. I'm sure you'll achieve your goal of " + userGoal + " today!")
elif weekDay == "Wednesday" or weekDay == "wednesday":
  print("Wednesday is hump day! I'm sure you'll achieve your goal of " + userGoal + " today!")
elif weekDay == "Thursday" or weekDay == "thursday":
  print("Thursdays are the best! I'm sure you'll achieve your goal of " + userGoal + " today!")
elif weekDay == "Friday" or weekDay == "friday":
  print("Friday is the best day of the week! I'm sure you'll achieve your goal of " + userGoal + " today!")
elif weekDay == "Saturday" or weekDay == "saturday":
  print("Saturday wait! I'm sure you'll achieve your goal of " + userGoal +" today!")
elif weekDay == "Sunday" or weekDay == "sunday":
  print("Sunday always comes too late! I'm sure you'll achieve your goal of " + userGoal + " today!")
