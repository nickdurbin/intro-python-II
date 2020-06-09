# A class for the items in the rooms.

class Item:
  def __init__(self, name, description, level):
    self.name = name
    self.description = description
    self.level = int(level)

  def picked_up(self):
    print(f"Beholdeth! You have discovered the {self.name} a level{self.level}.\nThe{self.name} is {self.description}.")

  def put_down(self):
    print(f"Yeah, who needs a {self.name} anyway? It was only saving your life.")

  def __repr__(self):
    return f"self.name = {self.name} ; self.description = {self.description} ; self.level = {self.level}"
