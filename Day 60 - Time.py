import datetime

print("EVENT COUNTDOWN TIMER\n")
event = input("What is the event? ").capitalize()
print("\nWhen is the event?")
day = int(input("Day: "))
# Makes sure the inputed month is a valid number.
while True:
    month = int(input("Month: "))
    if month < 1 or month > 12:
        print("Invalid month. Please enter a number between 1 and 12.")
    else:
        break
# Makes sure the inputed year has 4 digits.
while True:
    year = int(input("Year: "))
    # As len() doesn't work with int, we convert it to str before 
    if len(str(year)) != 4:
        print("Invalid year. Please enter a 4-digit year.")
    else:
        break
print()

today = datetime.date.today()
eventDate = datetime.date(year, month, day)

amount = eventDate - today
difference = amount.days

if eventDate > today:
    print(f"{event} is in {difference} days. Get ready! 🤩")
elif eventDate < today:
    print(f"Oh, no! You have missed {event} by {difference*(-1)} days. 😭")
else:
    print(f"Today is THE day! Have fun! 🥳")