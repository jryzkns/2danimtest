res = (660, 360)

W, H = res[0], res[1]

DOCK_N  = 0
DOCK_NE = 1
DOCK_E  = 2
DOCK_SE = 3
DOCK_S  = 4
DOCK_SW = 5
DOCK_W  = 6
DOCK_NW = 7
DOCK_NA = 8

from pygame import Rect

cb = (
    Rect(W//6,    0, 4*W//6, 5*H//6), # DOCK_N
    Rect(W//6,    0, 5*W//6, 5*H//6), # DOCK_NE
    Rect(W//6, H//6, 5*W//6, 4*H//6), # DOCK_E
    Rect(W//6, H//6, 5*W//6, 5*H//6), # DOCK_SE
    Rect(W//6, H//6, 4*W//6, 5*H//6), # DOCK_S
    Rect(   0, H//6, 5*W//6, 5*H//6), # DOCK_SW
    Rect(   0, H//6, 5*W//6, 4*H//6), # DOCK_W
    Rect(   0,    0, 5*W//6, 5*H//6), # DOCK_NW
    Rect(W//6, H//6, 4*W//6, 4*H//6)  # DOCK_NA
)
