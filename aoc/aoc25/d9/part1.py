import sys

coords = [tuple(map(int, line.split(","))) for line in sys.stdin]
n = len(coords)
def bf():
    res = 0
    for i in range(n):
        x1, y1 = coords[i]
        for j in range(i+1, n):
            x2, y2 = coords[j]
            res = max(res, (abs(x1-x2) + 1) * (abs(y1-y2) + 1))
    return res

print(bf())