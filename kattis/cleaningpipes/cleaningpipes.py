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

w, p = [int(x) for x in stdin.readline().split()]
W = [tuple(int(x) for x in stdin.readline().split()) for _ in range(w)]
lines = []
to_visit = set()
G = [[] for _ in range(p)]
for j in range(p):
    i, x2, y2 = [int(x) for x in stdin.readline().split()]
    line =  (W[i-1], (x2,y2))
    for k, l in enumerate(lines):
        if intersect(l, line):
            G[j].append(k)
            G[k].append(j)
            to_visit.add(j)
            to_visit.add(k)
    lines.append(line)


colors = {a : -1 for a in to_visit}
def bipartite(s, color=0):
    if colors[s] != -1:
        if colors[s] == color:
            return True
        return False
    
    to_visit.remove(s)
    colors[s] = color
    next_color = (color + 1) % 2
    for child in G[s]:
        if not bipartite(child, next_color):
            return False
    return True

while len(to_visit) > 0:
    s = to_visit.__iter__().__next__()
    if not bipartite(s):
        stdout.write("impossible")
        exit()
stdout.write("possible")