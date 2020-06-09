# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.n_to = ''
    self.w_to = ''
    self.s_to = ''
    self.e_to = ''
    self.items = []

  def item_aquired(self, items):
    for item in items:
      self.items.append(item)

  def item_dropped(self, items):
    for item in items:
      self.items.remove(item)

  def __str__(self):
    greeting = f"Welcome to {self.name}. {self.description}!"
    return greeting

  