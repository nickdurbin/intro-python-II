from room import Room
from player import Player
from items import Item

# Declare all the rooms

room = {
  'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

  'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

  'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

  'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

  'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# List of items

items = {
  'basic sword': Item("basic sword", "Will provide some protection against lesser evils.", 1),
  'rope': Item("rope", "Roughly 25meters in length. Great for climbing in and out of caves.", 2),
  'lantern': Item("lantern", "A simple item designed to light a path in the abyss.", 2),
  'gravity gun': Item("gravity gun", "A gun designed to disrupt the gravitational pull on enemies, objects, and oneself.", 23),
  'golden gun': Item("golden gun", "A weapon designed for one shot, one kill.", 35),
}


# Make a new player object that is currently in the 'outside' room.

player_name = input('Hello!\nYou have entered the Imaginarium Cave of Doctor Parnassus\nWhat is your name? ')
current_room = room['outside']
player = Player(player_name, current_room)

def quit_game():
  user_input = input().lower()
  print(f"Ummm, {player}. Are you sure you want to quit?\nYou will lose your progress.")
  input("[Y/n]")

  if user_input == "" or user_input == "Y" or user_input == "YES":
    print(f"Sad to see you go, {player}.\nSee you again soon! Muwhahaha!")
    exit()
  
  else:
    print(f"Good choice, {player}. Now find the treasure!")

# Write a loop

while True:
    # Prints the current room name
    # Prints the current description
    print(player.current_room)

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
  