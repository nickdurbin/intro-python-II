# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, items=[], location):
    self.name = name
    self.items = items
    self.location = location

    def player_actions(self, input):
      if input == "w":
        direction = "north"
      if input == "a":
        direction = "west"
      if input == "s":
        direction == "south"
      if input == "d":
        direction == "east"

      print(f"You have chosen to go {player_actions(direction)}.")

    def __str__(self):
      return None

    def __repr__(self):
      return f"self.name = {self.name}; self.items = {self.items}; self.items = {self.items}"


class Sub_Class(Player):
  def __init__(self, name, description, abilities, level):
    super().__init__(name, items, location)
      self.name = name
      self.description = description
      self.abilities = abilities
      self.level = level

