def player_actions(cmd, action, player):
  room = ''

  try: 
    if cmd == "n":
      room = player.current_room.n_to
      action = print(move_to())
    elif cmd == "a":
      room = player.current_room.w_to
      action = print(move_to())
    elif cmd == "s":
      room = player.current_room.s_to
      action = print(move_to())
    elif cmd == "d":
      room = player.current_room.e_to
      action = print(move_to())
    elif cmd == "i"
      action == print(check_inventory())
    elif cmd == "e"
      action == print(use_item())
    elif cmd == "h"
      action == print(use_heal())
    elif cmd == "left_shift"
      action == print(use_sprint())
    elif cmd == "spacebar"
      action == print(use_jump())
  
  except:
    print("Please choose a valid input command.")
  
  if room != "" or room != None:
    player.current_room == room
  else:
    print("You have run into a deadend!\nPlease choose another diirection.")

def move_to():
  
  