# PYGAME BOILERPLATE CODE
# JRYZKNS 2019

from game_context import *
import pygame as pg
from player import Player
from tilemap import Tilemap

pg.init()
game_win = pg.display.set_mode(res)

camera_bounds = pg.Rect(
        res[0]//6,
        res[1]//6, 
        4*res[0]//6, 
        4*res[1]//6)

bg = Tilemap()
world_w, world_h = bg.world_w, bg.world_h
player = Player(world_w, world_h)

bg.set_viewpoint(*player.hitbox.center)

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
            pdx, pdy = player.update(dt, bg.view_x, bg.view_y, camera_bounds)
            bg.update(pdx, pdy, dt)

        bg.draw(game_win)
        player.draw(game_win, bg.view_x, bg.view_y)

        pg.draw.rect(game_win, (255, 255, 255),
            camera_bounds, 1)

        pg.display.flip()
        game_clock.tick()