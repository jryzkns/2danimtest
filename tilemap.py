import pygame as pg
from game_context import *

class Tilemap:

    def __init__(self, init_loc, mapfile = "grass.anim"):

        self.tile_length = 30

        GRASS_ID = 1

        self.tiles = {
            GRASS_ID : pg.image.load("grass.png")
        }

        with open(mapfile, 'r') as map_file:
            self.map = map_file.read()
            self.map = self.map.split('\n')
            for i in range(len(self.map)):
                self.map[i] = [int(val) for val in self.map[i].split(',')]

        self.pre_render_map = pg.Surface(
            (len(self.map[0])*self.tile_length,len(self.map)*self.tile_length))
        self.prerender()

        self.view_x, self.view_y = init_loc[0]-res[0]//2, init_loc[1]-res[1]//2

    def prerender(self):
        for i in range(self.pre_render_map.get_width()//self.tile_length):
            for j in range(self.pre_render_map.get_height()//self.tile_length):
                loc = (i * self.tile_length, j * self.tile_length)
                self.pre_render_map.blit(self.tiles[self.map[j][i]], loc)

    def clamp_x(self, xval, x_min = 0, x_max = None):
        if x_max is None: x_max = self.pre_render_map.get_width() - res[0]
        if xval > x_max:   return x_max
        elif xval < x_min: return 0
        else:              return xval

    def clamp_y(self, yval, y_min = 0, y_max = None):
        if y_max is None: y_max = self.pre_render_map.get_height() - res[1]
        if yval > y_max:   return y_max
        elif yval < y_min: return 0
        else:              return yval

    def shift_perspective(self, dx, dy):
        self.view_x = self.clamp_x(self.view_x + dx)
        self.view_y = self.clamp_y(self.view_y + dy)

    def update(self, pdx, pdy, dt):
        self.shift_perspective(pdx, pdy)

    def draw(self, surf):
        surf.blit(
            self.pre_render_map
                    .subsurface(
                        pg.Rect(self.view_x, self.view_y, *res)),
                            (0, 0))