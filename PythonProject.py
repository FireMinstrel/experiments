import random
import sys
import os
import time

CELLS = [(0, 0), (0, 1), (0, 2),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2,)]
# Grid spaces

ZONENAME = 'zonename'
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False

room_names = {CELLS[0]: "entryway", CELLS[1]: "dining room", CELLS[2]: "kitchen",
              CELLS[3]: "hallway", CELLS[4]: "hallway", CELLS[5]: "hallway",
              CELLS[6]: "bedroom", CELLS[7]: "bathroom", CELLS[8]: "master bedroom"}

#Title Screen
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        print("You heard rumors about an abandoned, supposedly haunted house.  Guess who's going adventuring...?")
        get_moves(player)
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            setup_game() #placeholder until written
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    print('######################')
    print('###### Welcome! ######')
    print('######################')
    print('        -Play-        ')
    print('        -Help-        ')
    print('        -Quit-        ')
    title_screen_selections()

def help_menu():
    print('######################')
    print('###### Welcome! ######')
    print('######################')
    print('Use north, south, east, west to move')
    print('Type your commands to do them')
    print('Use "look" to inspect something')
    print('Good luck and have fun!')
    title_screen_selections()

def get_locations(): # Starting points of the necessary entities
  jock = random.choice(CELLS)
  oldMan = random.choice(CELLS)
  player = CELLS[0]

  if jock == oldMan or player == jock or oldMan == player: # Restarts the starting points if any are the same
    return get_locations()

  return jock, oldMan, player

def move_player(player, move): # move the player
  x, y = player

  if move == 'WEST':
    y -= 1
  if move == 'EAST':
    y += 1
  if move == 'NORTH':
    x -= 1
  if move == 'SOUTH':
    x += 1

  return x, y
  # Get player's current location

def get_moves(player): # display the moves the player can take
  moves = ['WEST', 'EAST', 'NORTH', 'SOUTH']
  # player = (x, y)

  if player[1] == 0:
    moves.remove('WEST')
  elif player[1] == 2:
    moves.remove('EAST')
  elif player[0] == 2:
    moves.remove('NORTH')
  elif player[0] == 0:
    moves.remove('SOUTH')

  return moves

def draw_map(player): # Draws the map
  print(' _ _ _')
  tile = '|{}'

  for spot, cell in enumerate(CELLS):
    if spot in [0, 1, 3, 4, 6, 7]:
      if cell == player:
        print(tile.format('X'), end='')
      else:
        print(tile.format('_'), end='')
    else:
      if cell == player:
        print(tile.format('X|'))
      else:
        print(tile.format('_|'))

jock, oldMan, player = get_locations()

title_screen()

while True:
  moves = get_moves(player)

  print("You're currently in the {}".format(room_names))

  draw_map(player)

  print("You can move {}".format(moves)) #fill in with available moves
  print("Enter QUIT to quit")

  move = input("> ")
  move = move.upper()

  if move == 'QUIT':
    break

  if move in moves:
    player = move_player(player, move)
  else:
    print("::CRASH::")
    continue

  if player == oldMan:
    print('An old man is sitting comfortably in a chair.')
    continue
  elif player == jock:
    print('Brock the jock is waiting impatiently.')
    continue
