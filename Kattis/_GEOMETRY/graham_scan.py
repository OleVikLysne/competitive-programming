
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


from functools import cmp_to_key
# this isnt even "actually" a graham scan, but it achieves the desired result in O(nlogn)
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