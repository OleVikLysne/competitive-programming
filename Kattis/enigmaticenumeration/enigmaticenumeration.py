import sys; input=sys.stdin.readline
from collections import deque

INF = 2**60

n, m = map(int, input().split())
g = [[] for _ in range(n)]
edges = []
for _ in range(m):
    u, v = (int(x)-1 for x in input().split())
    edges.append((u, v))
    g[u].append(v)
    g[v].append(u)

dist_matrix = [[INF]*n for _ in range(n)]
paths_matrix = [[0]*n for _ in range(n)]
def shortest_cycle(s):
    dist = dist_matrix[s]
    paths = paths_matrix[s]
    dist[s] = 0
    q = deque([s])
    shortest = INF
    while q:
        v = q.popleft()
        for u in g[v]:
            if dist[u] < dist[v]: continue
            if dist[u] != INF:
                shortest = min(shortest, dist[v] + dist[u] + 1)
                if dist[u] == dist[v] + 1:
                    paths[u] += 1
            else:
                dist[u] = dist[v] + 1
                q.append(u)
    return shortest

k = 2**60

for v in range(n):
    k = min(k, shortest_cycle(v))

count = 0
target = k // 2
if k % 2 == 1:
    for v in range(n):
        dist = dist_matrix[v]
        for u, w in edges:
            if dist[u] == dist[w] == target:
                count += 1
else:
    for v in range(n):
        dist = dist_matrix[v]
        paths = paths_matrix[v]
        for u in range(n):
            if dist[u] == target:
                count += (paths[u]*(paths[u]+1))//2
print(count//k)
