import tdl

colors = {
  'dark_wall': (0, 0, 100),
  'dark_ground': (50, 50, 150),
  'light_wall': (130, 110, 50),
  'light_ground': (200, 180, 50),
  'desaturated_green': (63, 127, 63),
  'darker_green': (0, 127, 0)
}

def render_all(game):
  game.console.clear()
  game.console.draw_char(game.player.x, game.player.y, game.player.char, colors.get('desaturated_green'), bg=None)
  tdl.flush()

def start():
  screen_width = 80
  screen_height = 50
  tdl.set_font('fonts/generic_rl_10x10.png', greyscale=True, altLayout=False)
  console = tdl.init(screen_width, screen_height, title='Dungeon Of The Cursed Python')
  return console

def stop(console):
  return

def get_size(console):
  return console.get_size()
