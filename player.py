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

        self.idx = 0
        self.fps = 5
        self.timer = 0

        self.state = IF

    def on_keyup(self, k):
        if k == pg.K_a:   self.state = IR
        elif k == pg.K_s: self.state = IF
        elif k == pg.K_d: self.state = IL
        elif k == pg.K_w: self.state = IB

    def update(self, dt):

        keymap = pg.key.get_pressed()
        if keymap[pg.K_a]:   self.state = MR
        elif keymap[pg.K_s]: self.state = MF
        elif keymap[pg.K_d]: self.state = ML
        elif keymap[pg.K_w]: self.state = MB

        self.timer += dt
        if self.timer >= 1/self.fps:
            self.timer -= 1/self.fps
            self.idx = (self.idx + 1) % alen

    def draw(self, surf):
        surf.blit(self.animations[self.state][self.idx], (100, 100))