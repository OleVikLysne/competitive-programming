import sys; input=sys.stdin.readline
from collections import deque

INF = float("inf")

n, m, k = map(int, input().split())
shops = (int(x)-1 for x in input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    i, j = (int(x)-1 for x in input().split())
    g[i].append(j)
    g[j].append(i)


distance = [INF]*n
source_map = [set() for _ in range(n)]
q = deque((x, 0, x) for x in shops)
while q:
    v, dist, source = q.popleft()
    dist += 1
    for u in g[v]:
        if u == source:
            continue
        if distance[u] + dist < distance[source] and (len(source_map[u]) > 1 or (distance[u] != INF and source not in source_map[u])):
            distance[source] = min(distance[source], distance[u] + dist)
        
        if distance[u] >= dist:
            q.append((u, dist, source))
            distance[u] = dist
            source_map[u].add(source)


print(*(x if x != INF else -1 for x in distance))