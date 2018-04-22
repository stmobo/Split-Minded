import renpy.exports as renpy
import math
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

def magn(v):
    return math.sqrt(v[0]**2 + v[1]**2)

def dist(v1, v2):
    return math.sqrt((v2[0] - v1[0])**2 + (v2[1] - v1[1])**2)

def unit_vec(v):
    m = math.sqrt(v[0]**2 + v[1]**2)

    if m < 0.0001:
        m = 0.0001

    return [v[0] / m, v[1] / m]

# vector with given magnitude in certain direction
def magn_dir_vec(magn, v1, v2=None):
    if v2 is None:
        uv = unit_vec(v1)
    else:
        uv = unit_vec((v1[0] - v2[0], v1[1] - v2[1]))

    return [uv[0]*magn, uv[1]*magn]
