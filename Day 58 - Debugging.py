import random
totalAttempts = 0

def game():
    attempts = 0
    """ Removed this variable from the while loop.
    Inside it, it was generating a new random number every time.
    This way, it will keep the generated random number."""
    number = random.randint(1,100)

    while True:
        guess = int(input("Pick a number between 1 and 100: "))
        if guess > number:
            print("Too high")
            attempts += 1
        elif guess < number:
            print("Too low")
            attempts += 1
        else:
            print("Just right!")
            print(f"{attempts} attempts this round")
            return attempts
        
while True:
    menu = input("1: Guess the random number game\n2: Total Score\n3: Exit\n> ")
    # Put the number in "" to make it a string.
    # This way, the input is recognized.
    if menu == "1":
        totalAttempts += game()
    elif menu == "2":
        print(f"You've had {totalAttempts} attempst")
    # I've added the option "3", as it's one of the options in the menu.
    # This was just for readability.
    elif menu == "3":
        break
    # Added an else statement to handle invalid inputs.
    # This way, any invalid input will lead to a prompt to try again.
    # The user will be sent back to the menu and will be able to try again.
    else:
        print("Invalid input, please try again.")
        continue