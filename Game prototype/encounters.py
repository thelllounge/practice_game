from weapons import weapons
from random import randint
class Enemy:
    def __init__(self, weapon, name):
        self.name = name
        self.level = 0
        self.total_hitpoints = 0
        self.current_hitpoints = 0
        self.base_damage = 0
        self.weapon = weapons[weapon]
        self.weapon_damage = self.weapon["damage"]
        self.type = "lackey"
        self.accuracy = 100

        
    def attack(self, target):
        hit_roll = randint(1,100)
        total_damage = self.base_damage + self.weapon_damage
        if hit_roll <= self.accuracy:
            target.damaged(total_damage, self.name)
            print(target.health) #there is something wrong and the message in the player's damaged function isn't printing I think.
        else:
            print(f"{self.name} missed!\n")

class Boss(Enemy):
    def __init__(self, weapon, name):
        super().__init__(weapon, name)

    def take_damage(self, damage):
        self.current_hitpoints -= damage
        if self.current_hitpoints <= 0:
            print(f"\nYou have defeated {self.name}.")
        if self.type == "lackey":
            print(f"{self.name}'s life is {self.current_hitpoints}/{self.total_hitpoints}")
        elif self.type == "boss":
            if self.current_hitpoints > self.total_hitpoints * .75:
                print(f"{self.name} seems fine.")
            elif self.current_hitpoints > self.total_hitpoints * .5:
                print(f"{self.name} isn't happy.")
            elif self.current_hitpoints > self.total_hitpoints * .25:
                print(f"{self.name} is swaying on their feet.")
            elif self.current_hitpoints <= self.total_hitpoints * .25:
                print(f"{self.name} looks really bad.")
    
class Goblin(Enemy):
    def __init__(self, weapon, name) -> None:
        super().__init__(weapon, name)
        self.level = 1
        self.total_hitpoints = 10
        self.current_hitpoints = 10
        self.base_damage = 5
        self.accuracy = randint(30, 45)
    
    def take_damage(self, damage):
        if self.current_hitpoints <= 0:
            print("This creature is already dead.")
            pass
        else:
            self.current_hitpoints -= damage
            if self.current_hitpoints <= 0:
                print(f"\nYou have defeated {self.name}.\n")

class GoblinLord(Boss):
    def __init__(self, weapon, name):
        super().__init__(weapon, name)
        self.name = f"{name}, the Goblin Lord"
        self.level = 10
        self.total_hitpoints = 50
        self. current_hitpoints = 50
        self.base_damage = 10
        self.type = "boss"
        self.accuracy = 70