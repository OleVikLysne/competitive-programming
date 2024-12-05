import heapq

g: list[list[tuple[int, float | int]]] = ...


# dijkstra to all nodes
def dijkstra(source):
    n = len(g)
    dist = [float("inf")]*n
    dist[source] = 0
    prev = [-1]*n
    pq = [(0, source)]
    while pq:
        _, v = heapq.heappop(pq)
        for u, w in g[v]:
            if dist[u] > dist[v]+w:
                dist[u] = dist[v]+w
                prev[u] = v
                heapq.heappush(pq, (dist[u], u))
    return dist, prev


# dijkstra to specific target node
def dijkstra(source, target):
    n = len(g)
    dist = [float("inf")]*n
    dist[source] = 0
    prev = [-1]*n
    pq = [(0, source)]
    while pq:
        d, v = heapq.heappop(pq)
        if v == target:
            return d, prev
        for u, w in g[v]:
            if dist[u] > dist[v]+w:
                dist[u] = dist[v]+w
                prev[u] = v
                heapq.heappush(pq, (dist[u], u))
    return False


# fails if the target wasn't reached
def get_path(prev, start, target):
    v = target
    path = [v]
    while v != start:
        v = prev[v]
        path.append(v)
    path.reverse()
    return path