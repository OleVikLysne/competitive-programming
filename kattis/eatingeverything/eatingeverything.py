import sys; input=sys.stdin.readline
sys.setrecursionlimit(2**30)

n, m = map(int, input().split())
g = [[] for _ in range(n)]
sat = [int(x) for x in input().split()]
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)

mem = [-1]*n
def dfs(v):
    if mem[v] != -1:
        return mem[v]
    mem[v] = 0
    for u in g[v]:
        mem[v] = max(mem[v], dfs(u))
    mem[v] = max(mem[v], (mem[v] / 2) + sat[v])
    return mem[v]

print(dfs(0))