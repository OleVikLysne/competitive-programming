import sys; input=sys.stdin.readline
import heapq
from collections import defaultdict

n = int(input())
g = [[] for _ in range(n)]
E = {}
for _ in range(n-1):
    u, v, w = map(int, input().split())
    if u < v:
        u, v = v, u
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)
    E[(u, v)] = w

depth = [-1]*n
depth[0] = 0
stack = [0]
pred = [-1]*n
W = [0]*n
while stack:
    v = stack.pop()
    for u in g[v]:
        if depth[u] == -1:
            depth[u] = depth[v] + 1
            pred[u] = v
            W[u] = E[(u, v) if u > v else (v, u)]
            stack.append(u)

D = max(depth)+1
depth_mat = [[] for _ in range(D)]
for v in range(n):
    depth_mat[depth[v]].append(v)

edge_weight = defaultdict(int)
for _ in range(2):
    heaps = [[(0, -1)]*2 for _ in range(n)]
    for d in range(D-1, 0, -1):
        for v in depth_mat[d]:
            u = pred[v]
            w = W[v]
            heapq.heappushpop(heaps[u], (heaps[v][1][0]+w, v))

    v = max(range(n), key = lambda v: (heaps[v][0][0] + heaps[v][1][0]))
    stack = [heaps[v][0][1], heaps[v][1][1]]
    while stack:
        v = stack.pop()
        if v == -1:
            continue
        u = pred[v]
        W[v] = -E[(u, v) if u > v else (v, u)]
        edge_weight[(u, v) if u > v else (v, u)] += 1
        stack.append(heaps[v][1][1])

res = 0
for u, v in E:
    res += E[(u, v)] * edge_weight.get((u, v), 2)
print(res)
