# A class for the items in the rooms.

class Item:
  def __init__(self, name: str, description: str, level: int):
    self.name = name
    self.description = description
    self.level = int(level)

  def picked_up(self):
    print(f"Beholdeth! You have discovered the {self.name} a level{self.level}.\nThe{self.name} is {self.description}.")

  def put_down(self):
    print(f"Yeah, who needs a {self.name} anyway? It was only saving your life.")

  def __str__(self):
    print(f"Name: {self.name} is a {self.description} and is level: {self.level}")

  def __repr__(self):
    return f"self.name = {self.name} ; self.description = {self.description} ; self.level = {self.level}"

# List of items
# compass = Item("compass", "To help you with direction when you need it most.", 0)
# basic_sword = Item("basic sword", "Will provide some protection against lesser evils.", 1)
# rope = Item("rope", "Roughly 25meters in length. Great for climbing in and out of caves.", 2)
# lantern = Item("lantern", "A simple item designed to light a path in the abyss.", 2)
# gravity_gun = Item("gravity gun", "A gun designed to disrupt the gravitational pull on enemies, objects, and oneself.", 23)
# golden_gun = Item("golden gun", "A weapon designed for one shot, one kill.", 35)