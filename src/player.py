# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room

  def player_actions(self, input):
    if input == "w":
      direction = "n"
    elif input == "a":
      direction = "w"
    elif input == "s":
      direction == "s"
    elif input == "d":
      direction == "e"

    print(f"You have chosen to go {direction}_to.")

  def __str__(self):
    return None

  def __repr__(self):
    return f"Player: (self.name = {repr(self.name)}, self.current_room = {repr(self.current_room)})"

player1 = Player("Nick", "Testing")

print(repr(player1))


# class Sub_Class(Player):
#   def __init__(self, name, description, abilities, level):
#     super().__init__(name, items, location)

