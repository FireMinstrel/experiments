X = "X"
EMPTY = " "
NUM_SQUARES = 13

class player:
    def __init__(self):
        self.location = 'start'
        self.game_over = False
myPlayer = player()

def new_map():
    """Create new game board."""
    spot = []
    for square in range(NUM_SQUARES):
        spot.append(EMPTY)
    return spot

def show_map(spot):
    """Display game board on screen."""
    print("\n\t", "|", spot[0], "|", spot[1], "|", spot[2], "|", spot[3], "|")
    print("\t", "-----------------")
    print("\t", "|", spot[4], "|", spot[5], "|", spot[6], "|", spot[7], "|")
    print("\t", "-----------------")
    print("\t", "|", spot[8], "|", spot[9], "|", spot[10], "|", spot[11], "|")
    print("\t", "-----------------")
    print("\t", "|", spot[12], "|", "\n")
    rowString = " "
    for index,row in enumerate(spot):
        if row == 0:
            rowString += "| |"
        else: rowString+= "|x|"
        if index % 4 == 0:
            print("-"*12)
            print(rowString)
            rowString = " "

def prompt():
    print("\n" + "============================")
    print("What would you like to do?")
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_actions:
        print("...Yeah...not getting that. What is it you wanted to do?\n")
        action = input("> ")
    if action.lower() == "quit":
        print("Goodbye!")
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk',]:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())

def legal_moves(spot):
    """Create list of legal moves."""
    moves = []
    for square in range(NUM_SQUARES):
        if spot[square] == EMPTY:
            moves.append(square)
    return moves

def player_move(myAction):
    show_map(spot)
    ask = "Where would you like to go?\n"
    dest = input(ask)
    if dest == ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
        print_location()
    elif dest == ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
        print_location()
    elif dest == ['right', 'east']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)
        print_location()
    elif dest == ['down', 'south']:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)
        print_location()

def move_direction(spot):
    """Get human move."""  
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_move("Where will you move?", 0, NUM_SQUARES)
        if move not in legal:
            print("\nYou can't go that way.\n")
    print("Fine...")
    return move

def main():
    turn = X
    spot = new_map()
    show_map(spot)
    while myPlayer.game_over is False:
        prompt()

main()
