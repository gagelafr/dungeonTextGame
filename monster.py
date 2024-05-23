class Monster:
    def __init__(self, name, level, health, damage):
        self.name = name
        self.level = 1
        self.health = health
        self.damage = damage
    
    def attack(self):
        return self.damage
    
testMonsters = [Monster("Grass", 10, 2, 1), Monster("Water", 20, 5, 1), Monster("Sand", 50, 10, 1)]