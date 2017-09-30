def get_command(console):
  key = console.getch()
  if key == 27:
    return {'exit': True}
  # Move Up
  elif key == 56 or key == 259 :
    return {'move': (0, -1)}
  # Move Down
  elif key == 50 or key == 258:
    return {'move': (0, 1)}
  # Move Left
  elif key == 52 or key == 260:
    return {'move': (-1, 0)}
  # Move Right
  elif key == 54 or key == 261:
    return {'move': (1, 0)}
  # Move Up-Left
  elif key == 55 or key == 262:
    return {'move': (-1, -1)}
  # Move Up-Right
  elif key == 57 or key == 339:
    return {'move': (1, -1)}
  # Move Down-Left
  elif key == 49 or key == 360:
    return {'move': (-1, 1)}
  # Move Down-Right
  elif key == 51 or key == 338:
    return {'move': (1, 1)}
  return {}