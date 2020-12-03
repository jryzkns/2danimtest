import pygame as pg
from lib import *

MF, MB, MR, ML = 1, 2, 3, 4
IF, IB, IR, IL = 5, 6, 7, 8
ss_path, alen = "Charactervector.png", 4

class Player:
    def __init__(self):
        ss = pg.image.load(ss_path)
        ss_w, ss_h = ss.get_size()
        f_w, f_h = ss_w//alen, ss_h//alen

        self.animations = {
            MF : get_quad_row(ss, ss_w,     0, f_h, alen),
            MB : get_quad_row(ss, ss_w,   f_h, f_h, alen),
            MR : get_quad_row(ss, ss_w, 2*f_h, f_h, alen),
            ML : get_quad_row(ss, ss_w, 3*f_h, f_h, alen),
            IF : alen * [ get_quad(ss, (0, 0), f_w, f_h) ],
            IB : alen * [ get_quad(ss, (0, f_h), f_w, f_h) ],
            IR : alen * [ get_quad(ss, (0, 2 * f_h), f_w, f_h) ],
            IL : alen * [ get_quad(ss, (3 * f_w, 3 * f_h), f_w, f_h) ]
        }

        self.aidx, self.fps, self.timer = 0, 5, 0
        self.state = IF

        self.x, self.y = 200, 200
    
    def on_keyup(self, k, 
        ku_xsitions = {pg.K_a:IR, pg.K_s:IF, pg.K_d:IL, pg.K_w:IB}):
        if k in ku_xsitions: self.state = ku_xsitions[k]

    def update(self, dt):

        keymap = pg.key.get_pressed()
        if keymap[pg.K_a]:   self.state = MR
        elif keymap[pg.K_s]: self.state = MF
        elif keymap[pg.K_d]: self.state = ML
        elif keymap[pg.K_w]: self.state = MB

        if self.state in (MR, MF, ML, MB):
            # code for moving and collision checking

        self.timer += dt
        if self.timer >= 1/self.fps:
            self.timer -= 1/self.fps
            self.aidx = (self.aidx + 1) % alen

    def draw(self, surf):
        surf.blit(self.animations[self.state][self.aidx], (self.x, self.y))