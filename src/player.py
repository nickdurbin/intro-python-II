# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
  def __init__(self, name: str, current_room: str, inventory: list):
    self.name = name
    self.current_room = current_room
    self.inventory = [] # list of items in the inventory per Readme

  def __str__(self):
    return f"Name: {self.name}\nCurrent Location: {self.current_room}"

  def __repr__(self):
    return f"Player: (self.name = {repr(self.name)}, self.current_room = {repr(self.current_room)})"

# class Sub_Class(Player):
#   def __init__(self, name, description, abilities, level):
#     super().__init__(name, current_name)
