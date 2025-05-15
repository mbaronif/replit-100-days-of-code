"""
This makes a template for a class:

class className:
    property1 = None #Properties (the data) stored in the class
    property1 = None
    property1 = None

def __init__ (self, property1, property2, property3):
    code here

    className.especies      -   returns the data stored in this class as the variable species
    className.method()     -   calls the method stored in this class
"""

class animal: # Class name 
    species = None #Properties (the data) stored in the class
    name = None
    sound = None

#Initialization - this code will be run as soon as the class is included
    def __init__ (self, name, species, sound): #Methods (subroutines) stored in the class
    #self must be included, and refers to the actual instance of the class
    #Methods must be indented inside the class
        self.name = name
        self.species = species
        self.sound = sound 
    
    def talk(self):
        print(f"""{self.name} says {self.sound}""")
    
class bird(animal):
    
    color = None #This is a property of the bird class, not the animal class
    
    def __init__ (self, color):
        self.name = "Bird"
        self.species = "Avian"
        self.sound = "Tweet"
        self.color = color #New property for the bird class

dog = animal("Dog", "Canine", "Woof")
dog.talk() #With the new method (talk), we can call the variable as a command

cow = animal("Cow", "Bovine", "Moo")
cow.talk()

polly = bird("Green") #Argument of the new property
polly.talk()
print(polly.color)
