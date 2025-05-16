class Character:
    name = None
    health = None
    mp = None #mp = magic points

    def __init__(self, name, health, mp):
        self.name = name
        self.health = health
        self.mp = mp

    def characterInfo(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Magic Points: {self.mp}")

class Player(Character):

    def __init__(self, name, health, mp, nickname, lives):
        super().__init__(name, health, mp)
        self.nickname = nickname
        self.lives = lives

    def characterInfo(self):
        super().characterInfo()
        print(f"Nickname: {self.nickname}")
        print(f"Lives: {self.lives}")    

class Enemy(Character):

    def __init__(self, name, health, mp, type, strength):
        super().__init__(name, health, mp)
        self.type = type
        self.strength = strength

    def characterInfo(self):
        super().characterInfo()
        print(f"Type: {self.type}")
        print(f"Strength: {self.strength}")

class Orc(Enemy):

    def __init__(self, name, health, mp, strength, speed):
        super().__init__(name, health, mp, "Orc", strength)
        self.speed = speed
    
    def characterInfo(self):
        super().characterInfo()
        print(f"Speed: {self.speed}")

class Vampire(Enemy):
    day = None

    def __init__(self, name, health, mp, strength, day):
        super().__init__(name, health, mp, "Vampire", strength)
        self.day = day
    
    def characterInfo(self):
        super().characterInfo()
        print(f"Day: {self.day}")

player1 = Player("Cameron Harvey", 100, 50, "Cameron", 3)

orc1 = Orc("Garzonk", 100, 60, 20, 20)
orc2 = Orc("Wubdagog", 100, 60, 10, 20)
orc3 = Orc("Drutha", 100, 60, 15, 20)

vampire1 = Vampire("Sabien", 100, 80, 80, day="Night")
vampire2 = Vampire("Griffin", 100, 80, 80, day="Day")


player1.characterInfo()
print(f"-----------------------")
orc1.characterInfo()
print(f"-----------------------")
orc2.characterInfo()
print(f"-----------------------")
orc3.characterInfo()
print(f"-----------------------")
vampire1.characterInfo()
print(f"-----------------------")
vampire2.characterInfo()
print(f"-----------------------")