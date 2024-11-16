name = input("Name: ").strip().capitalize()
birth = input("Date of birth: ").strip().capitalize()
phone = input("Phone number: ").strip()
email = input("Email address: ").strip()
address = input("Home address: ").strip().title()

contactCard = {"Name": name , 
               "Date of birth": birth, 
               "Phone number": phone, 
               "Email": email, 
               "Home address": address}

print()
print(f"Name: {contactCard['Name']}\nDate of birth: {contactCard['Date of birth']}\nPhone: {contactCard['Phone number']}\nEmail: {contactCard['Email']}\nHome address: {contactCard['Home address']}")
#Printing every element separetelly would make the code cleaner, and easy to customize.
