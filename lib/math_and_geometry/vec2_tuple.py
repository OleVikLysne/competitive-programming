import math

def length(v):
    return math.sqrt(squared_length(v))

def squared_length(v):
    return v[0]**2 + v[1]**2

def is_zero_vec(v):
    return v[0] == 0 and v[1] == 0

def normalize(v):
    if is_zero_vec(v):
        return v
    l = length(v)
    return (v[0] / l, v[1] / l)

def dot(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

def cross(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]

def angle(v1, v2, radians=False):
    res = math.acos(dot(normalize(v1), normalize(v2)))
    if radians:
        return res
    return math.degrees(res)

def polar_angle(v, radians=False):
    res = math.atan2(v[1], v[0])
    if radians:
        return res
    return math.degrees(res)

def orient(v, v1, v2):
    return (v1[0] - v[0]) * (v2[1] - v[1]) - (v1[1] - v[1]) * (v2[0] - v[0])

def right_of(v, other, origin=None):
    if origin is None:
        return cross(v, other) > 0
    return orient(origin, v, other) > 0

def left_of(v, other, origin=None):
    if origin is None:
        return cross(v, other) < 0
    return orient(origin, v, other) < 0

def inc_right_of(v, other, origin=None):
    return not left_of(v, other, origin)

def inc_left_of(v, other, origin=None):
    return not right_of(v, other, origin)

def rotate(v, theta, radians=False):
    """
    theta is assumed to be a value between 0-360 with radians=False.
    Otherwise, theta is assumed to be between 0 and 2*pi.
    Rotates counter-clockwise.
    """
    if not radians:
        if theta == 90:
            return (-v[1], v[0])
        if theta == 180:
            return (-v[0], -v[1])
        if theta == 270:
            return (v[1], -v[0])
        theta = math.radians(theta)

    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    return (
        v[0] * cos_theta - v[1] * sin_theta,
        v[0] * sin_theta + v[1] * cos_theta,
    )

def dist(v1, v2):
    return math.sqrt(squared_dist(v1, v2))

def squared_dist(v1, v2):
    return (v1[0] - v2[0])**2 + (v1[1] - v2[1])**2

def mul(v, other):
    return (v[0] * other, v[1] * other)

def truediv(v, other):
    return (v[0] / other, v[1] / other)

def add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def sub(v1, v2):
    return (v1[0] - v2[0], v1[1] - v2[1])

def neg(v):
    return (-v[0], -v[1])

def eq(v1, v2):
    return v1[0] == v2[0] and v1[1] == v2[1]

def lt(v1, v2):
    if v1[0] == v2[0]:
        return v1[1] < v2[1]
    return v1[0] < v2[0]

def gt(v1, v2):
    if v1[0] == v2[0]:
        return v1[1] > v2[1]
    return v1[0] > v2[0]

def repr(v):
    return f"({v[0]} {v[1]})"

def copy(v):
    return v


# Various useful functions


# line intersect
def intersect(line1, line2):
    (a, b), (c, d) = line1, line2
    oa = orient(c, d, a)
    ob = orient(c, d, b)
    oc = orient(a, b, c)
    od = orient(a, b, d)
    if oa * ob < 0 and oc * od < 0:
        x = (a[0] * ob - b[0] * oa) / (ob - oa)
        y = (a[1] * ob - b[1] * oa) / (ob - oa)
        return (x, y)
    return None


def graham_scan(points):
    """
    Returns the convex hull sorted counter-clockwise
    """
    n = len(points)
    if n <= 1:
        return points[:]

    points.sort()
    hull = []
    for p in points:
        while len(hull) > 1 and inc_right_of(p, hull[-1], hull[-2]):
            hull.pop()
        hull.append(p)

    k = len(hull)
    hull.append(points[-2])
    for i in range(n-3, -1, -1):
        p = points[i]
        while len(hull) > k and inc_right_of(p, hull[-1], hull[-2]):
            hull.pop()
        hull.append(p)
    hull.pop()

    return hull


# Area of polygon
def shoelace(poly):
    n = len(poly)
    left = right = 0
    for i in range(n):
        j = (i + 1) % n
        left += poly[i][0] * poly[j][1]
        right += poly[i][1] * poly[j][0]
    return abs(left - right) / 2

# Circumference of polygon
def poly_circumference(poly):
    n = len(poly)
    s = 0
    for i in range(n):
        j = (i + 1) % n
        s += dist(poly[i], poly[j])
    return s

def collinear(a, b, c):
    return orient(a, b, c) == 0

def is_on(p, p1, p2):
    if not collinear(p1, p2, p):
        return False
    if p1[0] != p2[0]:
        return min(p1[0], p2[0]) <= p[0] <= max(p1[0], p2[0])
    return min(p1[1], p2[1]) <= p[1] <= max(p1[1], p2[1])

def inside_polygon(poly, p):
    n = len(poly)
    inside = False
    x, y = p[0], p[1]
    for i in range(n):
        j = (i + 1) % n
        if is_on(p, poly[i], poly[j]):
            return True
        ix, iy = poly[i][0], poly[i][1]
        jx, jy = poly[j][0], poly[j][1]
        if (iy > y) != (jy > y) and x < (jx - ix) * (y - iy) / (jy - iy) + ix:
            inside = not inside
    return inside

def strictly_inside_polygon(poly, p):
    n = len(poly)
    for i in range(n):
        j = (i + 1) % n
        if collinear(p, poly[i], poly[j]):
            return False
    return inside_polygon(poly, p)

def polygon_intersect(poly1, poly2):
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

def rotating_calipers(hull):
    n = len(hull)
    max_distance = 0
    j = 1
    k = 2 % n
    for i in range(n):
        while squared_dist(hull[i], hull[j]) < squared_dist(hull[i], hull[k]):
            j = k
            k = (k + 1) % n
        max_distance = max(max_distance, squared_dist(hull[i], hull[j]))
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

def inside_convex(hull, p):
    """
    Returns true if p is inside the convex hull (or on the boundary). Assumes the hull is sorted counter-clockwise
    """
    n = len(hull)
    if n < 3:
        return False
    if right_of(p, hull[1], hull[0]):
        return False
    if left_of(p, hull[n-1], hull[0]):
        return False
    l, r = 0, n-1
    while l < r:
        mid = (l+r)//2
        if inc_left_of(p, hull[mid], hull[0]):
            l = mid + 1
        else:
            r = mid
    return inc_left_of(p, hull[r], hull[r-1])