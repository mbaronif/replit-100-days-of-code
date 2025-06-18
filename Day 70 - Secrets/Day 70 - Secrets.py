import os

password = os.environ['password']

userPassword = input("Enter the password: ")
if userPassword == password:
    print("Access granted.")
else:
    print("Access denied.")
    exit()