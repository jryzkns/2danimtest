# PYGAME BOILERPLATE CODE
# JRYZKNS 2019

from game_context import *
import pygame as pg
from player import Player
from tilemap import Tilemap

pg.init()
game_win = pg.display.set_mode(res)

bg = Tilemap()
player = Player()

running, paused, dt = True, False, 0
game_clock = pg.time.Clock()
game_clock.tick()

while running:

        # CALLBACKS
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                        paused = not paused
            elif event.type == pg.KEYUP:
                player.on_keyup(event.key)
        dt = game_clock.get_time()/1000.

        if not paused:
            bg.update(dt)
            player.update(dt)

        game_win.fill((0,0,0))

        bg.draw(game_win)
        player.draw(game_win)

        pg.display.flip()
        game_clock.tick()