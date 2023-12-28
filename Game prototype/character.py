from weapons import weapons

class Start:
    def __init__(self) -> None:
        self.name = input("What's your name?:\n")
        self.max_health = 30
        self.health = 30
        self.strength = 5
        self.inventory = {
            "weapon": None,
            "food": [],
            "key_items": [],
        }
        self.weapon = {
            "name": "unarmed",
            "damage": 0,
        }
        print(f"Hello there {self.name}")
    
    def __str__(self) -> str:
        return self.name
    
    def get_weapon(self, weapon):
        self.weapon = weapons[weapon]

        return self.inventory["weapon"]
    def pick_up_item(self, item):
        self.inventory["key_items"].append(item)
        print(f"Your inventory is now: {", ".join(self.inventory["key_items"])}.")
    
    def damaged(self, damage, enemy):
        self.health -= damage
        print(f"\n{enemy} hit you for {damage} damage. Your health is now {self.health}.")
        if self.health <= 0:
            print("Unfortunately you have died.")
            return False
        
    def heal(self, life):
        self.health += life
        print(f"You've gained {life} hit points. Your health is now {self.health}.")

    def attack(self, target):
        total_damage = self.strength + self.weapon["damage"]
        target.take_damage(total_damage)