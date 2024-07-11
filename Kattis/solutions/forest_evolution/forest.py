from functools import cmp_to_key
from sys import stdin

def cross(v1, v2):
    return v1[0]*v2[1] - v2[0]*v1[1]

def orient(anchor, v1, v2):
    foo = (v1[0]-anchor[0], v1[1]-anchor[1])
    bar = (v2[0]-anchor[0], v2[1]-anchor[1])
    return cross(foo, bar)

def intersect(line1, line2):
    (a,b), (c,d) = line1, line2
    oa = orient(c,d,a)
    ob = orient(c,d,b)
    oc = orient(a,b,c)
    od = orient(a,b,d)
    if oa*ob < 0 and oc*od < 0:
        x = (a[0]*ob-b[0]*oa)/(ob-oa)
        y = (a[1]*ob-b[1]*oa)/(ob-oa)
        return (x, y)
    return False


def compare(p1, p2, anchor):
    o = orient(anchor, p1, p2)
    if o >= 0:
        return 1
    else:
        return -1


def graham_scan(points: list):
    anchor = points[0]
    anchor_idx = 0
    n = len(points)
    for i in range(1, len(points)):
        y = points[i][1]
        if y < anchor[1] or (y == anchor[1] and points[i][0] < anchor[0]):
            anchor = points[i]
            anchor_idx = i

    points[n-1], points[anchor_idx] = points[anchor_idx], points[n-1]
    points.pop()
    points.sort(key=cmp_to_key(lambda p1, p2: compare(p1, p2, anchor)))

    hull = [anchor]
    for p in points:
        while len(hull) > 1 and orient(hull[-2], hull[-1], p) >= 0:
            hull.pop()
        hull.append(p)

    return hull

def shoelace(arr):
    left, right = 0, 0
    n = len(arr)
    for i in range(len(arr)):
        left += arr[i][0]*arr[(i+1)%n][1]
        right += arr[i][1]*arr[(i+1)%n][0]
    return abs(left-right)/2


def pn_poly(poly, p):
    x, y = p
    inside = False
    for i in range(len(poly)):
        j = (i+1) % len(poly)
        i_x, i_y = poly[i]
        j_x, j_y = poly[j]
        if (i_y > y) != (j_y > y) and x < (j_x-i_x) * (y-i_y) / (j_y-i_y) + i_x:
            inside = not inside
    return inside


def get_inside(poly1, poly2):
    new = []
    for i in range(len(poly1)):
        if pn_poly(poly2, poly1[i]):
            new.append(poly1[i])
    return new

def foo(poly1, poly2):
    new = get_inside(poly1, poly2)
    new.extend(get_inside(poly2, poly1))
    for i in range(len(poly1)):
        line = (poly1[i], poly1[(i+1)%len(poly1)])
        for j in range(len(poly2)):
            line2 = (poly2[j], poly2[(j+1)%len(poly2)])
            inter = intersect(line, line2)
            if inter:
                new.append(inter)
    return new

p, a = map(int, stdin.readline().split())
if p == 0 or a == 0:
    print(0)
    exit()
pines = [tuple(map(float, stdin.readline().split())) for _ in range(p)]
aspens = [tuple(map(float, stdin.readline().split())) for _ in range(a)]
pines  = graham_scan(pines)
aspens = graham_scan(aspens)
intersecting_poly = foo(pines, aspens)
if len(intersecting_poly) <= 2:
    print(0)
else:
    intersecting_poly = graham_scan(intersecting_poly)
    print(shoelace(intersecting_poly))