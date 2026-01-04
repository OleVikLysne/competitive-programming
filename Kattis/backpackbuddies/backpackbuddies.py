import sys; input=sys.stdin.readline
import heapq

def dijkstra(source, target):
    dist = [float("inf")]*len(g)
    dist[source] = 0
    pq = [(0, source)]
    while pq:
        d, v = heapq.heappop(pq)
        if v == target:
            return d
        for u, w in g[v]:
            if dist[u] > dist[v]+w:
                dist[u] = dist[v]+w
                heapq.heappush(pq, (dist[u], u))


def day_dijkstra(source, target):
    dist = [float("inf")]*len(g)
    dist[source] = 0
    pq = [(0, source)]
    while pq:
        d, v = heapq.heappop(pq)
        if v == target:
            return d
        for u, w in g[v]:
            time_until_sleep = 12 - (dist[v] % 12)
            next_d = dist[v] + w
            if w > time_until_sleep:
                next_d += time_until_sleep
            if dist[u] > next_d:
                dist[u] = next_d
                heapq.heappush(pq, (dist[u], u))


n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    g[u].append((v, w))
    g[v].append((u, w))

knight = dijkstra(0, n-1)
day = day_dijkstra(0, n-1)
extra_nights = (-(-day//12)) - (-(-knight//12))
day += extra_nights*12
print(day-knight)