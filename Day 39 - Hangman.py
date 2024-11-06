#My version - with many bugs

import random

hangmanWords = [
    "apple", "banana", "strawberry", "orange", "grapes",
    "avocado", "mango", "melon", "cherry", "pear"]
#Try to replace that for a bigger list later. Maybe there's a ready dictionary elsewhere.

rightWord = random.choice(hangmanWords) # Picks a word randomly
print(rightWord) #Note: Take this off when the program is complete.

found = [False] * len(rightWord)
# Creates a new list where the characters of the word are understood as false until
# they're discovered. Then, they become true, and are replaced by the correct letter.
letterBank = [] #Creates a list of letters that have already been used in the game, right or wrong.

lives = 5

while True:
    character = input("Choose a letter: ").lower() # Makes sure all letter inputs are accepted

    guess = "" # New list with the letters used
    letterBank.append(character)
    
    for position in range(0, len(rightWord)):
        if rightWord[position] == character[0] or found[position]:
            guess = guess + rightWord[position]
            found[position] = True
        else:
            guess = guess + "_ " #WRONG: It's not printing correctly anymore. Now it prints only 1 "_" after the inputted letter.
            break

    if guess == rightWord: # Checks if the word is completed.
        print(f"You found the word with {lives} left.")
        break

    if guess not in rightWord: # Counts down the lives after each mistake.
        #WRONG: It's considering even correct guesses.
        lives -= 1
        print("Nope, not in there")
        print(f"Only {lives} lives left")
        if lives == 0:
            print("Game over!")
            break

    print("Letters tried so far: ", letterBank)
    print(f"Current word: {guess}")

    
    #    letterBank.append(character)
    #    if character in letterBank:
    #    print("That letter was already tried.")
    #    continue
    
