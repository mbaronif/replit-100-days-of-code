import sqlite3
import datetime
import os
import time

# Connect to SQLite database and create a cursor
conn = sqlite3.connect('diary.db') # Connects to the database
cursor = conn.cursor() # Creates a cursor object to interact with the database

# Create the diary table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS diary (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL,
    timestamp TEXT NOT NULL
)
""")

pass_word = "12345" # Clear the console screen

print("MY PRIVATE DIARY\n")
password = input("Password: ")
time.sleep(0.5)
os.system("clear")

# Checks if the password is correct
if password != pass_word:
    print("Incorrect password. Access denied.")
    exit() # Exit the program if the password is incorrect

def diary_menu():
    print("Welcome to your private diary!\n")
    print("1. Add a new entry")
    print("2. View past entries")
    print("3. Close the diary")
    print()

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