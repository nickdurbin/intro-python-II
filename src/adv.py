from room import Room
from items import Item

# Declare all the rooms

room = {
  'outside': Room("Outside Cave Entrance", "\n\nNorth of you, the cave mount beckons", ["lantern"]),

  'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["basic sword"]),

  'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", ["rope"]),

  'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["gravity gun"]),

  'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ["golden gun"]),
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

item = {
  'compass': Item("compass", "To help you with direction when you need it most.", 0),
  'basic sword': Item("basic sword", "Will provide some protection against lesser evils.", 1),
  'rope': Item("rope", "Roughly 25meters in length. Great for climbing in and out of caves.", 2),
  'lantern': Item("lantern", "A simple item designed to light a path in the abyss.", 2),
  'gravity gun': Item("gravity gun", "A gun designed to disrupt the gravitational pull on enemies, objects, and oneself.", 23),
  'golden gun': Item("golden gun", "A weapon designed for one shot, one kill.", 35),
}