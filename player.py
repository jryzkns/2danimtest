import pygame as pg
from lib import *
from game_context import *

MF, MB, MR, ML = 1, 2, 3, 4
IF, IB, IR, IL = 5, 6, 7, 8
ss_path, alen = "Charactervector.png", 4

class Player:
    def __init__(self):
        ss = pg.image.load(ss_path)
        ss_w, ss_h = ss.get_size()
        self.f_w, self.f_h = ss_w//alen, ss_h//alen

        self.animations = {
            MF : get_quad_row(ss, ss_w,            0, self.f_h, alen),
            MB : get_quad_row(ss, ss_w,     self.f_h, self.f_h, alen),
            MR : get_quad_row(ss, ss_w, 2 * self.f_h, self.f_h, alen),
            ML : get_quad_row(ss, ss_w, 3 * self.f_h, self.f_h, alen),
            IF : alen * [ get_quad(ss, (0,                       0), self.f_w, self.f_h) ],
            IB : alen * [ get_quad(ss, (0,                self.f_h), self.f_w, self.f_h) ],
            IR : alen * [ get_quad(ss, (0,            2 * self.f_h), self.f_w, self.f_h) ],
            IL : alen * [ get_quad(ss, (3 * self.f_w, 3 * self.f_h), self.f_w, self.f_h) ]
        }

        self.x, self.y = 150, 150
        self.movespeed = 300

        self.fps = self.movespeed/30
        self.aidx, self.timer = 0, 0
        self.state = IF

        self.hitbox = self.recalc_hitbox()
    
    def on_keyup(self, k, 
        ku_xsitions = {pg.K_a:IR, pg.K_s:IF, pg.K_d:IL, pg.K_w:IB}):
        if k in ku_xsitions: self.state = ku_xsitions[k]

    def recalc_hitbox(self):
        return pg.Rect( self.x + 1/6 *self.f_w, 
                        self.y + 2/3 * self.f_h + 1/5 * self.f_h, 
                        4/6 * self.f_w, 
                        1/3 * self.f_h - 1/4 * self.f_h)

    def update(self, dt):

        dx, dy = 0, 0 
        keymap = pg.key.get_pressed()
        if keymap[pg.K_a]:   
            self.state = MR
            dx = -1*self.movespeed
        if keymap[pg.K_s]: 
            self.state = MF
            dy = self.movespeed
        if keymap[pg.K_d]: 
            self.state = ML
            dx = self.movespeed
        if keymap[pg.K_w]: 
            self.state = MB
            dy = -1*self.movespeed

        if (self.hitbox.y + dy*dt < 0 
            or self.hitbox.y + self.hitbox.h + dy*dt > res[1]):
            dy = 0

        if (self.hitbox.x + dx*dt < 0 
            or self.hitbox.x + self.hitbox.w + dx*dt > res[0]):
            dx = 0

        self.x += dx * dt
        self.y += dy * dt

        self.hitbox = self.recalc_hitbox()

        self.timer += dt
        if self.timer >= 1/self.fps:
            self.timer -= 1/self.fps
            self.aidx = (self.aidx + 1) % alen

    def draw(self, surf):
        pg.draw.rect(surf, (255, 255, 0), self.hitbox, 1)
        surf.blit(self.animations[self.state][self.aidx], (self.x, self.y))
