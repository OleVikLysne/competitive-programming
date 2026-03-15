import sys; input=sys.stdin.readline
from collections import deque
import heapq

INF = 2**60

n, m = map(int, input().split())
g = [[] for _ in range(n)]
gold = [0]*n
for i, x in enumerate(map(int, input().split()), 2):
    gold[i] = x
for _ in range(m):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)

def solve(mask):
    heap = [(0, 0)]
    dist = [INF]*n
    dist[0] = 0
    while heap:
        d, v = heapq.heappop(heap)
        if v == 1:
            break
        if dist[v] != d:
            continue
        for u in g[v]:
            w = gold[u] * (mask >> u & 1)
            if dist[u] > d + w:
                dist[u] = d + w
                heapq.heappush(heap, (dist[u], u))
    return dist[1]

dist = [INF]*n
dist[0] = 0
q = deque([(0, 1)])
masks = set()
while q:
    v, mask = q.popleft()
    if v == 1:
        masks.add(mask)
        continue

    for u in g[v]:
        if dist[u] < dist[v] + 1:
            continue
        dist[u] = dist[v] + 1
        q.append((u, mask | 1 << u))

res = 0
for mask in masks:
    tot = 0
    for i in range(n):
        if mask & 1 << i:
            tot += gold[i]
    res = max(res, tot - solve(mask))
print(res)
