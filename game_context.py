res = (660, 360)

WIDTH, HEIGHT = res[0], res[1]

NA, W, S, E, N = 0, 1, 2, 4, 8

NE = N + E
NW = N + W
SE = S + E
SW = S + W

from pygame import Rect

cb = {
    NA : Rect(WIDTH//6, HEIGHT//6, 4*WIDTH//6, 4*HEIGHT//6),
    W  : Rect(       0, HEIGHT//6, 5*WIDTH//6, 4*HEIGHT//6),
    S  : Rect(WIDTH//6, HEIGHT//6, 4*WIDTH//6, 5*HEIGHT//6),
    E  : Rect(WIDTH//6, HEIGHT//6, 5*WIDTH//6, 4*HEIGHT//6),
    N  : Rect(WIDTH//6,         0, 4*WIDTH//6, 5*HEIGHT//6),
    NE : Rect(WIDTH//6,         0, 5*WIDTH//6, 5*HEIGHT//6),
    SE : Rect(WIDTH//6, HEIGHT//6, 5*WIDTH//6, 5*HEIGHT//6),
    SW : Rect(       0, HEIGHT//6, 5*WIDTH//6, 5*HEIGHT//6),
    NW : Rect(       0,         0, 5*WIDTH//6, 5*HEIGHT//6),
}