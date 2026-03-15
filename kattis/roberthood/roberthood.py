from functools import cmp_to_key
from sys import stdin
from math import sqrt

def cross(v1, v2):
    return v1[0]*v2[1] - v2[0]*v1[1]

def orient(anchor, v1, v2):
    foo = (v1[0]-anchor[0], v1[1]-anchor[1])
    bar = (v2[0]-anchor[0], v2[1]-anchor[1])
    return cross(foo, bar)


    

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


def squared_dist(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2


def rotating_calipers(convex_hull):
    n = len(convex_hull)
    max_distance = 0
    for i in range(n):
        j = (i+1) % n
        k = (j+1) % n
        while squared_dist(convex_hull[i], convex_hull[j]) < squared_dist(convex_hull[i], convex_hull[k]):
            j = k
            k = (k+1) % n
            
        max_distance = max(max_distance, squared_dist(convex_hull[i], convex_hull[j]))
    
    return sqrt(max_distance)



c = int(stdin.readline())
points = [tuple(map(int, stdin.readline().split())) for _ in range(c)]
hull = graham_scan(points)
print(rotating_calipers(hull))