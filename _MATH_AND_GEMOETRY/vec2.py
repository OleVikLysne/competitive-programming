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
        res = math.atan2(self.x, self.y)
        if radians:
            return res
        return math.degrees(res)

    def orient(self, v1, v2) -> Union[float, int]:
        return (v1.x-self.x) * (v2.y - self.y) - (v1.y - self.y) * (v2.x-self.x)
        # v3 = v1 - self
        # v4 = v2 - self
        # return v3.cross(v4)

    def right_of(self, other, origin=None) -> bool:
        if origin is None:
            return self.cross(other) > 0
        return origin.orient(self, other) > 0

    def left_of(self, other, origin=None) -> bool:
        if origin is None:
            return self.cross(other) < 0
        return origin.orient(self, other) < 0

    def inc_right_of(self, other, origin=None) -> bool:
        return not self.left_of(other, origin)

    def inc_left_of(self, other, origin=None) -> bool:
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

    def __hash__(self):
        return hash((self.x, self.y))

    def copy(self):
        return self.__class__(self.x, self.y)


# Various useful functions


# line intersect
def intersect(line1: tuple[Vec2], line2: tuple[Vec2]):
    (a, b), (c, d) = line1, line2
    oa = c.orient(d, a)
    ob = c.orient(d, b)
    oc = a.orient(b, c)
    od = a.orient(b, d)
    if oa * ob < 0 and oc * od < 0:
        x = (a.x * ob - b.x * oa) / (ob - oa)
        y = (a.y * ob - b.y * oa) / (ob - oa)
        return Vec2(x, y)
    return None


def graham_scan(points: list[Vec2]) -> list[Vec2]:
    """
    Returns the convex hull sorted counter-clockwise
    """
    points.sort()
    bottom = []
    for p in points:
        while len(bottom) >= 2 and p.inc_right_of(bottom[-1], bottom[-2]):
            bottom.pop()
        bottom.append(p)

    top = []
    for p in reversed(points):
        while len(top) >= 2 and p.inc_right_of(top[-1],top[-2]):
            top.pop()
        top.append(p)
    
    bottom.extend(top[1:-1])
    return bottom


# Area of polygon
def shoelace(poly: list[Vec2]):
    n = len(poly)
    left = right = 0
    for i in range(n):
        j = (i + 1) % n
        left += poly[i].x * poly[j].y
        right += poly[i].y * poly[j].x
    return abs(left - right) / 2

# Circumference of polygon
def poly_circumference(poly: list[Vec2]):
    n = len(poly)
    s = 0
    for i in range(len(poly)):
        j = (i + 1) % n
        s += poly[i].dist(poly[j])
    return s


def collinear(a: Vec2, b: Vec2, c: Vec2):
    return a.orient(b, c) == 0

def is_on(p: Vec2, p1: Vec2, p2: Vec2):
    if not collinear(p1, p2, p):
        return False
    if p1.x != p2.x:
        return p1.x <= p.x <= p2.x or p2.x <= p.x <= p1.x
    return p1.y <= p.y <= p2.y or p2.y <= p.y <= p1.y

def inside_polygon(poly: list[Vec2], p: Vec2) -> bool:
    inside = False
    x, y = p.x, p.y
    for i in range(len(poly)):
        j = (i + 1) % len(poly)
        if is_on(p, poly[i], poly[j]):
            return True
        i_x, i_y = poly[i].x, poly[i].y
        j_x, j_y = poly[j].x, poly[j].y
        if (i_y > y) != (j_y > y) and x < (j_x - i_x) * (y - i_y) / (j_y - i_y) + i_x:
            if inside is True:
                return False
            inside = not inside
    return inside


def polygon_intersect(poly1: list[Vec2], poly2: list[Vec2]):
    def get_inside(poly1, poly2):
        for i in range(len(poly1)):
            if inside_polygon(poly2, poly1[i]):
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


def rotating_calipers(hull: list[Vec2]):
    n = len(hull)
    max_distance = 0
    j = 1
    k = 2 % n
    for i in range(n):
        while hull[i].squared_dist(hull[j]) < hull[i].squared_dist(hull[k]):
            j = k
            k = (k + 1) % n
        max_distance = max(max_distance, hull[i].squared_dist(hull[j]))
    return math.sqrt(max_distance)


def circle_intersection_area(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if d >= r1 + r2:
        return 0.0

    if d <= abs(r1 - r2):
        return math.pi * min(r1, r2) ** 2

    a = (
        r1**2 * math.acos((d**2 + r1**2 - r2**2) / (2 * d * r1))
        + r2**2 * math.acos((d**2 + r2**2 - r1**2) / (2 * d * r2))
        - 0.5
        * math.sqrt((-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2))
    )
    return a


def inside_convex(hull: list[Vec2], p: Vec2) -> bool:
    """
    Returns true if p is inside the convex hull (or on the boundary). Assumes the hull is sorted counter-clockwise
    """
    n = len(hull)
    if n < 3:
        return False
    if p.right_of(hull[1], hull[0]):
        return False
    if p.left_of(hull[n-1], hull[0]):
        return False
    l, r = 0, n-1
    while l < r:
        mid = (l+r)//2
        if p.inc_left_of(hull[mid], hull[0]):
            l = mid + 1
        else:
            r = mid
    return p.inc_left_of(hull[r], hull[r-1])
