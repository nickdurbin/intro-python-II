# Implement a class to hold room information. This should have name and
# description attributes.

line = "="*30
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
    room_greeting = f"{line}\n{line}\n\nWelcome to {self.name}. {self.description}!\nRoom Items: {room_items}\n"
    if self.s_to:
      room_greeting+= f'\nTo the south is: {self.s_to.name}\n'
    if self.e_to:
      room_greeting += f'\nTo the east is: {self.e_to.name}\n'
    if self.n_to:
      room_greeting += f'\nTo the north is: {self.n_to.name}\n'
    if self.w_to:
      room_greeting += f'\nTo the west is: {self.w_to.name}\n'
    for items in self.items:
      room_items += str(items)
    return room_greeting

  def __repr__(self):
    return f"self.name = {self.name} - self.description = {self.description} - self.items = {self.description}"
