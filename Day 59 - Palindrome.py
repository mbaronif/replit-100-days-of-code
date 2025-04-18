#Top menu
print("PALINDROME CHECKER\n")
print("Enter a word to check if it's a palindrome.\n")
word_input = input("> ").strip().lower()
print()

def palindrome_checker():
    # Reads the word backwards and compare it to the original word
    if word_input == word_input[::-1]:
        print("TRUE")
    else:
        print("FALSE")

palindrome_checker()