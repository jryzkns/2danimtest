from game_context import *

import pygame as pg

class Tilemap:

    def __init__(self, mapfile = "grass.anim"):

        self.t_size = 30

        GRASS_ID = 1

        self.tiles = {
            GRASS_ID : pg.image.load("grass.png")
        }

        with open(mapfile, 'r') as map_file:
            self.map = map_file.read()
            self.map = self.map.split('\n')
            for i in range(len(self.map)):
                self.map[i] = [int(val) for val in self.map[i].split(',')]

        self.world = pg.Rect( 0, 0, len(self.map[0]) * self.t_size, len(self.map) * self.t_size)

        self.pre_rendered_map = pg.Surface((self.world.w, self.world.h))
        self.pre_render()

        self.view_x, self.view_y = 0, 0
        self.render_view()

        self.dock_state = NA

    def render_view(self):
        self.view_box = pg.Rect(self.view_x, self.view_y, *res)
        self.view = self.pre_rendered_map.subsurface(self.view_box)

    def pre_render(self):
        for i in range(self.world.w//self.t_size):
            for j in range(self.world.h//self.t_size):
                self.pre_rendered_map.blit(self.tiles[self.map[j][i]], (i * self.t_size, j * self.t_size))

    def clamp_y(self, yval, y_min = 0, y_max = None):
        if y_max is None:   y_max = self.world.h - HEIGHT
        if   yval < y_min:  return y_min
        elif yval > y_max:  return y_max
        else:               return yval

    def clamp_x(self, xval, x_min = 0, x_max = None):
        if x_max is None:   x_max = self.world.w - WIDTH
        if   xval < x_min:  return x_min
        elif xval > x_max:  return x_max
        else:               return xval

    def set_viewpoint(self, x, y):
        self.view_x = self.clamp_x(x - WIDTH//2)
        self.view_y = self.clamp_y(y - HEIGHT//2)

    def determine_dock_state(self):
        self.dock_state = NA
        if self.view_box.top == self.world.top:
            self.dock_state += N
        if self.view_box.left == self.world.left:
            self.dock_state += W
        if self.view_box.right == self.world.right:
            self.dock_state += E
        if self.view_box.bottom == self.world.bottom:
            self.dock_state += S

    def update(self, pdx, pdy, dt):

        self.view_x = self.clamp_x(self.view_x + pdx)
        self.view_y = self.clamp_y(self.view_y + pdy)

        self.render_view()
        self.determine_dock_state()

    def draw(self, surf): surf.blit(self.view, (0, 0))
