# Imports the DB library from the replit DB
#from replit import db
import datetime

tweet = {}

def main_menu():
    print("Welcome to your personal and private Tweeter!")
    print("Choose from the options below:")
    print("1. Add a tweet")
    print("2. View all tweets")
    print("3. Exit")

while True:
    main_menu()
    choice = input("> ")

    if choice == "1":
        print("Add a tweet")
        timestamp = datetime.datetime.now() 
        tweet[timestamp] = input(f"🦜 > ")

    elif choice == "2":
        if not tweet:
            print("No tweets available.")
        
        else:
        # Sort tweets by timestamp, from most recent to oldest
            tweet_keys = sorted(tweet.keys(), reverse=True)
            page_size = 10
            start = 0
        
        # Display the first 10 tweet_keys in the DB
        while start < len(tweet_keys):
            end = start + page_size
            for time in tweet_keys[start:end]:
                print(f"{time}: {tweet[time]}")

            start = end  # Move to next page

                # Check if there are more tweets to display
            if start < len(tweet_keys):
                # Ask whether the user wants to see the next 10 tweets
                print("\nShow next tweets?")
                print("1. Yes")
                print("2. No")
                showMore = input("> ")
                if showMore != "1":
                    break
            else:
                print("No more tweets to show.\n")
                break
                
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

