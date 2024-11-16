webpages = {"Name" : None, "URL" : None, "Description" : None, 
            "Rating" : None,}

#Brute force:
while True:
    #Inputs
    name = input("Website's name: ").strip().title()
    url = input("Webpage's URL: ").strip().lower()
    desc = input("Webpage's description: ").strip().capitalize()
    #This makes sure every numerical input for Rating will be something between 1 and 5.
    while True:
        try:
            rating = int(input("Wepage's rating, from 1 to 5: ").strip())
            if rating <= 0:
                rating = 1
            elif rating >= 5:
                rating = 5
            break
        except ValueError:
            # Handles non-numeric inputs.
            print("Invalid rating input! It must be a number.")
    print()

    #Addition of new values to the dictionary
    webpages["Name"] = name
    webpages["URL"] = url
    webpages["Description"] = desc
    webpages["Rating"] = rating

    for name, value in webpages.items():
        #Adds the '/ 5' rating limit.
        if (value == rating):
            print(f"{name}: {rating} / 5")
        else:
            print(f"{name}: {value}")
    break


"""#Simpler way:
#It's missing some style I've added to the 'Brute force' version, though.
for name, value in webpages.items():
    webpages[name] = input(f"{name}: ")

print()

for name, value in webpages.items():
    print(f"{name}: {value}")"""
