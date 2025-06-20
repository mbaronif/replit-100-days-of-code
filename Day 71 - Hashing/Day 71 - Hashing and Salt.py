from replit import db
""" replit is Replit's DB. As I don't have access to this database, I'm using it as an example.
Here it'd be better to use a real database, like SQLite or MongoDB, but for simplicity, I'll use Replit's DB."""
import random

# Menu
print("Login System\nChoose an option:\n\n1. New User\n2. Login\n3. Exit")

# Registers a new user
def new_user():
    #Prompts the credentials of a new user
    username = input("Enter a username: ")
    password = input("Enter a new password: ")
    # Generates a random salt code
    salt = str(random.randint(1001, 9999))
    # Appends the salt to the password created
    salted_password = f"{password}{salt}"
    # Hashes the new password
    new_password = hash(salted_password)
    # Saves the new credentials to the DB
    db[username] = {
        "password": new_password,
        "salt": salt}
    # Makes the variables "user" and "password" usable outside this fuction
    return username, password

# Prompts and verify existing credentials
def login():
    # Prompts the user for existing credentials
    entry_user = input("Enter your username: ")
    entry_pass = input("Enter your password: ")
     
    # Checks whether the user is in the DB
    if entry_user not in db:
        print("User not found.")
        return
    
    stored_info = db[entry_user] # Searches the DB to verify whether the credentials entered in this fuctions exists
    salt = stored_info["salt"] # Retrives the "salt" of an existing credential from the DB
    hashed_pass = stored_info["password"] # Retrives the hashed "password" of an existing credential from the DB
   
   # Recreates the credentials the user inputed, and checks whether they are the same ones saved on the DB
    if hash(entry_pass + salt) == hashed_pass:
        print("You've logged in successfully.")
    else:
        print("Incorrect password.")


while True:
    menuOption = input("> ")
    if menuOption == "1":
        new_user()
    elif menuOption == "2":
        login()
    elif menuOption == "3":
        print("Exiting the system.")
        break
    else:
        print("Invalid option. Please try again.")