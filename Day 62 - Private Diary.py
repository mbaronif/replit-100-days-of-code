#from replit import db

pass_word = "12345"

while True:
    print("MY PRIVATE DIARY")
    password = input("Password: ")
    if password == pass_word:
        print("Welcome to your private diary!")
        print("1. Add a new entry")
        print("2. View past entries")
        print("3. Close the diary")
        choice = input("Please choose an option (1-3): ")
    else:
        break
    
    if choice == "1":
        pass
    
    elif choice == "2":
        pass

    elif choice == "3":
        print("Goodbye!")
        break
