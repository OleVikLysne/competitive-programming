def cross(v1, v2):
    return v1[0]*v2[1] - v1[1]*v2[0]

def orient(anchor, v1, v2):
    foo = (v1[0]-anchor[0], v1[1]-anchor[1])
    bar = (v2[0]-anchor[0], v2[1]-anchor[1])
    return cross(foo, bar)

def intersect(line1, line2):
    (a,b), (c,d) = line1, line2
    # if b == d: return True
    oa = orient(c,d,a)
    ob = orient(c,d,b)
    oc = orient(a,b,c)
    od = orient(a,b,d)
    if oa*ob < 0 and oc*od < 0:
        x = (a[0]*ob-b[0]*oa)/(ob-oa)
        y = (a[1]*ob-b[1]*oa)/(ob-oa)
        return (x, y)
    return False