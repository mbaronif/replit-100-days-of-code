myBill = float(input("What was the bill?: "))
tipValue = float(input("What percentage of tip would you like to leave? "))
numberOfPeople = int(input("How many people?: "))
answer = (myBill * ((tipValue/100)+1)) / numberOfPeople
answer = round(answer, 2)
print("You all owe", answer)
