import math
import pygame
import renpy.exports as renpy

class Vector2D:
    def __init__(self, x = None, y = None):
        if x is None and y is None:
            self.x = 0
            self.y = 0
        elif y is None:
            self.x = x[0]
            self.y = x[1]
        else:
            self.x = x
            self.y = y

    def __repr__(self):
        return "({:f}, {:f})".format(self.x, self.y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __lt__(self, other):
        return NotImplemented

    def __le__(self, other):
        return NotImplemented

    def __gt__(self, other):
        return NotImplemented

    def __ge__(self, other):
        return NotImplemented

    def __len__(self):
        return 2

    def __getitem__(self, key):
        if key == 0 or key == 'x':
            return self.x
        elif key == 1 or key == 'y':
            return self.y
        else:
            raise IndexError("Invalid index for 2D vector: "+str(key))

    def __setitem__(self, key, value):
        if key == 0 or key == 'x':
            self.x = value
        elif key == 1 or key == 'y':
            self.y = value
        else:
            raise IndexError("Invalid index for 2D vector: "+str(key))

    def __add__(self, other):
        try:
            return Vector2D(self.x + other[0], self.y + other[1])
        except (IndexError, TypeError):
            return Vector2D(self.x + other, self.y + other)

    def __sub__(self, other):
        try:
            return Vector2D(self.x - other[0], self.y - other[1])
        except (IndexError, TypeError):
            return Vector2D(self.x - other, self.y - other)

    def __mul__(self, other):
        try:
            return Vector2D(self.x * other[0], self.y * other[1])
        except (IndexError, TypeError):
            return Vector2D(self.x * other, self.y * other)

    def __truediv__(self, other):
        try:
            return Vector2D(self.x / other[0], self.y / other[1])
        except (IndexError, TypeError):
            return Vector2D(self.x / other, self.y / other)

    def __div__(self, other):
        return self.__truediv__(other)

    def __iadd__(self, other):
        try:
            self.x += other[0]
            self.y += other[1]
        except (IndexError, TypeError):
            self.x += other
            self.y += other

        return self

    def __isub__(self, other):
        try:
            self.x -= other[0]
            self.y -= other[1]
        except (IndexError, TypeError):
            self.x -= other
            self.y -= other

        return self

    def __imul__(self, other):
        try:
            self.x *= other[0]
            self.y *= other[1]
        except (IndexError, TypeError):
            self.x *= other
            self.y *= other

        return self

    def __itruediv__(self, other):
        try:
            self.x /= other[0]
            self.y /= other[1]
        except (IndexError, TypeError):
            self.x /= other
            self.y /= other

        return self

    def __idiv__(self, other):
        return self.__itruediv__(other)

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __pos__(self):
        return Vector2D(abs(self.x), abs(self.y))

    def magn(self):
        return math.sqrt((self.x**2) + (self.y**2))

    def __abs__(self):
        return self.magn()

    def normal(self):
        return Vector2D(self.y, -self.x)

    def unit(self):
        m = self.magn()

        return Vector2D(self.x / m, self.y / m)

    def unit_normal(self):
        m = self.magn()

        return Vector2D(self.y / m, -self.x / m)

    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y)

    def scalar_proj(self, other):
        return self.dot(other) / other.magn()

    def vector_proj(self, other):
        return other * (self.dot(other) / other.dot(other))

    def rotate(self, angle):
        return Vector2D(
            (self.x * math.cos(angle)) - (self.y * math.sin(angle)),
            (self.x * math.sin(angle)) + (self.y * math.cos(angle))
        )


class Polygon:
    def __init__(self, *args):
        self.points = []
        for arg in args:
            self.points.append(Vector2D(arg))

    def __len__(self):
        return len(self.points)

    def __iter__(self):
        return self.points.__iter__()

    def __repr__(self):
        return '[' + ', '.join([str(p) for p in self.points]) + ']'

    def copy(self):
        return Polygon(*tuple(self.points))

    def center(self):
        center = Vector2D(0, 0)

        for p in self.points:
            center += p

        center /= len(self.points)

        return center

    def translate(self, v):
        for idx, point in enumerate(self.points):
            self.points[idx] = point + v

    def rotate(self, angle, center=None):
        if center is None:
            center = self.center()

        self.translate(-center)

        for i, p in enumerate(self.points):
            self.points[i] = p.rotate(angle)

        self.translate(center)

    def sides(self):
        r = []
        for i, v in enumerate(self.points):
            if i != len(self.points)-1:
                r.append(self.points[i+1] - v)
            else:
                r.append(self.points[0] - v)

        return r

    def side_normals(self):
        r = []
        for i, v in enumerate(self.points):
            if i != len(self.points)-1:
                r.append((self.points[i+1] - v).unit_normal())
            else:
                r.append((self.points[0] - v).unit_normal())

        return r

    def project_on_axis(self, axis):
        proj_min = None
        proj_max = None

        for point in self.points:
            if proj_min is None:
                proj_min = point.dot(axis)
            else:
                proj_min = min(proj_min, point.dot(axis))

            if proj_max is None:
                proj_max = point.dot(axis)
            else:
                proj_max = max(proj_max, point.dot(axis))

        return (proj_min, proj_max)

def Rectangle(r, pos=None):
    if isinstance(r, pygame.Rect):
        if r.width == 0 or r.height == 0:
            raise ValueError("Cannot have a rectangle of zero width or height!")

        p = Polygon(r.topleft, r.topright, r.bottomright, r.bottomleft)
    else:
        if r[0] == 0 or r[1] == 0:
            raise ValueError("Cannot have a rectangle of zero width or height!")

        p = Polygon((-r[0]/2, r[1]/2), (r[0]/2, r[1]/2), (r[0]/2, -r[1]/2), (-r[0]/2, -r[1]/2))

        if pos is not None:
            p.translate(Vector2D(pos))

    return p


# Test to see if two Polygons intersect.
# If they don't, this returns None.
# Otherwise this returns the minimum translation vector needed to separate them.
def check_collision(polyA, polyB):
    #print("checking collisions between:")
    #print(str(polyA))
    #print(str(polyB))

    # Test all possible separating axes from A
    min_overlap_axis = None
    min_overlap = None

    for normal in polyA.side_normals():
        amin, amax = polyA.project_on_axis(normal)
        bmin, bmax = polyB.project_on_axis(normal)

        if amax < bmin or bmax < amin:
            return None  # no overlap on this axis -- we found a separating axis

        overlap1 = bmax - amin
        overlap2 = amax - bmin
        if abs(overlap1) < abs(overlap2):
            overlap = overlap1
        else:
            overlap = overlap2

        if min_overlap_axis is not None:
            if abs(overlap) < abs(min_overlap):
                min_overlap = overlap
                min_overlap_axis = normal
        else:
            min_overlap = overlap
            min_overlap_axis = normal

    # do the same for B
    for normal in polyB.side_normals():
        amin, amax = polyA.project_on_axis(normal)
        bmin, bmax = polyB.project_on_axis(normal)

        if amax < bmin or bmax < amin:
            return None

        overlap1 = bmax - amin
        overlap2 = amax - bmin
        if abs(overlap1) < abs(overlap2):
            overlap = overlap1
        else:
            overlap = overlap2

        if min_overlap_axis is not None:
            if abs(overlap) < abs(min_overlap):
                min_overlap = overlap
                min_overlap_axis = normal
        else:
            min_overlap = overlap
            min_overlap_axis = normal

    min_overlap = -abs(min_overlap)
    if min_overlap_axis.dot(polyB.center() - polyA.center()) < 0:
        # overlap axis points from polyB to polyA-- reverse overlap?
        min_overlap *= -1

    return min_overlap_axis * min_overlap
