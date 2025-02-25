import math
from typing import Union

"""
    Class for vector representation. NOT exhaustively tested (yet).
"""


class Vector:
    def __init__(self, *args):
        self.coords: list[Union[float, int]] = list(args)

    @property
    def x(self) -> Union[float, int]:
        return self.coords[0]

    @property
    def y(self) -> Union[float, int]:
        return self.coords[1]

    @property
    def z(self) -> Union[float, int]:
        return self.coords[2]

    @property
    def length(self) -> float:
        return math.sqrt(sum(a**2 for a in self.coords))

    @property
    def is_zero_vec(self):
        return all(x == 0 for x in self.coords)

    def normalize(self, in_place=True):
        if self.is_zero_vec:
            return self
        if not in_place:
            return self / self.length
        self /= self.length

    def dot(self, other) -> Union[float, int]:
        return sum(a * b for a, b in zip(self.coords, other.coords))

    def cross(self, other) -> Union[float, int]:
        return self.x * other.y - self.y * other.x

    def angle(self, other, radians=False) -> float:
        res = math.acos(
            self.normalize(in_place=False).dot(other.normalize(in_place=False))
        )
        if not radians:
            return math.degrees(res)
        return res

    def polar_angle(self, radians=False) -> float:
        ang = self.angle(Vector(1, 0))
        if self.y < 0:
            ang = 360 - ang
        if radians:
            return math.radians(ang)
        return ang

    def orient(self, v1, v2) -> Union[float, int]:
        v3 = v1 - self
        v4 = v2 - self
        return v3.cross(v4)

    def rotate(self, theta: Union[float, int], radians=False):
        """
        theta is assumed to be a value between 0-360 with radians=False.
        Otherwise, theta is assumed to be between 0 and 2*pi.
        Rotates counter-clockwise.
        """
        if len(self.coords) != 2:
            raise Exception("Rotate is currently only implemented for 2D")
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
        return sum((a - b) ** 2 for a, b in zip(self.coords, other.coords))

    def __mul__(self, other):
        if isinstance(other, Vector):
            raise Exception("Not implemented")
        elif isinstance(other, (int, float)):
            return self.__class__(*(a * other for a in self.coords))

    def __truediv__(self, other):
        if isinstance(other, Vector):
            raise Exception("Not implemented")
        elif isinstance(other, (int, float)):
            return self.__class__(*(a / other for a in self.coords))

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise Exception()
        return self.__class__(*(a + b for a, b in zip(self.coords, other.coords)))

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise Exception()
        return self.__class__(*(a - b for a, b in zip(self.coords, other.coords)))

    def __neg__(self):
        return self.__class__(*(-a for a in self.coords))

    def __imul__(self, other):
        if isinstance(other, Vector):
            raise Exception("Not implemented")
        for i in range(len(self.coords)):
            self.coords[i] *= other
        return self

    def __itruediv__(self, other):
        if isinstance(other, Vector):
            raise Exception("Not implemented")
        for i in range(len(self.coords)):
            self.coords[i] /= other
        return self

    def __iadd__(self, other):
        for i in range(len(self.coords)):
            self.coords[i] += other.coords[i]
        return self

    def __isub__(self, other):
        for i in range(len(self.coords)):
            self.coords[i] -= other.coords[i]
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __iter__(self):
        return iter(self.coords)

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.coords == other.coords
        return False

    def __lt__(self, other):
        return self.coords < other.coords

    def __gt__(self, other):
        return self.coords > other.coords

    def __repr__(self):
        return str(self.coords)

    def copy(self):
        return self.__class__(*self.coords)



# Various useful functions


# line intersect
def intersect(line1: tuple[Vector], line2: tuple[Vector]):
    (a, b), (c, d) = line1, line2
    oa = c.orient(d, a)
    ob = c.orient(d, b)
    oc = a.orient(b, c)
    od = a.orient(b, d)
    if oa * ob < 0 and oc * od < 0:
        x = (a.x * ob - b.x * oa) / (ob - oa)
        y = (a.y * ob - b.y * oa) / (ob - oa)
        return Vector(x, y)
    return None

# Area of polygon
def shoelace(arr: list[Vector]):
    left, right = 0, 0
    n = len(arr)
    for i in range(n):
        j = (i + 1) % n
        left += arr[i].x * arr[j].y
        right += arr[i].y * arr[j].x
    return abs(left - right) / 2



import sys; input=sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    points = [Vector(*map(int, input().split())) for _ in range(n)]
    d = points[1] - points[0]
    mid = points[0] + d / 2
    d.normalize()
    d = d.rotate(90)
    d *= 10**6

    inter_lines = [(mid, mid + d.rotate(45)), (mid, mid + d.rotate(-45))]
    poly = [mid]
    inc = False
    for i in range(1, n):
        p1, p2 = points[i], points[(i+1)%n]
        while inter_lines:
            diff = p2 - p1
            diff *= 1e-8
            line = (p1, p2+diff)
            if (inter_point := intersect(line, inter_lines[-1])) is not None:
                inter_lines.pop()
                poly.append(inter_point)
                inc = not inc
            else:
                break
        if inc:
            poly.append(p2)
    sys.stdout.write(f"{shoelace(poly) / shoelace(points)} ")
