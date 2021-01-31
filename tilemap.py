import pygame as pg
from game_context import *

class Tilemap:

    def __init__(self, mapfile = "grass.anim"):

        self.tile_size = 30

        GRASS_ID = 1

        self.tiles = {
            GRASS_ID : pg.image.load("grass.png")
        }

        with open(mapfile, 'r') as map_file:
            self.map = map_file.read()
            self.map = self.map.split('\n')
            for i in range(len(self.map)):
                self.map[i] = [int(val) for val in self.map[i].split(',')]

        self.world_w = len(self.map[0]) * self.tile_size
        self.world_h = len(self.map)    * self.tile_size

        self.pre_rendered_map = pg.Surface((self.world_w, self.world_h))
        self.pre_render()

        self.view_x, self.view_y = 0, 0

    def pre_render(self):
        for i in range(self.world_w//self.tile_size):
            for j in range(self.world_h//self.tile_size):
                loc = (i * self.tile_size, j * self.tile_size)
                self.pre_rendered_map.blit(self.tiles[self.map[j][i]], loc)

    def clamp_y(self, yval, y_min = 0, y_max = None):
        if y_max is None:   y_max = self.world_h - res[1]
        if   yval < y_min:  return y_min
        elif yval > y_max:  return y_max
        else:               return yval

    def clamp_x(self, xval, x_min = 0, x_max = None):
        if x_max is None:   x_max = self.world_w - res[0]
        if   xval < x_min:  return x_min
        elif xval > x_max:  return x_max
        else:               return xval

    def set_viewpoint(self, x, y):
        self.view_x = self.clamp_x(x - res[0]//2)
        self.view_y = self.clamp_y(y - res[1]//2)

    def update(self, pdx, pdy, dt):
        self.view_x = self.clamp_x(self.view_x + pdx)
        self.view_y = self.clamp_y(self.view_y + pdy)

    def draw(self, surf):
        surf.blit(self.pre_rendered_map
            .subsurface(pg.Rect(self.view_x, self.view_y, *res)), (0, 0))
