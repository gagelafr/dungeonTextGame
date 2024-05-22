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
    
    def movePlayer(self, direction):
        x, y = self.position
    
        if direction == "N":
            self.position = (x, y - 1)
        elif direction == "S":
            self.position = (x, y + 1)
        elif direction == "E":
            self.position = (x + 1, y)
        elif direction == "W":
            self.position = (x - 1, y)
        else:
            print("Invalid Direction")
        

testPlayer = Player("Hero")
testPlayer.movePlayer("N")
print(testPlayer.getPosition())

