import map
from player import Player

# Choice variable to update player's choice
choice = ""

# Boolean Value for Game Loop
gameOver = False

# Boolean Value to ensure player makes valid selection
choiceLoop = False

game_map = None

player = None

def main():
    global gameOver
    global choiceLoop
    global player
    global game_map

    # Game Loop
    while(not gameOver):
        start = startGame()

        if not start:
            break
            
        # Choice Loop to decide if the player wants to start the game
        generateMap()
        print("Game has started!\n")
        
        # Game Loop
        while(not gameOver):
            # Player Movement

            choice = move()

            # Move the playery
            player.updatePosition(choice)
            print("Player has moved to: " + str(player.getPosition()) + "\n")

            # Show the game map
            #print(map.printMap(game_map))
        gameOver = True


def processChoice(playerInput):
    choice = playerInput.upper()
    choice = choice.replace(" ", "")
    return choice

def startGame():
    loop = True
    while loop:
        choice = processChoice(input("Would you like to start the game? (Y/N)\n"))
        if choice == "Y":
            return True
        elif choice == "N":
            return False
        else:
            print("Please enter a valid choice.")
            loop = True

def generateMap():
    global player
    global game_map
    global gameOver

    # Generate Player
    player = Player("Hero")

    # Create the game map and populate it with monsters
    game_map = map.createMap(5, 5)

    # Create the game map and populate it with monsters
    game_map = map.createMap(5, 5)
    map.populateMap(game_map)
    
    # Find the furthest cell from monsters and place the player there
    player.setPosition(map.findFurthestCell(game_map))
    game_map[player.getPosition()] = player

    # Show the game map
    print("Your map has been created!")
    print(map.printMap(game_map))

def move():
    print("Where would you like to move?")
    print("Type 'N' to move North, 'S' to move South, 'W' to move West, 'E' to move East:\n")
    choice = processChoice(input())
    return choice

main()


