import monster

class Tile:

    def init(self):
        self.type = "Grass"
        self.position = (0, 0)
        self.monster = None
        self.hasPlayer = False

    # Getters
    def getType(self):
        return self.type
    
    def getPosition(self):
        return self.position
    
    def getMonster(self):
        return self.monster
    
    def getPlayer(self):
        return self.player
    
    # Setters
    def setType(self, type):
        self.type = type

    def setPosition(self, position):
        self.position = position
    
    def setMonster(self, monster):
        self.monster = monster
    
    def setPlayer(self, player):
        self.player = player
    
    
