import heapq

n: int = ...
g: list[list[tuple[int, float | int]]] = ...

def dijkstra(source):
    dist = [float("inf")]*n
    dist[source] = 0
    prev = [-1]*n
    pq = [(0, source)]
    while pq:
        _, u = heapq.heappop(pq)
        for v, w in g[u]:
            if dist[v] > dist[u]+w:
                dist[v] = dist[u]+w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    return dist, prev


def get_path(dist, prev, start, target):
    v = target
    if dist[v] == float("inf"):
        return False
    path = [v]
    while v != start:
        v = prev[v]
        path.append(v)
    path.reverse()
    return path