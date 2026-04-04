def cross(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]

def orient(v, v1, v2):
    return (v1[0] - v[0]) * (v2[1] - v[1]) - (v1[1] - v[1]) * (v2[0] - v[0])

def inc_right_of(v, other, origin):
    return orient(origin, v, other) <= 0

def graham_scan(points):
    """
    Returns the convex hull sorted counter-clockwise
    """
    points.sort()
    bottom = []
    for p in points:
        while len(bottom) >= 2 and inc_right_of(p, bottom[-1], bottom[-2]):
            bottom.pop()
        bottom.append(p)

    top = []
    for p in reversed(points):
        while len(top) >= 2 and inc_right_of(p, top[-1], top[-2]):
            top.pop()
        top.append(p)
    
    bottom.extend(top[1:-1])
    return bottom

import sys; input=sys.stdin.readline
points = [tuple(map(int, input().split())) for _ in range(int(input()))]
hull = graham_scan(points)
n = len(hull)
res = 0
for i in range(n-2):
    k = i + 2
    x, y = hull[i]
    for j in range(i+1, n-1):
        a, b = hull[j]
        q, w = hull[k]
        a1 = abs(x * (b - w) + a * (w - y) + q * (y - b))
        while k + 1 < n:
            q, w = hull[k+1]
            a2 = abs(x * (b - w) + a * (w - y) + q * (y - b))
            if a2 <= a1:
                break
            a1 = a2
            k += 1
        res = max(res, a1)
print(res/2)