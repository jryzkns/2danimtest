import pygame as pg
from game_context import *

class Tilemap:

    def __init__(self, mapfile = "grass.anim"):

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

    def update(self, dt):
        pass

    # TODO: try to move drawing tile by tile to constructor
    # use the idea with stationary platforms from platformer
    def draw(self, surf):
        for i in range(res[0]//self.tile_length):
            for j in range(res[1]//self.tile_length):
                loc = (i * self.tile_length, j * self.tile_length)
                surf.blit(self.tiles[self.map[j][i]], loc)