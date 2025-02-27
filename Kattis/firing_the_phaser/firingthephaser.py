import sys; input=sys.stdin.readline

import math
from typing import Union

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    @property
    def is_zero_vec(self):
        return self.x == 0 and self.y == 0

    def normalize(self, in_place=True):
        if self.is_zero_vec:
            return self
        if not in_place:
            return self / self.length
        self /= self.length

    def dot(self, other) -> Union[float, int]:
        return self.x * other.x + self.y * other.y

    def cross(self, other) -> Union[float, int]:
        return self.x * other.y - self.y * other.x

    def angle(self, other, radians=False) -> float:
        res = math.acos(
            self.normalize(in_place=False).dot(other.normalize(in_place=False))
        )
        if radians:
            return res
        return math.degrees(res)

    def polar_angle(self, radians=False) -> float:
        ang = self.angle(Vec2(1, 0))
        if self.y < 0:
            ang = 360 - ang
        if radians:
            return math.radians(ang)
        return ang

    def orient(self, v1, v2) -> Union[float, int]:
        return (v1.x-self.x) * (v2.y - self.y) - (v1.y - self.y) * (v2.x-self.x)
        # v3 = v1 - self
        # v4 = v2 - self
        # return v3.cross(v4)

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

    def dist(self, other) -> float:
        return math.sqrt(self.squared_dist(other))

    def squared_dist(self, other) -> Union[float, int]:
        return (self.x - other.x)**2 + (self.y - other.y)**2

    def __mul__(self, other):
        if isinstance(other, Vec2):
            raise Exception("Not implemented")
        elif isinstance(other, (int, float)):
            return self.__class__(self.x * other, self.y * other)

    def __truediv__(self, other):
        if isinstance(other, Vec2):
            raise Exception("Not implemented")
        elif isinstance(other, (int, float)):
            return self.__class__(self.x / other, self.y / other)

    def __add__(self, other):
        if not isinstance(other, Vec2):
            raise Exception()
        return self.__class__(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vec2):
            raise Exception()
        return self.__class__(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return self.__class__(-self.x, -self.y)

    def __imul__(self, other):
        if isinstance(other, Vec2):
            raise Exception("Not implemented")
        self.x *= other
        self.y *= other
        return self

    def __itruediv__(self, other):
        if isinstance(other, Vec2):
            raise Exception("Not implemented")
        self.x /= other
        self.y /= other
        return self

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.x
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        if isinstance(other, Vec2):
            return self.x == other.x and self.y == other.y
        return False

    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        return self.x < other.x

    def __gt__(self, other):
        if self.x == other.x:
            return self.y > other.y
        return self.x > other.x

    def __repr__(self):
        return f"Vec2({self.x} {self.y})"

    def copy(self):
        return self.__class__(self.x, self.y)



# line intersect
def intersect(line1: tuple[Vec2], line2: tuple[Vec2]):
    (a, b), (c, d) = line1, line2
    oa = c.orient(d, a)
    ob = c.orient(d, b)
    oc = a.orient(b, c)
    od = a.orient(b, d)
    return oa * ob < 0 and oc * od < 0

def line_poly_intersect(line: tuple[Vec2], poly: list[Vec2]):
    for i in range(len(poly)):
        if intersect(line, (poly[i], poly[(i+1) % len(poly)])):
            return True
    return False

def sign(x):
    if x < 0:
        return -1.0
    elif x == 0:
        return 0.0
    return 1.0


DELTA = 1e-6
n, l = map(int, input().split())
polys_ext = []
polys = []
for _ in range(n):
    x1, y1, x2, y2 = map(float, input().split())
    polys.append([Vec2(x1, y1), Vec2(x1, y2), Vec2(x2, y2), Vec2(x2, y1)])
    x1 -= DELTA
    y1 -= DELTA
    x2 += DELTA
    y2 += DELTA
    polys_ext.append([Vec2(x1, y1), Vec2(x1, y2), Vec2(x2, y2), Vec2(x2, y1)])

best = 1
for i in range(n):
    for v in polys[i]:
        for j in range(n):
            if best == n:
                print(best)
                exit()
            if i == j: continue
            poly = polys[j]
            idx = min(range(4), key=lambda x: v.squared_dist(poly[x]))
            for v2 in (poly[(idx+1)%4], poly[(idx-1)%4]):
                x1, y1 = poly[idx].x, poly[idx].y
                x2, y2 = v2.x, v2.y
                dx, dy = sign(x2-x1), sign(y2-y1)
                while True:
                    start = Vec2(x1, y1)
                    if v.squared_dist(start) <= l**2:
                        dir = v - start
                        dir.normalize()
                        dir *= l
                        line = (start, start + dir)
                        c = 2
                        for k in range(n):
                            if i == k or j == k: continue
                            if line_poly_intersect(line, polys_ext[k]):
                                c += 1
                        best = max(best, c)
                    if x1 == x2 and y1 == y2:
                        break
                    x1 += dx
                    y1 += dy
print(best)