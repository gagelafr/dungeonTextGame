class Player:
    def __init__(self, name):
        self.name = name
        damage = 2
        health = 10
    
    def attack(self):
        return self.damage

testPlayer = Player("Hero")
