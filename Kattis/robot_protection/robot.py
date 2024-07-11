from functools import cmp_to_key
from sys import stdin, stdout

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


def shoelace(arr):
    left, right = 0, 0
    n = len(arr)
    for i in range(len(arr)):
        left += arr[i][0]*arr[(i+1)%n][1]
        right += arr[i][1]*arr[(i+1)%n][0]
    return abs(left-right)/2


while (n:=int(stdin.readline())) != 0:
    points = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
    hull = graham_scan(points)
    stdout.write(str(shoelace(hull))+"\n")