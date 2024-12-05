import random
import time


def prettyPrint():
    for row in bingo: #Iterates through the outer array
        for elements in row: #Iterates through the inner arrays 
            print(f"{elements:^5}", end = " | ")        
        print()
        print(20*"-")
        time.sleep(0.1)
#Generates random numbers for the bingo card.
#The .sample method makes sure there'll be no repeated number.
numbers = random.sample(range(1, 90), 8)
#Sorts the random numbers, so they're displayed in numerical order
numbers.sort() 
#The bingo card
bingo = [ [numbers[0], numbers[1], numbers[2]],
         [numbers[3], "BINGO", numbers[4]],
         [numbers[5], numbers[6], numbers[7]]
]

#The final game
while True:
    print("\033[1;33mDavid's Nan's Bingo Card Generator\033[0m")
    print()
    prettyPrint()

    #If I don't convert the input into a integer, the comparison/check doesn't work.
    userNumber = int(input("What number was called? "))
    #This [:] creates a copy of the bingo card, to avoid modifying the original one
    for row in bingo[:]:
        #Checks each row for the userNumber
        if userNumber in row:
            #Finds the index of userNumber
            bingoIndex = row.index(userNumber)
            #Replaces the number with 'X'
            row[bingoIndex] = "X"
    #This will count all ocurrences of 'X' in the bingo card.
    totalX = sum(row.count("X") for row in bingo)
    if totalX == 8:
        print("Win! Game Over")
        break


#Bug: I couldn't eliminate the last line after the last column and line
