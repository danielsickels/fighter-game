import random

class Fighter():
    def __init__(self, name, health = 20, defense = 5, strength = 5, speed = 5):
        self.name = name
        self.health = (health)
        self.defense = defense
        self.strength = strength
        self.speed = speed
        #self.intellect = intellect
        self.valid_actions = ["Stats", "Attack", "Defend", "Boost Speed", "Run Away"]
        self.action = ""

    def __repr__(self):
        return self.name
    
    def print_stats(self):
        print(f"Health: {self.health}")
        print(f"Defense: {self.defense}")
        print(f"Strength: {self.strength}")
        print(f"Speed: {self.speed}")
        #print(f"Intellect: {self.intellect}")
    
    def attack(self, other_player):
        damage = self.strength - other_player.defense
        if damage <= 0:
            damage = 0
        print(f"{self.name} did {damage} damage to {other_player.name}!")

    def take_damage(self, damage):
        self.health = self.health - damage
        if damage == 0:
            pass
        else:
            print(f"{self.name} is now at {self.health} health.")

    def defend(self):
        self.defense += 2

    def boost_speed(self):
        self.speed += 2
    
    def death(self):
        if self.health <= 0:
            print(f"{self.name} is dead.")    

class GameManager:
    def __init__(self):
        self.fighter_1 = Fighter("Danny", strength=18)
        self.fighter_2 = Fighter("Mike")
        self.active_fighter = self.fighter_1

    def start_turn(self):
        while True:
            print(f"The active fighter is {self.active_fighter}, please choose an action:")
            print(f"{self.fighter_1.valid_actions}")
            action = input().lower()

            if action == "stats":
                self.active_fighter.print_stats()
                if self.active_fighter == self.fighter_1:
                    self.active_fighter = self.fighter_2
                else:
                    self.active_fighter = self.fighter_2
            elif action == "attack":
                if self.active_fighter == self.fighter_1:
                    self.fighter_1.attack(self.fighter_2)
                    self.fighter_2.take_damage(damage = self.fighter_1.strength - self.fighter_2.defense)
                else:
                    self.fighter_2.attack(self.fighter_1)
                    self.fighter_1.take_damage(damage = self.fighter_2.strength - self.fighter_1.defense)
            elif action == "defend":
                self.active_fighter.defend()
                print(f"{self.active_fighter} is prepared for an attack! {self.active_fighter} is at {self.active_fighter.defense} defense.")
            elif action == "run away":
                if self.active_fighter == self.fighter_1:
                    inactive_fighter = self.fighter_2
                else:
                    inactive_fighter = self.fighter_1
                print(f"{self.active_fighter} ran away! {inactive_fighter} wins!")
                break
            else:
                print("Not a valid action - Sorry, you lost your turn!")

            if self.active_fighter == self.fighter_1:
                self.active_fighter = self.fighter_2
            else:
                self.active_fighter = self.fighter_1




gametime = GameManager()
gametime.start_turn()


# print(self.fighter_1.attack(self.fighter_2))
# print(self.fighter_1.attack(self.fighter_2))
# print(f"{self.fighter_2.name} has {self.fighter_2.health} health.")
