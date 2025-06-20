from replit import db
# replit is Replit's DB. I'm just copying it here for the sake of the exercise.
# Here it'd be better to use a real database like SQLite or MongoDB, 
# but for simplicity and to have an example, we'll use Replit's DB.

usernmae = "david"
password = "Baldy1"
password = hash(password)
db[usernmae] = password

print(password)

print(db["david"])  # This will print the hashed password

ask = input("Password >")
ask = hash(ask) # Hash the input password to compare with the stored hash
if ask == db["david"]: # Compare the hashed input with the stored hash
    print("Login successful")