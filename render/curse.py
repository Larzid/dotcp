import curses

def render_all(game):
  game.console.clear()
  game.console.addstr(game.player.y, game.player.x, game.player.char)

def start():
  console = curses.initscr()
  curses.start_color()
  curses.curs_set(False)
  curses.noecho()
  curses.cbreak()
  console.keypad(True)
  return console

def stop(console):
  curses.nocbreak()
  console.keypad(False)
  curses.echo()
  curses.endwin()

def get_size(console):
  return (curses.COLS, curses.LINES) 
