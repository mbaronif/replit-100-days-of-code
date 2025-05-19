class Character: #Basic character
    name = None
    health = 100
    mp = 100 #mp = magic points

    def __init__(self, name):
        self.name = name

    def setStats(self, health, mp):
        self.health = health
        self.mp = mp

    def characterInfo(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Magic Points: {self.mp}")
class Player(Character):
    nickname = None
    lives = 3 # Initial number of lives

    def __init__(self, name, nickname, lives):
        super().__init__(name)
        self.nickname = nickname

    def isAlive(self): # Check if player is alive
        if self.lives > 0:
            print(f"{self.nickname} is alive")
            return True
        else:
            print(f"{self.nickname} has died")
            return False
    
    def characterInfo(self):
        super().characterInfo()
        print(f"Nickname: {self.nickname}")
        print(f"Lives: {self.lives}")

class Enemy(Character):
    type = None
    strength = None

    def __init__(self, name, type, strength):
        super().__init__(name)
        self.type = type
        self.strength = strength

    def characterInfo(self):
        super().characterInfo()
        print(f"Type: {self.type}")
        print(f"Strength: {self.strength}")
class Orc(Enemy):
    speed = None

    def __init__(self, name, strength, speed):
        super().__init__(name, "Orc", strength)
        self.speed = speed
    
    def characterInfo(self):
        super().characterInfo()
        print(f"Speed: {self.speed}")

class Vampire(Enemy):
    day = None

    def __init__(self, name, strength, day):
        super().__init__(name, "Vampire", strength)
        self.day = day
    
    def isDay(self): # Check if it's day or night
        if self.day == "Day":
            print(f"{self.name} is weak during the day")
            return True
        else:
            print(f"{self.name} is strong during the night")
            return False
        
    def characterInfo(self):
        super().characterInfo()
        print(f"Day: {self.day}")

player1 = Player("Cameron Harvey", "Cameron", 3) # Class's specific info
player1.setStats(100, 100) # Player's stats

orc1 = Orc("Garzonk", 60, 20)
orc1.setStats(100, 20)
orc2 = Orc("Wubdagog", 60, 10)
orc2.setStats(100, 20)
orc3 = Orc("Drutha", 60, 15)
orc3.setStats(100, 20)

vampire1 = Vampire("Sabien", 80, day="Night")
vampire1.setStats(100, 80)
vampire2 = Vampire("Griffin", 80, day="Day")
vampire2.setStats(100, 80)

player1.characterInfo()
print("-----------------------")
orc1.characterInfo()
print("-----------------------")
orc2.characterInfo()
print("-----------------------")
orc3.characterInfo()
print("-----------------------")
vampire1.characterInfo()
print("-----------------------")
vampire2.characterInfo()
print("-----------------------")ß