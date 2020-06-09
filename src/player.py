# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, actions, items, location):
    self.name = name
    self.actions = actions
    self.items = items
    self.location = location

    def __str__(self):
      return None

    def __repr__(self):
      return f"self.name = {self.name}; self.actions = {self.actions}; self.items = {self.items}; self.items = {self.items}"

class Sub_Class(Player):
  def __init__(self, name, description, abilities, level):
    super().__init__(name, actions, items, location)
      self.name = name
      self.description = description
      self.abilities = abilities
      self.level = level

