import random

class Fighter():
    def __init__(self, name, health = 50, defense = 5, strength = 5, speed = 5, intellect = 5):
        self.name = name
        self.health = health
        self.defense = defense
        self.strength = strength
        self.speed = speed
        self.intellect = intellect
    
    def __repr__(self):
        return self.name
    
    def print_stats(self):
        print(f"Health: {self.health}")
        print(f"Defense: {self.defense}")
        print(f"Strength: {self.strength}")
        print(f"Speed: {self.speed}")
        print(f"Intellect: {self.intellect}")

big_d = Fighter("Danny")
lil_d = Fighter("Mike", speed = 6)

current_attacker = big_d

if big_d.speed < lil_d.speed:
    current_attacker = lil_d