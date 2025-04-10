from __future__ import annotations
import math
from typing import Union

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def length(self) -> float:
        return math.sqrt(self.squared_length)
    
    @property
    def squared_length(self) -> Union[float, int]:
        return self.x**2 + self.y**2

    @property
    def is_zero_vec(self):
        return self.x == 0 and self.y == 0

    def normalize(self, in_place=True):
        if self.is_zero_vec:
            return self
        if not in_place:
            return self / self.length
        self /= self.length

    def dot(self, other: Vec2) -> Union[float, int]:
        return self.x * other.x + self.y * other.y

    def cross(self, other: Vec2) -> Union[float, int]:
        return self.x * other.y - self.y * other.x

    def angle(self, other: Vec2, radians=False) -> float:
        res = math.acos(
            self.normalize(in_place=False).dot(other.normalize(in_place=False))
        )
        if radians:
            return res
        return math.degrees(res)

    def polar_angle(self, radians=False) -> float:
        res = math.atan2(self.x, self.y)
        if radians:
            return res
        return math.degrees(res)

    def orient(self, v1: Vec2, v2: Vec2) -> Union[float, int]:
        return (v1.x-self.x) * (v2.y - self.y) - (v1.y - self.y) * (v2.x-self.x)
        # v3 = v1 - self
        # v4 = v2 - self
        # return v3.cross(v4)

    def right_of(self, other: Vec2, origin=None) -> bool:
        if origin is None:
            return self.cross(other) > 0
        return origin.orient(self, other) > 0

    def left_of(self, other: Vec2, origin=None) -> bool:
        if origin is None:
            return self.cross(other) < 0
        return origin.orient(self, other) < 0

    def inc_right_of(self, other: Vec2, origin=None) -> bool:
        return not self.left_of(other, origin)

    def inc_left_of(self, other: Vec2, origin=None) -> bool:
        return not self.right_of(other, origin)

    def rotate(self, theta: Union[float, int], radians=False):
        """
        theta is assumed to be a value between 0-360 with radians=False.
        Otherwise, theta is assumed to be between 0 and 2*pi.
        Rotates counter-clockwise.
        """
        if radians is False:
            if theta == 90:
                return self.__class__(-self.y, self.x)
            if theta == 180:
                return -self
            if theta == 270:
                return self.__class__(self.y, -self.x)
            theta = math.radians(theta)

        cos_theta = math.cos(theta)
        sin_theta = math.sin(theta)
        return self.__class__(
            self.x * cos_theta - self.y * sin_theta,
            self.x * sin_theta + self.y * cos_theta,
        )

    def dist(self, other: Vec2) -> float:
        return math.sqrt(self.squared_dist(other))

    def squared_dist(self, other: Vec2) -> Union[float, int]:
        return (self.x - other.x)**2 + (self.y - other.y)**2

    def __mul__(self, other: Union[float, int]):
        return self.__class__(self.x * other, self.y * other)

    def __truediv__(self, other: Union[float, int]):
        return self.__class__(self.x / other, self.y / other)

    def __add__(self, other: Vec2):
        return self.__class__(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vec2):
        return self.__class__(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return self.__class__(-self.x, -self.y)

    def __imul__(self, other: Union[float, int]):
        self.x *= other
        self.y *= other
        return self

    def __itruediv__(self, other: Union[float, int]):
        self.x /= other
        self.y /= other
        return self

    def __iadd__(self, other: Vec2):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other: Vec2):
        self.x -= other.x
        self.y -= other.x
        return self

    def __radd__(self, other: Vec2):
        return self.__add__(other)

    def __rsub__(self, other: Vec2):
        return self.__sub__(other)

    def __rmul__(self, other: Union[float, int]):
        return self.__mul__(other)

    def __eq__(self, other):
        if isinstance(other, Vec2):
            return self.x == other.x and self.y == other.y
        return False

    def __lt__(self, other: Vec2):
        if self.x == other.x:
            return self.y < other.y
        return self.x < other.x

    def __gt__(self, other: Vec2):
        if self.x == other.x:
            return self.y > other.y
        return self.x > other.x

    def __repr__(self):
        return f"Vec2({self.x} {self.y})"

    def __hash__(self):
        return hash((self.x, self.y))

    def copy(self):
        return self.__class__(self.x, self.y)

def collinear(a: Vec2, b: Vec2, c: Vec2):
    return a.orient(b, c) == 0

def is_on(p: Vec2, p1: Vec2, p2: Vec2):
    if not collinear(p1, p2, p):
        return False
    if p1.x != p2.x:
        return min(p1.x, p2.x) <= p.x <= max(p1.x, p2.x)
    return min(p1.y, p2.y) <= p.y <= max(p1.y, p2.y)

def inside_polygon(poly: list[Vec2], p: Vec2) -> bool:
    n = len(poly)
    inside = False
    x, y = p.x, p.y
    for i in range(n):
        j = (i + 1) % n
        if is_on(p, poly[i], poly[j]):
            return True
        ix, iy = poly[i].x, poly[i].y
        jx, jy = poly[j].x, poly[j].y
        if (iy > y) != (jy > y) and x < (jx - ix) * (y - iy) / (jy - iy) + ix:
            inside = not inside
    return inside

def strictly_inside_polygon(poly: list[Vec2], p: Vec2) -> bool:
    n = len(poly)
    for i in range(n):
        j = (i + 1) % n
        if collinear(p, poly[i], poly[j]):
            return False
    return inside_polygon(poly, p)


def solve(poly: list[Vec2], p: Vec2):
    if collinear(*poly):
        return collinear(poly[0], poly[1], p) and min(a.squared_length for a in poly) < p.squared_length < max(a.squared_length for a in poly)
    return strictly_inside_polygon(poly, p)


import sys; input = sys.stdin.readline
while True:
    x1, y1, z1 = map(int, input().split())
    if x1 == y1 == z1 == 0: break
    x2, y2, z2 = map(int, input().split())
    x3, y3, z3 = map(int, input().split())
    x4, y4, z4 = map(int, input().split())
    poly = [Vec2(x1, y1), Vec2(x2, y2), Vec2(x3, y3)]
    p = Vec2(x4, y4)
    print("YES" if solve(poly, p) else "NO")
    input()
