from sys import stdin, stdout

def cross(v1, v2):
    return v1[0]*v2[1] - v1[1]*v2[0]

def orient(v1, v2, v3):
    foo = (v2[0]-v1[0], v2[1]-v1[1])
    bar = (v3[0]-v1[0], v3[1]-v1[1])
    return cross(foo, bar)

def intersect(line1, line2):
    (a, b), (c, d) = line1, line2
    if b == d: return True
    oa = orient(c, d, a)
    ob = orient(c, d, b)
    oc = orient(a, b, c)
    od = orient(a, b, d)
    if oa*ob < 0 and oc*od < 0:
        return True
    return False

def binary_search(arr, val):
    n = len(arr)
    lower, upper, mid = 0, n, n>>1
    while lower!=mid:
        if arr[mid] == val: return True
        if arr[mid] < val:
            lower = mid
        else:
            upper = mid
        mid = (lower+upper)>>1
    return arr[mid] == val


while True:
    n = int(stdin.readline())
    if n == 0: break
    lines = []
    for _ in range(n):
        x1, y1, x2, y2 = [float(x) for x in stdin.readline().split()]
        lines.append( ((x1, y1), (x2, y2)) )

    G = [set() for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if intersect(lines[i], lines[j]):
                G[i].add(j)
                G[j].add(i)

    triangles = 0
    for i in range(2, n):
        for j in G[i]:
            if j>i: break
            for k in G[j]:
                if k > j: break
                if i in G[k]:
                    triangles += 1

    stdout.write(str(triangles)+"\n")