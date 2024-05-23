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

            # Ask the Player for their choice
            map.printMap(game_map)
            choice = input("Would you like to move, attack, or quit? (M/A/Q)\n")
            choice = processChoice(choice)

            # Process the Player's choice
            # Quit
            if choice == "Q":
                print("Thank you for playing!")
                gameOver = True
                break
            
            # Attack
            elif choice == "A":
                print("Player has attacked")

            # Move
            elif choice == "M":
                # Ask which direction the player would like to move and store the choice
                choice = move()
                # Store the player's current position
                old_position = player.getPosition()
                # Update the player's position
                player.updatePosition(choice)
                # Sotre the player's new position
                new_position = player.getPosition()
                # Move the player on the map
                map.moveObject(game_map, old_position, new_position)
                # Print the coordinates of the player
                print("Player has moved to: " + str(player.getPosition()) + "\n")

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


