import pygame as pg

def get_quad(sheet, start, w, h):
    return sheet.subsurface(pg.Rect(start, (w, h)))

def get_quad_row(sheet, sheet_w, start_y, h, num_x):
    row = []
    for i in range(num_x):
        start = (i * sheet_w//num_x, start_y)
        row.append(get_quad(sheet, start,sheet_w//num_x, h))
    return row