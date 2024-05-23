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
    
    def updatePosition(self, direction):
        y, x = self.position
    
        if direction == "N" and y > 0:
            self.position = (y - 1, x)
        elif direction == "S" and y < 5:
            self.position = (y + 1, x)
        elif direction == "E" and x < 5:
            self.position = (y, x + 1)
        elif direction == "W" and x > 0:
            self.position = (y, x - 1)
        else:
            print("Invalid Direction")
        

