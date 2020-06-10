from adv import item, room
from room import Room
from player import Player
from items import Item
from methods import player_actions, move_to
import sys

def run_game():
  # Make a new player object that is currently in the 'outside' room.
  player_name = input('Hello!\nYou have entered the Imaginarium Cave of Doctor Parnassus\nWhat is your name? ')
  current_room = room['outside']
  player = Player(player_name, current_room)
  
  def quit_game():
    print(f"Ummm, {player}. Are you sure you want to quit?\nYou will lose your progress.\nType [Y/n]")

    quit_input = input().lower()

    if quit_input == "" or quit_input == "Y" or quit_input == "YES":
      print(f"Sad to see you go, {player}.\nSee you again soon! Muwhahaha!")
      sys.exit()
    
    else:
      print(f"Good choice, {player}. Now find the treasure!")

  # Write a loop

  while True:
    # Prints the current room name
    # Prints the current description
    print(player.current_room)
    print(f"{player_name}, choose your path by pressing w, a, s, d or q for quit.")

    # Waits for user input and decides what to do.
    user_input = input().lower()

    # If the user enters "q", quit the game.
    if user_input == "q" or user_input == "quit":
      quit_game()
        
    # If the user enters a cardinal direction, attempt to move to the room there.
    if user_input == "w" or user_input == "a" or user_input == "s" or user_input == "d":
      player.player_actions(user_input)
    else:
      # Print an error message if the movement isn't allowed.
      print("Incorrect input.\nPlease enter a valid cardinal direct w, a ,s ,d or q to quit.")

print(run_game())