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
    
    @property
    def is_zero_vec(self):
        return all(x == 0 for x in self.coords)

    def normalize(self, in_place=True):
        if self.is_zero_vec:
            return self
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

    def polar_angle(self, radians=False) -> float:
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


# Convex hull
from functools import cmp_to_key
def graham_scan(points: list[Vector]):
    def compare(anchor: Vector, p1: Vector, p2: Vector):
        o = anchor.orient(p1, p2)
        if o < 0:
            return 1
        else:
            return -1

    if len(points) <= 2:
        return [x for x in points]
    anchor = points[0]
    anchor_idx = 0
    for i in range(1, len(points)):
        p = points[i]
        #if p.x < anchor.x or (p.x == anchor.x and p.y < anchor.y):
        if p.y < anchor.y or (p.y == anchor.y and p.x < anchor.x):
            anchor = p
            anchor_idx = i

    points[-1], points[anchor_idx] = points[anchor_idx], points[-1]
    points.pop()
    points.sort(key=cmp_to_key(lambda p1, p2: compare(anchor, p1, p2)))
    #points.sort(key=lambda x: (x - anchor).polar_angle())

    hull = [anchor]
    for p in points:
        while len(hull) > 1 and hull[-2].orient(hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)

    return hull


# Area of polygon
def shoelace(arr: list[Vector]):
    left, right = 0, 0
    n = len(arr)
    for i in range(n):
        j = (i + 1) % n
        left += arr[i].x * arr[j].y
        right += arr[i].y * arr[j].x
    return abs(left - right) / 2



def point_in_polygon(poly: list[Vector], p: Vector):
    inside = False
    x, y = p.x, p.y
    for i in range(len(poly)):
        j = (i+1) % len(poly)
        #line1 = (Vector(10**9+7, 1), p)
        # line2 = (poly[i], poly[j])
        # if intersect(line1, line2) is not None:
        #     inside = not inside
        i_x, i_y = poly[i].x, poly[i].y
        j_x, j_y = poly[j].x, poly[j].y
        if (i_y > y) != (j_y > y) and x < (j_x-i_x) * (y-i_y) / (j_y-i_y) + i_x:
            inside = not inside
    return inside



def polygon_intersect(poly1: list[Vector], poly2: list[Vector]):
    def get_inside(poly1, poly2):
        for i in range(len(poly1)):
            if point_in_polygon(poly2, poly1[i]):
                yield poly1[i]

    # all points in p1 that are inside p2
    points = list(get_inside(poly1, poly2))
    # all points in p2 that are inside p1
    points.extend(get_inside(poly2, poly1))


    # include all the intersection points
    for i in range(len(poly1)):
        line1 = (poly1[i], poly1[(i + 1) % len(poly1)])

        for j in range(len(poly2)):
            line2 = (poly2[j], poly2[(j + 1) % len(poly2)])
            inter = intersect(line1, line2)
            if inter:
                points.append(inter)

    # and finally, compute the convex hull to get the polygon itself
    return graham_scan(points)


def rotating_calipers(convex_hull: list[Vector]):
    n = len(convex_hull)
    max_distance = 0
    for i in range(n):
        j = (i+1) % n
        k = (j+1) % n
        while convex_hull[i].squared_dist(convex_hull[j]) < convex_hull[i].squared_dist(convex_hull[k]):
            j = k
            k = (k+1) % n
        max_distance = max(max_distance, convex_hull[i].squared_dist(convex_hull[j]))
    return math.sqrt(max_distance)