import sys; input=sys.stdin.readline
import bisect
nt, ns, r = map(int, input().split())
trees = [tuple(map(int, input().split())) for _ in range(nt)]
trees.sort(key=lambda x: x[0])
tree_set = set(trees)
read = [tuple(map(int, input().split())) for _ in range(ns)]

m = {}
for x, y in trees:
    m.setdefault(x, []).append(y)
for x in m:
    m[x].sort()

def trees_in_range(x, y):
    xl = bisect.bisect_left(trees, x-r, key = lambda a: a[0])
    xr = bisect.bisect_right(trees, x+r, key = lambda a: a[0])

    count = 0
    prev = -2**30
    for i in range(xl, xr):
        x2 = trees[i][0]
        if x2 == prev: continue
        prev = x2
        diff = r-abs(x2-x)
        yl = bisect.bisect_left(m[x2], y-diff)
        yr = bisect.bisect_right(m[x2], y+diff)
        count += yr-yl
    return count

def rotate():
    for i in range(ns):
        x, y = read[i]
        read[i] = (-y, x)

res = None
for _ in range(4):
    dx, dy = read[0]
    for x, y in trees:
        x += dx
        y += dy
        if (x, y) in tree_set: continue
        if trees_in_range(x, y) != ns:
            continue
        for i in range(1, ns):
            dx2, dy2 = read[i]
            x2 = x - dx2
            y2 = y - dy2
            if (x2, y2) not in tree_set:
                break
        else:
            if res is not None:
                print("Ambiguous")
                exit()
            res = (x, y)

    rotate()


if res is None:
    print("Impossible")
else:
    print(*res)