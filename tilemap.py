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

        self.dock_state = DOCK_NA

    def render_view(self):
        self.view_box = pg.Rect(self.view_x, self.view_y, *res)
        self.view = self.pre_rendered_map.subsurface(self.view_box)

    def pre_render(self):
        for i in range(self.world.w//self.t_size):
            for j in range(self.world.h//self.t_size):
                self.pre_rendered_map.blit(self.tiles[self.map[j][i]], (i * self.t_size, j * self.t_size))

    def clamp_y(self, yval, y_min = 0, y_max = None):
        if y_max is None:   y_max = self.world.h - H
        if   yval < y_min:  return y_min
        elif yval > y_max:  return y_max
        else:               return yval

    def clamp_x(self, xval, x_min = 0, x_max = None):
        if x_max is None:   x_max = self.world.w - W
        if   xval < x_min:  return x_min
        elif xval > x_max:  return x_max
        else:               return xval

    def set_viewpoint(self, x, y):
        self.view_x = self.clamp_x(x - W//2)
        self.view_y = self.clamp_y(y - H//2)

    def determine_dock_state(self):

        if self.view_box.top == self.world.top:
            if self.view_box.left == self.world.left:
                self.dock_state = DOCK_NW
            elif self.view_box.right == self.world.right:
                self.dock_state = DOCK_NE
            else: self.dock_state = DOCK_N
        elif self.view_box.bottom == self.world.bottom:
            if self.view_box.left == self.world.left:
                self.dock_state = DOCK_SW
            elif self.view_box.right == self.world.right:
                self.dock_state = DOCK_SE
            else: self.dock_state = DOCK_S
        else:
            if self.view_box.left == self.world.left:
                self.dock_state = DOCK_W
            elif self.view_box.right == self.world.right:
                self.dock_state = DOCK_E
            else: self.dock_state = DOCK_NA

    def update(self, pdx, pdy, dt):

        self.view_x = self.clamp_x(self.view_x + pdx)
        self.view_y = self.clamp_y(self.view_y + pdy)

        self.render_view()
        self.determine_dock_state()

    def draw(self, surf): surf.blit(self.view, (0, 0))
