from adv import item, room
from room import Room
from player import Player
from items import Item
from methods import player_actions, check_inventory, quit_game
import sys

line = "==============================================="

# Make a new player object that is currently in the 'outside' room.
player_name = input(f'\nHello!\n\n{line}\n{line}\n\nYou have entered the Imaginarium Cave of Doctor Parnassus\n\nWhat is your name? ')
current_room = room['outside']
player = Player(player_name, current_room, [])

def run_game():

  # Write a loop
  while True:
    # Prints the current room name
    # Prints the current description
    print(f"\n{player.current_room}")
    print(f"\n{player_name}, choose your path by pressing w, a, s, d or q for quit.")

    # Waits for user input and decides what to do.
    user_input = input().lower()

    # If the user enters "q", quit the game.
    if user_input == "q" or user_input == "quit":
      quit_game(player)
        
    # If the user enters a cardinal direction, attempt to move to the room there.
    elif user_input == "w" or user_input == "a" or user_input == "s" or user_input == "d":
      player_actions(user_input, player)
      print(current_room, "Ran after move_to function")
    else:
      # Print an error message if the movement isn't allowed.
      print("\nIncorrect input.\nPlease enter a valid cardinal direct w, a ,s ,d or q to quit.")

print(run_game())