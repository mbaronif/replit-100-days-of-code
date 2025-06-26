import sqlite3
import datetime
import os
import time
import random
import hashlib

#---DATABASE SETUP---
# Connect to SQLite database and create a cursor
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "diary.db")
conn = sqlite3.connect(db_path) # Connects to the database
cursor = conn.cursor() # Creates a cursor object to interact with the database

# Create the diary table, if it doesn't exist yet
cursor.execute("""
CREATE TABLE IF NOT EXISTS diary (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL,
    timestamp TEXT NOT NULL
)
""")

# Creates the users table, if it doesn't exist yet
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    salt TEXT NOT NULL
)
""")

conn.commit()

#---USER AUTHENTICATION---
# Checks for users in the database
def check_keys():
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    if count < 1:
        print("New user. Create an account.")
        new_user()

# Gives a consistent hash across sessions
def hash_password(password, salt):
    return hashlib.sha256((password + salt).encode()).hexdigest()

# Creates a new user, if there isn't any in the database
def new_user():
    username = input("Username: ")
    password = input("Password: ")
    salt = str(random.randint(1001,9999))
    salted_password = f"{password}{salt}"
    hashed_password = hash_password(password, salt)
    # Stores user in the users table
    cursor.execute("INSERT INTO users (username, password, salt) VALUES (?, ?, ?)",(username, hashed_password, salt))
    conn.commit()

#    return username, password

# Authenticates the user
def login():
    entry_user = input("Username: ")
    entry_password = input("Password: ")
    # Searches for user in the users table
    cursor.execute("SELECT password, salt FROM users WHERE username = ?", (entry_user,))
    result = cursor.fetchone()

    if result is None:
        print ("User not found. Access denied.")
        exit()
    # Checks the password in the users table
    stored_hashed_pass, salt = result
    if hash_password(entry_password, salt) == stored_hashed_pass:
        print("Welcome to the diary.")
    else:
        print("Incorrect password. Access denied.")
        exit()

#---DIARY MENU---
def diary_menu():
    print("Welcome to your private diary!\n")
    print("1. Add a new entry")
    print("2. View past entries")
    print("3. Close the diary")
    print()

#---MAIN PROGRAM---
print("MY PRIVATE DIARY\n")
print("This is a private diary. To get access, please, use your credentials.\n")

check_keys()
login()

time.sleep(1)
os.system("clear")

while True:
    diary_menu()
    choice = input("Please choose an option (1-3): ")
    time.sleep(0.5)
    os.system("clear")

    #Add
    if choice == "1":
        diary_entry = input("What are the news for today? >  ")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Get the entry's current date and time
        cursor.execute("INSERT INTO diary (content, timestamp) VALUES (?, ?)", (diary_entry, timestamp))
        conn.commit() # Save the entry in the database
        print("Entry saved!")
        time.sleep(0.5)
        os.system("clear")
        
    #View
    elif choice == "2":
        cursor.execute("SELECT * FROM diary ORDER BY timestamp DESC") # Show the entries in descending order, one by one
        entries = cursor.fetchall() # Fetch all entries from the database and save in the 'entries' variable
        
        if not entries: # If there are no entries in the database
            print("No entries found.")
            time.sleep(0.5)
            os.system("clear")
            continue
        else:
            index = 0

            while index < len(entries): # While there are still entries to show
                entry = entries[index]
                print(f"Date: {entry[2]}\nEntry: {entry[1]}\n")

                index += 1 # Increment the index to show the next entry

                if index < len(entries): # Check whether there are more entries to show
                    while True:
                        next_entry = input("Do you want to see the next entry? Yes/No: ").strip().lower()
                        time.sleep(0.8)
                        os.system("clear")
                        if next_entry == "no":
                            index = len(entries)  # Force outer loop to end
                            break
                        elif next_entry == "yes":
                            break
                        else:
                            print("Invalid input. Please enter 'Yes' or 'No'.\n")
                            continue
                else: # If there are no more entries to show, let the user know
                    print("This is the last entry.")
                    time.sleep(2)
                    os.system("clear")
                    break
    
    elif choice == "3":
        print("Goodbye!")
        time.sleep(1)
        os.system("clear")
        break

conn.close() # Close the database connection