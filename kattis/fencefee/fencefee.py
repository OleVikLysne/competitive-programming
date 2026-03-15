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
    
    def __hash__(self):
        return hash((self.x, self.y))


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


# Convex hull
from functools import cmp_to_key


def graham_scan(points: list[Vec2]):
    def compare(anchor: Vec2, p1: Vec2, p2: Vec2):
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
        # if p.x < anchor.x or (p.x == anchor.x and p.y < anchor.y):
        if p.y < anchor.y or (p.y == anchor.y and p.x < anchor.x):
            anchor = p
            anchor_idx = i

    points[-1], points[anchor_idx] = points[anchor_idx], points[-1]
    points.pop()
    points.sort(key=cmp_to_key(lambda p1, p2: compare(anchor, p1, p2)))
    # points.sort(key=lambda x: (x - anchor).polar_angle())

    hull = [anchor]
    for p in points:
        while len(hull) > 1 and hull[-2].orient(hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)

    return hull


def graham_scan(points: list[Vec2]):
    points.sort()
    top = []
    for p in points:
        while len(top) >= 2 and top[-2].orient(top[-1], p) >= 0:
            top.pop()
        top.append(p)

    bottom = []
    for p in reversed(points):
        while len(bottom) >= 2 and bottom[-2].orient(bottom[-1], p) >= 0:
            bottom.pop()
        bottom.append(p)

    top += bottom[1:-1]
    return top


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


def point_in_polygon(poly: list[Vec2], p: Vec2):
    inside = False
    x, y = p.x, p.y
    for i in range(len(poly)):
        j = (i + 1) % len(poly)
        i_x, i_y = poly[i].x, poly[i].y
        j_x, j_y = poly[j].x, poly[j].y
        if (i_y > y) != (j_y > y) and x < (j_x - i_x) * (y - i_y) / (j_y - i_y) + i_x:
            inside = not inside
    return inside


def polygon_intersect(poly1: list[Vec2], poly2: list[Vec2]):
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


def rotating_calipers(convex_hull: list[Vec2]):
    n = len(convex_hull)
    max_distance = 0
    for i in range(n):
        j = (i + 1) % n
        k = (j + 1) % n
        while convex_hull[i].squared_dist(convex_hull[j]) < convex_hull[i].squared_dist(
            convex_hull[k]
        ):
            j = k
            k = (k + 1) % n
        max_distance = max(max_distance, convex_hull[i].squared_dist(convex_hull[j]))
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


import sys; input=sys.stdin.readline
g: dict[Vec2, list[Vec2]] = {}
for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    p1 = Vec2(x1, y1)
    p2 = Vec2(x2, y2)
    g.setdefault(p1, []).append(p2)
    g.setdefault(p2, []).append(p1)
for p in g:
    g[p].sort(key=lambda a: (a-p).polar_angle())

seen = set()
areas = []
tot = 0
for v in g:
    for u in g[v]:
        if (v, u) in seen:
            continue
        seen.add((v, u))
        cur = u
        prev = v
        poly = [v]
        while cur != v:
            poly.append(cur)
            i = (g[cur].index(prev)+1) % len(g[cur])
            prev, cur = cur, g[cur][i]
            seen.add((prev, cur))
        tup = tuple(sorted(poly))
        if tup not in seen:
            seen.add(tup)
            areas.append(shoelace(poly)**2)
tot = sum(areas)
if len(areas) > 1:
    tot -= max(areas)
print(tot)
