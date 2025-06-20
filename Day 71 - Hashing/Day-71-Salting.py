from replit import db

password = "Baldy1"
salt = 10221
newPassword = f"{password}{salt}"  # Concatenate password and salt
newPassword = hash(newPassword)  # Hash the concatenated string

print(newPassword)
db["david"] = {"password": newPassword, "salt": salt}  # Store the hash and salt in the database

ans = input("Password > ")
salt = db["david"]["salt"]  # Retrieve the salt from the database
newPassword = f"{ans}{salt}"  # Concatenate input password with the salt
newPassword = hash(newPassword)  # Hash the concatenated string
if newPassword == db["david"]["password"]:  # Compare the hashed input with the stored hash
    print("Login successful")