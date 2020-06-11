# Implement a class to hold room information. This should have name and
# description attributes.

line = "==============================================="
class Room:
  def __init__(self, name: str, description: str, items: list):
    self.name = name
    self.description = description
    self.n_to = None
    self.w_to = None
    self.s_to = None
    self.e_to = None
    self.items = [] # list to hold items per Readme.

  def __str__(self):
    room_items = None
    for items in self.items:
      room_items += str(items)
    return f"{line}\n{line}\n\nWelcome to {self.name}. {self.description}!\nItems: {room_items}"

  def __repr__(self):
    return f"self.name = {self.name} - self.description = {self.description} - self.items = {self.description}"
