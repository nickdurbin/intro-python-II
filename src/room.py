# Implement a class to hold room information. This should have name and
# description attributes.
import player from Player

class Room:
  def __init__(self, name, items, description):
    self.name = name
    self.items = items
    self.walls = walls
    self.doors = doors

  def item_aquired(self, item):
    self.items.append(player.items)

  def item_dropped(self, item):
    self.items.remove(player.items)

  def __str__(self):
    greeting = f"Welcome to {self.name}, {player.name}!"
    return greeting

  