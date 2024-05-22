class Player:
    def __init__(self, name):
        self.name = name
        self.damage = 2
        self.health = 10
        self.position = (0, 0)
    
    # Getters and Setters for Player Class
    def getName(self):
        return self.name
    
    def getDamege(self):
        return self.damage
    
    def getHealth(self):
        return self.health
    
    def getPosition(self):
        return self.position
    
    def setName(self, name):
        self.name = name
    
    def setDamage(self, damage):
        self.damage = damage
    
    def setHealth(self, health):
        self.health = health
    
    def setPosition(self, position):
        self.position = position
    
   # def movePlayer(self, direction):
        

testPlayer = Player("Hero")

