import sys

input = sys.stdin.readline
from math import sqrt, pi, acos


INF = float("inf")

def squared_dist(vec1, vec2):
    (x1, y1, _), (x2, y2, _) = vec1, vec2
    return (x1-x2)**2 + (y1-y2)**2


def brute_force(i, j, s):
    d = INF
    closest_pair = (None, None)
    for k in range(i, j-1):
        for l in range(k+1, j):
            vec1, vec2 = arr[k], arr[l]
            distance = squared_dist(vec1, vec2)
            if distance < d:
                if s and vec1[2] == vec2[2] and M != F:
                    continue
                d = distance
                closest_pair = (vec1, vec2)
    return (d, closest_pair)

def _closest_pair(i, j, arr_x, arr_y, s):
    if j-i <= 3:
        return brute_force(i, j, s)
    mid = (j+i)//2
    
    mid_x = arr_x[mid][0]
    l_arr = []
    r_arr = []
    for e in arr_y:
        if e[0] < mid_x:
            l_arr.append(e)
        else:
            r_arr.append(e)
    
    l = _closest_pair(i, mid, arr_x, l_arr, s)
    r = _closest_pair(mid, j, arr_x, r_arr, s)
    d, closest = min(l, r, key=lambda x: x[0])
    strip = []
    for e in arr_y:
        if abs(e[0]-mid_x)**2 < d:
            strip.append(e)

    for k in range(len(strip)-1):
        for l in range(k+1, min((k+8), len(strip))):
            if (strip[k][1] - strip[l][1])**2 >= d:
                break
            distance = squared_dist(strip[k], strip[l])
            if distance < d:
                if s and strip[k][2] == strip[l][2] and M != F:
                    continue
                d = distance
                closest = (strip[k], strip[l])
    return (d, closest)

def closest_pair(arr, s):
    arr.sort(key=lambda x: x[0])
    arr_y = arr[:]
    arr_y.sort(key=lambda x: x[1])
    return _closest_pair(0, len(arr), arr, arr_y, s)


def circle_intersection_area(x1, y1, r1, x2, y2, r2):
    d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if d >= r1 + r2:
        return 0.0
    
    if d <= abs(r1-r2):
        return pi * min(r1, r2)**2

    a = (
        r1**2 * acos((d**2 + r1**2 - r2**2) / (2 * d * r1))
        + r2**2 * acos((d**2 + r2**2 - r1**2) / (2 * d * r2))
        - 0.5 * sqrt((-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2))
    )
    return a


n, F, M = input().split()
n = int(n)
M = float(M)
F = float(F)
f_list = []
m_list = []
both = []
for _ in range(n):
    g, x, y = input().split()
    x = float(x)
    y = float(y)
    if g == "M":
        r = M
        m_list.append((x, y, r))
    else:
        r = F
        f_list.append((x, y, r))
    both.append((x, y, r))

res = 0
for arr, s in [(m_list, False), (f_list, False), (both, True)]:
    if len(arr) == 1: continue
    d, (c1, c2) = closest_pair(arr, s)
    if c1 is None: continue
    res = max(res, circle_intersection_area(*c1, *c2))
print(res)