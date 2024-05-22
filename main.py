import map
from player import Player

# Choice variable to update player's choice
choice = ""

def startgame():
    # Boolean Value for Game Loop
    gameOver = False

    # Boolean Value to ensure player makes valid selection
    choiceLoop = True

    # Game Loop
    while(not gameOver):
        print("Are you ready to start your adventure?")
        # Choice Loop to decide if the player wants to start the game
        while(choiceLoop):
            choice = processChoice(input('Type "Y" or "N"\n'))

            if choice == "Y":
                print("Great! Let's get started!\n")

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
                
                # Close the choice loop
                choiceLoop = False

            elif choice == "N":
                print("Until next time adventurer!")
                choiceLoop = False

            else:
                print("Please choose a correct option!")

        gameOver = True

def processChoice(playerInput):
    choice = playerInput.upper()
    choice = choice.replace(" ", "")
    return choice

startgame()


