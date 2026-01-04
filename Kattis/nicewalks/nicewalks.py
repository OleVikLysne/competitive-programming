import sys; input=sys.stdin.readline
from collections import defaultdict

sys.setrecursionlimit(2**30)

def anc(v: int, k: int):
    i = k.bit_length()-1
    while k:
        if k & 1 << i:
            v = anc_matrix[i][v]
        k &= (1 << i) - 1
        i -= 1
    return v


def lca(u: int, v: int):
    if depth[v] > depth[u]:
        u, v = v, u
    u = anc(u, depth[u]-depth[v])
    if u == v:
        return v

    log_d = (depth[v]-1).bit_length()
    for i in range(log_d-1, -1, -1):
        if anc_matrix[i][u] != anc_matrix[i][v]:
            u = anc_matrix[i][u]
            v = anc_matrix[i][v]

    return anc_matrix[0][v]


def build_anc_matrix(g: list[list[int]], root=0):
    n = len(g)
    log_n = (n-1).bit_length()
    depth = [-1]*n
    depth[root] = 0
    anc_matrix = [[-1]*n for _ in range(log_n)]

    stack = [root]
    while stack:
        v = stack.pop()
        for u in g[v]:
            if depth[u] == -1:
                depth[u] = depth[v] + 1
                anc_matrix[0][u] = v
                stack.append(u)

    for i in range(1, log_n):
        for j in range(n):
            anc_matrix[i][j] = anc_matrix[i-1][anc_matrix[i-1][j]]

    return depth, anc_matrix


n, p, q = map(int, input().split())
edges = [tuple(int(x)-1 for x in input().split()) for _ in range(n-1)]
m = {"I": 0, "P": 1, "C": 2}

g = [[] for _ in range(n)]

for u, v in edges:
    g[u].append(v)
    g[v].append(u)

venues = defaultdict(list)
for _ in range(p):
    t, e = input().split()
    e = int(e)-1
    t = m[t]
    u, v = edges[e]
    venues[(u, v)].append(t)
    venues[(v, u)].append(t)

prev = [[-1]*3 for _ in range(n)]
def mark(v, l, par):
    for i, d in enumerate(l):
        prev[v][i] = d
    
    for u in g[v]:
        if u == par: continue
        new_l = l[:]
        for t in venues[(v, u)]:
            new_l[t] = depth[v]
        mark(u, new_l, v)
        
depth, anc_matrix = build_anc_matrix(g)
mark(0, [-1]*3, -1)

res = ["Y"]*q
for j in range(q):
    u, v = (int(x)-1 for x in input().split())
    w = lca(u, v)
    for i in range(3):
        if prev[u][i] < depth[w] and prev[v][i] < depth[w]:
            res[j] = "N"
            break
print("\n".join(res))