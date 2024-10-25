print ("Star Wars Name Generator")

# Brute force try

firstName = input("First name: ").strip().capitalize() # The first letter needs to be capitalized.
lastName = input("Last name: ").strip().lower() # The first letter needs to be lower-case.
mumsName = input("Mum's name: ").strip().capitalize() # The first letter needs to be capitalized.
cityBorn = input("Place where you were born: ").strip().lower() # The first letter needs to be lower-case.

firstSW = firstName[:3] # It's not couting from 0, apperently.
lastSW = lastName[:2] # It's not couting from 0, apperently.
mumSW = mumsName[:2] # It's not couting from 0, apperently.
citySW = cityBorn[:4:-1] # The only one which is "counting" characters correctly.

starWarsName = f"{firstSW}{lastSW} {mumSW}{citySW}"

print(starWarsName)

"""
# Alternative 1:

firstName = input("First name: ").strip()
lastName = input("Last name: ").strip()
mumsName = input("Mum's name: ").strip()
cityBorn = input("Place where you were born: ").strip()

starWarsName = f"{firstName[:3].title()}{lastName[:3].lower()} {mumsName[:2].title()}{cityBorn[:4:-1].lower()}"
print(starWarsName)

# Alternative 2
# Although simpler, more error-prone

all = input("Enter your first name, last name, mum's maiden name, and the city you were born in: ").split()

first = all[0].strip()
last = all[1].strip()
maiden = all[2].strip()
city = all[3].strip()

starWarsName = f"{first[:3].title()}{last[:2].lower()} {maiden[:2].title()}{city[:4:-1].lower()}"
print(starWarsName)
"""
