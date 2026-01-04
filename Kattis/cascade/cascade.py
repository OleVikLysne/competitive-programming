import sys; input=sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

deg = [len(x) for x in g]
visited = [False]*(n+1)
def solve(v, x):
    if visited[v]:
        return 0
    if x < 1e-5:
        return x
    visited[v] = True
    res = x
    for u in g[v]:
        res += solve(u, x / deg[u])
    visited[v] = False
    return res


v = int(input())
print(round(solve(v, 1), 1))
