f = open("hi.score", 'a+')

while True:
    initials = input("Enter your initials: ").upper()
    score = input("Enter your score: ")
    f.write(f"{initials} {score}\n")
    print("Score saved!")
    print("Do you want to save another score?")
    answer = input("Y/N: ")
    if answer.lower() != 'y':
        break

print("Thanks for playing!\nYour scores are saved!")
f.close()