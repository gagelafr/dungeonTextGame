import map
from monster import Monster

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
                game_map = map.createMap(4, 4)
                map.populateMap(game_map)
                print("Your map has been created!")
                print(map.printMap(game_map))
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


