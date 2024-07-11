import heapq

n: int = ...
g: list[tuple[int, float | int]] = ...

def dijkstra(source):
    dist = [float("inf") for _ in range(n)]
    dist[source] = 0
    pq = [(0, source)]
    while pq:
        _, u = heapq.heappop(pq)
        for (v, w) in g[u]:
            if dist[v] > dist[u]+w:
                dist[v] = dist[u]+w
                heapq.heappush(pq, (dist[v], v))
    return dist