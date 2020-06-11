def player_actions(cmd, player):
  action = None

  try:
    if cmd == "w" or cmd == "a" or cmd == "s" or cmd == "d":
      action = move_to(cmd, player)
    elif cmd == "i" or cmd == "inventory":
      action = check_inventory(player.inventory)

  except:
    print("There was an error with your request. Please check your input value.")


def move_to(cardinal_dir, player):
  room = None

  if cardinal_dir == "w":
    room = player.current_room.n_to
  elif cardinal_dir == "a":
    room = player.current_room.w_to
  elif cardinal_dir == "s":
    room = player.current_room.s_to
  elif cardinal_dir == "d":
    room = player.current_room.e_to

  if room != None or room != "":
    player.current_room = room
  else:
    print("\nYou have run into a deadend!\nPlease choose another direction.")

  return room

def check_inventory(list):
  if len(list) <= 0:
    print("\nYou have nothing in your inventory")
  else:
    for index, item in list:
      print(f"\nItem {index}: {item.name}")
  
  return list

line = "==============================================="

def quit_game(player):
  print(f"\n{line}\n{line}\n\nUmmm, {player.name}.\n\nAre you sure you want to quit?\n\nYou will lose your progress if yes.\n\nType [Y/n]")

  quit_input = input().lower()

  if quit_input == "" or quit_input == "y" or quit_input == "yes":
    print(f"\nSad to see you go, {player.name}.\nSee you again soon! Muwhahaha!")
    exit()
  
  else:
    print(f"\nGood choice, {player.name}. Now find the treasure!")