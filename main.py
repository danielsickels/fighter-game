import random

class Fighter:
    def __init__(self, name, health=20, defense=5, strength=5, speed=5):
        self.name = name
        self.health = health
        self.defense = defense
        self.strength = strength
        self.speed = speed
        self.valid_actions = ["stats", "attack", "defend", "boost speed", "run away"]

    def __repr__(self):
        return self.name

    def print_stats(self):
        stats = (f"Health: {self.health}\n"
                f"Defense: {self.defense}\n"
                f"Strength: {self.strength}\n"
                f"Speed: {self.speed}")
        print(stats)
    
    def attack(self, opponent):
        self.strength += 1
        strength_swing = random.randint(-2, 2)
        defense_swing = random.randint(-2, 2)
        
        effective_strength = self.strength + strength_swing
        effective_defense = opponent.defense + defense_swing
        
        damage = max(0, effective_strength - effective_defense)
        opponent.take_damage(damage)
        print(f"{self.name} did {damage} damage to {opponent.name}!")

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} is now at {self.health} health.")
        if self.health <= 0:
            print(f"{self.name} is dead.")

    def defend(self):
        self.defense += 2
        print(f"{self.name}'s defense increased to {self.defense}.")

    def boost_speed(self):
        self.speed += 2
        print(f"{self.name}'s speed increased to {self.speed}.")

    def get_effective_speed(self):
        return self.speed + random.randint(-2, 2)

class FightinTime:
    def __init__(self):
        player_names = self.get_player_names()
        self.fighters = [Fighter(player_names[0]), Fighter(player_names[1])]

    def get_player_names(self):
        names = []
        for i in range(1, 3):
            name = input(f"Enter player {i} name: ")
            names.append(name)
        return names

    def get_actions(self):
        actions = {}
        for fighter in self.fighters:
            print(f"\n{fighter.name}, choose your action: {fighter.valid_actions}")
            action = input(f"{fighter.name}: ").lower()
            actions[fighter] = action
        return actions

    def resolve_actions(self, actions):
        ordered_fighters = sorted(self.fighters, key=lambda f: f.get_effective_speed(), reverse=True)
        
        for fighter in ordered_fighters:
            action = actions[fighter]
            opponent = next(f for f in self.fighters if f != fighter)
            if action == "stats":
                fighter.print_stats()
            elif action == "attack":
                fighter.attack(opponent)
            elif action == "defend":
                fighter.defend()
            elif action == "boost speed":
                fighter.boost_speed()
            elif action == "run away":
                print(f"{fighter.name} has fled the battle.")
                return True
            else:
                print("Not a valid action - Sorry, you lost your turn!")
        return False

    def start(self):
        print("Welcome to the fighting game!")
        while all(fighter.health > 0 for fighter in self.fighters):
            actions = self.get_actions()
            if self.resolve_actions(actions):
                break  # Game ends if a fighter runs away

gametime = FightinTime()
gametime.start()
