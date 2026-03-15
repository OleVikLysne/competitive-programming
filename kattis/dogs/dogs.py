import sys; input=sys.stdin.readline
from math import sqrt

def sqdist(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def offset(a, b, t):
    if a == b:
        return a
    x1, y1 = a
    x2, y2 = b
    x3 = x2-x1
    y3 = y2-y1
    length = sqrt(x3**2+y3**2)
    return x1 + (x3 / length) * t, y1 + (y3 / length) * t


n = int(input())
A = [tuple(map(int, input().split())) for _ in range(n)]
m = int(input())
B = [tuple(map(int, input().split())) for _ in range(m)]

i = j = 1
p1, p2 = A[0], B[0]
res = 2**60
while i < n and j < m:
    if sqdist(p1, A[i]) < sqdist(p2, B[j]):
        t = sqrt(sqdist(p1, A[i]))
        p1p = A[i]
        i += 1
        p2p = offset(p2, B[j], t)
    else:
        t = sqrt(sqdist(p2, B[j]))
        p2p = B[j]
        j += 1
        p1p = offset(p1, A[i], t)

    lo, hi = 0, t
    while hi-lo > 1e-5:
        mi = (lo+hi)/2
        if sqdist(offset(p1, p1p, mi), offset(p2, p2p, mi)) < sqdist(offset(p1, p1p, mi+1e-8), offset(p2, p2p, mi+1e-8)):
            hi = mi
        else:
            lo = mi
    res = min(
        res,
        sqdist(offset(p1, p1p, lo), offset(p2, p2p, lo))
    )
    p1, p2 = p1p, p2p

print(sqrt(res))
