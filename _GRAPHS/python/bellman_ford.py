g: list[list[tuple[int, float | int]]] = ...

def bellman_ford(s, g, n):
    dist = [float("inf")]*n
    pred = [-1]*n
    dist[s] = 0
    for _ in range(n-1):
        for parent in range(n):
            for child, w in g[parent]:
                if dist[child] > dist[parent] + w:
                    dist[child] = dist[parent] + w
                    pred[child] = parent

    for parent in range(n):
        for child, w in g[parent]:
            if dist[child] > dist[parent] + w:
                return True # negative cycle
    return dist, pred