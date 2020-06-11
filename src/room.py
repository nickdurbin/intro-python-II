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

  def item_aquired(self, items):
    for item in items:
      self.items.append(item)

  def item_dropped(self, items):
    for item in items:
      self.items.remove(item)

  def room_items(self):
    print(f'{line}\n---- This Room Contains The Following Items ----\n{line}')
    for item in self.items:
        print(item)

  def __str__(self):
    return f"{line}\n{line}\n\nWelcome to {self.name}. {self.description}!"

  def __repr__(self):
    return f"self.name = {self.name} - self.description = {self.description} - self.items = {self.description}"
