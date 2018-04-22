import renpy.exports as renpy
import pygame

def rect_overlap(r1, r2):
    if r1.centerx > r2.centerx:
        x_overlap = r2.right - r1.left
    else:
        x_overlap = r2.left - r1.right

    if r1.centery > r2.centery:
        y_overlap = r2.bottom - r1.top
    else:
        y_overlap = r2.top - r1.bottom

    return x_overlap, y_overlap
