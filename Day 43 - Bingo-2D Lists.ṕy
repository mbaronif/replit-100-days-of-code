import random

bingoNum = random.randint(0, 90)
bingoA1 = random.randint(0, 90)
bingoA2 = random.randint(0, 90)
bingoA3 = random.randint(0, 90)
bingoB1 = random.randint(0, 90)
bingoB3 = random.randint(0, 90)
bingoC1 = random.randint(0, 90)
bingoC2 = random.randint(0, 90)
bingoC3 = random.randint(0, 90)

myBingo = [[bingoA1, bingoA2, bingoA3],
           [bingoB1, "BINGO", bingoB3],
           [bingoC1, bingoC2, bingoC3]
]
#myBingo.sort()  - It only sorts the lines, not all the elements in the table.
#                 Also, it changes the position of "BINGO".

print("\033[1;33mDavid's Nan's Bingo Card Generator\033[0m")
print()

for lines in myBingo: #Iterates through the outer array
    for elements in lines: #Iterates through the inner arrays 
        print(f"{elements:^5} |", end = " ")
    print()
    print("--------------------")
#It's working, but I can't sort the numbers through the whole table.


"""
#First try
print(f"{myBingo[0][0]:^5} | {myBingo[0][1]:^5} | {myBingo[0][2]:^5}")
print("--------------------")
print(f"{myBingo[1][0]:^5} | {myBingo[1][1]:^5} | {myBingo[1][2]:^5}")
print("--------------------")
print(f"{myBingo[2][0]:^5} | {myBingo[2][1]:^5} | {myBingo[2][2]:^5}")
"""
