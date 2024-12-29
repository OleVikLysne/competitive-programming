import sys; input=sys.stdin.readline
sys.setrecursionlimit(2**30)

n = int(input())
g = [[] for _ in range(n)]
deg = [0]*n
res = [-1]*n
for _ in range(n):
    a, b = (int(x)-1 for x in input().split())
    if a in g[b]:
        g[b].remove(a)
        g[a].remove(b)
        res[a] = b
        res[b] = a
    else:
        g[a].append(b)
        g[b].append(a)
        deg[a] += 1
        deg[b] += 1
    
def dfs(v):
    if res[v] != -1:
        return True
    for u in g[v]:
        if res[u] != v:
            res[v] = u
            if dfs(u):
                return True
            res[v] = -1
    return False

for i in range(n):
    if deg[i] == 1:
        dfs(i)

for i in range(n):
    dfs(i)
    print(i+1, res[i]+1)