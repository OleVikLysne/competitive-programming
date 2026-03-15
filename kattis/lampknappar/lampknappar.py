import sys; input=sys.stdin.readline
from collections import deque
import heapq

n = int(input())
g = [[] for _ in range(n)]
rev_g = [[] for _ in range(n)]
for i in range(n):
    for j in map(int, input().split()[1:]):
        g[i].append(j-1)
        rev_g[j-1].append(i)

INF = float("inf")
dist = [[INF]*n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0
    q = deque([(i, 0)])
    while q:
        v, d = q.popleft()
        for u in g[v]:
            if dist[i][u] == INF:
                dist[i][u] = d+1
                q.append((u, d+1))

if dist[0][n-1] == INF or dist[n-1][0] == INF:
    print("nej")
    exit()

pq = [(0, 0, 0)]
prev = [[INF]*n for _ in range(n)]
def add_to_pq(next_c, x, y):
    if prev[x][y] <= next_c:
        return
    prev[x][y] = next_c
    heapq.heappush(pq, (next_c, x, y))


prev[0][0] = 0
while pq:
    c, v, u = heapq.heappop(pq)
    if prev[v][u] != c:
        continue
    if v == n-1 and u == n-1:
        print(c)
        break

    if v != u:
        next_c = c + dist[v][u]-1
        add_to_pq(next_c, u, v)

    for w in g[v]:
        next_c = c + (1 if w != u else 0)
        add_to_pq(next_c, w, u)

    for w in rev_g[u]:
        next_c = c + (1 if v != w else 0)
        add_to_pq(next_c, v, w)
