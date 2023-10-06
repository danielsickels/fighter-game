import random

class Fighter():
    def __init__(self, name, health = 20, defense = 5, strength = 5, speed = 5):
        self.name = name
        self.health = health
        self.defense = defense
        self.strength = strength
        self.speed = speed
        #self.intellect = intellect
        self.valid_actions = ["Stats", "Attack", "Rage", "Defend", "Boost Speed", "Run Away"]
        self.action = ""

    def __repr__(self):
        return self.name
    
    def print_stats(self):
        print(f"Health: {self.health}")
        print(f"Defense: {self.defense}")
        print(f"Strength: {self.strength}")
        print(f"Speed: {self.speed}")
        #print(f"Intellect: {self.intellect}")
        print("")
    
    def attack(self, other_player):
        self.strength += 1
        damage = self.strength - other_player.defense
        if damage <= 0:
            damage = 0
        print(f"{self.name} did {damage} damage to {other_player.name}!")
        print("")
    
    def rage(self, other_player):
        self.strength += 3
        self.defense -= 1
        damage = self.strength - other_player.defense
        if damage <= 0:
            damage = 0
        print(f"{self.name} did {damage} damage to {other_player.name}!")
        print(f"{self.name} is exhausted, defense reduced by 1.")
        print("")

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

class GameManager:
    def __init__(self):
        self.fighter_1 = Fighter("Danny")
        self.fighter_2 = Fighter("Mike")
        self.active_fighter = self.fighter_1
        self.is_dead = False
    
    def check_for_death(self, active_fighter):
        if active_fighter.health <= 0:
            return True
        return False

    def start_turn(self):
        while not self.is_dead:
            print(f"The active fighter is {self.active_fighter}, please choose an action:")
            print(*self.fighter_1.valid_actions, sep = ", ")
            action = input().lower()

            if action == "stats":
                self.active_fighter.print_stats()
                if self.active_fighter == self.fighter_1:
                    self.active_fighter = self.fighter_2
                else:
                    self.active_fighter = self.fighter_1

            elif action == "attack":
                if self.active_fighter == self.fighter_1:
                    self.fighter_1.attack(self.fighter_2)
                    damage = self.fighter_1.strength - self.fighter_2.defense
                    if damage <= 0:
                        damage = 0
                    self.fighter_2.take_damage(damage)
                else:
                    self.fighter_2.attack(self.fighter_1)
                    damage = self.fighter_2.strength - self.fighter_1.defense
                    if damage <= 0:
                        damage = 0
                    self.fighter_1.take_damage(damage)
            
            elif action == "rage":
                if self.active_fighter == self.fighter_1:
                    self.fighter_1.rage(self.fighter_2)
                    damage = self.fighter_1.strength - self.fighter_2.defense
                    if damage <= 0:
                        damage = 0                    
                    self.fighter_2.take_damage(damage)
                else:
                    self.fighter_2.rage(self.fighter_1)
                    damage = self.fighter_2.strength - self.fighter_1.defense
                    if damage <= 0:
                        damage = 0                    
                    self.fighter_1.take_damage(damage)

            elif action == "defend":
                self.active_fighter.defend()
                print(f"{self.active_fighter} is prepared for an attack! {self.active_fighter} is at {self.active_fighter.defense} defense.")
                print("")
                
            elif action == "boost speed":
                self.active_fighter.boost_speed()
                print(f"{self.active_fighter} is feeling energetic! Their speed is {self.active_fighter.speed}")
                print("")

            elif action == "run away":
                if self.active_fighter == self.fighter_1:
                    inactive_fighter = self.fighter_2
                else:
                    inactive_fighter = self.fighter_1
                print(f"{self.active_fighter} ran away! {inactive_fighter} wins!")
                break

            else:
                if self.active_fighter == self.fighter_1:
                    self.active_fighter = self.fighter_2
                else:
                    self.active_fighter = self.fighter_1
                print(f"Not a valid action, please choose wisely.")
                print("")
                
            if self.active_fighter == self.fighter_1:
                self.active_fighter = self.fighter_2
            else:
                self.active_fighter = self.fighter_1
            
            if self.check_for_death(self.fighter_1):
                print(f"{self.fighter_1.name} has died. {self.fighter_2.name} wins!")
                self.is_dead = True
            elif self.check_for_death(self.fighter_2):
                print(f"{self.fighter_2.name} has died. {self.fighter_1.name} wins!")
                self.is_dead = True



gametime = GameManager()
gametime.start_turn()
