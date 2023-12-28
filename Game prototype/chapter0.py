import random
import encounters
import stuff

class ChapterZero:
    def __init__(self) -> None:
        pass
        
    def wakeUp(self, character):
        print("\nYou wake up in your bed and hear a lot of chaos.")
        answering = True
        while answering == True:
            answer1 = input("Do you get your weapon(1) or do you go back to sleep(2)?:\n")
            if answer1 == "1":
                character.get_weapon("sword")
                print("You see some goblins. Prepare to fight.")
                if not self.encounter_goblins(character):
                    print("You shall not pass")
                    break
                if not self.encounter_goblin_lord(character):
                    break
                answering == False
                # break
                #I can't remember why this break was here but I can't test taking it out until I fix the boss fight.
            elif answer1 == "2":
                print("You die in bed when someone breaks in your room and stabs you.\n")
                answering == False
                break
            else:
                print("Please answer 1 or 2.")           


    def encounter_goblins(self, character):
        number = random.randint(2,5)
        goblins = stuff.create_encounter(encounters.Goblin, "Goblin", 1, number)

        while sum([goblin.current_hitpoints for goblin in goblins]) > 0:
            print("\n")
            for goblin in goblins:
                print(f"{goblin.name} is level {goblin.level}, has a {goblin.weapon["name"]}, and has {goblin.current_hitpoints}/{goblin.total_hitpoints}hp.")
            choice = input("\nWhat do you want to?: attack or run\n")
            if choice == "attack":
                target = input("\nWhich enemy to do you want to attack?\n").capitalize()
                for goblin in goblins:
                    if goblin.name == target:
                        character.attack(goblin)
                        
            for goblin in goblins:
                if goblin.current_hitpoints > 0:
                    goblin.attack(character)
            for goblin in goblins:
                if goblin.current_hitpoints <= 0:
                    goblins.remove(goblin)
            if character.health <= 0:
                return False
            else:
                return True
        print("You have defeated all of the goblins. Now you must find out why they were attacking!\n")

    def encounter_goblin_lord(self, character):
        number = random.randint(3,7)
        goblins = stuff.create_encounter(encounters.Goblin, "Goblin", 1, number)
        goblins.append(encounters.GoblinLord("sword", "George"))
        for goblin in goblins:
            print(f"{goblin.name}'s weapon is a {goblin.weapon["name"]}. They have {goblin.current_hitpoints}, and their accuracy is {goblin.accuracy}.")
#Need to make it work for the boss, can't attack properly
        while sum([goblin.current_hitpoints for goblin in goblins]) > 0:
            print("\n")
            for goblin in goblins:
                print(f"{goblin.name} is level {goblin.level}, has a {goblin.weapon["name"]}, and has {goblin.current_hitpoints}/{goblin.total_hitpoints}hp.")
            choice = input("\nWhat do you want to?: attack or run\n")
            if choice == "attack":
                target = input("\nWhich enemy to do you want to attack?\n").capitalize()
                for goblin in goblins:
                    if goblin.name == target:
                        character.attack(goblin)
                        
            for goblin in goblins:
                if goblin.current_hitpoints > 0:
                    goblin.attack(character)
            for goblin in goblins:
                if goblin.current_hitpoints <= 0:
                    goblins.remove(goblin)
            if character.health <= 0:
                return False
            else:
                return True