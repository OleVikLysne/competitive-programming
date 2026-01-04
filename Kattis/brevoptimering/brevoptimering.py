import sys; input=sys.stdin.readline
from collections import deque

n = int(input())
g = [[] for _ in range(n)]
in_deg = [0]*n
roots = set(range(n))
M = [0]*n
U = [0]*n
for i in range(n):
    l = [int(x) for x in input().split()]
    M[i] = l[0]
    for k in range(2, len(l), 2):
        j, w = l[k]-1, l[k+1]/100
        g[i].append((j, w))
        in_deg[j] += 1
        roots.discard(j)

for v in roots:
    U[v] = M[v]

q = deque(roots)
while q:
    v = q.popleft()
    for u, w in g[v]:
        U[u] += w*U[v]
        in_deg[u] -= 1
        if in_deg[u] == 0:
            U[u] = min(M[u], U[u])
            q.append(u)

print(" ".join(str(i+1) for i in range(n) if U[i] == M[i]))