import tdl

def get_command(console):
  for event in tdl.event.get():
    if event.type == 'KEYDOWN':
        user_input = event
        break
  else:
    user_input = None
    
  if user_input:
    key_char = user_input.keychar
    if user_input.key == 'UP' or key_char == 'k' or key_char == 'KP8':
      return {'move': (0, -1)}
    elif user_input.key == 'DOWN' or key_char == 'j' or key_char == 'KP2':
      return {'move': (0, 1)}
    elif user_input.key == 'LEFT' or key_char == 'h' or key_char == 'KP4':
      return {'move': (-1, 0)}
    elif user_input.key == 'RIGHT' or key_char == 'l' or key_char == 'KP6':
      return {'move': (1, 0)}
    elif key_char == 'y' or key_char == 'KP7':
      return {'move': (-1, -1)}
    elif key_char == 'u' or key_char == 'KP9':
      return {'move': (1, -1)}
    elif key_char == 'b' or key_char == 'KP1':
      return {'move': (-1, 1)}
    elif key_char == 'n' or key_char == 'KP3':
      return {'move': (1, 1)}

    if user_input.key == 'ENTER' and user_input.alt:
      # Alt+Enter: toggle full screen
      return {'fullscreen': True}
    elif user_input.key == 'ESCAPE':
      # Exit the game
      return {'exit': True}

  # No key was pressed
  return {}