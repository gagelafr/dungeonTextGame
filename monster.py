class Monster:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
    
    def attacK(self):
        return self.damage
    
testMon = Monster("Goblin", 10, 2)