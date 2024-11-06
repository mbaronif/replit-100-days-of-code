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


# Working version (solution)
import random

hangmanWords = [
    "apple", "banana", "strawberry", "orange", "grapes",
    "avocado", "mango", "melon", "cherry", "pear"]

#Creates a list of letters that have already been used in the game, right or wrong.
letterBank = []

lives = 6

word = random.choice(hangmanWords) # Picks a word randomly

while True:
    character = input("Choose a letter: ").lower() # Makes sure all letter inputs are accepted

# Checks if the letter was already picked
    if character in letterBank:
        print("You've tried that before")
# If True, the player is prompted for a new letter
        continue

# Adds the letters picked to the letterBank, if it was not a repetition
    letterBank.append(character)

# Checks if the character is in the chosen word
    if character in word:
        print("You found a letter")
    else:
        print("Nope, not in there")
        lives -= 1
    
    allLetters = True

# This part is unindented because it has to occur regardless of the 2 if statements above
    print()
# If it's in the word, it'll check every position of the word
    for letter in word:
        if letter in letterBank:
# The letter is printed in the right position
            print(letter, end="")
        else:
# The gap sign will be put in place of the undiscovered letters
            print("_ ", end="")
            allLetters = False
    print()

# Checks if the word is complete
    if allLetters:
        print(f"You won with {lives} left!")
        break

# Checks the number of lives still available
    if lives <= 0:
        print(f"You ran out of lives. The answer was {word}.")
# If the player's out of lives, the game is broken
        break
# Tells the player how many lives they have left, if they haven't ran out of lives yet
    else:
        print(f"Only {lives} left.")
