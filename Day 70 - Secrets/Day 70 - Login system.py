import os

userID= os.environ['userID']
userPassword = os.environ['userPassword']

adminID = os.environ['adminID']
adminPassword = os.environ['adminPassword']

while True:
    loginID = input("Enter your ID: ")

    if  loginID == userID:
        userPass = input("Enter your password: ")
        if userPass != userPassword:
            print("Access denied.")
        else:
            print("Hello, user!")
            break
    elif loginID == adminID:
        adminPass = input("Enter your password: ")
        if adminPass != adminPassword:
            print("Access denied.")
        else:
            print("Hello, admin!")
            break
    else:
        print("Access denied.")