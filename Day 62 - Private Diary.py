#from replit import db

pass_word = "12345"

while True:
    print("MY PRIVATE DIARY")
    password = input("Password: ")
    # Condition to display the menu and diary
    if password == pass_word:
        print("Welcome to your private diary!")
        print("1. Add a new entry")
        print("2. View past entries")
        print("3. Close the diary")
        choice = input("Please choose an option (1-3): ")
    else:
        break
    
    # Conditions to work with the diary
    if choice == "1":
        entry = input("What are the news for today? >  ")
        # It needs to save the entry to a db
        pass
    
    elif choice == "2":
        # It needs to display the entries from the db
        # Then, prompt the user wether to see the next entry or to go back to the menu
        # Next entry must be displayed in reversed order (using reverse module)
        pass

    elif choice == "3":
        print("Goodbye!")
        break
