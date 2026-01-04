import sys; input=sys.stdin.readline

n, e = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(e):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

order = [int(x) for x in input().split()]
if len(order) != n:
    print("NO")
    exit()

visited = [False]*n
for i in range(n-1):
    v = order[i]
    u = order[i+1]
    visited[v] = True
    if visited[u] or (u not in g[v] and not all(visited[x] for x in g[v])):
        print("NO")
        break
else:
    print("YES")