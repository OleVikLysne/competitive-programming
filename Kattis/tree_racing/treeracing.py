import sys
sys.setrecursionlimit(2**30)
import io, os
Ø = io.BytesIO(os.read(0, os.fstat(0).st_size))
input = lambda: next(Ø)

n, m, k = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)


R = [-1]*(n+1)
speed = [0]*(n+1)
for i in range(m):
    p, t = map(int, input().split())
    speed[p] = t
    R[p] = i

e = int(input())

CP = [False]*(n+1)
for _ in range(int(input())):
    CP[int(input())] = True

df = [[] for _ in range(n+1)]
depth = [-1]*(n+1)
def solve(v, p, s):
    depth[v] = depth[p] + 1
    sn = v if CP[v] else s
    if speed[v]:
        df[sn].append(v)

    for u in g[v]:
        if u == p:
            continue
        solve(u, v, sn)

    if CP[v]:
        df[v].sort(key = lambda u: ((depth[u]-depth[v]) * speed[u], speed[u]))
        df[s].extend(df[v][:k])

solve(e, e, e)
res = ["-1"]*m
for v in df[e]:
    res[R[v]] = str(depth[v] * speed[v])

print("\n".join(res))