from sys import stdin, stdout
import math

"""
    Class for vector representation. NOT exhaustively tested (yet).
"""


class Vector:
    def __init__(self, *args):
        self.coords: list[float | int] = list(args)

    @property
    def x(self) -> float | int:
        return self.coords[0]

    @property
    def y(self) -> float | int:
        return self.coords[1]

    @property
    def z(self) -> float | int:
        return self.coords[2]

    @property
    def length(self) -> float:
        return math.sqrt(sum(a**2 for a in self.coords))

    def normalize(self, in_place=True):
        if not in_place:
            return self / self.length
        self /= self.length

    def dot(self, other) -> float | int:
        return sum(a * b for a, b in zip(self.coords, other.coords))

    def cross(self, other) -> float | int:
        return self.x * other.y - self.y * other.x

    def angle(self, other, radians=False) -> float:
        res = math.acos(
            self.normalize(in_place=False).dot(other.normalize(in_place=False))
        )
        if not radians:
            return math.degrees(res)
        return res

    def polar_angle(self, radians=False):
        ang = self.angle(Vector(1, 0))
        if self.y < 0:
            ang = 360 - ang
        if radians:
            return math.radians(ang)
        return ang

    def orient(self, v1, v2) -> float | int:
        v3 = v1 - self
        v4 = v2 - self
        return v3.cross(v4)

    def rotate(self, theta: float | int, radians=False):
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
        return math.dist(self.coords, other.coords)

    def squared_dist(self, other) -> float | int:
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2

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

    def __repr__(self):
        return str(self.coords)

    def copy(self):
        return self.__class__(*self.coords)


def graham_scan(points: list[Vector]):
    anchor = points[0]
    anchor_idx = 0
    for i in range(1, len(points)):
        p = points[i]
        if p.y < anchor.y or (p.y == anchor.y and p.x < anchor.x):
            anchor = p
            anchor_idx = i

    points[-1], points[anchor_idx] = points[anchor_idx], points[-1]
    points.pop()
    points.sort(key=lambda x: (x - anchor).polar_angle())

    hull = [anchor]
    for p in points:
        while len(hull) > 1 and hull[-2].orient(hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)

    return hull


def shoelace(arr: list[Vector]):
    left, right = 0, 0
    for i in range(len(arr) - 1):
        left += arr[i].x * arr[i + 1].y
        right += arr[i].y * arr[i + 1].x
    left += arr[-1].x * arr[0].y
    right += arr[-1].y * arr[0].x
    return abs(left - right) / 2


while (n := int(stdin.readline())) != 0:
    points = [Vector(*(map(int, stdin.readline().split()))) for _ in range(n)]
    hull = graham_scan(points)
    stdout.write(str(shoelace(hull)) + "\n")
