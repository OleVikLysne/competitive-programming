import sys; input=sys.stdin.readline
sys.setrecursionlimit(2**30)

def out():
    print("impossible")
    exit()
n, m = map(int, input().split())
g = [set() for _ in range(n)]
lounges = set()
remove = set()
for _ in range(m):
    i, j, l = map(int, input().split())
    i -= 1
    j -= 1
    if l == 2:
        if i in remove or j in remove:
            out()
        lounges.add(i)
        lounges.add(j)
    elif l == 0:
        if i in lounges or j in lounges:
            out()
        remove.add(i)
        remove.add(j)
    else:
        if i in lounges and j in lounges:
            out()
        if i in remove and j in remove:
            out()
        g[i].add(j)
        g[j].add(i)

b = True
while b:
    b = False
    for i in range(n):
        for j in g[i].copy():
            if j in lounges:
                if i in lounges:
                    out()
                g[i].remove(j)
                remove.add(i)
                b = True
            if j in remove:
                if i in remove:
                    out()
                g[i].remove(j)
                lounges.add(i)
                b = True


def bipartite(g):
    def _bipartite(g, v, colours, counts, c=0):
        if colours[v] != -1:
            if colours[v] != c:
                out()
            return
        colours[v] = c
        counts[c] += 1
        c = (c+1) % 2
        for u in g[v]:
            _bipartite(g, u, colours, counts, c)
    
    colours = [-1]*len(g)
    s = 0
    for i in range(len(g)):
        if colours[i] == -1:
            counts = [0, 0]
            _bipartite(g, i, colours, counts)
            s += min(counts)
    return s

print(len(lounges) + bipartite(g))
