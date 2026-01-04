import sys; input=sys.stdin.readline
import heapq

def dijkstra(stations, g):
    n = len(g)
    dist = [float("inf")]*n
    for source in stations:
        dist[source] = 0
    pq = [(0, source) for source in stations]
    while pq:
        _, v = heapq.heappop(pq)
        for u, w in g[v]:
            if dist[u] > dist[v]+w:
                dist[u] = dist[v]+w
                heapq.heappush(pq, (dist[u], u))
    return dist

def try_station(i, dist):
    dist = [x for x in dist]
    dist[i] = 0
    pq = [(0, i)]
    while pq:
        _, v = heapq.heappop(pq)
        for u, w in g[v]:
            if dist[u] > dist[v]+w:
                dist[u] = dist[v]+w
                heapq.heappush(pq, (dist[u], u))
    return max(dist)


t = int(input())
input()
for _ in range(t):
    f, n = map(int, input().split())
    stations = [int(input())-1 for _ in range(f)]
    g = [[] for _ in range(n)]
    for line in sys.stdin:
        if line == "\n": break
        a, b, w = map(int, line.split())
        a-=1
        b-=1
        g[a].append((b, w))
        g[b].append((a, w))
    dist = dijkstra(stations, g)
    m = float("inf")
    j = 0
    for i in range(n):
        x = try_station(i, dist)
        if x < m:
            m = x
            j = i
    print(j+1)
    print()
