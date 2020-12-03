# PYGAME BOILERPLATE CODE
# JRYZKNS 2019

res = (640, 360)

import pygame as pg
from player import Player

pg.init()
game_win = pg.display.set_mode(res)

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
            player.update(dt)

        game_win.fill((0,0,0))

        player.draw(game_win)

        pg.display.flip()
        game_clock.tick()