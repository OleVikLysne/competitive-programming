from sys import stdin, setrecursionlimit
setrecursionlimit(1000000)

n, m = map(int, stdin.readline().split())
vals = [int(stdin.readline()) for _ in range(n)]
g = [[] for _ in range(n)]
for _ in range(m):
    i, j = map(int, stdin.readline().split())
    g[i].append(j)
    g[j].append(i)



def dfs(v, visited=None):
    if visited is None:
        visited = set()
    visited.add(v)
    for u in g[v]:
        if u in visited: continue
        dfs(u, visited)
    return visited
    
remaining = set(range(n))
while remaining:
    v = remaining.__iter__().__next__()
    visited = dfs(v)
    if sum(vals[x] for x in visited) != 0:
        print("IMPOSSIBLE")
        exit()
    for x in visited:
        remaining.remove(x)
        vals[x] = 0

if sum(vals) == 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")