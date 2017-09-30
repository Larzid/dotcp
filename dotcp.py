#!/usr/bin/python

import argparse
from components.entity import Entity

arguments = argparse.ArgumentParser()
arguments.add_argument('-t', '--tdl', help='Run with tdl library.', action='store_true')
args = arguments.parse_args()

if args.tdl:
  from render import tdl_lib as graphic
  from key_map import tdl_key as key_set
else:
  from render import curse as graphic
  from key_map import curse_key as key_set

class Game():
  def __init__(self):
    self.console = graphic.start()
    (width, height) = graphic.get_size(self.console)
    self.player = Entity(width // 2, height // 2, '@')
  def loop(self):
    command = ''
    while command != 'exit':
      graphic.render_all(self)
      action = key_set.get_command(self.console)
      exit = action.get('exit')
      move = action.get('move')
      if exit:
        graphic.stop(self.console)
        command = 'exit'
      if move:
        dx, dy = move
        self.player.x += dx
        self.player.y += dy

state = Game()
state.loop()

