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
