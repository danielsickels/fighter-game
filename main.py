import random

class Fighter():
    def __init__(self, name, health = 20, defense = 5, strength = 5, speed = 5, intellect = 5):
        self.name = name
        self.health = health
        self.defense = defense
        self.strength = strength
        self.speed = speed
        self.intellect = intellect
        self.valid_actions = ["Attack", "Defend", "Boost Speed"]

    def __repr__(self):
        return self.name
    
    def print_stats(self):
        print(f"Health: {self.health}")
        print(f"Defense: {self.defense}")
        print(f"Strength: {self.strength}")
        print(f"Speed: {self.speed}")
        print(f"Intellect: {self.intellect}")
    
    def attack(self, other_player):
        damage = self.strength - other_player.defense
        if damage <= 0:
            damage = 0
        other_player.health -= damage
        return f"{self.name} did {damage} damage to {other_player.name}!"
        

    def defend(self):
        self.defense += 1
        self.speed += 1
    
    def boost_speed(self):
        self.speed += 2    
    

big_d = Fighter("Danny", strength= 8)
lil_d = Fighter("Mike")

current_attacker = big_d

if big_d.speed < lil_d.speed:
    current_attacker = lil_d

print(big_d.attack(lil_d))
print(big_d.attack(lil_d))
print(f"{lil_d.name} has {lil_d.health} health.")
